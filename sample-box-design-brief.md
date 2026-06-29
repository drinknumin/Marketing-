# Numin "$5 Sample Box" — Design Brief and Build Prompt

Everything a designer needs to build the sample-box test: the offer mechanics, every
screen, the subscription messaging, and the legal must-haves. The last section is a
copy-paste prompt for Claude Design.

---

## 1. How the offer works (the mechanics every screen must support)

**In one line:** Pay $5 today, get a 5-count sample box. If you don't cancel, on day 30
we start your monthly plan at $54/month (20-count box).

**The timeline:**

| When | What happens | Money |
|---|---|---|
| Day 0 (checkout) | Customer pays $5, the 5-count sample ships, the 30-day window starts | Charge $5 |
| ~Day 5 | Sample runs out (about a 5-day supply) | — |
| Days 5 to 29 | Nurture emails keep them warm and remind them the plan is coming | — |
| Days 1 to 29 | Free to cancel, owes nothing more | — |
| ~Day 26 | Reminder: "your plan starts in 4 days, $54 charge, cancel anytime" | — |
| Day 30 | If not cancelled, the monthly plan begins: charge $54, 20-count box ships | Charge $54 |
| Every 30 days after | Refill ships | Charge $54 |

**The big risk to watch:** the gap between the 5-day sample and the day-30 charge. They
have no product for about three weeks before we bill them. The nurture sequence (below)
exists to close that gap. If day-30 conversion comes in low, the levers are: a bigger
sample (say 14-count), enrolling sooner, or a stronger nurture sequence.

**Decisions to confirm before build (recommendation first):**
- **Does the $5 count toward the first box?** Recommend no — $5 is just the sample price.
  (Could credit it as goodwill if conversion needs help.)
- **Sample size:** 5-count (their call). Flag: only ~5 days of product. Consider 14-count
  if the gap hurts conversion.
- **Cancel terms:** cancel anytime in the 30 days, keep the sample, no charge (recommended).
- **Sample shipping:** small light mailer to keep the sample cost down (~$8 to $9 all in).

---

## 2. The legal must-haves (design these IN — do not bury them)

Because we charge people automatically at day 30, the FTC and the credit-card networks
require this. It also keeps chargebacks under 1%, which is what keeps the offer (and our
payment processing) alive. **Not optional:**

1. **Clear terms before payment** — the $5 now, the exact date and amount of the day-30
   charge ($54), the recurring $54/month, and how to cancel. Plain words, no fine print.
2. **The pre-checkout terms pop-up** (see surface E below) — an explicit confirmation of
   the deal right before they pay. This is the customer's express consent.
3. **A consent checkbox** at the buy button as well.
4. **Easy cancel** — one link, online, as easy as signing up.
5. **A reminder before the day-30 charge** (email + SMS, a few days out).
6. **An order confirmation that restates the terms and the dates.**

Make the clarity a trust feature, not a disclaimer. Honest "here's exactly what happens
and when" lifts conversion and crushes refunds.

---

## 3. Where it lives

This is an **isolated test**, separate from the main numin.com site:
- Its own landing page on a separate URL or subdomain.
- Paid ads (Meta) are the only traffic source. Small audience, capped budget.
- Walled off so we control everything, measure a clean cost per customer, and can switch
  it off instantly.

So the "homepage" and "product page" below are pages of this standalone funnel, not
changes to the live site.

---

## 4. The surfaces to design (in funnel order)

**A. Ad creative (Meta)** — the hook that earns the click. Must match the landing page
("Try Numin — $5 sample"). A few variations, static and short video.

**B. Entry pop-up (email capture)** — captures an email so we can remarket people who
don't buy. The $5 hook, one email field, one button. Light, dismissible. Fires on
exit-intent or after ~15 seconds. (This is different from the pre-checkout pop-up in E.)

**C. Landing page / homepage** — the main test page. Sections, top to bottom:
1. Hero: the $5 sample offer, the headline, one primary button ("Get my $5 sample").
2. The problem: decision fatigue, named plainly. Who it hits (professionals).
3. What Numin is and what it does.
4. **How the sample works** — a simple 3-step timeline ($5 today → try it → plan starts
   day 30 unless you cancel). This doubles as the legal disclosure, so keep it honest.
5. Proof: reviews, press logos, the guarantee.
6. The science, briefly (glutamate / the 4pm crash), kept light.
7. FAQ — answer "What happens after the sample? When am I charged?" head-on.
8. Final call to action with the terms restated.

**D. Product page** — the focused page where the sample is added to cart:
- Product, price framing ($5 today, then $54/month starting day 30), the timeline box, the button.
- The terms and consent line sit right at the add-to-cart.
- Trust badges, guarantee, a few reviews.

**E. Pre-checkout terms pop-up (REQUIRED)** — a modal that appears when they click to
check out, before payment. It restates the whole deal and requires an explicit tap to
continue. This is the express-consent step and the thing that prevents "I didn't know
I'd be charged" refunds. Two buttons: confirm and continue, or go back.

**F. Checkout** — minimal fields (paid social is mobile and impatient). States exactly
what's charged today ($5) and the full schedule. The consent checkbox.

**G. Subscription messaging (the lifecycle)** — on-screen and email/SMS:
1. Order confirmation (screen + email): "You paid $5 for your sample. If you don't
   cancel, on [date] we charge $54 and start your monthly plan."
2. **Gap nurture sequence** (days 5 to 26): a few emails — how to get the most from
   Numin, the science, reviews, "your plan starts [date]." This keeps them warm through
   the no-product gap.
3. Day ~26 reminder (email + SMS): plan starting, charge coming, one-click cancel.
4. Day 30 charge + shipping confirmation.
5. Cancellation flow — simple, a couple of clicks, with a pause/skip option offered.
6. Manage-subscription / account page.
7. Failed-payment email (if the day-30 charge fails, ask them to update their card).

