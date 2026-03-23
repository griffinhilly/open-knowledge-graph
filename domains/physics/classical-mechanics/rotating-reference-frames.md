---
id: rotating-reference-frames
title: Rotating Reference Frames
domain: physics
course: classical-mechanics
prerequisites:
- id: non-inertial-frames-and-pseudo-forces
  type: hard
builds-toward:
- coriolis-effect
tags:
- reference-frames
- rotation
- pseudo-forces
- centrifugal
stage: formal-systems
status: validated
---

# Rotating Reference Frames

## Core Idea
In a reference frame rotating with angular velocity ω, two pseudo-forces appear: the centrifugal force F_cf = m ω² r (pointing outward) and the Coriolis force F_cor = −2 m ω × v (perpendicular to velocity). The centrifugal force vanishes in the inertial frame (it accounts for centripetal acceleration in the rotating frame); the Coriolis force deflects moving objects perpendicular to their velocity.

## Questions

```yaml
- question: "An observer in an inertial frame watches a ball roll across a rotating merry-go-round. From the inertial observer's perspective, what does the ball's path look like?"
  type: multiple-choice
  options:
    - "Curved to the right, because the Coriolis force deflects it"
    - "A straight line, because no real horizontal forces act on the ball"
    - "Curved inward toward the center due to centripetal force"
    - "Spiraling outward due to the centrifugal force"
  answer: 1
  explanation: "From the inertial frame, Newton's first law applies: the ball moves in a straight line because no real horizontal force acts on it (ignoring friction). The Coriolis and centrifugal forces are pseudo-forces — they exist only in the rotating frame's equations of motion. An observer standing above the merry-go-round would see a straight-line trajectory. An observer *on* the merry-go-round would see a curved path and would need to introduce the Coriolis force to explain it within their (non-inertial) reference frame."

- question: "A stationary object rests on a rotating platform. In the rotating frame, the object appears to experience an outward push. What pseudo-force accounts for this, and why does it appear?"
  type: multiple-choice
  options:
    - "The Coriolis force, because the object is moving relative to the inertial frame"
    - "The centrifugal force, because the rotating frame continuously accelerates the object inward, requiring a compensating outward pseudo-force"
    - "The centripetal force, which acts outward in rotating frames"
    - "No pseudo-force is needed; the object is genuinely accelerating outward"
  answer: 1
  explanation: "In the inertial frame, keeping an object on a circular path requires centripetal force directed inward. In the rotating frame, the object is stationary — so by Newton's second law as applied in that frame, the net force must be zero. The centripetal force still acts inward, so to balance it, we introduce the centrifugal pseudo-force F_cf = mω²r directed outward. The centrifugal force is not real — it appears only because the frame is rotating. The Coriolis force (option A) acts only on objects that are *moving* within the rotating frame; a stationary object experiences no Coriolis force."

- question: "The Coriolis force is zero for an object that is stationary within the rotating frame."
  type: true-false
  answer: true
  explanation: "The Coriolis force is F_cor = −2m(ω × v), where v is the velocity of the object as measured in the rotating frame. If the object is stationary in the rotating frame, v = 0, so F_cor = 0. Only objects that are moving within the rotating frame experience a Coriolis deflection. This is why the Coriolis effect is important for large-scale atmospheric motion (where air masses move over great distances) but negligible for everyday objects at rest on Earth's surface."

- question: "The centrifugal force felt by a person on a spinning carousel is a real force that acts on them in both the rotating frame and the inertial frame."
  type: true-false
  answer: false
  explanation: "The centrifugal force is a pseudo-force — it exists only in the rotating (non-inertial) frame. In the inertial frame, there is no centrifugal force. What exists in the inertial frame is the centripetal force (e.g., friction or the normal force from the carousel seat) directed inward, which keeps the person on their circular path. In the rotating frame, this same centripetal force points inward and is 'balanced' by the outward centrifugal pseudo-force. The person feels pushed outward because the seat is pushing them inward."

- question: "Why are pseudo-forces like the centrifugal and Coriolis forces introduced when analyzing motion in a rotating frame? What problem do they solve?"
  type: short-answer
  answer: "Newton's second law F = ma holds only in inertial (non-accelerating) frames. In a rotating frame, objects appear to accelerate or curve even when no real force acts on them — because the frame itself is continuously changing direction. If you try to apply F = ma in a rotating frame using only real forces, the equations are wrong: they predict zero acceleration for objects that appear to be moving (from the rotating frame's perspective). Pseudo-forces are mathematical correction terms added to make Newton's second law hold formally in the rotating frame. The centrifugal force corrects for the frame's rotational acceleration on stationary objects; the Coriolis force corrects for the additional deflection experienced by moving objects."
  explanation: "The key insight is that pseudo-forces are bookkeeping devices, not physical forces — they have no source and don't appear in free-body diagrams drawn from inertial frames. Their value is purely computational: they let engineers and scientists use familiar Newtonian analysis in non-inertial frames like Earth's surface without constantly transforming to the inertial frame."
```

## Explainer

From your prerequisite on non-inertial frames and pseudo-forces, you know the fundamental idea: Newton's second law *F = ma* holds only in **inertial frames** — frames that are not accelerating relative to the fixed stars. When you work in an accelerating frame, you introduce **pseudo-forces** (fictitious forces) that have no physical source but account for the acceleration of the frame itself. In a car braking hard, you feel "thrown forward" — that's the pseudo-force that appears in the car's non-inertial (decelerating) frame. Rotating frames are a special case: instead of a one-time linear acceleration, the frame is continuously changing direction.

Consider why rotation counts as acceleration at all: **centripetal acceleration** is required to keep any object moving in a circle (it points inward, toward the axis). From the rotating frame, an object that is stationary in the inertial frame appears to be spiraling outward — and to explain this within the rotating frame, you must introduce a pseudo-force pushing it outward. This is the **centrifugal force**: F_cf = mω²r, directed radially outward from the axis of rotation. In the inertial frame, there is no centrifugal force — what exists is centripetal force directed inward, keeping the object on its circular path. In the rotating frame, these cancel: centripetal force pushes in, centrifugal force pushes out, and the object appears stationary.

The second pseudo-force is the **Coriolis force**: F_cor = −2m(ω × v). It appears only when an object is moving within the rotating frame — it is proportional to the object's velocity (as measured in the rotating frame) and directed perpendicular to that velocity. The cross product ω × v gives the direction: always at right angles to both the rotation axis and the object's velocity. The key intuition is this: when an object moves outward in a rotating frame, it is actually moving in a straight line in the inertial frame, but the frame is rotating under it — so from inside the frame, the path appears to curve. The Coriolis force is the pseudo-force that accounts for this apparent curvature.

To build intuition, imagine you are on a rotating merry-go-round and try to roll a ball straight across to a friend on the other side. From above (the inertial frame), the ball travels in a straight line. But from the merry-go-round frame, the ball appears to curve sideways — deflected by the Coriolis force. On Earth, the same effect operates at planetary scale: large air masses moving poleward in the Northern Hemisphere are deflected to the right (from their perspective), generating the counterclockwise rotation of low-pressure weather systems. Earth's rotation is slow (ω ≈ 7.3 × 10⁻⁵ rad/s), so Coriolis effects are negligible for small-scale motion in a kitchen but enormous for hurricanes and ocean currents — phenomena that unfold over thousands of kilometers and days.
