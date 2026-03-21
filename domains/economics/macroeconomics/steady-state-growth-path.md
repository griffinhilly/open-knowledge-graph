---
id: steady-state-growth-path
title: Steady-State Growth and the Balanced Growth Path
domain: economics
course: macroeconomics
prerequisites:
- id: solow-growth-model
  type: hard
- id: neoclassical-growth-steady-state
  type: hard
builds-toward:
- output-gap-and-potential-output
- technological-progress-and-productivity
tags:
- growth
- steady-state
- long-run
stage: advanced
status: draft
---

# Steady-State Growth and the Balanced Growth Path

## Core Idea
In steady-state growth, all variables grow at constant rates and the capital-output ratio remains constant. With Cobb-Douglas production and constant rates of population growth (n) and technological progress (g), the economy grows at n + g. The steady-state capital-output ratio depends on the savings rate, depreciation rate, and parameters of the production function. Deviations from steady-state generate dynamics toward convergence.

## Questions

```yaml
- question: "In the Solow model, a country on its balanced growth path permanently increases its savings rate. What is the correct long-run prediction?"
  type: multiple-choice
  options:
    - "The economy grows permanently faster, since more saving means more investment and capital accumulation"
    - "Output per worker grows permanently faster, since capital keeps accumulating indefinitely"
    - "The economy transitions to a new balanced growth path with a higher level of output per worker, but the same long-run growth rate n+g"
    - "The savings increase has no effect, since the capital-output ratio is pinned by technology alone"
  answer: 2
  explanation: "A higher savings rate raises the steady-state capital-output ratio K/Y = s/(δ+n+g) — a level effect. During transition, the economy grows faster than n+g as it converges to the new higher path. But the long-run growth rate remains n+g regardless of the savings rate. Option A is the classic misconception: diminishing returns to capital mean additional saving eventually only replaces depreciated capital and equips new workers, with no further effect on the growth rate. Permanent acceleration in per-worker output requires technological progress (g)."

- question: "Two identical economies differ only in their savings rates: Economy A saves 5%, Economy B saves 20%. Both have the same n, g, δ, and production function. In the long run, which statement is true?"
  type: multiple-choice
  options:
    - "Economy B grows faster in the long run because its higher saving generates more capital permanently"
    - "Both economies grow at the same rate (n+g), but Economy B has a higher level of output per worker"
    - "Economy A may overtake Economy B in the long run if its technology level is slightly higher"
    - "Economy B will converge to Economy A's income level due to diminishing returns to capital"
  answer: 1
  explanation: "Both economies grow at n+g in the long run — the balanced growth rate is determined by population growth and technological progress, not the savings rate. Economy B's higher savings rate means a higher steady-state capital-output ratio and therefore a permanently higher level of output per worker, but the growth rates are identical. The two economies grow in parallel on balanced growth paths, with B on a higher trajectory. This level-vs-growth-rate distinction is one of the most important results in growth theory."

- question: "In the Solow model, the long-run growth rate of output per worker is primarily determined by the savings rate."
  type: true-false
  answer: false
  explanation: "Long-run growth of output per worker is determined by the rate of technological progress g, not the savings rate. A higher savings rate raises the steady-state level of capital per worker (a level effect) and generates faster transitional growth, but once the new steady state is reached, output per worker grows at g regardless of saving. This is one of Solow's key policy implications: to permanently raise long-run growth per worker, you need technological innovation — encouraging saving cannot substitute for it."

- question: "On the balanced growth path, both total output Y and output per worker y = Y/L grow at constant rates, though not the same rate."
  type: true-false
  answer: true
  explanation: "Total output Y grows at n+g (population growth plus technological progress), while output per worker y = Y/L grows at g alone — the n component is 'used up' by the growing workforce. Both growth rates are constant and non-zero on the balanced path. The capital-output ratio K/Y = s/(δ+n+g) is also constant. This lockstep growth of all aggregate variables at constant rates is the defining feature of the balanced growth path, and it is what makes the path an analytically useful concept."

- question: "Why can't sustained increases in the savings rate drive permanent long-run growth of output per worker in the Solow model? What force prevents it?"
  type: short-answer
  answer: "Diminishing returns to capital. Each additional unit of capital adds less to output than the previous one. As saving raises the capital stock, each new unit of investment produces smaller output gains. Eventually, additional saving is entirely absorbed by covering depreciation plus equipping new workers and new technology — the 'break-even' investment requirement. At that point, capital per effective worker stops rising, and output per worker only grows through technological progress (g), which shifts the production function upward and escapes diminishing returns."
  explanation: "This is the central limitation of capital accumulation as a growth engine in the neoclassical framework. Any savings-rate increase merely shifts the steady state to a higher level — it does not permanently raise the growth rate. Only technological progress (or human capital accumulation, which can be modeled similarly) can drive permanent long-run growth per worker. This limitation of the Solow model motivated endogenous growth theory (Romer, Lucas), which tries to model the determinants of g rather than treating it as exogenous."
```

## Explainer

From the Solow model you already know, the key insight is that capital accumulation alone cannot drive permanent growth — diminishing returns ensure that the economy approaches a steady state where capital per effective worker stops changing. The **balanced growth path** formalizes what that steady state looks like when we allow population and technology to grow continuously. On this path, nothing is accelerating or decelerating; every important ratio has settled to a constant.

To see why growth rates must be n + g in steady state, think about what "steady state" means for capital per effective worker, k̃ = K/(A·L). For k̃ to remain constant, K must grow at the same rate as A·L. Since A grows at g and L grows at n, the product A·L grows at n + g. So total capital K grows at n + g. By the Cobb-Douglas production function, output Y also grows at n + g — same rate. Consumption and investment likewise grow at n + g. The **capital-output ratio** K/Y stays constant because both numerator and denominator grow at the same rate. This is the hallmark of balanced growth: all aggregate variables march in lockstep at n + g, while per-worker variables grow at g alone.

The **steady-state capital-output ratio** itself depends on the model's parameters. From the capital accumulation equation, at steady state savings must exactly cover depreciation and the "dilution" from new workers and better technology: s·Y = (δ + n + g)·K. Dividing both sides by Y gives K/Y = s/(δ + n + g). A higher savings rate raises the steady-state capital-output ratio; faster depreciation, population growth, or technological progress lowers it. This formula is useful because it pins down the long-run capital intensity without solving a differential equation.

What happens when the economy is *off* the balanced growth path? If k̃ is below its steady-state value — perhaps after a war destroys capital — savings exceeds break-even investment, so k̃ rises. The economy grows *faster* than n + g temporarily, catching up to the balanced path from below. If k̃ is above steady state (say, after a temporary savings surge), break-even investment exceeds savings and k̃ falls back. This **convergence property** means the balanced growth path acts like an attractor: regardless of where an economy starts, it tends toward the same long-run trajectory determined by s, δ, n, g, and the production function. Cross-country income differences in this model thus reflect either different parameter values or different positions on the convergence path — not fundamentally different growth mechanisms.
