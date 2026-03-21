---
id: free-fall
title: Free Fall and Gravitational Acceleration
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematic-equations
  type: hard
builds-toward:
- projectile-motion
- newtons-law-of-gravitation
tags:
- free-fall
- gravity
- acceleration
- kinematics
stage: formal-systems
status: validated
---

# Free Fall and Gravitational Acceleration

## Core Idea
Near Earth's surface, all objects in free fall (no air resistance) accelerate downward at g ≈ 9.8 m/s², regardless of mass. This was Galileo's great insight: heavy and light objects fall at the same rate. Free fall is the simplest application of kinematic equations with constant acceleration, and it sets the physical scale for everything in classical mechanics.

## How It's Best Learned
Drop objects and time them, then compare predictions from x = ½gt² to measurements. Extend to objects thrown upward: the acceleration is still −g throughout, even at the peak where velocity is zero.

## Common Misconceptions
- Believing heavier objects fall faster — this is only true when air resistance matters.
- Forgetting that g acts downward continuously, even as the object moves upward after being thrown.

## Questions

```yaml
- question: "A bowling ball and a ping-pong ball are dropped simultaneously from the same height in a vacuum chamber. Which hits the ground first?"
  type: multiple-choice
  options:
    - "The bowling ball — gravity pulls it more strongly because it is heavier"
    - "The ping-pong ball — it is lighter and therefore easier to accelerate"
    - "They hit simultaneously — all objects fall with the same acceleration g regardless of mass"
    - "The bowling ball — heavier objects always fall faster when dropped from rest"
  answer: 2
  explanation: "All objects fall with the same acceleration g ≈ 9.8 m/s² regardless of mass. The gravitational force on an object is F = mg, which is larger for a heavier object — but Newton's second law gives acceleration as a = F/m = mg/m = g. The mass cancels exactly. The heavier object is pulled harder by gravity, but it is proportionally harder to accelerate, and these two effects cancel precisely. The intuition that heavy objects fall faster comes from real-world experience with air resistance, which affects lighter objects more — but in a vacuum, the universality is exact."

- question: "A ball is thrown straight upward. At the exact instant it reaches its maximum height and momentarily has zero velocity, what is its acceleration?"
  type: multiple-choice
  options:
    - "Zero — the ball has stopped moving, so it is not accelerating"
    - "9.8 m/s² upward, since it is about to begin moving downward"
    - "9.8 m/s² downward — gravity acts continuously regardless of the direction or magnitude of velocity"
    - "Less than 9.8 m/s² — the ball is decelerating as it approaches the peak"
  answer: 2
  explanation: "Gravity acts continuously at g = 9.8 m/s² downward throughout the entire flight — while the ball moves up, at the peak, and while it falls down. At the peak, velocity is zero but acceleration is not. Acceleration measures how velocity is changing, not whether the object is moving. The ball's velocity changes from positive (upward) to zero to negative (downward) at a constant rate of 9.8 m/s² per second. Option A is the classic misconception: students conflate zero velocity with zero acceleration. If acceleration were truly zero at the peak, the ball would remain suspended there indefinitely."

- question: "In the absence of air resistance, a feather and a hammer dropped from the same height will reach the ground at the same time."
  type: true-false
  answer: true
  explanation: "This is Galileo's key insight, famously demonstrated on the Moon during Apollo 15. Without air resistance, all objects near Earth's surface fall with the same acceleration g. The feather falls slowly in air not because gravity pulls it less, but because air resistance (proportional to surface area and velocity) disproportionately impedes light objects. In vacuum, the feather's low mass means gravity's pull on it is small, but that small force also has little inertia to overcome — the ratio F/m = g is identical for both objects."

- question: "When a ball is thrown upward, its acceleration decreases as it rises (because it is slowing down) and increases as it falls back down (because it is speeding up)."
  type: true-false
  answer: false
  explanation: "Acceleration is constant at g = 9.8 m/s² downward throughout the entire trajectory. 'Slowing down' means velocity is decreasing in magnitude, but it does not mean acceleration is decreasing — a constant downward acceleration of 9.8 m/s² is precisely what causes the upward-moving ball to slow at a steady rate of 9.8 m/s per second. This confusion conflates the sign and magnitude of velocity with the sign and magnitude of acceleration. The acceleration doesn't know or care about the direction of velocity; it simply acts downward at g the entire time."

- question: "Why do all objects fall at the same rate in the absence of air resistance, regardless of their mass? Use Newton's second law to explain the cancellation."
  type: short-answer
  answer: "The gravitational force on an object is F = mg, which is proportional to its mass — heavier objects are pulled harder. But Newton's second law says a = F/m, so a = mg/m = g. The mass cancels completely: the increased gravitational pull on a heavier object is exactly offset by the increased inertia (resistance to acceleration) of that same mass. The result is that all objects near Earth's surface accelerate at g ≈ 9.8 m/s² regardless of mass. This cancellation is not a coincidence — it reflects the deep equivalence between gravitational mass (how strongly gravity pulls) and inertial mass (how hard it is to accelerate)."
  explanation: "This equivalence between gravitational and inertial mass — which Newton treated as a coincidence requiring experimental confirmation — became a foundational principle of Einstein's general relativity (the equivalence principle). In everyday terms: yes, a truck weighs more than a pebble, but the truck also needs proportionally more force to change its motion. In free fall, gravity provides exactly that proportional force, leaving the acceleration identical for both."
```

