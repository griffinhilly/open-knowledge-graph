---
id: solow-growth-model
title: Solow Growth Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: dynamic-optimization-macro
  type: hard
- id: production-function-microeconomics
  type: hard
- id: differential-equations-intro
  type: soft
- id: exponential-growth-and-decay
  type: hard
- id: steady-state-analysis-growth
  type: soft
builds-toward:
- steady-state-analysis-growth
- endogenous-growth-theory
- real-business-cycle-theory
tags:
- growth-models
- neoclassical
- capital-accumulation
stage: expert
status: validated
---

# Solow Growth Model

## Core Idea
The Solow model explains long-run economic growth through capital accumulation, labor force growth, and exogenous technological progress operating under diminishing returns to capital. It identifies the steady-state growth rate as determined solely by population growth and productivity growth—not by savings behavior—because capital accumulation has diminishing payoffs. The model's key insight is that only technological progress can sustain indefinite per-capita growth in a competitive economy.

## Questions

```yaml
- question: "A country permanently increases its savings rate. According to the Solow model, what is the long-run effect on per-capita GDP growth?"
  type: multiple-choice
  options:
    - "The long-run growth rate rises permanently"
    - "The long-run growth rate falls, because less is consumed"
    - "The long-run growth rate is unchanged, but the level of per-capita GDP rises to a new, higher steady state"
    - "The long-run growth rate is unchanged and so is the level of per-capita GDP"
  answer: 2
  explanation: "In the Solow model, the steady-state growth rate of per-capita output is pinned by the rate of technological progress (g) alone — it is independent of the savings rate. A higher savings rate raises capital per worker, which raises the level of per-capita GDP, but due to diminishing returns to capital the economy eventually settles at a new (higher) steady-state level where investment again exactly covers depreciation and workforce growth. The growth rate itself reverts to g."

- question: "The Solow model predicts that, holding technology constant, a higher savings rate permanently raises the long-run growth rate of per-capita GDP."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about the Solow model. A higher savings rate raises the steady-state *level* of capital and income per worker, but because of diminishing returns to capital, each additional unit of capital contributes less output. The growth rate during the transition to the new steady state temporarily exceeds g, but in the long run growth reverts to the exogenous rate of technological progress. Savings rate affects level, not the long-run growth rate."

- question: "Why can capital accumulation alone — without technological progress — not sustain indefinite growth in per-capita income?"
  type: short-answer
  answer: "Because of diminishing returns to capital: each additional unit of capital adds less and less to output. As capital per worker rises, new investment eventually only covers depreciation and workforce growth rather than raising output further. The economy reaches a steady state where per-capita income stops growing. Only technological progress, which shifts the production function upward, can permanently increase what each worker produces."
  explanation: "The production function in the Solow model satisfies the Inada conditions — marginal product of capital is large when capital is scarce and approaches zero as capital becomes abundant. This means there is a capital stock at which gross investment just covers (δ + n)k, leaving no net capital deepening. Technological progress (A growing) shifts this boundary outward continually, which is the only engine of sustained per-capita growth in the model."
```

## Explainer

The Solow model starts from a simple production function: output Y depends on capital K, labor L, and a technology level A. In per-worker terms (lowercase letters), output per worker y = f(k) where k is capital per worker. The crucial feature is diminishing returns — the curve f(k) gets flatter as k rises, like the right half of a square root function. This shapes everything that follows.

Capital accumulation is the engine: workers save a fraction s of output, and that saving becomes new investment. But capital also depreciates at rate δ and gets diluted by a growing workforce (rate n), so the effective "drag" on capital per worker is (δ + n)k. The economy reaches its steady state k* when investment sf(k) exactly covers this drag — no net capital deepening. At that point, per-capita output y* is constant (in the absence of technological progress).

Here is the insight that surprises most students: raising the savings rate s shifts the investment curve up, which moves k* to a higher level. But the long-run *growth rate* of per-capita income is unchanged — it returns to whatever technological progress dictates. Savings affect the destination (the level of k*), not the speed limit (g). This is called the "level effect vs. growth effect" distinction and is the model's most important testable prediction.

Technological progress A — which Solow took as exogenous, just "manna from heaven" — is what allows the production function to shift upward over time, continually raising the sustainable level of per-worker output. In steady state with technological progress growing at rate g, per-capita output grows at exactly g regardless of savings behavior. This is why economists found the Solow model both enlightening and frustrating: it explains convergence across countries well, but it just *assumes* the thing (technology) that actually drives long-run prosperity.

The model also predicts conditional convergence: poor countries with lower k than their steady state should grow faster than rich ones — not because poverty is an advantage, but because capital's marginal product is higher when capital is scarce. The empirical evidence broadly supports this when you condition on savings rates and institutions, and it is one of the most tested predictions in macroeconomics.
