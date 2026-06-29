# Numin "$1 Trial" — Design Brief and Build Prompt

Everything a designer needs to build the $1 trial test: the offer mechanics, every
screen, the subscription messaging, and the legal must-haves. The last section is a
copy-paste prompt for Claude Design.

---

## 1. How the offer works (the mechanics every screen must support)

**In one line:** Pay $1 today, get a full box of Numin. Keep it past 21 days and we
charge the rest; your monthly plan then runs at $54 a month.

**The timeline:**

| When | What happens | Money |
|---|---|---|
| Day 0 (checkout) | Customer pays $1, box 1 ships, trial starts | Charge $1 |
| Days 1 to 20 | Free to cancel, owes nothing more | — |
| ~Day 17 | Reminder: "trial ends in 3 days, charge coming, cancel anytime" | — |
| Day 21 | If not cancelled, charge the rest of box 1 | Charge $53 (box 1 now = $54) |
| Day 30 | First refill (box 2) ships, monthly plan begins | Charge $54 |
| Every 30 days after | Refill ships | Charge $54 |

**Decisions to confirm before build (I've put my recommendation first):**
- **Day-21 charge:** charge $53 so box 1 totals a clean $54 (recommended), or charge a
  full $54 on top of the $1. Recommend $53.
- **Returns:** "cancel anytime in 21 days, keep your box, no charge" (recommended —
  supplements can't be resold, so don't ask for physical returns), vs. requiring a
  mail-back. Recommend cancel-and-keep.
- **What $1 buys:** the full 20-pack (recommended — a real ~3-week supply, which is
  why the 21-day window works), vs. a small sample. Recommend the full box.
- **Trial length:** 21 days (matches when a 20-pack runs out). Keep.

---

## 2. The legal must-haves (design these IN — do not bury them)

Because we charge people automatically later, the FTC and the credit-card networks
require this. Getting it right also keeps chargebacks under 1%, which is what keeps
the offer alive. **These are not optional design elements:**

1. **Clear terms right next to the buy button, before payment** — the $1 now, the
   exact date and amount of the day-21 charge, the recurring $54/month, and how to
   cancel. In plain words, visible without scrolling or clicking.
2. **A consent checkbox** — an explicit "I understand I'll be charged $54 on [date]
   and $54/month after, unless I cancel."
3. **Easy cancel** — canceling must be as easy as signing up. One link, online, no
   phone call.
4. **A reminder before the day-21 charge** — email and SMS, a few days out.
5. **An order confirmation that restates the terms and the dates.**

Turn this into trust, not fine print: an honest "here's exactly what happens and when"
actually lifts conversion and crushes refunds.

---

## 3. Where it lives

This is an **isolated test**, separate from the main numin.com site:
- Its own landing page on a separate URL or subdomain.
- Paid ads (Meta) are the only traffic source. Small audience, capped budget.
- Because it's walled off, we control everything, measure a clean cost per customer,
  and can switch it off instantly.

So the "homepage" and "product page" below are sections/pages of this standalone
funnel, not changes to the live site.

---

## 4. The surfaces to design (in funnel order)

**A. Ad creative (Meta)** — the hook that earns the click. Message must match the
landing page exactly ("Try Numin for $1"). A few variations, static and short video.

**B. Pop-up (on the landing page)** — captures email so we can remarket people who
don't buy. Presents the $1 hook, one email field, one button. Light, fast, dismissible.
Likely fires on exit-intent or after ~15 seconds.

**C. Landing page / homepage** — the main test page. Sections, top to bottom:
1. Hero: the $1 offer, the headline, one primary button ("Start my $1 trial").
2. The problem: decision fatigue, named plainly. Who it hits (professionals).
3. What Numin is and what it does.
4. **How the $1 trial works** — the 3-step timeline as a simple graphic. This doubles
   as the legal disclosure, so it must be clear and honest.
5. Proof: reviews, press logos, the guarantee.
6. The science, briefly (glutamate / the 4pm crash), kept light.
7. FAQ — answer "Will I be charged?" head-on. Turn the terms into trust.
8. Final call to action with the terms restated.

**D. Product page** — the focused page where the trial is added to cart:
- Product, price framing ($1 today, then $54/month), the timeline box, the button.
- The terms and consent line sit right at the add-to-cart.
- Trust badges, guarantee, a few reviews.

**E. Cart / checkout** — the highest-stakes screen for compliance:
- States exactly what's charged today ($1) and the full schedule.
- The consent checkbox.
- As few fields as possible (paid social traffic is mobile and impatient).

**F. Subscription messaging (the lifecycle)** — on-screen and email/SMS:
1. Order confirmation (screen + email): "You paid $1. Trial runs to [date]. On [date]
   we charge $53 unless you cancel. Next box ships [date]."
2. Day ~17 reminder (email + SMS): trial ending, charge coming, one-click cancel.
3. Day 21 charge confirmation.
4. Day 30 refill shipping notice.
5. Cancellation flow — simple, a couple of clicks, with a "pause" or "skip" option offered.
6. Manage-subscription / account page.
7. Failed-payment email (if the day-21 or refill charge fails, ask them to update card).

---

## 5. Brand and visual direction

- **Numin** is a cognitive supplement built around **decision fatigue** — not generic
  "focus and energy." The angle is sharper decisions, less 4pm fog.
- **Audience:** professionals and decision-makers. Higher-end, not mass.
- **Tone:** scientific, calm, credible, premium. Think diagnostic, not hype. No
  BuzzFeed energy, no neon "ACT NOW."
- **Look:** clean and modern, lots of white space, charcoal text with a calm accent
  color, strong typography, real product photography.
- **Mobile-first.** Most paid-social traffic is on a phone. Design the phone view first,
  big tap targets, short copy, sticky CTA button.
- **Honest-conversion.** The clearest path to the button, with the terms shown plainly.
  Clarity is the conversion strategy here.

---

## 6. Example copy for the highest-stakes moments

Give these to the designer so the critical compliance text reads right:

**Terms box at the button:**
> Here's the deal: pay **$1 today** for your first box. Love it? Do nothing — on
> **[Month Day]** we'll charge **$53** for your first box, then **$54/month** starting
> **[Month Day]**. Cancel anytime before **[Month Day]** and you'll never be charged again.
> ☐ I understand and agree.

**Day-17 reminder (email + SMS):**
> Subject: Your Numin trial ends in 3 days
> Your 21-day trial ends **[date]**. If Numin's working for you, do nothing — we'll
> charge $53 and keep your plan going at $54/month. Not feeling it? **Cancel in one
> click**, no charge.

**Order confirmation:**
> You're in. You paid **$1** today. Your trial runs until **[date]**. On **[date]**
> we'll charge **$53** unless you cancel. Your next box ships **[date]**. Manage anytime here.

---

## 7. ===== COPY-PASTE PROMPT FOR CLAUDE DESIGN =====

> You are designing a conversion-focused "$1 trial" funnel for **Numin**, a premium
> cognitive supplement positioned around **decision fatigue** (sharper decisions, less
> 4pm mental fog — not generic "focus and energy"). The audience is busy professionals
> and decision-makers. Tone: scientific, calm, credible, premium — diagnostic, never
> hypey. Look: clean and modern, generous white space, charcoal text with one calm
> accent color, strong type, real product photography. **Design mobile-first** with big
> tap targets and a sticky call-to-action; then show the desktop version.
>
> **The offer:** Pay $1 today, get a full 20-count box. The customer enrolls in a
> monthly plan with a 21-day trial. On day 21, if they haven't cancelled, we charge $53
> (so the first box totals $54). On day 30 the first refill ships and monthly billing
> begins at $54/month. They can cancel anytime in the 21 days, keep the box, and owe
> nothing.
>
> **Non-negotiable legal elements (the FTC and card networks require these — design
> them in clearly, never bury them):** state all terms in plain words right next to the
> buy button before payment (the $1 today, the exact date and amount of the day-21
> charge, the recurring $54/month, how to cancel); include a consent checkbox; make
> canceling one click; and design a reminder sent a few days before the day-21 charge.
> Treat this clarity as a conversion and trust feature.
>
> **Design these screens, all responsive and on-brand:**
> 1. **Pop-up** — exit-intent/timed, captures an email, presents the $1 hook, one
>    field, one button.
> 2. **Landing page (homepage)** — hero with the $1 offer and primary CTA; the
>    decision-fatigue problem; what Numin is; a simple 3-step "how the $1 trial works"
>    timeline (this doubles as the legal disclosure); reviews + press + guarantee; a
>    brief science section; an FAQ that answers "Will I be charged?" head-on; a final
>    CTA with terms restated.
> 3. **Product page** — the $1 trial add-to-cart, price framing ($1 today, then
>    $54/month), the timeline box, the terms + consent line at the button, trust badges
>    and a few reviews.
> 4. **Checkout** — minimal fields, exactly what's charged today and the full schedule,
>    the consent checkbox.
> 5. **Subscription / lifecycle messaging** — order confirmation (screen + email), the
>    day-17 reminder (email + SMS), the day-21 charge confirmation, the day-30 refill
>    notice, a simple cancellation flow (offer pause/skip), and a manage-subscription page.
>
> Use this exact copy for the highest-stakes moments:
> - Terms box: "Here's the deal: pay $1 today for your first box. Love it? Do nothing —
>   on [date] we'll charge $53 for your first box, then $54/month starting [date].
>   Cancel anytime before [date] and you'll never be charged again. ☐ I understand and agree."
> - Reminder: "Your 21-day trial ends [date]. If Numin's working for you, do nothing —
>   we'll charge $53 and keep your plan going at $54/month. Not feeling it? Cancel in one
>   click, no charge."
>
> Deliver each screen as a clean, labeled mockup (mobile and desktop), with real copy,
> not lorem ipsum.
