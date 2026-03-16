---
id: uncertainty-relation-measurements
title: Uncertainty Relations and Simultaneous Measurement
domain: physics
course: modern-physics
prerequisites:
- id: heisenberg-uncertainty-principle
  type: hard
builds-toward:
- hydrogen-quantum-energy-levels
tags:
- quantum-mechanics
- uncertainty
stage: advanced
status: draft
---

# Uncertainty Relations and Simultaneous Measurement

## Core Idea
The uncertainty principle ΔxΔp ≥ ℏ/2 states that position and momentum cannot be simultaneously known to arbitrary precision. More generally, for any two operators that do not commute, [Â, B̂] ≠ 0, there is an uncertainty relation: ΔA·ΔB ≥ |⟨[Â,B̂]⟩|/2. This is not a limitation of measurement apparatus but a fundamental feature of quantum mechanics: incompatible observables cannot have simultaneous definite values.

## Explainer

You already know the Heisenberg uncertainty principle as the statement ΔxΔp ≥ ℏ/2. But where does this come from, and how does it generalize? The key is the **commutator**. Two observables are said to be **compatible** if their operators commute — [Â, B̂] = ÂB̂ − B̂Â = 0 — and **incompatible** if they do not. Compatible observables can be simultaneously measured to arbitrary precision, because the system can be in an eigenstate of both at once. Incompatible observables cannot: if the system has a definite value of A, then B is genuinely indefinite, not just unknown to us.

The position and momentum operators have commutator [x̂, p̂] = iℏ. Plugging into the **Robertson inequality** — ΔA·ΔB ≥ |⟨[Â,B̂]⟩|/2 — gives the familiar ΔxΔp ≥ ℏ/2 directly. The Robertson inequality applies to any pair of observables: energy and time (ΔEΔt ≥ ℏ/2), two components of angular momentum (ΔL_xΔL_y ≥ ℏ|⟨L_z⟩|/2), and more. Each of these is a statement about the mathematical structure of the operators involved, not about the clumsiness of the experimenter.

The most important conceptual shift from your earlier understanding: the uncertainty is **not about disturbance**. The old "microscope" thought experiment suggested that measuring position kicks the particle and disturbs its momentum. This is misleading. A particle in a momentum eigenstate simply does not have a definite position — the wavefunction is a plane wave spread over all space. The uncertainty is ontological, not epistemological. When ΔA is small, the wavefunction is sharply peaked in A-space, which mathematically forces ΔB to be large in the conjugate space via Fourier analysis.

A powerful way to see the structure: two observables can be simultaneously measured (they commute) if and only if there exists a complete set of states that are eigenstates of both operators simultaneously. For compatible pairs like energy and the z-component of angular momentum in a hydrogen atom, you can specify both quantum numbers exactly. For incompatible pairs like L_x and L_y, no such joint eigenstate exists — specifying L_x completely scrambles L_y. This is the algebraic heart of the uncertainty principle, and it turns out to be the same mathematical structure behind why measuring one observable can "collapse" the state and destroy information about the other.
