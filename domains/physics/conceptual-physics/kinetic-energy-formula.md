---
id: kinetic-energy-formula
title: "Kinetic Energy: KE = ½mv²"
domain: physics
course: conceptual-physics
prerequisites:
- id: kinetic-energy-intro
  type: hard
- id: work-as-force-times-distance
  type: hard
- id: exponents-intro
  type: hard
builds-toward:
- kinetic-energy
- work-energy-theorem
tags:
- kinetic-energy
- formula
stage: abstract-reasoning
status: draft
---
# Kinetic Energy: KE = ½mv²

## Core Idea
Kinetic energy is the energy an object has because it is moving. The formula is KE = ½mv², where m is mass in kilograms and v is speed in meters per second. Because velocity is squared, doubling an object's speed quadruples its kinetic energy. This makes speed far more important than mass in determining kinetic energy. Kinetic energy is measured in joules.

## How It's Best Learned
Calculate the kinetic energy of familiar objects (a thrown baseball, a moving car, a running person) and compare. Change the speed in the formula and see how dramatically kinetic energy increases. Discuss why car crash damage is so much worse at highway speeds compared to parking-lot speeds.

## Common Misconceptions
- Doubling speed doubles kinetic energy. (Because of the v² in the formula, doubling speed actually quadruples kinetic energy.)
- A heavier object always has more kinetic energy. (A light object moving fast can have more kinetic energy than a heavy object moving slowly.)
- Kinetic energy is the same as momentum. (Momentum is p = mv, while kinetic energy is KE = ½mv². They have different formulas, different units, and behave differently.)
- Objects at rest have kinetic energy because they have mass. (KE = ½mv²; if v = 0, then KE = 0. Mass alone does not give kinetic energy.)

## Questions

```yaml
- question: "A 2 kg ball moves at 3 m/s. What is its kinetic energy?"
  type: multiple-choice
  options: ["6 J", "9 J", "3 J", "18 J"]
  answer: 1
  explanation: "KE = ½mv² = ½ × 2 × 3² = ½ × 2 × 9 = 9 J."

- question: "If you triple the speed of an object, its kinetic energy increases by a factor of nine."
  type: true-false
  answer: true
  explanation: "KE depends on v². Tripling v means the new KE = ½m(3v)² = ½m × 9v² = 9 × the original KE."

- question: "Why is a car crash at 60 mph so much more destructive than a crash at 30 mph?"
  type: short-answer
  answer: "Because kinetic energy depends on speed squared. Doubling the speed quadruples the kinetic energy, so there is four times as much energy to be absorbed in the crash."
  explanation: "At 60 mph (double 30 mph), the kinetic energy is 2² = 4 times greater. That extra energy causes far more damage to the vehicles and occupants."
```

## Explainer
You already know from everyday experience that moving objects carry energy — a rolling bowling ball can knock down pins, a moving car can crumple a fender, and a thrown basketball can knock a drink off a table. Physics gives this energy a name: **kinetic energy**, from the Greek word for motion. The formula that quantifies it is **KE = ½mv²**.

Let us break this formula down. The **m** is mass in kilograms, and **v** is speed in meters per second. The **½** is just a constant that comes from the mathematics of how work and energy are related. The most important feature is the **v²** — velocity is squared. This means that speed has a far greater impact on kinetic energy than mass does.

Here is a concrete example. A 1,000 kg car moving at 10 m/s has KE = ½ × 1,000 × 10² = 50,000 J. Now double the speed to 20 m/s: KE = ½ × 1,000 × 20² = 200,000 J. The speed doubled, but the kinetic energy quadrupled. Triple the speed to 30 m/s and the kinetic energy goes up by a factor of nine, to 450,000 J. This is why speed limits exist and why highway collisions are so much more devastating than low-speed fender benders.

Compare this to momentum (p = mv), where doubling speed simply doubles momentum. The squared relationship in kinetic energy makes it a fundamentally different quantity. Two objects can have the same momentum but very different kinetic energies, or vice versa. Each quantity is useful in different situations — momentum for analyzing collisions, kinetic energy for analyzing energy transfers.

Kinetic energy connects directly to the concept of **work**. The work-energy theorem states that the net work done on an object equals its change in kinetic energy. If you do 100 J of net work on a ball starting from rest, the ball ends up with 100 J of kinetic energy. This tight relationship between work and kinetic energy is one of the most useful tools in physics, allowing you to solve motion problems through energy methods instead of force-and-acceleration methods.
