---
id: screw-mechanics-self-locking
title: Screw Mechanics and Self-Locking
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: friction-wedges-screws-belts
  type: hard
- id: dry-friction-coulombs-law
  type: soft
builds-toward:
- multiforce-member-analysis
tags:
- statics
- friction
- screws
- power screws
- self-locking
stage: formal-systems
status: draft
---

# Screw Mechanics and Self-Locking

## Core Idea
A power screw converts rotational torque into linear force (or vice versa) by exploiting the inclined-plane geometry of its threads. The lead angle (lambda) is the helix angle of the thread, and the relationship between the applied torque M and the axial load W is M = Wr tan(lambda +/- phi_s) for raising/lowering, where phi_s = arctan(mu_s) is the friction angle. A screw is self-locking when the lead angle is less than the friction angle (lambda < phi_s), meaning the load cannot back-drive the screw without an externally applied torque. Self-locking is essential in applications like clamps, jacks, and vises where the load must remain stationary once positioned. Efficiency of a power screw is eta = tan(lambda) / tan(lambda + phi_s), and self-locking screws always have efficiency below 50%.

## How It's Best Learned
Model the screw thread as an unwrapped inclined plane with a block sliding under friction. Derive the raising and lowering torque equations from this equivalent model, then verify the self-locking condition by checking whether the lowering torque is positive (self-locking) or negative (overhauling). Work numerical examples with different lead angles and friction coefficients to build intuition for the transition between self-locking and overhauling regimes.

## Common Misconceptions
- Confusing lead (axial advance per revolution) with pitch (axial distance between adjacent threads) — they differ for multi-start screws.
- Assuming all screws are self-locking without verifying that lambda < phi_s for the given friction coefficient.
- Forgetting to distinguish between the raising and lowering torque formulas, which use (lambda + phi_s) and (lambda - phi_s) respectively.
