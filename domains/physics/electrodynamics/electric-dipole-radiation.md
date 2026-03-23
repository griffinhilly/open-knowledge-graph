---
id: electric-dipole-radiation
title: Electric Dipole Radiation and Radiation Patterns
domain: physics
course: electrodynamics
prerequisites:
- id: multipole-expansion-radiation
  type: hard
- id: larmor-formula
  type: soft
builds-toward:
- radiation-reaction-force
tags:
- dipole-radiation
- antenna
- patterns
stage: expert
status: draft
---

# Electric Dipole Radiation and Radiation Patterns

## Core Idea
Electric dipole radiation from time-varying dipole moment p(t) dominates for non-relativistic sources. Radiated power and angular distribution depend on dipole acceleration magnitude and direction. Maximum radiation perpendicular to acceleration; zero along it. Dipole antennas exploit this pattern.

## Questions

```yaml
- question: "A water molecule has a permanent electric dipole moment and is moving at constant velocity through vacuum. Does it radiate electromagnetic energy?"
  type: multiple-choice
  options:
    - "Yes — because it has a nonzero dipole moment, it continuously radiates"
    - "Yes — because moving charges always radiate"
    - "No — only an accelerating dipole moment (p̈ ≠ 0) produces radiation; constant velocity means p̈ = 0"
    - "No — only oscillating dipoles radiate, and a water molecule is not oscillating"
  answer: 2
  explanation: "The key insight is that radiation requires the second time derivative of the dipole moment (p̈) to be nonzero. A molecule moving at constant velocity has a dipole moment that is neither changing in magnitude nor direction in its rest frame — p̈ = 0 — so it produces no radiation. Option A is the most common misconception: the mere existence of a dipole moment is not sufficient. Option B confuses this with Larmor radiation from accelerating point charges — but even there, constant-velocity motion produces no radiation. Only acceleration (of charges or of the dipole moment itself) drives radiation."

- question: "A half-wave dipole antenna is oriented vertically (along the z-axis) and driven to oscillate at its resonant frequency. At which direction from the antenna is radiated power maximum?"
  type: multiple-choice
  options:
    - "Along the z-axis (above and below the antenna), because that is the direction the antenna points"
    - "In the horizontal plane perpendicular to the antenna, because the radiation pattern is proportional to sin²θ with zero emission along the dipole axis"
    - "Equally in all directions, since a resonant antenna is omnidirectional"
    - "At 45° angles above and below the horizontal plane, where sin²θ is maximized"
  answer: 1
  explanation: "The dipole radiation pattern is dP/dΩ ∝ sin²θ, where θ is the angle measured from the dipole axis. This means zero power is radiated along the axis (θ = 0°, directly above and below) and maximum power is radiated in the equatorial plane perpendicular to the axis (θ = 90°). For a vertical antenna, maximum broadcast is in the horizontal plane around the antenna — which is why broadcast towers are built tall and vertical, maximizing signal to receivers on the ground. The pattern resembles a donut with the hole on the vertical axis."

- question: "Doubling the oscillation frequency of an electric dipole (while keeping its peak dipole moment p₀ constant) doubles the total radiated power."
  type: true-false
  answer: false
  explanation: "False. The total radiated power from an oscillating dipole is P = p̈²/(6πε₀c³). For p(t) = p₀cos(ωt), we have p̈ = -ω²p₀cos(ωt), so the time-averaged power scales as P ∝ ω⁴p₀². Doubling ω while keeping p₀ fixed increases power by a factor of 2⁴ = 16, not 2. This ω⁴ dependence has profound consequences: blue light (higher frequency) is scattered far more efficiently than red light by atmospheric molecules (the basis of blue sky), and higher-frequency antennas radiate far more power for the same dipole amplitude."

- question: "The electric field in the far-zone radiation from an oscillating dipole lies in the plane containing the observation direction and the dipole axis."
  type: true-false
  answer: true
  explanation: "True. In the radiation zone, the electric field E⃗ is perpendicular to the propagation direction r̂ and lies in the plane spanned by r̂ and the dipole axis. This means the radiation is linearly polarized, with the polarization direction determined by the geometry of the source relative to the observer. This fact underlies polarization-selective reception in antenna engineering: a receiving antenna oriented parallel to the E-field direction of the incoming wave will couple to it most efficiently, while one oriented perpendicular will receive no signal."

- question: "Why does a static electric dipole — one with a fixed charge separation that is not changing in time — produce no electromagnetic radiation, even though it has a nonzero electric field extending through all of space?"
  type: short-answer
  answer: "Radiation requires energy to propagate away from the source at the speed of light without returning. A static dipole has a field that falls off as 1/r³ in the near zone — this is a 'bound' field that stores energy locally but does not transport it to infinity. Radiation fields fall off as 1/r, carrying energy flux (proportional to 1/r²) through any sphere at large distance, yielding a finite power. This 1/r behavior arises only when p̈ ≠ 0 — the oscillating current drives the field configuration to 'peel off' as a wave. With p̈ = 0, no 1/r term appears in the fields, and no power escapes to infinity."
  explanation: "The mathematical distinction is between near-field (quasi-static) terms that decay rapidly with distance and far-field (radiation) terms that decay as 1/r. The static dipole has only near-field terms. Physically, the oscillating dipole continuously launches new wavefronts that detach from the source and propagate outward — this detachment is impossible for a static configuration."
```

