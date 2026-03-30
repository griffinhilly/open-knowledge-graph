---
id: hawking-radiation
title: Hawking Radiation
domain: physics
course: general-relativity
prerequisites:
- id: black-hole-thermodynamics
  type: hard
- id: black-holes-schwarzschild
  type: hard
tags:
- hawking-radiation
- black-hole-evaporation
- information-paradox
- unruh-effect
- quantum-fields-curved-spacetime
stage: expert
status: validated
---

# Hawking Radiation

## Core Idea
Hawking radiation is the thermal radiation emitted by black holes due to quantum effects near the event horizon, discovered by Stephen Hawking in 1974. A Schwarzschild black hole of mass M radiates as a perfect blackbody with temperature T_H = ħc³/(8πGMk), inversely proportional to the mass — smaller black holes are hotter. The radiation arises because the vacuum state defined by an observer falling freely through the horizon differs from the vacuum state defined by a distant stationary observer: what the infalling observer sees as empty space, the distant observer sees as a thermal bath of particles. The radiated power is P = ħc⁶/(15360π G²M²), causing the black hole to lose mass and eventually evaporate completely in a time t_evap ~ 5120πG²M³/(ħc⁴). For astrophysical black holes, T_H is negligibly small (~60 nanokelvin for a solar-mass black hole), but the conceptual implications are profound: black hole evaporation raises the information paradox, one of the deepest unsolved problems in theoretical physics.

## Questions

```yaml
- question: "A black hole with twice the mass of another has a Hawking temperature that is:"
  type: multiple-choice
  options:
    - "Twice as high"
    - "Four times as high"
    - "Half as high"
    - "The same"
  answer: 2
  explanation: "The Hawking temperature T_H = ħc³/(8πGMk) is inversely proportional to the mass M. Doubling M halves the temperature. This is the opposite of ordinary thermodynamic objects, where adding energy (mass-energy) increases the temperature. Black holes have negative heat capacity: as they radiate and lose mass, they get hotter, which causes them to radiate faster, which causes them to lose mass faster — a runaway process that ends in complete evaporation."

- question: "The Hawking temperature of a solar-mass black hole is about 60 nanokelvin. This is far colder than the cosmic microwave background temperature of 2.7 K."
  type: true-false
  answer: true
  explanation: "For M = M_☉ ≈ 2 × 10³⁰ kg, T_H = ħc³/(8πGMk) ≈ 6 × 10⁻⁸ K. Since this is far below the CMB temperature (2.725 K), a solar-mass black hole actually absorbs more radiation from the CMB than it emits, causing it to grow rather than evaporate. Only black holes lighter than about 10²² kg (roughly the mass of the Moon) would currently have T_H > T_CMB and be actively evaporating. No black hole evaporation has been observed, and astrophysical black holes will not begin to evaporate until the universe cools below their Hawking temperature — trillions of years from now."

- question: "Explain the information paradox that arises from black hole evaporation."
  type: short-answer
  answer: "If a black hole forms from matter in a specific quantum state (a pure state) and then evaporates completely via Hawking radiation, the radiation appears to be exactly thermal — determined only by the black hole's mass, spin, and charge, with no information about the initial state encoded in the radiation. A pure state has evolved into a mixed (thermal) state, violating unitarity — the quantum mechanical principle that time evolution preserves information. Either: (1) information is truly lost (violating quantum mechanics), (2) information is encoded in subtle correlations in the Hawking radiation (violating the semiclassical approximation), (3) a remnant retains the information, or (4) the semiclassical picture breaks down in unexpected ways. Recent progress via the Page curve and quantum extremal surfaces suggests option (2), but a complete resolution requires a full theory of quantum gravity."
  explanation: "The information paradox, posed by Hawking in 1976, has driven four decades of theoretical progress. It is not merely a technicality — it forces a confrontation between general relativity and quantum mechanics at a fundamental level. The resolution likely requires understanding quantum gravity, making it one of the sharpest theoretical constraints on any quantum gravity candidate."

- question: "Describe the relationship between Hawking radiation and the Unruh effect, and explain why they are considered manifestations of the same physics."
  type: short-answer
  answer: "The Unruh effect states that a uniformly accelerating observer in flat Minkowski spacetime perceives the vacuum as a thermal bath at temperature T_U = ħa/(2πck), where a is the proper acceleration. Hawking radiation can be understood as a gravitational analog: by the equivalence principle, a stationary observer near a black hole horizon is equivalent to an accelerating observer in flat spacetime. The surface gravity κ plays the role of the acceleration a, and the Hawking temperature T_H = ħκ/(2πck) has the same form as the Unruh temperature. Both effects arise from the same underlying physics: the observer-dependence of the particle concept in quantum field theory — different observers in relative acceleration disagree about the vacuum state and hence about the number of particles present."
  explanation: "The connection between Hawking and Unruh effects illustrates a deep principle: the particle content of a quantum field is observer-dependent. There is no absolute notion of 'empty space' in quantum field theory on curved backgrounds. This observer-dependence is the conceptual core of Hawking radiation."
```

