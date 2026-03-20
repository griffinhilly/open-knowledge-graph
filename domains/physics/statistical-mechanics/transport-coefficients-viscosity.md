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

## Explainer

Viscosity is the transport of momentum. When a fluid has a velocity gradient — layers of fluid moving at different speeds — faster layers drag on slower ones, transferring momentum across the gradient. The viscosity coefficient η quantifies this: the momentum flux (force per unit area) between adjacent layers is η times the velocity gradient dv/dy. In a gas, this momentum transfer happens through collisions: fast-moving molecules from a high-velocity layer wander into a slower layer and exchange momentum through collisions, and vice versa. Everything follows from tracking this microscopic exchange.

A simple mean-free-path argument gives the essential physics. A molecule traveling from a high-velocity layer carries extra momentum ~ m Δv, where Δv is the velocity difference over one mean free path λ. It deposits this momentum after traveling ~ λ before colliding. The number flux of such molecules crossing unit area per second is ~ ½ n v̄ (where v̄ is the mean thermal speed). Multiplying, the momentum flux (= η × dv/dy) is ~ n m v̄ λ × (dv/dy), so **η ~ nm v̄ λ**. Since λ ~ 1/(nσ) for a collision cross-section σ, the n cancels: η ~ mv̄/(σ). This is the famous result that **viscosity is independent of density**. Counter-intuitive at first — denser air seems "thicker" — but correct: more molecules carry momentum, but each travels a shorter distance before colliding. The two effects exactly cancel, and η depends only on T (through v̄ ∝ √T) and m.

The Chapman-Enskog expansion you studied gives the rigorous version of this argument. Rather than the crude mean-free-path estimate, it systematically solves the Boltzmann equation perturbatively: the distribution function is expanded around the local Maxwellian in powers of the Knudsen number (mean free path / system size). At first order, this gives an exact expression for the viscosity in terms of molecular parameters and the collision integral Ω⁽²·²⁾, which encodes how molecules interact during collisions. For hard spheres, Ω⁽²·²⁾ is exactly calculable; for realistic molecules with intermolecular potentials (like Lennard-Jones), it requires numerical integration. The result is η = (5π/32) × mv̄/(πd²) × a correction factor — a factor of order unity that the crude estimate missed.

The comparison with experiment is where kinetic theory proves its worth. For noble gases (helium, argon) — where the pairwise potential is well-characterized — the Chapman-Enskog prediction of η matches measurements to within a percent over wide temperature ranges. Temperature dependence is especially clean: η ∝ T^{1/2} for hard spheres, modified by the temperature-dependent collision integral for real gases (typically η ∝ T^{0.6–0.8} in practice). The density-independence prediction has been confirmed experimentally from low pressures up to moderate densities, breaking down only when molecules interact simultaneously with multiple partners — the regime where the simple pairwise Boltzmann equation fails and the Green-Kubo formula approach you'll study next becomes necessary.