## Explainer

In your study of multipole expansions and the Larmor formula, you found that accelerating charges radiate electromagnetic energy, and that the leading-order term in the multipole expansion of the radiation field comes from the **electric dipole moment** p⃗(t) of the source. For any localized charge distribution oscillating at frequency ω with size much smaller than the radiation wavelength (the non-relativistic, long-wavelength limit), the dipole term dominates all higher multipole contributions by factors of (kd) ≪ 1, where d is the source size. This is why dipole radiation is the first and most important radiation mechanism to master.

The **electric dipole moment** p⃗ = Σ qᵢrᵢ captures the overall charge separation in the source. For a sinusoidally oscillating dipole p(t) = p₀ cos(ωt), the second time derivative p̈ = −ω²p₀ cos(ωt) enters the radiation fields. The radiated power follows from the Larmor formula generalized to dipoles: P = p̈²/(6πε₀c³) (in SI). The key insight is that **it is the acceleration of the dipole moment, not just its existence, that produces radiation**. A static dipole radiates nothing; a uniformly moving dipole radiates nothing; only a changing p̈ (equivalently, changing current distribution) produces radiation.

The **angular radiation pattern** is one of the most beautiful results in classical electrodynamics. The power radiated per unit solid angle varies as dP/dΩ ∝ sin²θ, where θ is the angle measured from the direction of p̈. This means: maximum radiation is emitted perpendicular to the oscillation direction (θ = 90°, a band around the "equator" of the dipole), and zero radiation is emitted along the dipole axis (θ = 0°, the "poles"). Visualize a toroidal or donut-shaped pattern, with the hole aligned along the dipole. The radiation is also polarized: the electric field in the far zone lies in the plane containing the observation direction and the dipole axis.

This pattern directly explains antenna design. A **half-wave dipole antenna** is a conducting rod driven to oscillate current back and forth along its length. The pattern broadcasts strongest broadside (perpendicular to the rod) and nothing off the ends — exactly the sin²θ shape. Engineers orient antennas accordingly. The same physics governs how atoms radiate light: an excited atom's oscillating electron distribution can be approximated as an oscillating dipole, and dipole selection rules (which transitions are allowed) govern which spectral lines appear bright. The sin²θ pattern, the ω⁴ power dependence on frequency, and the dominance of perpendicular emission are features you will encounter repeatedly in radiation physics, optics, and antenna engineering.
