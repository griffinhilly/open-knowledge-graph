---
id: beta-and-systematic-risk
title: Beta and Systematic Risk
domain: economics
course: financial-economics
prerequisites:
- id: portfolio-diversification
  type: hard
- id: bivariate-regression
  type: soft
- id: correlation-coefficient
  type: soft
builds-toward:
- capital-asset-pricing-model
tags:
- beta
- systematic-risk
- market-risk
- covariance
- capm
stage: formal-systems
status: validated
---

# Beta and Systematic Risk

## Core Idea
Beta (β) measures an asset's sensitivity to market-wide movements — its systematic (non-diversifiable) risk. Formally, β = Cov(rᵢ, rₘ) / Var(rₘ), estimated by regressing historical asset returns on market returns. A beta of 1 means the asset moves in lockstep with the market; beta > 1 amplifies market swings (cyclical or technology stocks); beta < 1 dampens them (utilities, consumer staples); negative beta means the asset tends to move against the market. Because idiosyncratic risk can be freely diversified away, only beta — not total volatility — determines the risk premium in equilibrium.

## How It's Best Learned
Estimate beta by regressing monthly stock returns on index returns over a 5-year window and interpret the slope coefficient. Compare betas across cyclical (high beta) and defensive (low beta) sectors. Understand the Hamada equation relating levered and unlevered beta to see how financial leverage raises beta.

## Common Misconceptions
- A highly volatile stock with low correlation to the market can have low beta — volatility and systematic risk are distinct concepts.
- Beta estimated from historical data is unstable and sensitive to the chosen time window and market proxy, making forward-looking beta a source of significant estimation error.

## Questions

```yaml
- question: "A biotech stock has extremely high daily price volatility because its value depends on clinical trial outcomes uncorrelated with the economic cycle. What would you expect its beta to be?"
  type: multiple-choice
  options:
    - "Very high (beta > 2) because the stock is very risky"
    - "Close to zero, because low correlation to the market produces low beta regardless of total volatility"
    - "Equal to 1, because all stocks must track the market over time"
    - "Negative, because the stock falls when the market rises"
  answer: 1
  explanation: "Beta = Cov(rᵢ, rₘ) / Var(rₘ). If the stock's returns are uncorrelated with the market, Cov(rᵢ, rₘ) ≈ 0, so beta ≈ 0 — despite extremely high total volatility. This is the critical distinction between systematic and idiosyncratic risk. The biotech stock is risky in total, but its risk is firm-specific and diversifiable. A diversified portfolio holder can neutralize this risk, so the market offers no additional return for bearing it."

- question: "Why might a high-volatility stock earn a lower expected return than a lower-volatility stock in an efficient market?"
  type: multiple-choice
  options:
    - "Because high-volatility stocks are more liquid and thus command lower premiums"
    - "Because the market misprices high-volatility stocks, creating arbitrage opportunities"
    - "Because the high-volatility stock's risk may be mostly idiosyncratic and diversifiable, leaving little systematic risk to be rewarded"
    - "Because investors prefer volatile stocks for upside potential and bid up their prices"
  answer: 2
  explanation: "If a stock's volatility comes from firm-specific events uncorrelated with the market, that volatility is idiosyncratic and can be eliminated by holding the stock in a diversified portfolio. Since investors can costlessly diversify it away, the market offers no additional return for bearing it. A stock with lower total volatility but higher beta commands a higher required return because its systematic risk cannot be diversified away. Required return is determined by beta, not raw volatility."

- question: "A highly volatile stock with low correlation to the market can have low beta."
  type: true-false
  answer: true
  explanation: "True — this is one of the most important distinctions in finance. Beta = Cov(rᵢ, rₘ) / Var(rₘ), which depends on correlation with the market, not on total volatility. A stock whose price swings wildly due to firm-specific events (drug trials, patent disputes) can have near-zero beta if those swings are uncorrelated with market movements. High idiosyncratic volatility does not imply high systematic risk."

- question: "A stock with beta = 1.5 is expected to rise about 15% when the overall market rises 10%."
  type: true-false
  answer: true
  explanation: "True. Beta measures sensitivity to market movements: a beta of 1.5 means the stock's returns are expected to move 1.5 times the market's returns. A 10% market gain corresponds to approximately a 15% expected gain; a 10% market decline corresponds to approximately a 15% expected decline. This amplification is why high-beta stocks are considered more exposed to market risk — they swing further in both directions."

- question: "Explain why only systematic risk should command a risk premium in an efficient market, while idiosyncratic risk earns no additional expected return."
  type: short-answer
  answer: "Idiosyncratic risk is firm-specific and uncorrelated across stocks. By holding a diversified portfolio, investors eliminate this risk at virtually no cost — losses in one stock are offset by gains in others. Because investors can freely eliminate idiosyncratic risk, competition bids away any excess return it might offer. Systematic risk affects all stocks simultaneously and cannot be diversified away, so investors must bear it to participate in markets at all — they rationally demand compensation proportional to beta."
  explanation: "The logic: what you can eliminate at no cost, you won't be compensated for; what you cannot eliminate, you must be compensated for. Diversification renders idiosyncratic risk irrelevant for pricing, leaving beta — the undiversifiable component — as the sole driver of expected returns in the CAPM framework. This is why beta, not total volatility (standard deviation), is the relevant risk measure for a diversified investor."
```

