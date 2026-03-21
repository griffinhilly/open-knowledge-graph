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

## Questions

```yaml
- question: "During a financial crisis, Treasury yields fall sharply while investment-grade corporate bond yields rise. What best explains the dramatic widening of credit spreads?"
  type: multiple-choice
  options:
    - "Corporate bonds pay fixed coupons, so their yields automatically rise when interest rates fall"
    - "Default risk, liquidity risk, and risk aversion all rise simultaneously while Treasuries rally on flight-to-quality demand"
    - "Credit rating agencies downgrade all corporate bonds simultaneously, mechanically increasing their yields"
    - "The Federal Reserve raises interest rates during crises, increasing borrowing costs for corporations"
  answer: 1
  explanation: "Spread widening in crises comes from multiple forces acting together: expected defaults rise, liquidity dries up (markets thin out, bid-ask spreads widen), and risk aversion surges. At the same time, Treasuries rally as investors flee to safety — yields fall. The spread widens from both ends. Rating downgrades may follow, but they react to market conditions rather than drive them."

- question: "A corporate bond yields 5.5% while a Treasury bond of the same maturity yields 4.0%. The 150 bps credit spread primarily represents:"
  type: multiple-choice
  options:
    - "Purely the expected annual default loss — the probability of default times the loss given default"
    - "Compensation only for liquidity risk, since investment-grade bonds rarely default"
    - "Compensation for default risk, liquidity risk, and credit cycle risk — more than expected default losses alone can explain"
    - "The coupon premium paid to attract investors who prefer corporate bonds over Treasuries"
  answer: 2
  explanation: "Credit spreads decompose into a default risk premium and a liquidity premium, and empirical research finds that actual expected default losses alone substantially underexplain observed spreads. Liquidity risk and credit cycle compensation account for a large share — more than naive default probability calculations would predict. Even investment-grade bonds carry meaningful liquidity risk."

- question: "Credit spreads on corporate bonds tend to widen during economic expansions and narrow during recessions."
  type: true-false
  answer: false
  explanation: "The opposite is true. Spreads NARROW in expansions (defaults are rare, investors are risk-hungry and willing to accept less compensation) and WIDEN in recessions (defaults spike, liquidity dries up, risk aversion surges). This cyclical pattern means corporate bonds perform worst precisely when economic conditions are most painful — a key source of credit risk distinct from interest rate risk."

- question: "A high-yield (BB-rated) bond typically carries a wider credit spread than an investment-grade (BBB-rated) bond because it carries higher default probability and lower liquidity."
  type: true-false
  answer: true
  explanation: "Credit ratings signal default risk, and higher default risk (plus lower liquidity) commands a wider spread. High-yield bonds historically carry spreads of 300–1000+ bps compared to 50–300 bps for investment-grade bonds, reflecting meaningfully higher expected default rates and thinner markets. During the 2008–09 crisis, high-yield spreads exceeded 2,000 bps."

- question: "Why might a corporate bond's credit spread be larger than what expected default losses alone would predict? What other risks does the spread compensate investors for?"
  type: short-answer
  answer: "Beyond default risk, the spread compensates for liquidity risk — the difficulty of selling the bond quickly at fair value, especially in stressed markets — and for credit cycle risk: the mark-to-market losses from spread widening during downturns, even if the bond ultimately doesn't default. Empirical studies find that expected default losses alone account for less than half of observed spreads in many market conditions; the rest reflects liquidity premiums and compensation for bearing credit cycle volatility."
  explanation: "This distinction matters for portfolio management: investors who focus only on default probability will underestimate the true risk of corporate bond holdings. Spread widening can cause substantial losses long before any actual default occurs."
```

## Explainer

From bond pricing and yield-to-maturity, you know that a bond's price is the present value of its future cash flows, and that yield moves inversely with price. But you learned those concepts primarily in the context of government bonds — securities with essentially zero default risk. Corporate bonds introduce a new dimension: the borrower might not pay. The **credit spread** is the market's price for that risk.

The credit spread is simply the difference in yield-to-maturity between a corporate bond and a Treasury bond of the same maturity. If a 10-year Treasury yields 4.0% and a 10-year investment-grade corporate bond yields 5.2%, the credit spread is 120 basis points (1.20 percentage points). That 120 bps premium is what investors demand to hold the corporate bond instead of the "risk-free" Treasury. The spread decomposes into two main components: a **default risk premium** (compensation for expected losses from default) and a **liquidity premium** (compensation for the corporate bond being harder to buy and sell quickly at fair value). In practice, empirical studies find that liquidity and credit cycle risk account for a surprisingly large share of spreads — more than pure expected default losses alone would predict.

**Credit ratings** from agencies like Moody's, S&P, and Fitch provide shorthand for default risk. Investment-grade bonds (rated BBB-/Baa3 or above) carry relatively narrow spreads — historically 50–300 bps over Treasuries depending on the cycle. High-yield or "junk" bonds (rated BB+/Ba1 or below) carry much wider spreads — often 300–1000+ bps — reflecting meaningfully higher default probabilities. During the 2008–09 financial crisis, high-yield spreads exceeded 2,000 bps as markets priced near-certain defaults for many issuers.

Spreads are not static — they move dramatically with the economic cycle. In expansions, corporate earnings are healthy, defaults are rare, and investors are risk-hungry: spreads compress as demand for corporate bonds rises and investors are willing to accept less compensation. In recessions or financial stress, defaults spike, liquidity dries up, and risk aversion surges: spreads widen sharply, causing corporate bond prices to fall even as Treasury prices rise (the classic "flight to quality"). This **spread widening** creates mark-to-market losses for holders, which is why credit spread risk is a distinct source of portfolio risk separate from interest rate risk — two bonds with identical durations can have very different price behavior in a credit crisis if one is a Treasury and the other is a corporate bond.

## How It's Best Learned
Look up current investment-grade and high-yield spread indices (e.g., ICE BofA OAS indices) and chart them against recessions to see the cyclical pattern. Then compare the implied default-loss rate (spread × recovery-adjusted default probability) to actual historical default rates to understand how much of the spread is genuine default premium versus liquidity compensation.
