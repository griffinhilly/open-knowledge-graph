---
id: growth-accounting-decomposition
title: Growth Accounting and Sources of Economic Growth
domain: economics
course: macroeconomics
prerequisites:
- id: production-function-macroeconomics
  type: hard
- id: economic-growth-theory
  type: soft
builds-toward:
- steady-state-growth-path
- technological-progress-and-productivity
tags:
- growth
- productivity
- accounting
stage: advanced
status: validated
---

# Growth Accounting and Sources of Economic Growth

## Core Idea
Growth accounting decomposes output growth into contributions from capital growth, labor growth, and total factor productivity (TFP) growth: ΔY/Y = α(ΔK/K) + (1-α)(ΔL/L) + ΔA/A. The Solow residual (TFP growth) captures technological progress but also mismeasurement and organizational improvements. Growth accounting reveals that in developed economies, most long-run growth comes from productivity rather than factor accumulation.

## Questions

```yaml
- question: "An economy has capital share α = 1/3. Capital grows 6%, labor grows 3%, and GDP grows 6% that year. What is TFP (Solow residual) growth?"
  type: multiple-choice
  options:
    - "–3%: TFP is output growth minus total input growth (6% – 6% – 3%)"
    - "2%: capital contributes 2% (= 1/3 × 6%), labor contributes 2% (= 2/3 × 3%), leaving a 2% residual"
    - "6%: TFP equals output growth since factor accumulation is the baseline"
    - "3%: TFP is the unweighted average of capital and labor growth rates"
  answer: 1
  explanation: "Growth accounting weights each input by its income share: capital contributes α × ΔK/K = 1/3 × 6% = 2%, and labor contributes (1–α) × ΔL/L = 2/3 × 3% = 2%. Total factor contribution = 4%. With GDP growing 6%, TFP = 6% – 4% = 2%. The most common error (option A) forgets the income-share weights and subtracts raw growth rates — but raw input growth of 9% exceeding output growth of 6% doesn't mean TFP is negative; the weights are what matter."

- question: "Empirical growth accounting shows roughly two-thirds of long-run growth per worker in rich economies comes from TFP. What does this imply for strategies that attempt to sustain growth purely through capital investment?"
  type: multiple-choice
  options:
    - "Capital investment is the more reliable lever because it is directly controllable, unlike TFP"
    - "Capital accumulation faces diminishing returns; each additional unit contributes less than the last, so capital investment alone cannot sustain long-run growth"
    - "Rich economies should shift investment from capital to labor to balance the growth contributions"
    - "The 2/3 figure likely reflects measurement error in TFP, so capital's true contribution is larger"
  answer: 1
  explanation: "From the production function, capital exhibits diminishing marginal returns — as K/L rises, each additional unit of capital adds less to output. A country doubling its capital grows output by less than double, so the capital contribution to growth shrinks over time. Sustained long-run growth therefore requires ongoing TFP growth — improvements in how inputs are used. This is one of the core insights of growth accounting: factor accumulation explains catch-up growth but not sustained long-run prosperity."

- question: "If a country doubles all its factor inputs — capital and labor — and GDP exactly doubles, then TFP growth over that period is positive."
  type: true-false
  answer: false
  explanation: "Under constant returns to scale, doubling all inputs produces exactly double the output with zero TFP growth. Growth accounting assigns TFP growth = ΔY/Y – α(ΔK/K) – (1–α)(ΔL/L). If Y doubles (100% growth) and K and L both double, then the formula gives: 100% – α×100% – (1–α)×100% = 100% – 100% = 0%. TFP growth measures how much more output the economy extracts from a given bundle of inputs — not just whether output grew."

- question: "Because TFP is computed as a residual — output growth not explained by capital and labor — it absorbs all measurement errors in those inputs."
  type: true-false
  answer: true
  explanation: "This is Solow's own acknowledged limitation — he called the residual 'a measure of our ignorance.' TFP captures genuine technological progress, organizational improvements, and better resource allocation, but it also absorbs any mismeasurement of capital quality, hours worked, or human capital. If capital services are mismeasured (e.g., computing capital depreciation incorrectly), the error flows into TFP. This is why growth accounting reveals the proximate sources of growth without fully identifying their underlying causes."

- question: "What is the Solow residual, and why does its dominance in long-run growth data matter for understanding economic development?"
  type: short-answer
  answer: "The Solow residual is TFP growth — the portion of output growth not explained by capital and labor input growth, computed as ΔA/A = ΔY/Y – α(ΔK/K) – (1–α)(ΔL/L). Its dominance matters because sustained long-run prosperity cannot come from simply accumulating more factors (which face diminishing returns) but requires ongoing improvements in the efficiency of production — better technology, organization, and resource allocation."
  explanation: "Growth accounting separates proximate accounting from deeper explanation. Countries can grow quickly during catch-up phases by building factories and expanding their workforce, but once factor accumulation slows (as returns diminish), only TFP growth can sustain income levels. This shifts the policy question from 'how do we accumulate more?' to 'how do we innovate and improve efficiency?' — the right question for understanding long-run development."
```

## Explainer

From your study of the macroeconomic production function, you know that output Y depends on inputs: capital K, labor L, and total factor productivity A, in a relationship like Y = A × F(K, L). This tells us *what* determines output but not *how much* each component explains observed growth. Growth accounting applies this framework to a diagnostic question: when GDP grew by 3% last year, how much came from having more capital, how much from having more workers (or workers putting in more hours), and how much from getting more output from the same inputs?

The decomposition follows from logarithmic differentiation of the production function under two standard assumptions: constant returns to scale, and competitive factor markets where each factor earns its marginal product. Under these conditions, capital's share of national income (α ≈ 0.33 in most rich economies) equals the elasticity of output with respect to capital. This gives the accounting equation: ΔY/Y ≈ α(ΔK/K) + (1-α)(ΔL/L) + ΔA/A. Capital's contribution is α times capital's growth rate; labor's contribution is (1-α) times labor's growth rate. The residual — output growth minus these two calculated contributions — is **Total Factor Productivity growth** (ΔA/A), often called the **Solow residual** after Robert Solow who first applied it systematically in 1957.

TFP growth captures everything that makes the economy more productive without simply using more inputs: technological improvement (better machines, new production methods, improved software), organizational and managerial improvements, better resource allocation across firms and sectors, and gains from specialization and trade. Think of it as the efficiency of the economy's production process. A country that doubles its capital and labor and gets exactly twice the output has TFP growth of zero — it just scaled up. A country that doubles its inputs and gets 2.2 times the output has positive TFP growth of roughly 10% — it got smarter about how it uses what it has. The uncomfortable corollary is that TFP is calculated as a residual, meaning it absorbs all measurement error in capital and labor inputs. Solow himself acknowledged this problem, noting that his residual was "a measure of our ignorance."

The empirical results from growth accounting reshape our understanding of development. For today's rich economies, roughly two-thirds of long-run growth per worker comes from TFP, with capital deepening (more capital per worker) contributing the remainder. This ratio has profound implications: because of diminishing returns to capital (from your production function), a country cannot sustain growth indefinitely by simply accumulating more machines. Each additional unit of capital contributes less than the last. Sustained long-run growth *requires* sustained TFP growth — continuous improvements in how inputs are combined. For rapidly industrializing countries like South Korea and Taiwan in the 1960s–80s, factor accumulation mattered more during the catch-up phase (vast amounts of capital were being installed where little existed before), but even there, TFP ultimately drove convergence toward the technology frontier. This is the bridge between growth accounting and growth theory: accounting reveals the proximate sources of growth; theory explains why TFP grows at all.
