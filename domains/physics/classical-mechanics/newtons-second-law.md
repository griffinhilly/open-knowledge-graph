---
id: newtons-second-law
title: 'Newton''s Second Law: F = ma'
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-first-law
  type: hard
- id: kinematics-1d
  type: hard
- id: vectors-in-two-dimensions
  type: soft
builds-toward:
- free-body-diagrams
- friction-forces
- work-and-energy
- momentum-and-impulse
- circular-motion-dynamics
tags:
- newtons-laws
- force
- acceleration
- dynamics
stage: formal-systems
status: validated
---

# Newton's Second Law: F = ma

## Core Idea
The net force on an object equals the product of its mass and acceleration: ΣF = ma. Force and acceleration are both vectors pointing in the same direction. This law connects kinematics (how things move) to dynamics (why they move). It is the central equation of classical mechanics and underlies virtually every problem in the course.

## How It's Best Learned
Always start by identifying all forces on the object, then sum them as vectors to get the net force. Apply separately in each coordinate direction: ΣFx = max and ΣFy = may. Work many problems of increasing complexity before combining with energy or momentum methods.

## Common Misconceptions
- Using total force (magnitude of individual forces) instead of the net (vector sum) force.
- Confusing mass and weight: mass is a scalar property of matter; weight is the gravitational force mg acting on it.
- Thinking F = ma means force causes velocity, not acceleration.

## Questions

```yaml
- question: "A 3 kg object has two forces acting on it: 10 N to the right and 4 N to the left. What is the magnitude and direction of the object's acceleration?"
  type: multiple-choice
  options: ["4.67 m/s² to the right", "2 m/s² to the right", "3.33 m/s² to the left", "14 m/s² to the right"]
  answer: 1
  explanation: "The net force is 10 N - 4 N = 6 N to the right. By F = ma, a = F_net / m = 6 / 3 = 2 m/s² to the right. The most common error is using the total magnitude of forces (10 + 4 = 14 N) instead of the net force — this tests the misconception of confusing total force with net force."

- question: "If no net force acts on a moving object, the object will slow down and eventually stop."
  type: true-false
  answer: false
  explanation: "This is Newton's First Law (the law of inertia), and it is directly connected to the Second Law: when ΣF = 0, then a = 0, meaning the velocity does not change. The object continues at constant velocity. The intuition that things 'naturally stop' comes from everyday experience with friction, which is itself a force."

- question: "An object has a mass of 5 kg and is accelerating at 3 m/s². If the mass is doubled but the net force stays the same, what happens to the acceleration?"
  type: short-answer
  answer: "The acceleration is halved to 1.5 m/s²."
  explanation: "From F = ma, if F stays constant and m doubles, then a = F/(2m) = original acceleration / 2. This illustrates the inverse relationship between mass and acceleration: mass is a measure of how much an object resists acceleration."
```

## Explainer

From kinematics, you know how to describe motion — position, velocity, acceleration. From Newton's First Law, you know that objects do not change their velocity unless something forces them to. The Second Law is the missing link: it tells you *how much* the velocity changes when a force acts, and in what direction.

The equation ΣF = ma says that the net force on an object — the vector sum of every force acting on it — equals the object's mass multiplied by its acceleration. The key word is *net*. If you push a book to the right with 5 N and friction pushes back with 3 N, the net force is 2 N to the right, and that is the force that determines the acceleration. You never plug individual forces into F = ma; you always find the net force first.

Mass plays the role of resistance to acceleration. Think of it this way: if you apply the same net force to a basketball and a bowling ball, the basketball accelerates much more because it has less mass. Mass is not the same as weight — mass is how much stuff is in the object (measured in kilograms), while weight is the gravitational force pulling it down (W = mg, measured in Newtons). An astronaut on the Moon has the same mass but much less weight.

Because force and acceleration are both vectors, the Second Law works independently in each direction. For a problem with forces in two dimensions, you write ΣFx = max for the horizontal direction and ΣFy = may for the vertical direction. This decomposition is powerful: a ball rolling off a table has gravitational acceleration only in the y-direction, while its x-velocity stays constant. Each direction is governed by its own version of F = ma.

Nearly every problem in mechanics — from blocks on ramps to orbiting planets — starts with this law. The skill to develop is systematic: identify the object, list every force on it, sum those forces as vectors to get the net force, then apply a = ΣF/m. This process becomes second nature with practice, and it is the foundation for everything that follows in classical mechanics.
