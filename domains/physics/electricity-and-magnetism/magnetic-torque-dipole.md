---
id: magnetic-torque-dipole
title: Torque on Magnetic Dipoles
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-current-wires
  type: hard
builds-toward:
- inductance-circuits-rl-transients
tags:
- torque
- dipole
- rotation
stage: formal-systems
status: draft
---

# Torque on Magnetic Dipoles

## Core Idea
A current loop with magnetic moment μ = IA (A is area vector) in field B experiences torque τ = μ × B. Torque tends to align the dipole with the field. Potential energy is U = −μ⋅B.

## Questions

```yaml
- question: "A rectangular current loop is placed in a uniform magnetic field with its plane parallel to the field (magnetic moment perpendicular to B). What happens?"
  type: multiple-choice
  options:
    - "The loop accelerates in the direction of the field — the net force pushes it toward stronger field regions"
    - "Nothing happens — a uniform field cannot affect a current loop"
    - "The loop experiences zero net force but maximum torque, which rotates it toward alignment with the field"
    - "The loop experiences both a net force and a torque, since the field acts on each current-carrying side"
  answer: 2
  explanation: "In a uniform field, the forces on opposite sides of the loop are equal and opposite, so net translational force is zero — the loop doesn't move through space. But those equal-and-opposite forces act on different lines, creating a torque that rotates the loop. Torque is maximum when μ is perpendicular to B (the configuration here) and zero when μ is parallel to B. Option A describes behavior in a non-uniform field. Option D is wrong — net force is zero even though forces act on each side."

- question: "A magnetic dipole is oriented antiparallel to an external field (θ = 180°). Which statement about its energy and stability is correct?"
  type: multiple-choice
  options:
    - "U = −μB; this is the lowest-energy (stable) equilibrium"
    - "U = +μB; this is the highest-energy (unstable) equilibrium — the dipole will flip if perturbed"
    - "U = 0; antiparallel orientation is neutral since the dot product is undefined at 180°"
    - "U = −μB; the system is in unstable equilibrium because torque is at maximum"
  answer: 1
  explanation: "U = −μ·B = −μB cos θ. At θ = 180°, cos 180° = −1, so U = −μB(−1) = +μB — the maximum energy state. This is an unstable equilibrium: torque is zero (cos θ appears in τ = μB sin θ, and sin 180° = 0), so there's no torque at this exact orientation, but any small perturbation creates a torque that drives the dipole all the way to θ = 0 (the stable, minimum energy state at U = −μB). Option A has the right formula but wrong value. Option D gets the energy right but wrong about torque — torque at 180° is also zero."

- question: "A current loop in a uniform magnetic field experiences a net translational force that pushes it toward the region of strongest field."
  type: true-false
  answer: false
  explanation: "In a uniform field, net translational force on a current loop is exactly zero. The forces on opposite current segments cancel as a pair. Translational force only occurs in a non-uniform (gradient) field, where the force magnitude on one side differs from the other. This is why magnetic traps and force-on-dipole problems specify field gradients. The confusion here is between torque (which does exist in a uniform field) and translational force (which requires a field gradient)."

- question: "The torque on a magnetic dipole is zero when the magnetic moment is aligned parallel to the external field."
  type: true-false
  answer: true
  explanation: "τ = μ × B, so |τ| = μB sin θ. When μ is parallel to B, θ = 0, and sin 0 = 0, giving zero torque. This is the stable equilibrium configuration — the orientation where potential energy U = −μB cos 0 = −μB is minimized. A dipole released from any angle will oscillate about this aligned position. The same principle governs why compass needles align with Earth's magnetic field and why atomic magnetic moments precess around applied fields in MRI."

- question: "Explain why the potential energy of a magnetic dipole is written U = −μ·B, and what the negative sign reveals about the equilibrium orientation."
  type: short-answer
  answer: "The negative sign means potential energy is lowest when μ and B are parallel (θ = 0), making alignment the stable equilibrium. U = −μB cos θ ranges from −μB (aligned, minimum energy) to +μB (antiparallel, maximum energy). Systems naturally evolve toward lower potential energy, so a dipole released from any orientation will torque toward alignment. The negative sign encodes the physical fact that it costs energy to flip a dipole against a field — this energy difference (2μB) is exactly the photon energy absorbed in magnetic resonance imaging when a nuclear spin is flipped."
  explanation: "The sign convention follows from the work done by the torque as the dipole rotates. When the dipole aligns with B, the torque does positive work, reducing stored energy — hence the negative sign. This is the same mathematical structure as electric potential energy of a dipole (U = −p·E): both systems minimize energy by aligning their dipole moment with the external field. Understanding the sign is essential for applying this to atomic physics (Zeeman effect), NMR, and ferromagnetism."
```

## Explainer

From your study of magnetic forces on current-carrying wires, you know that a wire of length L carrying current I in a field B experiences force F = IL × B. A rectangular current loop in a uniform magnetic field extends this idea: opposite sides carry opposite current directions, so they experience opposite forces. In a uniform field these forces cancel out as net force — the loop doesn't translate. But they don't act on the same line, so they create a **torque** that tends to rotate the loop.

The quantity that characterizes the loop's response to an external magnetic field is the **magnetic dipole moment** μ = IA, where I is the current and A is the area vector (magnitude = loop area, direction given by the right-hand rule relative to the current flow). The torque is τ = μ × B. The cross product means torque is zero when μ is parallel to B (the equilibrium orientation) and maximum when μ is perpendicular to B. The direction of the torque always acts to rotate μ toward alignment with B — just as a compass needle rotates toward north.

The **potential energy** U = −μ⋅B = −μB cos θ completes the picture. When μ is antiparallel to B (θ = 180°), U = +μB — the highest energy state. When μ is parallel to B (θ = 0°), U = −μB — the lowest energy state. A dipole released from any orientation will oscillate about the aligned configuration (or relax to it if there's damping), exactly like a pendulum swinging toward equilibrium. The energy difference between aligned and antialigned states is 2μB, which appears in many physical contexts: this is the energy cost of flipping an atomic magnetic moment in an external field, the basis of magnetic resonance and the Zeeman effect.

The magnetic dipole is the magnetic analog of the electric dipole. Both feel torques (τ = p × E electrically, τ = μ × B magnetically) and both have potential energy minimized when aligned with the field. The difference is that magnetic dipoles arise from circulating currents, not separated charges — but the mathematical structure is identical. This parallel runs deep: it underlies the similarity between electric and magnetic terms in Maxwell's equations and explains why magnetic materials (with atomic current loops) behave so analogously to dielectric materials (with electric dipoles) when placed in external fields.
