---
id: ergodicity-breaking
title: Ergodicity Breaking
domain: physics
course: statistical-mechanics
prerequisites:
- id: ergodic-hypothesis
  type: hard
- id: phase-transitions
  type: soft
builds-toward:
- spin-glasses-quenched-disorder
tags:
- non-equilibrium
- disorder
- dynamics
stage: advanced
status: draft
---

# Ergodicity Breaking

## Core Idea
Ergodicity breaking occurs when a system's phase space fragments into disconnected regions separated by high barriers, preventing exploration of all microstates within experimental timescales. This commonly occurs in glasses and disordered systems, where dynamics become trapped in limited phase space regions far from true equilibrium.

## Explainer

The **ergodic hypothesis** you studied earlier makes a sweeping claim: given long enough time, a system visits every microstate consistent with its macroscopic constraints, and time averages equal ensemble averages. Statistical mechanics is built on this foundation. Ergodicity breaking is what happens when that assumption fails — and understanding *when* and *why* it fails is essential for understanding glasses, disordered magnets, proteins, and a wide range of complex systems.

The simplest way to picture ergodicity breaking is through a **free energy landscape**. Imagine phase space not as a flat field but as a mountainous terrain, where valleys are configurations of low free energy and ridges are high-barrier transitions between them. In a well-behaved ergodic system, thermal fluctuations are large enough to hop over barriers on reasonable timescales, so the system explores all valleys. Ergodicity breaks when the barriers become so high — or so numerous — that the system is effectively trapped in one valley forever on any practical observation timescale. The system is not at true thermodynamic equilibrium; it is stuck in a **metastable state** that will never relax to the global minimum.

Glasses are the paradigm example. Cool a liquid fast enough and it does not crystallize; instead it becomes increasingly viscous as temperature drops, until molecular rearrangements become so slow that the material behaves mechanically like a solid. At the glass transition temperature T_g, the structural relaxation time exceeds experimental timescales — the system is frozen into one particular amorphous configuration out of an astronomically large number of equivalent configurations. Different glass samples cooled by different routes end up in different valleys; their properties depend on history, not just temperature and pressure. This history-dependence is the smoking gun of ergodicity breaking. From the phase transitions prerequisite, you know that a symmetry-broken ordered phase (like a ferromagnet below T_c) also breaks ergodicity — the system is trapped in one magnetization direction and never spontaneously flips — but that is **spontaneous symmetry breaking** at a sharp phase transition. Glass is subtler: there is no sharp transition, no obvious order parameter, and the trapping is kinetic rather than thermodynamic.

**Spin glasses** represent a more exotic form: magnetic systems with quenched random interactions where some bonds favor alignment and others anti-alignment. No single ordered state wins; instead the system freezes into a frustrated configuration that depends on the specific disorder realization. The system's phase space fragments into an exponentially large number of nearly-degenerate valleys separated by high barriers — an extreme form of ergodicity breaking called **replica symmetry breaking**. Time averages become sample-dependent and the usual statistical mechanics ensemble must be reconsidered. The study of ergodicity breaking thus sits at the boundary between equilibrium statistical mechanics, dynamics, and the physics of disordered systems — the frontier this course is building toward.
