---
id: newtons-first-law
title: 'Newton''s First Law: The Law of Inertia'
domain: physics
course: classical-mechanics
prerequisites:
- id: kinematics-1d
  type: soft
builds-toward:
- newtons-second-law
- free-body-diagrams
tags:
- newtons-laws
- inertia
- force
- equilibrium
stage: formal-systems
status: validated
---

# Newton's First Law: The Law of Inertia

## Core Idea
An object at rest stays at rest, and an object in uniform motion stays in uniform motion, unless acted upon by a net external force. This defines inertia — the tendency of matter to resist changes in its state of motion. It also defines what an inertial reference frame is: one in which Newton's laws hold, i.e., a frame that is not itself accelerating.

## How It's Best Learned
Think carefully about what 'net force' means — objects in constant velocity have zero net force, not zero force. Everyday examples like a book on a table or a hockey puck sliding on ice make the concept tangible.

## Common Misconceptions
- Believing a moving object requires a continuous force to keep moving (Aristotelian intuition that force causes motion, not acceleration).
- Thinking that 'no motion' implies 'no force' — a stationary object can have many forces that cancel out.

## Questions

```yaml
- question: "A hockey puck slides across nearly frictionless ice at constant velocity. What is the net force on it?"
  type: multiple-choice
  options:
    - "A net force in the direction of motion, maintaining its velocity"
    - "Zero net force — nothing is changing its velocity"
    - "A small net force opposing motion, which will eventually stop it"
    - "A net force equal to its weight"
  answer: 1
  explanation: "Newton's First Law: constant velocity means zero net force. The puck continues moving because no net force acts on it — not because some force is 'keeping it going.' Option A is the Aristotelian misconception: that motion requires a continuous cause. The near-frictionless ice eliminates the decelerating force that would otherwise change the velocity."

- question: "A book rests motionless on a table. Which statement correctly describes the forces on it?"
  type: multiple-choice
  options:
    - "No forces act on the book because it is not moving"
    - "Only gravity acts, since the table is rigid and cannot exert force"
    - "Gravity pulls down and the normal force pushes up; these cancel to give zero net force"
    - "The table pushes up harder than gravity pulls down, keeping the book stationary"
  answer: 2
  explanation: "A stationary object does NOT mean zero force — it means zero NET force. Gravity and the normal force are both real and present; they are equal and opposite, summing to zero. Option A is the most common misconception. Option D is wrong because unequal forces would produce acceleration, not rest."

- question: "An object moving at constant velocity must have a net force acting on it to maintain that motion."
  type: true-false
  answer: false
  explanation: "This is Aristotle's view, not Newton's. Newton's First Law states that zero net force means constant velocity — including nonzero constant velocity. Force is required only to CHANGE velocity (accelerate or decelerate), not to sustain it. The illusion that motion requires force comes from everyday experience where friction is always present, decelerating moving objects."

- question: "An inertial reference frame is one in which Newton's laws hold as stated — specifically, a frame that is not itself accelerating."
  type: true-false
  answer: true
  explanation: "Newton's First Law implicitly defines inertial frames as its domain of validity. In a non-inertial frame (like a braking car), objects appear to accelerate without any applied force — a violation of the First Law. Newton's laws apply cleanly only from frames that are not themselves accelerating. This is a foundational constraint for all subsequent mechanics."

- question: "Why does everyday experience mislead people into thinking that objects require a continuous force to keep moving? What is the Newtonian correction?"
  type: short-answer
  answer: "Everyday objects slow down because friction is always present — it is a real decelerating force. Aristotle observed that moving objects come to rest and concluded that rest is natural and motion requires a continuous cause. Newton recognized that friction is the cause of deceleration, not the absence of a 'driving force.' On a frictionless surface in space, an object would continue at constant velocity indefinitely. The Newtonian correction: force causes change in velocity (acceleration), not velocity itself."
  explanation: "The key reframe is: instead of asking 'what keeps things moving?' ask 'what changes their motion?' Inertia is the tendency to resist changes in motion — which means constant motion (including rest) is the natural state, and force is what departs from it."
```

## Explainer

Before Newton, the dominant view of motion — tracing back to Aristotle — was that objects naturally come to rest, and that motion requires a continuous cause. Push a cart and it eventually stops; that seems to confirm that rest is the natural state and motion needs explaining. Newton's First Law overturns this picture completely. The question is not "what keeps things moving?" but "what changes their motion?" **Inertia** is the property of matter that resists changes in velocity — not changes in position, but changes in *how fast and in what direction* something is moving.

The law states: an object at rest stays at rest, and an object moving at constant velocity stays moving at constant velocity, unless a **net external force** acts on it. The word "net" is critical. From your kinematics work, you know that an object sitting on a table is not moving, but it is not experiencing zero force — gravity pulls it down and the normal force pushes it up, and these cancel. What matters is the vector sum of all forces. When net force is zero, velocity is constant (which includes zero as a special case). When net force is nonzero, velocity changes — that is the content of Newton's Second Law, which this topic builds toward.

The reason everyday experience misleads us is friction. When you push a book across a table and let go, it slows down — but not because motion naturally fades, because friction is a real force decelerating it. Imagine the same book on a frictionless surface in space: it would continue at constant velocity indefinitely. The hockey puck on nearly-frictionless ice approaches this ideal. What Aristotle saw as "natural rest" is actually the result of pervasive friction in everyday environments. Remove the friction, and the Newtonian picture is revealed: no force is required to *maintain* motion, only to *change* it.

Newton's First Law also defines the concept of an **inertial reference frame** — a coordinate system that is not itself accelerating. In a braking car, objects appear to fly forward "by themselves," apparently violating the First Law. But there is no force on those objects; it is the car (and your reference frame) that is decelerating. Newton's laws hold cleanly only from inertial frames. This is not a technicality but a foundational point: it sets the stage for all subsequent mechanics. Once you know what frame you are in and what forces are acting, the entire motion of a system is determined. The First Law tells you when no determination is needed — when things are simply left alone to continue doing what they are already doing.
