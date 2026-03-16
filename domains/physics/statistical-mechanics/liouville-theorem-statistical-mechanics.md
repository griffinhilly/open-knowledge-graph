---
id: liouville-theorem-statistical-mechanics
title: Liouville's Theorem
domain: physics
course: statistical-mechanics
prerequisites:
- id: ensemble-theory-fundamentals
  type: hard
- id: hamiltonian-mechanics
  type: hard
builds-toward:
- ergodic-hypothesis
- phase-space-density-evolution
tags:
- foundations
- phase-space
- dynamics
stage: advanced
status: draft
---

# Liouville's Theorem

## Core Idea
Liouville's theorem states that the density of microstates in phase space is conserved under Hamiltonian evolution: ∂ρ/∂t + {ρ,H} = 0. This shows that the 'volume' occupied by an ensemble in phase space remains invariant as the system evolves, establishing a connection between deterministic dynamics and statistical ensembles.

## Explainer

From Hamiltonian mechanics, you know that the state of a system with N degrees of freedom is a single point in a 2N-dimensional **phase space** — N coordinates q₁, …, qN and N momenta p₁, …, pN. The equations of motion, q̇ᵢ = ∂H/∂pᵢ and ṗᵢ = −∂H/∂qᵢ, define a flow field in this space: each point moves along a trajectory determined by the Hamiltonian H. From ensemble theory, rather than tracking one system, we imagine a vast collection (ensemble) of identical systems in different microstates — a cloud of points in phase space. The **phase space density** ρ(q, p, t) describes how densely those points are distributed.

Liouville's theorem says this cloud flows like an incompressible fluid. As the ensemble evolves, the shape of the cloud distorts — it can stretch and twist — but its total volume never changes. The mathematical statement is the continuity equation ∂ρ/∂t + {ρ, H} = 0, where {ρ, H} is the **Poisson bracket** Σᵢ (∂ρ/∂qᵢ ∂H/∂pᵢ − ∂ρ/∂pᵢ ∂H/∂qᵢ). This is the phase-space analog of the incompressibility condition ∇·v = 0 for fluid flow. The proof uses Hamilton's equations directly: the divergence of the phase-space velocity field is identically zero, ∂q̇ᵢ/∂qᵢ + ∂ṗᵢ/∂pᵢ = ∂²H/∂qᵢ∂pᵢ − ∂²H/∂pᵢ∂qᵢ = 0, by symmetry of mixed partial derivatives.

The physical meaning is profound. An equivalent way to state the theorem is that ρ is constant along any trajectory: dρ/dt = ∂ρ/∂t + {ρ, H} = 0. If you ride along with a point in the ensemble, the density around you never changes. This means **Hamiltonian evolution preserves information**: no two trajectories can merge (that would compress the cloud and violate the theorem), and no information is ever lost about the initial microstate. This has deep implications. For a stationary (equilibrium) ensemble, we need ∂ρ/∂t = 0, which requires {ρ, H} = 0 — so ρ must be a function of H alone. This is why the canonical ensemble takes the form ρ ∝ exp(−H/kT): it is a function of H and therefore automatically satisfies the Liouville condition.

Liouville's theorem also provides the foundation for the **ergodic hypothesis**: if the theorem guarantees that a finite-volume region of phase space preserves its volume forever, then a single trajectory might (under ergodic conditions) eventually visit every part of the energy surface. The time average then equals the ensemble average — the key step that connects the trajectory of a single physical system to the averages computed from the statistical ensemble. Without Liouville's theorem, the whole framework of connecting deterministic mechanics to statistical mechanics would lack a rigorous underpinning.
