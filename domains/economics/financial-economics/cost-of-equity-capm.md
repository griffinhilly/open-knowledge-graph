---
id: cost-of-equity-capm
title: Cost of Equity and CAPM Application
domain: economics
course: financial-economics
prerequisites:
- id: capital-asset-pricing-model
  type: hard
- id: equity-risk-premium
  type: hard
- id: systematic-unsystematic-risk
  type: hard
builds-toward:
- weighted-average-cost-of-capital
- free-cash-flow-dcf-valuation
tags:
- capm
- discount-rate
- equity-valuation
stage: formal-systems
status: draft
---

# Cost of Equity and CAPM Application

## Core Idea
CAPM estimates the cost of equity as r_e = r_f + β(r_m − r_f), where r_f is risk-free rate, β is systematic risk, and (r_m − r_f) is equity risk premium. This discount rate reflects only the risk that cannot be diversified away.

## How It's Best Learned
Estimate beta for a stock using regression. Then calculate cost of equity using historical and forward-looking risk premiums. Compare across industries to validate reasonableness.

## Explainer

When a firm needs to raise equity capital, it cannot simply look up an interest rate — there is no promised repayment, so there is no contractual rate. Instead, equity investors require a return that compensates them for the risk they bear. The **cost of equity** is that required return: the minimum return a firm must earn on equity-financed investments to leave shareholders no worse off. CAPM gives you the formula for it: r_e = r_f + β(r_m − r_f). Each component has economic meaning grounded in your prerequisite concepts.

The **risk-free rate** r_f is the return available with certainty — typically the yield on short-term government securities. The **equity risk premium** (r_m − r_f) is the additional return investors demand for holding the entire market portfolio instead of the risk-free asset — the premium for bearing systematic risk in aggregate. You already know from your systematic/unsystematic risk prerequisite that diversification eliminates unsystematic (firm-specific) risk entirely. Rational investors in competitive markets are not compensated for risk they could diversify away for free. The only risk priced is the systematic risk that cannot be diversified — the portion of a stock's risk that moves with the market.

Beta captures exactly this undiversifiable exposure. A beta of 1.3 means the stock moves about 1.3% for every 1% move in the market — it amplifies market risk. Multiplying beta by the equity risk premium scales the market premium to reflect this stock's specific systematic exposure. A utility stock with beta of 0.5 demands a cost of equity roughly halfway between the risk-free rate and the market return; a biotech company with beta of 2.0 demands twice the market premium above the risk-free rate. The formula is nothing more than: start at the safe rate, then add compensation proportional to how much systematic risk you are asking equity holders to bear.

In practice, estimating the cost of equity requires judgment at each step. Beta is typically estimated by regressing the stock's excess returns on market excess returns over 3–5 years of monthly data — a noisy estimate, often supplemented by industry averages or Bayesian shrinkage toward 1. The equity risk premium is debated: historical estimates (US market premium over T-bills since 1926 is roughly 5–7%) may not reflect the forward-looking premium. Survey-based or model-implied ERP estimates range widely. The result feeds directly into the **weighted average cost of capital** and **DCF valuation**: since all equity cash flows get discounted at r_e, a small change in beta or ERP assumptions can change an enterprise valuation by 20–30%. This sensitivity is why professional analysts run cost-of-equity estimates as a range and subject them to explicit scenario analysis rather than treating a single CAPM estimate as a precise number.
