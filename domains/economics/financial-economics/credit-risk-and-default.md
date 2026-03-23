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
status: validated
---

# Credit Risk and Default Probability

## Core Idea
Default probability (PD) and loss given default (LGD) are the core inputs to credit risk modeling. PD can be estimated from historical default rates, bond prices, or equity market signals. Recovery rates vary significantly by seniority and industry. Credit models quantify expected losses and guide portfolio construction.

## How It's Best Learned
Extract implied default probabilities from bond yield spreads and compare to historical default rates for the same rating category. Examine how recovery rates vary by bond seniority.

## Questions

```yaml
- question: "An analyst evaluates two corporate bonds, both rated BB by the same rating agency, both with a 5% annual probability of default. The analyst weights them equally in a credit portfolio. What critical factor is the analyst likely ignoring?"
  type: multiple-choice
  options:
    - "The bonds may have different maturities, which affects duration risk but not credit expected loss"
    - "BB-rated bonds always have identical recovery rates within the same rating category"
    - "The bonds may have different seniority levels, which affects loss given default (LGD) and therefore expected losses even with equal PD"
    - "Expected loss only depends on PD; recovery rates are a separate accounting concern"
  answer: 2
  explanation: "Expected loss = PD × LGD × EAD. Two bonds with identical PD but different seniority have very different LGDs: senior secured creditors typically recover 60–80 cents on the dollar, while subordinated creditors recover 20–30 cents. A BB-rated senior secured bond and a BB-rated subordinated bond have the same probability of default but dramatically different expected losses. Focusing only on credit ratings without decomposing PD and LGD leads to mispriced portfolios."

- question: "A corporate bond's credit spread widens from 80 basis points to 300 basis points over a single month, while the company's rating-agency historical default rate for that rating category remains unchanged. What happens to the market-implied probability of default?"
  type: multiple-choice
  options:
    - "It stays unchanged — market-implied PD tracks historical default rates by definition"
    - "It increases — market-implied PD is derived from the credit spread and updates in real time as spreads change"
    - "It decreases — wider spreads indicate that investors demand more compensation, suggesting lower risk"
    - "It becomes undefined — market-implied PD cannot be compared to historical PD because they measure different things"
  answer: 1
  explanation: "Market-implied PD is extracted from the credit spread using the approximation PD ≈ spread / (1 - recovery rate). As the spread widens from 80 to 300 bps, the market-implied PD rises proportionally. This is precisely the forward-looking advantage of market-implied PD: it updates in real time as market participants reassess default risk, while historical rating-agency default rates are backward-looking averages that change slowly. The two measures can diverge significantly during periods of market stress."

- question: "A secured senior bondholder typically recovers a higher fraction of their investment after a default than an unsecured subordinated bondholder, because seniority determines the order of claims on the defaulting firm's assets."
  type: true-false
  answer: true
  explanation: "Seniority governs the waterfall of claims in bankruptcy: secured senior creditors are paid first (typically recovering 60–80 cents on the dollar), followed by unsecured senior creditors (40–50 cents), then subordinated creditors (20–30 cents), with equity holders often receiving nothing. This ordering is why LGD differs systematically by seniority: higher seniority means lower LGD (higher recovery), which means lower expected loss even at the same PD."

- question: "Market-implied default probabilities are always preferable to historical default rates because they are more accurate and forward-looking."
  type: true-false
  answer: false
  explanation: "Market-implied PD has the advantage of being forward-looking and updating in real time — it reflects current market sentiment about default risk. But it is also volatile, can be distorted by liquidity premiums and risk aversion (spreads can widen due to market fear, not just actual default risk), and requires assumptions about recovery rates to compute. Historical default rates are backward-looking and slower to update, but they are more stable and based on actual observed defaults. Neither is universally superior — analysts use both, recognizing their complementary strengths and limitations."

- question: "Explain why two bonds with the same credit rating and the same probability of default can have different expected losses, and identify the key factor that explains the difference."
  type: short-answer
  answer: "Expected loss = PD × LGD × EAD. If two bonds have the same PD and the same exposure (EAD), expected loss still differs if LGD differs. LGD equals one minus the recovery rate, and recovery rates vary significantly by seniority: senior secured bonds recover 60–80% while subordinated bonds recover 20–30%. A BB-rated senior secured bond and a BB-rated subordinated bond have the same PD but very different expected losses. Seniority is the key factor — it determines how much lenders actually lose in a default, which is what LGD captures."
  explanation: "This is one of the most practically important insights in credit analysis. Credit ratings summarize default probability but do not fully capture expected loss, because they do not indicate seniority or recovery rates. Portfolio managers and loan pricers must decompose credit risk into its three components (PD, LGD, EAD) rather than relying on ratings alone. Two bonds with the same rating can have very different risk profiles depending on where they sit in the capital structure."
```

## Explainer

From bond pricing and credit spreads, you know that corporate bonds trade at higher yields than equivalent Treasury bonds — the difference being the **credit spread**, which compensates investors for the possibility that the issuer won't pay back. Credit risk modeling makes this compensation explicit. The central goal is to quantify *how likely* a borrower is to default and *how much* lenders would lose if they did, so that bonds can be priced correctly and portfolios can be managed responsibly.

The three core inputs to credit risk are **probability of default** (PD), **loss given default** (LGD), and **exposure at default** (EAD). Expected loss is simply their product: EL = PD × LGD × EAD. PD is the likelihood that a borrower fails to make scheduled payments within a given horizon (usually one year). LGD is the fraction of the exposure that the lender actually loses — one minus the recovery rate. EAD is the total outstanding balance at the time of default. A loan with a 2% PD, 40% LGD, and $1 million exposure has an expected loss of $8,000. This calculation drives loan pricing, reserve requirements, and portfolio risk limits at every lending institution.

PD can be estimated in three ways. **Historical rates** use decades of rating-agency data: historically, investment-grade bonds default in under 1% of cases annually, while speculative-grade bonds default at rates of 3–10%+. **Market-implied PD** extracts default probability from the credit spread: a bond trading at a 300 bps spread over the risk-free rate implies a higher default probability than one at 50 bps. The exact relationship requires an assumption about recovery rates — roughly, PD ≈ spread / (1 - recovery rate). This market-based approach is forward-looking and updates in real time, while historical rates are backward-looking but less volatile.

Recovery rates — what creditors get back after default — vary dramatically by **seniority**. Secured senior creditors typically recover 60–80 cents on the dollar; unsecured senior creditors 40–50%; subordinated creditors 20–30%; equity holders often receive nothing. These rates also vary by industry: asset-heavy industries (utilities, real estate) have higher recovery rates than asset-light ones (software, services) because there are more tangible assets to liquidate. Understanding seniority matters for portfolio construction: two bonds with the same PD but different seniority have different LGDs and therefore different expected losses — a fact that gets obscured when analysts focus only on credit ratings without decomposing the risk components.
