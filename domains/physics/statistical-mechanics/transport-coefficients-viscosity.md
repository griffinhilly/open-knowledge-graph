---
id: transport-coefficients-viscosity
title: 'Transport Coefficients: Viscosity'
domain: physics
course: statistical-mechanics
prerequisites:
- id: chapman-enskog-expansion
  type: hard
builds-toward: []
tags:
- transport
- kinetic-theory
- viscosity
stage: advanced
status: draft
---
# Transport Coefficients: Viscosity

## Core Idea
Viscosity quantifies a fluid's resistance to flow. Kinetic theory predicts that viscosity depends only on temperature and molecular mass (not density), and provides quantitative expressions in terms of molecular parameters. The Chapman-Enskog solution yields viscosity coefficients that can be compared with experiments and extended to polyatomic molecules.

## Questions

```yaml
- question: "A gas container has its pressure doubled at constant temperature (doubling the density). According to kinetic theory, what happens to the gas viscosity?"
  type: multiple-choice
  options:
    - "It doubles — there are twice as many molecules available to transfer momentum across the velocity gradient"
    - "It is approximately unchanged — the mean free path halves (canceling the effect of more carriers), so η is density-independent"
    - "It decreases by half — the shorter mean free path means momentum is deposited locally and doesn't travel far"
    - "It increases by √2 — viscosity scales with the square root of density"
  answer: 1
  explanation: "Viscosity is density-independent in an ideal gas: η ~ mv̄/σ, where the number density n has cancelled. Doubling density doubles the number of molecules crossing unit area per second, but it also halves the mean free path λ ~ 1/(nσ), so each molecule deposits its carried momentum only half as far. The two effects exactly cancel. This is the famous counterintuitive result first predicted by Maxwell and confirmed experimentally: denser air is not more viscous. The density-independence breaks down only at high densities where multiple-body collisions become significant."

- question: "How does the viscosity of an ideal gas change as temperature increases?"
  type: multiple-choice
  options:
    - "It decreases — hotter molecules collide more frequently, disrupting organized flow more effectively"
    - "It is unchanged — viscosity depends only on molecular mass and size, not temperature"
    - "It increases — higher temperature means higher mean thermal speed v̄ ∝ √T, so molecules carry more momentum per crossing and η ∝ √T (or somewhat higher for real gases)"
    - "It decreases then increases, showing a minimum at intermediate temperatures"
  answer: 2
  explanation: "Gas viscosity increases with temperature. The mean thermal speed v̄ ∝ √T, and since η ~ mv̄/σ, viscosity scales as √T for ideal hard-sphere gases (modified to roughly T^{0.6–0.8} for real gases with realistic potentials). This is opposite to liquid viscosity, which decreases with temperature. In liquids, viscosity arises from intermolecular attraction holding layers together — higher temperature weakens this. In gases, viscosity arises from momentum-carrying molecular flights — higher temperature means faster molecules carrying more momentum. The underlying mechanism is completely different, so the temperature dependence runs in opposite directions."

- question: "A denser gas (at fixed temperature) will have higher viscosity than a less dense sample of the same gas, because more molecules are available to transfer momentum between layers."
  type: true-false
  answer: false
  explanation: "This is the central counterintuitive result of kinetic theory: gas viscosity is independent of density (over the ideal gas range). More molecules do cross the layer per second — but each one also has a shorter mean free path and deposits its momentum closer to where it came from. The increased number of carriers is exactly offset by the reduced distance each carrier travels. Maxwell predicted this in 1860, was reportedly skeptical of his own result, and was vindicated by experiment. The density-independence is a direct consequence of the mean free path λ ~ 1/(nσ) canceling the density factor in the carrier flux."

- question: "Gas viscosity arises because faster-moving molecules from a high-velocity layer carry their excess momentum into a slower-moving adjacent layer during collisions."
  type: true-false
  answer: true
  explanation: "This is the correct microscopic picture of viscosity as momentum transport. A fluid with a velocity gradient (fast layers adjacent to slow layers) has molecules thermally wandering across layer boundaries. A molecule from a fast-moving layer carries momentum proportional to its excess velocity; when it collides with a molecule in a slower layer, this momentum is partially transferred, accelerating the slower layer and decelerating the fast layer — which is the macroscopic effect we call viscous drag. Viscosity quantifies the proportionality between the velocity gradient and the resulting momentum flux."

- question: "Explain qualitatively why the viscosity of an ideal gas is independent of its density, starting from the microscopic picture of momentum transfer."
  type: short-answer
  answer: "Viscosity requires molecules to carry momentum from fast-moving layers to slow-moving ones. The momentum transported per unit time per unit area is proportional to two things: the number of molecules crossing the layer boundary (proportional to density n) and the distance each molecule travels before depositing its momentum (the mean free path λ ~ 1/(nσ), inversely proportional to n). When density increases, more molecules cross the boundary — but each one collides sooner and deposits its momentum locally. The product n × λ ~ n × 1/(nσ) = 1/σ is independent of n. The two effects exactly cancel, leaving viscosity dependent only on molecular mass, size, and thermal speed (hence temperature)."
  explanation: "Maxwell famously derived this result and was so surprised he reportedly tested it experimentally himself. The intuition is that what counts for viscosity is not how many molecules are present, but how effective each layer is at communicating its momentum to adjacent layers. Doubling the density doubles both the communication channel capacity and the resistance to long-range transport, leaving the net transport efficiency unchanged. This has practical implications: gas viscosity is relatively easy to predict from first principles using molecular parameters alone, with no empirical density-dependence to fit."
```

