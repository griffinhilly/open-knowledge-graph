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
stage: advanced
status: draft
---

# AK Model of Endogenous Growth

## Core Idea
The AK model assumes constant returns to a broad capital aggregate (including human capital, infrastructure, and knowledge), eliminating the diminishing returns that limit growth in Solow-type models. With constant marginal returns to capital, the savings rate directly determines the growth rate, creating a knife-edge equilibrium where growth is endogenous and persistent. Though analytically simple, the model illustrates how broad-based capital accumulation without technological bottlenecks can sustain long-run growth.

## Explainer

From endogenous growth theory, you know the central dissatisfaction with the Solow model: long-run growth depends entirely on exogenous technological progress, which the model takes as given rather than explaining. The **AK model** is the simplest possible fix. It replaces the Solow production function Y = K^α · L^(1−α) with just Y = AK, where A is a constant productivity parameter and K represents a broad capital aggregate. The entire output of the economy is proportional to this single capital stock, with no diminishing returns.

The key insight is in what "K" means. In the Solow model, capital means physical machines and buildings, and adding more machines to a fixed labor force yields progressively smaller output gains — **diminishing marginal returns**. The AK model sidesteps this by defining K broadly to include human capital (education, skills), organizational knowledge, and infrastructure alongside physical equipment. The argument is that when a firm invests in training workers *and* buying machines *and* developing processes simultaneously, these investments complement each other in ways that prevent returns from diminishing. A new computer is more productive when the worker using it is better trained, and better training is more valuable when better tools are available. The aggregate "capital" grows without hitting a ceiling.

The mathematical consequence is striking. In the Solow model, the economy converges to a **steady state** where capital per worker stops growing — additional saving just replaces depreciation because each new unit of capital adds less output than the last. In the AK model, there is no steady state. Because the marginal product of capital is constant at A, every unit of saving generates the same return regardless of how much capital already exists. The **growth rate of output** becomes g = sA − δ, where s is the savings rate and δ is depreciation. Higher savings rates mean permanently faster growth, not just a temporarily higher level of output. This is a fundamentally different prediction: policy that raises investment rates (through subsidies, tax incentives, or public education spending) permanently accelerates growth rather than producing a one-time level shift.

The AK model is deliberately stark — a teaching tool, not a complete theory. Its "knife-edge" property (returns to capital must be *exactly* constant, not slightly diminishing) makes it fragile. If returns are even slightly diminishing, the economy eventually converges to a steady state and the Solow logic reasserts itself. Real endogenous growth models (Romer, Lucas) provide microfoundations for *why* returns might not diminish — knowledge spillovers, increasing returns to ideas, human capital externalities. But the AK framework captures the essential mechanism in one equation: if you can plausibly argue that broad capital accumulation faces constant returns, then growth is self-sustaining and policy matters for the long run, not just the transition path.
