---
id: finite-square-well
title: The Finite Square Well
domain: physics
course: quantum-mechanics
prerequisites:
- id: particle-in-a-box
  type: hard
- id: schrodinger-eigenvalue-problem
  type: hard
- id: wavefunctions-boundary-conditions
  type: hard
- id: quantum-tunneling
  type: soft
builds-toward:
- nuclear-shell-model-magic-numbers
tags:
- schrodinger-equation
- bound-states
- potential-well
- scattering-states
stage: advanced
status: validated
---

# The Finite Square Well

## Core Idea
The finite square well is a region of constant negative potential, V = −V₀ for |x| < a, with V = 0 outside. Bound states have energies between −V₀ and 0; their wavefunctions oscillate inside the well and decay exponentially outside, so the particle has a nonzero chance of being found in the classically forbidden region. Matching ψ and dψ/dx at the walls gives transcendental equations. Their graphical solution shows that the well holds only a finite number of bound states, and in one dimension it always holds at least one. States with E > 0 are scattering states, which pass over the well and are partly reflected.

## How It's Best Learned
Solve inside and outside separately, then impose continuity of ψ and ψ' at x = a. Use the even/odd symmetry to split the problem in two. Solve the resulting equations graphically by plotting tan z against √(z₀²/z² − 1), which shows at a glance how many states exist. Compare the results with the infinite well of the same width in both the deep and shallow limits.

## Common Misconceptions
- A particle bound in the well is never found outside it. (The wavefunction decays exponentially outside but is not zero, so there is a nonzero probability of finding the particle in the classically forbidden region.)
- A shallow enough well has no bound states. (In one dimension any attractive square well, however shallow or narrow, has at least one bound state. In three dimensions this is not true.)
- The energy levels are the same as for an infinite well of the same width. (The wavefunctions leak past the walls, so the effective width is larger and each level lies lower, measured from the bottom of the well.)

## Questions

```yaml
- question: "In one dimension, every finite square well, no matter how shallow or narrow, has at least one bound state."
  type: true-false
  answer: true
  explanation: "In the graphical solution, the even-state curve tan z always crosses √(z₀²/z² − 1) at least once for any z₀ > 0, so there is always an even ground state."
- question: "Compared with an infinite well of the same width, the ground-state energy of a finite well (measured from the bottom of the well) is:"
  type: multiple-choice
  options: ["Higher", "Lower", "Exactly the same", "Zero"]
  answer: 1
  explanation: "The finite-well wavefunction extends into the walls, so it bends less sharply inside. Less curvature means less kinetic energy and a lower energy."
- question: "A finite well has the dimensionless strength z₀ = (a/ħ)√(2mV₀) = 4. How many bound states does it have?"
  type: multiple-choice
  options: ["1", "2", "3", "4"]
  answer: 2
  explanation: "A new state appears each time z₀ passes a multiple of π/2. Since 4 lies between π (about 3.14) and 3π/2 (about 4.71), there are three states: two even and one odd."
- question: "An electron is bound with energy E = −1.0 eV relative to the region outside the well. Estimate the distance over which its wavefunction decays by a factor e outside the well."
  type: short-answer
  answer: "About 0.2 nm"
  explanation: "κ = √(2m|E|)/ħ = √(2 × 9.11 × 10⁻³¹ × 1.60 × 10⁻¹⁹)/(1.055 × 10⁻³⁴) ≈ 5.1 × 10⁹ m⁻¹. The decay length is 1/κ ≈ 0.2 nm."
```

## Explainer
The infinite square well is a useful first model, but real potentials have finite depth. Take V = −V₀ inside |x| < a and V = 0 outside, and look first for bound states with −V₀ < E < 0.

Inside the well the kinetic energy E + V₀ is positive, so the Schrödinger equation gives oscillating solutions with wavenumber k = √(2m(E + V₀))/ħ. Outside, the energy is below the potential, and the solutions are real exponentials, e^(−κ|x|), with κ = √(−2mE)/ħ. Only the decaying exponential is allowed, because a growing one cannot be normalized. The particle has a real chance of being found outside the well, in a region where classical physics says it could never go.

The potential is symmetric, so the solutions can be chosen even or odd. For even states, ψ = cos kx inside. Requiring both ψ and dψ/dx to be continuous at x = a gives κ = k tan(ka). For odd states, ψ = sin kx inside, and the condition becomes κ = −k cot(ka). These equations cannot be solved in closed form. Introduce z = ka and z₀ = (a/ħ)√(2mV₀). The even condition becomes tan z = √(z₀²/z² − 1). Plotting both sides shows the solutions as crossing points. The right side falls to zero at z = z₀, so only a finite number of crossings exist.

Several results follow from the graph. There is always at least one even state, since the first branch of tan z starts at zero and rises without limit before z = π/2. A new bound state, alternately odd and even, appears each time z₀ passes a multiple of π/2. For a deep, wide well (large z₀), the low-lying levels approach those of an infinite well of width 2a, measured from the bottom. For any finite depth they lie a little lower, because the wavefunction leaks into the walls.

For E > 0 the particle is not bound. It travels over the well and is partly reflected at the edges. The transmission coefficient reaches exactly 1 when the well's width holds a whole number of half-wavelengths, a condition 2a√(2m(E + V₀))/ħ = nπ. This perfect transmission is related to the Ramsauer-Townsend effect, in which slow electrons pass through noble-gas atoms almost without scattering. The finite well also serves as a first model for electrons in quantum-well semiconductor devices and for nucleons in a nucleus.
