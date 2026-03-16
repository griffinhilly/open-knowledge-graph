---
id: dsge-model-foundations
title: Dynamic Stochastic General Equilibrium Models
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: new-keynesian-framework-overview
  type: hard
- id: bellman-equation-dynamic-programming
  type: soft
tags:
- dsge-models
- general-equilibrium
- stochastic-shocks
stage: advanced
status: draft
---

# Dynamic Stochastic General Equilibrium Models

## Core Idea
DSGE models combine dynamic optimization by agents (Euler equations, Bellman equations), imperfect competition, and nominal frictions in a general equilibrium framework. Agents optimize given expectations; all markets clear; equilibrium outcomes depend on stochastic processes for productivity, monetary policy, fiscal policy, and other disturbances.

## Explainer

You already know the New Keynesian framework: firms set prices with some stickiness, a central bank follows an interest rate rule, and output is demand-determined in the short run. A **DSGE model** is the full formal machinery that makes this framework rigorous. The acronym tells you what it does. **Dynamic**: agents make decisions today that depend on what they expect tomorrow — households choose how much to consume versus save, firms choose prices knowing they may be stuck with them for several periods. **Stochastic**: the economy is buffeted by random shocks — productivity changes, monetary policy surprises, shifts in government spending — and agents must optimize under this uncertainty. **General Equilibrium**: all markets (goods, labor, bonds) clear simultaneously, so every agent's decisions are consistent with every other agent's decisions.

The building blocks are familiar from your prerequisite work. Households maximize lifetime utility subject to a budget constraint, yielding an **Euler equation** that links today's consumption to tomorrow's expected consumption and the real interest rate. Firms maximize profits subject to a production function and pricing frictions (typically Calvo-style staggered price-setting, where only a random fraction of firms can adjust prices each period). A central bank sets the nominal interest rate according to a **Taylor rule** that responds to inflation and output deviations. The model is closed by market-clearing conditions: total demand equals total supply in every market, every period.

What makes DSGE models powerful — and difficult — is that everything is **simultaneously determined**. A productivity shock lowers marginal costs, which lets firms that can reprice cut prices, which raises real money balances, which affects consumption decisions, which changes labor demand, which feeds back to marginal costs. The equilibrium is the fixed point where all these feedback loops are mutually consistent. In practice, the nonlinear system of equations is solved by **log-linearizing** around a steady state: expressing each variable as a percentage deviation from its long-run value and solving the resulting system of linear difference equations. This yields **impulse response functions** showing how each variable responds over time to a one-standard-deviation shock.

The standard medium-scale DSGE model (like the Smets-Wouters model used at central banks) adds further frictions to match data: **habit formation** in consumption (utility depends on the change in consumption, not just the level), **investment adjustment costs** (it is costly to change the rate of investment quickly), **wage stickiness** (workers also face Calvo-style frictions in wage setting), and **variable capital utilization** (firms can run machines harder in booms). Each friction adds a wedge between the frictionless benchmark and observed behavior, and the model is estimated by matching these wedges to macroeconomic time series using Bayesian methods. The result is a disciplined framework for policy analysis: you can ask "what happens if the central bank raises rates by 50 basis points?" and trace the full general-equilibrium response through every market in the economy.
