---
id: credit-risk-and-default
title: Credit Risk and Default Probability
domain: economics
course: financial-economics
prerequisites:
- id: bond-pricing
  type: hard
- id: corporate-bond-credit-spreads
  type: hard
builds-toward:
- value-at-risk-measurement
tags:
- credit
- default
- risk-measurement
stage: formal-systems
status: draft
---

# Credit Risk and Default Probability

## Core Idea
Default probability (PD) and loss given default (LGD) are the core inputs to credit risk modeling. PD can be estimated from historical default rates, bond prices, or equity market signals. Recovery rates vary significantly by seniority and industry. Credit models quantify expected losses and guide portfolio construction.

## How It's Best Learned
Extract implied default probabilities from bond yield spreads and compare to historical default rates for the same rating category. Examine how recovery rates vary by bond seniority.

## Explainer

From bond pricing and credit spreads, you know that corporate bonds trade at higher yields than equivalent Treasury bonds — the difference being the **credit spread**, which compensates investors for the possibility that the issuer won't pay back. Credit risk modeling makes this compensation explicit. The central goal is to quantify *how likely* a borrower is to default and *how much* lenders would lose if they did, so that bonds can be priced correctly and portfolios can be managed responsibly.

The three core inputs to credit risk are **probability of default** (PD), **loss given default** (LGD), and **exposure at default** (EAD). Expected loss is simply their product: EL = PD × LGD × EAD. PD is the likelihood that a borrower fails to make scheduled payments within a given horizon (usually one year). LGD is the fraction of the exposure that the lender actually loses — one minus the recovery rate. EAD is the total outstanding balance at the time of default. A loan with a 2% PD, 40% LGD, and $1 million exposure has an expected loss of $8,000. This calculation drives loan pricing, reserve requirements, and portfolio risk limits at every lending institution.

PD can be estimated in three ways. **Historical rates** use decades of rating-agency data: historically, investment-grade bonds default in under 1% of cases annually, while speculative-grade bonds default at rates of 3–10%+. **Market-implied PD** extracts default probability from the credit spread: a bond trading at a 300 bps spread over the risk-free rate implies a higher default probability than one at 50 bps. The exact relationship requires an assumption about recovery rates — roughly, PD ≈ spread / (1 - recovery rate). This market-based approach is forward-looking and updates in real time, while historical rates are backward-looking but less volatile.

Recovery rates — what creditors get back after default — vary dramatically by **seniority**. Secured senior creditors typically recover 60–80 cents on the dollar; unsecured senior creditors 40–50%; subordinated creditors 20–30%; equity holders often receive nothing. These rates also vary by industry: asset-heavy industries (utilities, real estate) have higher recovery rates than asset-light ones (software, services) because there are more tangible assets to liquidate. Understanding seniority matters for portfolio construction: two bonds with the same PD but different seniority have different LGDs and therefore different expected losses — a fact that gets obscured when analysts focus only on credit ratings without decomposing the risk components.
