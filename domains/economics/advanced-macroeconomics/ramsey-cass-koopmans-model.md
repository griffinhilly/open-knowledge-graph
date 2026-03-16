---
id: ramsey-cass-koopmans-model
title: Ramsey-Cass-Koopmans Model
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: dynamic-optimization-macro
  type: hard
- id: consumer-optimum
  type: hard
- id: lagrange-multipliers
  type: soft
- id: constrained-optimization-lagrange
  type: soft
- id: constrained-optimization
  type: hard
- id: differential-equations-intro
  type: hard
- id: calculus
  type: hard
builds-toward:
- endogenous-growth-theory
tags:
- consumption-saving
- intertemporal-optimization
- endogenous-savings
stage: advanced
status: draft
---

# Ramsey-Cass-Koopmans Model

## Core Idea
The Ramsey-Cass-Koopmans model endogenizes savings behavior by having infinitely-lived households optimize consumption over time subject to intertemporal budget constraints and dynamic capital accumulation. Savings and consumption respond to interest rates, discount rates, and expectations about future income, creating richer short-run and long-run dynamics than the exogenous-savings Solow model. This framework demonstrates how optimal consumption paths align with capital accumulation and provides foundations for analyzing fiscal policy and monetary policy effects on savings.

## Explainer

The Solow model treats the savings rate as a fixed parameter — households save a constant fraction of income regardless of circumstances. The Ramsey-Cass-Koopmans (RCK) model removes this shortcut by asking: what would forward-looking households actually choose to save? The answer comes from the same constrained optimization tools you learned with consumer theory and Lagrange multipliers, extended into continuous time using differential equations. Households maximize lifetime utility — the discounted sum of instantaneous utility from consumption over an infinite horizon — subject to the constraint that their wealth evolves according to income earned, consumption spent, and returns on accumulated capital.

The central result is the **Euler equation** (also called the Keynes-Ramsey rule), which governs how consumption grows over time. It says consumption growth is positive when the marginal product of capital exceeds the household's discount rate — when the return to saving outweighs impatience. If capital is scarce and productive, households defer consumption to build wealth. As capital accumulates and its marginal product falls, consumption growth slows until the economy reaches a **steady state** where the return to capital exactly compensates for impatience and any depreciation. This is the same steady-state logic as the Solow model, but now the savings rate adjusts endogenously along the transition path rather than being imposed from outside.

The dynamics of the RCK model are best understood through a **phase diagram** in capital-consumption space. The system has two key curves: one where capital is constant (investment equals depreciation) and one where consumption is constant (the Euler equation holds with zero growth). Their intersection is the steady state. Most initial conditions lead to paths that diverge — either consumption explodes and capital collapses, or consumption collapses and capital overshoots. Only one path, the **saddle path**, converges to the steady state, and rational forward-looking households select exactly this path. This saddle-path stability is what makes the model determinate: given any initial capital stock, there is a unique optimal consumption level.

Why does this matter beyond the Solow model? Because savings behavior now responds to policy. A temporary tax increase causes households to smooth consumption by drawing down savings — something the Solow model cannot capture. A permanent increase in government spending crowds out capital accumulation because households, facing lower lifetime wealth, reduce saving. The RCK model also eliminates the **dynamic inefficiency** problem possible in the Solow model: optimizing households never over-accumulate capital past the golden rule, because doing so would mean the return on saving falls below their discount rate and they would rationally consume more instead. This framework forms the backbone of modern dynamic macroeconomics and is the starting point for models of endogenous growth, real business cycles, and new Keynesian DSGE models.
