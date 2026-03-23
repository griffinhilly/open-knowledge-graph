---
id: green-kubo-formula
title: Green-Kubo Formula
domain: physics
course: statistical-mechanics
prerequisites:
- id: response-functions-definition
  type: hard
- id: linear-response-theory-statmech
  type: hard
builds-toward:
- transport-coefficients-viscosity
- thermal-conductivity-kinetic
tags:
- response
- transport
- fluctuation-dissipation
stage: expert
status: validated
---

# Green-Kubo Formula

## Core Idea
The Green-Kubo formula expresses transport coefficients as time integrals of equilibrium correlation functions: η = (V/kT)∫₀^∞ ⟨σ_xy(t)σ_xy(0)⟩dt. This remarkable result allows macroscopic transport properties to be computed from microscopic equilibrium fluctuations without requiring explicit non-equilibrium simulations.

## Questions

```yaml
- question: "To measure the viscosity of a complex fluid computationally, you could simulate it under an applied shear stress and measure the velocity gradient. The Green-Kubo formula offers an alternative. What is it?"
  type: multiple-choice
  options:
    - "There is no alternative — viscosity is inherently a non-equilibrium property requiring a non-equilibrium simulation"
    - "Compute the viscosity from the static stress tensor at a single equilibrium snapshot"
    - "Compute the viscosity from the time-integral of the stress autocorrelation function in an equilibrium simulation"
    - "Apply the Green-Kubo formula only to electrical conductivity; viscosity requires non-equilibrium methods"
  answer: 2
  explanation: "The Green-Kubo formula is η = (V/kT)∫₀^∞ ⟨σ_xy(t)σ_xy(0)⟩dt. You run an ordinary equilibrium simulation, record the stress tensor at each timestep, compute how it correlates with itself over time, and integrate. No shear flow, no applied force. Option A is the misconception this topic attacks: transport coefficients look non-equilibrium, but the fluctuation-dissipation theorem connects them to equilibrium dynamics. Option B misses the time correlation — a static snapshot doesn't capture memory or decay."

- question: "In the Green-Kubo formula for viscosity, a longer autocorrelation decay time for the stress tensor corresponds to:"
  type: multiple-choice
  options:
    - "Lower viscosity — fast relaxation means the fluid resists shear less"
    - "Higher viscosity — slow stress relaxation means the fluid retains shear stress memory longer"
    - "Higher temperature — longer decay times indicate greater thermal fluctuation energy"
    - "A shorter integration window needed, since the autocorrelation function decays quickly"
  answer: 1
  explanation: "Viscosity is the resistance to flow — how long a fluid 'remembers' an applied shear stress. A fluid whose stress autocorrelation decays slowly (long memory) requires large sustained force to flow: high viscosity. A fluid that rapidly loses stress memory flows easily: low viscosity. Honey has slow stress relaxation; water has fast stress relaxation. The integral of the autocorrelation function captures the total 'area under the memory curve,' which is the viscosity."

- question: "The Green-Kubo formula follows from the fluctuation-dissipation theorem, which connects equilibrium fluctuations to the system's response to external perturbations."
  type: true-false
  answer: true
  explanation: "True — the fluctuation-dissipation theorem is the physical principle that underlies the Green-Kubo formula. It states that the same microscopic dynamics governing how spontaneous thermal fluctuations relax also governs how the system responds to (and dissipates) an externally applied perturbation. This is why measuring equilibrium fluctuations tells you about non-equilibrium transport: the mechanism is the same in both cases."

- question: "The Green-Kubo formula is specific to viscosity and cannot be extended to other transport coefficients like electrical conductivity or thermal conductivity."
  type: true-false
  answer: false
  explanation: "False — the Green-Kubo framework applies uniformly across all linear transport coefficients. Electrical conductivity is the time-integral of the current-current autocorrelation function; thermal conductivity is the time-integral of the energy-flux autocorrelation function. Each transport coefficient is the time-integral of the relevant flux autocorrelation. This unification across different transport phenomena under a single mathematical framework is one of the deep results of non-equilibrium statistical mechanics."

- question: "Why does measuring equilibrium fluctuations tell you about a system's response to an applied non-equilibrium perturbation? What principle connects them?"
  type: short-answer
  answer: "The fluctuation-dissipation theorem connects them. At equilibrium, a system constantly undergoes thermal fluctuations — small, spontaneous deviations in stress, current, or energy flux. The rate at which these fluctuations decay is governed by the same microscopic dynamics that would dissipate an externally applied perturbation. In other words, the system does not 'know' whether a deviation from equilibrium was caused by a thermal fluctuation or an external force — it relaxes the same way in either case. The Green-Kubo formula turns this insight into a calculation: the decay rate of equilibrium fluctuations is the transport coefficient."
  explanation: "The key insight is that transport is not fundamentally about driving a system out of equilibrium — it is about how the system relaxes. Equilibrium fluctuations are constantly doing this relaxation work, and watching them reveals everything about transport without ever needing an external perturbation."
```

## Explainer

From your study of linear response theory, you know that when a small external perturbation drives a system slightly away from equilibrium, the response is proportional to the perturbation. The proportionality constant is the relevant transport coefficient — viscosity for a shear stress, electrical conductivity for an electric field, thermal conductivity for a temperature gradient. What the Green-Kubo formula adds is a startling bridge: you can compute these non-equilibrium transport coefficients purely from equilibrium simulations, by measuring how spontaneous thermal fluctuations decay in time.

The physical logic behind this is the **fluctuation-dissipation theorem**: the same microscopic dynamics that dissipates an applied perturbation also governs how spontaneous equilibrium fluctuations relax. A system in equilibrium is constantly undergoing tiny fluctuations in stress, current, and energy flux — and the rate at which these fluctuations decay is controlled by the same transport processes that govern macroscopic relaxation. So instead of driving the system out of equilibrium and measuring how it responds, you watch the equilibrium fluctuations and measure their decay.

Concretely, for shear viscosity η, the Green-Kubo formula is η = (V/kT)∫₀^∞ ⟨σ_xy(t)σ_xy(0)⟩dt. The integrand is the **autocorrelation function** of the off-diagonal stress tensor component σ_xy — it measures how correlated the stress at time t is with the stress at time 0. At t = 0 the correlation is maximum (the stress is perfectly correlated with itself). As t increases, the stress evolves under Hamiltonian dynamics and loses memory of its initial value. The time integral of this decay gives the viscosity. A system with slow stress relaxation (long memory) has high viscosity; a system that rapidly loses stress memory has low viscosity.

The Green-Kubo formula is practically powerful for molecular dynamics simulations. Rather than simulating a flowing fluid and measuring force-velocity profiles — a technically demanding non-equilibrium calculation — you simulate an equilibrium fluid, record the stress tensor at every timestep, compute the autocorrelation function, and integrate. The same framework yields other transport coefficients: electrical conductivity comes from current autocorrelations, thermal conductivity from energy-flux autocorrelations. This unification across different transport phenomena through a single mathematical framework is one of the deep results of non-equilibrium statistical mechanics.
