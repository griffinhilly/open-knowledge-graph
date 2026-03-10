---
id: half-life-decay-law
title: Half-Life and the Radioactive Decay Law
domain: physics
course: modern-physics
prerequisites:
- id: radioactive-decay
  type: hard
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- nuclear-fission-fusion
tags:
- nuclear
- half-life
- decay-constant
- exponential
- carbon-dating
stage: advanced
status: draft
---

# Half-Life and the Radioactive Decay Law

## Core Idea
The number of undecayed nuclei decreases exponentially: N(t) = N₀ e^(−λt), where λ is the decay constant (probability of decay per unit time per nucleus). The half-life T½ = ln2/λ is the time for half the nuclei to decay, independent of how many remain. The activity A = λN also decays exponentially. Because each nucleus decays independently with fixed probability, the decay law is exact on average for large N and follows from Poisson statistics. Applications include radiocarbon dating, medical isotopes, and nuclear waste management.

## How It's Best Learned
Derive N(t) by solving the first-order ODE dN/dt = −λN. Practice computing the amount remaining after multiple half-lives without a calculator. For carbon-14 dating, work backward from activity ratio to time.

## Common Misconceptions
- After two half-lives none of the material remains — after two half-lives one-quarter remains; the material never fully disappears in finite time.
- The decay law implies you can predict exactly when a nucleus will decay — the law predicts average rates; individual decays are random quantum events with no deterministic schedule.
