# Numin — Offer Design & Unit Economics

Three offers, the economics behind each, and the CAC tolerance / tracking
thresholds to know whether they're working. Built off the brand & growth memo.

> **All numbers below are a model, not gospel.** They hang on a handful of
> assumptions (next section). Correct the inputs and the conclusions move with
> them — the structure is the useful part.

---

## 0. Base unit economics (the foundation)

| Input | Value | Source / assumption |
|---|---|---|
| Subscription price (20-pack, recurring) | **$54/mo** | ≈ $2.70/unit, per the memo |
| One-time list price | $60 | current site |
| Fully-loaded COGS | **50%** | product + pack + ship + fees, per memo |
| → Variable cost per shipment | **~$27** | 50% of $54 |
| → **Contribution margin per shipment** | **~$27** | what's left to pay for CAC + profit |
| Avg paid shipments per customer (M) | **3 / 4 / 5** | "most don't stay past ~4 months" → base case **4** |
| Healthy target | **LTV:CAC ≥ 3:1** | standard D2C; payback inside ~3 shipments |

**The single most important number: the physical product costs ~$27 per
20-pack no matter what price you charge for it.** That's why a deep
first-order discount pencils now and didn't before — more on that under Offer 1.

**Contribution LTV** (what actually pays back CAC):

| Shipments (M) | 3 | 4 | 5 |
|---|---|---|---|
| Contribution LTV | $81 | **$108** | $135 |

> ⚠️ Caveat: if the 50% is **product-only** and shipping/fees are on top
> (~$5–6/order), shave that off the first order and off contribution. I've
> flagged where it bites.

---

## 1. The headline you can't dodge

At **~$27 contribution** and **~4-month retention**, a healthy **3:1** requires:

| Retention (M) | Max CAC for 3:1 |
|---|---|
| 3 shipments | **$27** |
| 4 shipments | **$36** |
| 5 shipments | **$45** |

So at today's retention, the business is only *healthy* if **CAC sits around
$30–45.** That is the whole game. Current blended CAC (~$143) loses money
because contribution LTV is ~$100 — you're paying ~$1.40 to make ~$1.00. Every
offer below is judged on one question: **does it pull blended CAC toward $30–45
(and/or push retention past 4 months)?**

Two levers, not one:
- **Offers + site** pull CAC down (better conversion, better first-order deal).
- **Retention** (failed-payment recovery, winback, the churn phone calls) raises
  M, which *widens your CAC tolerance*. Recovering failed payments is the
  cheapest M-boost you have — it lifts the whole table at ~$0 cost.

---

## 2. Master CAC tolerance table

Contribution-based LTV:CAC at $27/shipment. Green = healthy (≥3:1),
amber = profitable but thin (1–3x), red = underwater (<1x).

| CAC | Break-even (shipments) | M=3 ($81) | M=4 ($108) | M=5 ($135) |
|---|---|---|---|---|
| **$20** | 0.7 — pays back on order 1 | 4.1x 🟢 | 5.4x 🟢 | 6.8x 🟢 |
| **$50** | 1.9 — ~month 2 | 1.6x 🟡 | 2.2x 🟡 | 2.7x 🟡 |
| **$80** | 3.0 — ~month 3 | 1.0x 🔴 | 1.4x 🟡 | 1.7x 🟡 |
| **$100** | 3.7 — ~month 4 | 0.8x 🔴 | 1.1x 🟡 | 1.4x 🟡 |

Reading it: **$20 CAC is great at any plausible retention. $50 is workable but
never hits 3:1 at current retention. $80–100 only survives if you also extend
retention** — exactly why the churn work matters as much as the offers.

---

## 3. Offer 1 — "Unlock the deal" (the comeback offer)

**The old email-gated subscribe-and-save, brought back because 50% COGS finally
lets it pencil.** This is the everyday acquisition + list-building engine, and
the direct fix for opt-in (6.2% → 2.7%) and email volume (750 → 350/mo).

**Structure**
- Inflated one-time anchor: **$90** ("20-pack, $90").
- Pop-up gate: *enter email to unlock 45% off your first subscription order.*
- Subscribe price: **first order $49**, then **$54/mo** recurring.
- The discount only exists if you (a) give an email and (b) start a subscription.

**Why it works now and didn't before** — same physical $27–54 cost, different era:

