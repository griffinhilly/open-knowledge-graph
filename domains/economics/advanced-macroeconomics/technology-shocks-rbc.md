---
id: technology-shocks-rbc
title: Technology Shocks and Propagation Mechanisms
domain: economics
course: advanced-macroeconomics
prerequisites:
- id: real-business-cycle-theory
  type: hard
builds-toward:
- new-keynesian-framework
tags:
- shocks
- propagation
- technology
stage: formal-systems
status: draft
---

# Technology Shocks and Propagation Mechanisms

## Core Idea
Technology shocks are changes in total factor productivity that shift the production function. RBC models show that a positive technology shock causes agents to increase investment and hours worked (as future returns to capital are higher), generating co-movement of output, consumption, and investment. Persistence in technology shocks and agents' expectations of future productivity are crucial for explaining why shocks have long-lived effects on the economy and are central to understanding business cycle propagation.

## Explainer

From real business cycle theory, you know that RBC models explain economic fluctuations as optimal responses to real disturbances rather than as market failures. The most important of these disturbances is the **technology shock** — a change in **total factor productivity (TFP)** that shifts how efficiently the economy converts inputs into output. Think of it concretely: a new software platform that lets every worker produce 5% more with the same hours and capital. The production function Y = A·F(K, L) shifts upward when A increases, meaning every combination of capital and labor now yields more output.

The interesting question is not that a productivity improvement raises output — that is mechanical — but *how* rational agents respond to it and *why* those responses generate the patterns we observe in business cycles. When TFP rises, the **marginal product of both capital and labor** increases. Higher returns to capital make investment more attractive, so firms invest more today to have more capital in the productive future. Higher wages from the productivity boost induce workers to supply more labor — this is the **intertemporal substitution of labor** at work. Workers recognize that their time is temporarily more valuable and shift leisure to less productive periods. The result is that output, consumption, investment, and hours worked all rise together, which matches the **co-movement** we observe in actual business cycle data.

**Persistence** is the critical ingredient that separates a meaningful theory from a trivial one. If technology shocks were purely temporary — lasting a single quarter — their effects would be too brief to resemble actual recessions and expansions. RBC models typically assume that TFP follows an **autoregressive process** (often AR(1)), where today's productivity level is highly correlated with tomorrow's. A positive shock of, say, 1% might decay by only 5–10% per quarter, meaning its effects linger for years. This persistence is what generates the **propagation mechanism**: agents, knowing that productivity will remain elevated, spread their response across many periods through investment in physical capital and through consumption smoothing. Capital accumulation acts as an internal amplifier — the additional investment from the shock builds a larger capital stock, which keeps output elevated even as the original shock fades.

The debate around technology shocks centers on whether they are truly the dominant source of business cycles. Critics point out that it is hard to identify what a negative technology shock looks like — economies rarely "forget" how to produce things. Empirical work using structural VARs has produced conflicting evidence on whether positive technology shocks actually increase or decrease hours worked in the short run. Despite these challenges, the technology shock framework remains foundational because it established the methodological template for modern macroeconomics: write down an explicit model with optimizing agents, specify the stochastic process driving the economy, and test whether the model's simulated moments match the data. Even New Keynesian models that add price stickiness and monetary policy build directly on this RBC foundation.
