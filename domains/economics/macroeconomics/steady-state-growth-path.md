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
stage: abstract-reasoning
status: draft
---

# Steady-State Growth and the Balanced Growth Path

## Core Idea
In steady-state growth, all variables grow at constant rates and the capital-output ratio remains constant. With Cobb-Douglas production and constant rates of population growth (n) and technological progress (g), the economy grows at n + g. The steady-state capital-output ratio depends on the savings rate, depreciation rate, and parameters of the production function. Deviations from steady-state generate dynamics toward convergence.

## Explainer

From the Solow model you already know, the key insight is that capital accumulation alone cannot drive permanent growth — diminishing returns ensure that the economy approaches a steady state where capital per effective worker stops changing. The **balanced growth path** formalizes what that steady state looks like when we allow population and technology to grow continuously. On this path, nothing is accelerating or decelerating; every important ratio has settled to a constant.

To see why growth rates must be n + g in steady state, think about what "steady state" means for capital per effective worker, k̃ = K/(A·L). For k̃ to remain constant, K must grow at the same rate as A·L. Since A grows at g and L grows at n, the product A·L grows at n + g. So total capital K grows at n + g. By the Cobb-Douglas production function, output Y also grows at n + g — same rate. Consumption and investment likewise grow at n + g. The **capital-output ratio** K/Y stays constant because both numerator and denominator grow at the same rate. This is the hallmark of balanced growth: all aggregate variables march in lockstep at n + g, while per-worker variables grow at g alone.

The **steady-state capital-output ratio** itself depends on the model's parameters. From the capital accumulation equation, at steady state savings must exactly cover depreciation and the "dilution" from new workers and better technology: s·Y = (δ + n + g)·K. Dividing both sides by Y gives K/Y = s/(δ + n + g). A higher savings rate raises the steady-state capital-output ratio; faster depreciation, population growth, or technological progress lowers it. This formula is useful because it pins down the long-run capital intensity without solving a differential equation.

What happens when the economy is *off* the balanced growth path? If k̃ is below its steady-state value — perhaps after a war destroys capital — savings exceeds break-even investment, so k̃ rises. The economy grows *faster* than n + g temporarily, catching up to the balanced path from below. If k̃ is above steady state (say, after a temporary savings surge), break-even investment exceeds savings and k̃ falls back. This **convergence property** means the balanced growth path acts like an attractor: regardless of where an economy starts, it tends toward the same long-run trajectory determined by s, δ, n, g, and the production function. Cross-country income differences in this model thus reflect either different parameter values or different positions on the convergence path — not fundamentally different growth mechanisms.
