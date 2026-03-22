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

## Questions

```yaml
- question: "Rocket A moves at 0.9c to the left and rocket B moves at 0.9c to the right, as measured from Earth. How fast does an observer in rocket A measure rocket B to be moving?"
  type: multiple-choice
  options:
    - "1.8c — the velocities add directly since we are combining speeds in a single calculation"
    - "0.9c — velocities cannot add at all in special relativity"
    - "Approximately 0.994c — the relativistic addition formula applies and the denominator pulls the result below c"
    - "Exactly c — any two velocities near c combine to exactly c"
  answer: 2
  explanation: "The Galilean sum 0.9c + 0.9c = 1.8c describes only the rate at which the separation between the rockets grows as measured from Earth — a valid coordinate quantity in that frame, but not a velocity of either rocket. To find rocket B's speed in rocket A's rest frame, apply the relativistic formula: (0.9 + 0.9)/(1 + 0.9×0.9) = 1.8/1.81 ≈ 0.994c. The denominator (1 + uv/c²) is what pulls the result back below c. This is not a coincidence — it is built into the Lorentz transformation structure."

- question: "A spaceship traveling at 0.8c relative to Earth fires a laser beam forward. What speed does Earth measure the laser beam traveling?"
  type: multiple-choice
  options:
    - "1.8c — the ship's speed adds directly to the speed of light"
    - "c — the speed of light is invariant in all inertial frames, and the formula confirms this"
    - "0.2c — the beam's speed is reduced because the ship is moving toward the beam"
    - "Slightly greater than c, but unmeasurable with current instruments"
  answer: 1
  explanation: "Apply the formula with u = c (speed of light in the ship's frame) and v = 0.8c (ship's speed): u′ = (c + 0.8c)/(1 + 0.8c·c/c²) = 1.8c/1.8 = c. The result is exactly c. This is not an independent postulate bolted onto the formula — it falls out naturally from the Lorentz transformation algebra. The denominator (1 + uv/c²) cancels the numerator's excess in exactly the right way whenever u = c."

- question: "The rate at which the separation between two rockets increases, as measured by a stationary observer, can exceed c even though neither rocket moves faster than c."
  type: true-false
  answer: true
  explanation: "In a single inertial frame, the rate of change of separation between two objects is a coordinate quantity, not the speed of any physical thing. If rocket A moves left at 0.9c and rocket B moves right at 0.9c as measured from Earth, Earth observes their separation growing at 1.8c per unit time. No object is moving at 1.8c — this is just arithmetic on two separate velocities in the same frame. Special relativity restricts the speed of a physical object in any inertial frame to less than c; it does not restrict coordinate separation rates, which is why closing speed and relative velocity must be carefully distinguished."

- question: "If object A moves at 0.6c relative to Earth and object B moves at 0.8c in the same direction relative to Earth, then object B moves at 0.2c relative to object A."
  type: true-false
  answer: false
  explanation: "The naive subtraction 0.8c − 0.6c = 0.2c is the Galilean result. Applying the relativistic formula: (0.8c − 0.6c)/(1 − 0.6×0.8) = 0.2c/(1 − 0.48) = 0.2c/0.52 ≈ 0.385c. The relativistic result is nearly twice the Galilean estimate here, illustrating that the correction is non-trivial even at moderate speeds. The denominator (1 − uv/c²) < 1 when both objects move in the same direction, which amplifies the relative velocity above the naive difference — though still keeping it below c."

- question: "Why does applying the relativistic velocity addition formula with u = c always yield c, regardless of the value of v?"
  type: short-answer
  answer: "Substituting u = c into the formula gives (c + v)/(1 + vc/c²) = (c + v)/(1 + v/c) = c(1 + v/c)/(1 + v/c) = c. The factor (1 + v/c) appears identically in both numerator and denominator and cancels exactly. This is not a coincidence — the Lorentz transformation from which the formula is derived was constructed precisely to preserve the invariance of c. The cancellation is a mathematical expression of the second postulate of special relativity: light has the same speed c in every inertial frame."
  explanation: "This result shows that the relativistic addition formula does not just approximate c-invariance or treat it as a boundary condition — it builds c-invariance into its algebraic structure. The formula reduces to Galilean addition at low speeds (when uv/c² ≪ 1) and enforces c-invariance at the extreme (when u = c). It is consistent both with everyday experience and with the foundational postulate of special relativity."
```

## Explainer

You already know from the Lorentz transformation how coordinates change between inertial frames. The relativistic velocity addition formula is a direct consequence of that algebra. Suppose a spaceship moves at velocity v relative to Earth, and fires a probe at velocity u within its own frame. Classically you'd simply add: u + v. But this fails because the Lorentz transformation mixes space and time — a time interval in one frame contributes to the spatial interval measured in another. When you divide the Lorentz-transformed displacement by the Lorentz-transformed time interval and simplify, the denominator (1 + uv/c²) appears automatically, giving u′ = (u + v)/(1 + uv/c²).

The denominator is the key to understanding why nothing exceeds c. If both u and v are less than c, the denominator is always greater than 1 — it "pulls back" the sum. When u = c (a light beam), the formula gives u′ = (c + v)/(1 + v/c) = c(1 + v/c)/(1 + v/c) = c. Light moves at c in every inertial frame, exactly as the second postulate of special relativity demands. This is not a coincidence or a separate assumption — it falls out of the Lorentz transformation structure you already know.

The **closing speed** misconception deserves careful attention. In a frame where rocket A moves left at 0.9c and rocket B moves right at 0.9c, the distance between them shrinks at 1.8c as measured in that frame — that is a valid calculation of how fast the separation decreases. But this is not the velocity of either object; it is a coordinate rate of change, not the speed of any physical thing. If you ask "how fast does rocket B appear to move in rocket A's rest frame?" that's when the addition formula applies, giving (0.9 + 0.9)/(1 + 0.81) = 1.8/1.81 ≈ 0.994c — still less than c.

At low speeds (u, v ≪ c), the product uv/c² in the denominator is negligible, and the formula reduces to u + v — the familiar Galilean result. Special relativity contains classical mechanics as a limiting case, not a contradiction of it. The relativistic formula is the more fundamental one; Newton's rule works because everyday velocities are so much smaller than c that the correction is unmeasurable. This limiting behavior is a useful sanity check whenever you apply the formula.
