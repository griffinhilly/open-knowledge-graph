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
- id: friction-in-mechanical-devices
  type: soft
- id: belt-and-rope-friction
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
status: validated
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

## Questions

```yaml
- question: "A power screw has a lead angle of 6° and a friction angle of 8°. A heavy load is placed on the screw with no torque applied to the screw shaft. What happens?"
  type: multiple-choice
  options:
    - "The load back-drives the screw downward because the incline exceeds the friction capacity"
    - "The load remains stationary — the screw is self-locking because the lead angle (6°) is less than the friction angle (8°)"
    - "The screw is at the self-locking threshold, so small vibrations will cause it to slip"
    - "The efficiency is above 50%, so the screw cannot be self-locking"
  answer: 1
  explanation: "The self-locking condition is λ < φ_s. Here 6° < 8°, so the screw is self-locking. In the inclined-plane analogy, the thread slope is shallower than the friction angle — friction is strong enough to prevent the load from sliding the screw backward. Applying the lowering torque formula M = Wr·tan(λ − φ_s) = Wr·tan(−2°) gives a negative value, meaning you would need to apply torque in the raising direction to make the load descend. Without that torque, the load holds."

- question: "An engineer designing a lifting jack selects a screw with a very small lead angle, reasoning that smaller lead angles improve mechanical efficiency. What error has she made?"
  type: multiple-choice
  options:
    - "A small lead angle requires a larger friction coefficient to function, which is difficult to achieve"
    - "A small lead angle means λ << φ_s, placing the screw deeply in the self-locking regime where efficiency is well below 50% — if high efficiency is the goal, a larger lead angle is needed (at the cost of requiring a separate brake to prevent back-driving)"
    - "Lead angle does not affect efficiency — only the friction coefficient determines how much torque is wasted"
    - "A small lead angle causes problems only during lowering, not during raising"
  answer: 1
  explanation: "Efficiency η = tan(λ) / tan(λ + φ_s), and for a self-locking screw (λ < φ_s) this is always below 50%. As λ decreases, efficiency drops further — the screw becomes safer against back-driving but wastes more input torque as heat. The efficiency bound of 50% is not coincidental: it is a mathematical consequence of self-locking. So the engineer faces a real tradeoff: safety (self-locking) vs. efficiency. A lifting application like a car jack accepts low efficiency; a precision positioning stage would choose a high-lead-angle ballscrew and a separate brake."

- question: "A self-locking power screw always has a mechanical efficiency below 50%."
  type: true-false
  answer: true
  explanation: "This follows directly from the efficiency formula η = tan(λ) / tan(λ + φ_s). For a self-locking screw, λ < φ_s, which means λ + φ_s > 2λ. Using the tangent addition formula and the fact that tan is monotone, η = tan(λ)/tan(λ + φ_s) < tan(λ)/tan(2λ) = 1/2 when λ < φ_s. Intuitively: the same friction force that prevents back-driving (self-locking) also resists the applied torque during raising, dissipating more than half the input energy as heat. This 50% bound is a fundamental law of screw mechanics, not a design deficiency."

- question: "A screw with a lead angle of 30° and a friction angle of 15° is self-locking because the large lead angle provides greater mechanical advantage against the load."
  type: true-false
  answer: false
  explanation: "The self-locking condition is λ < φ_s — lead angle must be LESS than friction angle. Here λ = 30° > φ_s = 15°, so the screw is overhauling (back-drivable). The load CAN drive the screw backward without any applied torque. Mechanical advantage from a large lead angle works in the opposite direction: a large lead angle advances the load more per revolution (good for speed) but reduces the friction-to-slope ratio, making back-driving easier. Self-locking requires a shallow thread helix (small λ) so friction dominates the incline geometry."

- question: "Explain why the self-locking condition requires the lead angle to be less than the friction angle, using the inclined-plane analogy."
  type: short-answer
  answer: "Unwrapping the screw thread produces an inclined plane with slope angle λ (the lead angle), with the load W as a block on the incline. The block will hold without applied force only if friction is strong enough to resist gravity along the slope. The critical condition is when the friction force exactly equals the gravitational component along the plane, which occurs at the friction angle φ_s = arctan(μ_s). For inclinations shallower than φ_s (λ < φ_s), friction wins — the block holds and the screw is self-locking. For inclinations steeper than φ_s (λ > φ_s), the gravitational component wins — the block slides and the screw is overhauling. The lowering torque formula M = Wr·tan(λ − φ_s) encodes this directly: when λ < φ_s the torque is negative, meaning the load cannot descend without external assistance."
  explanation: "The inclined-plane analogy is the conceptual key to all screw analysis. It transforms a seemingly complex 3D helical problem into a familiar 2D statics problem. Once you see the screw as a wrapped inclined plane, the raising formula (load must push up against both gravity and friction), the lowering formula (friction now partially aids descent), and the self-locking condition (friction exceeds the slope component) all follow naturally from force balance on the block."
```

## Explainer

You already know from wedge analysis that a sloped surface under friction can transmit force in one direction but resist it in the other — the friction angle φ_s = arctan(μ_s) is the boundary between "slides" and "holds." A power screw is precisely a wedge wrapped helically around a cylinder. **Unwrapping** the thread helix onto a flat plane produces an inclined plane of angle λ (the **lead angle**), with a block (the load W) riding on it under friction. All of the torque and self-locking analysis follows directly from this mental model.

The **lead angle** λ = arctan(lead / 2πr) relates the axial advance per revolution to the circumference at the mean thread radius. A fine-pitch screw has a shallow lead angle; a coarse or multi-start screw has a steep one. When torque is applied to advance the load (raising mode), the applied force must push the block up the inclined plane against both gravity and friction, giving M_raise = Wr tan(λ + φ_s). When torque is applied to retract (lowering mode), the formula becomes M_lower = Wr tan(λ − φ_s) — friction now acts partially in the direction of motion, aiding the descent.

The **self-locking condition** λ < φ_s follows immediately from the lowering formula. If λ < φ_s, then (λ − φ_s) < 0, which means the calculated lowering torque is negative — you would need to apply torque in the raising direction to make the load descend. In the absence of that torque, the load stays put: the screw is self-locking. Physically, friction is strong enough relative to the thread slope that the load cannot drive the screw backward. If λ > φ_s (called **overhauling**), the positive lowering torque means the load would back-drive the screw unless a brake holds it.

A useful consequence is the **efficiency bound**: the efficiency η = tan(λ) / tan(λ + φ_s) is always below 50% for a self-locking screw. This is not a design flaw — it is the price of self-locking. The same friction that makes the jack hold a car safely in the air is the friction that wastes more than half the input torque as heat. In applications like a clamp or vise, 50% efficiency is acceptable; in a ballscrew positioning stage where efficiency and backdrivability are both needed, engineers deliberately choose λ > φ_s and add a separate brake. Understanding the trade-off lets you select or reject self-locking as a feature, rather than stumbling into it accidentally.
