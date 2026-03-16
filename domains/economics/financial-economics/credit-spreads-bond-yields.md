---
id: credit-spreads-bond-yields
title: Credit Spreads and Bond Yields
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: yield-to-maturity
  type: hard
builds-toward:
- bond-portfolio-strategies
tags:
- fixed-income
- credit-risk
- yield-analysis
stage: formal-systems
status: draft
---

# Credit Spreads and Bond Yields

## Core Idea
Credit spreads are the difference between a corporate bond's yield and a risk-free government bond of the same maturity. They compensate investors for default risk and credit quality, widening when investor risk appetite declines and narrowing when credit conditions improve.

## How It's Best Learned
Compare yields across bond issuers with different credit ratings and maturities. Track how spreads move during economic downturns versus expansions. Use credit spread data to infer market expectations about default probability.

## Explainer

From bond pricing you know that a bond's yield is the discount rate that equates the present value of its cash flows to its current price — higher risk demands a higher yield to compensate investors. From yield-to-maturity you know how to compute that rate and interpret it as the annualized return if held to maturity. The **credit spread** is the next conceptual step: it isolates the part of a corporate bond's yield that compensates specifically for credit risk, by comparing it to a risk-free benchmark with the same maturity.

Concretely, if a 10-year U.S. Treasury note yields 4.0% and a 10-year investment-grade corporate bond yields 5.2%, the credit spread is 120 **basis points** (1.20 percentage points). That gap represents the market's collective judgment about the additional return required to hold the corporate bond rather than the safe government alternative. The spread incorporates three components: expected default probability, expected loss given default (how much is recovered if the issuer does default), and a **risk premium** for bearing the uncertainty of those outcomes. Even a bond that investors believe will almost certainly be repaid in full must offer a spread because investors demand compensation for the non-zero chance of loss.

Credit spreads are not static — they compress and widen in response to economic conditions, and this movement is itself an important market signal. During recessions or financial stress, spreads widen dramatically as investors demand more compensation for heightened default risk and flee toward safe assets (a "flight to quality"). During expansions, spreads narrow as credit conditions improve and investor confidence rises. The 2008 financial crisis produced historic spread widening; corporate bonds that had traded at 100 basis points over Treasuries suddenly traded at 500 or more. Watching spread dynamics is therefore a real-time indicator of credit market sentiment.

The relationship between credit spread and credit rating is systematic but imperfect. **Investment-grade bonds** (BBB/Baa and above) trade at tighter spreads reflecting low default probability; **high-yield bonds** (below investment grade, sometimes called "junk bonds") trade at much wider spreads reflecting elevated default risk. As an issuer's credit quality deteriorates, its spreads widen — its existing bonds fall in price even without any change in benchmark rates. This is **credit risk** in action: bond prices can fall not because interest rates moved, but because the market's assessment of the issuer's ability to repay has changed. Understanding credit spreads as a priced risk separate from interest rate risk is fundamental to fixed income analysis.
