---
id: wkb-approximation
title: The WKB Approximation
domain: physics
course: quantum-mechanics
prerequisites:
- id: differential-equations
  type: hard
- id: commutation-relations
  type: soft
builds-toward:
- wkb-quantization-rule
tags:
- wkb
- semiclassical
stage: formal-systems
status: draft
---
# The WKB Approximation

## Core Idea
WKB is a semiclassical method valid when de Broglie wavelength varies slowly. Writing ψ(x) ≈ A(x) e^{iS(x)/ℏ} accurately describes tunneling, quantization, and smooth-potential scattering.

## Questions

```yaml
- question: "An electron with energy E encounters a potential barrier where V > E over a region of width L. According to the WKB approximation, which factor most strongly governs the tunneling probability?"
  type: multiple-choice
  options:
    - "The kinetic energy of the electron at the center of the barrier"
    - "The frequency of the electron's wavefunction oscillation outside the barrier"
    - "The group velocity of the electron's wavepacket approaching the barrier"
    - "The exponential factor exp(−2∫|p|dx/ℏ), which depends on both the barrier height and width"
  answer: 3
  explanation: "The WKB tunneling probability is T ∝ exp(−2∫|p|dx/ℏ), where |p| = √(2m(V−E)) is the imaginary local momentum inside the barrier. This exponential factor depends on both the height (V−E, which determines |p|) and the width (the integration range L) of the barrier. Both parameters enter exponentially, so even modest increases in barrier height or width drastically reduce tunneling probability. This exponential suppression is why tunneling is a quantum phenomenon with no classical analog."

- question: "A physics student says the WKB approximation is best applied when a particle's potential energy changes very rapidly — varying significantly over distances much shorter than the de Broglie wavelength. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — rapidly varying potentials require an approximation method, which is exactly what WKB provides"
    - "Yes — the WKB method was developed specifically for step-function and rapidly varying potentials"
    - "No — WKB requires the potential (and hence the de Broglie wavelength) to change SLOWLY over one de Broglie wavelength; rapidly varying potentials violate the approximation's validity condition"
    - "No — WKB is only valid for constant potentials where exact solutions exist"
  answer: 2
  explanation: "The validity condition for WKB is precisely the opposite of what the student claims. WKB works when the de Broglie wavelength λ = h/p(x) varies slowly over one wavelength — formally, |dλ/dx| ≪ 1. This is the 'semiclassical limit': the potential changes so slowly that the wavefunction locally resembles a plane wave. When the potential changes rapidly (on scales comparable to λ), the approximation breaks down because the local momentum p(x) cannot be treated as nearly constant. Exact solutions are used at abrupt steps; WKB is used for smooth, slowly varying potentials."

- question: "In the classically allowed region (E > V), the WKB wavefunction has amplitude proportional to 1/√p — larger where the particle moves slowly and smaller where it moves fast — which reflects conservation of probability current."
  type: true-false
  answer: true
  explanation: "Probability current J = |ψ|² × v must be constant for a steady-state solution. Since v ∝ p, we need |ψ|² ∝ 1/p, giving |ψ| ∝ 1/√p. Where the particle moves slowly (small p, near a turning point), the wavefunction amplitude is large — the particle 'spends more time' there. Where it moves fast (large p), the amplitude is small. This is the quantum analog of how a classical particle decelerates near turning points and spends more time in low-kinetic-energy regions."

- question: "The WKB approximation remains accurate at classical turning points where E = V(x), since the potential is varying smoothly and continuously at those locations."
  type: true-false
  answer: false
  explanation: "Classical turning points are precisely where WKB breaks down, even though the potential is smooth there. At a turning point, E = V(x), so p(x) = √(2m(E−V)) = 0. The WKB amplitude formula 1/√p diverges at p = 0, signaling failure of the approximation. Physically, the de Broglie wavelength λ = h/p also diverges — the 'slowly varying wavelength' condition collapses. Airy functions are required to connect the oscillating (classically allowed) and decaying (classically forbidden) WKB solutions across turning points."

- question: "Why does the WKB approximation break down at classical turning points, and what happens to the wavefunction amplitude formula at those points?"
  type: short-answer
  answer: "At a classical turning point, E = V(x), so the local kinetic energy is zero and the local momentum p(x) = √(2m(E−V)) = 0. The WKB amplitude formula 1/√p diverges as p → 0, predicting infinite amplitude — which is unphysical. The approximation's validity condition (wavelength changes slowly over one wavelength) also fails here because λ = h/p → ∞. This breakdown requires using Airy functions — exact solutions to the Schrödinger equation near a linear turning point — to bridge between the oscillating WKB solution in the allowed region and the exponentially decaying solution in the forbidden region."
  explanation: "Turning points are the price WKB pays for being a local approximation. It works wherever the potential is nearly constant over one wavelength, but at turning points the wavelength itself becomes infinite and the local-momentum description fails. The connection formulas derived from Airy function analysis are what make WKB quantization possible: they enforce consistent boundary conditions around a bound state, yielding the Bohr-Sommerfeld quantization rule."
```

## Explainer

Most quantum mechanics problems with exact analytical solutions share a special feature: the potential is either constant, or changes abruptly in a way that lets you patch together exact solutions in each region. Real physical potentials — an electron moving through a slowly varying electric field, a nucleus tunneling through a Coulomb barrier — vary smoothly and continuously. The **WKB approximation** (named for Wentzel, Kramers, and Brillouin) is the method for handling these smooth potentials, and it reveals the deep bridge between quantum mechanics and classical physics.

The key insight is that any wavefunction can be written as ψ(x) = A(x) e^{iS(x)/ℏ}, where A(x) is a slowly varying amplitude and S(x) is a phase that encodes the local oscillation rate. From your study of differential equations, you know that the Schrödinger equation −(ℏ²/2m)ψ'' + V(x)ψ = Eψ determines how ψ varies. Substituting the WKB form and keeping only leading-order terms in ℏ gives S'(x) = ±p(x), where p(x) = √(2m(E−V(x))) is the **local de Broglie momentum**. The WKB approximation is valid when p(x) changes slowly over one de Broglie wavelength — the same condition that makes a slowly varying potential "nearly classical."

In **classically allowed regions** (E > V, so p is real), ψ oscillates: ψ ∝ (1/√p) e^{±i∫p dx/ℏ}. The amplitude 1/√p has a clean physical interpretation — where p is large (fast particle), the wavefunction oscillates rapidly but has small amplitude; where p is small (slow particle near a turning point), amplitude grows. This is just conservation of probability current. In **classically forbidden regions** (E < V, so p becomes imaginary), the wavefunction exponentially decays or grows instead of oscillating. **Tunneling** is precisely when a particle traverses a classically forbidden region: the WKB tunneling probability is T ∝ exp(−2∫|p|dx/ℏ), where the integral runs across the barrier. The exponential suppression depends on both the height and width of the barrier — thick, tall barriers give tiny tunneling probability.

The WKB approximation breaks down at **turning points** where E = V(x) and p(x) = 0 — the amplitude 1/√p diverges. This is exactly where the classical particle would stop and reverse direction. At these points, more careful analysis using Airy functions is required to connect the oscillating and decaying solutions across the turning point. The resulting **connection formulas** are what make WKB quantization possible: requiring consistent matching of the WKB solutions around a bound state gives the Bohr-Sommerfeld quantization condition ∮ p dx = (n+½)h, which recovers the correct energy levels for smooth potentials and reduces to the old Bohr quantization in the classical limit.
