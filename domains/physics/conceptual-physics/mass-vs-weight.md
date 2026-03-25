---
id: mass-vs-weight
title: Mass vs. Weight
domain: physics
course: conceptual-physics
prerequisites:
- id: newtons-second-law-conceptual
  type: hard
- id: what-is-gravity
  type: hard
- id: momentum-intro
  type: soft
builds-toward:
- newtons-law-of-gravitation
- free-fall
tags:
- mass
- weight
- gravity
stage: abstract-reasoning
status: validated
---
# Mass vs. Weight

## Core Idea
Mass is the amount of matter in an object and is measured in kilograms. Weight is the gravitational force acting on that mass, calculated by W = mg, where g is the acceleration due to gravity (about 9.8 m/s² on Earth). Mass stays the same no matter where you are, but weight changes depending on the strength of gravity at your location.

## How It's Best Learned
Compare the mass of an object on a balance scale (which compares masses) with its weight on a spring scale (which measures gravitational force). Discuss how an astronaut's mass stays the same on the Moon but their weight drops to about one-sixth.

## Common Misconceptions
- Mass and weight are the same thing. (Mass is the amount of matter and never changes; weight is a force that depends on gravity.)
- You would be weightless in the International Space Station because there is no gravity. (Gravity is still strong there — astronauts feel weightless because they are in free fall along with the station.)
- A scale always measures mass. (Bathroom scales measure the force of gravity on you — your weight. Balance scales compare masses.)
- Your mass changes when you go to the Moon. (Only your weight changes. Your mass — the amount of stuff you are made of — stays the same.)

## Questions

```yaml
- question: "An astronaut has a mass of 80 kg. On the Moon, where g ≈ 1.6 m/s², what is the astronaut's weight?"
  type: multiple-choice
  options: ["80 N", "128 N", "784 N", "50 kg"]
  answer: 1
  explanation: "Weight = mass × g = 80 kg × 1.6 m/s² = 128 N. The astronaut's mass stays 80 kg, but the weight is much less than on Earth (where it would be about 784 N)."

- question: "Your mass would be different on Jupiter than on Earth."
  type: true-false
  answer: false
  explanation: "Mass is an intrinsic property of matter — it does not change based on location. Only weight changes because gravitational acceleration differs between planets."

- question: "What is the weight of a 5 kg object on Earth (g = 9.8 m/s²)?"
  type: short-answer
  answer: "49 N, because W = mg = 5 × 9.8 = 49 N."
  explanation: "Weight equals mass times gravitational acceleration. 5 kg × 9.8 m/s² = 49 newtons."
```

## Explainer
In everyday life, people use "mass" and "weight" interchangeably. You might say you weigh 70 kilograms, but in physics, those two words mean very different things. **Mass** is the amount of matter in an object, measured in kilograms (kg). **Weight** is the gravitational force pulling on that mass, measured in newtons (N).

The connection between them comes from Newton's Second Law. Since weight is just the force of gravity on an object, and F = ma, we can write **W = mg**, where W is weight, m is mass, and g is the gravitational acceleration at that location. On Earth, g is approximately 9.8 m/s², so a 10 kg object weighs about 98 N.

Here is why the distinction matters: if you traveled to the Moon, your mass would stay exactly the same — you are still made of the same atoms. But the Moon's gravitational acceleration is only about 1.6 m/s², roughly one-sixth of Earth's. So your weight would drop to about one-sixth of what it is on Earth. You would feel incredibly light and could jump much higher, even though nothing about your body changed.

This also explains why astronauts aboard the International Space Station appear weightless. The ISS orbits only about 400 km above Earth, where gravity is still about 90% as strong as on the surface. The astronauts float not because gravity is absent, but because both they and the station are in **free fall** — constantly falling toward Earth but moving sideways fast enough to keep missing it. In free fall, there is no normal force pushing up on you, so you experience apparent weightlessness even though gravitational force still acts on your mass.

Understanding the mass-weight distinction is essential for solving physics problems correctly. Whenever a problem gives you mass in kilograms and asks for a force, you need to multiply by g to get weight. And whenever you see a force measured in newtons, remember that it is not the same as mass — it is mass multiplied by gravitational acceleration.