## Explainer

Viscosity is the transport of momentum. When a fluid has a velocity gradient — layers of fluid moving at different speeds — faster layers drag on slower ones, transferring momentum across the gradient. The viscosity coefficient η quantifies this: the momentum flux (force per unit area) between adjacent layers is η times the velocity gradient dv/dy. In a gas, this momentum transfer happens through collisions: fast-moving molecules from a high-velocity layer wander into a slower layer and exchange momentum through collisions, and vice versa. Everything follows from tracking this microscopic exchange.

A simple mean-free-path argument gives the essential physics. A molecule traveling from a high-velocity layer carries extra momentum ~ m Δv, where Δv is the velocity difference over one mean free path λ. It deposits this momentum after traveling ~ λ before colliding. The number flux of such molecules crossing unit area per second is ~ ½ n v̄ (where v̄ is the mean thermal speed). Multiplying, the momentum flux (= η × dv/dy) is ~ n m v̄ λ × (dv/dy), so **η ~ nm v̄ λ**. Since λ ~ 1/(nσ) for a collision cross-section σ, the n cancels: η ~ mv̄/(σ). This is the famous result that **viscosity is independent of density**. Counter-intuitive at first — denser air seems "thicker" — but correct: more molecules carry momentum, but each travels a shorter distance before colliding. The two effects exactly cancel, and η depends only on T (through v̄ ∝ √T) and m.

The Chapman-Enskog expansion you studied gives the rigorous version of this argument. Rather than the crude mean-free-path estimate, it systematically solves the Boltzmann equation perturbatively: the distribution function is expanded around the local Maxwellian in powers of the Knudsen number (mean free path / system size). At first order, this gives an exact expression for the viscosity in terms of molecular parameters and the collision integral Ω⁽²·²⁾, which encodes how molecules interact during collisions. For hard spheres, Ω⁽²·²⁾ is exactly calculable; for realistic molecules with intermolecular potentials (like Lennard-Jones), it requires numerical integration. The result is η = (5π/32) × mv̄/(πd²) × a correction factor — a factor of order unity that the crude estimate missed.

The comparison with experiment is where kinetic theory proves its worth. For noble gases (helium, argon) — where the pairwise potential is well-characterized — the Chapman-Enskog prediction of η matches measurements to within a percent over wide temperature ranges. Temperature dependence is especially clean: η ∝ T^{1/2} for hard spheres, modified by the temperature-dependent collision integral for real gases (typically η ∝ T^{0.6–0.8} in practice). The density-independence prediction has been confirmed experimentally from low pressures up to moderate densities, breaking down only when molecules interact simultaneously with multiple partners — the regime where the simple pairwise Boltzmann equation fails and the Green-Kubo formula approach you'll study next becomes necessary.
