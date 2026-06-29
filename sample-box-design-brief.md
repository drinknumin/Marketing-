# Numin "$5 Starter" — Design Brief and Build Prompt

Everything a designer needs to build the gated $5 sample test: the offer mechanics, the
three screens (pop-up, landing page, product page), the subscription messaging, and the
legal must-haves. The last section is a copy-paste prompt for Claude Design.

---

## 1. How the offer works (the mechanics every screen must support)

**In one line:** Unlock the deal with your email and phone, pay $5, and get a 5-count
sample box. If you don't cancel, your monthly plan starts in 2 weeks at $54/month
(20-count box).

**Two ways to buy (shown as a plan selector on the product page):**
1. **One-time — $54** for a 20-count box, bought "as is." No subscription, no trial,
   no recurring charge. Always directly buyable, no unlock needed.
2. **The $5 Starter** — the gated, low-commitment way to try (the mechanics below).
Only the $5 Starter is gated behind the email + phone unlock. The one-time box is a
plain sale.

**The deal is gated.** The only way to get the $5 price is to enter an email and phone
number in the pop-up. That unlock is the trade: we give the cheap sample, they join our
email and text lists. The phone number matters — the day-11 text reminder is what keeps
the day-14 charge from feeling like a surprise.

**The timeline:**

| When | What happens | Money |
|---|---|---|
| Day 0 | Unlock with email + phone, pay $5, 5-count sample ships, 2-week window starts | Charge $5 |
| ~Day 5 | Sample runs out (about a 5-day supply) | — |
| Days 1 to 13 | Free to cancel, keep the sample, owe nothing | — |
| ~Day 11 | Reminder (email + SMS): "plan starts in 3 days, $54, cancel anytime" | — |
| Day 14 | If not cancelled, the monthly plan begins: charge $54, 20-count box ships | Charge $54 |
| Every 30 days after | Refill ships | Charge $54 |

**Decisions to confirm (recommendation first):**
- **Does the $5 count toward the first box?** Recommend no — $5 is just the sample price.
- **Sample size:** 5-count (their call). The 9-day gap to the day-14 charge is manageable
  with the reminder. A 10 to 14-count would nearly close the gap if conversion needs help.
- **Cancel terms:** cancel anytime in 14 days, keep the sample, no charge (recommended).

---

## 2. The legal must-haves (design these IN — do not bury them)

The **$5 Starter** charges automatically at day 14 and collects a phone number for texts,
so two sets of rules apply: the FTC subscription rules and the texting rules (TCPA). (The
one-time $54 box is a plain sale — none of this applies to it.) Both protect us from
chargebacks and complaints. **Not optional for the $5 Starter:**

1. **Clear terms before payment** — the $5 now, the exact date and amount of the day-14
   charge ($54), the recurring $54/month, and how to cancel. Plain words.
2. **SMS + email consent at the unlock** — a clear line that by entering their email and
   phone they agree to receive marketing emails and texts, with opt-out wording (reply
   STOP). This sits in the pop-up.
3. **A consent checkbox** at the buy button restating the trial terms.
4. **Easy cancel** — one link, online, as easy as signing up.
5. **A reminder before the day-14 charge** (email + SMS, ~3 days out).
6. **An order confirmation that restates the terms and the dates.**

---

## 3. Where it lives

This is an **isolated test**, separate from the main numin.com site: its own landing page
on a separate URL or subdomain, paid ads (Meta) as the only traffic, small audience,
capped budget. Walled off so we control everything, measure a clean cost per customer, and
can switch it off instantly.

---

## 4. The three screens to design