---

## 5. Brand and visual direction

- **Numin** is a cognitive supplement built around **decision fatigue** — not generic
  "focus and energy." The angle is sharper decisions, less 4pm fog.
- **Audience:** professionals and decision-makers. Higher-end, not mass.
- **Tone:** scientific, calm, credible, premium. Diagnostic, not hype. No BuzzFeed
  energy, no neon "ACT NOW."
- **Look:** clean and modern, lots of white space, charcoal text with a calm accent
  color, strong typography, real product photography.
- **Mobile-first.** Most paid-social traffic is on a phone. Phone view first, big tap
  targets, short copy, sticky CTA button.
- **Honest-conversion.** Clearest path to the button, with the terms shown plainly.
  Clarity is the conversion strategy here.

---

## 6. Example copy for the highest-stakes moments

Give these to the designer so the critical text reads right:

**Pre-checkout terms pop-up:**
> Before you go, here's the deal:
> You pay **$5 today** for your sample.
> If you love it, do nothing — on **[Month Day]** we'll charge **$54** and ship your
> first full month (20 count), then **$54/month**.
> Cancel anytime before **[Month Day]** and you'll never be charged again.
> [ Go back ]   [ I understand — place my $5 order ]

**Terms box at the button:**
> $5 today for your sample. On **[date]** we charge **$54** and start your monthly plan
> (20-count, $54/month) unless you cancel. Cancel anytime, one click.
> ☐ I understand and agree.

**Day-26 reminder (email + SMS):**
> Subject: Your Numin plan starts in 4 days
> Your sample's done its job. On **[date]** we'll charge $54 and ship your first full box
> (20 count), then $54/month. Want it? Do nothing. Not yet? **Cancel in one click.**

**Order confirmation:**
> You're in. You paid **$5** for your sample, shipping today. If you don't cancel, on
> **[date]** we'll charge **$54** and start your monthly plan. Manage anytime here.

---

## 7. ===== COPY-PASTE PROMPT FOR CLAUDE DESIGN =====

> You are designing a conversion-focused "$5 sample box" funnel for **Numin**, a premium
> cognitive supplement positioned around **decision fatigue** (sharper decisions, less
> 4pm mental fog — not generic "focus and energy"). The audience is busy professionals
> and decision-makers. Tone: scientific, calm, credible, premium — diagnostic, never
> hypey. Look: clean and modern, generous white space, charcoal text with one calm
> accent color, strong type, real product photography. **Design mobile-first** with big
> tap targets and a sticky call-to-action, then show the desktop version.
>
> **The offer:** Pay $5 today, get a 5-count sample box. No further charge unless they
> stay. If they don't cancel, on day 30 the monthly plan begins: $54/month for a
> 20-count box. They can cancel anytime in the 30 days, keep the sample, and owe nothing.
>
> **Non-negotiable legal elements (the FTC and card networks require these — design them
> in clearly, never bury them):** state all terms in plain words before payment (the $5
> today, the exact date and amount of the day-30 charge of $54, the recurring $54/month,
> how to cancel); show a pre-checkout pop-up that restates the full deal and requires an
> explicit tap to continue; include a consent checkbox at the buy button; make canceling
> one click; and design a reminder sent a few days before the day-30 charge. Treat this
> clarity as a conversion and trust feature.
>
> **Design these screens, all responsive and on-brand:**
> 1. **Entry pop-up** — exit-intent/timed, captures an email, presents the $5 hook, one
>    field, one button.
> 2. **Landing page (homepage)** — hero with the $5 sample offer and primary CTA; the
>    decision-fatigue problem; what Numin is; a simple 3-step "how the sample works"
>    timeline ($5 today, try it, plan starts day 30 unless you cancel — this doubles as
>    the legal disclosure); reviews + press + guarantee; a brief science section; an FAQ
>    that answers "When am I charged?" head-on; a final CTA with terms restated.
> 3. **Product page** — the $5 sample add-to-cart, price framing ($5 today, then
>    $54/month starting day 30), the timeline box, the terms + consent line at the
>    button, trust badges and a few reviews.
> 4. **Pre-checkout terms pop-up** — a modal that appears when they click to check out,
>    before payment, restating the full deal with an explicit confirm button and a go-back
>    button.
> 5. **Checkout** — minimal fields, exactly what's charged today and the full schedule,
>    the consent checkbox.
> 6. **Subscription / lifecycle messaging** — order confirmation (screen + email); a
>    short gap nurture sequence (a few emails between day 5 and day 26 that keep them warm
>    while they're out of product); the day-26 reminder (email + SMS); the day-30 charge
>    and shipping confirmation; a simple cancellation flow (offer pause/skip); and a
>    manage-subscription page.
>
> Use this exact copy for the highest-stakes moments:
> - Pre-checkout pop-up: "Before you go, here's the deal: you pay $5 today for your
>   sample. If you love it, do nothing — on [date] we'll charge $54 and ship your first
>   full month (20 count), then $54/month. Cancel anytime before [date] and you'll never
>   be charged again." Buttons: "Go back" and "I understand — place my $5 order."
> - Terms box: "$5 today for your sample. On [date] we charge $54 and start your monthly
>   plan (20-count, $54/month) unless you cancel. Cancel anytime, one click. ☐ I
>   understand and agree."
> - Reminder: "Your sample's done its job. On [date] we'll charge $54 and ship your first
>   full box (20 count), then $54/month. Want it? Do nothing. Not yet? Cancel in one click."
>
> Deliver each screen as a clean, labeled mockup (mobile and desktop), with real copy,
> not lorem ipsum.
