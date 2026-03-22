---
id: acceleration-and-velocity
title: "Acceleration: How Velocity Changes"
domain: physics
course: conceptual-physics
prerequisites:
- id: newtons-second-law-conceptual
  type: hard
- id: what-is-speed
  type: hard
- id: one-step-equations
  type: hard
builds-toward:
- kinematics-1d
- kinematic-equations
tags:
- acceleration
- velocity
- change
- rate
stage: abstract-reasoning
status: draft
---
# Acceleration: How Velocity Changes

## Core Idea
Acceleration is the rate at which velocity changes over time: a = Δv/Δt. It tells you how quickly something speeds up, slows down, or changes direction. Positive acceleration means speeding up in the chosen direction, while negative acceleration (deceleration) means slowing down. Acceleration is measured in meters per second squared (m/s²).

## How It's Best Learned
Time yourself (or a toy car) going from rest to full speed and calculate the acceleration. Compare a car that reaches 60 mph in 4 seconds vs. one that takes 10 seconds — both reach the same speed, but the first one had greater acceleration. Use a ramp and a ball to observe how gravity causes constant acceleration downhill.

## Common Misconceptions
- Acceleration always means going faster. (Acceleration can mean speeding up, slowing down, or changing direction — it is any change in velocity.)
- If an object has zero velocity, it has zero acceleration. (A ball at the peak of a throw has zero velocity for an instant but is still accelerating downward due to gravity.)
- Higher speed means higher acceleration. (A car cruising at 100 km/h on a highway with constant speed has zero acceleration, while a car going from 0 to 10 km/h is accelerating.)
- Acceleration and velocity always point in the same direction. (When you are slowing down, acceleration points opposite to your velocity.)

## Questions

```yaml
- question: "A car goes from 0 m/s to 20 m/s in 5 seconds. What is its acceleration?"
  type: multiple-choice
  options: ["4 m/s²", "100 m/s²", "20 m/s²", "25 m/s²"]
  answer: 0
  explanation: "Acceleration = change in velocity / time = (20 - 0) / 5 = 4 m/s²."

- question: "An object moving at constant velocity has an acceleration of zero."
  type: true-false
  answer: true
  explanation: "Acceleration is the rate of change of velocity. If velocity is not changing — same speed, same direction — then acceleration is zero."

- question: "A ball is thrown straight up. At the very top of its path, what is its acceleration?"
  type: short-answer
  answer: "9.8 m/s² downward (the acceleration due to gravity), even though its velocity is momentarily zero."
  explanation: "Gravity acts on the ball throughout its flight. At the top, velocity is zero for an instant, but acceleration due to gravity never stops."
```

## Explainer
Speed tells you how fast you are going right now. **Acceleration** tells you how fast that speed is changing. If a basketball player sprints from rest to full speed in two seconds, they experienced a large acceleration. If they jog up to speed over ten seconds, the acceleration was smaller — even if they reached the same top speed.

Formally, **acceleration = change in velocity / change in time**, or **a = Δv / Δt**. The Greek letter delta (Δ) means "change in." If a car's velocity increases from 10 m/s to 30 m/s over 4 seconds, its acceleration is (30 - 10) / 4 = 5 m/s². The unit m/s² reads as "meters per second per second" — meaning the velocity changes by 5 meters per second during each second that passes.

Acceleration is not just about speeding up. When you slam the brakes in a car, your velocity decreases — that is negative acceleration (sometimes called **deceleration**). When a car goes around a curve at constant speed, its direction changes, and since velocity includes direction, the car is still accelerating. Any change in speed or direction counts as acceleration.

One important case is **free fall**. When you drop a ball, gravity accelerates it downward at about 9.8 m/s². After one second, it is falling at 9.8 m/s. After two seconds, 19.6 m/s. After three seconds, 29.4 m/s. The speed increases by the same amount each second — that is what constant acceleration looks like. This steady increase continues (ignoring air resistance) regardless of the object's mass, which is why a hammer and a feather fall at the same rate in a vacuum.

Understanding acceleration bridges the gap between knowing how fast something moves and understanding why it moves the way it does. Combined with Newton's Second Law (a = F/m), acceleration connects forces to motion, making it one of the most central ideas in all of physics.
