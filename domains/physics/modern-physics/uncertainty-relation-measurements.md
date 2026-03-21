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

## Questions

```yaml
- question: "An electron is prepared in a precise momentum eigenstate — its momentum is known exactly. What can we say about its position?"
  type: multiple-choice
  options:
    - "Its position is also precisely known, since preparing a precise momentum state requires localizing the particle"
    - "Its position is unknown to us but is in principle precisely defined — the uncertainty is about our knowledge, not the electron itself"
    - "Its position is genuinely indefinite — the electron does not have a definite position, not just one that is unknown to the experimenter"
    - "Its position uncertainty depends on how carefully the momentum was measured"
  answer: 2
  explanation: "A momentum eigenstate has a wavefunction that is a plane wave extending over all space — position is genuinely not defined, not just unknown to the experimenter. The electron in a momentum eigenstate doesn't have a position we merely fail to know; position is undefined in this state. The uncertainty ΔxΔp ≥ ℏ/2 reflects this structural feature of quantum mechanics, not a limitation of measurement apparatus."

- question: "Two observables can be simultaneously measured to arbitrary precision if and only if which condition holds?"
  type: multiple-choice
  options:
    - "Both observables are bounded operators on Hilbert space"
    - "Their operators commute — [Â, B̂] = 0 — meaning there exists a complete set of simultaneous eigenstates for both"
    - "The measurement of one observable is performed before the measurement of the other"
    - "The observables are measured with instruments that do not physically interact with the quantum system"
  answer: 1
  explanation: "Compatible observables have commuting operators, which means there exists a complete set of states that are eigenstates of both operators simultaneously — the system can have definite values of both at once. Incompatible observables have no such joint eigenstate: specifying one completely forces the conjugate to be indefinite. This is the algebraic heart of the uncertainty principle — not experimental clumsiness but the mathematical structure of quantum observables."

- question: "The Heisenberg uncertainty principle is fundamentally about the ontology of quantum states: incompatible observables cannot have simultaneous definite values, regardless of how the measurement is performed."
  type: true-false
  answer: true
  explanation: "This is the crucial upgrade from the 'microscope' thought experiment. The old picture suggested that measuring position physically disturbs momentum. But the uncertainty is deeper: a particle in a momentum eigenstate simply does not have a definite position, whether or not any measurement has been made. The uncertainty ΔxΔp ≥ ℏ/2 is a statement about the mathematical structure of quantum states via the Robertson inequality and commutator [x̂, p̂] = iℏ, not about experimental technique."

- question: "If a physicist devised an infinitely precise measuring instrument with no back-action on the quantum system, they could in principle measure both position and momentum simultaneously to arbitrary precision."
  type: true-false
  answer: false
  explanation: "No improvement in measurement technology can circumvent the uncertainty principle, because the uncertainty is not caused by measurement disturbance. A particle simply cannot be in a state that has both a definite position and a definite momentum — these are incompatible observables whose operators don't commute. The Robertson inequality ΔxΔp ≥ ℏ/2 holds for any quantum state, independently of how the measurement is performed."

- question: "Why does Heisenberg's 'microscope' thought experiment give a misleading picture of the uncertainty principle, and what is the correct interpretation?"
  type: short-answer
  answer: "The microscope thought experiment suggests that measuring position requires photons that physically kick the particle and disturb its momentum, making the uncertainty sound epistemological — we could know both values, but the act of measurement prevents it. The correct interpretation is ontological: a particle in a momentum eigenstate (plane wave spread over all space) genuinely does not have a definite position — no measurement is needed for this to be true. The uncertainty ΔxΔp ≥ ℏ/2 follows mathematically from the commutator [x̂, p̂] = iℏ via the Robertson inequality. It is a constraint on the structure of quantum states, not a statement about what we can know about pre-existing definite values."
  explanation: "The distinction matters both philosophically and practically. If uncertainty were epistemic, we might hope to measure both quantities indirectly, or circumvent the disturbance with clever apparatus. Because it is ontological — the simultaneous definite values simply don't exist — no such workaround is possible. This is why the uncertainty principle cannot be engineered away."
```

## Explainer

You already know the Heisenberg uncertainty principle as the statement ΔxΔp ≥ ℏ/2. But where does this come from, and how does it generalize? The key is the **commutator**. Two observables are said to be **compatible** if their operators commute — [Â, B̂] = ÂB̂ − B̂Â = 0 — and **incompatible** if they do not. Compatible observables can be simultaneously measured to arbitrary precision, because the system can be in an eigenstate of both at once. Incompatible observables cannot: if the system has a definite value of A, then B is genuinely indefinite, not just unknown to us.

The position and momentum operators have commutator [x̂, p̂] = iℏ. Plugging into the **Robertson inequality** — ΔA·ΔB ≥ |⟨[Â,B̂]⟩|/2 — gives the familiar ΔxΔp ≥ ℏ/2 directly. The Robertson inequality applies to any pair of observables: energy and time (ΔEΔt ≥ ℏ/2), two components of angular momentum (ΔL_xΔL_y ≥ ℏ|⟨L_z⟩|/2), and more. Each of these is a statement about the mathematical structure of the operators involved, not about the clumsiness of the experimenter.

The most important conceptual shift from your earlier understanding: the uncertainty is **not about disturbance**. The old "microscope" thought experiment suggested that measuring position kicks the particle and disturbs its momentum. This is misleading. A particle in a momentum eigenstate simply does not have a definite position — the wavefunction is a plane wave spread over all space. The uncertainty is ontological, not epistemological. When ΔA is small, the wavefunction is sharply peaked in A-space, which mathematically forces ΔB to be large in the conjugate space via Fourier analysis.

A powerful way to see the structure: two observables can be simultaneously measured (they commute) if and only if there exists a complete set of states that are eigenstates of both operators simultaneously. For compatible pairs like energy and the z-component of angular momentum in a hydrogen atom, you can specify both quantum numbers exactly. For incompatible pairs like L_x and L_y, no such joint eigenstate exists — specifying L_x completely scrambles L_y. This is the algebraic heart of the uncertainty principle, and it turns out to be the same mathematical structure behind why measuring one observable can "collapse" the state and destroy information about the other.
