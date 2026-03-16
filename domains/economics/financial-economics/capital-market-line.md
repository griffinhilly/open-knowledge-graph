---
id: capital-market-line
title: Capital Market Line and Optimal Portfolios
domain: economics
course: financial-economics
prerequisites:
- id: efficient-frontier-portfolio-theory
  type: hard
- id: risk-adjusted-performance-measures
  type: hard
tags:
- portfolio-theory
- efficient-frontier
- capm
stage: formal-systems
status: draft
---

# Capital Market Line and Optimal Portfolios

## Core Idea
The capital market line is the tangency line from the risk-free rate to the efficient frontier, representing the best risk-return tradeoff available. All investors hold the same risky portfolio (market portfolio) plus borrowing or lending at the risk-free rate.

## How It's Best Learned
Plot the efficient frontier and identify the tangency portfolio. Show that the CML slope equals the Sharpe ratio of the market portfolio. Verify that all points on the CML offer better risk-return combinations than non-tangent portfolios.

## Explainer

From the efficient frontier, you know that risky portfolios have an upper boundary in risk-return space — no combination of risky assets can push you above that curve. But the efficient frontier assumes you can only hold risky assets. The **capital market line** arises when you introduce a risk-free asset: a bond or Treasury bill that pays a guaranteed return r_f with zero variance. Mixing a risk-free asset with any risky portfolio produces a straight line in (σ, E[r]) space, because variance scales quadratically while expected return scales linearly with portfolio weights — and the covariance between a risky portfolio and a risk-free asset is zero.

The critical insight is that one specific line dominates all others. Draw a line from the risk-free rate on the vertical axis outward toward the efficient frontier. The steepest such line is the one that just touches the frontier — the **tangency portfolio**. This line is the CML, and every point on it has a higher expected return per unit of risk than any point on the efficient frontier alone (except the tangency point itself, which lies on both). The slope of the CML equals (E[r_M] − r_f) / σ_M, which is the **Sharpe ratio** of the tangency portfolio — the reward-to-risk ratio you already know from risk-adjusted performance measures.

Now comes the powerful result: under the assumptions of the Capital Asset Pricing Model, all investors, regardless of risk tolerance, choose portfolios on the CML by varying only the proportion allocated to the *same* risky portfolio (the market portfolio) and the risk-free asset. A risk-tolerant investor borrows at the risk-free rate to lever up their market portfolio exposure (moving right along the CML past the tangency point). A conservative investor holds mostly the risk-free asset with a small allocation to the market portfolio (moving left toward r_f). This **separation theorem** says that the portfolio construction problem splits into two independent decisions: identify the optimal risky portfolio (the tangency point — the same for everyone) and then choose how much risk to take (where on the CML to sit — different for everyone).

This framework has direct implications for performance evaluation. Any managed portfolio that lies below the CML is offering worse risk-return than a simple combination of the market portfolio and cash. A portfolio above the CML would represent alpha — genuine outperformance after adjusting for market risk. The practical importance of the CML is thus not just theoretical elegance: it defines the benchmark against which active management must be judged.
