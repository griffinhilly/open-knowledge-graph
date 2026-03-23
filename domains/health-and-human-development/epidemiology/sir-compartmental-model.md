---
id: sir-compartmental-model
title: SIR Compartmental Models for Infectious Disease
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: basic-reproduction-number
  type: hard
builds-toward:
- seir-model-latency
tags:
- compartmental-models
- sir-model
- modeling
- disease-transmission
stage: expert
status: draft
---

# SIR Compartmental Models for Infectious Disease

## Core Idea
The SIR model divides a population into Susceptible, Infected, and Recovered compartments and uses differential equations to model transitions. The force of infection (β × I/N) drives susceptible → infected transitions; the recovery rate (γ) drives infected → recovered transitions. SIR models predict epidemic dynamics, peak timing, and final size, forming the basis for control strategy evaluation.

## Questions

```yaml
- question: "An epidemic with R₀ = 4 is spreading. After the peak, daily cases are declining — but 40% of the population is still susceptible. A student claims: 'The epidemic is declining because the virus is running out of people to infect.' What does the SIR model actually say?"
  type: multiple-choice
  options:
    - "The student is correct — case declines always indicate that susceptibles are nearly exhausted"
    - "Cases are declining because the susceptible fraction has dropped below 1/R₀ = 25%, so each case now generates fewer than one new case on average — not because susceptibles are exhausted"
    - "The epidemic is declining because the virus has mutated to a less transmissible variant"
    - "The model predicts cases cannot decline while 40% of the population remains susceptible"
  answer: 1
  explanation: "Post-peak decline is driven by the epidemic threshold, not by exhaustion of susceptibles. When S/N falls below 1/R₀, the effective reproduction number Rₑ = R₀ × S/N drops below 1, so each infected person generates fewer than one new case and incidence falls. With R₀ = 4, the threshold is S/N = 0.25 — the epidemic peaks and begins declining when 75% are immune, even though 25% (not 0%) remain susceptible. A substantial susceptible fraction always survives uninfected."

- question: "In the SIR model, what does the herd immunity threshold represent?"
  type: multiple-choice
  options:
    - "The fraction of the population that must be vaccinated to achieve zero new infections"
    - "The minimum immune fraction (1 − 1/R₀) at which each infectious case generates on average fewer than one new case, causing incidence to decline"
    - "The fraction of the population that will ultimately be infected before the epidemic ends"
    - "The susceptible fraction below which the pathogen cannot survive at all"
  answer: 1
  explanation: "The herd immunity threshold is 1 − 1/R₀ — the immune fraction at which the effective reproduction number Rₑ falls below 1. It does not require zero susceptibles; it requires enough immune individuals that transmission chains shrink on average. Note that it is not the same as the final attack rate (how many are ultimately infected), which is determined by the final size equation and is always larger than the herd immunity threshold for R₀ > 1."

- question: "In the SIR model, the epidemic reaches its peak number of infectious individuals at exactly the moment the susceptible fraction crosses the herd immunity threshold (S/N = 1/R₀)."
  type: true-false
  answer: true
  explanation: "The peak of I occurs when dI/dt = 0, which requires β(I/N)S − γI = 0, simplifying to S/N = γ/β = 1/R₀. At this exact moment — when the susceptible fraction first equals 1/R₀ — new infections precisely balance recoveries. After this point, susceptibles continue to be depleted, Rₑ stays below 1, and I declines. This is also the instant the herd immunity threshold is first crossed."

- question: "In an SIR epidemic, the epidemic ends only when essentially all susceptibles have been infected — the final uninfected individuals are those who happened to avoid contact with any infectious person by chance."
  type: true-false
  answer: false
  explanation: "The SIR model shows that a predictable fraction of susceptibles always escapes infection, determined by the final size equation: ln(S∞/S₀) = −R₀(1 − S∞/N). The epidemic self-extinguishes before reaching all susceptibles because the susceptible pool is depleted enough that Rₑ < 1, and the epidemic shrinks to zero before infecting everyone. The survivors are 'saved' by the depletion dynamics of the epidemic, not by chance avoidance — and the exact fraction is a deterministic function of R₀ alone."

- question: "Why does an SIR epidemic continue to decline in cases even when a substantial fraction of the population remains susceptible? Explain the mechanism."
  type: short-answer
  answer: "The epidemic declines whenever the effective reproduction number Rₑ = R₀ × S/N falls below 1 — meaning each infectious case generates fewer than one new case on average. This happens when the susceptible fraction S/N drops below 1/R₀ (the herd immunity threshold), even if many susceptibles remain. The mechanism is depletion: as infected individuals recover and acquire immunity, the density of susceptibles in the population decreases, reducing the force of infection β(I/N). New infections occur more slowly than recoveries, so I shrinks. The epidemic ends not from exhaustion of all susceptibles, but because the susceptible pool has been depleted enough to make sustained transmission impossible."
  explanation: "Students often confuse 'epidemic ending' with 'all susceptibles infected.' The SIR model clarifies that the epidemic is self-limiting through a threshold effect — depletion drives Rₑ below 1 before susceptibles are exhausted."
```

