---
id: wavefunction-and-probability
title: Wavefunction and the Born Rule
domain: physics
course: modern-physics
prerequisites:
- id: heisenberg-uncertainty-principle
  type: hard
- id: simple-probability
  type: soft
builds-toward:
- schrodinger-equation-intro
- particle-in-a-box
tags:
- quantum
- wavefunction
- born-rule
- probability-density
stage: advanced
status: draft
---

# Wavefunction and the Born Rule

## Core Idea
In quantum mechanics a particle is described by a complex-valued wavefunction ψ(x, t). The Born rule states that the probability of finding the particle in an interval dx is |ψ(x,t)|² dx, so |ψ|² is the probability density. The wavefunction must be normalized so that the total probability integrates to one. Observables (energy, momentum) correspond to operators acting on ψ; measured values are eigenvalues of these operators, and measurement collapses ψ to the corresponding eigenstate.

## How It's Best Learned
Work with simple normalized wavefunctions (Gaussian, square) and compute probability of finding the particle in a region. The connection to operators is best introduced after computing expectation values ⟨x⟩ = ∫ x|ψ|² dx and comparing with ⟨p⟩ = ∫ ψ*(−iℏ ∂/∂x)ψ dx.

## Common Misconceptions
- The wavefunction is a real physical wave like a water wave — ψ is complex and has no direct classical analog; only |ψ|² is physically measurable.
- Wavefunction collapse is instantaneous everywhere, which violates relativity — the collapse is a feature of the probability description; no physical signal travels superluminally.
