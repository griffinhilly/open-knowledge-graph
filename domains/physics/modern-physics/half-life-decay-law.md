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
- id: exponential-growth-and-decay
  type: soft
- id: natural-logarithm-and-e
  type: soft
builds-toward:
- nuclear-fission-fusion
tags:
- nuclear
- half-life
- decay-constant
- exponential
- carbon-dating
stage: advanced
status: validated
---

# Half-Life and the Radioactive Decay Law

## Core Idea
The number of undecayed nuclei decreases exponentially: N(t) = N₀ e^(−λt), where λ is the decay constant (probability of decay per unit time per nucleus). The half-life T½ = ln2/λ is the time for half the nuclei to decay, independent of how many remain. The activity A = λN also decays exponentially. Because each nucleus decays independently with fixed probability, the decay law is exact on average for large N and follows from Poisson statistics. Applications include radiocarbon dating, medical isotopes, and nuclear waste management.

## How It's Best Learned
Derive N(t) by solving the first-order ODE dN/dt = −λN. Practice computing the amount remaining after multiple half-lives without a calculator. For carbon-14 dating, work backward from activity ratio to time.

## Common Misconceptions
- After two half-lives none of the material remains — after two half-lives one-quarter remains; the material never fully disappears in finite time.
- The decay law implies you can predict exactly when a nucleus will decay — the law predicts average rates; individual decays are random quantum events with no deterministic schedule.

## Explainer

You already know from your study of radioactive decay that unstable nuclei spontaneously transform, emitting particles or radiation. The key insight of the decay law is that every nucleus decays independently and randomly, with a fixed probability λ per unit time — the **decay constant**. Because probability is constant in time, a nucleus that has been sitting undecayed for a million years is no more likely to decay in the next second than a freshly created nucleus. This memoryless property is what makes radioactive decay fundamentally different from, say, a person aging.

From your study of exponential functions, you know that the equation dN/dt = −λN describes a quantity whose rate of change is proportional to itself. Solving this gives N(t) = N₀ e^(−λt): the number of remaining nuclei decays exponentially. The constant λ sets the timescale. Define the **half-life** T½ as the time for N to fall to N₀/2. Setting e^(−λT½) = 1/2 and taking the natural logarithm gives T½ = ln(2)/λ ≈ 0.693/λ. Crucially, T½ depends only on the nuclear species — not on temperature, pressure, chemical form, or how many nuclei remain. After each additional half-life, exactly half the remaining nuclei decay, regardless of how much time has already passed.

The activity A = λN is the number of decays per second (measured in becquerels, Bq). Since N decays exponentially, so does A: A(t) = A₀ e^(−λt) = A₀ · 2^(−t/T½). When solving problems without a calculator, counting in half-lives is often easier: after n half-lives, the fraction remaining is (1/2)^n. After 10 half-lives, less than 0.1% remains; nothing is truly gone in finite time, but the levels become negligible.

**Radiocarbon dating** illustrates these ideas concretely. Living organisms continuously exchange carbon with the atmosphere, maintaining a fixed ratio of ¹⁴C (T½ = 5,730 years) to ¹²C. When an organism dies, exchange stops and ¹⁴C begins decaying. Measuring the ¹⁴C/¹²C ratio in a sample and comparing it to the atmospheric standard gives the elapsed time t = (T½/ln2) × ln(A₀/A). The method works reliably for materials up to about 50,000 years old — beyond that, too little ¹⁴C remains to measure accurately. Longer-lived isotopes like ²³⁸U (T½ = 4.5 billion years) are used for geological timescales by the same logic.
