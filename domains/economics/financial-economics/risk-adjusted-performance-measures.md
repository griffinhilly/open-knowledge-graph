---
id: risk-adjusted-performance-measures
title: Risk-Adjusted Performance Measures
domain: economics
course: financial-economics
prerequisites:
- id: capital-asset-pricing-model
  type: hard
- id: efficient-frontier-portfolio-theory
  type: hard
- id: arbitrage-pricing-theory
  type: soft
- id: market-anomalies-and-puzzles
  type: soft
tags:
- sharpe-ratio
- jensen-alpha
- treynor-ratio
- performance-evaluation
- alpha
stage: advanced
status: validated
---
# Risk-Adjusted Performance Measures

## Core Idea
Risk-adjusted performance measures evaluate whether a portfolio's returns are commensurate with the risk taken. The Sharpe ratio = (rp − rₓ) / σp measures return per unit of total risk and is appropriate when the portfolio represents an investor's entire wealth. Jensen's alpha = actual return − CAPM-predicted return measures excess return above what the portfolio's beta predicts — positive alpha is the goal of active management. The Treynor ratio uses beta rather than total volatility in the denominator, appropriate when the portfolio is a component of a larger diversified position. These measures are used to identify genuine manager skill, to attribute performance to factor exposures vs. true alpha, and to determine whether active management fees are justified.

## How It's Best Learned
Calculate Sharpe ratio and Jensen's alpha for a real actively managed mutual fund over a 10-year period and compare to a passive index. Understand why a fund can have positive alpha on a CAPM basis but negative alpha once Fama-French factors are added. Note that any strategy with optionlike features (selling volatility) can artificially inflate its Sharpe ratio.

## Common Misconceptions
- Positive alpha is not proof of manager skill — it may reflect luck, benchmark misspecification, or undisclosed exposure to risk factors not included in the pricing model.
- The Sharpe ratio implicitly assumes normally distributed returns; strategies that sell options or take on tail risk can display high Sharpe ratios right up until a catastrophic loss.

## Questions

```yaml
- question: "A hedge fund has reported a Sharpe ratio of 2.5 for five consecutive years by systematically selling out-of-the-money put options (collecting premiums when markets are calm). Why might this Sharpe ratio be misleading?"
  type: multiple-choice
  options:
    - "Options strategies are exempt from CAPM analysis, making the Sharpe ratio inapplicable"
    - "The Sharpe ratio uses beta in the denominator, which options strategies artificially inflate"
    - "The strategy exhibits low measured volatility but carries large tail risk — rare catastrophic losses that don't appear in historical standard deviation until they occur"
    - "A Sharpe ratio above 2.0 is mathematically impossible with normal return distributions"
  answer: 2
  explanation: "Selling options generates steady income with low observed volatility — until a crash materializes and the short puts are deeply in-the-money. The Sharpe ratio uses historical standard deviation (σ) in the denominator, which is low during calm periods. This inflates the ratio right up until a catastrophic loss event, which is precisely when the strategy's true risk reveals itself. This is a classic example of the Sharpe ratio's limitation: it implicitly assumes normally distributed returns and misses strategies with negative skewness and fat left tails. Option B is wrong — the Sharpe ratio uses σ, not beta."

- question: "Two managers each run a sub-portfolio within a large diversified pension fund. Manager A: Sharpe ratio 0.6, Treynor ratio 0.10. Manager B: Sharpe ratio 0.9, Treynor ratio 0.06. Which manager added more value to the pension fund?"
  type: multiple-choice
  options:
    - "Manager B — a higher Sharpe ratio always indicates better risk-adjusted performance"
    - "Manager A — the Treynor ratio is the correct measure for sub-portfolios, and Manager A's is higher"
    - "They are equivalent — both ratios must agree for a valid comparison"
    - "Cannot determine without knowing their Jensen's alphas relative to the fund's benchmark"
  answer: 1
  explanation: "When a portfolio is one component of a larger diversified holding, idiosyncratic risk diversifies away in context. Only systematic risk (beta) matters for evaluating that sub-portfolio's contribution. The Treynor ratio uses beta in the denominator for exactly this reason. Manager A's higher Treynor ratio means they delivered more excess return per unit of systematic risk — the relevant measure. Manager B's higher Sharpe ratio reflects lower total volatility, but that idiosyncratic volatility is irrelevant when it's a sleeve within a diversified fund. Choosing the wrong measure leads to rewarding the wrong manager."

- question: "A fund reporting positive Jensen's alpha relative to a CAPM benchmark has definitively demonstrated manager skill."
  type: true-false
  answer: false
  explanation: "Positive CAPM alpha is necessary but not sufficient evidence of skill. It may instead reflect exposure to well-known priced factors — size (small-cap premium), value (HML), momentum, or profitability — that the one-factor CAPM benchmark doesn't capture. A strategy that simply buys small-cap value stocks would show positive CAPM alpha in many periods, but that alpha disappears when evaluated against a Fama-French multi-factor model. True alpha requires that excess returns persist after accounting for all known systematic risk factors, and even then, it could reflect luck over the evaluation period."

- question: "The Treynor ratio is more appropriate than the Sharpe ratio for evaluating a sub-portfolio within a larger diversified fund, because only systematic risk (beta) is relevant in that context."
  type: true-false
  answer: true
  explanation: "This is the key contextual principle for choosing between these measures. The Sharpe ratio is appropriate when the portfolio in question represents the investor's entire wealth — there is no larger portfolio to absorb its idiosyncratic risk. When the portfolio is a sleeve within a larger diversified fund, the fund-level diversification eliminates idiosyncratic volatility, leaving only systematic risk as the relevant cost. The Treynor ratio correctly charges only for that remaining systematic risk. Using Sharpe in this context penalizes managers whose portfolios happen to be more volatile even if that volatility adds no systematic risk."

- question: "Why might a fund that shows positive Jensen's alpha versus a simple market-beta benchmark show zero or negative alpha when evaluated against a Fama-French multi-factor model?"
  type: short-answer
  answer: "CAPM uses only market beta to predict expected return. If the fund loads heavily on known priced factors — small-cap stocks (size premium), cheap stocks (value premium), or past winners (momentum premium) — those factor exposures generate returns that CAPM incorrectly attributes to skill. When the Fama-French model explicitly controls for size, value, and momentum factors, those returns are correctly identified as compensation for systematic factor risk, not alpha. Only the residual return unexplained by all known factors counts as true alpha."
  explanation: "This is why professional performance attribution increasingly decomposes returns into factor exposures versus residual alpha. The practical implication is that apparent alpha against a simple benchmark invites the question: 'What systematic risk is this strategy exposed to that my benchmark doesn't capture?' If the answer is 'exposure to size and value,' the manager hasn't generated alpha — they've constructed a factor portfolio without disclosing it as such."
```

