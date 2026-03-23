---
id: floating-rate-bonds
title: Floating Rate Bonds and Variable-Coupon Debt
domain: economics
course: financial-economics
prerequisites:
- id: bond-basics
  type: hard
- id: bond-pricing
  type: hard
builds-toward:
- interest-rate-swaps
tags:
- bonds
- floating-rate
- interest-rate
stage: formal-systems
status: validated
---

# Floating Rate Bonds and Variable-Coupon Debt

## Core Idea
Floating-rate bonds have coupons that reset periodically (often quarterly) tied to a benchmark rate like LIBOR plus a spread. They protect investors from rising rates (prices remain stable) and issuers from falling rates (lower funding costs). Understanding the mechanics of rate resets, caps, and spreads is essential for valuation and duration analysis.

## Questions

```yaml
- question: "Interest rates rise sharply from 3% to 5%. An investor holds two bonds with identical maturity and credit quality: one fixed-rate at 3% coupon, one floating-rate at benchmark + 0.5%. What happens to each bond's price?"
  type: multiple-choice
  options:
    - "Both fall in price — rising rates hurt all bond prices equally"
    - "The fixed-rate bond falls in price; the floating-rate bond's price stays near par"
    - "The floating-rate bond falls more — it has higher payment uncertainty"
    - "The fixed-rate bond falls; the floating-rate bond falls less because the spread provides a cushion"
  answer: 1
  explanation: "The fixed-rate bond locks in 3% coupons, now below market — investors demand a discount. The floating-rate bond resets its coupon to 5.5% at the next reset date, so both the cash flows and the discount rate rise together, keeping present value roughly constant. Option A is wrong because floaters are specifically designed to avoid price decline. Option D is wrong — the spread doesn't 'cushion' anything; the reset mechanism eliminates the interest rate sensitivity almost entirely."

- question: "Why is a floating-rate bond's effective duration approximately equal to the time until the next coupon reset, rather than the bond's full maturity?"
  type: multiple-choice
  options:
    - "Because floating-rate bonds are always short-term instruments that mature quickly"
    - "Because the benchmark rate determines the bond's maturity date"
    - "Because at each reset the bond reprices to market — between resets it behaves like an ultra-short-term instrument maturing at the next reset date"
    - "Because the fixed spread dominates the duration calculation"
  answer: 2
  explanation: "Duration measures price sensitivity to rate changes. A floater reprices to par at each reset because it pays what the market requires at that moment. Between resets it is essentially a fixed-rate bond maturing at the next reset date — days or weeks away — which has negligible price sensitivity. Option A is wrong; floaters can have long legal maturities of 10 or 20 years. Option B is nonsensical. Option D is backwards — the spread is fixed and small; it's the variable benchmark component that drives near-zero duration."

- question: "A floating-rate bond's price stays near par when market interest rates rise because its coupon payments increase proportionally, keeping the bond's present value roughly constant."
  type: true-false
  answer: true
  explanation: "This is the core mechanism. Bond price equals the present value of future cash flows. For a fixed-rate bond, the numerators (cash flows) are fixed while the denominator (discount rate) rises — price falls. For a floater, both the numerators and denominator rise together, so the ratio (present value) stays approximately constant. This isn't an approximation of why floaters work — it is the fundamental reason they were invented."

- question: "An investor in a floating-rate bond faces no meaningful price risk as long as market interest rates remain stable."
  type: true-false
  answer: false
  explanation: "Even with stable interest rates, a floater faces credit spread risk. The coupon resets to benchmark + fixed spread. If the issuer's creditworthiness deteriorates, the market demands a wider spread — but the fixed spread in the coupon formula doesn't change. The bond's price falls to reflect inadequate compensation for the now-higher credit risk. This is often overlooked: rates can be perfectly stable while the issuer's credit quality erodes, causing the floater's price to decline just as a fixed-rate bond would in a rising-rate environment."

- question: "Explain why a floating-rate bond's price stays near par even as market interest rates change significantly over the bond's lifetime."
  type: short-answer
  answer: "A floater's coupon resets to the current benchmark at each reset date. Because cash flows adjust proportionally with the discount rate used to price them, the present value remains approximately constant. Between resets the bond behaves like an ultra-short-term instrument maturing at the next reset date, which has minimal price sensitivity. At each reset, the bond reprices back to par by definition — the investor is effectively rolling over a very short-term instrument at current market rates."
  explanation: "The key is effective duration: a floater's price sensitivity is determined by the time to next reset (days to weeks), not its legal maturity. This is the designed property of the instrument — issuers and investors both use it specifically to decouple income from capital value. The near-zero price sensitivity holds as long as we're talking about interest rate risk; credit spread risk, which floaters do not eliminate, is a separate and often underappreciated exposure."
```

## Explainer

From your study of bond basics and bond pricing, you understand the inverse relationship between bond prices and interest rates: when rates rise, the present value of fixed future cash flows falls, so bond prices fall. This **interest rate risk** (duration risk) is the central risk of holding fixed-rate bonds. A 10-year bond with a 3% coupon falls meaningfully in price if rates rise to 4%, because you are now locked into below-market coupons. **Floating-rate bonds** (floaters) are designed to eliminate most of this price sensitivity by having the coupon adjust with the market.

Instead of a fixed coupon, a floater pays a coupon that resets periodically — typically quarterly — equal to a benchmark rate plus a fixed **spread**. Historically the benchmark was LIBOR (London Interbank Offered Rate); since LIBOR's discontinuation, it is typically SOFR (Secured Overnight Financing Rate) or a government short-term rate. If the benchmark is 3% and the spread is 0.50%, today's coupon is 3.50%. If the benchmark rises to 4% by the next reset date, the coupon resets to 4.50%. Because cash flows adjust with the market rate, the bond's price stays close to par — its **effective duration** is approximately equal only to the time until the next reset (days or weeks), not the time to maturity.

Understanding *why* this works deepens your bond pricing intuition. A bond's value equals the present value of its future cash flows, discounted at current market rates. For a fixed-rate bond, if market rates rise, the discount rate rises but the cash flows stay the same, so price falls. For a floater, the cash flows themselves rise proportionally with the discount rate, keeping the present value roughly constant. Think of it this way: between reset dates, a floater behaves like an extremely short-term bond — one that matures at the next reset. It has low duration because the investor will receive par-value-equivalent cash flows shortly and can reinvest at prevailing rates. This is why floaters are said to have near-zero duration: they continuously reprice to market.

The residual risks of floaters are worth understanding clearly. **Credit spread risk** remains: if the issuer's creditworthiness deteriorates, the fixed spread component may no longer adequately compensate investors for the credit risk, and the price falls even if market interest rates haven't changed. **Caps** on the benchmark rate (maximum coupon limits) can disadvantage investors if rates rise above the cap, reintroducing some interest rate risk from above. For issuers, floaters are attractive when they believe rates will fall — their funding costs decline automatically. For investors, floaters are defensive instruments when rates are expected to rise — they avoid capital losses and their income keeps pace with the market. This creates natural use cases: banks that borrow short-term and lend long-term issue floaters to match their liability structure; pension funds and insurance companies with long-dated fixed liabilities tend to prefer fixed-rate bonds.
