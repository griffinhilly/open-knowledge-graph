---
id: corporate-bond-credit-spreads
title: Corporate Bond Credit Spreads
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: yield-to-maturity
  type: hard
builds-toward:
- credit-risk-and-default
- hedging-with-derivatives
tags:
- bonds
- credit
- spreads
- risk
stage: formal-systems
status: draft
---

# Corporate Bond Credit Spreads

## Core Idea
Credit spreads are the yield differences between corporate bonds and Treasury bonds of similar maturity, compensating investors for default risk, liquidity risk, and credit cycles. Spreads widen during economic stress and narrow during expansions, creating both risk and opportunity. Spread levels reflect market expectations of credit conditions.

## Explainer

From bond pricing and yield-to-maturity, you know that a bond's price is the present value of its future cash flows, and that yield moves inversely with price. But you learned those concepts primarily in the context of government bonds — securities with essentially zero default risk. Corporate bonds introduce a new dimension: the borrower might not pay. The **credit spread** is the market's price for that risk.

The credit spread is simply the difference in yield-to-maturity between a corporate bond and a Treasury bond of the same maturity. If a 10-year Treasury yields 4.0% and a 10-year investment-grade corporate bond yields 5.2%, the credit spread is 120 basis points (1.20 percentage points). That 120 bps premium is what investors demand to hold the corporate bond instead of the "risk-free" Treasury. The spread decomposes into two main components: a **default risk premium** (compensation for expected losses from default) and a **liquidity premium** (compensation for the corporate bond being harder to buy and sell quickly at fair value). In practice, empirical studies find that liquidity and credit cycle risk account for a surprisingly large share of spreads — more than pure expected default losses alone would predict.

**Credit ratings** from agencies like Moody's, S&P, and Fitch provide shorthand for default risk. Investment-grade bonds (rated BBB-/Baa3 or above) carry relatively narrow spreads — historically 50–300 bps over Treasuries depending on the cycle. High-yield or "junk" bonds (rated BB+/Ba1 or below) carry much wider spreads — often 300–1000+ bps — reflecting meaningfully higher default probabilities. During the 2008–09 financial crisis, high-yield spreads exceeded 2,000 bps as markets priced near-certain defaults for many issuers.

Spreads are not static — they move dramatically with the economic cycle. In expansions, corporate earnings are healthy, defaults are rare, and investors are risk-hungry: spreads compress as demand for corporate bonds rises and investors are willing to accept less compensation. In recessions or financial stress, defaults spike, liquidity dries up, and risk aversion surges: spreads widen sharply, causing corporate bond prices to fall even as Treasury prices rise (the classic "flight to quality"). This **spread widening** creates mark-to-market losses for holders, which is why credit spread risk is a distinct source of portfolio risk separate from interest rate risk — two bonds with identical durations can have very different price behavior in a credit crisis if one is a Treasury and the other is a corporate bond.

## How It's Best Learned
Look up current investment-grade and high-yield spread indices (e.g., ICE BofA OAS indices) and chart them against recessions to see the cyclical pattern. Then compare the implied default-loss rate (spread × recovery-adjusted default probability) to actual historical default rates to understand how much of the spread is genuine default premium versus liquidity compensation.
