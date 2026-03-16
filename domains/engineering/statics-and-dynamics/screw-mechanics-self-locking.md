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

## Explainer

You already know from wedge analysis that a sloped surface under friction can transmit force in one direction but resist it in the other — the friction angle φ_s = arctan(μ_s) is the boundary between "slides" and "holds." A power screw is precisely a wedge wrapped helically around a cylinder. **Unwrapping** the thread helix onto a flat plane produces an inclined plane of angle λ (the **lead angle**), with a block (the load W) riding on it under friction. All of the torque and self-locking analysis follows directly from this mental model.

The **lead angle** λ = arctan(lead / 2πr) relates the axial advance per revolution to the circumference at the mean thread radius. A fine-pitch screw has a shallow lead angle; a coarse or multi-start screw has a steep one. When torque is applied to advance the load (raising mode), the applied force must push the block up the inclined plane against both gravity and friction, giving M_raise = Wr tan(λ + φ_s). When torque is applied to retract (lowering mode), the formula becomes M_lower = Wr tan(λ − φ_s) — friction now acts partially in the direction of motion, aiding the descent.

The **self-locking condition** λ < φ_s follows immediately from the lowering formula. If λ < φ_s, then (λ − φ_s) < 0, which means the calculated lowering torque is negative — you would need to apply torque in the raising direction to make the load descend. In the absence of that torque, the load stays put: the screw is self-locking. Physically, friction is strong enough relative to the thread slope that the load cannot drive the screw backward. If λ > φ_s (called **overhauling**), the positive lowering torque means the load would back-drive the screw unless a brake holds it.

A useful consequence is the **efficiency bound**: the efficiency η = tan(λ) / tan(λ + φ_s) is always below 50% for a self-locking screw. This is not a design flaw — it is the price of self-locking. The same friction that makes the jack hold a car safely in the air is the friction that wastes more than half the input torque as heat. In applications like a clamp or vise, 50% efficiency is acceptable; in a ballscrew positioning stage where efficiency and backdrivability are both needed, engineers deliberately choose λ > φ_s and add a separate brake. Understanding the trade-off lets you select or reject self-locking as a feature, rather than stumbling into it accidentally.
