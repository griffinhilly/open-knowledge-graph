---
id: neoclassical-growth-steady-state
title: Steady-State Growth and Balanced Growth Path
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: solow-growth-model
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- endogenous-growth-theory
- ramsey-cass-koopmans-model
tags:
- steady-state
- capital
- long-run-equilibrium
stage: advanced
status: draft
---

# Steady-State Growth and Balanced Growth Path

## Core Idea
In neoclassical growth, economies converge to a steady state where capital stock is constant and output grows at the exogenous technology rate. Steady-state capital satisfies s·f(k*) = (δ + n + g)k*, where n is population growth and g is productivity growth.

## Explainer

From the Solow growth model, you already know the fundamental equation of capital accumulation: the change in capital per effective worker equals investment minus break-even investment, or Δk = s·f(k) − (δ + n + g)k. The **steady state** is the point where these two forces exactly balance — where new investment precisely replaces the capital that is lost to depreciation (δ), diluted by population growth (n), and rendered less significant by technological progress (g). At this point, k* is constant, and the economy settles into a **balanced growth path** where output per worker grows at rate g and total output grows at rate n + g.

The steady state is not just a theoretical convenience — it is an **attractor**. To see why, consider what happens away from k*. If k < k* (the economy has less capital than its steady-state level), then s·f(k) > (δ + n + g)k — investment exceeds break-even, so capital per effective worker is rising. The economy grows faster than its long-run rate as it accumulates capital. Conversely, if k > k* (perhaps due to a temporary investment boom), break-even investment exceeds actual investment, and k falls back toward k*. This convergence is guaranteed by the **concavity of the production function** — diminishing returns to capital mean that the marginal product of capital is high when capital is scarce and low when capital is abundant. From your knowledge of differential equations and eigenvalue analysis, you can formalize this: linearizing around k*, the system has a negative eigenvalue, confirming local stability.

The steady-state condition s·f(k*) = (δ + n + g)k* reveals what determines long-run living standards. A higher savings rate s shifts the investment curve upward, raising k* and output per effective worker — but with diminishing returns, each successive increase in s buys less additional output. Higher population growth n or depreciation δ raises the break-even investment line, lowering k*. Crucially, the long-run **growth rate** of output per worker is pinned at g regardless of s, n, or δ. This is the Solow model's most striking — and controversial — prediction: policy can affect the **level** of income but not its **growth rate** in the long run. Only exogenous technological progress drives sustained per-capita growth.

The **balanced growth path** is the steady state expressed in levels rather than ratios. Along this path, output Y grows at rate n + g, capital K grows at rate n + g (maintaining a constant capital-output ratio), consumption C grows at rate n + g, and real wages grow at rate g while the interest rate (marginal product of capital) is constant. These "Kaldor facts" — constant capital-output ratio, constant factor shares, steady growth in output per worker — broadly match long-run data for developed economies, which is a key reason the neoclassical framework remains central to growth economics. The steady state also provides the baseline against which richer models — with optimizing savings (Ramsey), human capital, or endogenous innovation — are constructed and evaluated.
