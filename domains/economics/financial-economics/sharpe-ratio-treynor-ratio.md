---
id: sharpe-ratio-treynor-ratio
title: 'Risk-Adjusted Return Measures: Sharpe and Treynor Ratios'
domain: economics
course: financial-economics
prerequisites:
- id: risk-adjusted-performance-measures
  type: hard
- id: expected-return-and-variance-of-assets
  type: hard
tags:
- performance-measurement
- risk-adjustment
- portfolio-evaluation
stage: advanced
status: draft
---

# Risk-Adjusted Return Measures: Sharpe and Treynor Ratios

## Core Idea
Sharpe ratio = (return − risk-free rate) / volatility measures return per unit of total risk. Treynor ratio = (return − risk-free rate) / beta measures return per unit of systematic risk. Sharpe ratio ranks portfolios for investors with undiversified wealth; Treynor ranks for diversified investors.

## Questions

```yaml
- question: "Fund A has a Sharpe ratio of 0.6 and a Treynor ratio of 0.9. Fund B has a Sharpe ratio of 0.8 and a Treynor ratio of 0.5. A pension fund manager is selecting one fund to add to an already well-diversified multi-manager portfolio. Which fund should she prefer, and why?"
  type: multiple-choice
  options:
    - "Fund B, because its higher Sharpe ratio indicates superior risk-adjusted performance"
    - "Fund A, because its higher Treynor ratio means it delivers more excess return per unit of systematic risk — the relevant risk for a component of a diversified portfolio"
    - "Either fund — both metrics should produce the same ranking for diversified investors"
    - "Fund A, because a lower Sharpe ratio signals lower total volatility, which is always desirable"
  answer: 1
  explanation: "For a portfolio that is one component of a larger diversified portfolio, idiosyncratic risk washes out at the total portfolio level. Only systematic risk (beta) matters. The Treynor ratio measures excess return per unit of beta — exactly the right metric here. Fund A's higher Treynor (0.9 vs. 0.5) means it contributes more return per unit of market risk it adds. Fund B's higher Sharpe reflects better total-risk-adjusted performance — relevant only if Fund B is the investor's entire portfolio."

- question: "An investor holds only a single hedge fund as her entire investment. Which ratio should she use to evaluate it, and why?"
  type: multiple-choice
  options:
    - "Treynor ratio, because systematic risk is what hedge funds specialize in managing"
    - "Both ratios equally — they are interchangeable for concentrated investors"
    - "Sharpe ratio, because she cannot diversify away the fund's idiosyncratic risk — total volatility is the relevant cost"
    - "Neither — hedge funds should be evaluated by absolute return only"
  answer: 2
  explanation: "When a fund represents your entire investment, you bear all of its risk — both idiosyncratic (company-specific) and systematic (market-wide). The Sharpe ratio uses standard deviation (total volatility) as the risk measure, making it appropriate for stand-alone or concentrated allocations. The Treynor ratio uses beta (systematic risk only), which understates the true risk faced by an undiversified investor whose idiosyncratic component cannot be cancelled out."

- question: "Two portfolios with identical Sharpe ratios can have different Treynor ratios."
  type: true-false
  answer: true
  explanation: "Yes — the ratios measure different things. Sharpe uses total standard deviation; Treynor uses beta. A portfolio with high idiosyncratic volatility (high standard deviation) but low market sensitivity (low beta) could have a low Sharpe but a high Treynor. Conversely, a portfolio highly correlated with the market might have high beta relative to its standard deviation, giving a high Sharpe but a low Treynor. The two ratios can produce any relative ranking."

- question: "A portfolio with a higher Sharpe ratio is always a better investment than one with a lower Sharpe ratio."
  type: true-false
  answer: false
  explanation: "The Sharpe ratio is only the right metric for investors who hold the portfolio as their entire investment. For a diversified institutional investor evaluating one sleeve of a multi-asset portfolio, the Treynor ratio is more appropriate — and the Sharpe-superior fund may have a worse Treynor ratio, making it the inferior choice in that context. 'Better' depends on the investor's situation: whether they can diversify away the idiosyncratic risk determines which measure is relevant."

- question: "Explain when the Treynor ratio is more appropriate than the Sharpe ratio, and why the two measures can rank the same set of portfolios differently."
  type: short-answer
  answer: "The Treynor ratio is appropriate when a portfolio is one component of a larger diversified portfolio, so its idiosyncratic risk washes out at the total portfolio level. Only systematic risk (beta) is then relevant. The Sharpe ratio is appropriate when the portfolio represents the investor's entire investment, so total volatility (including idiosyncratic) is the relevant cost. They rank portfolios differently because a fund can have high idiosyncratic risk (raising standard deviation and lowering Sharpe) while having low beta (raising Treynor) — or vice versa."
  explanation: "The core insight is that 'risk' is context-dependent: what risk you bear depends on what else you hold. For a concentrated investor, idiosyncratic risk is real and costly. For a diversified investor, it's irrelevant. Using the wrong metric in the wrong context leads to systematically incorrect portfolio selection — preferring funds that hurt diversified investors or dismissing funds that would complement a diversified portfolio well."
```

## Explainer

From your study of expected returns and variance, you know that raw return is an incomplete measure of investment performance. A portfolio that returns 20% by taking enormous risks is not necessarily better than one returning 12% with minimal volatility. Risk-adjusted return measures are designed to make portfolios comparable by asking: how much return did this portfolio earn per unit of risk it took on? The **Sharpe ratio** and **Treynor ratio** are the two most fundamental answers to that question — and they differ precisely in what they consider "risk."

The **Sharpe ratio** divides the portfolio's excess return (return above the risk-free rate) by the portfolio's standard deviation of returns. The risk-free rate is subtracted because you can earn it without any risk — a good manager must beat that baseline. Standard deviation is used as the risk measure because it captures total volatility: both idiosyncratic (company-specific) risk and systematic (market-wide) risk. A portfolio with a Sharpe ratio of 0.8 earns 0.8 units of excess return per unit of total volatility. The Sharpe ratio is the right measure when you're evaluating a portfolio that represents your **entire** investment — for example, a hedge fund investor who puts all their wealth in one fund, or an endowment evaluating a stand-alone allocation. In these cases, you cannot diversify away the idiosyncratic component, so total volatility is the relevant cost.

The **Treynor ratio** divides excess return by **beta** — the portfolio's sensitivity to the market — rather than by total standard deviation. Beta measures only systematic risk, the part that cannot be diversified away by holding a broad portfolio. The Treynor ratio is appropriate when evaluating a portfolio that is one component of a larger diversified portfolio. If you manage a growth equity sleeve within a larger institutional portfolio, the idiosyncratic risk in that sleeve is diversified away at the total portfolio level. What matters is how much market risk your sleeve contributes — its beta — relative to its excess return. A portfolio can have high standard deviation but low beta (it's volatile in idiosyncratic ways that wash out in a large portfolio), making it look poor on the Sharpe ratio but good on the Treynor ratio.

The practical implication is that the two measures can rank portfolios differently, and both rankings can be correct for different investors. Suppose Fund A has Sharpe 0.6, Treynor 0.9, and Fund B has Sharpe 0.8, Treynor 0.5. A pension fund building a diversified multi-manager portfolio prefers Fund A (higher Treynor); an individual who will hold only this fund prefers Fund B (higher Sharpe). Neither ratio is universally superior — the right measure depends on the investment context. A common mistake is applying the Treynor ratio to an undiversified investor, or the Sharpe ratio to a well-diversified institutional portfolio, and drawing incorrect conclusions about manager skill. Always start by asking: what does this portfolio's risk look like from the perspective of the investor who holds it?
