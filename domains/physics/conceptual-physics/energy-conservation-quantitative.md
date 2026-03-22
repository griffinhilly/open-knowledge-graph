---
id: energy-conservation-quantitative
title: Conservation of Energy with Numbers
domain: physics
course: conceptual-physics
prerequisites:
- id: energy-conservation-intro
  type: hard
- id: kinetic-energy-formula
  type: hard
- id: gravitational-potential-energy
  type: hard
- id: two-step-equations
  type: soft
builds-toward:
- conservation-of-energy
- total-mechanical-energy-conservation
tags:
- conservation
- energy
- calculation
stage: abstract-reasoning
status: draft
---
# Conservation of Energy with Numbers

## Core Idea
The law of conservation of energy states that the total energy in a closed system stays constant — energy changes form but is never created or destroyed. In problems involving gravity and motion, this means the total of kinetic energy (½mv²) and gravitational potential energy (mgh) stays the same: KE₁ + PE₁ = KE₂ + PE₂. This lets you calculate speeds and heights without knowing the forces involved at every point.

## How It's Best Learned
Track a ball rolling down a ramp: calculate PE at the top and KE at the bottom, and verify they are equal. Work through roller coaster problems where you find the speed at different heights by setting total energy equal at each point. Use simulation software to watch energy bar charts change in real time.

## Common Misconceptions
- Energy conservation means energy stays in the same form. (Energy freely converts between forms — PE to KE to heat — but the total remains constant.)
- You always need to know the forces to find the speed at the bottom of a hill. (Energy conservation lets you bypass force analysis entirely, using only heights and speeds.)
- Conservation of energy only works when there is no friction. (It always works; friction just converts mechanical energy to thermal energy. If you account for all forms, total energy is still conserved.)
- The mass cancels out in every energy conservation problem. (Mass cancels when comparing PE and KE of the same object, but not when different objects or additional energy forms are involved.)

## Questions

```yaml
- question: "A 2 kg ball is dropped from 5 m. Using energy conservation, what is its speed just before hitting the ground? (Use g = 10 m/s²)"
  type: multiple-choice
  options: ["5 m/s", "10 m/s", "20 m/s", "50 m/s"]
  answer: 1
  explanation: "PE at top = KE at bottom: mgh = ½mv². The mass cancels: gh = ½v². So v² = 2gh = 2 × 10 × 5 = 100. v = 10 m/s."

- question: "If a roller coaster has 50,000 J of potential energy at the top of a hill and no kinetic energy, it will have 50,000 J of kinetic energy at the bottom (ignoring friction)."
  type: true-false
  answer: true
  explanation: "By conservation of energy, all the PE at the top converts to KE at the bottom when friction is ignored. Total energy stays at 50,000 J."

- question: "A skateboarder rolls down a 3 m ramp starting from rest. What is their speed at the bottom? (Use g = 10 m/s²)"
  type: short-answer
  answer: "About 7.7 m/s. Using mgh = ½mv², the mass cancels, giving v = √(2 × 10 × 3) = √60 ≈ 7.7 m/s."
  explanation: "Setting PE at top equal to KE at bottom: mgh = ½mv². Mass cancels. v = √(2gh) = √(2 × 10 × 3) = √60 ≈ 7.7 m/s."
```

## Explainer
Conservation of energy is one of the most powerful principles in all of physics. It says that **energy cannot be created or destroyed, only converted from one form to another**. In mechanics, the two main forms are **kinetic energy** (KE = ½mv²) and **gravitational potential energy** (PE = mgh). When an object rises, KE converts to PE as it slows down. When it falls, PE converts to KE as it speeds up. The total — KE + PE — stays the same throughout the motion.

Here is why this is so useful. Suppose a ball is dropped from 20 meters. You want to find its speed just before hitting the ground. Using forces and kinematics, you would need to know the acceleration and apply motion equations. Using energy conservation, you just write: PE at the top equals KE at the bottom. Since the ball starts at rest (KE₁ = 0) and ends at ground level (PE₂ = 0), you get **mgh = ½mv²**. The mass cancels on both sides, leaving v = √(2gh). Plug in: v = √(2 × 9.8 × 20) ≈ 19.8 m/s. Done.

Notice that the mass canceled out. This means that a heavy ball and a light ball dropped from the same height reach the same speed — consistent with what Galileo demonstrated centuries ago. The energy method does not care about the path or the time; it only cares about the starting and ending conditions. A ball sliding down a curvy ramp from 20 meters high reaches the same speed at the bottom as one dropped straight down from 20 meters (assuming no friction).

For more complex problems, you use the full equation: **KE₁ + PE₁ = KE₂ + PE₂**. On a roller coaster, if you know the speed and height at one point, you can find the speed at any other point. At the top of a 40-meter hill moving at 5 m/s, the coaster has both KE and PE. At the bottom, all that energy is KE. Halfway up the next hill, the energy is split between KE and PE. You can solve for unknown speeds or heights at any location.

When friction is present, some mechanical energy converts to **thermal energy** (heat). The total energy is still conserved — you just need to account for the heat: KE₁ + PE₁ = KE₂ + PE₂ + heat lost to friction. This means the object ends up with less KE than the frictionless case, which matches your experience — real roller coasters slow down over time and need the first hill to be the tallest.
