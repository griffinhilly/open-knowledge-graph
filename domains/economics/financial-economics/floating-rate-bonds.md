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
status: draft
---

# Floating Rate Bonds and Variable-Coupon Debt

## Core Idea
Floating-rate bonds have coupons that reset periodically (often quarterly) tied to a benchmark rate like LIBOR plus a spread. They protect investors from rising rates (prices remain stable) and issuers from falling rates (lower funding costs). Understanding the mechanics of rate resets, caps, and spreads is essential for valuation and duration analysis.

## Explainer

From your study of bond basics and bond pricing, you understand the inverse relationship between bond prices and interest rates: when rates rise, the present value of fixed future cash flows falls, so bond prices fall. This **interest rate risk** (duration risk) is the central risk of holding fixed-rate bonds. A 10-year bond with a 3% coupon falls meaningfully in price if rates rise to 4%, because you are now locked into below-market coupons. **Floating-rate bonds** (floaters) are designed to eliminate most of this price sensitivity by having the coupon adjust with the market.

Instead of a fixed coupon, a floater pays a coupon that resets periodically — typically quarterly — equal to a benchmark rate plus a fixed **spread**. Historically the benchmark was LIBOR (London Interbank Offered Rate); since LIBOR's discontinuation, it is typically SOFR (Secured Overnight Financing Rate) or a government short-term rate. If the benchmark is 3% and the spread is 0.50%, today's coupon is 3.50%. If the benchmark rises to 4% by the next reset date, the coupon resets to 4.50%. Because cash flows adjust with the market rate, the bond's price stays close to par — its **effective duration** is approximately equal only to the time until the next reset (days or weeks), not the time to maturity.

Understanding *why* this works deepens your bond pricing intuition. A bond's value equals the present value of its future cash flows, discounted at current market rates. For a fixed-rate bond, if market rates rise, the discount rate rises but the cash flows stay the same, so price falls. For a floater, the cash flows themselves rise proportionally with the discount rate, keeping the present value roughly constant. Think of it this way: between reset dates, a floater behaves like an extremely short-term bond — one that matures at the next reset. It has low duration because the investor will receive par-value-equivalent cash flows shortly and can reinvest at prevailing rates. This is why floaters are said to have near-zero duration: they continuously reprice to market.

The residual risks of floaters are worth understanding clearly. **Credit spread risk** remains: if the issuer's creditworthiness deteriorates, the fixed spread component may no longer adequately compensate investors for the credit risk, and the price falls even if market interest rates haven't changed. **Caps** on the benchmark rate (maximum coupon limits) can disadvantage investors if rates rise above the cap, reintroducing some interest rate risk from above. For issuers, floaters are attractive when they believe rates will fall — their funding costs decline automatically. For investors, floaters are defensive instruments when rates are expected to rise — they avoid capital losses and their income keeps pace with the market. This creates natural use cases: banks that borrow short-term and lend long-term issue floaters to match their liability structure; pension funds and insurance companies with long-dated fixed liabilities tend to prefer fixed-rate bonds.