| | First order @ $49 | COGS | First-order contribution |
|---|---|---|---|
| **Old, 90% COGS** (20-pack) | $49 | ~$54 | **−$5** (lose money before CAC) |
| **Old 40-pack @ ~$40, 90%** | ~$40 | ~$90 | **−$50** 🔴 (why it never penciled) |
| **Now, 50% COGS** (20-pack) | $49 | **$27** | **+$22** 🟢 |

The "low-quality buyer" worry was never proven — and at 50% COGS even a
mediocre cohort is contribution-positive from order one. The offer's real job is
**cheap, contribution-positive email capture.**

**Contribution LTV by retention:** order 1 = $22, then +$27/order →
2: $49 · 3: $76 · 4: $103 · 5: $130.

**CAC tolerance (Offer 1):**

| CAC | Profitable by | LTV:CAC @ M=4 ($103) |
|---|---|---|
| $20 | order 1 | 5.2x 🟢 |
| $50 | order 2 | 2.1x 🟡 |
| $80 | order 3–4 | 1.3x 🟡 |
| $100 | order 4 | 1.0x 🔴 |

**Track / tolerance:**
- **Opt-in rate** — target back to **5–6%+** (pre-change baseline 6.2%).
- **Email volume** — back toward **~700+/mo**.
- First-order contribution stays **positive** (it will, by design).
- **Kill/rework if:** opt-in stays <3% *or* this cohort retains materially worse
  than the historical $1/unit cohort did (finally test the "low-quality" claim
  instead of assuming it).

**Risk:** lowest of the three. Worst case you've rebuilt the list and acquired
profitably. Brand cost: anchor-discounting trains people to wait for deals —
acceptable for a performance engine, watch it doesn't bleed into brand channels.

---

## 4. Offer 2 — The "$1 Mega Trial" (the swing)

**Pay $1, get the product, get charged at day 21 if you keep it, refill at the
month mark if you don't cancel.** Highest upside, highest risk, most operational
surface area. This is a **CAC-compression bet**, not a margin play.

**Structure**
- **Day 0:** pay **$1**, subscribe, receive the 20-pack (~3-week supply — the
  pack size and the trial window line up, which is the clever part).
- **Day 21:** if not cancelled/returned, charged the balance to **$54** for the
  pack you kept.
- **Day ~30:** refill ships, normal **$54/mo** subscription begins.

