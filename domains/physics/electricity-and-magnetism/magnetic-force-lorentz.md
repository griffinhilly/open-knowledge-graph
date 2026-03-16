---
id: magnetic-force-lorentz
title: Magnetic Force on Moving Charges (Lorentz Force)
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: conservation-of-electric-charge
  type: soft
- id: cross-product
  type: hard
builds-toward:
- magnetic-force-conductors
tags:
- lorentz-force
- magnetic
- motion
stage: formal-systems
status: draft
---

# Magnetic Force on Moving Charges (Lorentz Force)

## Core Idea
A charge q moving with velocity v⃗ in a magnetic field B⃗ experiences force F⃗ = q(v⃗ × B⃗). This force is perpendicular to both v⃗ and B⃗, so it does no work and cannot change particle speed—only direction. Particles move in circles perpendicular to B⃗ with radius r = mv/(qB), demonstrating the non-conservative nature of magnetic forces.

## Explainer

From your study of the cross product, you know that v⃗ × B⃗ produces a vector perpendicular to both inputs, with a magnitude of |v||B|sin θ where θ is the angle between them. The **Lorentz magnetic force** F⃗ = q(v⃗ × B⃗) puts this geometry directly into physics: a charged particle moving through a magnetic field gets pushed sideways — always sideways. The direction is given by the right-hand rule: point your fingers along v⃗, curl them toward B⃗, and your thumb points in the direction of the force on a positive charge. A negative charge feels the opposite direction.

The most profound consequence of the perpendicularity is that **the magnetic force does no work**. Work is force dotted with displacement, W = F⃗·dr⃗. But the displacement of a particle is always along its velocity, and the force is always perpendicular to the velocity, so the dot product is always zero. Magnetic forces are a perpetual steering mechanism — they can redirect particles without ever speeding them up or slowing them down. This is why magnetic fields alone cannot accelerate particles from rest; particle accelerators use electric fields to gain energy and magnetic fields to bend the beam.

What happens when a charge enters a uniform magnetic field perpendicular to B⃗? The force is always perpendicular to the velocity, which continuously changes the velocity's direction without changing its magnitude. This is precisely the condition for **circular motion**: the Lorentz force provides the centripetal acceleration. Setting qvB = mv²/r and solving gives the **cyclotron radius** r = mv/(qB). Faster particles curve more gently (larger r); stronger fields bend them more tightly (smaller r); heavier particles are harder to deflect (larger m means larger r). If the particle has a velocity component along B⃗, that component is unaffected, so the particle traces a helix — a combination of circular motion perpendicular to B⃗ and straight-line motion along it.

This combination of steering ability and force-direction rule is exploited throughout physics and engineering. Mass spectrometers separate ions by their cyclotron radius — different m/q ratios give different circular arcs, allowing identification of isotopes. Cyclotrons and synchrotrons use it to guide particle beams. The aurora borealis results from charged particles spiraling along Earth's magnetic field lines and funneling toward the poles. As you go on to study forces on current-carrying conductors, you will apply the same F = qv × B logic to many drifting charges simultaneously, recovering the macroscopic force on wires.
