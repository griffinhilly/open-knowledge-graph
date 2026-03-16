---
id: relativistic-velocity-addition
title: Relativistic Velocity Addition
domain: physics
course: modern-physics
prerequisites:
- id: lorentz-transformation
  type: hard
builds-toward:
- relativistic-momentum-energy
tags:
- relativity
- velocity
- addition
- c-invariance
stage: advanced
status: validated
---

# Relativistic Velocity Addition

## Core Idea
When two velocities are combined in special relativity, the result is not simply u + v but u′ = (u + v)/(1 + uv/c²). This formula ensures that no combination of velocities less than c can ever exceed c, and that adding any velocity to c still yields c. It reduces to the classical u + v when both speeds are small compared to c.

## Common Misconceptions
- If both objects move at 0.9c in opposite directions, a third observer sees them approaching at 1.8c — that is the closing speed in a single frame; neither object moves faster than c in any frame.
- The formula only applies to motion along one axis — for transverse components additional γ factors appear in the full 3D version.

## Explainer

You already know from the Lorentz transformation how coordinates change between inertial frames. The relativistic velocity addition formula is a direct consequence of that algebra. Suppose a spaceship moves at velocity v relative to Earth, and fires a probe at velocity u within its own frame. Classically you'd simply add: u + v. But this fails because the Lorentz transformation mixes space and time — a time interval in one frame contributes to the spatial interval measured in another. When you divide the Lorentz-transformed displacement by the Lorentz-transformed time interval and simplify, the denominator (1 + uv/c²) appears automatically, giving u′ = (u + v)/(1 + uv/c²).

The denominator is the key to understanding why nothing exceeds c. If both u and v are less than c, the denominator is always greater than 1 — it "pulls back" the sum. When u = c (a light beam), the formula gives u′ = (c + v)/(1 + v/c) = c(1 + v/c)/(1 + v/c) = c. Light moves at c in every inertial frame, exactly as the second postulate of special relativity demands. This is not a coincidence or a separate assumption — it falls out of the Lorentz transformation structure you already know.

The **closing speed** misconception deserves careful attention. In a frame where rocket A moves left at 0.9c and rocket B moves right at 0.9c, the distance between them shrinks at 1.8c as measured in that frame — that is a valid calculation of how fast the separation decreases. But this is not the velocity of either object; it is a coordinate rate of change, not the speed of any physical thing. If you ask "how fast does rocket B appear to move in rocket A's rest frame?" that's when the addition formula applies, giving (0.9 + 0.9)/(1 + 0.81) = 1.8/1.81 ≈ 0.994c — still less than c.

At low speeds (u, v ≪ c), the product uv/c² in the denominator is negligible, and the formula reduces to u + v — the familiar Galilean result. Special relativity contains classical mechanics as a limiting case, not a contradiction of it. The relativistic formula is the more fundamental one; Newton's rule works because everyday velocities are so much smaller than c that the correction is unmeasurable. This limiting behavior is a useful sanity check whenever you apply the formula.