So a **converted** trial customer is just a normal subscriber whose first 21
days were at-risk. A **non-converter** costs you the pack: $1 collected − $27
cost = **−$26** (supplements aren't resaleable on return — assume full loss),
**plus the ad cost you already spent to acquire that trial.**

**The economics live and die on two numbers: trial-start CAC and the day-21
conversion rate (c).** Effective cost per *paying* customer:

> **CPP = CAC / c + ((1 − c) / c) × $26**
>
> *(ad cost spread over only the converters, plus the product you ate on
> non-converters)*

**Effective cost per paying customer (CPP):**

| Trial-start CAC | c = 40% | c = 50% | c = 60% | c = 70% |
|---|---|---|---|---|
| **$20** | $89 | $66 | $51 | $40 |
| **$50** | $164 | $126 | $101 | $82 |
| **$80** | $239 | $186 | $150 | $125 |
| **$100** | $289 | $226 | $184 | $154 |

**LTV:CAC at base retention (M=4, $108 contribution LTV):**

| Trial-start CAC | c = 40% | c = 50% | c = 60% | c = 70% |
|---|---|---|---|---|
| **$20** | 1.2x 🟡 | 1.6x 🟡 | 2.1x 🟡 | 2.7x 🟡 |
| **$50** | 0.7x 🔴 | 0.9x 🔴 | 1.1x 🟡 | 1.3x 🟡 |
| **$80** | 0.5x 🔴 | 0.6x 🔴 | 0.7x 🔴 | 0.9x 🔴 |
| **$100** | 0.4x 🔴 | 0.5x 🔴 | 0.6x 🔴 | 0.7x 🔴 |

**Read this carefully:** the $1 trial is **underwater at $50+ CAC across almost
every conversion rate**, and only reaches a healthy 3:1 in the extreme corner
(CAC ~$20, c ~70%, M=5 → ~3.4x). It is **not** a margin play.

**It is a bet that "$1" collapses your CAC.** A $1 hook should lift landing
conversion several-fold (your site is at 1.24% vs a 2.5–3.5% benchmark; a $1
offer can push 4–6%+), and CAC falls roughly in proportion. **If the $1 offer
drives trial-start CAC into the ~$20–30 band and holds conversion ≥55–60%, it's
a real volume engine at ~1.5–2x.** If it can't get CAC under ~$40, it's a money
pit — walk away. Run it on a *slice* of paid traffic and prove the CAC drop
before scaling.

**Track / tolerance (hard guardrails):**
- **Trial-start CAC ≤ $30** (the entire thesis — if this doesn't materialize, stop).
- **Day-21 conversion ≥ 55–60%** (#1 health metric).
- **Chargeback/dispute rate < 1%** — card networks flag at ~1% and can freeze
  processing. Surprise day-21 charges are the classic trigger.
- Cancel-before-21 rate, day-30 refill rate, and converted-cohort retention vs
  normal subscribers.
- Live monitor: **CPP < contribution LTV with ≥1.5x cushion**, recomputed weekly
  from the formula above.
- **Kill if:** conversion <45%, chargebacks >1%, or CPP > LTV.

**Compliance (do not skip):** this is **negative-option billing** — regulated by
the FTC and the card networks (and "click-to-cancel" rules). Required:
unmistakable disclosure of the day-21 charge *before* checkout, an **email/SMS
reminder a few days before** the charge, one-click cancel, and clean records.
Get this wrong and chargebacks + processor risk will sink the offer regardless
of the unit math.

---

## 5. Offer 3 — Gift with Purchase (the brand-safe option)

**Subscribe and get the branded spoon / tin / bottle free on your first order.**
The memo's instinct. Protects price and margin, adds perceived value without
training people to wait for discounts, reinforces brand.

**Structure**
- No price discount. Subscribe at **$54** → free branded accessory on order 1.
- GWP landed cost ~**$6** (branded tin/spoon).
- Pop-up: *subscribe today and we'll include the [tin], free.*

**Economics:** first-order contribution **$27 − $6 = $21**, recurring **$27** —
essentially the base case minus a one-time $6. Contribution LTV by retention:
1: $21 · 2: $48 · 3: $75 · 4: $102 · 5: $129. CAC tolerance ≈ the master table
(a hair lighter on order 1).

**Track / tolerance:**
- Subscribe-rate lift vs a no-GWP control (does the gift actually move conversion?).
- Retention ≥ control (gifts can attract worse cohorts — verify it doesn't).
- First-order contribution stays positive after GWP cost (it does).
- **Kill if:** no conversion lift over control, or GWP cohort churns faster.

**Risk:** low, but typically a **smaller conversion lift than a price cut**, and
it adds inventory/fulfillment complexity. Best where you don't want to
anchor-discount — e.g., brand-led or PR-driven traffic.

---

## 6. Side-by-side & recommendation

| | Offer 1: Unlock | Offer 2: $1 Trial | Offer 3: GWP |
|---|---|---|---|
| Primary job | Email capture + cheap acq | CAC compression / volume | Brand-safe conversion lift |
| First-order contribution | +$22 | **−$26** until day-21 convert | +$21 |
| Risk | Low | **High** (CAC + chargebacks + compliance) | Low |
| Healthy at CAC… | ≤ ~$45 | only ≤ ~$30 **and** c ≥ 60% | ≤ ~$45 |
| Fixes which gap | Opt-in 6.2→2.7, emails 750→350 | Site CVR 1.24% | Conversion w/o discounting |
| Brand cost | Trains discount-waiting | Highest (surprise charge) | Lowest |

**Recommendation:**
1. **Run Offer 1 now** as the default acquisition + list engine. It's the
   fastest fix for opt-in and email volume, it's contribution-positive from
   order one at 50% COGS, and it's low risk. Use it to *finally test* the
   "low-quality buyer" assumption you walked away on.
2. **Test Offer 2 on a slice** of paid traffic as a CAC-compression experiment,
   with the guardrails above locked in *before* launch (disclosure, reminders,
   chargeback monitoring). Scale **only** if it genuinely drives trial-start CAC
   under ~$30 at ≥55–60% conversion. Treat it as a bet on CAC, not on margin.
3. **Keep Offer 3 in the pocket** for brand-led / PR traffic where you don't want
   to anchor-discount — and as the cleaner long-term face once the brand carries
   more weight.

**The thing under all three:** at ~$27 contribution and ~4-month retention,
nothing is healthy above ~$45 CAC. The offers buy you cheaper acquisition; the
churn work (failed-payment recovery first, then the customer calls) buys you a
higher M — and a higher M is what makes an $80–100 CAC survivable. You need both.
