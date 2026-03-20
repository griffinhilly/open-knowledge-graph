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

## Explainer

Most quantum mechanics problems with exact analytical solutions share a special feature: the potential is either constant, or changes abruptly in a way that lets you patch together exact solutions in each region. Real physical potentials — an electron moving through a slowly varying electric field, a nucleus tunneling through a Coulomb barrier — vary smoothly and continuously. The **WKB approximation** (named for Wentzel, Kramers, and Brillouin) is the method for handling these smooth potentials, and it reveals the deep bridge between quantum mechanics and classical physics.

The key insight is that any wavefunction can be written as ψ(x) = A(x) e^{iS(x)/ℏ}, where A(x) is a slowly varying amplitude and S(x) is a phase that encodes the local oscillation rate. From your study of differential equations, you know that the Schrödinger equation −(ℏ²/2m)ψ'' + V(x)ψ = Eψ determines how ψ varies. Substituting the WKB form and keeping only leading-order terms in ℏ gives S'(x) = ±p(x), where p(x) = √(2m(E−V(x))) is the **local de Broglie momentum**. The WKB approximation is valid when p(x) changes slowly over one de Broglie wavelength — the same condition that makes a slowly varying potential "nearly classical."

In **classically allowed regions** (E > V, so p is real), ψ oscillates: ψ ∝ (1/√p) e^{±i∫p dx/ℏ}. The amplitude 1/√p has a clean physical interpretation — where p is large (fast particle), the wavefunction oscillates rapidly but has small amplitude; where p is small (slow particle near a turning point), amplitude grows. This is just conservation of probability current. In **classically forbidden regions** (E < V, so p becomes imaginary), the wavefunction exponentially decays or grows instead of oscillating. **Tunneling** is precisely when a particle traverses a classically forbidden region: the WKB tunneling probability is T ∝ exp(−2∫|p|dx/ℏ), where the integral runs across the barrier. The exponential suppression depends on both the height and width of the barrier — thick, tall barriers give tiny tunneling probability.

The WKB approximation breaks down at **turning points** where E = V(x) and p(x) = 0 — the amplitude 1/√p diverges. This is exactly where the classical particle would stop and reverse direction. At these points, more careful analysis using Airy functions is required to connect the oscillating and decaying solutions across the turning point. The resulting **connection formulas** are what make WKB quantization possible: requiring consistent matching of the WKB solutions around a bound state gives the Bohr-Sommerfeld quantization condition ∮ p dx = (n+½)h, which recovers the correct energy levels for smooth potentials and reduces to the old Bohr quantization in the classical limit.
