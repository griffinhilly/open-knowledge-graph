---
id: dsge-models-framework
title: DSGE Models Framework
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: new-keynesian-model-baseline
  type: hard
- id: rational-expectations-macro
  type: hard
builds-toward:
- financial-frictions-amplification
tags:
- dynamic-models
- general-equilibrium
- stochastic-shocks
- policy-analysis
stage: advanced
status: draft
---

# DSGE Models Framework

## Core Idea
Dynamic Stochastic General Equilibrium (DSGE) models integrate dynamic optimization by households and firms, stochastic shocks to productivity, preferences, monetary policy, and fiscal policy, and equilibrium relationships into a unified framework. They provide rigorous microfoundations while remaining tractable for quantitative analysis, policy simulation, and forecasting. DSGE models incorporating multiple imperfections (sticky prices, financial frictions, search frictions) are workhorses at central banks worldwide for forecasting and monetary policy evaluation.

## Explainer

From your study of the New Keynesian baseline and rational expectations, you already understand the core building blocks: households optimize consumption and labor supply, firms set prices subject to nominal rigidities, a central bank follows a policy rule, and agents form expectations consistent with the model's actual dynamics. A **DSGE model** is the fully assembled machine that connects all of these pieces into a closed system where every market clears, every agent optimizes, and the economy responds dynamically to random disturbances.

The name itself is a roadmap. **Dynamic** means the model tracks how the economy evolves over time — households and firms make decisions today based on expectations about tomorrow, and those decisions feed forward into future states. **Stochastic** means the economy is buffeted by random shocks: a productivity innovation that makes workers suddenly more efficient, a shift in consumer confidence, an unexpected change in monetary policy. These shocks are the impulses that set the economy in motion; the model's structure determines how those impulses propagate and decay. **General Equilibrium** means all markets — goods, labor, bonds, money — clear simultaneously, so every variable is endogenous. There is no partial-equilibrium shortcut where you hold part of the economy fixed while studying another; everything adjusts together.

Building a DSGE model follows a standard workflow. First, specify the optimizing problems: a representative household maximizes lifetime utility over consumption and leisure subject to a budget constraint; a representative firm maximizes profits subject to a production function and price-setting friction (typically Calvo-style staggered pricing from your New Keynesian prerequisite). Second, derive the first-order conditions — Euler equations, labor supply equations, Phillips curves — that characterize optimal behavior. Third, impose market clearing and a monetary policy rule (such as a Taylor rule). Fourth, **log-linearize** around the steady state to obtain a system of linear expectational difference equations. This linearized system can be solved using standard techniques (Blanchard-Kahn conditions, which ensure a unique stable rational expectations equilibrium) and simulated by feeding in stochastic shocks.

The power of DSGE models lies in their ability to ask structured counterfactual questions. What happens if the central bank raises interest rates by 50 basis points? The model traces the full chain: higher rates reduce consumption through the Euler equation, lower demand causes firms to cut prices (slowly, due to nominal rigidity), employment falls, output contracts, and inflation gradually declines. Because the model is internally consistent, every channel operates simultaneously and feeds back on the others. Central banks use these models not because they believe the economy is literally populated by identical optimizing agents, but because the framework disciplines the analysis — every assumed mechanism must be explicit, every response must be consistent with the model's logic, and every shock can be traced from impulse to outcome through **impulse response functions** that reveal the economy's dynamic adjustment path.
