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

## Explainer

From your study of kinematic equations, you know how to describe motion with constant acceleration: position changes as ½at², velocity changes as at, and the two are linked through v² = v₀² + 2aΔx. Free fall is simply the specific case where that constant acceleration is provided by gravity near Earth's surface — **g ≈ 9.8 m/s²** directed downward. Everything you learned about kinematics applies immediately; free fall is kinematics with the acceleration already filled in for you. The conceptual work is understanding *why* g is universal and what it means physically.

Galileo's great insight — the one that overturned two thousand years of Aristotelian physics — is that all objects near Earth's surface fall with the same acceleration regardless of mass. A bowling ball and a tennis ball, dropped from the same height in a vacuum, hit the ground simultaneously. This seems wrong to everyday intuition because we live in air, not vacuum, and air resistance matters far more for light objects. But strip away air and the universality is exact. Why? Because the gravitational force on an object is proportional to its mass (F = mg), but so is its inertia (Newton's second law: a = F/m). The two factors cancel exactly: a = mg/m = g. The mass drops out. Every kilogram of mass is pulled harder by gravity and is proportionally harder to accelerate, and these effects precisely offset. This cancellation is deep — it points toward the equivalence principle at the heart of general relativity.

The trickiest part of free fall problems involves objects thrown upward. Students often think that at the peak — where velocity is momentarily zero — the acceleration is also zero, or that acceleration "switches direction" as the object starts to fall back down. Neither is true. **g acts downward continuously throughout the motion**, whether the object is moving up, is momentarily at rest at the peak, or is moving down. The velocity changes sign (from positive to negative, if you define up as positive), but the acceleration is always −g. At the peak, the object is decelerating at exactly 9.8 m/s² — just like every other moment of the flight. This is why the time to reach the peak equals the time to fall back to the starting point, and why the speed on the way up at any height equals the speed on the way down at that same height.

Use the kinematic equation x = x₀ + v₀t + ½gt² with g = −9.8 m/s² (taking up as positive) as your primary tool. To find time of flight, set x = x₀ and solve for t. To find maximum height, set v = 0 (v = v₀ + gt) and solve for t, then substitute back. These calculations are not new techniques — they are your kinematic tools applied to the universal constant g. Mastering free fall now is essential for projectile motion, where you'll decompose two-dimensional trajectories into a free-fall component (vertical) and a constant-velocity component (horizontal), treating them independently.
