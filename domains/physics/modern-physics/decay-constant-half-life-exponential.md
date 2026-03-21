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
stage: advanced
status: draft
---

# Radioactive Decay Constant and Half-Life

## Core Idea
Radioactive decay follows the exponential law N(t) = N₀e^(−λt), where λ is the decay constant. The half-life t₁/₂ = (ln 2)/λ is the time for half the nuclei to decay and is independent of the sample size or initial amount. Different isotopes have vastly different half-lives (from nanoseconds to billions of years), determined by nuclear structure and the competing decay modes.

## Questions

```yaml
- question: "A hospital has 10¹² atoms of technetium-99m (half-life 6 hours); a research lab has only 10⁶ atoms of the same isotope. After 6 hours, what fraction of each sample remains?"
  type: multiple-choice
  options:
    - "Half of both samples — the half-life is a property of the isotope, independent of sample size"
    - "The hospital sample retains more than half because large samples have lower activity per atom"
    - "The research lab sample retains more because fewer atoms means less inter-nuclear interaction"
    - "The half-life predicts nothing without knowing the initial activity of each sample"
  answer: 0
  explanation: "The half-life is a property of the isotope, not the sample. Each nucleus independently has the same fixed probability per unit time (λ) of decaying, regardless of how many other nuclei are present. After one half-life, exactly half the nuclei in any sample — large or small — will have decayed, on average. The hospital's 10¹² atoms reduce to ~5×10¹¹; the lab's 10⁶ reduce to ~5×10⁵. The fraction remaining is (1/2) for both. This is a direct consequence of the memoryless, probabilistic nature of radioactive decay."

- question: "Carbon-14 has a half-life of 5,730 years. An ancient organic artifact contains 1/8 of the C-14 found in living organisms. Approximately how old is the artifact?"
  type: multiple-choice
  options:
    - "About 5,730 years — one half-life accounts for the reduction"
    - "About 11,460 years — 1/8 requires two halvings"
    - "About 17,190 years — three half-lives, since (1/2)³ = 1/8"
    - "Cannot be determined without knowing the original C-14 concentration"
  answer: 2
  explanation: "After n half-lives, the fraction remaining is (1/2)^n. If 1/8 remains, then (1/2)^n = 1/8 = (1/2)³, so n = 3 half-lives. The artifact is 3 × 5,730 = 17,190 years old. The original C-14 concentration does not need to be measured independently — it is assumed to equal that of living organisms (set by atmospheric equilibrium), and the ratio of C-14 to stable C-12 in the artifact provides the fraction remaining."

- question: "A radioactive nucleus that has existed for 100 years without decaying is more likely to decay in the next second than a freshly created nucleus of the same isotope."
  type: true-false
  answer: false
  explanation: "Radioactive decay is a memoryless quantum process: the probability per unit time of decaying (the decay constant λ) is fixed by nuclear structure and does not change with the age of the nucleus. A nucleus that has 'survived' for 100 years has the same probability per second of decaying as a nucleus created one second ago. This memorylessness is a fundamental property of quantum tunneling and exponential distributions — there is no accumulation of 'pressure to decay' over time. This is why the half-life is constant and independent of the sample's history."

- question: "An isotope with a shorter half-life has higher activity (more decays per second) per atom than an isotope with a longer half-life, given the same number of atoms."
  type: true-false
  answer: true
  explanation: "Activity A = λN = (ln 2 / t₁/₂) × N. For a fixed number of atoms N, shorter half-life means larger λ, hence higher activity per atom. This is why polonium-213 (half-life ~4 microseconds) is extraordinarily radioactive — each atom decays almost immediately — while uranium-238 (half-life 4.5 billion years) has nearly negligible activity per atom but persists indefinitely. This trade-off governs medical isotope selection: technetium-99m (6-hour half-life) is intense enough to detect but short-lived enough to be safe."

- question: "Why does the half-life of a radioactive isotope remain constant regardless of sample size, temperature, or how old the nuclei are?"
  type: short-answer
  answer: "Because radioactive decay is a probabilistic, memoryless quantum process. Each nucleus has an intrinsic, fixed probability per unit time (λ) of decaying, determined solely by nuclear structure. This probability does not change with time (no memory), is unaffected by neighboring nuclei (no collective effect), and is independent of temperature or pressure (no classical trigger needed). The half-life t₁/₂ = ln2/λ depends only on λ, which is a property of the isotope. Since all nuclei of a given isotope share the same λ, the half-life is the same regardless of how many there are, how old they are, or what conditions they are in."
  explanation: "This contrasts with macroscopic processes like chemical reactions, where temperature and concentration dramatically affect rates. Radioactive decay is governed by quantum mechanics (tunneling through the nuclear potential barrier), not classical thermodynamics. The only way to change a nucleus's decay rate is to change its nuclear structure — which is why chemical or thermal manipulation cannot speed or slow nuclear decay, a fact that was once considered deeply surprising."
```

## Explainer

Radioactive decay is fundamentally probabilistic: each nucleus has a fixed probability per unit time of decaying, regardless of how old it is, how many other nuclei are nearby, or what temperature or pressure it is under. That constant probability per unit time is the **decay constant** λ. If you have N nuclei at time t, the rate at which they decay is proportional to how many you have: dN/dt = -λN. This is the defining equation of exponential decay, and its solution is N(t) = N₀e^(-λt), where N₀ is the initial number. The exponential shape arises directly from the memoryless property of radioactive decay — a nucleus has no "memory" of how long it has existed.

The **half-life** t₁/₂ is the time after which exactly half the original nuclei remain. Setting N(t₁/₂) = N₀/2 and solving gives t₁/₂ = (ln 2)/λ ≈ 0.693/λ. This is a fixed property of the isotope — it doesn't depend on N₀, so a sample of 10¹² atoms and a sample of 10⁶ atoms of the same isotope both have the same half-life. After one half-life, half remain; after two half-lives, one quarter; after three, one eighth. After n half-lives, the fraction remaining is (1/2)^n. The **activity** A = λN gives the number of decays per second (measured in becquerels, Bq); it also decays exponentially with the same half-life as N.

Half-lives span an extraordinary range. Polonium-213 has a half-life of about 4 microseconds; carbon-14 has a half-life of 5,730 years (the basis of radiocarbon dating); uranium-238 has a half-life of 4.5 billion years, comparable to the age of the solar system. This range reflects the vastly different quantum tunneling probabilities and nuclear energy differences involved in alpha, beta, and gamma decay. For carbon-14 dating, the long half-life means the isotope is still present in measurable quantities in organic material from thousands of years ago; the ratio of C-14 to stable C-12 tells you how long ago the organism stopped exchanging carbon with the atmosphere.

A practical insight: because activity A = λN = N(ln 2)/t₁/₂, an isotope with a very short half-life has very high activity per atom but disappears quickly, while an isotope with a long half-life has low activity per atom but persists nearly indefinitely. This is why medically useful radioisotopes for imaging (like technetium-99m with a 6-hour half-life) are chosen to be intense enough to detect but short-lived enough to be safe. The exponential law also appears in nuclear reactor kinetics, radioactive waste management calculations, and geologic age dating — any situation where a fixed fraction of a population transforms per unit time follows the same mathematics.
