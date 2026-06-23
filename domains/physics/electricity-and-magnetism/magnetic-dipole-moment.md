---
id: magnetic-dipole-moment
title: Magnetic Dipole Moment from Current Loops
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: circular-motion-dynamics
  type: hard
tags:
- magnetism
- dipoles
- angular momentum
stage: formal-systems
status: validated
---

# Magnetic Dipole Moment from Current Loops

## Core Idea
A current loop has magnetic dipole moment μ = IA, where I is current and A is the area vector. The magnetic dipole plays the same role in magnetism as electric dipole does in electrostatics. A dipole experiences torque τ = μ × B in an external field and has potential energy U = -μ·B. The dipole moment can arise from circulating currents, spinning particles, or intrinsic spin.

## Questions

```yaml
- question: "A current loop sits in a uniform external magnetic field B. When is the loop's potential energy U = -μ·B at its minimum?"
  type: multiple-choice
  options:
    - "When the plane of the loop is perpendicular to B (the loop's axis is aligned with the field)"
    - "When the plane of the loop is parallel to B (the loop's axis is perpendicular to the field)"
    - "When μ is antiparallel to B"
    - "Potential energy is the same in all orientations because B is uniform"
  answer: 0
  explanation: "U = -μ·B = -μB cosθ, where θ is the angle between μ and B. This is minimized when cosθ = 1, i.e., when μ is parallel to B. The magnetic moment vector μ points along the loop's axis (perpendicular to the loop's plane), so the loop's axis must align with B. Option B is the maximum-torque orientation (θ = 90°), not minimum energy. Option C (antiparallel) gives U = +μB — maximum energy, an unstable equilibrium."

- question: "Two circular current loops have identical areas. Loop A carries current I; Loop B carries current 2I. How do their magnetic dipole moments compare?"
  type: multiple-choice
  options:
    - "They are equal — magnetic dipole moment depends only on area, not on current magnitude"
    - "Loop B has twice the magnetic dipole moment of Loop A"
    - "Loop A has twice the magnetic dipole moment of Loop B"
    - "The comparison requires knowing the loops' radii, not just their areas"
  answer: 1
  explanation: "The magnetic dipole moment is μ = IA, so it is proportional to both current and area. Loop B carries 2I with the same area A, giving μ_B = 2IA = 2μ_A. Option A is the common error of confusing area as the sole determinant. Since both loops have the same area, the difference in current is the only variable — and it enters linearly."

- question: "The torque on a magnetic dipole in a uniform external field tends to push the dipole toward regions of stronger magnetic field."
  type: true-false
  answer: false
  explanation: "Torque and translational force are distinct effects. Torque (τ = μ × B) acts to rotate the dipole — aligning μ with B, it brings the system to lower energy. A net force pushing the dipole toward stronger field regions is a separate phenomenon that requires a non-uniform field: F = ∇(μ·B). In a uniform field, there is torque but zero net translational force. Conflating torque with force is a common error that comes from confusing two different equations."

- question: "A current loop and a spinning uniformly charged sphere can both possess magnetic dipole moments because both involve charge in circulation."
  type: true-false
  answer: true
  explanation: "Any closed path of moving charge constitutes a current loop and therefore has a magnetic dipole moment μ = IA. A spinning charged sphere has surface charges rotating about the spin axis — each charged element traces a circular orbit, constituting a small current loop. The total dipole moment is the sum over all such elements. This is why spinning particles (electrons, protons, neutrons) have magnetic moments, and why the magnetic dipole concept spans from laboratory coils to intrinsic quantum spin."

- question: "Why does a compass needle align with Earth's magnetic field? Explain using the magnetic dipole moment and the torque equation."
  type: short-answer
  answer: "A compass needle is a magnetic dipole with moment μ. In Earth's external field B, it experiences torque τ = μ × B. This torque is nonzero whenever μ is not aligned with B, and it acts to rotate the needle toward alignment. The torque vanishes when μ is parallel to B (minimum energy, U = -μB). Any slight perturbation from alignment restores the torque, making parallel alignment a stable equilibrium. The needle swings to this minimum-energy orientation and (after damping) stays there."
  explanation: "This question tests whether students can connect the abstract equation τ = μ × B to a concrete physical phenomenon. The key steps are: (1) a compass needle is a magnetic dipole; (2) a dipole in an external field experiences a torque that is zero only when μ and B are parallel; (3) parallel alignment is minimum energy (U = -μB), so it is a stable equilibrium; (4) therefore the torque consistently drives the needle to point along the field. The same reasoning explains how MRI machines manipulate nuclear dipole moments and how electric motors produce rotation."
```

## Explainer

You already know that moving charges create magnetic fields, and that a magnetic field exerts forces on moving charges. A **current loop** — any closed path carrying a steady current — is the simplest object that synthesizes both: it produces a magnetic field around it, and it responds to external magnetic fields with a net torque. The compact quantity that encodes everything about how a loop interacts with an external field is its **magnetic dipole moment** μ⃗ = I A⃗, where I is the current and A⃗ is the area vector (magnitude = enclosed area, direction given by the right-hand rule relative to the current's circulation direction).

The analogy to the electric dipole is precise and useful. An electric dipole p⃗ = q d⃗ (two equal and opposite charges separated by a distance d) experiences torque τ⃗ = p⃗ × E⃗ in an electric field and has energy U = −p⃗·E⃗. The magnetic dipole obeys exactly the same equations: τ⃗ = μ⃗ × B⃗ and U = −μ⃗·B⃗. The torque tries to align the dipole with the external field (minimum energy when μ⃗ and B⃗ are parallel). This is why a compass needle — a small magnetic dipole — aligns with Earth's magnetic field: the torque rotates it until μ⃗ points along B⃗.

From circular-motion dynamics, you know that a particle moving in a circle has angular momentum L⃗ proportional to its mass, speed, and radius. A charged particle in circular motion also constitutes a current loop, so it has both angular momentum and magnetic dipole moment. The ratio μ/L is the **gyromagnetic ratio**, and it connects mechanical angular momentum to magnetic response. For an electron in a classical circular orbit, this ratio is e/2m_e. In quantum mechanics the same ratio governs how angular momentum quantum numbers relate to magnetic moments, and the anomalous gyromagnetic ratio of the electron (approximately 2, not 1) was one of the first puzzles that quantum field theory had to explain.

The magnetic dipole concept scales from the microscopic to the macroscopic. A single current loop in a lab, an electron orbiting a nucleus, a spinning proton, the coil in an electric motor, and the magnetized domain in a piece of iron are all magnetic dipoles at different scales. The dipole moment characterizes how strongly each responds to and contributes to magnetic fields. Understanding the torque and energy equations here is the direct prerequisite for understanding how MRI machines manipulate nuclear dipole moments, how electric motors convert electrical energy to rotational mechanical energy, and how ferromagnetism arises from the alignment of atomic dipoles.
