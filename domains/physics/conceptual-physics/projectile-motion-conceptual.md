---
id: projectile-motion-conceptual
title: Projectile Motion
domain: physics
course: conceptual-physics
prerequisites:
- id: acceleration-and-velocity
  type: hard
- id: what-is-gravity
  type: hard
builds-toward:
- projectile-motion
- kinematics-2d
tags:
- projectile
- trajectory
- gravity
stage: abstract-reasoning
status: validated
---
# Projectile Motion

## Core Idea
Projectile motion is the curved path an object follows when launched into the air and affected only by gravity (ignoring air resistance). The key insight is that horizontal and vertical motions are independent: the object moves at a constant horizontal speed while simultaneously accelerating downward due to gravity. This combination of constant horizontal velocity and increasing vertical velocity creates a parabolic path.

## How It's Best Learned
Toss a ball horizontally off a table and observe its curved path. Compare the landing point when you throw it gently vs. hard — the harder throw goes farther horizontally but hits the ground at the same time. Use a video camera or slow-motion replay to see the parabolic arc. Discuss how basketball shots and soccer kicks are real-world examples.

## Common Misconceptions
- A projectile's horizontal velocity changes during flight. (Without air resistance, the horizontal velocity remains constant — only the vertical velocity changes due to gravity.)
- An object dropped straight down reaches the ground sooner than one thrown horizontally from the same height. (They hit the ground at the same time because vertical acceleration is the same for both; the horizontal motion does not affect the vertical fall.)
- A projectile moves in a straight line until gravity "takes over." (Gravity acts from the instant the object is launched. The curve begins immediately.)
- A ball thrown at an angle goes up because the throwing force continues to push it upward. (The force of the throw only exists during contact. Once released, only gravity acts on the ball.)

## Questions

```yaml
- question: "A ball is thrown horizontally from a cliff. At the same moment, another ball is dropped straight down from the same height. Which hits the ground first?"
  type: multiple-choice
  options: ["The dropped ball", "The thrown ball", "They hit at the same time", "It depends on how hard the ball was thrown"]
  answer: 2
  explanation: "Both balls have the same initial vertical velocity (zero) and the same gravitational acceleration. The horizontal throw does not affect vertical fall time, so they hit the ground simultaneously."

- question: "During projectile motion (ignoring air resistance), the horizontal speed of the object remains constant."
  type: true-false
  answer: true
  explanation: "With no horizontal forces acting (air resistance ignored), there is nothing to change the horizontal velocity. Only the vertical velocity changes, due to gravity."

- question: "Why does a projectile follow a curved path instead of a straight line?"
  type: short-answer
  answer: "Because the constant horizontal velocity combines with a continuously increasing downward velocity from gravity, creating a curved (parabolic) trajectory."
  explanation: "The horizontal and vertical components of motion combine. The vertical speed keeps increasing due to gravity while the horizontal speed stays the same, bending the path into a curve."
```

## Explainer
When a basketball player shoots a three-pointer, the ball traces a beautiful arc through the air. That arc is a **projectile** path, and understanding it requires a powerful idea: the horizontal and vertical parts of the ball's motion are completely independent of each other.

Once the ball leaves the player's hands, the only force acting on it (ignoring air resistance) is **gravity**, which pulls straight down. There is no horizontal force. This means the ball's horizontal speed stays exactly the same throughout the flight, while its vertical speed changes constantly — increasing on the way down (or decreasing on the way up, if the ball was launched at an angle).

Here is a thought experiment that reveals this independence. Imagine standing on a cliff holding two balls. You drop one straight down and throw the other horizontally at the same instant. Which one hits the ground first? Surprisingly, they both hit at the same time. The dropped ball falls straight down, while the thrown ball curves outward and downward — but both experience the same vertical acceleration due to gravity. The thrown ball lands farther from the cliff, but not later.

The shape of a projectile's path is a **parabola** — a specific mathematical curve that results from constant horizontal velocity combined with constant vertical acceleration. The launch angle determines the shape: a ball launched straight horizontally makes a half-parabola downward, while a ball launched at an angle makes a symmetric arc that goes up, reaches a peak, and comes back down.

This independence of horizontal and vertical motion is what makes projectile problems manageable. Instead of trying to analyze the full curved path all at once, you can separate it into two simpler problems: a constant-velocity problem horizontally and a constant-acceleration problem vertically. Solve each one independently, then combine the results to find where and when the projectile lands. It is one of the most elegant problem-solving techniques in physics.
