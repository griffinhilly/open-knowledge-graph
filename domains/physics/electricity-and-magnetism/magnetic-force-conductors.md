---
id: magnetic-force-conductors
title: Magnetic Force on Current-Carrying Conductors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-force-lorentz
  type: hard
builds-toward:
- magnetic-torque-dipole
tags:
- magnetic-force
- current
- conductor
stage: formal-systems
status: draft
---

# Magnetic Force on Current-Carrying Conductors

## Core Idea
A wire of length L carrying current I in a magnetic field B⃗ experiences force F⃗ = I(L⃗ × B⃗), where L⃗ is in the direction of current. For an arbitrary path: F⃗ = I ∫ d⃗ℓ × B⃗. In a uniform field, F = BIL sin(θ), where θ is the angle between wire and field. This is the net result of Lorentz forces on all moving charge carriers.

## Explainer

You already know the Lorentz force: a charge q moving with velocity v⃗ in a magnetic field B⃗ experiences F⃗ = qv⃗ × B⃗. A current-carrying wire is simply a conductor where many charges are drifting in one direction. The **magnetic force on a conductor** is not a new law — it is the Lorentz force summed over all the mobile charge carriers inside.

Here is how the summation works. Consider a wire segment of length dℓ with cross-sectional area A. If the carrier density is n (charges per volume), each with charge q and drift velocity v_d, then the current is I = nqv_d·A. The number of carriers in the segment is n·A·dℓ. Each experiences force q·v_d × B⃗, so the total force on the segment is (n·A·dℓ)·q·v_d × B⃗ = I·dℓ × B⃗. This is the differential form F⃗ = I∫dℓ⃗ × B⃗, where dℓ⃗ points along the current direction.

For a straight wire of length L in a uniform field, this gives F = BIL sin(θ), where θ is the angle between the wire and the field. The direction of the force is given by the right-hand rule on I·L⃗ × B⃗: point fingers along the current, curl toward B⃗, and the thumb points in the force direction. Maximum force occurs when the wire is perpendicular to the field (θ = 90°); a wire parallel to the field experiences no force. This is the operating principle of electric motors — loop-shaped conductors in a magnetic field experience torques because opposite sides of the loop carry current in opposite directions and therefore experience forces in opposite directions, producing rotation.

The key subtlety is that the magnetic force is transmitted to the wire as a whole, not just to the electrons. The drifting electrons are pushed sideways by B⃗, but since they are confined within the conductor, they push on the lattice of positive ions, and the entire wire accelerates. This mechanical force on macroscopic objects is the bridge between microscopic electromagnetism and everyday engineering: it underlies speakers, rail guns, magnetohydrodynamic drives, and every electromagnetic actuator ever built.
