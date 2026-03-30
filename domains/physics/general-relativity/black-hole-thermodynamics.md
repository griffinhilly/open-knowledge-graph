---
id: black-hole-thermodynamics
title: Black Hole Thermodynamics
domain: physics
course: general-relativity
prerequisites:
- id: black-holes-schwarzschild
  type: hard
- id: kerr-solution
  type: soft
tags:
- black-hole-thermodynamics
- bekenstein-hawking
- entropy
- area-theorem
- laws-of-black-hole-mechanics
stage: expert
status: validated
---

# Black Hole Thermodynamics

## Core Idea
Black hole thermodynamics establishes a precise analogy — elevated to physical identity by Hawking's discovery of black hole radiation — between the laws of black hole mechanics and the laws of thermodynamics. The four laws are: (0) the surface gravity κ is constant over the event horizon (analogous to thermal equilibrium at uniform temperature); (1) dM = (κ/8πG)dA + Ω_H dJ + Φ_H dQ (analogous to dE = TdS + work terms); (2) the horizon area A never decreases in classical processes (analogous to entropy never decreasing); (3) κ cannot be reduced to zero in a finite number of steps (analogous to the unattainability of absolute zero). Bekenstein proposed that black holes carry entropy S_BH = kA/(4l_P²), proportional to the horizon area, and Hawking's calculation of black hole radiation confirmed that black holes have temperature T_H = ħκ/(2πck), validating the thermodynamic interpretation. Black hole entropy is enormous — a solar-mass black hole has S ~ 10⁷⁷k, vastly exceeding the entropy of any ordinary matter configuration of the same mass.

## Questions

```yaml
- question: "The Bekenstein-Hawking entropy of a black hole is proportional to:"
  type: multiple-choice
  options:
    - "The volume enclosed by the event horizon"
    - "The mass of the black hole"
    - "The area of the event horizon"
    - "The surface gravity of the event horizon"
  answer: 2
  explanation: "S_BH = kA/(4l_P²), where A is the horizon area and l_P = √(ħG/c³) is the Planck length. This area scaling is deeply surprising — in ordinary thermodynamics, entropy is an extensive quantity proportional to volume, not area. The area law suggests that the degrees of freedom of a black hole live on its boundary (the horizon), not in its interior. This is one of the key motivations for the holographic principle, which conjectures that the information content of any region is bounded by its surface area in Planck units."

- question: "Hawking's area theorem states that the total horizon area of black holes can never decrease in any classical process. This is violated by Hawking radiation."
  type: true-false
  answer: true
  explanation: "The classical area theorem (proved by Hawking in 1971) assumes the null energy condition, which is satisfied by all classical matter. Hawking radiation is a quantum effect that violates the null energy condition near the horizon (through the creation of negative-energy partners that fall into the black hole). As the black hole radiates, it loses mass and its horizon area decreases, violating the classical area theorem. This is consistent because the area theorem's assumptions (classical GR + null energy condition) do not hold when quantum effects are included. The generalized second law — that the sum of black hole entropy and ordinary entropy never decreases — remains valid."

- question: "Explain why Bekenstein's area-entropy relation was initially controversial, and how Hawking's radiation calculation resolved the controversy."
  type: short-answer
  answer: "Bekenstein proposed in 1972 that black holes carry entropy proportional to their horizon area, to prevent violations of the second law of thermodynamics (dropping a hot object into a black hole would otherwise destroy entropy). The controversy was that if black holes have entropy, they must have temperature, and if they have temperature, they must radiate — but classically, nothing escapes a black hole. Hawking's 1974 calculation of quantum particle creation near the horizon showed that black holes do radiate thermally at temperature T_H = ħκ/(2πck), with the entropy coefficient being exactly S = kA/(4l_P²). This resolved the controversy by showing that the thermodynamic analogy is exact: black holes are genuine thermodynamic objects."
  explanation: "Hawking's calculation was originally intended to disprove Bekenstein's proposal — he expected to show that black holes do not radiate. When the calculation showed they do, it was one of the most important surprises in theoretical physics, connecting gravity, quantum mechanics, and thermodynamics."

- question: "A Schwarzschild black hole of mass M has entropy S = 4πGM²k/(ħc). Compare this with the entropy of the Sun."
  type: short-answer
  answer: "For a solar-mass black hole (M ≈ 2 × 10³⁰ kg): S_BH = 4πG M²k/(ħc) ≈ 4π(6.67×10⁻¹¹)(2×10³⁰)²(1.38×10⁻²³)/((1.05×10⁻³⁴)(3×10⁸)) ≈ 1.5 × 10⁵⁴ J/K, or about 10⁷⁷ in units of k. The Sun's thermodynamic entropy is approximately 10⁵⁸ k. A solar-mass black hole has about 10¹⁹ times more entropy than the Sun — an enormous factor. This reflects the fact that a black hole is the highest-entropy state for a given mass and size, which is why gravitational collapse is thermodynamically irreversible (in the classical limit)."
  explanation: "The vast entropy of black holes dominates the entropy budget of the observable universe. The total entropy of all black holes in the universe (~10¹⁰⁴ k) vastly exceeds the entropy of all other sources combined (~10⁸⁸ k for CMB photons, the next largest contributor). This makes black holes the thermodynamic 'endpoint' of gravitational evolution."
```

