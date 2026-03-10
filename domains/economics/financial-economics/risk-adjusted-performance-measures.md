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
tags:
- sharpe-ratio
- jensen-alpha
- treynor-ratio
- performance-evaluation
- alpha
stage: formal-systems
status: draft
---

# Risk-Adjusted Performance Measures

## Core Idea
Risk-adjusted performance measures evaluate whether a portfolio's returns are commensurate with the risk taken. The Sharpe ratio = (rp − rₓ) / σp measures return per unit of total risk and is appropriate when the portfolio represents an investor's entire wealth. Jensen's alpha = actual return − CAPM-predicted return measures excess return above what the portfolio's beta predicts — positive alpha is the goal of active management. The Treynor ratio uses beta rather than total volatility in the denominator, appropriate when the portfolio is a component of a larger diversified position. These measures are used to identify genuine manager skill, to attribute performance to factor exposures vs. true alpha, and to determine whether active management fees are justified.

## How It's Best Learned
Calculate Sharpe ratio and Jensen's alpha for a real actively managed mutual fund over a 10-year period and compare to a passive index. Understand why a fund can have positive alpha on a CAPM basis but negative alpha once Fama-French factors are added. Note that any strategy with optionlike features (selling volatility) can artificially inflate its Sharpe ratio.

## Common Misconceptions
- Positive alpha is not proof of manager skill — it may reflect luck, benchmark misspecification, or undisclosed exposure to risk factors not included in the pricing model.
- The Sharpe ratio implicitly assumes normally distributed returns; strategies that sell options or take on tail risk can display high Sharpe ratios right up until a catastrophic loss.
