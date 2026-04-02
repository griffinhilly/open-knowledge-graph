---
id: total-factor-productivity-and-growth-sources
title: Total Factor Productivity and the Sources of Growth
domain: economics
course: macroeconomics
prerequisites:
- id: solow-growth-model
  type: hard
- id: endogenous-growth-theory
  type: soft
- id: technological-progress-and-productivity
  type: soft
- id: growth-accounting-decomposition
  type: soft
tags:
- productivity
- growth
- tfp
stage: expert
status: validated
---
# Total Factor Productivity and the Sources of Growth

## Core Idea
Growth accounting decomposes output growth into contributions from capital accumulation, labor growth, and total factor productivity (TFP)—the residual measuring technological progress and efficiency improvements. The Solow residual shows that most long-run growth comes from TFP, not capital deepening, highlighting the importance of innovation, education, and institutions. TFP growth varies across countries and over time, explaining divergent growth rates.

## Questions

```yaml
- question: "Country A and Country B have identical savings rates, labor force growth rates, and initial capital stocks. After 50 years, Country A is twice as wealthy per capita. Growth accounting would attribute this divergence primarily to:"
  type: multiple-choice
  options:
    - "Country A having accumulated more capital through higher investment efficiency"
    - "Country A having higher TFP growth — differences in technology, institutions, and efficiency that factor accumulation alone cannot explain"
    - "Country A having a younger population, contributing more labor hours per capita"
    - "Country A experiencing lower capital depreciation rates, preserving more of its stock"
  answer: 1
  explanation: "With identical savings rates and labor force growth, the Solow model predicts both countries converge to the same steady-state income level — persistent capital accumulation differences cannot explain the divergence. TFP (the Solow residual) captures everything that is not capital or labor: technology, institutions, organizational efficiency, infrastructure quality. The empirical finding is that most long-run per-capita income divergence across countries traces to TFP differences, not factor accumulation differences. Options C and D might contribute to TFP through indirect channels but are not the growth accounting category."

- question: "Using the Cobb-Douglas framework Y = AK^0.3 L^0.7, output grows 3% per year, capital grows 4%, and labor grows 1%. What is TFP growth?"
  type: multiple-choice
  options:
    - "3% — TFP growth equals total output growth when using a production function approach"
    - "1.9% — TFP equals the combined contribution of capital and labor to output growth"
    - "1.5% — computed as output growth minus the unweighted average of input growth rates"
    - "1.1% — the residual after subtracting weighted factor contributions: 3% minus 0.3(4%) minus 0.7(1%)"
  answer: 3
  explanation: "Growth accounting decomposes output growth as ΔY/Y = α(ΔK/K) + (1-α)(ΔL/L) + ΔA/A. Plugging in: 3% = 0.3(4%) + 0.7(1%) + ΔA/A = 1.2% + 0.7% + ΔA/A = 1.9% + ΔA/A. Therefore ΔA/A = 3% - 1.9% = 1.1%. Option A conflates TFP growth with total output growth. Option B gives the factors' total contribution (1.9%) — what inputs explain — which is the opposite of TFP. Option C ignores income shares, incorrectly treating capital and labor contributions as equally weighted."

- question: "In the Solow model, doubling a country's capital stock per worker will approximately double its output per worker, because capital and output scale proportionally."
  type: true-false
  answer: false
  explanation: "The Cobb-Douglas production function has diminishing returns to capital: output per worker scales as k^α, where α is capital's income share (typically ~0.3). Doubling capital per worker multiplies output per worker by 2^0.3 ≈ 1.23 — a 23% increase, not a doubling. This is precisely why capital deepening cannot sustain long-run growth: each additional unit of capital adds less and less output. Only TFP growth — shifts in the production function itself — can sustain growth indefinitely without hitting diminishing returns."

- question: "TFP is called a 'residual' because it cannot be measured directly — it is inferred from the output growth that factor accumulation alone cannot explain."
  type: true-false
  answer: true
  explanation: "We observe output growth and can measure capital and labor growth along with their income shares. After attributing growth proportionally to factor inputs, whatever remains is the Solow residual — TFP growth. TFP is 'measured by subtraction,' not by directly observing technology improvements. This is sometimes called 'a measure of our ignorance' because it bundles together everything we cannot attribute to factors: technology, institutions, efficiency, organizational practices, and human capital quality."

- question: "Why can capital deepening not sustain long-run per-capita growth, and what does TFP represent that capital accumulation cannot capture?"
  type: short-answer
  answer: "Capital deepening faces diminishing returns: each additional unit of capital added to a fixed labor force raises output by less than the previous unit, following the concave shape of the production function. Eventually, an economy reaches a steady state where additional investment only offsets depreciation and population growth, with no net increase in capital per worker. TFP represents shifts in the production function itself — better technology, more efficient organization, improved institutions, higher-quality human capital — that raise the output achievable from any given stock of inputs. Unlike capital, TFP improvements do not diminish: a better algorithm or stronger institutions raise productivity for every unit of capital and labor simultaneously."
  explanation: "The policy implication is that long-run growth depends on TFP drivers — R&D, education, institutional reform, technology adoption — not only on incentivizing capital accumulation. Higher savings rates produce a transition to a higher steady state, but only sustained TFP growth produces ongoing improvement beyond that steady state."
```

## Explainer

Think about why some countries grow rich and others stagnate. The Solow model you studied showed that capital deepening — adding more machines per worker — generates growth, but at a diminishing rate. Eventually an economy reaches its steady state where capital per worker stops rising. Yet we observe sustained long-run growth in wealthy economies for over a century. Where does it come from? The answer is **total factor productivity (TFP)**: the ability to squeeze more output from the same inputs. TFP captures everything that isn't capital or labor — technology, organizational efficiency, institutions, infrastructure quality, and the knowledge embedded in the workforce.

Growth accounting makes this precise using the Cobb-Douglas production function. If output Y depends on capital K, labor L, and technology A as Y = AK^α·L^(1-α), then output growth can be decomposed: ΔY/Y ≈ α(ΔK/K) + (1-α)(ΔL/L) + ΔA/A. The first two terms are contributions from capital and labor growth, weighted by their income shares (α and 1-α). The residual — what's left after accounting for factor accumulation — is the **Solow residual**, which equals TFP growth. This is why TFP is called a residual: we cannot measure it directly, only infer it from what factors alone cannot explain. It is growth that comes from doing things smarter, not just from adding more inputs.

The empirical finding that reshaped macroeconomics: the Solow residual is large. In most developed economies, TFP growth accounts for roughly half to two-thirds of long-run output growth per capita. Capital deepening matters, but it runs into diminishing returns — doubling capital does not double output. TFP has no such constraint. A better algorithm, a new molecule, a reformed legal system, improved management practices — these shift the production function itself, permanently raising the output achievable from any given stock of inputs. Economists call this "working smarter, not just harder."

This explains divergent growth rates across countries in a way pure capital accumulation cannot. Two countries with identical savings rates and labor force growth will converge to the same steady-state income level in the basic Solow model — yet we observe massive, persistent divergence. The missing piece is TFP. Countries differ in their rates of innovation, technology adoption, institutional quality, and human capital formation. Endogenous growth theory pushes further: rather than treating TFP growth as manna from heaven, it models the specific investments — in R&D, education, and infrastructure — that generate it. The policy implication is direct: if most long-run growth comes from TFP, and TFP comes from institutions, innovation, and education, then those are the levers that matter most for development strategy.
