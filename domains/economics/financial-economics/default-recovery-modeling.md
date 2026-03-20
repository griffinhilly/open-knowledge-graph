---
id: default-recovery-modeling
title: Default Probability and Recovery Rate Estimation
domain: economics
course: financial-economics
prerequisites:
- id: credit-risk-and-default
  type: hard
- id: corporate-bond-credit-spreads
  type: soft
builds-toward: []
tags:
- credit-risk
- default
- recovery
- modeling
stage: formal-systems
status: draft
---
# Default Probability and Recovery Rate Estimation

## Core Idea
Default probability (PD) and loss given default (LGD, or recovery rate R = 1 - LGD) are critical parameters for credit risk management. Expected loss equals PD × LGD × Exposure, and bond yields must compensate for expected losses plus credit risk premium. Recovery rates vary substantially by seniority, collateral, and industry, requiring careful empirical estimation.

## Explainer

From your study of credit risk and default, you know that lenders face two distinct uncertainties when extending credit: will the borrower default, and if so, how much will be recovered? Your study of corporate bond credit spreads showed how these uncertainties are priced into yields. This topic formalizes both components into measurable quantities and shows how they combine into a complete framework for expected credit loss.

**Probability of default (PD)** is the likelihood that a borrower fails to honor a promised payment within a given horizon, typically one year. There are two main estimation approaches. **Structural models** (Merton's approach) treat the firm's equity as a call option on its assets: default occurs when asset value falls below the face value of debt at maturity. This links PD to observable market data — stock price and equity volatility — through options pricing logic. **Reduced-form models** instead estimate a default intensity (hazard rate) directly from market prices of credit instruments, without specifying an economic mechanism for why default occurs. Each approach has tradeoffs: structural models require balance sheet assumptions about unobservable asset values; reduced-form models are more flexible and market-consistent but less transparent about underlying drivers.

**Recovery rate (R)** is the fraction of face value recovered in default; **loss given default (LGD)** = 1 − R is the fraction permanently lost. Empirically, recovery rates vary enormously by position in the capital structure. Secured senior debt historically recovers 60–70 cents on the dollar; junior unsecured bonds recover 30–40 cents; equity recovers close to nothing. Collateral quality and industry matter too — asset-heavy industries like real estate have higher recoveries than service firms with few tangible assets. Crucially, recoveries tend to fall during systemic crises (fire-sale asset values), exactly when defaults are highest. This negative correlation between PD and recovery — both worsening together — means credit portfolios suffer more in downturns than simple averages suggest.

The three components combine into **expected loss (EL) = PD × LGD × Exposure at Default (EAD)**. This formula is the foundation of bank credit risk management and regulatory capital requirements under the Basel accords. A $1 million loan with a 2% annual PD and 40% LGD has an expected annual loss of $8,000. Banks price this expected loss into their lending spreads and hold regulatory capital against it. The **unexpected loss** — the volatility around the expected loss — drives economic capital requirements and depends heavily on correlation: when many borrowers default simultaneously in a downturn, losses cluster and can far exceed the sum of individual expected losses.

Credit spreads connect these parameters to observable bond prices. Under risk-neutral pricing, the credit spread approximately equals PD × LGD for short maturities. This allows you to back out market-implied PDs from bond prices given an assumed recovery rate. In practice, spreads also embed a liquidity premium, so market-implied PDs systematically overstate actual default probabilities — an important caveat when using spread data for empirical credit analysis.
