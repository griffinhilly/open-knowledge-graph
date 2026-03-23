---
id: archimedes-principle-conceptual
title: "Archimedes' Principle: Buoyancy"
domain: physics
course: conceptual-physics
prerequisites:
- id: floating-and-sinking
  type: hard
- id: density-intro
  type: hard
- id: pressure-force-over-area
  type: hard
tags:
- buoyancy
- archimedes
- displacement
stage: abstract-reasoning
status: validated
---
# Archimedes' Principle: Buoyancy

## Core Idea
Archimedes' Principle states that any object in a fluid experiences an upward buoyant force equal to the weight of the fluid it displaces. If the buoyant force equals the object's weight, it floats. If the object weighs more than the fluid it displaces, it sinks. This explains why heavy steel ships float — they are shaped to displace a huge volume of water, creating a buoyant force large enough to support their weight.

## How It's Best Learned
Weigh an object in air and then while submerged in water using a spring scale — the difference is the buoyant force. Mold a ball of clay (which sinks) into a boat shape (which floats) to demonstrate how shape affects the volume of displaced water. Measure the volume of water displaced and verify it matches the predicted buoyant force.

## Common Misconceptions
- Heavy objects always sink. (A steel aircraft carrier weighing thousands of tons floats because its hollow shape displaces enough water to create a buoyant force equal to its weight.)
- Buoyancy depends on an object's weight alone. (Buoyancy depends on the weight of displaced fluid, which depends on the object's volume and the fluid's density, not just the object's weight.)
- Objects float because they are "lighter than water." (More precisely, objects float when their average density is less than the fluid's density. A hollow steel ball has a low average density even though steel itself is denser than water.)
- The buoyant force increases the deeper an object sinks. (For a fully submerged object, the buoyant force is constant regardless of depth, because the displaced volume does not change.)

## Questions

```yaml
- question: "A solid block displaces 0.5 m³ of water when fully submerged. What is the buoyant force? (Density of water = 1,000 kg/m³, g = 10 m/s²)"
  type: multiple-choice
  options: ["500 N", "5,000 N", "50 N", "50,000 N"]
  answer: 1
  explanation: "Buoyant force = weight of displaced water = ρVg = 1,000 × 0.5 × 10 = 5,000 N."

- question: "A ball of clay sinks in water, but the same clay shaped into a bowl can float."
  type: true-false
  answer: true
  explanation: "The bowl shape displaces more water than the solid ball because it is hollow, creating a larger buoyant force. If the buoyant force equals or exceeds the clay's weight, the bowl floats."

- question: "How can a massive steel ship float when a small steel bolt sinks?"
  type: short-answer
  answer: "The ship's hollow hull displaces an enormous volume of water, creating a buoyant force equal to the ship's weight. The steel bolt displaces only a tiny volume of water — not enough buoyant force to support its weight because solid steel is denser than water."
  explanation: "Archimedes' Principle says buoyancy depends on displaced fluid volume. The ship's shape gives it a very large displacement volume and a low average density, allowing it to float."
```

## Explainer
The story goes that the ancient Greek scientist Archimedes was taking a bath when he noticed the water level rise as he settled in. He leaped out shouting "Eureka!" — "I have found it!" What he found was the principle of **buoyancy**: when an object is placed in a fluid, the fluid pushes up on it with a force equal to the weight of the fluid that the object pushes aside (displaces).

Mathematically, the **buoyant force** equals the weight of displaced fluid: F_buoyant = ρ_fluid × V_displaced × g, where ρ is the fluid's density, V is the volume of fluid displaced, and g is gravitational acceleration. A beach ball pushed underwater displaces a large volume of water, so the buoyant force is substantial — you can feel the water pushing the ball back up. A marble displaces very little water, so the buoyant force on it is tiny.

Whether an object floats or sinks comes down to a comparison: **if the buoyant force equals the object's weight, it floats.** This happens when the object's average density is less than the fluid's density. Wood floats in water because wood is less dense than water. Iron sinks because iron is denser. But density is average density, not the density of the material alone. A steel ship has a hull filled with air, making its **average** density much less than water's. The ship's hollow shape displaces an enormous volume of water — enough that the buoyant force supports the ship's entire weight.

This is why shaping matters so much. A solid ball of clay sinks because it displaces a small volume of water relative to its weight. But mold that same clay into a wide, shallow bowl, and it displaces much more water. If the bowl displaces enough water for the buoyant force to match the clay's weight, it floats — even though the material has not changed at all.

Archimedes' Principle applies to all fluids, not just water. Hot air balloons float in the atmosphere because the warm air inside the balloon is less dense than the cooler air outside, so the balloon's total weight (including the basket, passengers, and envelope) is less than the weight of the air it displaces. Submarines control their buoyancy by flooding or emptying ballast tanks — adding water makes them denser than the surrounding seawater (they sink), and expelling water makes them less dense (they rise). Buoyancy is one of the most practical and intuitive applications of fluid physics.
