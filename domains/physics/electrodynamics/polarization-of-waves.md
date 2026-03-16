---
id: polarization-of-waves
title: Polarization of Electromagnetic Waves
domain: physics
course: electrodynamics
prerequisites:
- id: plane-waves-in-vacuum
  type: hard
builds-toward:
- electromagnetic-waves-in-media
- cavity-resonators
tags:
- polarization
- wave-properties
- light
stage: abstract-reasoning
status: draft
---

# Polarization of Electromagnetic Waves

## Core Idea
Polarization describes how the electric field vector varies in time as a wave propagates. Linear polarization has E oscillating along a fixed direction. Circular and elliptical polarizations occur when E rotates. Polarization states decompose into orthogonal linear or circular components. Materials interact selectively with different polarizations.

## Explainer

From your study of plane waves in vacuum, you know that a plane wave propagating in the z-direction has E⃗ and B⃗ both transverse — perpendicular to ẑ. This means E⃗ lives in the x-y plane at each point along the wave. **Polarization** is simply the description of how that transverse E⃗ vector moves as a function of time. The question "what is the polarization state?" is asking: if you stood at a fixed point and watched the tip of the E⃗ arrow, what pattern would it trace?

The simplest case is **linear polarization**: E⃗ oscillates back and forth along a single fixed direction in the x-y plane. You can write it as E⃗(z,t) = E₀ cos(kz − ωt) x̂, where the tip of the vector traces a straight line along x̂. Think of shaking a jump rope purely up and down — that is linear polarization. If you superpose two linearly polarized waves of equal amplitude but with a 90° phase difference — E_x = E₀ cos(kz − ωt) and E_y = E₀ cos(kz − ωt − π/2) = E₀ sin(kz − ωt) — the resulting vector has constant magnitude E₀ but rotates continuously in the x-y plane. This is **circular polarization**: the tip of E⃗ traces a circle. Right-circular polarization rotates clockwise when viewed from the direction the wave is traveling; left-circular rotates counterclockwise. The general case of two orthogonal components with arbitrary amplitude ratio and phase difference traces an ellipse — **elliptical polarization** — of which both linear and circular are special cases.

The reason polarization matters is that materials interact with light in polarization-dependent ways. A **polarizer** (like a polaroid filter) transmits only the component of E⃗ along a preferred axis, blocking the perpendicular component. When unpolarized light passes through a polarizer, its intensity is cut in half; when polarized light passes through one rotated by angle θ, Malus's law gives transmitted intensity I = I₀ cos²θ. **Birefringent** crystals have different refractive indices for the two orthogonal polarization components, so they travel at different speeds and accumulate a phase difference — transforming linear polarization into elliptical and vice versa. This effect is used in wave plates (quarter-wave plates convert linear to circular, half-wave plates rotate the polarization direction). At interfaces, reflected and transmitted waves have polarization-dependent reflection coefficients (Fresnel equations), with Brewster's angle giving a condition where reflected light is purely s-polarized.

The decomposition of polarization states into two orthogonal basis states — whether linear or circular — is a linear algebra operation. Any polarization state is a two-component complex vector, and any polarizer or wave plate is a 2×2 complex matrix acting on it. This **Jones calculus** formalism makes systematic calculations straightforward and foreshadows the way quantum states are written as vectors acted on by operators — the polarization of a photon is, in fact, a direct physical realization of a quantum two-level system.

## Questions

```yaml
- question: "A plane wave has E⃗(z,t) = E₀[cos(kz − ωt) x̂ + cos(kz − ωt + π/2) ŷ]. What is the polarization state, and which way does the electric field vector rotate?"
  type: short-answer
  answer: "This is circular polarization. Since the y-component leads the x-component by π/2, when the x-component is at its maximum the y-component is zero, and when x = 0 the y-component is at maximum. The tip of E⃗ traces a circle. By convention (viewed from the direction of propagation), this is left-circular polarization."
  explanation: "The key is comparing the phases: E_x = E₀ cos(kz−ωt), E_y = E₀ cos(kz−ωt+π/2) = −E₀ sin(kz−ωt). At t=0, z=0: E_x = E₀, E_y = 0. A moment later: E_x decreases, E_y becomes negative — the vector rotates clockwise in the x-y plane when viewed from the +z direction, which is left-circular by the common convention."

- question: "Unpolarized light of intensity I₀ passes through two polarizers. The first has its transmission axis vertical; the second is rotated 60° from vertical. What fraction of the original intensity exits the second polarizer?"
  type: short-answer
  answer: "After the first polarizer: I₁ = I₀/2 (unpolarized light loses half). After the second polarizer: I₂ = I₁ cos²(60°) = (I₀/2)(1/2)² = I₀/8. One-eighth of the original intensity exits."
  explanation: "Malus's law applies between the two polarizers: the light exiting the first polarizer is fully polarized along vertical, and the second polarizer transmits I₁ cos²θ where θ = 60° is the angle between their axes. cos²(60°) = (0.5)² = 0.25, so I₂ = (I₀/2)(0.25) = I₀/8."
```
