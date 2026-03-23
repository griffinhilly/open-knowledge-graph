---
id: ak-model-endogenous-growth
title: AK Model of Endogenous Growth
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: endogenous-growth-theory
  type: hard
tags:
- endogenous-growth
- constant-returns
- capital-accumulation
stage: expert
status: validated
---

# AK Model of Endogenous Growth

## Core Idea
The AK model assumes constant returns to a broad capital aggregate (including human capital, infrastructure, and knowledge), eliminating the diminishing returns that limit growth in Solow-type models. With constant marginal returns to capital, the savings rate directly determines the growth rate, creating a knife-edge equilibrium where growth is endogenous and persistent. Though analytically simple, the model illustrates how broad-based capital accumulation without technological bottlenecks can sustain long-run growth.

## Questions

```yaml
- question: "A government permanently subsidizes investment, raising the economy's savings rate. In the AK model, what is the long-run effect on the growth rate of output?"
  type: multiple-choice
  options:
    - "The growth rate temporarily rises during a transition period, then returns to its original level"
    - "The growth rate permanently rises, because the savings rate directly determines the growth rate"
    - "Only the level of output rises; the long-run growth rate is determined by technology, not savings"
    - "The growth rate falls, because more investment means less consumption and lower welfare"
  answer: 1
  explanation: "In the AK model, the long-run growth rate is g = sA − δ, so a permanent rise in s produces a permanent rise in g. This is the fundamental departure from Solow: in Solow, higher savings raises the level of output per worker but not the long-run growth rate (which depends only on exogenous technology). Option C describes the Solow result — the most common wrong answer here — and confuses the two models."

- question: "Why does the AK model produce no steady state, unlike the Solow model?"
  type: multiple-choice
  options:
    - "Because the AK model ignores depreciation, so capital always grows"
    - "Because constant returns to capital mean each additional unit of capital generates the same output as the last, so saving never 'runs out of steam'"
    - "Because total factor productivity A grows over time, continuously shifting the production function upward"
    - "Because the AK model assumes an infinite labor supply that keeps the marginal product of capital constant"
  answer: 1
  explanation: "In Solow, the economy converges to a steady state because of diminishing returns: each additional unit of capital adds less output, so eventually new saving just covers depreciation. In the AK model, the marginal product of capital is constant at A regardless of the capital stock — there are no diminishing returns to the broadly defined K. So the gap between new capital formation and depreciation never closes, and the economy grows without bound. A is wrong because AK models include depreciation (δ) — it's the constant MPK, not the absence of δ, that removes the steady state."

- question: "In the AK model, a permanently higher savings rate leads to permanently faster long-run output growth."
  type: true-false
  answer: true
  explanation: "Yes — this is the defining property of the AK model. The growth rate g = sA − δ is directly proportional to the savings rate s. This contrasts sharply with the Solow model, where a higher savings rate shifts the economy to a higher output level but leaves the long-run growth rate unchanged (determined by exogenous technology). Policy that raises investment rates has permanent growth effects in the AK framework."

- question: "The AK model assumes diminishing marginal returns to capital, just like the Solow model, but incorporates knowledge externalities that offset them at the aggregate level."
  type: true-false
  answer: false
  explanation: "The AK model assumes *constant* marginal returns to a broad capital aggregate — this is its defining assumption, and the source of both its power and its fragility. The 'broad K' interpretation (including human capital, knowledge, infrastructure) is the justification for why returns might not diminish, but the model itself simply assumes Y = AK with no externalities needed. Models that explicitly model knowledge externalities (Romer 1986) provide microfoundations for constant returns, but the AK model takes constant returns as a primitive assumption."

- question: "Why does the AK model predict that policy (e.g., tax incentives for investment) has permanent growth effects, while the Solow model predicts only temporary level effects?"
  type: short-answer
  answer: "In Solow, diminishing returns to capital mean that each unit of investment adds less output as the capital stock grows, so higher savings eventually just replaces depreciation at a higher but stable level — a steady state. In AK, constant returns mean every additional unit of capital generates the same output increment regardless of how much capital already exists, so the economy never 'settles down.' A higher savings rate translates directly into a permanently higher growth rate, making policy interventions that raise investment have lasting consequences."
  explanation: "The key is the presence or absence of diminishing returns. Solow's diminishing returns create a convergence force that eventually offsets the savings advantage. AK's constant returns eliminate this force. Students often conflate 'higher output' with 'higher growth' — the Solow model does raise output with higher savings, but only to a new steady-state level; the growth rate along the steady-state path remains at the exogenous rate of technological progress."
```

## Explainer

From endogenous growth theory, you know the central dissatisfaction with the Solow model: long-run growth depends entirely on exogenous technological progress, which the model takes as given rather than explaining. The **AK model** is the simplest possible fix. It replaces the Solow production function Y = K^α · L^(1−α) with just Y = AK, where A is a constant productivity parameter and K represents a broad capital aggregate. The entire output of the economy is proportional to this single capital stock, with no diminishing returns.

The key insight is in what "K" means. In the Solow model, capital means physical machines and buildings, and adding more machines to a fixed labor force yields progressively smaller output gains — **diminishing marginal returns**. The AK model sidesteps this by defining K broadly to include human capital (education, skills), organizational knowledge, and infrastructure alongside physical equipment. The argument is that when a firm invests in training workers *and* buying machines *and* developing processes simultaneously, these investments complement each other in ways that prevent returns from diminishing. A new computer is more productive when the worker using it is better trained, and better training is more valuable when better tools are available. The aggregate "capital" grows without hitting a ceiling.

The mathematical consequence is striking. In the Solow model, the economy converges to a **steady state** where capital per worker stops growing — additional saving just replaces depreciation because each new unit of capital adds less output than the last. In the AK model, there is no steady state. Because the marginal product of capital is constant at A, every unit of saving generates the same return regardless of how much capital already exists. The **growth rate of output** becomes g = sA − δ, where s is the savings rate and δ is depreciation. Higher savings rates mean permanently faster growth, not just a temporarily higher level of output. This is a fundamentally different prediction: policy that raises investment rates (through subsidies, tax incentives, or public education spending) permanently accelerates growth rather than producing a one-time level shift.

The AK model is deliberately stark — a teaching tool, not a complete theory. Its "knife-edge" property (returns to capital must be *exactly* constant, not slightly diminishing) makes it fragile. If returns are even slightly diminishing, the economy eventually converges to a steady state and the Solow logic reasserts itself. Real endogenous growth models (Romer, Lucas) provide microfoundations for *why* returns might not diminish — knowledge spillovers, increasing returns to ideas, human capital externalities. But the AK framework captures the essential mechanism in one equation: if you can plausibly argue that broad capital accumulation faces constant returns, then growth is self-sustaining and policy matters for the long run, not just the transition path.
