# Amazon DSP — First-Party Data (Email List) Prep

Turn a **Shopify customer export** into a **hashed, Amazon-DSP-ready audience file**
that satisfies Amazon's first-party data requirements.

Amazon DSP / Amazon Marketing Cloud (AMC) require that all personal information
(email, phone, name, address) be **normalized and SHA-256 hashed before upload**.
[`prepare_amazon_dsp.py`](./prepare_amazon_dsp.py) does that for you, locally.

- **Runs entirely on your machine.** Raw emails/PII are read from your local
  export, hashed, and only the hashed output is written. Nothing is uploaded by
  this script.
- **No dependencies.** Pure Python 3.8+ standard library.
- **Compliance-first default.** Only email-marketing **subscribers** are included
  unless you explicitly opt out of that filter.

---

## 1. Export your list from Shopify

Shopify Admin → **Customers** → (optionally pick a segment / filter) →
**Export** → choose **CSV for Excel, Numbers, or other spreadsheet programs** →
**Export customers**. Save the file, e.g. `customers.csv`.

> Tip: To pre-filter to subscribers in Shopify, use the
> *"Email subscription status is Subscribed"* customer filter before exporting.
> The script also filters by consent on its own (see below), so either works.

## 2. Run the tool

```bash
python3 prepare_amazon_dsp.py customers.csv -o amazon_dsp_audience.csv
```

You'll get a summary like:

```
Amazon DSP audience file — preparation summary
----------------------------------------------------
  Identifier columns included : EMAIL, PHONE, FIRST_NAME, LAST_NAME, ADDRESS, CITY, STATE, ZIP, COUNTRY_CODE
  Consent filter              : subscribed
  Rows read                   : 24,113
  Dropped (not subscribed)    : 3,902
  Dropped (no valid email)    : 55
  Unique users written        : 20,156
  -> amazon_dsp_audience.csv

  ✓  Above Amazon's 2,000-user minimum for exact audiences ...
```

Try it right now against the included fake data:

```bash
python3 prepare_amazon_dsp.py sample_shopify_export.csv -o /tmp/test.csv
```

## 3. Upload to Amazon DSP / AMC

Upload `amazon_dsp_audience.csv` as your hashed audience / identity dataset.
The file is UTF-8, comma-delimited, with the identifier columns Amazon expects.

---

## Output format

| Column | Hashed? | Notes |
|---|---|---|
| `user_id` | **No** | Your stable per-record key (Shopify Customer ID, else derived). |
| `EMAIL` | Yes (SHA-256) | |
| `PHONE` | Yes | E.164 digits, no `+` |
| `FIRST_NAME` | Yes | |
| `LAST_NAME` | Yes | |
| `ADDRESS` | Yes | street line only |
| `CITY` | Yes | |
| `STATE` | Yes | |
| `ZIP` | Yes | |
| `COUNTRY_CODE` | Yes | ISO 3166-1 alpha-2 |

Columns are only included if your export actually contains that data. Providing
more identifiers → higher match rate. Email alone is the single strongest key.

## Normalization (applied before hashing)

Every hash is SHA-256, output as lowercase hex.

| Field | Rule |
|---|---|
| EMAIL | trim; lowercase |
| PHONE | digits only; strip intl prefix / leading zero; prepend country code if missing (default `1`); E.164 without `+` |
| FIRST/LAST NAME | trim; lowercase; letters only |
| ADDRESS | trim; lowercase; drop punctuation; standardize suffixes (`STREET`→`st`) & directionals (`NORTH`→`n`); tokens joined with no spaces |
| CITY | trim; lowercase; alphanumeric only |
| STATE | trim; lowercase; alphanumeric only |
| ZIP | trim; lowercase; alphanumeric only; US truncated to 5 digits |
| COUNTRY_CODE | ISO alpha-2, lowercase |

This mirrors Amazon's published rules and the address logic in their official
[audience normalization SDK](https://github.com/amzn/amazon-ads-advertiser-audience-normalization-sdk-py).
Because normalization is deterministic, `123 North Main Street` and
`123 N Main St` hash to the same value — which is exactly how matching improves.

## Options

| Flag | Default | Purpose |
|---|---|---|
| `-o, --output` | `amazon_dsp_audience.csv` | Output path. |
| `--consent {subscribed,all}` | `subscribed` | `subscribed` keeps only email-marketing subscribers. `all` keeps everyone — use only if you have a lawful basis for every row. |
| `--no-require-email` | (email required) | Keep rows that have another identifier even without an email. |
| `--default-country-code` | `1` | Calling code prepended to phones lacking one (`1` = US/CA). |
| `--gzip` | off | Gzip output (Amazon supports GZIP). |
| `--max-rows-per-file N` | off | Split into parts of ≤ N rows (Amazon recommends splitting files > 1 GB). |
| `--delimiter` / `--input-delimiter` | `,` | Field delimiters. |

## Audience-size guidance (from Amazon)

- **2,000+** matched users → exact audiences.
- **500+** matched users → lookalike audiences.
- Amazon recommends providing **10,000 – 5,000,000** rows of hashed data.

The script's count is *pre-match*; Amazon's matched count will be lower, so aim
well above the minimums.

## Compliance notes

- Only upload **permission-based** data. The default `--consent subscribed`
  filter enforces this from your Shopify email-marketing consent field; if no
  consent column is found, the script warns you loudly.
- Do not upload **GDPR un-consented** event data.
- Amazon also requires acceptance of its *Sending Personal Information to Amazon
  Ads* terms and, for event/AMC datasets, an **Amazon consent signal**
  (`consentType` = TCF/GPP/ACS, plus `country`). This script produces an
  **identity audience file**; if you're building a time-series (FACT) event
  dataset that needs consent columns, tell me and I'll extend it.

_Field normalization follows Amazon Ads' hashed-records guidance:
[Format audience file for hashing](https://advertising.amazon.com/help/GCCXMZYCK4RXWS6C)
· [hashed-records API docs](https://advertising.amazon.com/API/docs/en-us/data-provider/hashed-records)._