## Explainer

From your study of kinematic equations, you know how to describe motion with constant acceleration: position changes as ½at², velocity changes as at, and the two are linked through v² = v₀² + 2aΔx. Free fall is simply the specific case where that constant acceleration is provided by gravity near Earth's surface — **g ≈ 9.8 m/s²** directed downward. Everything you learned about kinematics applies immediately; free fall is kinematics with the acceleration already filled in for you. The conceptual work is understanding *why* g is universal and what it means physically.

Galileo's great insight — the one that overturned two thousand years of Aristotelian physics — is that all objects near Earth's surface fall with the same acceleration regardless of mass. A bowling ball and a tennis ball, dropped from the same height in a vacuum, hit the ground simultaneously. This seems wrong to everyday intuition because we live in air, not vacuum, and air resistance matters far more for light objects. But strip away air and the universality is exact. Why? Because the gravitational force on an object is proportional to its mass (F = mg), but so is its inertia (Newton's second law: a = F/m). The two factors cancel exactly: a = mg/m = g. The mass drops out. Every kilogram of mass is pulled harder by gravity and is proportionally harder to accelerate, and these effects precisely offset. This cancellation is deep — it points toward the equivalence principle at the heart of general relativity.

The trickiest part of free fall problems involves objects thrown upward. Students often think that at the peak — where velocity is momentarily zero — the acceleration is also zero, or that acceleration "switches direction" as the object starts to fall back down. Neither is true. **g acts downward continuously throughout the motion**, whether the object is moving up, is momentarily at rest at the peak, or is moving down. The velocity changes sign (from positive to negative, if you define up as positive), but the acceleration is always −g. At the peak, the object is decelerating at exactly 9.8 m/s² — just like every other moment of the flight. This is why the time to reach the peak equals the time to fall back to the starting point, and why the speed on the way up at any height equals the speed on the way down at that same height.

Use the kinematic equation x = x₀ + v₀t + ½gt² with g = −9.8 m/s² (taking up as positive) as your primary tool. To find time of flight, set x = x₀ and solve for t. To find maximum height, set v = 0 (v = v₀ + gt) and solve for t, then substitute back. These calculations are not new techniques — they are your kinematic tools applied to the universal constant g. Mastering free fall now is essential for projectile motion, where you'll decompose two-dimensional trajectories into a free-fall component (vertical) and a constant-velocity component (horizontal), treating them independently.