## Explainer

From your study of the efficient frontier, you know that investors care about both return and risk — that a higher return is not automatically better if it comes with proportionally higher risk. From CAPM, you know that the only risk that earns a premium is systematic risk, measured by beta. Risk-adjusted performance measures translate these ideas into tools for evaluating whether a portfolio — or a manager — has actually earned its returns relative to the risk taken.

The **Sharpe ratio** is the most widely used measure: (r_p − r_f) / σ_p. It asks how much excess return (above the risk-free rate) you received per unit of total volatility. A Sharpe ratio of 0.8 means the portfolio earned 0.8 percentage points of excess return for each 1% of standard deviation. When comparing two portfolios of similar asset classes, the one with the higher Sharpe ratio delivered better risk-adjusted performance. Crucially, the Sharpe ratio uses total risk (σ_p), making it appropriate when the portfolio under evaluation represents the investor's entire wealth — there is no larger portfolio absorbing its idiosyncratic risk.

**Jensen's alpha** takes a different approach rooted in CAPM. CAPM predicts what a portfolio *should* return given its beta: E(r_p) = r_f + β_p(r_m − r_f). Alpha is the actual return minus this CAPM-predicted return. Positive alpha means the manager generated return above what compensation for systematic risk alone would predict — which is the goal of every active manager. If a fund has β = 1.2 and the market earned 10%, the fund should have earned roughly r_f + 1.2(10% − r_f). If it actually earned more than that, the difference is alpha. Alpha is the right metric when you want to isolate genuine skill from leverage or systematic factor exposure — a fund that simply buys high-beta stocks in a rising market earns no alpha even with stellar raw returns.

The **Treynor ratio** = (r_p − r_f) / β_p uses beta in the denominator instead of total volatility. This is appropriate when the portfolio is one component of a larger diversified holding — the idiosyncratic risk of this sub-portfolio diversifies away in context, so only systematic risk matters. A manager running a tech sleeve within a diversified pension fund should be evaluated on Treynor, not Sharpe.

All three measures share a critical vulnerability: they are only as good as the risk model used to define "expected return." Jensen's alpha against CAPM looks very different from alpha against a Fama-French five-factor model. Many strategies that appear to generate alpha versus a simple market-beta benchmark are simply loading on well-known priced factors — size, value, momentum, profitability — that the benchmark missed. This is why professional performance attribution increasingly decomposes returns into factor exposures versus true residual alpha. A positive Sharpe ratio or Jensen's alpha invites the follow-up question: *what risk is this strategy actually exposed to that I am not measuring?*
