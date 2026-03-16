---
id: fluctuation-dissipation-theorem
title: Fluctuation-Dissipation Theorem
domain: physics
course: statistical-mechanics
prerequisites:
- id: boltzmann-transport-equation
  type: soft
- id: canonical-ensemble
  type: hard
builds-toward:
- linear-response-theory
tags:
- fluctuations
- dissipation
- non-equilibrium
stage: advanced
status: draft
---

# Fluctuation-Dissipation Theorem

## Core Idea
The fluctuation-dissipation theorem (FDT) relates equilibrium fluctuations in an observable to the dissipative response of that observable to an external perturbation. For a system in thermal equilibrium, the autocorrelation function ⟨ΔA(t) ΔA(0)⟩ equals the time-integral of the linear response function, connecting intrinsic noise to damping.

## Explainer

From the canonical ensemble, you know that a system in thermal equilibrium at temperature T is constantly fluctuating: its energy, magnetization, pressure, or any other observable wiggles around its mean value because of thermal agitation. These fluctuations are not noise in an engineering sense — they are real, inevitable consequences of thermodynamics. The **fluctuation-dissipation theorem** makes a surprising connection: these same thermal fluctuations that jostle a system at equilibrium are intimately related to the system's ability to *dissipate* energy when perturbed. The two phenomena — spontaneous internal fluctuations and resistive response to external forces — are two faces of the same underlying physics.

The simplest and most intuitive example is Einstein's 1905 relation for Brownian motion: D = k_B T / (6πηr), where D is the diffusion coefficient, η is the fluid viscosity, and r is the particle radius. The left side characterizes fluctuations (the random walk, or equivalently the **diffusion** of a particle at equilibrium). The right side contains the drag coefficient 6πηr, which characterizes **dissipation** (how much force is needed to pull the particle through the fluid at a given speed). Einstein's relation says these are not independent: any mechanism that damps a particle's motion also drives its random fluctuations, with k_B T as the exchange rate set by temperature. A more viscous fluid damps faster *and* jostles harder in exactly the right proportion to maintain thermal equilibrium.

The general theorem frames this in terms of linear response theory. Suppose you perturb a system with a small external field h(t) that couples to an observable A. The **linear response function** χ(t) describes how ⟨A⟩ changes in response: ⟨A(t)⟩ = ∫χ(t − t') h(t') dt'. The imaginary part of χ in the frequency domain, χ''(ω), is the dissipative component — it captures the phase lag between drive and response that characterizes energy absorption. The FDT states that χ''(ω) = (ω/2k_B T) C(ω), where C(ω) is the power spectrum of equilibrium fluctuations — the Fourier transform of the **autocorrelation function** ⟨ΔA(t) ΔA(0)⟩. This is a profound result: you can measure the dissipative response of a material from the equilibrium noise alone, without applying any external field.

The FDT has wide-ranging applications. In electronics, it explains **Johnson-Nyquist noise**: a resistor at temperature T generates voltage noise with power spectral density 4k_B T R, where R is the resistance. The same mechanism that makes a resistor dissipate current also makes it emit noise voltage. In nanomechanics, it predicts the thermal vibrations of a cantilever from its mechanical quality factor. In optics, it connects the imaginary part of the dielectric constant (absorption) to the spectral density of electromagnetic fluctuations in a medium. The theorem ultimately reflects the equipartition theorem from the canonical ensemble: every degree of freedom in equilibrium carries k_B T/2 of energy, and any coupling that can drain energy can also supply it.
