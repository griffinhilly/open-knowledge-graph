---
id: steady-state-analysis-growth
title: Steady-State Analysis in Growth Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: eigenvalues-eigenvectors
  type: hard
- id: systems-of-linear-equations
  type: hard
builds-toward:
- golden-rule-capital-accumulation
tags:
- equilibrium-analysis
- long-run-growth
- dynamics
stage: expert
status: validated
---

# Steady-State Analysis in Growth Models

## Core Idea
A steady state in growth models is a balanced-growth path where all variables grow at constant rates and capital-to-labor ratios remain constant. Analyzing steady-state properties reveals long-run equilibrium capital stocks, consumption levels, and growth rates that determine welfare. Stability analysis around the steady state shows whether economies converge to equilibrium or diverge after disturbances, providing crucial insights into long-run economic behavior.

## Questions

```yaml
- question: "A linearized growth model has a Jacobian matrix with eigenvalues −0.3 and +0.5. What does this imply about the steady state?"
  type: multiple-choice
  options:
    - "The steady state is globally stable — both eigenvalues are non-zero, so all paths converge"
    - "The steady state is a saddle point — only the saddle path converges; all other trajectories diverge"
    - "The steady state is unstable — any perturbation causes permanent divergence regardless of initial conditions"
    - "The positive eigenvalue indicates oscillatory cycling around the steady state"
  answer: 1
  explanation: "One negative and one positive eigenvalue defines saddle-point stability. The stable manifold (saddle path) is a single converging trajectory. Paths not on it diverge — one eigenvalue negative means there is a direction of attraction, but the positive eigenvalue means there is also a direction of repulsion. This is the typical result in two-variable growth models like Ramsey-Cass-Koopmans."

- question: "In the Solow model, which mathematical condition defines the steady-state capital-per-worker ratio k*?"
  type: multiple-choice
  options:
    - "The capital stock is at its maximum possible level given technology"
    - "Per-capita output growth equals the population growth rate"
    - "New investment exactly replaces depreciated capital: sf(k*) = (n + δ)k*"
    - "The marginal product of capital equals zero"
  answer: 2
  explanation: "The steady state is where the capital-per-worker ratio stops changing — the 'bathtub' analogy where inflow equals outflow. sf(k) represents new investment per worker; (n + δ)k represents capital needed to replace depreciation and equip new workers. At k*, these are equal, so Δk = 0. Finding k* reduces a dynamic system to a single algebraic equation."

- question: "In the Solow model, a higher savings rate leads to a higher steady-state capital stock per worker."
  type: true-false
  answer: true
  explanation: "A higher savings rate s shifts up the investment curve sf(k), raising its intersection with the breakeven investment line (n + δ)k. This produces a higher k*. Raising s doesn't change the breakeven line — it only changes how much saving is available to accumulate capital — so the new steady state has more capital per worker and correspondingly higher output and consumption (up to the Golden Rule level)."

- question: "If a steady state has a positive eigenvalue, the economy is guaranteed to converge to it eventually as long as the initial conditions are close enough."
  type: true-false
  answer: false
  explanation: "A positive eigenvalue means the system is locally unstable in that direction — perturbations grow, not shrink, along the corresponding eigenvector. Convergence requires all eigenvalues to have negative real parts. A saddle point (one negative, one positive) has only a one-dimensional stable manifold; initial conditions not on it diverge. 'Close to steady state' is not sufficient for convergence when a positive eigenvalue exists."

- question: "In a model with saddle-point stability, why must forward-looking agents immediately 'jump' to the saddle path after a shock rather than adjusting gradually?"
  type: short-answer
  answer: "Paths not on the saddle path lead to economically impossible outcomes: capital eventually goes to zero (no production) or consumption goes to zero or infinity. Since rational forward-looking agents anticipate these outcomes and rule them out, they must jump to the unique path that converges — the saddle path. The 'jump' is not arbitrary; it is the only choice consistent with both optimality and feasibility."
  explanation: "This is what makes the saddle path a prediction, not just a mathematical artifact. In the Ramsey model, consumption is the 'jumping' variable — it can be chosen freely in each period. Capital is 'predetermined' — it can't jump. So after a shock, the agent immediately sets consumption to the saddle path value. Any other choice leads to a path the agent knows will eventually violate a feasibility constraint, so rational agents never choose it."
```

## Explainer

In a growth model like the Solow model, the economy accumulates capital over time: workers save part of their income, and that saving becomes new machines, buildings, and equipment. But capital also depreciates — it wears out. The **steady state** is the point where these two forces exactly balance: new investment replaces depreciated capital, and the capital-per-worker ratio stops changing. Think of it like filling a bathtub with a slow leak — the steady state is the water level where inflow equals outflow. Once you reach it, the water level holds constant even though water keeps flowing in and draining out.

To find the steady state mathematically, you set the change in the capital-per-worker ratio to zero and solve the resulting equation. In the Solow model, this means solving sf(k) = (n + δ)k, where s is the savings rate, f(k) is per-capita output, n is population growth, and δ is the depreciation rate. The solution k* gives you the long-run capital stock, and from it you can derive steady-state output, consumption, and investment. The power of this approach is that it collapses a dynamic system — one that evolves over time — into a single algebraic problem about where the system eventually rests.

But finding the steady state is only half the question. You also need to know whether the economy actually converges to it after a shock, and this is where your background in **eigenvalues** and **systems of linear equations** becomes essential. To analyze stability, you linearize the dynamic system around the steady state — essentially taking a first-order Taylor approximation — and examine the eigenvalues of the resulting Jacobian matrix. If all eigenvalues have negative real parts, the steady state is **stable**: small perturbations decay over time and the economy returns to equilibrium. If any eigenvalue has a positive real part, the system is unstable in that direction, meaning some shocks push the economy permanently away from the steady state.

In richer models like the Ramsey-Cass-Koopmans model, the steady state involves two variables (capital and consumption), and the linearized system produces a 2×2 matrix with two eigenvalues. The typical result is one negative and one positive eigenvalue, creating a **saddle-point stability**: there is exactly one path — the **saddle path** — along which the economy converges to the steady state. All other paths eventually diverge. This is why forward-looking agents must "jump" to the saddle path immediately after a shock; any other initial consumption choice leads to an economically impossible outcome (zero consumption or infinite capital). The eigenvalue structure thus determines not just whether the economy converges, but how it converges and what the transition dynamics look like along the way.
