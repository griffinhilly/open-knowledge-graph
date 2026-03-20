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

## Explainer

From your study of the efficient frontier, you know that investors care about both return and risk — that a higher return is not automatically better if it comes with proportionally higher risk. From CAPM, you know that the only risk that earns a premium is systematic risk, measured by beta. Risk-adjusted performance measures translate these ideas into tools for evaluating whether a portfolio — or a manager — has actually earned its returns relative to the risk taken.

The **Sharpe ratio** is the most widely used measure: (r_p − r_f) / σ_p. It asks how much excess return (above the risk-free rate) you received per unit of total volatility. A Sharpe ratio of 0.8 means the portfolio earned 0.8 percentage points of excess return for each 1% of standard deviation. When comparing two portfolios of similar asset classes, the one with the higher Sharpe ratio delivered better risk-adjusted performance. Crucially, the Sharpe ratio uses total risk (σ_p), making it appropriate when the portfolio under evaluation represents the investor's entire wealth — there is no larger portfolio absorbing its idiosyncratic risk.

**Jensen's alpha** takes a different approach rooted in CAPM. CAPM predicts what a portfolio *should* return given its beta: E(r_p) = r_f + β_p(r_m − r_f). Alpha is the actual return minus this CAPM-predicted return. Positive alpha means the manager generated return above what compensation for systematic risk alone would predict — which is the goal of every active manager. If a fund has β = 1.2 and the market earned 10%, the fund should have earned roughly r_f + 1.2(10% − r_f). If it actually earned more than that, the difference is alpha. Alpha is the right metric when you want to isolate genuine skill from leverage or systematic factor exposure — a fund that simply buys high-beta stocks in a rising market earns no alpha even with stellar raw returns.

The **Treynor ratio** = (r_p − r_f) / β_p uses beta in the denominator instead of total volatility. This is appropriate when the portfolio is one component of a larger diversified holding — the idiosyncratic risk of this sub-portfolio diversifies away in context, so only systematic risk matters. A manager running a tech sleeve within a diversified pension fund should be evaluated on Treynor, not Sharpe.

All three measures share a critical vulnerability: they are only as good as the risk model used to define "expected return." Jensen's alpha against CAPM looks very different from alpha against a Fama-French five-factor model. Many strategies that appear to generate alpha versus a simple market-beta benchmark are simply loading on well-known priced factors — size, value, momentum, profitability — that the benchmark missed. This is why professional performance attribution increasingly decomposes returns into factor exposures versus true residual alpha. A positive Sharpe ratio or Jensen's alpha invites the follow-up question: *what risk is this strategy actually exposed to that I am not measuring?*