### A. The pop-up (Alia style)
This is the gate for the $5 Starter (the one-time $54 box doesn't need it) and the first
thing they see. Model it on the Alia pop-up we already use.

- **Layout: 50/50 split.** Left half is a full-bleed image (product or a sharp
  professional lifestyle shot). Right half is the offer and the form.
- **Right side, top to bottom:**
  - The offer name, concise and bold: **"THE $5 STARTER"**
  - Headline: **"Try Numin for $5"**
  - One-line deal: "Get a 5-day sample for $5. Keep it, and your plan starts in 2 weeks at
    $54/month. Cancel anytime."
  - **Email field**
  - **Phone field**
  - Button: **"Unlock my $5 deal"**
  - Consent line (small): "By signing up you agree to get emails and texts from Numin and
    to the trial terms. Reply STOP to opt out."
  - A small "No thanks" dismiss link.
- **Mobile:** image on top (shorter), form below. Big tap targets. Keep it to one screen.
- The deal stays locked until they submit. On submit, the offer unlocks and they go to the
  product page or straight to checkout.

### B. The homepage / landing page
The main test page. The deal spelled out clearly, top to bottom:
1. Hero: "THE $5 STARTER" name, the headline, and the primary button ("Unlock my $5 deal,"
   which opens the pop-up). One-line deal under it.
2. The problem: decision fatigue, named plainly. Who it hits (professionals).
3. What Numin is and what it does.
4. **How the $5 Starter works** — a simple 3-step timeline: unlock + pay $5 → try it for 2
   weeks → plan starts day 14 unless you cancel. This doubles as the legal disclosure.
5. Proof: reviews, press logos, the guarantee.
6. The science, briefly (glutamate / the 4pm crash).
7. FAQ — answer "When am I charged? How do I cancel?" head-on.
8. A quiet secondary path for buy-once shoppers ("Prefer to buy once? $54 for a 20-count
   box."), linking to the product page.
9. Final call to action with the terms restated.

### C. The product page (with a plan selector)
The page where the customer chooses how to buy. Two columns on desktop (image left, info
right), stacked on mobile. The core is a **plan selector** with two choices:
- **One-time — $54.** One 20-count box, no subscription, no trial. Selecting it shows a
  simple "Add to cart — $54." Buyable directly, no pop-up, no trial terms.
- **The $5 Starter** (visually primary, tag it "Best way to try"). "$5 today, then
  $54/month from day 14 unless you cancel." Gated — until unlocked it reads "Unlock for $5"
  and the button opens the pop-up (email + phone). Once unlocked, it's selected at $5 with
  the trial terms shown.
- When the $5 Starter is selected, show the 3-step timeline box and the terms + consent
  checkbox right at the button. When One-time is selected, show only the price and add-to-cart.
- Below: trust badges, guarantee, a few reviews, a short ingredients/science strip.

### Plus: the subscription messaging (lifecycle)
Order confirmation (screen + email), a short nurture email or two before day 11, the day-11
reminder (email + SMS), the day-14 charge + shipping confirmation, an easy cancel flow
(offer pause/skip), and a manage-subscription page.

---

## 5. Brand and visual direction

- **Numin** is a premium cognitive supplement built around **decision fatigue** — sharper
  decisions, less 4pm fog. Not generic "focus and energy."
- **Audience:** professionals and decision-makers. Higher-end, not mass.
- **Tone:** scientific, calm, credible, premium. Diagnostic, not hype. No neon "ACT NOW."
- **Look:** clean and modern, lots of white space, charcoal text with one calm accent
  color, strong typography, real product photography.
- **Mobile-first.** Most paid-social traffic is on a phone. Phone view first, big tap
  targets, short copy, sticky CTA.
- **Honest-conversion.** The clearest path to the button, terms shown plainly. Clarity is
  the conversion strategy.

---

## 6. Example copy for the highest-stakes moments

**Pop-up (right side):**
> THE $5 STARTER
> Try Numin for $5.
> Get a 5-day sample for $5. Keep it, and your plan starts in 2 weeks at $54/month. Cancel
> anytime.
> [ email ]  [ phone ]
> [ Unlock my $5 deal ]
> By signing up you agree to get emails and texts from Numin and to the trial terms. Reply
> STOP to opt out.

**Terms box at the button:**
> $5 today for your sample. On **[date]** we charge **$54** and start your monthly plan
> (20-count, $54/month) unless you cancel. Cancel anytime, one click. ☐ I understand and agree.

**Day-11 reminder (email + SMS):**
> Your Numin plan starts in 3 days. On **[date]** we'll charge $54 and ship your first full
> box (20 count), then $54/month. Want it? Do nothing. Not yet? Cancel in one click.

**Order confirmation:**
> You're in. You paid **$5** for your sample, shipping today. If you don't cancel, on
> **[date]** we'll charge **$54** and start your monthly plan. Manage anytime here.

**Plan selector (product page):**
> One-time — $54. One 20-count box, no subscription.
> The $5 Starter — $5 today, then $54/month from day 14 unless you cancel.

---

## 7. ===== COPY-PASTE PROMPT FOR CLAUDE DESIGN =====

> You are designing a conversion-focused "$5 Starter" funnel for **Numin**, a premium
> cognitive supplement positioned around **decision fatigue** (sharper decisions, less 4pm
> mental fog — not generic "focus and energy"). Audience: busy professionals and
> decision-makers. Tone: scientific, calm, credible, premium — diagnostic, never hypey.
> Look: clean and modern, generous white space, charcoal text with one calm accent color,
> strong type, real product photography. **Design mobile-first** with big tap targets and a
> sticky call-to-action, then show the desktop version.
>
> **Two ways to buy (a plan selector on the product page):** (1) one-time $54 for a
> 20-count box, no subscription, always directly buyable; (2) the $5 Starter, the gated
> trial. Only the $5 Starter is gated.
>
> **The $5 Starter:** The $5 deal is gated. To unlock it, the customer enters their email and
> phone number. Then they pay $5 and get a 5-count sample box. If they don't cancel, on day
> 14 the monthly plan begins: $54/month for a 20-count box. They can cancel anytime in the
> 14 days, keep the sample, and owe nothing.
>
> **Non-negotiable legal elements (these apply only to the $5 Starter — the one-time $54
> box is a plain sale and needs none of this; design them in clearly, never bury them):**
> state all terms in plain words before payment (the $5 today, the exact date and amount of the
> day-14 charge of $54, the recurring $54/month, how to cancel); in the pop-up, include a
> clear email + SMS consent line with opt-out wording (reply STOP); include a consent
> checkbox at the buy button; make canceling one click; and design a reminder sent ~3 days
> before the day-14 charge. Treat this clarity as a conversion and trust feature.
>
> **Design these three screens, plus the lifecycle messages, all responsive and on-brand:**
> 1. **Pop-up (Alia style)** — a 50/50 split: a full-bleed image on the left, and on the
>    right the concise offer name ("THE $5 STARTER"), a headline ("Try Numin for $5"), the
>    one-line deal, an email field, a phone field, an "Unlock my $5 deal" button, the
>    email/SMS consent line, and a small "No thanks" dismiss. On mobile, image on top and
>    form below, one screen. The $5 deal stays locked until they submit.
> 2. **Homepage / landing page** — hero with the offer name, headline, and a button that
>    opens the pop-up; the decision-fatigue problem; what Numin is; a simple 3-step "how the
>    $5 Starter works" timeline (unlock + pay $5, try it 2 weeks, plan starts day 14 unless
>    you cancel — this doubles as the legal disclosure); reviews + press + guarantee; a
>    brief science section; an FAQ that answers "When am I charged?" head-on; a final CTA
>    with terms restated.
> 3. **Product page (with a plan selector)** — two choices: One-time ($54, 20-count, no
>    subscription, buyable directly with a simple "Add to cart — $54", no trial terms) and
>    the $5 Starter (visually primary, "best way to try": $5 today, then $54/month from day
>    14 unless cancelled; gated — until unlocked it reads "Unlock for $5" and opens the
>    pop-up for email + phone). When the $5 Starter is selected, show the 3-step timeline and
>    the terms + consent checkbox at the button. Plus trust badges and a few reviews.
> Also design the lifecycle messages: order confirmation, a day-11 reminder (email + SMS),
> the day-14 charge confirmation, and a one-click cancel flow.
>
> Use this exact copy where it matters:
> - Pop-up deal line: "Get a 5-day sample for $5. Keep it, and your plan starts in 2 weeks
>   at $54/month. Cancel anytime." Consent: "By signing up you agree to get emails and texts
>   from Numin and to the trial terms. Reply STOP to opt out."
> - Terms box: "$5 today for your sample. On [date] we charge $54 and start your monthly plan
>   (20-count, $54/month) unless you cancel. Cancel anytime, one click. ☐ I understand and agree."
> - Reminder: "Your Numin plan starts in 3 days. On [date] we'll charge $54 and ship your
>   first full box (20 count), then $54/month. Want it? Do nothing. Not yet? Cancel in one click."
>
> Deliver each screen as a clean, labeled mockup (mobile and desktop), with real copy, not
> lorem ipsum.
