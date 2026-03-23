---
id: parallel-circuits
title: Parallel Circuits
domain: physics
course: conceptual-physics
prerequisites:
- id: ohms-law-conceptual
  type: hard
- id: series-circuits
  type: hard
builds-toward:
- dc-circuits-series-parallel
tags:
- parallel
- circuit
- branches
stage: abstract-reasoning
status: validated
---
# Parallel Circuits

## Core Idea
In a parallel circuit, components are connected across the same two points, giving current multiple paths to follow. Each branch receives the full battery voltage. The total current from the battery splits among the branches, with more current flowing through lower-resistance paths. The total resistance is less than the smallest individual resistance: 1/R_total = 1/R₁ + 1/R₂ + .... If one branch breaks, the others continue working.

## How It's Best Learned
Connect two light bulbs in parallel with a battery and observe that each shines at full brightness. Remove one bulb and see that the other stays lit. Measure the current in each branch and verify that the branch currents add up to the total current from the battery.

## Common Misconceptions
- Total resistance in parallel is the sum of individual resistances. (This is the series rule. In parallel, 1/R_total = 1/R₁ + 1/R₂ + ..., making the total resistance less than any individual branch.)
- Adding more branches in parallel increases total resistance. (The opposite: more branches provide more paths for current, reducing the total resistance.)
- Each branch gets a fraction of the battery voltage. (In parallel, every branch gets the full voltage of the battery.)
- Current is the same in every branch. (Current splits based on resistance — lower resistance branches carry more current.)

## Questions

```yaml
- question: "Two 6 Ω resistors are connected in parallel. What is the total resistance?"
  type: multiple-choice
  options: ["12 Ω", "6 Ω", "3 Ω", "0.33 Ω"]
  answer: 2
  explanation: "1/R_total = 1/6 + 1/6 = 2/6 = 1/3, so R_total = 3 Ω. Two equal resistors in parallel give half the resistance of one."

- question: "In a parallel circuit, each branch receives the full battery voltage."
  type: true-false
  answer: true
  explanation: "All branches in a parallel circuit are connected directly across the same two points (the battery terminals), so each branch experiences the full voltage."

- question: "A 12 V battery is connected to two resistors in parallel: 4 Ω and 12 Ω. How much total current leaves the battery?"
  type: short-answer
  answer: "4 A. The 4 Ω branch draws 12/4 = 3 A, the 12 Ω branch draws 12/12 = 1 A, so total current = 3 + 1 = 4 A."
  explanation: "Each branch gets the full 12 V. Use I = V/R for each branch separately: 3 A + 1 A = 4 A total. (You can verify: R_total = 3 Ω, so I_total = 12/3 = 4 A.)"
```

## Explainer
While a series circuit has one path for current, a **parallel circuit** offers multiple paths. Picture a river that splits into several channels around an island — water flows through all channels simultaneously, and the total flow is the sum of each channel's flow. Similarly, in a parallel circuit, current from the battery splits among the branches and recombines on the other side.

The defining feature of parallel circuits is that **every branch receives the full voltage** of the battery. This is because each branch connects directly between the same two points (the positive and negative terminals of the battery). It does not matter how many branches there are — each one sees the complete voltage. This is why appliances in your house all operate at the same voltage (120V in the US) despite being on different circuits — they are all connected in parallel across the power supply.

**Current** divides among the branches based on their resistance. A branch with low resistance draws more current, while a branch with high resistance draws less. The total current from the battery equals the sum of all branch currents. If one branch draws 2 A and another draws 3 A, the battery supplies 5 A total.

The formula for **total resistance** in parallel is 1/R_total = 1/R₁ + 1/R₂ + .... This produces a total resistance that is always **less** than the smallest individual resistance. Adding more branches always decreases total resistance because you are providing more paths for current — like opening more checkout lanes at a store to reduce the overall wait. Two 100 Ω resistors in parallel give 50 Ω. Add a third, and it drops to about 33 Ω.

The biggest practical advantage of parallel circuits is **independence**: if one branch fails, the others continue to work normally. This is why your house is wired in parallel — when a light bulb burns out in the kitchen, your living room TV does not go dark. Each branch is an independent path. This reliability, combined with the fact that every device gets the full voltage it needs, makes parallel the standard wiring configuration for nearly all real-world electrical systems.
