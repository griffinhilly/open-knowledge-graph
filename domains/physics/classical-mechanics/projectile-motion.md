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

## Explainer

The key insight in projectile motion — the one that makes all the calculations tractable — is the **independence of horizontal and vertical motion**. Your prerequisites give you the tools: from **2D kinematics**, you know how to track position and velocity as vectors; from **free fall**, you know that a vertically falling object accelerates at g ≈ 9.8 m/s² downward and that there is no horizontal force. Put these together: a launched projectile has its initial velocity split into two components, and after launch those components evolve completely independently of each other.

Horizontally, there is no force (ignoring air resistance), so there is no horizontal acceleration. Horizontal velocity is constant throughout the flight: v_x = v₀ cos θ, where θ is the launch angle. This is pure uniform motion: x(t) = v₀ cos θ · t. Vertically, only gravity acts, giving constant downward acceleration: v_y(t) = v₀ sin θ − gt, and y(t) = v₀ sin θ · t − ½gt². The horizontal and vertical equations share the variable t — time — and that shared variable is the bridge. To find how far the projectile travels horizontally, you first find how long it is in the air (from the vertical equation, by setting y = 0 for a landing at the same height as launch), then substitute that time into the horizontal equation.

The parabolic trajectory emerges directly from this structure. If you eliminate t between x(t) and y(t), you get y as a quadratic function of x — the equation of a parabola. The **maximum range** on flat ground occurs at a 45° launch angle; at 45°, the horizontal and vertical components of initial velocity are equal, which optimally balances time-in-the-air (set by vertical motion) against horizontal speed. A useful result from **trigonometry**: launch angles symmetric about 45° — say, 30° and 60° — produce identical horizontal range, because the range formula involves sin(2θ), and sin(60°) = sin(120°).

A subtle but important point: the **apex** of the trajectory is the moment when vertical velocity equals zero, not when horizontal velocity is zero — the horizontal velocity never reaches zero in ideal projectile motion. At the apex, v_y = v₀ sin θ − gt_apex = 0, giving t_apex = v₀ sin θ / g. The projectile is still moving forward at the apex with horizontal speed v₀ cos θ; it is simply neither rising nor falling for that instant. The total time of flight for a symmetric trajectory is exactly twice the time to apex. These relationships give you a practical toolkit: most projectile problems reduce to finding time of flight, maximum height, or range from initial conditions, and the decomposition into independent axes is always the first step.
