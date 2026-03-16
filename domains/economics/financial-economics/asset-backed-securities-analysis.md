---
id: asset-backed-securities-analysis
title: Asset-Backed Securities and Securitization Analysis
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: credit-risk-and-default
  type: soft
builds-toward:
- default-recovery-modeling
tags:
- securitization
- abs
- mortgages
- credit-risk
stage: formal-systems
status: draft
---

# Asset-Backed Securities and Securitization Analysis

## Core Idea
Securitization pools cash-flowing assets (mortgages, auto loans, receivables) into tranched securities with different risk priorities. Senior tranches have priority in receiving payments and thus lower credit risk; junior and equity tranches absorb losses first. ABS valuation requires modeling prepayment risk, default rates, and recovery rates, which depend critically on macroeconomic conditions and portfolio composition.

## Explainer

From bond pricing, you know how to value a fixed stream of cash flows: discount each payment at the appropriate risk-adjusted rate. Asset-backed securities extend this framework, but with a twist — the cash flows themselves are uncertain. A mortgage-backed security, for example, represents a claim on monthly principal and interest payments from hundreds or thousands of homeowners. These payments can stop (default) or accelerate (prepayment when homeowners refinance), making the timing and size of cash flows stochastic. Securitization is the process of packaging these uncertain claims into marketable bonds.

The central innovation of securitization is **tranching** — the waterfall structure that allocates cash flows and losses in a predetermined priority order. Imagine a pool of 1,000 mortgages generating monthly cash flows. The **senior tranche** is paid first from these flows and absorbs losses last; if only 10% of mortgages default, the senior tranche might be fully protected. The **junior (mezzanine) tranche** is paid next and absorbs losses after the equity tranche is wiped out. The **equity (residual) tranche** is paid last and absorbs the first losses. By subordinating lower tranches, the structure transforms a pool of risky assets into securities with a range of credit profiles — the senior tranche can be rated AAA even if the underlying mortgages are subprime.

Valuing an ABS requires three key inputs beyond standard bond pricing. **Prepayment risk** is the possibility that borrowers repay early — often because interest rates fall and they refinance. Prepayment is modeled using the **PSA (Public Securities Association) prepayment speed** convention, which measures prepayments as a percentage of a standard benchmark. Early prepayment shortens the security's duration and can hurt investors who paid a premium expecting longer cash flows. **Default rates** estimate what fraction of the underlying borrowers will fail to pay, typically modeled using historical loss curves and macroeconomic scenarios. **Recovery rates** estimate how much is recouped after default through collateral liquidation (e.g., foreclosure on the house).

The 2008 financial crisis revealed how these models can fail catastrophically. Rating agencies assumed home prices could not fall nationally, making their default and recovery models drastically overoptimistic for subprime MBS. Senior tranches rated AAA were, in reality, much riskier than their ratings implied because the underlying assumptions were wrong and correlations across the pool were far higher than assumed — when housing fell, defaults spiked everywhere simultaneously. This experience established that ABS analysis must stress-test correlation assumptions: diversification across a portfolio of loans only protects you if defaults are uncorrelated, but macroeconomic shocks can make them highly correlated at exactly the wrong moment.
