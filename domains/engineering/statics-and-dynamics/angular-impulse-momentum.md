---
id: angular-impulse-momentum
title: Angular Impulse and Momentum for Rigid Bodies
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: impulse-momentum-particles
  type: hard
- id: mass-moment-of-inertia
  type: hard
builds-toward:
- vibrations-single-dof
tags:
- dynamics
- angular momentum
- angular impulse
- conservation
- rigid bodies
- impact
stage: formal-systems
status: draft
---

# Angular Impulse and Momentum for Rigid Bodies

## Core Idea
The angular impulse-momentum principle extends the particle-based impulse-momentum method to rigid bodies by accounting for rotational inertia. For a rigid body in planar motion, the angular momentum about the mass center G is H_G = I_G * omega, and the angular impulse-momentum equation is ΣM_G * dt (integrated over time) = I_G * omega_2 - I_G * omega_1. When moments are summed about a fixed point O, H_O = I_O * omega (for pure rotation) or H_O = I_G * omega + m * v_G * d (for general motion, where d is the moment arm of the linear momentum about O). Conservation of angular momentum applies when the net external angular impulse about a point is zero — this is critical in analyzing collisions and sudden impacts of rigid bodies, where impulsive forces at the impact point create large angular impulses while other forces (gravity, spring forces) are negligible over the short impact duration.

## How It's Best Learned
Combine the linear impulse-momentum equation (for the mass center) with the angular impulse-momentum equation (about the mass center or a fixed point) to solve rigid-body impact problems. For eccentric impacts, set up the coefficient of restitution equation at the contact point and solve simultaneously with impulse-momentum. Practice with problems involving a rod striking a pivot or a ball hitting a bat to see how the impact point location affects post-impact angular velocity.

## Common Misconceptions
- Using mass moment of inertia about the wrong point — H_G = I_G * omega uses I about G, while H_O = I_O * omega is valid only for rotation about the fixed point O.
- Forgetting the m * v_G * d cross-term when computing angular momentum about a point that is not the mass center or a fixed point of rotation.
- Applying conservation of angular momentum about a point where external forces (like pin reactions) create nonzero angular impulses during the time interval of interest.
