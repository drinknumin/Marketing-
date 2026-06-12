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
| **Offer 2 — $1 trial** | Email unlocks the $1 deal | **20–33%** (benchmark: ~33% elsewhere) | ~2,600–4,300 | High intent (see funnel note) | Med — billing/compliance |
| **Quiz — Decision Profile** | Email gates the result + toolkit | **5–10%** | ~650–1,300 | Med (toolkit-seekers; brand-aligned) | High — custom build |

> ⚠️ Rates are **benchmark-based estimates to validate by test.** The $1 trial's
> **~33%** is anchored to a real result from a comparable $1 deal at another brand
> (not yet run at Numin). Treat the low end of each range as the conservative
> planning number.

---

## Read the $1 trial as a funnel, not one number
"Opt-in" isn't the same action for a free pop-up and a $1 offer. The $1 trial has
**three steps**, and only the first is the opt-in:
1. **Pop-up email opt-in** — drop an email to claim the $1 deal. Lowest-friction
   action there is — this is the **20–33%** (~2,600–4,300/mo).
2. **Paid trial start** — put a card down and pay the $1. A subset of step 1.
3. **Retained subscriber** — convert at day 21 and stay. A subset of step 2 —
   where refunds, chargebacks, and the day-21 conversion live (see
   `numin-offers-and-economics.md`).

Offers 1/3 and the quiz only have step 1, so the $1 trial **wins opt-in by a wide
margin** — but its real value is decided in steps 2–3. It can flood the list and
still lose money if the back end leaks.

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

**Offer 2 — $1 trial.** The opt-in **winner by a wide margin** — though **new to
Numin**. A comparable, simpler $1 deal run at another brand ($1 now → charged at
day 30, no day-21 step) hit **~33% pop-up opt-in** and produced a flood of emails.
"$1 for the product" is a stronger hook than "X% off" or "find your type," so it
sits well above the others. Our proposed structure (charged at day 21 if not
returned, refill day 30) has more complex terms to disclose, which likely shaves
opt-in a bit — **~20% is a reasonable planning number against that ~33%
benchmark** (~2,600–4,300/mo). The caution isn't opt-in; it's everything
downstream of it (trial start → day-21 conversion → retention, plus
refunds/chargebacks) — see the economics doc.

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

1. **$1 trial — highest opt-in by far (~33% benchmark elsewhere; new to Numin).** If raw email volume is
   the goal, nothing else is close (~2,600–4,300/mo). Green-light rests on the
   downstream economics (day-21 conversion + retention + refunds), **not** opt-in
   — pair with the economics doc before scaling.
2. **Offer 1 (discount pop-up) — the safe, simple workhorse.** Proven ~6%, lowest
   build, profitable on the first order. Good steady-state default, and the
   fallback if the $1 trial's back end doesn't pencil.
3. **Quiz — highest brand fit, biggest build.** Strong opt-in ceiling and owns the
   decision-fatigue territory; longer to build, rate hinges on completion. Start
   now, test once live.
4. **Offer 3 (GWP)** — brand-safe A/B against Offer 1 if discount-training the
   customer is a concern.

## How we'll measure
- Primary: **opt-in rate vs. 2.7%** and **emails/mo vs. ~350** (target ~6%+, ~780+/mo).
- Per-mechanism: completion/drop-off (quiz especially), and cost per email.
- **$1 trial specifically:** track all three funnel steps — email opt-in → paid
  trial start → retained subscriber — not just opt-in, or you'll mistake a flood
  of emails for a flood of customers.
- Downstream (ties to `numin-offers-and-economics.md`): what each email cohort is
  worth — purchase rate, CAC, and retention — since a high opt-in that doesn't
  convert is worth less than a smaller, higher-intent one.

> Opt-in volume is only half the picture; pair this with the economics doc before
> committing budget.
