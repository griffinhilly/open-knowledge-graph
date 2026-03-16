---
id: dsge-models
title: 'DSGE Models: Dynamic Stochastic General Equilibrium'
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: new-keynesian-framework
  type: hard
- id: phillips-curve-new-keynesian
  type: hard
- id: constrained-optimization-lagrange
  type: soft
- id: eigenvalues-eigenvectors
  type: soft
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: linear-transformations
  type: soft
- id: systems-of-linear-equations
  type: soft
- id: matrix-operations
  type: soft
builds-toward:
- monetary-policy-transmission
- fiscal-multipliers-macro
tags:
- dsge
- general-equilibrium
- stochastic
stage: formal-systems
status: draft
---

# DSGE Models: Dynamic Stochastic General Equilibrium

## Core Idea
DSGE models integrate microeconomic optimization with macroeconomic outcomes under uncertainty. Households and firms solve dynamic problems subject to constraints and expectations; aggregate equilibrium clears markets while agents are subject to exogenous shocks. DSGE models allow simulation of policy experiments and analysis of how shocks propagate through the economy. They form the baseline framework for modern central bank analysis of monetary policy and represent the state-of-the-art tool for macroeconomic forecasting and policy evaluation.

## Explainer

You already know the New Keynesian framework and the Phillips curve relationship between inflation and output. DSGE models are the formal machinery that makes these ideas rigorous and quantitatively operational. The name itself is the roadmap: **Dynamic** means agents make decisions over time, weighing today against tomorrow. **Stochastic** means the economy is hit by random shocks — technology changes, oil price spikes, shifts in consumer confidence. **General Equilibrium** means all markets (goods, labor, bonds) clear simultaneously, and every agent's choices are consistent with every other agent's choices.

A canonical DSGE model has three blocks. The **household block** specifies a representative consumer who maximizes lifetime utility over consumption and leisure, subject to a budget constraint. This yields an Euler equation — the intertemporal optimality condition you know from constrained optimization — linking today's consumption to expected future consumption and the real interest rate. The **firm block** specifies producers who set prices, often with Calvo-style staggered pricing (only a random fraction of firms can adjust prices each period), generating the New Keynesian Phillips curve as an equilibrium relationship. The **policy block** specifies a central bank following a Taylor-type rule, raising interest rates when inflation or output exceeds target. Together, these three blocks — typically expressed as a system of linearized difference equations — fully determine the dynamic response of output, inflation, and interest rates to any shock.

Solving the model requires the linear algebra from your prerequisites. After log-linearizing around a steady state, the model reduces to a system of the form **E_t[x_{t+1}] = A·x_t + B·ε_t**, where x is the vector of state variables and ε represents shocks. The eigenvalues of the matrix A determine whether the system has a unique stable solution — the **Blanchard-Kahn conditions** require exactly as many explosive eigenvalues as there are forward-looking (jump) variables. This is where your knowledge of eigenvalues and systems of linear equations pays off directly: checking these conditions and computing impulse response functions is fundamentally an exercise in matrix algebra.

The power of DSGE models lies in **counterfactual policy analysis**. Because the model is built from optimization problems, its structure does not change when policy changes — unlike reduced-form statistical models, which suffer from the Lucas critique. You can ask: "What would happen to inflation if the central bank responded more aggressively to output gaps?" and get an answer that accounts for how households and firms would adjust their behavior to the new rule. This is why central banks from the Federal Reserve to the ECB maintain large DSGE models as core tools. The limitation is that the models' predictions are only as good as their assumptions — the representative agent, rational expectations, and specific functional forms — and the 2008 crisis exposed how much standard DSGE models missed by omitting financial frictions and heterogeneous agents.
