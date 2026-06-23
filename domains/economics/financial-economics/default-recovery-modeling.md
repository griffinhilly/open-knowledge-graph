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
- id: credit-analysis-bond-selection
  type: soft
builds-toward: []
tags:
- credit-risk
- default
- recovery
- modeling
stage: formal-systems
status: validated
---
# Default Probability and Recovery Rate Estimation

## Core Idea
Default probability (PD) and loss given default (LGD, or recovery rate R = 1 - LGD) are critical parameters for credit risk management. Expected loss equals PD × LGD × Exposure, and bond yields must compensate for expected losses plus credit risk premium. Recovery rates vary substantially by seniority, collateral, and industry, requiring careful empirical estimation.

## Questions

```yaml
- question: "A corporate bond yields 5% while a risk-free Treasury of the same maturity yields 2%, implying a credit spread of 3%. An analyst concludes that the market-implied default probability is 3%. Why is this likely an overestimate?"
  type: multiple-choice
  options:
    - "Credit spreads undercount default probability because they don't include LGD"
    - "Credit spreads embed a liquidity premium on top of expected loss, inflating the implied PD beyond the actual default probability"
    - "Treasury yields already include a credit component, so the spread is not a pure default signal"
    - "Default probability can only be estimated from equity prices, not bond prices"
  answer: 1
  explanation: "Under risk-neutral pricing, credit spread ≈ PD × LGD for short maturities. But observed spreads also include a liquidity premium — investors demand extra yield for holding less liquid instruments, regardless of default risk. This means the spread is higher than expected loss alone, so backing out PD from the spread produces an overestimate of actual default probability. In practice, market-implied PDs from bond spreads are systematically higher than historically realized default rates, partly for this reason."

- question: "A bank has a $2 million loan outstanding. The borrower has a 5% annual probability of default, and the bank expects to recover 40% of the loan if default occurs. What is the expected annual credit loss?"
  type: multiple-choice
  options:
    - "$60,000"
    - "$100,000"
    - "$40,000"
    - "$4,000"
  answer: 0
  explanation: "Expected Loss = PD × LGD × EAD. LGD = 1 − recovery rate = 1 − 0.40 = 0.60. EL = 0.05 × 0.60 × $2,000,000 = $60,000. Note that option B ($100,000) is the result of using 5% × $2M, ignoring recovery — a common error that conflates PD with loss rate. Banks price this $60,000 expected loss into their lending spread and hold regulatory capital for it."

- question: "During a severe economic downturn, default rates and recovery rates tend to move in opposite directions — as defaults rise, recoveries fall — amplifying credit losses beyond what simple expected-loss calculations predict."
  type: true-false
  answer: true
  explanation: "This negative correlation between PD and recovery is one of the most important (and most often underestimated) features of credit risk. In a crisis, more borrowers default simultaneously AND assets are sold at fire-sale prices, reducing recovery values. A bank that calculated EL = PD × LGD using average historical values for each separately would understate crisis losses because those averages apply to normal times. The positive correlation of losses across borrowers (systematic risk) combined with this PD/recovery correlation is why bank capital requirements must account for concentration risk and systemic scenarios."

- question: "Market-implied default probabilities derived from credit spreads tend to underestimate actual default probabilities because bond investors are overly optimistic."
  type: true-false
  answer: false
  explanation: "The direction is reversed. Market-implied PDs derived from credit spreads tend to *overestimate* actual default probabilities. This is because credit spreads include a liquidity premium — extra yield demanded for illiquidity — in addition to compensation for expected loss. When you back out PD from a spread assuming it reflects only default risk, the PD is inflated. Empirically, realized default rates are typically well below market-implied PDs from spreads, especially for investment-grade bonds where liquidity premiums are proportionally large."

- question: "Explain why using the formula EL = PD × LGD × EAD to estimate a credit portfolio's total expected loss may significantly understate actual losses during a financial crisis."
  type: short-answer
  answer: "Two reasons compound: (1) PD and recovery rates are negatively correlated in crises — both worsen simultaneously. Using average PD and average LGD from normal times misses this. (2) Defaults cluster — many borrowers default together in a systemic shock, meaning portfolio losses are correlated, not independent. The formula gives each loan's expected loss correctly but treating them as independent ignores correlation, which drives unexpected portfolio-level losses far above the sum of individual ELs."
  explanation: "The formula EL = PD × LGD × EAD is accurate for a single loan in normal times. The problem at the portfolio level is correlation: if a recession causes 10 borrowers to all default at once, the portfolio loss isn't 10 × EL (individual) — it's much higher than what the formula implies when applied independently to each loan. This is why regulatory frameworks (Basel) require banks to hold capital for unexpected losses (the variance around EL) not just expected losses, and why stress testing under correlated adverse scenarios is essential for sound credit risk management."
```

## Explainer

From your study of credit risk and default, you know that lenders face two distinct uncertainties when extending credit: will the borrower default, and if so, how much will be recovered? Your study of corporate bond credit spreads showed how these uncertainties are priced into yields. This topic formalizes both components into measurable quantities and shows how they combine into a complete framework for expected credit loss.

**Probability of default (PD)** is the likelihood that a borrower fails to honor a promised payment within a given horizon, typically one year. There are two main estimation approaches. **Structural models** (Merton's approach) treat the firm's equity as a call option on its assets: default occurs when asset value falls below the face value of debt at maturity. This links PD to observable market data — stock price and equity volatility — through options pricing logic. **Reduced-form models** instead estimate a default intensity (hazard rate) directly from market prices of credit instruments, without specifying an economic mechanism for why default occurs. Each approach has tradeoffs: structural models require balance sheet assumptions about unobservable asset values; reduced-form models are more flexible and market-consistent but less transparent about underlying drivers.

**Recovery rate (R)** is the fraction of face value recovered in default; **loss given default (LGD)** = 1 − R is the fraction permanently lost. Empirically, recovery rates vary enormously by position in the capital structure. Secured senior debt historically recovers 60–70 cents on the dollar; junior unsecured bonds recover 30–40 cents; equity recovers close to nothing. Collateral quality and industry matter too — asset-heavy industries like real estate have higher recoveries than service firms with few tangible assets. Crucially, recoveries tend to fall during systemic crises (fire-sale asset values), exactly when defaults are highest. This negative correlation between PD and recovery — both worsening together — means credit portfolios suffer more in downturns than simple averages suggest.

The three components combine into **expected loss (EL) = PD × LGD × Exposure at Default (EAD)**. This formula is the foundation of bank credit risk management and regulatory capital requirements under the Basel accords. A $1 million loan with a 2% annual PD and 40% LGD has an expected annual loss of $8,000. Banks price this expected loss into their lending spreads and hold regulatory capital against it. The **unexpected loss** — the volatility around the expected loss — drives economic capital requirements and depends heavily on correlation: when many borrowers default simultaneously in a downturn, losses cluster and can far exceed the sum of individual expected losses.

Credit spreads connect these parameters to observable bond prices. Under risk-neutral pricing, the credit spread approximately equals PD × LGD for short maturities. This allows you to back out market-implied PDs from bond prices given an assumed recovery rate. In practice, spreads also embed a liquidity premium, so market-implied PDs systematically overstate actual default probabilities — an important caveat when using spread data for empirical credit analysis.
