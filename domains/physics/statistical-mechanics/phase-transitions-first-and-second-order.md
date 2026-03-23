---
id: phase-transitions-first-and-second-order
title: 'Phase Transitions: First Order and Second Order'
domain: physics
course: statistical-mechanics
prerequisites:
- id: gibbs-free-energy
  type: hard
- id: helmholtz-free-energy
  type: soft
builds-toward:
- critical-phenomena-critical-exponents
- landau-theory
tags:
- phase-transitions
- thermodynamics
- classification
stage: expert
status: draft
---

# Phase Transitions: First Order and Second Order

## Core Idea
First-order transitions (e.g., liquid-gas) involve a discontinuous jump in density and latent heat; Gibbs free energy is continuous but its first derivatives (entropy, volume) are discontinuous. Second-order transitions (e.g., ferromagnetic) show no latent heat or density jump; Gibbs energy and its first derivative are continuous, but second derivatives diverge.

## Questions

```yaml
- question: "Water is heated at 1 atm. At 100°C, the temperature stops rising even as heat continues to be added, and two phases coexist until all the liquid has converted to steam. How does the Ehrenfest classification categorize this transition, and what thermodynamic feature determines the classification?"
  type: multiple-choice
  options:
    - "Second-order, because the temperature remains constant and there is no abrupt change in any macroscopic property"
    - "First-order, because the first derivatives of Gibbs free energy — entropy and volume — are discontinuous at the transition"
    - "First-order, because the Gibbs free energy itself is discontinuous at 100°C"
    - "Second-order, because the heat capacity diverges at the boiling point rather than showing a finite latent heat"
  answer: 1
  explanation: "The liquid-gas transition at 100°C is a textbook first-order transition. The Gibbs free energy G is continuous at the transition (if it weren't, the system wouldn't choose that transition point), but its first derivatives are discontinuous: entropy S = −(∂G/∂T)_P jumps, producing latent heat, and volume V = (∂G/∂P)_T jumps, producing the density change. The constant temperature during boiling and the coexistence of phases are hallmarks of a first-order transition. Option C is a common confusion — G must be continuous."

- question: "What happens to the order parameter at a second-order (continuous) phase transition?"
  type: multiple-choice
  options:
    - "It jumps discontinuously from zero to a finite value at the transition temperature"
    - "It remains zero throughout — second-order transitions involve no symmetry breaking"
    - "It grows continuously from zero below the transition temperature, reaching a finite value only well below the critical point"
    - "It diverges to infinity at the critical temperature, making the transition detectable"
  answer: 2
  explanation: "A defining characteristic of second-order transitions is that the order parameter — spontaneous magnetization for a ferromagnet, superfluid density for a superconductor — grows continuously from zero rather than appearing abruptly. This is why they are called 'continuous transitions.' The discontinuous jump of the order parameter is the hallmark of a first-order transition. At exactly the critical temperature, the order parameter is zero, but it increases smoothly as the system cools below the transition."

- question: "At a first-order phase transition, the Gibbs free energy G is discontinuous — it jumps abruptly at the transition temperature."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. At a first-order transition, G is continuous — the two phases have equal Gibbs free energies precisely at the transition point, which is why the system undergoes the transition there. What is discontinuous are the FIRST DERIVATIVES of G: entropy S = −(∂G/∂T)_P and volume V = (∂G/∂P)_T. The discontinuity in entropy is the latent heat. If G itself were discontinuous, there would be no thermodynamic criterion for when the transition occurs."

- question: "Second-order phase transitions are characterized by diverging fluctuations at all length scales near the critical point, making the system scale-invariant."
  type: true-false
  answer: true
  explanation: "Near a second-order transition, the correlation length — the typical size of correlated fluctuations — grows without bound and becomes infinite at the critical point itself. This means fluctuations exist at every length scale simultaneously, giving rise to scale invariance. This is the physical origin of critical opalescence (light scattering at all wavelengths near a liquid-gas critical point) and is why second-order transitions are described by renormalization group theory. It also explains why the second derivatives of G (heat capacity, compressibility) diverge — they measure these fluctuations."

- question: "Why is there no latent heat in a second-order phase transition?"
  type: short-answer
  answer: "Latent heat arises when the entropy jumps discontinuously at the transition — a finite amount of heat is absorbed at a fixed temperature without a temperature change. In a second-order transition, the first derivatives of the Gibbs free energy (including entropy) are continuous — the entropy changes smoothly as the system crosses the transition point. Since there is no sudden jump in entropy (no ΔS at the transition temperature itself), there is no latent heat L = TΔS. The order parameter grows from zero continuously, so the system never needs to absorb a finite amount of energy to 'unlock' a new phase."
  explanation: "The key is the distinction between first and second derivatives of G. Latent heat = TΔS where ΔS is the entropy discontinuity at the transition. In second-order transitions, ΔS = 0 at the transition point (S is continuous), so L = 0. However, second derivatives of G like heat capacity DO diverge, reflecting the diverging fluctuations — which is why a sharp heat capacity anomaly can occur without a finite latent heat."
```

## Explainer

Phase transitions are among the most striking phenomena in nature: a substance abruptly changes character — liquid to gas, paramagnet to ferromagnet, normal metal to superconductor — at a precise temperature and pressure. The Ehrenfest classification organizes this diversity into two fundamental categories based on which derivatives of the **Gibbs free energy** G(T, P) are discontinuous at the transition point.

For a **first-order transition**, G itself is continuous across the transition (if it weren't, the system wouldn't choose that point), but its first partial derivatives are discontinuous. Since S = −(∂G/∂T)_P and V = (∂G/∂P)_T, a discontinuous first derivative means a jump in entropy — which is the **latent heat** L = TΔS — and a jump in volume (density change). This is the familiar liquid-gas transition: when water boils at 100°C, it absorbs 2260 J/g of latent heat while its density drops by a factor of ~1600. The two phases coexist along the transition curve, with equal Gibbs free energies. Moving along the coexistence curve toward the **critical point**, the latent heat and density jump shrink continuously, reaching zero at the critical point — where the transition changes character entirely.

A **second-order transition** (also called a **continuous transition**) has no latent heat and no coexistence: the system transforms smoothly in the sense that the **order parameter** — the quantity that characterizes the ordered phase — grows continuously from zero rather than jumping. For a ferromagnet, the order parameter is spontaneous magnetization, which appears below the Curie temperature and grows continuously. However, the second derivatives of G diverge at the transition: the heat capacity C_P = −T(∂²G/∂T²)_P and the compressibility κ_T = −(1/V)(∂²G/∂P²)_T both blow up. This divergence reflects the growth of fluctuations: near a second-order transition, fluctuations occur at all length scales simultaneously, making the system **scale-invariant** and the correlation length infinite.

The free energy framework unifies both cases with a single geometric picture. At a first-order transition, the G(T) curves for two phases cross: each phase has lower G in its own stability region, and they are equal exactly on the coexistence line. At a second-order transition, G approaches the same value from both phases continuously, with matching first derivatives. The practical diagnostic is straightforward: if heating a substance causes it to absorb latent heat at a fixed temperature (with coexisting phases), the transition is first-order. If instead the heat capacity diverges sharply without a finite latent heat, it is second-order. Both types are driven by the competition between energy, which favors ordered states, and entropy, which favors disorder — encoded together in the free energy G = H − TS.
