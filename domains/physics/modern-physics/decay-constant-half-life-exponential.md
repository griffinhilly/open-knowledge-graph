---
id: decay-constant-half-life-exponential
title: Radioactive Decay Constant and Half-Life
domain: physics
course: modern-physics
prerequisites:
- id: alpha-decay-emission
  type: soft
- id: beta-decay-emission
  type: soft
- id: gamma-decay-emission
  type: soft
tags:
- nuclear
- radioactivity
- exponential
stage: abstract-reasoning
status: draft
---

# Radioactive Decay Constant and Half-Life

## Core Idea
Radioactive decay follows the exponential law N(t) = N₀e^(−λt), where λ is the decay constant. The half-life t₁/₂ = (ln 2)/λ is the time for half the nuclei to decay and is independent of the sample size or initial amount. Different isotopes have vastly different half-lives (from nanoseconds to billions of years), determined by nuclear structure and the competing decay modes.

## Explainer

Radioactive decay is fundamentally probabilistic: each nucleus has a fixed probability per unit time of decaying, regardless of how old it is, how many other nuclei are nearby, or what temperature or pressure it is under. That constant probability per unit time is the **decay constant** λ. If you have N nuclei at time t, the rate at which they decay is proportional to how many you have: dN/dt = -λN. This is the defining equation of exponential decay, and its solution is N(t) = N₀e^(-λt), where N₀ is the initial number. The exponential shape arises directly from the memoryless property of radioactive decay — a nucleus has no "memory" of how long it has existed.

The **half-life** t₁/₂ is the time after which exactly half the original nuclei remain. Setting N(t₁/₂) = N₀/2 and solving gives t₁/₂ = (ln 2)/λ ≈ 0.693/λ. This is a fixed property of the isotope — it doesn't depend on N₀, so a sample of 10¹² atoms and a sample of 10⁶ atoms of the same isotope both have the same half-life. After one half-life, half remain; after two half-lives, one quarter; after three, one eighth. After n half-lives, the fraction remaining is (1/2)^n. The **activity** A = λN gives the number of decays per second (measured in becquerels, Bq); it also decays exponentially with the same half-life as N.

Half-lives span an extraordinary range. Polonium-213 has a half-life of about 4 microseconds; carbon-14 has a half-life of 5,730 years (the basis of radiocarbon dating); uranium-238 has a half-life of 4.5 billion years, comparable to the age of the solar system. This range reflects the vastly different quantum tunneling probabilities and nuclear energy differences involved in alpha, beta, and gamma decay. For carbon-14 dating, the long half-life means the isotope is still present in measurable quantities in organic material from thousands of years ago; the ratio of C-14 to stable C-12 tells you how long ago the organism stopped exchanging carbon with the atmosphere.

A practical insight: because activity A = λN = N(ln 2)/t₁/₂, an isotope with a very short half-life has very high activity per atom but disappears quickly, while an isotope with a long half-life has low activity per atom but persists nearly indefinitely. This is why medically useful radioisotopes for imaging (like technetium-99m with a 6-hour half-life) are chosen to be intense enough to detect but short-lived enough to be safe. The exponential law also appears in nuclear reactor kinetics, radioactive waste management calculations, and geologic age dating — any situation where a fixed fraction of a population transforms per unit time follows the same mathematics.
