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
stage: expert
status: validated
---

# Dynamic Stochastic General Equilibrium Models

## Core Idea
DSGE models combine dynamic optimization by agents (Euler equations, Bellman equations), imperfect competition, and nominal frictions in a general equilibrium framework. Agents optimize given expectations; all markets clear; equilibrium outcomes depend on stochastic processes for productivity, monetary policy, fiscal policy, and other disturbances.

## Questions

```yaml
- question: "Which feature of DSGE models most fundamentally distinguishes them from a reduced-form VAR model used for macroeconomic forecasting?"
  type: multiple-choice
  options:
    - "DSGE models use Bayesian estimation while VARs use maximum likelihood"
    - "All markets clear simultaneously and every agent's optimizing decisions are mutually consistent through general equilibrium, so the model has structural micro-foundations"
    - "DSGE models include stochastic shocks, which VARs cannot capture"
    - "DSGE models are calibrated to match theory, not estimated from data"
  answer: 1
  explanation: "The defining feature is general equilibrium with micro-foundations: households, firms, and a central bank all optimize, and their decisions must be mutually consistent — labor supply equals labor demand, goods market clears, etc. A VAR forecasts statistical patterns in data without asking why agents behave as they do or how markets balance. Option C is wrong — VARs can and do include stochastic shocks. Option D is wrong — medium-scale DSGE models like Smets-Wouters are estimated from data using Bayesian methods."

- question: "In a DSGE model, a positive productivity shock lowers firms' marginal costs. Some price-adjusting firms cut prices. A student argues: 'Lower prices means the analysis is complete — the economy adjusts by reducing inflation.' What critical general equilibrium feedback is this student missing?"
  type: multiple-choice
  options:
    - "The central bank must approve all price changes before they take effect"
    - "Lower prices raise real money balances, which affects consumption decisions through the Euler equation, changing labor demand, which feeds back to marginal costs — all simultaneously"
    - "Wages are sticky, so labor markets cannot clear quickly enough for the analysis to matter"
    - "Calvo pricing means only a random fraction of firms can reprice, so aggregate prices barely change"
  answer: 1
  explanation: "This is the 'simultaneously determined' problem that makes DSGE hard. Lower prices → higher real wealth and consumption (Euler equation responds) → higher labor demand → wages rise → marginal costs rise → partially offsetting the initial shock. Meanwhile the Taylor rule adjusts interest rates, affecting investment... all in the same period. The student's mistake is analyzing a single market in isolation rather than tracing feedback through the entire general equilibrium. This is why log-linearization and solving a system of equations simultaneously is required."

- question: "The 'stochastic' in DSGE means the model's outcomes are fundamentally random and therefore cannot generate reliable predictions about how the economy responds to policy changes."
  type: true-false
  answer: false
  explanation: "Stochastic means the model includes random shocks (productivity, monetary policy surprises, etc.) drawn from specified probability distributions. But the model produces deterministic responses to these shocks — specifically, impulse response functions showing the expected path of each variable following a one-standard-deviation shock. The stochastic structure allows the model to match the variance properties of data, but policy analysis is conducted by simulating specific shock scenarios, not by hoping for randomness to wash out."

- question: "Log-linearizing a DSGE model around a steady state converts the nonlinear system of optimality conditions into a linear system of equations in percentage deviations, which can then be solved analytically for impulse response functions."
  type: true-false
  answer: true
  explanation: "Log-linearization is the standard solution technique. Because the true nonlinear system (with Euler equations, Calvo pricing, Taylor rule, market clearing conditions) has no closed-form solution, researchers approximate by taking first-order Taylor expansions in log-deviations from the deterministic steady state. The resulting linear system CAN be solved analytically (or via matrix methods), giving the impulse response functions. Higher-order approximations exist for when nonlinearity matters, such as at the zero lower bound."

- question: "Why must DSGE models use the general equilibrium approach rather than modeling each market independently? What goes wrong if you analyze labor markets, goods markets, and financial markets in separate partial-equilibrium models?"
  type: short-answer
  answer: "Partial equilibrium analysis holds other markets constant — it cannot capture how changes in one market propagate to and feed back from others. In reality, a monetary policy shock changes interest rates, which affects investment demand (goods market), which changes labor demand (labor market), which affects wages and marginal costs, which affects firms' pricing (goods market again), which affects real balances, which affects consumption (goods market yet again). Each loop requires knowing the others' outcomes simultaneously. Modeling them separately produces inconsistent results: your labor market model assumes goods demand is fixed while your goods market model assumes wages are fixed. General equilibrium solves all markets jointly, finding the fixed point where every agent's decision is consistent with every other's."
  explanation: "The deeper point: macroeconomic policy works through linkages between markets. A model that ignores these linkages cannot trace the full effect of a policy change and will systematically miss second-round effects — which are often as large as the first-round ones."
```

## Explainer

You already know the New Keynesian framework: firms set prices with some stickiness, a central bank follows an interest rate rule, and output is demand-determined in the short run. A **DSGE model** is the full formal machinery that makes this framework rigorous. The acronym tells you what it does. **Dynamic**: agents make decisions today that depend on what they expect tomorrow — households choose how much to consume versus save, firms choose prices knowing they may be stuck with them for several periods. **Stochastic**: the economy is buffeted by random shocks — productivity changes, monetary policy surprises, shifts in government spending — and agents must optimize under this uncertainty. **General Equilibrium**: all markets (goods, labor, bonds) clear simultaneously, so every agent's decisions are consistent with every other agent's decisions.

The building blocks are familiar from your prerequisite work. Households maximize lifetime utility subject to a budget constraint, yielding an **Euler equation** that links today's consumption to tomorrow's expected consumption and the real interest rate. Firms maximize profits subject to a production function and pricing frictions (typically Calvo-style staggered price-setting, where only a random fraction of firms can adjust prices each period). A central bank sets the nominal interest rate according to a **Taylor rule** that responds to inflation and output deviations. The model is closed by market-clearing conditions: total demand equals total supply in every market, every period.

What makes DSGE models powerful — and difficult — is that everything is **simultaneously determined**. A productivity shock lowers marginal costs, which lets firms that can reprice cut prices, which raises real money balances, which affects consumption decisions, which changes labor demand, which feeds back to marginal costs. The equilibrium is the fixed point where all these feedback loops are mutually consistent. In practice, the nonlinear system of equations is solved by **log-linearizing** around a steady state: expressing each variable as a percentage deviation from its long-run value and solving the resulting system of linear difference equations. This yields **impulse response functions** showing how each variable responds over time to a one-standard-deviation shock.

The standard medium-scale DSGE model (like the Smets-Wouters model used at central banks) adds further frictions to match data: **habit formation** in consumption (utility depends on the change in consumption, not just the level), **investment adjustment costs** (it is costly to change the rate of investment quickly), **wage stickiness** (workers also face Calvo-style frictions in wage setting), and **variable capital utilization** (firms can run machines harder in booms). Each friction adds a wedge between the frictionless benchmark and observed behavior, and the model is estimated by matching these wedges to macroeconomic time series using Bayesian methods. The result is a disciplined framework for policy analysis: you can ask "what happens if the central bank raises rates by 50 basis points?" and trace the full general-equilibrium response through every market in the economy.
