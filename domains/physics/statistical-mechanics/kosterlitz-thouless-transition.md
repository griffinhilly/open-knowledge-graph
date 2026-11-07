---
id: kosterlitz-thouless-transition
title: The Berezinskii-Kosterlitz-Thouless Transition
domain: physics
course: statistical-mechanics
prerequisites:
- id: long-range-order
  type: hard
- id: renormalization-group-intro
  type: hard
- id: two-point-correlation-functions
  type: hard
- id: spontaneous-symmetry-breaking
  type: soft
- id: goldstone-theorem
  type: soft
builds-toward:
- superfluidity
tags:
- phase-transitions
- topological-defects
- vortices
- two-dimensions
- xy-model
stage: expert
status: validated
---

# The Berezinskii-Kosterlitz-Thouless Transition

## Core Idea
In two dimensions, a system with a continuous symmetry, such as the XY model of planar spins, cannot develop true long-range order at any nonzero temperature (the Mermin-Wagner theorem). It can still have a phase transition. At low temperature, correlations decay as a power of distance and vortices are bound in vortex-antivortex pairs; above a temperature T_KT, free vortices unbind and correlations decay exponentially. This topological transition, worked out by Vadim Berezinskii and by Michael Kosterlitz and David Thouless in the early 1970s, describes superfluid helium films, thin superconducting films, and related two-dimensional systems.

## How It's Best Learned
Start with spin waves in the XY model and show that their fluctuations destroy long-range order in two dimensions but leave power-law correlations. Then compute the energy and entropy of a single vortex and find the temperature at which free vortices become favourable. Present the renormalization-group flow of stiffness and vortex fugacity qualitatively. End with the universal jump in superfluid density measured in helium films.

## Common Misconceptions
- No long-range order means no phase transition. (The BKT transition separates a phase with power-law correlations from one with exponential decay, without any order parameter becoming nonzero.)
- The BKT transition is a symmetry-breaking transition like the Ising transition. (No symmetry is broken on either side; the transition is driven by the unbinding of topological defects.)
- The specific heat shows a sharp peak at T_KT. (The free energy has only an essential singularity at T_KT, which is invisible in practice; the specific heat has a smooth maximum somewhat above T_KT.)

## Questions

```yaml
- question: "For the XY model with coupling J, a single vortex in a system of size L with lattice spacing a has energy about πJ ln(L/a) and entropy about 2k_B ln(L/a). At what temperature does this simple argument predict free vortices appear?"
  type: multiple-choice
  options: ["T = J/k_B", "T = πJ/(2k_B)", "T = 2πJ/k_B", "T = 0"]
  answer: 1
  explanation: "The free energy is F = E − TS = (πJ − 2k_BT) ln(L/a). It becomes negative, favouring free vortices, when T > πJ/(2k_B)."
- question: "Below T_KT, the two-dimensional XY model has a nonzero average magnetization in the limit of infinite system size."
  type: true-false
  answer: false
  explanation: "The Mermin-Wagner theorem forbids spontaneous breaking of a continuous symmetry in two dimensions at any T > 0. The low-temperature phase has power-law correlations but zero average magnetization."
- question: "How does the spin-spin correlation function behave at large distance r in the low-temperature phase?"
  type: multiple-choice
  options: ["It approaches a nonzero constant", "It decays as a power law, r^(−η)", "It decays exponentially, e^(−r/ξ)", "It grows with r"]
  answer: 1
  explanation: "Spin-wave fluctuations give quasi-long-range order, with an exponent η that depends on temperature and reaches 1/4 at T_KT. Above T_KT, free vortices make the decay exponential."
- question: "Explain how the BKT transition is consistent with the Mermin-Wagner theorem."
  type: short-answer
  answer: "Mermin-Wagner forbids a nonzero order parameter, not a phase transition. The BKT transition separates two phases that both have zero magnetization; they differ in how correlations decay and in whether vortices are bound or free."
  explanation: "The low-temperature phase has a finite spin stiffness (or superfluid density) without long-range order. That stiffness drops to zero at T_KT."
```

## Explainer
Consider planar spins on a two-dimensional lattice, each described by an angle θ, with energy −J cos(θᵢ − θⱼ) between neighbours. At low temperature the spins are nearly aligned and the energy can be expanded in gradients of θ. The resulting spin waves are soft, and in two dimensions their thermal fluctuations grow logarithmically with system size. Any attempt at long-range order is washed out. This is the content of the Mermin-Wagner theorem of 1966: no spontaneous breaking of a continuous symmetry at nonzero temperature in two dimensions with short-range interactions. What survives is quasi-long-range order. The correlation ⟨cos(θ(r) − θ(0))⟩ decays as a power law, r^(−η), with η growing with temperature.

Spin waves are not the only excitations. A vortex is a configuration in which θ winds by 2π around a point. Far from its core, the gradient of θ falls as 1/r, so the energy grows logarithmically, E ≈ πJ ln(L/a), where L is the system size and a the lattice spacing. The vortex can sit anywhere on the lattice, roughly (L/a)² places, so its entropy is S ≈ 2k_B ln(L/a). The free energy F = (πJ − 2k_BT) ln(L/a) changes sign at T = πJ/(2k_B). Below this, isolated vortices cost infinite free energy in a large system, and vortices appear only in tightly bound vortex-antivortex pairs. Above it, free vortices proliferate and scramble the phase, and correlations decay exponentially.

Kosterlitz and Thouless presented this picture in 1973, building on Berezinskii's earlier work, and Kosterlitz gave a full renormalization-group treatment in 1974. Bound pairs screen the interaction between vortices and lower the effective stiffness. The flow equations show a line of fixed points at low temperature, which explains why η varies continuously, and a transition at the end of that line where η = 1/4. The transition is unusual. Above T_KT the correlation length diverges as exp(b/√(T − T_KT)), faster than any power law, and the free energy is smooth to all orders, so there is no sharp feature in the specific heat.

A testable prediction concerns superfluid films. The superfluid density ρ_s should drop to zero discontinuously at T_KT, with a jump fixed by fundamental constants: ρ_s/T_KT = 2m²k_B/(πħ²), where m is the helium atom's mass. David Bishop and John Reppy confirmed this universal jump in helium-4 films in 1978. Related behaviour appears in thin superconducting films, Josephson junction arrays, and ultracold atomic gases. The 2016 Nobel Prize in Physics went to Thouless, Haldane, and Kosterlitz for theoretical discoveries of topological phase transitions and topological phases of matter.
