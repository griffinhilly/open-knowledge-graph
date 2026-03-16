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
builds-toward:
- magnetic-field-from-current-element
tags:
- magnetism
- dipoles
- angular momentum
stage: formal-systems
status: draft
---

# Magnetic Dipole Moment from Current Loops

## Core Idea
A current loop has magnetic dipole moment μ = IA, where I is current and A is the area vector. The magnetic dipole plays the same role in magnetism as electric dipole does in electrostatics. A dipole experiences torque τ = μ × B in an external field and has potential energy U = -μ·B. The dipole moment can arise from circulating currents, spinning particles, or intrinsic spin.

## Explainer

You already know that moving charges create magnetic fields, and that a magnetic field exerts forces on moving charges. A **current loop** — any closed path carrying a steady current — is the simplest object that synthesizes both: it produces a magnetic field around it, and it responds to external magnetic fields with a net torque. The compact quantity that encodes everything about how a loop interacts with an external field is its **magnetic dipole moment** μ⃗ = I A⃗, where I is the current and A⃗ is the area vector (magnitude = enclosed area, direction given by the right-hand rule relative to the current's circulation direction).

The analogy to the electric dipole is precise and useful. An electric dipole p⃗ = q d⃗ (two equal and opposite charges separated by a distance d) experiences torque τ⃗ = p⃗ × E⃗ in an electric field and has energy U = −p⃗·E⃗. The magnetic dipole obeys exactly the same equations: τ⃗ = μ⃗ × B⃗ and U = −μ⃗·B⃗. The torque tries to align the dipole with the external field (minimum energy when μ⃗ and B⃗ are parallel). This is why a compass needle — a small magnetic dipole — aligns with Earth's magnetic field: the torque rotates it until μ⃗ points along B⃗.

From circular-motion dynamics, you know that a particle moving in a circle has angular momentum L⃗ proportional to its mass, speed, and radius. A charged particle in circular motion also constitutes a current loop, so it has both angular momentum and magnetic dipole moment. The ratio μ/L is the **gyromagnetic ratio**, and it connects mechanical angular momentum to magnetic response. For an electron in a classical circular orbit, this ratio is e/2m_e. In quantum mechanics the same ratio governs how angular momentum quantum numbers relate to magnetic moments, and the anomalous gyromagnetic ratio of the electron (approximately 2, not 1) was one of the first puzzles that quantum field theory had to explain.

The magnetic dipole concept scales from the microscopic to the macroscopic. A single current loop in a lab, an electron orbiting a nucleus, a spinning proton, the coil in an electric motor, and the magnetized domain in a piece of iron are all magnetic dipoles at different scales. The dipole moment characterizes how strongly each responds to and contributes to magnetic fields. Understanding the torque and energy equations here is the direct prerequisite for understanding how MRI machines manipulate nuclear dipole moments, how electric motors convert electrical energy to rotational mechanical energy, and how ferromagnetism arises from the alignment of atomic dipoles.
