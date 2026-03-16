---
id: dynamics-newtons-second-law
title: Newton's Second Law Applied to Particle Dynamics
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-rectilinear
  type: hard
- id: kinematics-particles-curvilinear
  type: hard
- id: newtons-second-law
  type: hard
- id: free-body-diagrams
  type: hard
builds-toward:
- work-energy-particles
- impulse-momentum-particles
tags:
- dynamics
- Newton's second law
- equations of motion
- particles
stage: formal-systems
status: validated
---

# Newton's Second Law Applied to Particle Dynamics

## Core Idea
In dynamics, ΣF = ma is applied component-by-component in the chosen coordinate system to find acceleration given forces, or to find required forces given a desired motion. In Cartesian form: ΣFx = max, ΣFy = may. In normal-tangential form: ΣFt = maₜ = m(dv/dt), ΣFn = maₙ = mv²/ρ. In polar form: ΣFr = m(r̈ − rθ̇²), ΣFθ = m(rθ̈ + 2ṙθ̇). The FBD shows only real forces; ma is kept on the equation's right side as the kinetic resultant.

## How It's Best Learned
Draw the FBD and a separate kinetic diagram (showing the ma vector) side by side. Choose the coordinate system consistent with the kinematics. For circular motion, identify centripetal acceleration direction explicitly to avoid sign errors.

## Common Misconceptions
- Including the ma term as a fictitious 'inertia force' on the FBD — ma belongs on the equation's right side, not the left.
- Applying equilibrium (ΣF = 0) to an accelerating particle.
- Mixing unit systems (e.g., pounds-force with kilograms) without applying the correct conversion factor.

## Questions

```yaml
- question: "A particle moves in a circle at constant speed. Which statement correctly describes the free-body diagram (FBD)?"
  type: multiple-choice
  options:
    - "The FBD includes a centripetal force mv²/r directed inward as one of the applied forces"
    - "The FBD shows only real applied forces; ΣFn = mv²/r is an equation relating those forces to acceleration, not an additional force"
    - "The FBD includes an outward inertia force ma to balance the net inward force"
    - "No FBD is needed because the particle travels at constant speed"
  answer: 1
  explanation: "The FBD contains only real physical forces (gravity, tension, normal force, etc.). The term mv²/r is the kinetic resultant — it appears on the right side of ΣFn = maₙ. Placing it on the FBD as an applied force would double-count it. The kinetic diagram showing the ma vector is drawn separately."

- question: "In polar coordinates, if a particle moves at constant radial distance r from the origin (pure rotation), the radial equation simplifies to ΣFr = −mrθ̇²."
  type: true-false
  answer: true
  explanation: "The general radial equation is ΣFr = m(r̈ − rθ̇²). When r is constant, ṙ = 0 and r̈ = 0, leaving ΣFr = −mrθ̇². This negative radial term represents the centripetal acceleration directed inward toward the origin, consistent with the particle being held on a circular path."

- question: "Why is it incorrect to include a 'centrifugal force' pointing outward on the free-body diagram when applying Newton's second law to a particle rounding a curve?"
  type: short-answer
  answer: "Newton's second law ΣF = ma is valid in inertial (non-accelerating) reference frames. In an inertial frame only real contact and body forces act on the particle; centrifugal force is a fictitious force that appears only when the equations are written in a rotating (non-inertial) reference frame."
  explanation: "Adding a fictitious centrifugal force to the FBD while also computing the real net force would incorrectly cancel the centripetal acceleration. In an inertial frame the net inward force — whatever combination of normal, tension, and gravity provides it — equals mv²/r, which is the centripetal requirement derived from the particle's curved path."
```

## Explainer

Newton's second law ΣF = ma looks simple, but applying it to particle dynamics requires two things you did not need in statics: a careful choice of coordinate system and a clean separation between the free-body diagram (real forces) and the kinetic diagram (the ma resultant). In statics ΣF = 0, so the coordinate system barely matters. In dynamics, the choice of coordinates determines how messy your algebra gets.

For Cartesian coordinates the equations are ΣFx = max and ΣFy = may, with constant unit vectors i and j. This works well for straight-line or projectile-type problems. For motion along a curved path, normal-tangential (n-t) coordinates are often cleaner: ΣFt = maₜ = m(dv/dt) gives the rate at which speed changes, while ΣFn = maₙ = mv²/ρ relates the net inward force to the centripetal requirement. Notice that even at constant speed (aₜ = 0), a net inward force is still needed to keep the particle curving — this is a common point of confusion. For problems phrased in terms of an angle from a fixed point, polar coordinates give ΣFr = m(r̈ − rθ̇²) and ΣFθ = m(rθ̈ + 2ṙθ̇), where the −rθ̇² and 2ṙθ̇ terms encode centripetal and Coriolis effects respectively.

The most persistent error in dynamics problems is treating ma as a force on the FBD — sometimes called a "D'Alembert inertia force." This leads students to write ΣF = 0 (equilibrium!) by moving ma to the left side, which is mathematically equivalent but pedagogically dangerous because it blurs the distinction between real forces and acceleration. Draw the FBD with real forces only, then set their sum equal to the mass times acceleration. Keeping these diagrams separate is the professional engineering practice for a reason: it prevents sign errors and makes the physics transparent.

When setting up any dynamics problem, the workflow is: (1) draw the FBD with all real forces, (2) choose the coordinate system that aligns naturally with the motion (circular path → n-t, angle-defined path → polar), (3) write the scalar equations component by component, and (4) bring in kinematic relationships from curvilinear kinematics to express acceleration in terms of position, speed, or time. Problems that combine a force law with a kinematic constraint — like a bead on a rotating rod — require all three coordinate-system forms to work together.
