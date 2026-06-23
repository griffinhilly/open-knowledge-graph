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
- id: rigid-body-kinetics-force-acceleration
  type: soft
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
status: validated
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

## Questions

```yaml
- question: "During a brief impact between a bat and a ball, which reference point should you choose to eliminate the unknown impulsive contact force from your angular impulse-momentum equation?"
  type: multiple-choice
  options:
    - "The mass center G of the bat, because I_G is always known"
    - "The contact point itself, because the impulsive force acts there and creates a zero moment arm"
    - "A fixed point far from the impact, to minimize moment arms of all forces"
    - "The center of mass of the ball, to treat both objects symmetrically"
  answer: 1
  explanation: "A moment equals force times perpendicular distance. If you sum moments about the contact point, the impulsive contact force — acting at exactly that point — has zero moment arm and thus contributes zero angular impulse. This eliminates the unknown from the equation, leaving something you can solve. This is the same strategy used in statics: choose a moment center that passes through unknown forces to remove them. Summing about G (option A) does not eliminate the contact force, because the contact point is generally not at G."

- question: "A rigid body slides across a surface while also rotating (general planar motion). You want to compute its angular momentum about a fixed floor point O. Which formula applies?"
  type: multiple-choice
  options:
    - "H_O = I_O × ω, using mass moment of inertia about O"
    - "H_O = I_G × ω, using mass moment of inertia about the mass center G"
    - "H_O = I_G × ω + m × v_G × d, where d is the perpendicular distance from O to v_G"
    - "H_O = m × v_G × d only, because the spinning contribution cancels for a sliding body"
  answer: 2
  explanation: "For a body in general planar motion (not rotating about a fixed point), angular momentum about any point O has two contributions: (1) the spin about the mass center (I_G × ω) and (2) the orbital contribution of the mass center moving around O (m × v_G × d). Omitting the cross-term (option B) is the most common error in rigid-body impact problems. H_O = I_O × ω is valid only when O is a fixed point the body rotates about — it cannot be applied to a body that simultaneously slides and spins."

- question: "During a very brief impact, gravitational impulse is negligible compared to the impulsive contact forces and can be ignored in the impulse-momentum equations."
  type: true-false
  answer: true
  explanation: "Impulse = force × time. During an impact, the contact force is enormous (often thousands of newtons over microseconds) while gravity is modest (weight × small Δt). Because the impact time interval is so short, gravity's impulse contribution is negligible compared to the impulsive contact force. This approximation is standard in impact mechanics and is what allows 'finite' forces like gravity, springs, and friction to be ignored during the impact duration while treating contact forces as dominant."

- question: "The formula H_O = I_O × ω can be used to compute angular momentum about any chosen reference point O for a rigid body in planar motion."
  type: true-false
  answer: false
  explanation: "H_O = I_O × ω is only valid when O is a fixed point about which the body rotates. For a body in general planar motion — simultaneous translation and rotation — the correct expression is H_O = I_G × ω + m × v_G × d. Using H_O = I_O × ω for a body that is also translating would be incorrect because I_O implicitly assumes all motion is rotational about O. This is one of the most common errors in rigid-body impact analysis."

- question: "Explain why the location of the impact point on a bat (near the barrel vs. near the handle) affects post-impact rotation, even if the same magnitude of force is applied."
  type: short-answer
  answer: "Angular impulse equals the contact force times its perpendicular distance (moment arm) from the bat's mass center. Even for the same contact force, a point near the barrel (far from G) creates a large moment arm, delivering more angular impulse and producing greater post-impact angular velocity. A contact point near G creates little moment arm and barely spins the bat. This is why the 'sweet spot' exists: at a specific location, the angular and linear impulses combine so that the reaction force at the grip point is zero, eliminating the sting in the batter's hands."
  explanation: "This connects the abstract formula (angular impulse = ΣM × Δt) to the physical intuition of torque. Moment arm is the lever in angular impulse-momentum, just as in statics. Understanding this makes clear why impact problems require both linear and angular impulse-momentum equations simultaneously — they are coupled through the geometry of where the force is applied relative to G."
```

## Explainer

From your work with impulse-momentum for particles, you already know that a net force applied over time produces a change in linear momentum: F·Δt = Δ(mv). The angular version works identically — replace force with moment, and replace mass times velocity with **angular momentum**. For a rigid body spinning about its mass center G, the angular momentum is H_G = I_G · ω, where I_G is the mass moment of inertia you studied previously. A net moment applied over a time interval produces a change in H_G: ∫ΣM_G dt = I_G·ω₂ − I_G·ω₁. The left side is the **angular impulse**; the right side is the change in angular momentum.

The choice of reference point matters greatly. When a body rotates about a fixed pin O, you can sum angular momentum directly about O using H_O = I_O·ω. But for a body in general planar motion — sliding and rotating simultaneously — H_O has two contributions: the spinning of the body about its own center (I_G·ω) plus the "orbiting" of its mass center around O (m·v_G·d, where d is the perpendicular distance from O to the velocity vector of G). Forgetting this cross-term is the most common error in rigid-body impact problems.

**Conservation of angular momentum** applies when the net external angular impulse about a chosen point is zero over the time interval of interest. The key is selecting the right point. During a very brief impact, forces at the contact point are enormous (impulsive) while gravity and spring forces are negligible by comparison. If you sum moments about the contact point itself, those impulsive contact forces vanish from the equation — and you can write conservation of angular momentum even though large forces are present. This is the same reasoning you used for linear impulse-momentum: during an impact, sum about the point where unknown impulsive forces act to eliminate them from the equation.

**Eccentric impact** — when a force strikes a body at a point other than its mass center — couples rotation and translation. A ball striking a bat near the end transmits both linear and angular impulses to the bat. To solve these problems, combine three equations: the linear impulse-momentum equation for the mass center (covers translation), the angular impulse-momentum equation about G (covers rotation), and the coefficient-of-restitution equation at the contact point (relates relative velocities before and after). These three equations in three unknowns (two post-impact velocities and one angular velocity, depending on geometry) constitute the complete rigid-body impact solution. The location of the impact point relative to G is what determines how much the body spins after the hit — striking a bat at the "sweet spot" minimizes the sting in your hands precisely because the angular and linear impulses combine to produce zero reaction at the pivot point of your grip.
