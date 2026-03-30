---
id: diffusion-and-ficks-laws
title: Diffusion and Fick's Laws
domain: chemistry
course: physical-chemistry
prerequisites:
- id: transport-phenomena-gases
  type: hard
- id: differential-equations-intro-separable
  type: soft
- id: partial-derivatives
  type: soft
- id: kinetic-theory-of-gases
  type: soft
tags:
- Ficks-laws
- diffusion-coefficient
- random-walk
- concentration-gradient
- Stokes-Einstein
stage: advanced
status: validated
---

# Diffusion and Fick's Laws

## Core Idea
Fick's first law states that the diffusion flux J = −D(∂c/∂x) is proportional to the concentration gradient, with diffusion coefficient D. Fick's second law ∂c/∂t = D(∂²c/∂x²) describes how concentration profiles evolve in time, with Gaussian spreading: ⟨x²⟩ = 2Dt for one-dimensional diffusion. The diffusion coefficient for a gas scales as D ∝ T^(3/2)/p from kinetic theory; for a sphere in a liquid, the Stokes-Einstein equation gives D = kT/(6πηr), connecting diffusion to viscosity η and solute radius r. Self-diffusion, mutual diffusion, and tracer diffusion coefficients are distinct but related through the Onsager reciprocal relations.

## How It's Best Learned
Solve the diffusion equation analytically for a point source and verify ⟨x²⟩ = 2Dt. Use the Stokes-Einstein equation to estimate the size of proteins from measured diffusion coefficients (a technique used in DLS).

## Common Misconceptions
- Confusing Fick's first law (steady-state flux) with Fick's second law (time-dependent concentration change); the first applies to steady-state, the second to transient diffusion.
- Thinking diffusion only applies to gases; the Stokes-Einstein equation and Fick's laws describe diffusion in liquids and solutions equally well.

## Questions

```yaml
- question: "Fick's first law (J = −D ∂c/∂x) tells you that diffusion flux is proportional to which quantity?"
  type: multiple-choice
  options:
    - "The absolute concentration c at a given point"
    - "The concentration gradient ∂c/∂x"
    - "The rate of change of flux over time"
    - "The square root of the diffusion coefficient D"
  answer: 1
  explanation: "Flux (J) is driven by the concentration gradient — the spatial rate of change of concentration — not by absolute concentration. A region of uniformly high concentration has no net flux; a steep gradient drives strong flux. The negative sign indicates flow runs from high to low concentration."

- question: "Fick's first law describes how a concentration profile changes over time in a non-steady-state diffusion system."
  type: true-false
  answer: false
  explanation: "This describes Fick's second law: ∂c/∂t = D(∂²c/∂x²). Fick's first law applies to steady-state conditions where the flux is constant in time and space (∂c/∂t = 0). The two laws address different physical situations: first law for steady-state flux, second law for transient spreading."

- question: "What physical meaning does the relation ⟨x²⟩ = 2Dt convey about diffusion?"
  type: short-answer
  answer: "The mean squared displacement of a diffusing particle grows linearly with time t, so the characteristic distance a particle spreads scales as √(2Dt) — not linearly with time. This reflects the random-walk nature of diffusion: many small random steps accumulate, but the net displacement grows more slowly than if particles moved in a straight line."
  explanation: "This result, derived from solving the diffusion equation for a point source, is one of the most important in all of transport theory. It distinguishes diffusion (⟨x²⟩ ∝ t) from directed drift (⟨x⟩ ∝ t). In practice, measuring ⟨x²⟩ vs. t in dynamic light scattering gives D directly, from which the Stokes-Einstein equation yields particle size."
```

## Explainer

Imagine dropping a crystal of food dye into still water and watching it spread. The dye does not move in any preferred direction — every molecule executes a random walk, jostling in all directions due to thermal motion. Yet the net result is clear: dye moves from regions of high concentration toward regions of low concentration. Fick's laws describe this macroscopic consequence of microscopic randomness.

Fick's first law captures the steady-state picture: the diffusion flux J (moles crossing unit area per unit time) is proportional to the local concentration gradient, with the diffusion coefficient D as the proportionality constant: J = −D(∂c/∂x). The negative sign is essential — flux flows in the direction of decreasing concentration. If the gradient is steep, flux is large; if concentration is uniform, flux is zero regardless of how high the concentration is. This law applies when the concentration profile has settled into a time-independent shape (steady state), as in a membrane separating two well-mixed reservoirs.

Fick's second law extends the analysis to transient situations, where concentration profiles evolve over time: ∂c/∂t = D(∂²c/∂x²). This is a partial differential equation whose solutions describe how an initial concentration distribution spreads and flattens over time. For a point source of material released at x = 0 and t = 0, the solution is a Gaussian profile whose width grows in time. The key result is ⟨x²⟩ = 2Dt: mean squared displacement is proportional to t, not t². Diffusion is slower than ballistic motion — a consequence of the random-walk mechanism where forward and backward steps partially cancel.

The diffusion coefficient D is not a universal constant — it depends on what is diffusing and in what medium. For a gas, kinetic theory gives D ∝ T^(3/2)/p: faster molecules (higher T) and fewer collisions (lower p) mean faster diffusion. For a spherical particle in a liquid, the Stokes-Einstein equation gives D = kT/(6πηr), where η is viscosity and r is the particle radius. This equation has a remarkable practical use: measuring D by tracking particle motion (e.g., in dynamic light scattering) lets you infer the particle's radius — a standard technique for sizing proteins and nanoparticles.

Finally, do not fall into the trap of thinking Fick's laws are only for gases. They describe diffusion in any medium — liquids, solids, and biological membranes — and are foundational to understanding everything from drug delivery kinetics to oxygen transport in tissue to heat conduction (which obeys an identical mathematical form).
