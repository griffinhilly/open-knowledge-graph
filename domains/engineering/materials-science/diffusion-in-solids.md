---
id: diffusion-in-solids
title: Diffusion in Solids
domain: engineering
course: materials-science
prerequisites:
- id: crystal-defects
  type: hard
- id: diffusion-and-ficks-laws
  type: hard
- id: arrhenius-equation
  type: soft
- id: partial-derivatives
  type: soft
- id: differential-equations-intro
  type: soft
- id: kinetic-molecular-theory
  type: soft
- id: point-defects-and-vacancies
  type: hard
- id: point-defects-vacancies-and-interstitials
  type: hard
builds-toward:
- heat-treatment-of-steels
- sintering-and-powder-processing
tags:
- diffusion
- ficks-law
- vacancy-mechanism
- carburization
stage: expert
status: validated
---

# Diffusion in Solids

## Core Idea
Diffusion in solids is the thermally activated migration of atoms through a crystal lattice, primarily via vacancy exchange or interstitial hopping. Fick's first law relates steady-state flux to a concentration gradient; Fick's second law describes time-dependent concentration profiles. The diffusivity D follows an Arrhenius relationship D = D₀ exp(−Qd/RT), where Qd is the activation energy for diffusion. Engineering processes such as carburization (adding carbon to steel surfaces) and dopant diffusion in semiconductors are directly governed by these principles.

## How It's Best Learned
Solve Fick's second law for the semi-infinite solid boundary condition (using the complementary error function solution) applied to carburization problems. Plot concentration vs. depth at different times to build intuition.

## Common Misconceptions
- Interstitial diffusion (e.g., carbon in iron) is much faster than substitutional diffusion because interstitials don't require a vacancy.
- Higher temperature dramatically accelerates diffusion; even a 50°C difference can change diffusivity by an order of magnitude.

## Questions

```yaml
- question: "A steel part is carburized at temperature T₁ and then again at a higher temperature T₂. The diffusivity D follows D = D₀ exp(−Qd/RT). Which outcome is expected at T₂?"
  type: multiple-choice
  options:
    - "D decreases because higher temperature destabilizes the lattice"
    - "D increases because the exponential term becomes less negative, raising D dramatically"
    - "D stays the same because D₀ is fixed"
    - "D increases linearly with temperature"
  answer: 1
  explanation: "In the Arrhenius expression D = D₀ exp(−Qd/RT), raising T makes the exponent −Qd/RT less negative, so exp(−Qd/RT) grows. Because the relationship is exponential, even a modest temperature increase produces a large jump in D — often an order of magnitude for a 50°C rise."

- question: "Carbon diffusing into iron (interstitial diffusion) is faster than iron atoms exchanging sites (substitutional diffusion) because interstitial atoms do not require a neighboring vacancy to move."
  type: true-false
  answer: true
  explanation: "Substitutional diffusion depends on a vacancy being adjacent to the diffusing atom — a relatively rare event. Interstitial atoms (like C in the iron lattice) are small enough to hop between existing gaps without waiting for vacancies, giving interstitial diffusion a lower activation energy Qd and therefore higher D at any given temperature."

- question: "During carburization of steel, how does the carbon concentration profile change with increasing exposure time at constant temperature?"
  type: short-answer
  answer: "The profile broadens and carbon penetrates deeper into the steel. The complementary error function solution C(x,t) = Cs − (Cs − C₀)·erf(x / 2√(Dt)) shows that the characteristic diffusion depth scales as √(Dt), so longer time t pushes the concentration profile further from the surface while the surface concentration remains fixed at Cs."
  explanation: "The erfc solution comes directly from Fick's second law for a semi-infinite solid with constant surface concentration. The √(Dt) scaling is fundamental: doubling the time does not double the penetration depth — it increases it by only √2. This sublinear growth explains why extremely deep case hardening requires very long times or much higher temperatures."
```

## Explainer

Diffusion in solids is superficially similar to diffusion in liquids or gases, but the rigid crystal lattice changes everything. Atoms in a solid are not free to wander — they are trapped in potential wells at lattice sites. For a substitutional atom (one occupying a regular lattice site) to move, it must jump into an adjacent **vacancy**, and vacancies are rare. This is why substitutional diffusion is slow: the atom must wait for both a thermally activated jump and a neighboring empty site. Interstitial atoms — like carbon squeezed into the gaps of an iron lattice — face a different situation: the interstitial sites are always "available," so the only barrier is the activation energy to squeeze through the lattice. Interstitial diffusion is therefore much faster than substitutional diffusion, even in the same material.

The temperature dependence of diffusivity is captured by the Arrhenius equation D = D₀ exp(−Qd / RT), where Qd is the activation energy, R is the gas constant, and T is the absolute temperature. This is the same form you encountered in chemical kinetics, and for the same reason: both processes require thermal energy to surmount an energy barrier. The exponential sensitivity to temperature means that small changes in T translate to large changes in D — a 50°C increase can change diffusivity by an order of magnitude. In practice, this is why heat-treatment temperatures are tightly controlled.

Fick's first law J = −D(dC/dx) describes the **steady-state** flux of atoms down a concentration gradient. But most engineering problems involve time-dependent concentration profiles, which requires Fick's second law: ∂C/∂t = D ∂²C/∂x². For the standard carburization setup — a semi-infinite steel bar with a fixed surface carbon concentration Cs exposed at t = 0 — the solution is C(x,t) = Cs − (Cs − C₀)·erf(x / 2√(Dt)), where erf is the error function and C₀ is the initial uniform carbon content. This solution encodes the idea that the "diffusion front" propagates inward as √(Dt): doubling time moves carbon not twice as deep, but only √2 times as deep.

To use this solution, you identify x (depth below surface), t (exposure time), D (diffusivity at the treatment temperature, calculated from the Arrhenius formula), and the boundary/initial conditions. The practical goal in carburization is to achieve a target carbon concentration at a target depth — for example, 0.4 wt% C at 1 mm depth — and you solve for the required time or temperature. This links your abstract understanding of Fick's law back to the hardness profile of a manufactured gear tooth.
