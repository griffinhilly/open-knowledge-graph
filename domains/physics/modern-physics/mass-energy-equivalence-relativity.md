---
id: mass-energy-equivalence-relativity
title: Mass-Energy Equivalence and E=mc²
domain: physics
course: modern-physics
prerequisites:
- id: relativistic-momentum-energy
  type: hard
builds-toward:
- photon-particle-properties
- binding-energy-stability-curve
tags:
- special-relativity
- energy
- mass
stage: advanced
status: validated
---

# Mass-Energy Equivalence and E=mc²

## Core Idea
Energy and mass are interchangeable according to Einstein's equation E = mc², where a small amount of mass contains enormous energy. The rest energy of any object is E₀ = mc², and the total relativistic energy is E = γmc². This explains nuclear binding energy, matter-antimatter annihilation, and why particle accelerators must accelerate particles to relativistic speeds to create new particles.

## Questions

```yaml
- question: "A nuclear fission reaction releases a large amount of energy. A student says: 'Mass was destroyed and converted into energy.' What is wrong with this description?"
  type: multiple-choice
  options:
    - "Nothing is wrong — mass is destroyed and energy is created in nuclear reactions"
    - "Mass is not involved at all — nuclear energy comes from releasing stored electromagnetic potential energy"
    - "Mass and energy are the same thing; the rest energy decreased and kinetic energy increased, but total energy is conserved — mass was not 'destroyed'"
    - "The description is imprecise but harmless; no energy is actually released, only redistributed among particles"
  answer: 2
  explanation: "The phrase 'mass destroyed and converted into energy' implies mass and energy are separate things that can be interconverted. But E = mc² says they are the same thing in different units. In fission, the total rest mass of the products is less than the reactants (mass defect), because some rest energy has become kinetic energy of the fragments. No energy is created or destroyed — it is already conserved throughout. The right frame is: rest energy decreased, kinetic energy increased, total energy unchanged."

- question: "A photon has zero rest mass. Using the full relativistic energy-momentum relation E² = (pc)² + (mc²)², what is the energy of a photon with momentum p?"
  type: multiple-choice
  options:
    - "E = 0, because a massless particle has no rest energy and therefore no total energy"
    - "E = mc² still applies, with m interpreted as the photon's effective mass"
    - "E = pc — the mc² term vanishes, leaving only the momentum contribution"
    - "E = γmc², but with γ → ∞ as v → c, so the energy is formally infinite"
  answer: 2
  explanation: "Setting m = 0 in E² = (pc)² + (mc²)² gives E² = (pc)², so E = pc. This is consistent with the photon relation E = hf and p = hf/c, which gives pc = hf = E. The expression E = γmc² is indeterminate for photons (both γ and m diverge/vanish), which is why the full energy-momentum relation is the correct starting point. The full relation is Lorentz-invariant and covers both massive and massless particles."

- question: "The equation E = mc² applies only to objects at rest; for a moving object, the correct expression for its total energy is E = γmc²."
  type: true-false
  answer: true
  explanation: "E = mc² (or E₀ = mc²) is specifically the rest energy — the energy a particle has when v = 0 and γ = 1. The total relativistic energy of a moving particle is E = γmc², where γ = 1/√(1 − v²/c²) > 1 whenever v > 0. E = mc² is a special case of E = γmc² with v = 0. This is not a flaw in E = mc²; it correctly describes the enormous energy content of mass even at rest."

- question: "In matter-antimatter annihilation, mass is destroyed and energy is created from very little, which is why the process seems to violate conservation of mass."
  type: true-false
  answer: false
  explanation: "Mass-energy equivalence means mass is not a separately conserved quantity — energy is. When an electron and positron annihilate to produce two gamma rays, the rest energy of both particles (2 × 511 keV = 1.022 MeV) is entirely converted to photon energy. Total energy is conserved throughout. There is no 'creation from nothing.' The apparent violation of 'mass conservation' is simply because mass conservation is not the correct law — energy conservation (which includes rest energy) is."

- question: "What is the mass defect of a nucleus, and how does it provide direct experimental evidence for E = mc²?"
  type: short-answer
  answer: "The mass defect is the difference between the mass of a nucleus and the sum of the masses of its constituent protons and neutrons. A helium-4 nucleus, for example, is lighter than two free protons plus two free neutrons. This missing mass corresponds exactly to the binding energy of the nucleus via E = Δmc² — the energy required to pull the nucleus apart into its components. Measuring both the mass defect (with a mass spectrometer) and the binding energy (from nuclear reaction energetics) and verifying E = Δmc² is a direct, quantitative confirmation of mass-energy equivalence."
  explanation: "The mass defect is one of the clearest experimental confirmations of E = mc². It shows that binding energy has mass — the bound system weighs less because some of the constituent rest energy was released as binding energy when the nucleus formed. This effect is tiny for chemical bonds (far too small to measure) but large enough to measure precisely in nuclear physics (about 0.7% for helium-4). It also explains why nuclear fuel releases millions of times more energy than chemical fuel per kilogram."
```

## Explainer

From your prerequisite on relativistic momentum and energy, you know that Newton's expression p = mv fails at high speeds and must be replaced by the relativistic momentum **p⃗ = γm v⃗**, where **γ = 1/√(1 − v²/c²)** is the Lorentz factor. You also know that the total relativistic energy of a particle is **E = γmc²**. The famous equation E = mc² is the special case of this when v = 0: a particle at rest (γ = 1) still has energy E₀ = mc², called the **rest energy**. Mass is not merely something that has energy stored in it — mass is a form of energy, and energy has inertia (resistance to acceleration) proportional to E/c².

The magnitude of the rest energy is staggering. One kilogram of matter at rest contains E = (1)(3 × 10⁸)² = 9 × 10¹⁶ joules — roughly the energy released by two million tons of TNT. The factor c² ≈ 9 × 10¹⁶ m²/s² acts as a conversion constant between mass units and energy units. Most physical processes — chemical reactions, heating, mechanical deformation — convert only a minuscule fraction of rest mass into other energy forms. Nuclear reactions are different: a uranium fission event converts roughly 0.1% of rest mass to kinetic energy of fragments, which is why nuclear fuel is millions of times more energy-dense than chemical fuel.

The full relativistic energy-momentum relation, **E² = (pc)² + (mc²)²**, is worth examining carefully. For a massive particle at rest (p = 0), it reduces to E = mc². For a photon, which has m = 0, it gives E = pc — consistent with the photon relation E = hf and p = hf/c you know from wave-particle duality. This unified equation covers both massive and massless particles and is Lorentz invariant: the quantity E² − (pc)² = (mc²)² has the same value in every inertial frame. The mass m in this equation is the **invariant mass** (or rest mass), a Lorentz scalar — not the outdated "relativistic mass" mγ that some older texts use.

**Mass-energy equivalence** is not merely a theoretical statement — it is directly verified by nuclear physics. A helium-4 nucleus weighs less than the sum of its two protons and two neutrons by a deficit called the **mass defect**. This missing mass (about 0.7% of the total) has been converted into the **binding energy** that holds the nucleus together. To split helium into its constituents, you must supply exactly E = Δmc² of energy. Conversely, in matter-antimatter annihilation — say, an electron and positron colliding — all of the rest mass of both particles converts to photon energy: two gamma rays, each with energy 511 keV = m_e c². In a particle accelerator, when you want to create new massive particles, you must supply at least the rest energy of the particles you intend to create — which is why high-energy physics requires particle beams with energies in the GeV to TeV range.
