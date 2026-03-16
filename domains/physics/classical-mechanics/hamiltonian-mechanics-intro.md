---
id: hamiltonian-mechanics-intro
title: Hamiltonian Mechanics (Introduction)
domain: physics
course: classical-mechanics
prerequisites:
- id: lagrangian-mechanics-intro
  type: hard
- id: partial-derivatives
  type: hard
tags:
- hamiltonian
- formalism
- mechanics
- phase-space
stage: formal-systems
status: draft
---

# Hamiltonian Mechanics (Introduction)

## Core Idea
Hamiltonian mechanics uses the Hamiltonian H = T + V (total energy) and canonical variables (position q, momentum p). Hamilton's equations ∂H/∂p = dq/dt and −∂H/∂q = dp/dt are first-order, time-reversible, and symmetric in q and p, making phase-space analysis elegant. For time-independent systems, H is conserved (energy conservation), and this formalism is the foundation for quantum mechanics via the Schrödinger equation.

## Explainer

From Lagrangian mechanics, you know the key move: instead of tracking force vectors (Newton's approach), you write the Lagrangian L = T − V as a function of generalized coordinates and velocities, then derive equations of motion from the principle of stationary action. The Lagrangian approach is powerful because it handles constraints automatically and works in any coordinate system. Hamiltonian mechanics is a further transformation that reshapes the same physics into a more symmetric and conceptually powerful form.

The **Hamiltonian** is constructed via a **Legendre transform** of the Lagrangian: instead of tracking position q and velocity q̇, you track position q and the **generalized momentum** p = ∂L/∂q̇. This coordinate change from (q, q̇)-space to (q, p)-space — called **phase space** — is the conceptual heart of the Hamiltonian formalism. The Hamiltonian H(q, p) is typically just total energy T + V expressed in terms of positions and momenta. **Hamilton's equations** then describe evolution: dq/dt = ∂H/∂p and dp/dt = −∂H/∂q. Notice that the Lagrangian's second-order equations of motion (like F = ma) become two coupled first-order equations — a mathematical improvement that makes the system easier to analyze.

The real payoff is the elegance of phase space. Every possible state of the system is a single point (q, p) in phase space; dynamical evolution is a trajectory through it. Hamilton's equations define a **flow** — a vector field in phase space — and **Liouville's theorem** says this flow preserves phase-space volume. This conservation law has no obvious Newtonian analog; it is a deep structural feature of classical mechanics. The geometry of phase space — orbits, fixed points, stable and unstable manifolds — becomes the language for understanding dynamics, chaos, and stability in ways that force-based approaches cannot easily express.

**Poisson brackets**, defined as {f, g} = ∑(∂f/∂q ∂g/∂p − ∂f/∂p ∂g/∂q), give Hamilton's equations a compact algebraic form: df/dt = {f, H}. Any quantity with a zero Poisson bracket with H is conserved; this gives a systematic way to find conservation laws. For time-independent systems, H itself satisfies dH/dt = {H, H} = 0, immediately yielding energy conservation without additional assumptions.

This algebraic structure is exactly what bridges to quantum mechanics — the Poisson bracket becomes the commutator, position and momentum become operators satisfying [q̂, p̂] = iℏ, and the Hamiltonian operator generates time evolution via the Schrödinger equation. Hamiltonian mechanics is therefore not just a reformulation of classical physics; it is the conceptual scaffold that makes quantum mechanics intelligible. Understanding why H and the canonical variables have the mathematical properties they do in classical mechanics is essential preparation for understanding why quantum mechanics is structured the way it is.
