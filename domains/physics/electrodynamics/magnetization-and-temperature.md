---
id: magnetization-and-temperature
title: Temperature Dependence of Magnetization
domain: physics
course: electrodynamics
prerequisites:
- id: ferromagnetism-microscopic-view
  type: hard
- id: statistical-interpretation-of-entropy
  type: soft
tags:
- curie-temperature
- phase-transition
- thermal-effects
stage: expert
status: validated
---

# Temperature Dependence of Magnetization

## Core Idea
Thermal fluctuations compete with exchange interaction; above the Curie temperature ferromagnetic order disappears. The magnetization vanishes as (Tₓ - T)^β near the critical point, characterizing the ferromagnetic-paramagnetic phase transition.

## Questions

```yaml
- question: "A student heats an iron magnet and observes it losing magnetization. A classmate says 'the magnet loses all its magnetization abruptly at exactly 1043 K, like ice melting at 0°C.' What is correct?"
  type: multiple-choice
  options:
    - "The classmate is right — the transition is sharp and discontinuous, like a first-order phase transition"
    - "The student's observation is correct: magnetization decreases smoothly and continuously to zero as temperature approaches Tc, characteristic of a second-order phase transition"
    - "Neither — magnets don't lose magnetization from heat; only their external field changes"
    - "The classmate is right about the discontinuity but wrong about the temperature — the transition temperature varies continuously with applied field"
  answer: 1
  explanation: "The ferromagnetic-paramagnetic transition is a second-order (continuous) phase transition. Unlike melting (a first-order transition with a discontinuous jump in the order parameter), the magnetization M shrinks smoothly to zero as T → Tc from below, scaling as M ~ (Tc − T)^β. There is no abrupt jump. The classmate's ice-melting analogy applies to first-order transitions; the magnetic transition is categorically different — and this distinction matters for understanding critical phenomena and universality classes."

- question: "What happens to the entropy of an iron sample as it is heated through the Curie temperature from below?"
  type: multiple-choice
  options:
    - "Entropy decreases sharply at Tc as thermal energy becomes the dominant factor"
    - "Entropy increases as the system transitions from an ordered ferromagnetic state to a disordered paramagnetic state with more accessible microstates"
    - "Entropy remains constant — phase transitions conserve thermodynamic entropy"
    - "Entropy decreases above Tc because paramagnets have fewer magnetic configurations than ferromagnets"
  answer: 1
  explanation: "In the ferromagnetic state, moments are aligned — a highly constrained, low-entropy configuration. Above Tc, moments fluctuate randomly and can point in many directions, giving a much larger number of accessible microstates and higher entropy. The free energy F = U − TS determines which phase is stable: at high temperature, the entropy term −TS dominates and favors the disordered (paramagnetic) phase. This energy-entropy competition is the thermodynamic engine underlying every phase transition."

- question: "An iron magnet heated to 500°C (773 K) retains its ferromagnetism, since the Curie temperature of iron is approximately 770°C (1043 K)."
  type: true-false
  answer: true
  explanation: "At 500°C (773 K), the temperature is below the Curie temperature of iron (1043 K). Below Tc, the exchange interaction dominates thermal fluctuations, and long-range magnetic order is maintained — the material remains ferromagnetic. Only when T exceeds Tc does the system transition to the paramagnetic phase. This is why moderate heating does not destroy permanent magnets, but extreme heating does."

- question: "Above the Curie temperature, a material becomes largely magnetically inert — it cannot respond to an external magnetic field at most."
  type: true-false
  answer: false
  explanation: "Above Tc, a material becomes paramagnetic, not magnetically inert. Paramagnets respond to external fields: an applied field partially aligns the disordered moments, producing a weak magnetization proportional to the field strength. What is lost above Tc is *spontaneous* magnetization — the ability to maintain alignment without any external field. When the external field is removed, thermal fluctuations randomize the moments again. Paramagnetism is a real and measurable magnetic response; it is simply much weaker than ferromagnetism."

- question: "Why is the Curie temperature a sharp, well-defined threshold, even though the magnetization vanishes continuously rather than abruptly at Tc?"
  type: short-answer
  answer: "The Curie temperature marks the precise point where thermal energy and the exchange interaction balance: below Tc, exchange interaction wins and long-range order is thermodynamically stable; above Tc, thermal fluctuations dominate and disorder is stable. Tc is sharp because it is a phase transition — the ordered phase becomes thermodynamically unstable at a specific temperature determined by the material's exchange interaction strength. The transition is continuous (second-order) because the order parameter (magnetization) decreases smoothly to zero, scaled by the critical exponent β, rather than dropping discontinuously."
  explanation: "This combination — sharp threshold, continuous approach — is the hallmark of a second-order phase transition. The sharpness comes from the thermodynamic instability at Tc (a qualitative change in which phase minimizes free energy); the continuity comes from the absence of latent heat and the smooth variation of the order parameter. Understanding this distinction between 'sharp' and 'discontinuous' is essential for working with critical phenomena and universality classes in statistical mechanics."
```

## Explainer

You know from ferromagnetism that neighboring atomic magnetic moments align due to the **exchange interaction** — a quantum mechanical effect arising from the Pauli exclusion principle and electrostatic repulsion. This alignment creates magnetic domains and spontaneous bulk magnetization even without an external field. But thermal energy works against this order: higher temperature means more random thermal fluctuations that knock individual magnetic moments out of alignment with their neighbors. The competition between exchange interaction (which favors order) and thermal energy (which favors disorder) determines whether a material is ferromagnetic.

The **Curie temperature** Tc is the threshold temperature at which this competition tips decisively toward disorder. Below Tc, the exchange interaction wins: thermal fluctuations are not strong enough to break up the long-range alignment, and the material supports spontaneous magnetization. Above Tc, thermal energy dominates: moments fluctuate randomly, there is no long-range order, and the material becomes **paramagnetic** — it can be weakly magnetized by an external field but has no spontaneous order. Iron's Curie temperature is about 1043 K (770°C); nickel's is 627 K. This is why heating a permanent magnet can destroy its magnetism.

The transition at Tc is a **second-order phase transition** (or continuous phase transition). Unlike a first-order transition (like melting ice) where a discontinuous jump in an order parameter occurs at the transition temperature, the ferromagnetic-paramagnetic transition is continuous: the spontaneous magnetization M shrinks smoothly to zero as T approaches Tc from below. Near the critical point, M scales as M ~ (Tc - T)^β, where β is a **critical exponent**. The mean-field theory prediction is β = 1/2, but real materials deviate from this due to fluctuation effects, and the exact value of β depends on dimensionality and the symmetry of the order parameter — this is the domain of the renormalization group and universality classes in statistical mechanics.

Your entropy prerequisite is directly relevant here. The paramagnetic state above Tc has higher entropy: moments are disordered and can point in many directions, giving a large number of accessible microstates. The ferromagnetic state below Tc has lower entropy: moments are aligned, and the system is in a more constrained configuration. The free energy F = U - TS determines which phase is stable: at high T, the entropy term -TS becomes dominant and favors the disordered phase. This framing — order vs. disorder governed by a balance of energy and entropy — generalizes far beyond magnetism to every phase transition in condensed matter physics, from superconductivity to structural phase transitions in crystals.
