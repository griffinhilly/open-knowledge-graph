---
id: real-business-cycle-theory
title: Real Business Cycle Theory
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: solow-growth-model
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-algebra
  type: soft
builds-toward:
- monetary-neutrality-long-run
- new-keynesian-model-baseline
tags:
- business-cycles
- productivity-shocks
- competitive-equilibrium
- flexible-prices
stage: advanced
status: draft
---

# Real Business Cycle Theory

## Core Idea
RBC theory models business cycles as efficient responses to exogenous technology shocks in competitive markets with flexible prices, rational expectations, and perfectly functioning financial markets. Persistent technology shocks drive both output and employment fluctuations through intertemporal substitution and income effects on labor supply, with no involuntary unemployment in equilibrium. RBC models minimize a role for monetary policy in stabilization and predict that output fluctuations reflect optimal responses to real fundamentals rather than nominal frictions.

## Explainer

From the Solow growth model, you already understand how an economy's output depends on capital, labor, and technology, and how the economy converges toward a steady state. Real Business Cycle theory takes that same production-function framework and asks a different question: what if the fluctuations we observe in GDP, employment, and investment are not failures of the market but *optimal responses* to changes in technology? Where Solow treats technology as a smooth trend, RBC introduces **technology shocks** — random, persistent changes in total factor productivity — as the primary driver of business cycles.

The core mechanism works through two channels you can trace back to consumer optimization. When a positive technology shock hits, workers become more productive, so real wages rise. The **income effect** makes workers want to consume more leisure (work less), but the **substitution effect** makes the current period an unusually good time to work (wages are temporarily high relative to future wages). RBC models assume the substitution effect dominates, so labor supply increases during booms. This **intertemporal substitution of labor** is the engine that generates co-movement between output, employment, consumption, and investment — the defining feature of business cycles in the data.

What makes RBC theory provocative is its welfare implication. Because markets are perfectly competitive, prices are fully flexible, and agents have rational expectations, the resulting equilibrium is Pareto efficient. Recessions are not waste — they are the economy's optimal response to a negative productivity shock. If technology regresses temporarily, it is *efficient* for people to work less, invest less, and produce less. This means government stabilization policy — fiscal stimulus, monetary easing — is unnecessary at best and harmful at worst, since it would push the economy away from its efficient response.

The mathematical structure builds on dynamic optimization. A representative agent maximizes expected lifetime utility subject to a budget constraint and the economy's aggregate production function. The solution involves linearizing the system of Euler equations and resource constraints around the steady state, which is where your linear algebra background becomes relevant — the linearized system's dynamics depend on the **eigenvalues** of the coefficient matrix, which determine whether the economy converges back to steady state or diverges after a shock. Stable eigenvalues inside the unit circle generate the hump-shaped impulse responses that RBC models use to match GDP and employment data. The model is then calibrated (not estimated) to match key moments in the data — output volatility, consumption smoothness, investment volatility, and the correlation structure among aggregates.

RBC theory's lasting contribution is methodological even for economists who reject its policy conclusions. It established the **dynamic stochastic general equilibrium (DSGE)** approach as the standard framework in macroeconomics. New Keynesian models, which you will encounter next, keep the DSGE structure but add nominal rigidities and imperfect competition — precisely the frictions RBC assumes away. Understanding RBC is essential because it is the benchmark: every subsequent macro model is defined by which RBC assumptions it relaxes and why.