## Explainer

Hawking's 1974 calculation is one of the most important results in theoretical physics, connecting general relativity, quantum field theory, and thermodynamics. The calculation treats quantum fields (for simplicity, a massless scalar field) propagating on the fixed curved background of a collapsing star forming a black hole. The key insight is that the vacuum state — the state with no particles — is defined differently by different observers. An observer freely falling through the horizon defines a vacuum (the "in" vacuum) that is regular at the horizon. A distant stationary observer defines a different vacuum (the "out" vacuum) adapted to the late-time geometry. These two vacua differ, and the Bogoliubov transformation relating them shows that the "out" observer detects a thermal flux of particles with temperature T_H = ħc³/(8πGMk) — the Hawking temperature.

The temperature is inversely proportional to the mass, which gives black holes the remarkable property of negative heat capacity. As a black hole radiates and loses mass, it gets hotter, which increases the radiation rate, which accelerates the mass loss. For a Schwarzschild black hole, the radiated power scales as P ∝ M⁻², so the mass decreases faster and faster. The evaporation time for a black hole of initial mass M is t_evap ≈ 5120πG²M³/(ħc⁴). For a solar-mass black hole, this is about 10⁶⁷ years — inconceivably longer than the current age of the universe (~10¹⁰ years). For a black hole of mass ~10¹¹ kg (about the mass of a mountain), the evaporation time is roughly the age of the universe, and its final moments would produce a burst of high-energy radiation.

The physical mechanism is often described in terms of virtual particle pairs created near the horizon, with one particle falling in and the other escaping. While this picture is qualitatively helpful, it is not quantitatively accurate — the actual calculation involves the Bogoliubov transformation between vacuum states, not a local particle-pair process. A more precise description is the Unruh effect extended to curved spacetime: a stationary observer near the black hole horizon is accelerating (to resist falling in), and the equivalence principle relates this to the Unruh effect — an accelerating observer perceives the vacuum as a thermal bath. The Hawking temperature T_H = ħκ/(2πck), where κ is the surface gravity, has exactly the Unruh form with acceleration replaced by surface gravity.

The deepest implication of Hawking radiation is the information paradox. Hawking's calculation shows that the radiation is exactly thermal — its state is determined solely by the black hole's mass, spin, and charge, with no dependence on the details of what fell in. If the black hole evaporates completely, the quantum information about the initial state seems to be destroyed, violating the unitarity of quantum mechanics. Hawking originally argued that information is genuinely lost, but most physicists now believe information is preserved, encoded in subtle correlations among the Hawking radiation quanta that the semiclassical approximation misses. Recent progress — the island formula, the Page curve from quantum extremal surfaces, connections to the AdS/CFT correspondence — provides evidence that unitarity is preserved, but the complete mechanism remains unclear. Resolving the information paradox is likely to reveal fundamental aspects of quantum gravity and has been one of the most productive theoretical puzzles of the past half century.
