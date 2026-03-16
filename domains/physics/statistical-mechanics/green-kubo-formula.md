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
stage: advanced
status: draft
---

# Green-Kubo Formula

## Core Idea
The Green-Kubo formula expresses transport coefficients as time integrals of equilibrium correlation functions: η = (V/kT)∫₀^∞ ⟨σ_xy(t)σ_xy(0)⟩dt. This remarkable result allows macroscopic transport properties to be computed from microscopic equilibrium fluctuations without requiring explicit non-equilibrium simulations.

## Explainer

From your study of linear response theory, you know that when a small external perturbation drives a system slightly away from equilibrium, the response is proportional to the perturbation. The proportionality constant is the relevant transport coefficient — viscosity for a shear stress, electrical conductivity for an electric field, thermal conductivity for a temperature gradient. What the Green-Kubo formula adds is a startling bridge: you can compute these non-equilibrium transport coefficients purely from equilibrium simulations, by measuring how spontaneous thermal fluctuations decay in time.

The physical logic behind this is the **fluctuation-dissipation theorem**: the same microscopic dynamics that dissipates an applied perturbation also governs how spontaneous equilibrium fluctuations relax. A system in equilibrium is constantly undergoing tiny fluctuations in stress, current, and energy flux — and the rate at which these fluctuations decay is controlled by the same transport processes that govern macroscopic relaxation. So instead of driving the system out of equilibrium and measuring how it responds, you watch the equilibrium fluctuations and measure their decay.

Concretely, for shear viscosity η, the Green-Kubo formula is η = (V/kT)∫₀^∞ ⟨σ_xy(t)σ_xy(0)⟩dt. The integrand is the **autocorrelation function** of the off-diagonal stress tensor component σ_xy — it measures how correlated the stress at time t is with the stress at time 0. At t = 0 the correlation is maximum (the stress is perfectly correlated with itself). As t increases, the stress evolves under Hamiltonian dynamics and loses memory of its initial value. The time integral of this decay gives the viscosity. A system with slow stress relaxation (long memory) has high viscosity; a system that rapidly loses stress memory has low viscosity.

The Green-Kubo formula is practically powerful for molecular dynamics simulations. Rather than simulating a flowing fluid and measuring force-velocity profiles — a technically demanding non-equilibrium calculation — you simulate an equilibrium fluid, record the stress tensor at every timestep, compute the autocorrelation function, and integrate. The same framework yields other transport coefficients: electrical conductivity comes from current autocorrelations, thermal conductivity from energy-flux autocorrelations. This unification across different transport phenomena through a single mathematical framework is one of the deep results of non-equilibrium statistical mechanics.
