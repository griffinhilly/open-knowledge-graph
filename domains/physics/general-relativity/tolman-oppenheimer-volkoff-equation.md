---
id: tolman-oppenheimer-volkoff-equation
title: Relativistic Stars and the Tolman-Oppenheimer-Volkoff Equation
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: schwarzschild-solution
  type: hard
- id: stress-energy-tensor
  type: hard
- id: neutron-star-structure-and-properties
  type: soft
builds-toward: []
tags:
- stellar-structure
- neutron-stars
- hydrostatic-equilibrium
- perfect-fluid
- compact-objects
stage: expert
status: validated
---

# Relativistic Stars and the Tolman-Oppenheimer-Volkoff Equation

## Core Idea
The Tolman-Oppenheimer-Volkoff (TOV) equation is the general-relativistic condition for hydrostatic equilibrium in a static, spherically symmetric star made of perfect fluid. It comes from solving Einstein's equations inside the star and replaces the Newtonian law dP/dr = −Gmρ/r² with a version in which pressure itself adds to gravity. Given an equation of state P(ρ), integrating the TOV equation outward from the centre gives the star's mass and radius, and outside the star the metric matches the Schwarzschild solution. The equation predicts a maximum mass for neutron stars, above which no stable static configuration exists.

## How It's Best Learned
Write the general static, spherically symmetric metric and the perfect-fluid stress-energy tensor, then derive the tt and rr field equations and the conservation law ∇_μT^μν = 0. Compare each relativistic correction term with its Newtonian counterpart. Integrate the equations numerically for a simple equation of state and plot mass against radius. Discuss the constant-density interior Schwarzschild solution and the Buchdahl limit on compactness.

## Common Misconceptions
- More internal pressure always lets a star support more mass. (In general relativity pressure is a source of gravity, so raising the pressure also strengthens the pull it must resist; past a point, stiffening the star cannot prevent collapse.)
- The maximum neutron-star mass is fixed by general relativity alone. (The maximum mass depends on the equation of state of dense matter, which is still uncertain; relativity sets the framework and general bounds.)
- Newtonian hydrostatic equilibrium is accurate enough for neutron stars. (A neutron star's compactness 2GM/(Rc²) is around 0.3 or more, so relativistic corrections are large.)

## Questions

```yaml
- question: "The TOV equation is dP/dr = −G(ρ + P/c²)(m + 4πr³P/c²) / [r²(1 − 2Gm/(rc²))]. What does it reduce to when P ≪ ρc² and Gm/(rc²) ≪ 1?"
  type: multiple-choice
  options: ["dP/dr = 0", "dP/dr = −Gmρ/r²", "dP/dr = −GmP/(r²c²)", "dP/dr = −4πGρr"]
  answer: 1
  explanation: "Dropping the P/c² terms and the factor 1 − 2Gm/(rc²) leaves the Newtonian equation of hydrostatic equilibrium, dP/dr = −Gm(r)ρ/r²."
- question: "A static perfect-fluid star whose density does not increase outward can have radius R = 1.1 × (2GM/c²)."
  type: true-false
  answer: false
  explanation: "Buchdahl's theorem requires 2GM/(Rc²) < 8/9, that is, R > (9/8) × 2GM/c² = 1.125 × 2GM/c². A radius of 1.1 times the Schwarzschild radius is too compact."
- question: "Why do the relativistic terms in the TOV equation make collapse easier than in Newtonian gravity?"
  type: multiple-choice
  options: ["They remove the pressure from the equation", "Pressure contributes to the gravitating mass-energy, and the factor 1 − 2Gm/(rc²) in the denominator strengthens the gradient", "They make the star rotate", "They reduce the density at the centre"]
  answer: 1
  explanation: "The terms P/c² in two places and the denominator 1 − 2Gm/(rc²) all increase the required pressure gradient. Gravity grows faster than the pressure that resists it."
- question: "Using GM_sun/c² ≈ 1.48 km, estimate the compactness 2GM/(Rc²) of a 1.4 solar-mass neutron star with radius 12 km."
  type: short-answer
  answer: "About 0.35"
  explanation: "2GM/c² = 2 × 1.4 × 1.48 km ≈ 4.1 km. Dividing by 12 km gives about 0.35, so relativistic effects are strong."
```

## Explainer
In Newtonian stellar structure, a spherical star is held up by the balance dP/dr = −Gm(r)ρ/r², where m(r) is the mass inside radius r. This works well for the Sun, where 2GM/(Rc²) is about 4 × 10⁻⁶. For neutron stars it fails, because the gravitational fields are strong and the pressure is comparable to the energy density.

The relativistic version starts from a static, spherically symmetric metric,

ds² = −e^(2Φ(r))c²dt² + [1 − 2Gm(r)/(rc²)]⁻¹dr² + r²dΩ²,

and a perfect fluid with energy density ρc² and pressure P. The tt component of Einstein's equations gives dm/dr = 4πr²ρ, which looks Newtonian, although m(r) now includes all forms of energy. The rr component and the conservation of stress-energy combine into the TOV equation:

dP/dr = −G(ρ + P/c²)(m + 4πr³P/c²) / [r²(1 − 2Gm/(rc²))].

Richard Tolman and, separately, Robert Oppenheimer and George Volkoff published this result in 1939.

Each correction makes gravity stronger. The factor ρ + P/c² says that pressure adds to the inertia and weight of the fluid. The term 4πr³P/c² says that pressure adds to the source of gravity. The denominator 1 − 2Gm/(rc²) grows small in compact stars and steepens the gradient further. As a result, compressing a star to raise its pressure also raises the gravity that the pressure must resist.

To build a model, choose an equation of state P(ρ), pick a central density, and integrate dm/dr and dP/dr outward until P = 0. That radius is the surface R, and m(R) = M is the mass seen from outside, where the metric is the Schwarzschild solution. Repeating for many central densities traces a mass-radius curve. The mass rises with central density up to a maximum and then falls; stars beyond the maximum are unstable and collapse. Oppenheimer and Volkoff, treating neutron-star matter as a free neutron gas, found a maximum of about 0.7 solar masses. Neutron stars with measured masses near 2 solar masses show that real nuclear matter is much stiffer, and the TOV equation is how astronomers turn mass and radius measurements into tests of dense-matter physics.

A general bound holds for any static fluid star whose density does not increase outward. Buchdahl showed in 1959 that 2GM/(Rc²) < 8/9, so such a star must be larger than 9/8 of its Schwarzschild radius.
