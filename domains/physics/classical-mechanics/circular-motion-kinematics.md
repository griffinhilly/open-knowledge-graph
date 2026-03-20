---
id: circular-motion-kinematics
title: 'Circular Motion: Kinematics'
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematics-2d
  type: hard
- id: radian-measure
  type: soft
- id: arc-length-circles
  type: soft
- id: projectile-motion
  type: soft
- id: trigonometric-ratios-review
  type: soft
- id: polar-coordinates
  type: soft
- id: converting-degrees-and-radians
  type: hard
- id: unit-circle
  type: soft
builds-toward:
- circular-motion-dynamics
- rotational-kinematics
- simple-harmonic-motion
tags:
- circular-motion
- centripetal-acceleration
- period
- frequency
stage: formal-systems
status: validated
---
# Circular Motion: Kinematics

## Core Idea
An object moving in a circle at constant speed is nonetheless accelerating because its direction changes. The centripetal acceleration points toward the center of the circle and has magnitude a_c = v²/r = ω²r, where ω is the angular velocity. Period T (time per revolution), frequency f = 1/T, and angular velocity ω = 2π/T are the key kinematic parameters.

## How It's Best Learned
Derive the centripetal acceleration formula geometrically by computing the change in velocity vector over a small arc. Practice converting between linear quantities (v, a) and angular quantities (ω, α) using the arc-length relationships v = ωr and a_t = αr.

## Common Misconceptions
- Thinking 'constant speed' means 'no acceleration' — speed is constant but velocity direction changes, so acceleration is nonzero.
- Confusing centripetal acceleration (directed inward) with tangential acceleration (directed along the arc).

## Questions

```yaml
- question: "A car drives at constant speed around a circular roundabout. Which statement about the car's acceleration is correct?"
  type: multiple-choice
  options:
    - "The car has zero acceleration because its speed is constant."
    - "The car has a centripetal acceleration directed outward, away from the center."
    - "The car has a centripetal acceleration directed inward, toward the center."
    - "The car has a tangential acceleration directed along its direction of travel."
  answer: 2
  explanation: "Acceleration is the rate of change of velocity, which is a vector. Even at constant speed, the direction of velocity changes continuously in circular motion, producing a nonzero acceleration. This centripetal ('center-seeking') acceleration always points toward the center of the circle. Its magnitude is a_c = v²/r. There is no tangential acceleration when speed is constant."

- question: "An object moving in a circle at constant speed experiences no net force, because its speed (and therefore kinetic energy) is not changing."
  type: true-false
  answer: false
  explanation: "This is the central misconception in circular motion. Net force is required to produce acceleration, and centripetal acceleration is nonzero even at constant speed. The net force (centripetal force, F = mv²/r) acts inward at all times, continuously changing the direction of the velocity vector without changing its magnitude. Kinetic energy is indeed constant, but force and energy change are different things."

- question: "An object moves in a circle of radius r at angular velocity ω. Express its centripetal acceleration in terms of ω and r, and explain why centripetal acceleration must point toward the center."
  type: short-answer
  answer: "Centripetal acceleration is a_c = ω²r. It points toward the center because the velocity vector is always tangent to the circle, and the rate of change of a tangent vector (as the object moves around) points radially inward toward the center. Geometrically, the change in velocity Δv over a small arc points toward the center, so the acceleration a = Δv/Δt does too."
  explanation: "The derivation comes from computing the vector difference between velocity at two nearby points on the circle. As Δt → 0, the direction of Δv converges to radially inward. The magnitude |Δv|/Δt gives v²/r = ω²r (using v = ωr). Both forms are useful: v²/r when linear speed is given, ω²r when angular velocity is given."
```

## Explainer

From 1D kinematics you learned that acceleration means changing speed. Circular motion challenges this intuition: an object can accelerate while its speed stays perfectly constant. The key is remembering that velocity is a vector — it has both magnitude (speed) and direction. When an object moves in a circle, its speed may be fixed, but its direction of motion changes continuously. Any change in velocity, whether in magnitude or direction, constitutes acceleration.

To see this concretely, imagine a car moving clockwise around a circular track. At the top of the circle the car moves to the right; a quarter-turn later it moves downward. The velocity vector has rotated 90°. The change in velocity over that quarter-turn points inward — toward the center of the circle — and dividing by the time elapsed gives the centripetal acceleration. Working through the geometry carefully (comparing velocity vectors at two nearby points and taking the limit as the arc shrinks) yields the formula a_c = v²/r = ω²r, always directed toward the center.

The three key kinematic parameters — period T, frequency f, and angular velocity ω — are tightly linked. T is the time for one complete revolution; f = 1/T is revolutions per second (Hz); ω = 2π/T is radians per second. The arc-length relation s = rθ connects angular and linear quantities: differentiating gives v = ωr (linear speed equals angular speed times radius), and differentiating again gives the tangential acceleration a_t = αr when angular speed is changing. For uniform circular motion (constant speed), α = 0 and only the centripetal acceleration exists.

It helps to keep centripetal and tangential acceleration clearly distinct. Centripetal acceleration (a_c = v²/r) points radially inward and is responsible for changing the *direction* of velocity. Tangential acceleration (a_t = αr) points along the arc and is responsible for changing the *magnitude* of velocity (speeding up or slowing down). In uniform circular motion there is only centripetal acceleration. In non-uniform circular motion (a car speeding around a curve) both components are present simultaneously, and the total acceleration vector is their vector sum.

These kinematic quantities describe the *motion* without specifying the *cause*. What produces the centripetal acceleration — a tension, friction, gravity, or a normal force — is the subject of circular motion dynamics. But understanding the kinematics first is essential: before you can apply Newton's second law to circular motion (F_net = ma_c = mv²/r), you must be clear that the required acceleration exists, is nonzero even at constant speed, and always points toward the center.
