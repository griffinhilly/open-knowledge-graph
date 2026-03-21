---
id: projectile-motion
title: Projectile Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematics-2d
  type: hard
- id: free-fall
  type: hard
- id: vectors-in-two-dimensions
  type: soft
- id: parametric-equations-intro
  type: soft
- id: trigonometric-ratios-review
  type: soft
builds-toward:
- circular-motion-kinematics
tags:
- projectile
- parabolic-trajectory
- kinematics
- 2d
stage: formal-systems
status: validated
---

# Projectile Motion

## Core Idea
A projectile is any object launched with an initial velocity and subject only to gravitational acceleration. Horizontal velocity is constant (no horizontal force), while vertical motion is free fall. The resulting trajectory is a parabola. Range, maximum height, and time of flight are all determined by the initial speed and launch angle.

## How It's Best Learned
Solve problems at multiple launch angles (30°, 45°, 60°) and verify that 45° gives maximum range on flat ground. Use simulation tools to visualize trajectories and check against calculations.

## Common Misconceptions
- Thinking horizontal velocity changes during flight — it only changes if there is horizontal force (like drag).
- Using total velocity magnitude instead of just the vertical component when computing time to peak.
- Assuming that maximum range always occurs at 45° — this changes if launch and landing heights differ.

## Questions

```yaml
- question: "A ball is launched at 30 m/s at a 40° angle. At the highest point of its trajectory, what is true about its velocity?"
  type: multiple-choice
  options:
    - "Velocity is zero — the ball momentarily stops before falling"
    - "Velocity equals 30 m/s in the horizontal direction"
    - "Velocity equals 30 cos(40°) horizontally and is nonzero"
    - "Only the vertical component remains; horizontal velocity has been lost to gravity"
  answer: 2
  explanation: "At the apex, vertical velocity is zero (the ball is neither rising nor falling), but horizontal velocity is unchanged throughout the flight — there is no horizontal force to alter it. The horizontal component remains v₀cos(40°) for the entire flight. Option A is a very common misconception: students often assume the ball 'stops' at the top. Option D reverses the physics — gravity only acts vertically, so only the vertical component is reduced."

- question: "A golfer hits two balls with identical speed: one at 30°, one at 60°. Ignoring air resistance and assuming flat ground, how do their horizontal ranges compare?"
  type: multiple-choice
  options:
    - "The 60° shot travels farther because it stays in the air longer"
    - "The 30° shot travels farther because it has more horizontal velocity"
    - "They travel the same horizontal distance"
    - "The 45° shot would travel farther than either, but we cannot compare these two without calculating"
  answer: 2
  explanation: "Launch angles symmetric about 45° produce identical range on flat ground. This follows from the range formula R = (v₀² sin 2θ)/g: sin(2×30°) = sin(60°) = sin(120°) = sin(2×60°). Options A and B identify real trade-offs — the 60° shot stays up longer, the 30° shot has higher horizontal speed — but these effects exactly cancel. This symmetry is a beautiful result from the sin(2θ) structure of the range formula."

- question: "At the highest point of its trajectory, a projectile has zero velocity."
  type: true-false
  answer: false
  explanation: "Only the vertical component of velocity is zero at the apex — the projectile has stopped rising and hasn't yet begun to fall. The horizontal component, unchanged throughout the flight (no horizontal force acts), remains v₀cosθ. The total velocity at the apex is v₀cosθ, directed purely horizontally. This is the most common single misconception in projectile motion: confusing 'vertical velocity = 0' with 'total velocity = 0.'"

- question: "A projectile launched at 30° and one launched at 60° from the same point with the same initial speed land at the same horizontal distance on flat ground."
  type: true-false
  answer: true
  explanation: "The horizontal range formula R = v₀²sin(2θ)/g shows that complementary angles (adding to 90°) give the same sin(2θ) value: sin(60°) = sin(120°). The 30° shot has more horizontal speed but less time aloft; the 60° shot has less horizontal speed but more time aloft. These effects precisely cancel, yielding equal range."

- question: "Explain why time of flight for a projectile is determined entirely by the vertical component of motion, not by the horizontal speed."
  type: short-answer
  answer: "Gravity acts only vertically, so only the vertical motion controls when the projectile hits the ground. The projectile lands when its vertical position returns to zero, which occurs at a time determined by solving y(t) = v₀sinθ·t − ½gt² = 0. The horizontal speed v₀cosθ determines how far the projectile travels during that time, but has no influence on how long it is in the air. This is the independence of horizontal and vertical motion: they share time as a variable, but neither axis's physics depends on the other."
  explanation: "Students sometimes think a faster horizontal speed 'carries' the projectile further and keeps it in the air longer — but horizontal motion has no vertical component and cannot affect vertical acceleration. The time in the air is a vertical problem only; range is then horizontal speed multiplied by that pre-determined flight time."
```

## Explainer

The key insight in projectile motion — the one that makes all the calculations tractable — is the **independence of horizontal and vertical motion**. Your prerequisites give you the tools: from **2D kinematics**, you know how to track position and velocity as vectors; from **free fall**, you know that a vertically falling object accelerates at g ≈ 9.8 m/s² downward and that there is no horizontal force. Put these together: a launched projectile has its initial velocity split into two components, and after launch those components evolve completely independently of each other.

Horizontally, there is no force (ignoring air resistance), so there is no horizontal acceleration. Horizontal velocity is constant throughout the flight: v_x = v₀ cos θ, where θ is the launch angle. This is pure uniform motion: x(t) = v₀ cos θ · t. Vertically, only gravity acts, giving constant downward acceleration: v_y(t) = v₀ sin θ − gt, and y(t) = v₀ sin θ · t − ½gt². The horizontal and vertical equations share the variable t — time — and that shared variable is the bridge. To find how far the projectile travels horizontally, you first find how long it is in the air (from the vertical equation, by setting y = 0 for a landing at the same height as launch), then substitute that time into the horizontal equation.

The parabolic trajectory emerges directly from this structure. If you eliminate t between x(t) and y(t), you get y as a quadratic function of x — the equation of a parabola. The **maximum range** on flat ground occurs at a 45° launch angle; at 45°, the horizontal and vertical components of initial velocity are equal, which optimally balances time-in-the-air (set by vertical motion) against horizontal speed. A useful result from **trigonometry**: launch angles symmetric about 45° — say, 30° and 60° — produce identical horizontal range, because the range formula involves sin(2θ), and sin(60°) = sin(120°).

A subtle but important point: the **apex** of the trajectory is the moment when vertical velocity equals zero, not when horizontal velocity is zero — the horizontal velocity never reaches zero in ideal projectile motion. At the apex, v_y = v₀ sin θ − gt_apex = 0, giving t_apex = v₀ sin θ / g. The projectile is still moving forward at the apex with horizontal speed v₀ cos θ; it is simply neither rising nor falling for that instant. The total time of flight for a symmetric trajectory is exactly twice the time to apex. These relationships give you a practical toolkit: most projectile problems reduce to finding time of flight, maximum height, or range from initial conditions, and the decomposition into independent axes is always the first step.
