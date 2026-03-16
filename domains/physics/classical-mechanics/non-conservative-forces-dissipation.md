---
id: non-conservative-forces-dissipation
title: Non-Conservative Forces and Energy Dissipation
domain: physics
course: classical-mechanics
prerequisites:
- id: friction-forces
  type: hard
- id: conservative-vector-fields-mechanics
  type: hard
builds-toward:
- energy-dissipation-and-irreversibility
tags:
- forces
- dissipation
- irreversibility
stage: formal-systems
status: draft
---

# Non-Conservative Forces and Energy Dissipation

## Core Idea
Non-conservative forces like friction, air resistance, and viscosity convert mechanical energy into heat and internal energy. Their work is path-dependent, and mechanical energy decreases over time.

## Explainer

From your prerequisite on **conservative vector fields**, you know the defining property of conservative forces: the work they do is path-independent, and there exists a potential energy function V such that F = −∇V. Gravity and the spring force are conservative — any energy you "spend" lifting an object or compressing a spring is stored as potential energy and is fully recoverable. Total mechanical energy KE + PE stays constant. **Non-conservative forces** break this symmetry: the work they do depends on the path taken, not just the endpoints, and the "spent" energy does not return as mechanical energy.

**Friction** is the canonical example. When you slide a block across a floor, kinetic friction opposes motion at every instant along the path. Take the block on a round trip — push it forward 1 m, then pull it back 1 m — and friction does negative work in *both* legs of the journey. The work done going forward is −f·d; the work done going back is also −f·d. You end where you started, but you have lost 2f·d of mechanical energy. There is no potential energy function for friction because energy is not stored and recovered — it is genuinely lost to heat and sound. This is the precise meaning of path-dependence: the total work done by friction between two points depends on how you travel between them, not just the endpoints.

The energy accounting equation for systems with non-conservative forces is ΔKE + ΔPE = W_nc, where W_nc is the work done by all non-conservative forces. Because friction and drag always oppose motion, W_nc is negative, and total **mechanical energy decreases**. This "missing" mechanical energy does not vanish — it converts into **thermal energy** (heat) and internal energy of the materials. The first law of thermodynamics ensures total energy is conserved across all forms, but the mechanical portion steadily shrinks. In any real-world system — a pendulum in air, a car slowing to a stop, a ball bouncing — dissipation is always present.

The deepest consequence is **irreversibility**. A conservative system — a frictionless pendulum, an ideal spring — is time-reversible: play the motion backward and it obeys the same physical laws as forward motion. Add friction, and reversal becomes impossible: the reversed motion would require friction to spontaneously *add* energy to the system, which never happens. Dissipation gives physical processes a **direction in time**: the forward slide and the backward slide are distinguishable by the heat generated. This asymmetry is the mechanical foundation of the second law of thermodynamics — the tendency of isolated systems toward greater disorder and energy dispersal — which you will explore in the topic on energy dissipation and irreversibility. Non-conservative forces are the bridge between Newton's reversible equations of motion and the irreversible thermal world we actually inhabit.
