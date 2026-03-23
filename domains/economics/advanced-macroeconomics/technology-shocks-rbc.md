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
stage: expert
status: draft
---

# Technology Shocks and Propagation Mechanisms

## Core Idea
Technology shocks are changes in total factor productivity that shift the production function. RBC models show that a positive technology shock causes agents to increase investment and hours worked (as future returns to capital are higher), generating co-movement of output, consumption, and investment. Persistence in technology shocks and agents' expectations of future productivity are crucial for explaining why shocks have long-lived effects on the economy and are central to understanding business cycle propagation.

## Questions

```yaml
- question: "In an RBC model, a positive technology shock causes hours worked to rise. Which mechanism best explains this?"
  type: multiple-choice
  options:
    - "Workers are forced to work more because firms hire aggressively during expansions"
    - "Rational workers recognize their time is temporarily more valuable and substitute leisure from today into lower-productivity future periods"
    - "Output prices fall due to higher productivity, causing workers to demand higher wages and work more"
    - "Government automatically increases labor supply by cutting unemployment benefits during expansions"
  answer: 1
  explanation: "This is intertemporal substitution of labor: rational workers recognize that the technology shock has temporarily raised wages. They optimally shift leisure into the future, when productivity and wages will be relatively lower. This is not a forced or price-driven response — it is a rational intertemporal trade. The RBC framework interprets business cycle fluctuations in hours as optimal responses to changing incentives, not as market failures or deviations from equilibrium."

- question: "Critics of RBC theory note that empirical evidence on whether positive technology shocks increase or decrease hours worked in the short run is mixed. What aspect of the model does this criticism most directly challenge?"
  type: multiple-choice
  options:
    - "The assumption that capital depreciates over time"
    - "The claim that technology shocks are the dominant source of business cycles"
    - "The use of logarithmic utility functions in the model"
    - "The autoregressive specification of the TFP process"
  answer: 1
  explanation: "If positive technology shocks actually decreased hours worked in the short run (as some structural VAR studies suggest), the co-movement predicted by the model — output, consumption, investment, and hours all rising together — breaks down. This challenges the core claim that technology shocks drive business cycles. The intertemporal substitution mechanism predicts hours rise with positive shocks; if data shows otherwise, technology shocks may not be the dominant driver even if the mechanism itself is valid."

- question: "In RBC models, a technology shock has long-lasting effects on the economy primarily because the shock itself is assumed to be permanent."
  type: true-false
  answer: false
  explanation: "RBC models typically assume technology follows an autoregressive (AR) process — the shock is persistent but not permanent; it decays slowly over time. The long-lasting effects arise from the model's propagation mechanism: rational agents invest heavily in capital in response to elevated productivity, and that capital stock remains elevated even after the original shock has largely dissipated. Capital accumulation is the internal amplifier that converts a transient productivity improvement into a prolonged expansion."

- question: "A model that treats business cycles as equilibrium responses to technology shocks implies that monetary policy has no role in stabilizing the economy."
  type: true-false
  answer: true
  explanation: "In a pure RBC model, business cycle fluctuations are optimal responses to real disturbances — there are no market failures to correct. If expansions reflect workers rationally working more when productivity is high, and recessions reflect optimal leisure, then policy intervention cannot improve welfare; it can only distort otherwise efficient choices. Monetary policy stabilization only makes sense when prices are sticky and monetary transmission affects real activity, which is why New Keynesian models that add price rigidity to the RBC core give monetary policy a stabilizing role."

- question: "Why is the persistence of technology shocks — rather than their magnitude — considered the critical ingredient for explaining business cycle dynamics in RBC models?"
  type: short-answer
  answer: "A one-period productivity improvement would cause output to spike and immediately return to trend, not generating the prolonged expansions and contractions characteristic of actual business cycles. Persistence means elevated productivity lasts multiple periods, giving agents time to respond dynamically: they invest more in capital (which takes time to install and produces returns over many periods) and smooth consumption over the expansion. The accumulating capital stock then propagates the effect forward even as the underlying productivity shock fades. Without persistence, there is no propagation mechanism and the model produces fluctuations far too brief to resemble real business cycles."
  explanation: "This connects the AR(1) assumption about TFP to the observable duration of business cycles. A shock decaying by only 5–10% per quarter will have effects visible 2–3 years later, matching typical expansion lengths. The investment response is also duration-dependent: firms invest in new capital only if they expect favorable conditions to persist long enough for the investment to pay off. Persistence is what makes rational-agent responses generate long-lived macroeconomic dynamics."
```

## Explainer

From real business cycle theory, you know that RBC models explain economic fluctuations as optimal responses to real disturbances rather than as market failures. The most important of these disturbances is the **technology shock** — a change in **total factor productivity (TFP)** that shifts how efficiently the economy converts inputs into output. Think of it concretely: a new software platform that lets every worker produce 5% more with the same hours and capital. The production function Y = A·F(K, L) shifts upward when A increases, meaning every combination of capital and labor now yields more output.

The interesting question is not that a productivity improvement raises output — that is mechanical — but *how* rational agents respond to it and *why* those responses generate the patterns we observe in business cycles. When TFP rises, the **marginal product of both capital and labor** increases. Higher returns to capital make investment more attractive, so firms invest more today to have more capital in the productive future. Higher wages from the productivity boost induce workers to supply more labor — this is the **intertemporal substitution of labor** at work. Workers recognize that their time is temporarily more valuable and shift leisure to less productive periods. The result is that output, consumption, investment, and hours worked all rise together, which matches the **co-movement** we observe in actual business cycle data.

**Persistence** is the critical ingredient that separates a meaningful theory from a trivial one. If technology shocks were purely temporary — lasting a single quarter — their effects would be too brief to resemble actual recessions and expansions. RBC models typically assume that TFP follows an **autoregressive process** (often AR(1)), where today's productivity level is highly correlated with tomorrow's. A positive shock of, say, 1% might decay by only 5–10% per quarter, meaning its effects linger for years. This persistence is what generates the **propagation mechanism**: agents, knowing that productivity will remain elevated, spread their response across many periods through investment in physical capital and through consumption smoothing. Capital accumulation acts as an internal amplifier — the additional investment from the shock builds a larger capital stock, which keeps output elevated even as the original shock fades.

The debate around technology shocks centers on whether they are truly the dominant source of business cycles. Critics point out that it is hard to identify what a negative technology shock looks like — economies rarely "forget" how to produce things. Empirical work using structural VARs has produced conflicting evidence on whether positive technology shocks actually increase or decrease hours worked in the short run. Despite these challenges, the technology shock framework remains foundational because it established the methodological template for modern macroeconomics: write down an explicit model with optimizing agents, specify the stochastic process driving the economy, and test whether the model's simulated moments match the data. Even New Keynesian models that add price stickiness and monetary policy build directly on this RBC foundation.
