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
stage: advanced
status: draft
---

# Capital Market Line and Optimal Portfolios

## Core Idea
The capital market line is the tangency line from the risk-free rate to the efficient frontier, representing the best risk-return tradeoff available. All investors hold the same risky portfolio (market portfolio) plus borrowing or lending at the risk-free rate.

## How It's Best Learned
Plot the efficient frontier and identify the tangency portfolio. Show that the CML slope equals the Sharpe ratio of the market portfolio. Verify that all points on the CML offer better risk-return combinations than non-tangent portfolios.

## Questions

```yaml
- question: "Two investors both accept the assumptions of the CAPM and know the capital market line. Investor A is highly risk-tolerant; Investor B is very conservative. According to the separation theorem, what should differ between their portfolios?"
  type: multiple-choice
  options:
    - "They should hold different mixes of risky assets, each customized to their risk tolerance"
    - "Only the proportion allocated to the market portfolio versus the risk-free asset — the risky portion is identical for both"
    - "A should hold mostly equities; B should hold mostly bonds, because bond-heavy portfolios have lower risk"
    - "A should construct a leveraged portfolio with margin; B should hold only Treasury bills and no equities"
  answer: 1
  explanation: "The separation theorem says the optimal risky portfolio is the same for all investors — the market portfolio, which is the tangency point on the efficient frontier. Investors differ only in how much of that single risky portfolio they hold versus the risk-free asset. A risk-tolerant investor lends less (or borrows to lever up the market portfolio), moving right along the CML. A conservative investor holds mostly the risk-free asset with a small slice of the market portfolio, moving left. Neither constructs their own custom blend of risky assets."

- question: "A managed fund's performance is plotted in (σ, E[r]) space. It falls below the capital market line. What does this mean for investors?"
  type: multiple-choice
  options:
    - "The fund has negative alpha and is actively destroying shareholder value"
    - "A superior risk-return outcome is available by simply combining the market portfolio with the risk-free asset"
    - "The fund's Sharpe ratio is negative, meaning it earned less than the risk-free rate"
    - "The fund is too concentrated and needs to diversify across more asset classes"
  answer: 1
  explanation: "Any point below the CML is dominated: for the same level of risk (σ), a portfolio on the CML offers a higher expected return. You can achieve that dominating portfolio by combining the market portfolio with the risk-free asset in the right proportions — no active management required. The fund manager must beat the CML (earn alpha) to justify its fees; sitting below the line means passive investors do better with a trivial two-asset strategy. Note that being below the CML doesn't necessarily mean a negative Sharpe ratio — it just means the Sharpe ratio is below that of the market portfolio."

- question: "The slope of the capital market line equals the Sharpe ratio of the market (tangency) portfolio."
  type: true-false
  answer: true
  explanation: "The CML runs from r_f on the vertical axis to the tangency portfolio (the market portfolio) at (σ_M, E[r_M]). Its slope is (E[r_M] − r_f) / σ_M, which is exactly the Sharpe ratio of the market portfolio — the excess return per unit of total risk. This slope represents the price of risk in the market: for each additional unit of standard deviation you accept, the CML tells you how much additional expected return you receive. No risky portfolio offers a better trade than this slope."

- question: "According to the separation theorem, conservative investors should hold a different blend of risky assets than aggressive investors — one tilted toward lower-volatility stocks and away from high-volatility equities."
  type: true-false
  answer: false
  explanation: "This is a common and tempting misconception. The separation theorem says the optimal risky portfolio is identical for all investors regardless of risk preference — it is the market portfolio, the tangency point on the efficient frontier. Risk tolerance affects only the split between this single risky portfolio and the risk-free asset, not the composition of the risky portion. A conservative investor holds the market portfolio in a smaller proportion, combined with more of the risk-free asset. Constructing a custom low-volatility risky portfolio is suboptimal — it would place that investor below the CML."

- question: "What is the separation theorem, and why does it imply that any managed risky portfolio lying below the capital market line is indefensible for investors of any risk tolerance?"
  type: short-answer
  answer: "The separation theorem states that the optimal risky portfolio is the same for all investors under CAPM assumptions — the market portfolio (the tangency point). Risk tolerance only determines the ratio of market portfolio to risk-free asset, not the composition of the risky part. Because the CML represents the highest possible expected return for every level of risk achievable by combining any portfolio with the risk-free asset, a managed portfolio below the CML is dominated for every investor: no matter how risk-tolerant or risk-averse, they can achieve a better risk-return outcome by simply blending the market index fund with cash."
  explanation: "The CML is a universal efficiency frontier. Any point below it — regardless of Sharpe ratio or diversification — can be bettered by the market portfolio plus risk-free combination. This is the theoretical foundation for passive indexing: if the CML represents the best attainable tradeoff, active managers must generate alpha (push their portfolio above the line) to justify active fees. Most do not."
```

## Explainer

From the efficient frontier, you know that risky portfolios have an upper boundary in risk-return space — no combination of risky assets can push you above that curve. But the efficient frontier assumes you can only hold risky assets. The **capital market line** arises when you introduce a risk-free asset: a bond or Treasury bill that pays a guaranteed return r_f with zero variance. Mixing a risk-free asset with any risky portfolio produces a straight line in (σ, E[r]) space, because variance scales quadratically while expected return scales linearly with portfolio weights — and the covariance between a risky portfolio and a risk-free asset is zero.

The critical insight is that one specific line dominates all others. Draw a line from the risk-free rate on the vertical axis outward toward the efficient frontier. The steepest such line is the one that just touches the frontier — the **tangency portfolio**. This line is the CML, and every point on it has a higher expected return per unit of risk than any point on the efficient frontier alone (except the tangency point itself, which lies on both). The slope of the CML equals (E[r_M] − r_f) / σ_M, which is the **Sharpe ratio** of the tangency portfolio — the reward-to-risk ratio you already know from risk-adjusted performance measures.

Now comes the powerful result: under the assumptions of the Capital Asset Pricing Model, all investors, regardless of risk tolerance, choose portfolios on the CML by varying only the proportion allocated to the *same* risky portfolio (the market portfolio) and the risk-free asset. A risk-tolerant investor borrows at the risk-free rate to lever up their market portfolio exposure (moving right along the CML past the tangency point). A conservative investor holds mostly the risk-free asset with a small allocation to the market portfolio (moving left toward r_f). This **separation theorem** says that the portfolio construction problem splits into two independent decisions: identify the optimal risky portfolio (the tangency point — the same for everyone) and then choose how much risk to take (where on the CML to sit — different for everyone).

This framework has direct implications for performance evaluation. Any managed portfolio that lies below the CML is offering worse risk-return than a simple combination of the market portfolio and cash. A portfolio above the CML would represent alpha — genuine outperformance after adjusting for market risk. The practical importance of the CML is thus not just theoretical elegance: it defines the benchmark against which active management must be judged.
