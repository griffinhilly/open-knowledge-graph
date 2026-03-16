---
id: lorentz-transformations-em-fields
title: Lorentz Transformations of Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: lorentz-covariance-em
  type: hard
- id: lorentz-transformation
  type: hard
tags:
- field-transformation
- relativity
- electric-magnetic-duality
stage: advanced
status: draft
---

# Lorentz Transformations of Electromagnetic Fields

## Core Idea
Lorentz transformations relate electric and magnetic fields measured in different reference frames according to specific transformation rules. These rules reveal that E and B transform in an interdependent way: what appears as a pure electric field in one frame has a magnetic component in another, and vice versa. This 'electric-magnetic duality' demonstrates that the distinction between E and B is relative and depends on the observer's motion.

## Explainer

You already know how coordinates and velocities transform between inertial frames under the Lorentz transformation, and you know from Lorentz covariance of electromagnetism that E⃗ and B⃗ together form the antisymmetric **electromagnetic field tensor** Fᵘᵛ. The transformation rules for the fields are simply what you get when you apply the Lorentz transformation to this tensor. For a boost with velocity v along the x-axis, the components parallel to the boost direction are unchanged (E_x′ = E_x, B_x′ = B_x), while the transverse components mix: E_y′ = γ(E_y − vB_z), E_z′ = γ(E_z + vB_y), and the corresponding equations for B′. The structure is exactly parallel to how time and space mix under a boost — but now it's E and B mixing.

The cleanest illustration is a stationary point charge. In the charge's rest frame, there is a pure electrostatic field E⃗ pointing radially outward and B⃗ = 0 everywhere. Now boost to a frame where the charge is moving (equivalently, look at the fields of a moving charge from a stationary observer's perspective). The Lorentz transformation produces both a modified electric field and a nonzero magnetic field — exactly the fields you'd calculate by applying the Biot-Savart law to the moving charge. There is no new physics: the magnetic field of a moving charge is simply the electric field of the charge *as seen from a different inertial frame*. This is the deepest meaning of **electric-magnetic duality**: E and B are not independent physical objects but two aspects of a single electromagnetic field, whose decomposition into "electric" and "magnetic" parts depends on the observer's state of motion.

Two key **invariants** survive the transformation unchanged. The quantity E² − c²B² is a Lorentz scalar: all observers agree on its value. The quantity E⃗·B⃗ is also invariant. These invariants carry real information: if E⃗·B⃗ = 0 in one frame, it is zero in all frames (so perpendicular E and B remain perpendicular under any boost). If E² > c²B² in one frame, there exists a frame where B = 0; if B² > E²/c², there exists a frame where E = 0. These conditions tell you whether a given field configuration is "more electric" or "more magnetic" in an observer-independent sense.

The transformation rules resolve the classic paradox of a current-carrying wire seen from different frames. In the wire's rest frame, there is a magnetic field surrounding the wire and zero net electric field (the wire is neutral overall). But from the frame of a drifting electron in the wire, the positive lattice ions are moving — their Lorentz-contracted spacing increases the positive charge density, producing a net electric field. The electron's drift in the lab frame corresponds to a Coulomb attraction in its own rest frame. Both descriptions predict the same physical force on a nearby test charge; they just attribute it to E in one frame and B in another. This is not coincidence — it is the Lorentz transformation guaranteeing that forces and their physical effects are the same in all inertial frames.