## Explainer

From your prerequisite on the **basic reproduction number R₀**, you understand that epidemic spread depends on the average number of secondary infections generated by a single case in a fully susceptible population, and that R₀ > 1 is necessary for an outbreak to grow. The SIR model gives R₀ a mechanistic derivation and explains its components: R₀ = β/γ, where β is the rate at which an infected individual transmits to each susceptible contact and γ is the recovery rate (the reciprocal of the average infectious period). Rather than treating R₀ as a black-box quantity estimated from case counts, the SIR model shows *why* the epidemic threshold depends on this ratio and predicts the full temporal trajectory — when the epidemic peaks, how large it gets, and what fraction of the population ultimately escapes infection.

The SIR model divides a closed population of size N into three compartments. **S** (susceptible) individuals can be infected; **I** (infectious) individuals can transmit; **R** (recovered) individuals are immune and no longer participate in transmission. The core dynamic is driven by the **force of infection**: the per-capita rate at which susceptibles become infected equals β × (I/N) — the transmission rate times the fraction of the population currently infectious. This gives dS/dt = −β(I/N)S and dI/dt = β(I/N)S − γI. The epidemic grows when dI/dt > 0, which requires (βS/N)/γ > 1 — equivalently, S/N > 1/R₀. This is the **epidemic threshold**: an outbreak expands when the susceptible fraction exceeds 1/R₀. The complement, 1 − 1/R₀, is the **herd immunity threshold** — the minimum immune fraction needed for the epidemic to self-extinguish.

The epidemic trajectory has a characteristic shape. Initially, with nearly the entire population susceptible, I grows approximately exponentially at rate β − γ = γ(R₀ − 1). As the epidemic proceeds, susceptibles are depleted, the force of infection weakens, and the I curve bends over. The **peak of I** occurs exactly when S/N = 1/R₀ — the moment the herd immunity threshold is first crossed. After the peak, I declines even though many people remain susceptible, because the susceptible pool has been depleted enough that new infections no longer outpace recoveries. Crucially, the epidemic ends before the entire susceptible population is infected: a fraction of susceptibles always survives uninfected, "saved" not by immunity but by the geographic depletion of infectious individuals before they could reach them. The **final size equation** — ln(S∞/S₀) = −R₀(1 − S∞/N) — gives the exact proportion ultimately infected as a function of R₀ alone.

Each intervention maps directly onto a model parameter. **Vaccination** reduces S before the epidemic starts, raising the effective immune fraction and — if vaccination coverage reaches the herd immunity threshold — preventing epidemic growth entirely. **Isolation and treatment** shorten the infectious period (reducing 1/γ, thus raising γ and lowering R₀). **Social distancing and masking** reduce β by decreasing the contact rate or per-contact transmission probability. This parameter-level clarity is why the SIR model is the standard foundation for public health modeling: interventions can be compared quantitatively, and the relative contribution of different strategies is explicit. The model's simplifying assumptions — constant β and γ, homogeneous random mixing, permanent immunity — are relaxed in extensions you will study next (the SEIR model adds an exposed/latent compartment E for diseases with incubation periods), but the core logic of thresholds, depletion dynamics, and intervention mapping originates here.