## Explainer

From portfolio diversification, you know that combining assets reduces risk — but not all risk goes away. Idiosyncratic risks (a company's CEO resigns, a product fails a safety test, a competitor wins a key contract) wash out when you hold many stocks, because these events are uncorrelated across firms. What cannot be diversified away is **systematic risk**: the risk that moves the whole market at once — recessions, interest rate spikes, geopolitical crises. Every stock is exposed to this background noise, and the question beta answers is: *how exposed?*

Beta is the slope coefficient from regressing an asset's historical returns on the market's returns — precisely the bivariate regression you studied as a prerequisite. If you plot monthly returns of a stock against the S&P 500 over five years, the slope of the best-fit line is beta. A slope of 1 means the asset tracks the market one-for-one: when the market rises 10%, the stock rises about 10%. A beta of 1.5 means the stock amplifies market moves — up 15% when the market rises 10%, down 15% when it falls 10%. A beta of 0.5 means the stock is relatively insulated from market swings. The formally correct expression is β = Cov(rᵢ, rₘ) / Var(rₘ), which from your correlation work you can recognize as the ratio that captures how much of the market's variance the asset shares, normalized by total market variance.

The critical insight — which follows directly from why diversification works — is that only beta, not total volatility, should command a risk premium in a well-functioning market. If a stock has high volatility but low correlation to the market (think: a biotech company whose outcomes depend on drug trial results, not the economic cycle), you can neutralize its idiosyncratic risk by holding it alongside other assets. The market will not pay you extra expected return for bearing risk you could have easily eliminated by diversifying. But systematic risk is unavoidable — no amount of diversification removes it — so investors rationally demand higher expected return to hold high-beta assets. This is the economic logic that CAPM will formalize.

In practice, measuring beta involves several judgment calls. The choice of time window (1 year vs. 5 years), return frequency (daily, weekly, monthly), and market proxy (S&P 500, total market index, global index) all affect the estimate significantly. Furthermore, **beta is not stable**: a company's beta changes as its business mix, leverage, and macro exposure evolve. Financial leverage also mechanically raises beta — the **Hamada equation** shows that levered beta equals unlevered (asset) beta scaled up by (1 + D(1-T)/E), because debt amplifies equity's sensitivity to business fluctuations. For valuation and cost-of-capital work, analysts often "unlever" beta to isolate pure business risk, then re-lever at the target capital structure. This distinction between asset beta and equity beta is essential when comparing firms with different financing structures.
