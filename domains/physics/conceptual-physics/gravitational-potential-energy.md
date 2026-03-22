---
id: gravitational-potential-energy
title: "Gravitational Potential Energy: PE = mgh"
domain: physics
course: conceptual-physics
prerequisites:
- id: potential-energy-intro
  type: hard
- id: work-as-force-times-distance
  type: hard
- id: mass-vs-weight
  type: soft
builds-toward:
- potential-energy
- gravitational-potential-energy-extended
tags:
- potential-energy
- gravity
- height
stage: abstract-reasoning
status: draft
---
# Gravitational Potential Energy: PE = mgh

## Core Idea
Gravitational potential energy (GPE) is the energy stored in an object because of its height above a reference level. The formula is PE = mgh, where m is mass (kg), g is gravitational acceleration (9.8 m/s² on Earth), and h is height (m). The higher or heavier an object is, the more gravitational potential energy it has. This energy can be converted into kinetic energy when the object falls.

## How It's Best Learned
Lift a ball to different heights and drop it — observe that it hits the ground harder from higher up. Calculate PE at different heights and connect it to how fast the ball is moving when it lands. Compare lifting a light ball vs. a heavy ball to the same height to see how mass affects PE.

## Common Misconceptions
- Gravitational potential energy depends on where the object is going. (It depends only on the object's current height relative to the reference level, not its future path.)
- The reference level (h = 0) must always be the ground. (You can choose any convenient reference level. What matters is the change in height.)
- An object at ground level has no energy at all. (It has zero gravitational PE relative to the ground, but it may have kinetic energy, thermal energy, or chemical energy.)
- Gravitational PE exists only when the object is falling. (The energy is stored as long as the object is above the reference level, whether it is moving or not.)

## Questions

```yaml
- question: "A 3 kg book sits on a shelf 2 meters above the floor. What is its gravitational potential energy relative to the floor? (Use g = 10 m/s²)"
  type: multiple-choice
  options: ["6 J", "30 J", "60 J", "15 J"]
  answer: 2
  explanation: "PE = mgh = 3 × 10 × 2 = 60 J."

- question: "Doubling the height of an object doubles its gravitational potential energy."
  type: true-false
  answer: true
  explanation: "PE = mgh is directly proportional to height. If h doubles while m and g stay the same, PE doubles."

- question: "Why does a roller coaster start by climbing to the top of the tallest hill?"
  type: short-answer
  answer: "To store the maximum gravitational potential energy, which will be converted to kinetic energy as the coaster descends through the rest of the ride."
  explanation: "The initial climb gives the coaster PE = mgh. As it drops, this PE converts to KE (speed). The tallest hill provides enough energy for the entire ride."
```

## Explainer
Imagine carrying a basketball up to the top of a stadium. It took effort to get the ball up there — you had to do work against gravity. Where did that energy go? It did not just vanish. It got stored as **gravitational potential energy** (GPE), waiting to be released the moment you let the ball drop.

The formula **PE = mgh** captures exactly how much energy is stored. The **m** is the object's mass, **g** is the gravitational acceleration (about 9.8 m/s² on Earth, often rounded to 10 for easier calculation), and **h** is the height above whatever reference point you choose. A 5 kg ball held 10 meters high has PE = 5 × 9.8 × 10 = 490 J of stored gravitational energy.

The reference level — where h = 0 — is your choice. If you are on the second floor of a building, you might set the floor as your reference. Relative to the ground outside, the same object would have a larger h and therefore more PE. What matters in most problems is the **change** in height, not the absolute value. When a roller coaster drops 30 meters, it converts the PE associated with those 30 meters into kinetic energy, regardless of whether the track is at sea level or on a mountaintop.

This leads to one of the most elegant ideas in physics: the exchange between gravitational potential energy and kinetic energy. At the top of a drop, a roller coaster has maximum PE and minimum KE (it is barely moving). At the bottom, the PE has been converted almost entirely into KE (it is moving at maximum speed). On the way back up the next hill, KE converts back into PE as the coaster slows down. This back-and-forth trade is the core of energy conservation in mechanics.

Gravitational potential energy also explains why dams generate electricity (water high up has enormous PE that converts to KE as it falls, spinning turbines), why ski jumpers crouch at the top of the ramp (maximizing the height they fall through), and why it is so much harder to bike uphill than downhill (you are adding PE on the way up and releasing it on the way down).
