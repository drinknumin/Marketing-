#!/usr/bin/env python3
"""
prepare_amazon_dsp.py
=====================

Turn a Shopify customer CSV export into a hashed, Amazon-DSP-ready audience file.

Amazon DSP / Amazon Marketing Cloud (AMC) require that all personally
identifiable information (email, phone, name, address) be NORMALIZED and then
SHA-256 hashed *before* upload. This script does exactly that, entirely on your
own machine — raw PII is read from your local export, hashed, and only the
hashed output is written out.

It is dependency-free (Python 3.8+ standard library only). Nothing is uploaded
or sent anywhere by this script.

--------------------------------------------------------------------------------
QUICK START
--------------------------------------------------------------------------------
1. In Shopify Admin, go to Customers -> Export -> "All customers" (or a filtered
   segment) -> CSV for Excel/Numbers/etc. Save the file, e.g. customers.csv
2. Run:

       python3 prepare_amazon_dsp.py customers.csv -o amazon_dsp_audience.csv

3. Upload amazon_dsp_audience.csv to Amazon DSP / AMC.

By default only customers who are SUBSCRIBED to email marketing are included
(permission-based data, as Amazon's policy requires). See --consent below.

--------------------------------------------------------------------------------
NORMALIZATION RULES (applied before hashing)
--------------------------------------------------------------------------------
All hashes are SHA-256, emitted as a lowercase hex string.

  EMAIL        trim whitespace; lowercase.
  PHONE        keep digits only; drop a leading intl prefix / trunk zero; if the
               number has no country code, prepend the default one (US = 1);
               result is E.164 digits with no "+".
  FIRST_NAME   trim; lowercase; drop everything that is not a letter.
  LAST_NAME    trim; lowercase; drop everything that is not a letter.
  ADDRESS      trim; lowercase; drop punctuation; standardize street suffixes
               (STREET->st) and directionals (NORTH->n); join tokens with no
               spaces (mirrors Amazon's official AddressHash SDK). Street line
               only — never city/state/zip/country.
  CITY         trim; lowercase; drop non-alphanumeric characters.
  STATE        trim; lowercase; drop non-alphanumeric characters (US = 2-letter).
  ZIP          trim; lowercase; drop non-alphanumeric; US zips truncated to 5.
  COUNTRY_CODE ISO 3166-1 alpha-2, lowercased.

References:
  - Amazon Ads "Format audience file for hashing"
    https://advertising.amazon.com/help/GCCXMZYCK4RXWS6C
  - Amazon Ads hashed-records API docs
    https://advertising.amazon.com/API/docs/en-us/data-provider/hashed-records
  - Official address SDK (Apache-2.0)
    https://github.com/amzn/amazon-ads-advertiser-audience-normalization-sdk-py
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import re
import sys
import unicodedata
from pathlib import Path

# --------------------------------------------------------------------------- #
# Output schema (Amazon DSP / AMC identifier columns)
# --------------------------------------------------------------------------- #
# user_id is your own stable record reference (NOT hashed).
# Everything else here is PII and is SHA-256 hashed.
HASHED_COLUMNS = [
    "EMAIL",
    "PHONE",
    "FIRST_NAME",
    "LAST_NAME",
    "ADDRESS",
    "CITY",
    "STATE",
    "ZIP",
    "COUNTRY_CODE",
]

# --------------------------------------------------------------------------- #
# Shopify header aliases -> our canonical field name.
# Keys are matched case-insensitively with all non-alphanumerics stripped, so
# "First Name", "first_name" and "FirstName" all collapse to "firstname".
# --------------------------------------------------------------------------- #
FIELD_ALIASES = {
    "user_id": ["customerid", "id", "customer_id"],
    "EMAIL": ["email", "customeremail"],
    "PHONE": ["phone", "defaultaddressphone", "phonenumber"],
    "FIRST_NAME": ["firstname"],
    "LAST_NAME": ["lastname"],
    "ADDRESS": ["address1", "defaultaddressaddress1", "address", "street"],
    "CITY": ["city", "defaultaddresscity"],
    "STATE": ["provincecode", "defaultaddressprovincecode", "province", "state", "region"],
    "ZIP": ["zip", "defaultaddresszip", "postalcode", "postcode", "zipcode"],
    "COUNTRY_CODE": ["countrycode", "defaultaddresscountrycode", "country"],
}

# Columns that tell us whether a customer consented to email marketing.
CONSENT_ALIASES = [
    "acceptsemailmarketing",
    "emailmarketingconsent",
    "emailmarketingstate",
    "marketingstate",
]
SUBSCRIBED_VALUES = {"yes", "true", "1", "subscribed"}

# --------------------------------------------------------------------------- #
# Address normalization tables (subset of Amazon's official AddressHash SDK,
# covering common US suffixes / directionals). Street line only.
# --------------------------------------------------------------------------- #
_DIRECTIONALS = {
    "east": "e", "west": "w", "north": "n", "south": "s",
    "northeast": "ne", "northwest": "nw", "southeast": "se", "southwest": "sw",
    "so": "s", "no": "n",
}
_SUFFIXES = {
    "avenue": "ave", "boulevard": "blvd", "circle": "cir", "court": "ct",
    "center": "ctr", "centre": "ctr", "drive": "dr", "freeway": "fwy",
    "highway": "hwy", "lane": "ln", "parkway": "pkwy", "place": "pl",
    "plaza": "plz", "road": "rd", "square": "sq", "street": "st",
    "terrace": "ter", "trail": "trl", "way": "way", "alley": "aly",
    "crossing": "xing", "expressway": "expy", "junction": "jct",
    "loop": "loop", "point": "pt", "route": "rte", "turnpike": "tpke",
}
_NUMBER_INDICATORS = {"number": "", "num": "", "no": "", "#": ""}


# --------------------------------------------------------------------------- #
# Normalizers
# --------------------------------------------------------------------------- #
def _clean(value):
    return (value or "").strip()


def normalize_email(value):
    v = _clean(value).lower()
    if "@" not in v or "." not in v.split("@")[-1]:
        return ""
    return v


def normalize_phone(value, default_country_code="1"):
    digits = re.sub(r"\D", "", _clean(value))
    if not digits:
        return ""
    # Drop international dialing prefix "00" and any single leading trunk zero.
    if digits.startswith("00"):
        digits = digits[2:]
    elif digits.startswith("0"):
        digits = digits.lstrip("0")
    if not digits:
        return ""
    cc = re.sub(r"\D", "", default_country_code)
    # If it already carries the country code, leave it; otherwise prepend it.
    # Heuristic tuned for NANP (US/CA): a bare 10-digit number gets the CC.
    if cc == "1":
        if len(digits) == 10:
            digits = cc + digits
    else:
        if not digits.startswith(cc):
            digits = cc + digits
    if len(digits) < 8 or len(digits) > 15:  # E.164 sanity bounds
        return ""
    return digits


def _letters_only(value):
    v = unicodedata.normalize("NFKC", _clean(value)).lower()
    return "".join(ch for ch in v if ch.isalpha())


def normalize_first_name(value):
    return _letters_only(value)


def normalize_last_name(value):
    return _letters_only(value)


def _alnum_only(value):
    v = unicodedata.normalize("NFKC", _clean(value)).lower()
    return "".join(ch for ch in v if ch.isalnum())


def normalize_city(value):
    return _alnum_only(value)


def normalize_state(value):
    return _alnum_only(value)


def normalize_zip(value, country_code=""):
    v = _alnum_only(value)
    # US postal codes are the 5-digit base (drop ZIP+4).
    if country_code.lower() in ("", "us", "usa") and v[:5].isdigit():
        return v[:5]
    return v


def normalize_country(value):
    v = _clean(value).lower()
    aliases = {
        "united states": "us", "usa": "us", "us": "us", "u.s.": "us",
        "united states of america": "us",
        "canada": "ca", "ca": "ca",
        "united kingdom": "gb", "uk": "gb", "gb": "gb", "great britain": "gb",
    }
    if v in aliases:
        return aliases[v]
    return v[:2] if len(v) >= 2 else v


def normalize_address(value):
    v = _clean(value).lower()
    if not v:
        return ""
    # Replace punctuation with spaces, collapse to tokens.
    v = re.sub(r"[^\w\s]", " ", v)
    tokens = v.split()
    out = []
    for tok in tokens:
        if tok in _NUMBER_INDICATORS:
            mapped = _NUMBER_INDICATORS[tok]
            if mapped:
                out.append(mapped)
            continue
        tok = _DIRECTIONALS.get(tok, tok)
        tok = _SUFFIXES.get(tok, tok)
        out.append(tok)
    # Amazon's SDK joins normalized address tokens with no separator.
    return "".join(out)


NORMALIZERS = {
    "EMAIL": lambda v, row: normalize_email(v),
    "PHONE": lambda v, row: normalize_phone(v, row["_default_cc"]),
    "FIRST_NAME": lambda v, row: normalize_first_name(v),
    "LAST_NAME": lambda v, row: normalize_last_name(v),
    "ADDRESS": lambda v, row: normalize_address(v),
    "CITY": lambda v, row: normalize_city(v),
    "STATE": lambda v, row: normalize_state(v),
    "ZIP": lambda v, row: normalize_zip(v, row.get("_country_raw", "")),
    "COUNTRY_CODE": lambda v, row: normalize_country(v),
}


def sha256_hex(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest() if value else ""


# --------------------------------------------------------------------------- #
# Header mapping
# --------------------------------------------------------------------------- #
def _canon(header):
    return re.sub(r"[^a-z0-9]", "", (header or "").lower())


def build_header_map(fieldnames):
    """Map each canonical output field to the actual column name in the file."""
    canon_to_actual = {}
    for name in fieldnames:
        canon_to_actual.setdefault(_canon(name), name)

    mapping = {}
    for field, aliases in FIELD_ALIASES.items():
        for alias in aliases:
            if alias in canon_to_actual:
                mapping[field] = canon_to_actual[alias]
                break

    consent_col = None
    for alias in CONSENT_ALIASES:
        if alias in canon_to_actual:
            consent_col = canon_to_actual[alias]
            break
    return mapping, consent_col


def is_subscribed(raw_value):
    return _clean(raw_value).lower() in SUBSCRIBED_VALUES


# --------------------------------------------------------------------------- #
# Core processing
# --------------------------------------------------------------------------- #
def process(rows, header_map, consent_col, args):
    stats = {
        "read": 0, "written": 0,
        "dropped_no_consent": 0, "dropped_no_email": 0,
        "dropped_no_identifier": 0,
    }
    active_cols = [c for c in HASHED_COLUMNS if c in header_map]
    seen_users = set()
    out_rows = []
    fallback_id = 0

    for raw in rows:
        stats["read"] += 1

        if consent_col is not None and args.consent == "subscribed":
            if not is_subscribed(raw.get(consent_col)):
                stats["dropped_no_consent"] += 1
                continue

        ctx = {"_default_cc": args.default_country_code}
        if "COUNTRY_CODE" in header_map:
            ctx["_country_raw"] = _clean(raw.get(header_map["COUNTRY_CODE"]))

        normalized = {}
        for field in active_cols:
            src_val = raw.get(header_map[field], "")
            normalized[field] = NORMALIZERS[field](src_val, ctx)

        if args.require_email and not normalized.get("EMAIL"):
            stats["dropped_no_email"] += 1
            continue
        if not any(normalized.get(f) for f in active_cols):
            stats["dropped_no_identifier"] += 1
            continue

        # Stable per-record user_id (not hashed). Prefer Shopify Customer ID,
        # else derive a deterministic id from the hashed email.
        raw_user_id = _clean(raw.get(header_map["user_id"])).lstrip("'") if "user_id" in header_map else ""
        if raw_user_id:
            user_id = raw_user_id
        elif normalized.get("EMAIL"):
            user_id = sha256_hex(normalized["EMAIL"])[:16]
        else:
            fallback_id += 1
            user_id = f"row{fallback_id}"

        if user_id in seen_users:
            continue  # de-duplicate
        seen_users.add(user_id)

        out_row = {"user_id": user_id}
        for field in active_cols:
            out_row[field] = sha256_hex(normalized[field])
        out_rows.append(out_row)
        stats["written"] += 1

    return out_rows, ["user_id"] + active_cols, stats


def open_out(path, use_gzip):
    if use_gzip:
        return gzip.open(path, "wt", encoding="utf-8", newline="")
    return open(path, "w", encoding="utf-8", newline="")


def write_output(out_rows, columns, args):
    out_path = Path(args.output)
    max_rows = args.max_rows_per_file
    chunks = [out_rows]
    if max_rows and len(out_rows) > max_rows:
        chunks = [out_rows[i:i + max_rows] for i in range(0, len(out_rows), max_rows)]

    written_paths = []
    for idx, chunk in enumerate(chunks):
        if len(chunks) > 1:
            target = out_path.with_name(f"{out_path.stem}_part{idx + 1:03d}{out_path.suffix}")
        else:
            target = out_path
        if args.gzip:
            target = target.with_suffix(target.suffix + ".gz")
        with open_out(target, args.gzip) as fh:
            writer = csv.DictWriter(fh, fieldnames=columns, delimiter=args.delimiter)
            writer.writeheader()
            writer.writerows(chunk)
        written_paths.append(target)
    return written_paths


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Convert a Shopify customer CSV export into a hashed Amazon DSP audience file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("input", help="Path to the Shopify customer CSV export.")
    p.add_argument("-o", "--output", default="amazon_dsp_audience.csv",
                   help="Output CSV path (default: amazon_dsp_audience.csv).")
    p.add_argument("--consent", choices=["subscribed", "all"], default="subscribed",
                   help="'subscribed' (default) keeps only email-marketing subscribers; "
                        "'all' keeps everyone (use only with a lawful basis for all rows).")
    p.add_argument("--default-country-code", default="1",
                   help="Country calling code to prepend to phone numbers lacking one (default: 1 = US/CA).")
    p.add_argument("--require-email", dest="require_email", action="store_true", default=True,
                   help="Drop rows without a valid email (default: on).")
    p.add_argument("--no-require-email", dest="require_email", action="store_false",
                   help="Keep rows that have some other identifier even without an email.")
    p.add_argument("--delimiter", default=",",
                   help="Output delimiter (default: comma). Amazon accepts any single-char delimiter.")
    p.add_argument("--gzip", action="store_true", help="Gzip the output (Amazon supports GZIP).")
    p.add_argument("--max-rows-per-file", type=int, default=0,
                   help="Split output into files of at most N rows each (0 = single file).")
    p.add_argument("--input-delimiter", default=",",
                   help="Delimiter of the input file (default: comma).")
    args = p.parse_args(argv)

    in_path = Path(args.input)
    if not in_path.exists():
        p.error(f"input file not found: {in_path}")

    with open(in_path, "r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh, delimiter=args.input_delimiter)
        if not reader.fieldnames:
            p.error("input file has no header row.")
        header_map, consent_col = build_header_map(reader.fieldnames)
        if "EMAIL" not in header_map and args.require_email:
            p.error(
                "Could not find an email column in the input. Columns seen: "
                + ", ".join(reader.fieldnames)
            )
        rows = list(reader)

    out_rows, columns, stats = process(rows, header_map, consent_col, args)
    written_paths = write_output(out_rows, columns, args)

    # ---- Report ----------------------------------------------------------- #
    print("Amazon DSP audience file — preparation summary", file=sys.stderr)
    print("-" * 52, file=sys.stderr)
    print(f"  Identifier columns included : {', '.join(c for c in columns if c != 'user_id')}", file=sys.stderr)
    if consent_col is None and args.consent == "subscribed":
        print("  Consent column              : NONE FOUND — no consent filter applied!", file=sys.stderr)
    else:
        print(f"  Consent filter              : {args.consent}", file=sys.stderr)
    print(f"  Rows read                   : {stats['read']:,}", file=sys.stderr)
    print(f"  Dropped (not subscribed)    : {stats['dropped_no_consent']:,}", file=sys.stderr)
    print(f"  Dropped (no valid email)    : {stats['dropped_no_email']:,}", file=sys.stderr)
    print(f"  Dropped (no identifier)     : {stats['dropped_no_identifier']:,}", file=sys.stderr)
    print(f"  Unique users written        : {stats['written']:,}", file=sys.stderr)
    for pth in written_paths:
        print(f"  -> {pth}", file=sys.stderr)

    # Amazon audience-size guidance.
    if stats["written"] < 500:
        print("\n  ⚠  Fewer than 500 matched users — below Amazon's lookalike minimum.", file=sys.stderr)
    elif stats["written"] < 2000:
        print("\n  ⚠  Between 500 and 2,000 users — enough for LOOKALIKE audiences only "
              "(exact audiences need 2,000+ matched users).", file=sys.stderr)
    else:
        print("\n  ✓  Above Amazon's 2,000-user minimum for exact audiences "
              "(note: this is pre-match; actual matched count will be lower).", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
