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
stage: advanced
status: validated
---

# Cost of Equity and CAPM Application

## Core Idea
CAPM estimates the cost of equity as r_e = r_f + β(r_m − r_f), where r_f is risk-free rate, β is systematic risk, and (r_m − r_f) is equity risk premium. This discount rate reflects only the risk that cannot be diversified away.

## How It's Best Learned
Estimate beta for a stock using regression. Then calculate cost of equity using historical and forward-looking risk premiums. Compare across industries to validate reasonableness.

## Questions

```yaml
- question: "Firm A is a small mining startup with highly volatile returns — its total return variance is very high. However, its returns are completely uncorrelated with the market (beta ≈ 0). According to CAPM, what is Firm A's cost of equity?"
  type: multiple-choice
  options:
    - "High — investors require extra compensation for the high total volatility they bear"
    - "Approximately equal to the risk-free rate — uncorrelated risk earns no market premium under CAPM"
    - "Equal to the market return — all equity carries the market premium regardless of correlation"
    - "Undefined — CAPM cannot price assets with idiosyncratic volatility"
  answer: 1
  explanation: "Under CAPM, only systematic (market-correlated) risk is priced. Firm A's high total variance is entirely idiosyncratic (unsystematic) — it could be eliminated by an investor who holds a diversified portfolio. Because diversification is free in competitive markets, rational investors will not demand extra compensation for risk they can eliminate. With beta ≈ 0, the CAPM formula gives r_e ≈ r_f + 0·(r_m − r_f) = r_f. This result seems counterintuitive — a volatile startup requires no equity premium? — but the logic is rigorous: the risk premium compensates only for what cannot be diversified away."

- question: "A utility company has beta = 0.4 and a tech startup has beta = 2.2. The risk-free rate is 4% and the equity risk premium is 6%. What is each company's cost of equity, and what does the difference reflect economically?"
  type: multiple-choice
  options:
    - "Utility: 6.4%, Tech: 17.2% — the difference reflects total business risk"
    - "Utility: 6.4%, Tech: 17.2% — the difference reflects only systematic risk exposure, not total volatility"
    - "Both 10% — CAPM applies the same market return to all equity"
    - "Utility: 4%, Tech: 4% — both earn the risk-free rate since equity risk can be diversified"
  answer: 1
  explanation: "Utility: r_e = 4% + 0.4(6%) = 4% + 2.4% = 6.4%. Tech: r_e = 4% + 2.2(6%) = 4% + 13.2% = 17.2%. The 10.8 percentage point difference reflects systematic risk only — how much each stock's returns move with the overall market. The utility's revenues are stable regardless of economic cycles (low beta); the startup's returns are highly amplified by market conditions (high beta). Both firms likely have high total volatility, but investors in the utility face little undiversifiable risk. The CAPM cost of equity measures only the compensation for that undiversifiable portion."

- question: "Under CAPM, a stock with very high total return volatility but low beta should have a high cost of equity, because investors are exposed to substantial uncertainty."
  type: true-false
  answer: false
  explanation: "Total volatility includes both systematic and unsystematic components. CAPM prices only the systematic component (captured by beta), because unsystematic risk can be eliminated through diversification at no cost. A stock with high total volatility but low correlation with the market has mostly unsystematic risk — the kind a diversified investor has already neutralized in their portfolio. CAPM says the market will not compensate for risk you can eliminate yourself for free. High total volatility with low beta → low CAPM cost of equity."

- question: "Beta measures a stock's total return variability, which is why highly volatile stocks always have high betas and high costs of equity."
  type: true-false
  answer: false
  explanation: "Beta measures a stock's sensitivity to market movements — specifically, the covariance of the stock's returns with market returns, divided by the variance of market returns. It captures systematic (co-movement) risk, not total variability. A stock can have very high total variance (high absolute volatility) but low beta if its volatility is driven by firm-specific events uncorrelated with the market. For example, a small biotech whose returns swing wildly based on clinical trial outcomes may have a low beta if those outcomes are independent of overall market conditions."

- question: "Why does CAPM only compensate investors for systematic risk and not for unsystematic (firm-specific) risk, and what assumption makes this true?"
  type: short-answer
  answer: "CAPM assumes investors hold diversified portfolios. In a diversified portfolio, unsystematic (firm-specific) risks — individual company events, CEO changes, product failures — cancel out across many holdings. Because diversification is available to any investor, competitive markets will not reward bearing a risk that can be freely eliminated. Only systematic risk — the portion that co-moves with the entire market and cannot be diversified away even in a perfectly diversified portfolio — demands a risk premium. Beta measures exactly this undiversifiable exposure: stocks that amplify market swings (high beta) impose uncompensable risk on every investor; stocks that are insensitive to the market (low beta) do not."
  explanation: "The key assumption is that investors can costlessly diversify. In practice, transaction costs, illiquidity, and constraints on portfolio construction mean some investors do bear unsystematic risk. This is one reason CAPM is an idealization — real-world asset pricing shows that factors beyond beta (size, value, momentum) seem to earn premiums, suggesting the market does partially price some 'diversifiable' risks. But CAPM's core insight — that only co-movement with the market should earn a premium in a competitive, frictionless setting — remains the foundation of modern cost-of-capital estimation."
```

## Explainer

When a firm needs to raise equity capital, it cannot simply look up an interest rate — there is no promised repayment, so there is no contractual rate. Instead, equity investors require a return that compensates them for the risk they bear. The **cost of equity** is that required return: the minimum return a firm must earn on equity-financed investments to leave shareholders no worse off. CAPM gives you the formula for it: r_e = r_f + β(r_m − r_f). Each component has economic meaning grounded in your prerequisite concepts.

The **risk-free rate** r_f is the return available with certainty — typically the yield on short-term government securities. The **equity risk premium** (r_m − r_f) is the additional return investors demand for holding the entire market portfolio instead of the risk-free asset — the premium for bearing systematic risk in aggregate. You already know from your systematic/unsystematic risk prerequisite that diversification eliminates unsystematic (firm-specific) risk entirely. Rational investors in competitive markets are not compensated for risk they could diversify away for free. The only risk priced is the systematic risk that cannot be diversified — the portion of a stock's risk that moves with the market.

Beta captures exactly this undiversifiable exposure. A beta of 1.3 means the stock moves about 1.3% for every 1% move in the market — it amplifies market risk. Multiplying beta by the equity risk premium scales the market premium to reflect this stock's specific systematic exposure. A utility stock with beta of 0.5 demands a cost of equity roughly halfway between the risk-free rate and the market return; a biotech company with beta of 2.0 demands twice the market premium above the risk-free rate. The formula is nothing more than: start at the safe rate, then add compensation proportional to how much systematic risk you are asking equity holders to bear.

In practice, estimating the cost of equity requires judgment at each step. Beta is typically estimated by regressing the stock's excess returns on market excess returns over 3–5 years of monthly data — a noisy estimate, often supplemented by industry averages or Bayesian shrinkage toward 1. The equity risk premium is debated: historical estimates (US market premium over T-bills since 1926 is roughly 5–7%) may not reflect the forward-looking premium. Survey-based or model-implied ERP estimates range widely. The result feeds directly into the **weighted average cost of capital** and **DCF valuation**: since all equity cash flows get discounted at r_e, a small change in beta or ERP assumptions can change an enterprise valuation by 20–30%. This sensitivity is why professional analysts run cost-of-equity estimates as a range and subject them to explicit scenario analysis rather than treating a single CAPM estimate as a precise number.
