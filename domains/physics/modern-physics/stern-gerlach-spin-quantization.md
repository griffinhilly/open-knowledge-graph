---
id: stern-gerlach-spin-quantization
title: 'Stern-Gerlach Experiment: Spin Quantization and Measurement'
domain: physics
course: modern-physics
prerequisites:
- id: electron-spin-magnetic-moment
  type: hard
- id: measurement-problem-quantum
  type: hard
tags:
- spin
- measurement
- quantum-mechanics
- experimental
stage: advanced
status: draft
---

# Stern-Gerlach Experiment: Spin Quantization and Measurement

## Core Idea
An inhomogeneous magnetic field exerts a force on a magnetic dipole. Atoms with spin experience a force proportional to the z-component of spin, splitting a beam into two: spin-up and spin-down. Cascading Stern-Gerlach devices reveal that spin measurement is projective (a spin-up atom will always show as spin-up in another z-aligned device) and that spin components are incompatible observables (measuring S_x destroys information about S_z).

## How It's Best Learned
Trace particle trajectories through sequential Stern-Gerlach devices with different orientations. Understand that measurement of one component randomizes the others. Quantitatively predict splitting angles and beam intensities.

## Common Misconceptions
Particles do not have pre-existing definite spin states that are merely revealed by measurement (measurement creates the outcome). The two beams have equal intensity only if the initial beam is unpolarized; oriented beams split unequally.

## Explainer

You already know that an electron has a **magnetic moment** proportional to its spin. In a uniform magnetic field the electron just precesses — nothing dramatic. But when Stern and Gerlach ran a beam of silver atoms through a *non-uniform* magnetic field, the field gradient exerted a net force on each magnetic dipole, bending the trajectory upward or downward depending on the orientation of the moment. The key prediction of classical physics was a continuous smear of deflections, since classically the magnetic moment could point in any direction. What they observed instead was exactly two discrete spots — direct evidence that the z-component of spin takes only two values, +ℏ/2 and −ℏ/2. **Spin quantization** is not a theoretical assumption imposed on the theory; it is an experimental result that demands the theory.

The power of the Stern-Gerlach experiment goes beyond measuring spin. It is also the clearest demonstration of **projective measurement**. If you take the spin-up beam from one z-aligned device and send it into a second z-aligned device, you get 100% spin-up output — no spin-down. The first measurement prepared a definite state, and the second measurement simply confirms it. This is not like sorting balls by color; it is the state itself being created by the measurement act. No pre-existing property is being revealed.

The deeper insight comes from **sequential measurements with rotated devices**. Take the spin-up output of a z-device and send it into an x-aligned device. Now you get 50% spin-up-x and 50% spin-down-x — perfectly random. Take the spin-up-x output and feed it back into a z-device: again 50/50. Measuring S_x has completely randomized S_z. This is not a disturbance from imprecision; it follows from the algebra of spin operators. S_x and S_z do not commute, so they are **incompatible observables** — having a definite value for one implies maximal uncertainty in the other, exactly as the Heisenberg uncertainty principle demands for non-commuting operators.

This incompatibility has a concrete consequence: information about spin is orientation-specific. A beam that is "pure spin-up-z" has zero net S_x polarization, and vice versa. The Stern-Gerlach apparatus acts like a rotatable basis projector, filtering out one component of the quantum state and discarding the rest. Building the intuition that measurement is selection rather than revelation — and that different component measurements are genuinely exclusive — is the conceptual core of understanding spin and, more broadly, quantum measurement theory.
