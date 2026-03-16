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

## Explainer

From your work with impulse-momentum for particles, you already know that a net force applied over time produces a change in linear momentum: F·Δt = Δ(mv). The angular version works identically — replace force with moment, and replace mass times velocity with **angular momentum**. For a rigid body spinning about its mass center G, the angular momentum is H_G = I_G · ω, where I_G is the mass moment of inertia you studied previously. A net moment applied over a time interval produces a change in H_G: ∫ΣM_G dt = I_G·ω₂ − I_G·ω₁. The left side is the **angular impulse**; the right side is the change in angular momentum.

The choice of reference point matters greatly. When a body rotates about a fixed pin O, you can sum angular momentum directly about O using H_O = I_O·ω. But for a body in general planar motion — sliding and rotating simultaneously — H_O has two contributions: the spinning of the body about its own center (I_G·ω) plus the "orbiting" of its mass center around O (m·v_G·d, where d is the perpendicular distance from O to the velocity vector of G). Forgetting this cross-term is the most common error in rigid-body impact problems.

**Conservation of angular momentum** applies when the net external angular impulse about a chosen point is zero over the time interval of interest. The key is selecting the right point. During a very brief impact, forces at the contact point are enormous (impulsive) while gravity and spring forces are negligible by comparison. If you sum moments about the contact point itself, those impulsive contact forces vanish from the equation — and you can write conservation of angular momentum even though large forces are present. This is the same reasoning you used for linear impulse-momentum: during an impact, sum about the point where unknown impulsive forces act to eliminate them from the equation.

**Eccentric impact** — when a force strikes a body at a point other than its mass center — couples rotation and translation. A ball striking a bat near the end transmits both linear and angular impulses to the bat. To solve these problems, combine three equations: the linear impulse-momentum equation for the mass center (covers translation), the angular impulse-momentum equation about G (covers rotation), and the coefficient-of-restitution equation at the contact point (relates relative velocities before and after). These three equations in three unknowns (two post-impact velocities and one angular velocity, depending on geometry) constitute the complete rigid-body impact solution. The location of the impact point relative to G is what determines how much the body spins after the hit — striking a bat at the "sweet spot" minimizes the sting in your hands precisely because the angular and linear impulses combine to produce zero reaction at the pivot point of your grip.
