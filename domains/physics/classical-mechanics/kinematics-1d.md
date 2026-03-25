---
id: kinematics-1d
title: Kinematics in One Dimension
domain: physics
course: classical-mechanics
prerequisites:
- id: slope-concept
  type: soft
- id: derivative-as-slope-of-tangent
  type: soft
- id: graphing-linear-equations
  type: soft
- id: antiderivatives
  type: soft
- id: vector-addition-subtraction
  type: soft
- id: functions-domain-codomain-range
  type: soft
- id: power-rule
  type: soft
builds-toward:
- kinematic-equations
- kinematics-2d
- newtons-first-law
tags:
- kinematics
- motion
- velocity
- acceleration
stage: formal-systems
status: validated
---

# Kinematics in One Dimension

## Core Idea
Kinematics describes motion without asking why it happens. Position, velocity, and acceleration are the three key quantities: velocity is the rate of change of position, and acceleration is the rate of change of velocity. In calculus terms, v = dx/dt and a = dv/dt. Understanding these relationships — both graphically and algebraically — is the foundation for all of classical mechanics.

## How It's Best Learned
Start by plotting position vs. time for simple scenarios and extracting velocity from slope. Then move to velocity-time graphs and interpret acceleration as slope. Connecting graphs to physical scenarios (a car braking, a ball thrown upward) builds genuine intuition before equations are introduced.

## Common Misconceptions
- Confusing velocity and speed: velocity is a signed quantity in 1D, speed is its magnitude.
- Thinking 'zero velocity' means 'zero acceleration' — a ball at the peak of its arc has zero velocity but nonzero acceleration.
- Misreading position-time graphs: a steep slope means high speed, not high position.

## Questions

```yaml
- question: "A ball is thrown straight upward. At the very top of its trajectory, what is true about its velocity and acceleration?"
  type: multiple-choice
  options: ["Both velocity and acceleration are zero", "Velocity is zero; acceleration is nonzero and directed downward", "Velocity is nonzero; acceleration is zero", "Both velocity and acceleration are nonzero and directed downward"]
  answer: 1
  explanation: "At the peak, the ball momentarily stops moving upward — its velocity is zero. But gravity does not stop acting. The acceleration due to gravity is approximately 9.8 m/s² downward throughout the entire flight, including at the peak. Zero velocity does not imply zero acceleration; confusing these two quantities is one of the most common kinematics errors."

- question: "On a position-time graph, a steeper slope indicates a higher position."
  type: true-false
  answer: false
  explanation: "On a position-time graph, the slope at any point equals the instantaneous velocity, not the position. A steep slope means the object is moving quickly; a flat (zero-slope) segment means it is momentarily at rest. The vertical height of the curve shows position, but steepness (slope) shows speed. Conflating slope with height is a classic graph-reading error."

- question: "What is the difference between velocity and speed in one-dimensional kinematics, and why does the distinction matter?"
  type: short-answer
  answer: "Speed is the magnitude of velocity — always non-negative. Velocity is signed: positive if moving in the chosen positive direction, negative if moving the other way. The distinction matters because displacement and direction of motion depend on the sign of velocity, not just its magnitude."
  explanation: "In 1D kinematics, we choose a positive direction (e.g., 'up' or 'to the right'). An object moving in the opposite direction has negative velocity but positive speed. This distinction becomes critical when computing displacements and identifying turning points: an object with velocity -10 m/s is moving fast — just in the negative direction."
```

## Explainer

Kinematics is the description of motion — not the *causes* of motion (that comes later with Newton's laws), but the geometry and mathematics of how position changes over time. Three quantities are central to everything: **position** (where the object is), **velocity** (how fast its position is changing), and **acceleration** (how fast its velocity is changing). Each is a rate of change of the previous one: v = dx/dt and a = dv/dt.

The best way to build intuition is through graphs. Imagine plotting the position of a car as it drives forward, slows, and stops. On a position-time graph the curve rises, becomes less steep, and flattens out. The **slope at any point on that curve equals the instantaneous velocity** — this is exactly the connection to derivatives you may have seen in calculus. Where the slope is steep, the car is moving fast; where it is zero (flat), the car is stopped. Now plot that velocity over time: as the car brakes, velocity decreases toward zero. The **slope of the velocity-time graph equals acceleration**. A downward slope means the velocity is decreasing — the car is decelerating.

An important and counterintuitive case: a ball thrown straight upward. On the way up, velocity is positive (upward) and decreasing. At the peak, velocity is exactly zero — but acceleration is still −9.8 m/s² (downward), because gravity never stops acting. This is where many students go wrong: they assume "stopped" means "no forces, no acceleration." It doesn't. Acceleration is about the *rate of change* of velocity, and the ball's velocity is continuously changing through the peak even though its value is momentarily zero. The instant after the peak, velocity becomes negative (downward) and the ball accelerates toward the ground.

Finally, keep velocity and speed clearly distinguished. In one dimension, you choose a positive direction (say, "up" or "to the right"). Velocity is signed — positive if moving in the positive direction, negative if moving the other way. Speed is the magnitude of velocity, always non-negative. A car moving leftward at 60 km/h has velocity −60 km/h (if rightward is positive) but speed 60 km/h. This distinction becomes critical when calculating displacement (which depends on direction) versus total distance traveled (which does not), and when interpreting what a negative value on a velocity-time graph actually means physically.
