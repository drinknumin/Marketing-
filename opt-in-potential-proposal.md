# Opt-In Potential by Offer — Proposal for Team Review

**Purpose:** compare the email-capture (opt-in) potential of each candidate
offer/mechanism so the team can decide what to test first. Focus here is
**opt-in volume**, not unit economics — the CAC/LTV math for each offer lives in
`numin-offers-and-economics.md`.

---

## Where we are now
- **Current opt-in: 2.7%** (down from **6.2%** before the site + price change).
- **Email volume: ~350/mo** (down from **~750/mo**).
- **Implied traffic: ~13,000 visitors/mo** (350 ÷ 2.7% ≈ 13K; 750 ÷ 6.2% ≈ 12.1K — consistent).
- **Rule of thumb: every +1 pt of opt-in ≈ ~130 emails/mo.** Getting back to 6%
  ≈ ~780/mo; 8% ≈ ~1,040/mo.

**The bar:** beat 2.7%, target a return to **~6%+** (~780+/mo).

---

## The comparison

| Mechanism | Opt-in trigger | Est. opt-in rate | Emails/mo (~13K traffic) | Email quality / intent | Build & risk |
|---|---|---|---|---|---|
| **Baseline** (today's generic pop-up) | Email for newsletter/generic | **2.7%** (actual) | ~350 | Low–med | Live |
| **Offer 1 — Discount pop-up** | Email unlocks the discount code | **5–7%** | ~650–910 | Med–high (deal-seekers, but converted before) | Low — proven, fast |
| **Offer 3 — Gift-with-purchase** | Email unlocks the free gift | **3–5%** | ~390–650 | Med | Low — needs gift inventory |
| **Offer 2 — $1 trial** | Trial start (email **+ card**) | **3–6%** | ~390–780 (all customers) | Highest intent | Med — billing/compliance setup |
| **Quiz — Decision Profile** | Email gates the result + toolkit | **5–10%** | ~650–1,300 | Med (toolkit-seekers; brand-aligned) | High — custom build |

> ⚠️ Every rate above except the baseline is a **benchmark-based estimate, not a
> measured result.** They're hypotheses to validate by test. Ranges reflect that
> uncertainty; treat the low end as the conservative planning number.

---

## Mechanism by mechanism

**Offer 1 — Discount pop-up (email-gated).** The most proven option: this is the
mechanism that delivered **6.2%** before the site/price change, so restoring a
strong money-off offer should return opt-in to the **5–7%** band — roughly
**+300–560 emails/mo** over today. Lowest build, fastest to live. Captured
emails skew deal-seeker but this cohort converted for us historically. *This is
the fastest lever to refill the list.*

**Offer 3 — Gift-with-purchase pop-up.** A free branded gift (spoon/tin) is less
universally compelling than straight money-off, so it typically opts in **below
a discount but above a generic ask — ~3–5%**. Main appeal is that it captures
emails **without discount-training** the customer. Reasonable as a brand-safe
alternative to Offer 1, or an A/B against it.

**Offer 2 — $1 trial.** Different axis: the "opt-in" here is a **trial start,
which captures email *and* a card on file** — so it's a purchase action, not a
free email. Fewer pure emails than a free pop-up could get, but **every capture
is a (tentative) customer**, i.e. the highest-intent list of the five. A $1 hook
should lift site conversion well above today's 1.24%, so **~3–6% of visitors**
starting a trial is plausible. Note: you can still run a free email pop-up
*alongside* it to catch non-buyers.

**Quiz — Decision Profile.** Highest **ceiling** and best brand fit (it owns the
"decision fatigue" territory). Quiz pop-ups commonly capture **2–4× a static
pop-up**, so **5–10%** is a realistic visitor-level range — potentially the
single biggest email source (**~650–1,300/mo**). Two caveats for the team: it's
the **highest build effort** (custom Octane AI flow + result pages + Klaviyo +
toolkit PDFs), and the realized rate is **gated by completion** — a long
question set drives drop-off before the email gate, so the rate is the most
sensitive to execution and the least proven for us.

---

## Suggested test sequence (for discussion)

1. **Offer 1 (discount pop-up) first** — proven ~6%, lowest build, fastest way to
   refill the list while everything else is built. Restores ~+300–560 emails/mo.
2. **Quiz in parallel** — highest ceiling and on-brand; longer build, so start it
   now and test once live. Watch completion rate closely.
3. **Offer 2 ($1 trial)** — test as its own acquisition play (captures customers,
   not just emails); judge on the economics doc, not opt-in alone.
4. **Offer 3 (GWP)** — hold as the brand-safe A/B against Offer 1 if
   discount-training the customer is a concern.

## How we'll measure
- Primary: **opt-in rate vs. 2.7%** and **emails/mo vs. ~350** (target ~6%+, ~780+/mo).
- Per-mechanism: completion/drop-off (quiz especially), and cost per email.
- Downstream (ties to `numin-offers-and-economics.md`): what each email cohort is
  worth — purchase rate, CAC, and retention — since a high opt-in that doesn't
  convert is worth less than a smaller, higher-intent one.

> Opt-in volume is only half the picture; pair this with the economics doc before
> committing budget.