## Explainer

The connection between black holes and thermodynamics emerged from a puzzle in the early 1970s. If you drop a hot gas (which has high entropy) into a black hole, the gas and its entropy disappear behind the horizon. If the black hole has no entropy of its own, the total entropy of the universe decreases — violating the second law of thermodynamics. Bekenstein resolved this in 1972 by proposing that black holes carry entropy proportional to their horizon area: S_BH = ηkA/l_P², where η was initially undetermined. He argued that the information content of anything that falls into a black hole is captured by the increase in horizon area, preserving a "generalized second law" in which the total of ordinary entropy plus black hole entropy never decreases.

The formal laws of black hole mechanics, derived by Bardeen, Carter, and Hawking in 1973, reinforced the analogy. The zeroth law states that the surface gravity κ (a measure of the gravitational "acceleration" at the horizon) is constant across the event horizon of a stationary black hole — analogous to temperature being uniform in thermal equilibrium. The first law relates changes in mass, area, angular momentum, and charge through dM = (κ/8πG)dA + Ω_H dJ + Φ_H dQ — analogous to dE = TdS + work. The second law (Hawking's area theorem) states that the total horizon area never decreases in any classical process — analogous to entropy never decreasing. The third law states that κ = 0 (an extremal black hole) cannot be reached in a finite number of steps — analogous to the unattainability of absolute zero.

The analogy became physical reality through Hawking's 1974 discovery that black holes radiate. By studying quantum field theory on the curved Schwarzschild background, Hawking showed that the vacuum near the event horizon is unstable: virtual particle pairs are created, with one partner falling into the black hole (negative energy, from the exterior perspective) and the other escaping as real radiation. The spectrum is exactly thermal — a perfect blackbody — with temperature T_H = ħc³/(8πGMk) for a Schwarzschild black hole. This fixed the proportionality constant in Bekenstein's entropy formula at the celebrated value S_BH = kA/(4l_P²) = kc³A/(4Għ). The laws of black hole mechanics are not merely analogous to thermodynamics; they are thermodynamics.

The implications are far-reaching. Black hole entropy is proportional to area, not volume — the holographic principle, conjectured by 't Hooft and Susskind, generalizes this to all gravitational systems: the maximum entropy in any region is proportional to its boundary area in Planck units, not its volume. Black hole evaporation raises the information paradox: if a black hole forms from a pure quantum state and evaporates to thermal radiation (a mixed state), unitarity — a fundamental principle of quantum mechanics — appears to be violated. Resolving the information paradox is one of the central problems in quantum gravity and has driven major developments including the AdS/CFT correspondence, the firewall debate, and recent breakthroughs involving the Page curve and quantum extremal surfaces. Black hole thermodynamics sits at the intersection of gravity, quantum mechanics, and information theory, and continues to provide the sharpest clues about the nature of quantum gravity.
