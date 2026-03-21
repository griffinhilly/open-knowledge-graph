---
id: couple-moment
title: Couple and Moment of a Couple
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: moment-of-force-2d
  type: hard
builds-toward:
- equivalent-force-systems
tags:
- statics
- couple
- pure moment
- free vector
stage: formal-systems
status: validated
---

# Couple and Moment of a Couple

## Core Idea
A couple consists of two parallel forces of equal magnitude but opposite direction separated by a perpendicular distance d. The net force of a couple is zero, but it produces a pure moment M = F·d that tends to rotate a body without translating it. Critically, the moment of a couple is a free vector — its rotational effect is identical regardless of where the couple is applied on the rigid body. Couples can be added algebraically in 2D or as vectors in 3D.

## How It's Best Learned
Recognize when a loading condition reduces to a pure couple (zero net force). Practice identifying couples embedded within larger force systems before applying superposition to find the total resultant moment.

## Common Misconceptions
- Thinking the moment of a couple depends on the chosen moment point — it does not.
- Confusing a force-couple system (force plus moment at a point) with a pure couple.
- Forgetting that couples can be freely moved anywhere on the body without changing their mechanical effect.

## Questions

```yaml
- question: "An engineer needs to apply a pure 60 N·m torque to a bolt using a couple — two opposing 30 N forces separated by 2 m. At which location on the structural member should she apply this couple to ensure 60 N·m acts at the bolt?"
  type: multiple-choice
  options:
    - "Directly at the bolt — moments depend on position, so the couple must act there"
    - "Symmetrically about the bolt centerline to cancel any net force"
    - "It does not matter — the couple's moment is a free vector and its effect is identical anywhere on the body"
    - "At least 2 m from the bolt to avoid geometric interference"
  answer: 2
  explanation: "A couple's moment is a free vector — it has magnitude and direction but no fixed point of application. Moving a couple anywhere on a rigid body produces the same rotational effect because all reference-point terms cancel when computing the total moment of two equal and opposite forces. The engineer can place it wherever is mechanically convenient; the 60 N·m torque is transmitted identically to the bolt regardless of placement."

- question: "Two forces act on a rigid bar: 15 N upward at point A and 15 N downward at point B, separated by 4 m. What is the net mechanical effect on the bar?"
  type: multiple-choice
  options:
    - "A net upward force of 30 N with no rotational effect"
    - "No net force and a pure moment of 60 N·m — a couple"
    - "A net force of 15 N downward and a moment of 60 N·m about A"
    - "No effect — equal and opposite forces cancel completely"
  answer: 1
  explanation: "Equal-magnitude, opposite-direction, parallel forces form a couple. The net force is 15 − 15 = 0 (no translation). The moment is M = F × d = 15 × 4 = 60 N·m (pure rotation). Option D is wrong because the forces are offset — even with zero net force, the separation creates a moment. Option C is wrong because the forces are equal and opposite, giving zero net force."

- question: "The moment produced by a couple about point A differs from the moment computed about a different point B elsewhere on the same rigid body."
  type: true-false
  answer: false
  explanation: "This is the defining property of a couple. When computing the total moment of two forces F and −F at positions r₁ and r₂, the result is (r₁ − r₂) × F = d × F. The position vectors r₁ and r₂ both shift equally when the reference point changes, so their difference (r₁ − r₂) remains constant. The moment center cancels completely, giving M = F·d regardless of reference point — the same value about every point."

- question: "A couple may be relocated to any point on a rigid body without changing the body's mechanical response."
  type: true-false
  answer: true
  explanation: "Because a couple's moment is a free vector — independent of position — it can be placed anywhere on (or off) the rigid body without altering its rotational effect. This distinguishes couples from forces, which are sliding vectors that may only move along their line of action. The freedom of the couple vector is why, when simplifying complex force systems, any couple moment can be relocated to the most convenient reference point."

- question: "Why does a single force's moment change when the reference point is moved, but a couple's moment remains the same regardless of reference point?"
  type: short-answer
  answer: "A single force F at position r₁ produces moment r₁ × F about the origin. Move the reference to point P: the moment becomes (r₁ − P) × F, which depends on P. A couple has forces F and −F at positions r₁ and r₂. Total moment about P: (r₁ − P) × F + (r₂ − P) × (−F) = (r₁ − r₂) × F. The P terms cancel algebraically, leaving only the relative displacement between the two forces. The reference point has no effect on the result."
  explanation: "This algebraic cancellation is why the couple's moment is called a free vector — it genuinely has no preferred point of application. A single force's moment is bound to a specific line of action; the couple's moment floats freely in space while retaining its full mechanical meaning. This makes couples especially useful in equivalent force system analysis: the couple moment can slide to any convenient location during simplification."
```

## Explainer

You already know how to compute the moment of a single force about a point: M = r × F, where r is the position vector from the moment center to the force. Notice that this moment depends on *which point you choose* — move the moment center, and r changes, so M changes. This is the normal behavior of a force. A **couple** is special precisely because it escapes this dependence entirely.

A couple consists of two forces: equal in magnitude, parallel, opposite in direction, and separated by a perpendicular distance d. Think of turning a steering wheel with both hands, or twisting a jar lid — two forces, no net push in any direction. The net force is zero (they cancel), so the couple cannot translate the body. But the forces are offset, so they do create rotation. Computing the total moment about *any* point P reveals something remarkable: all the terms involving P's position cancel out. What remains is M = F·d regardless of where P is. The couple's moment is the same no matter what reference point you use.

This is what makes the couple's moment a **free vector**: it has a magnitude and direction, but no fixed point of application. You can move it anywhere on — or off — the rigid body and its mechanical effect is unchanged. This is in sharp contrast to a force, which is a **sliding vector** (it can slide along its line of action but not move off it) or a force-moment pair at a specific point. The freedom of the couple vector is what makes it so useful in analyzing equivalent force systems: when you replace a distributed loading by its resultant, the result is typically a single force plus a free couple moment at any convenient point.

In 2D, couples add algebraically: counterclockwise is positive. In 3D, they add as vectors with direction given by the right-hand rule. When you encounter a loading configuration with zero net force but nonzero net moment, you are looking at a pure couple — recognizing this immediately simplifies the analysis of any problem involving wrench loads, torsion, or gear pairs.
