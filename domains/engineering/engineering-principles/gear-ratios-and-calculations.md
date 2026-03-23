---
id: gear-ratios-and-calculations
title: Gear Ratios and Calculations
domain: engineering
course: engineering-principles
prerequisites:
- id: ratios
  type: hard
- id: mechanical-advantage-intro
  type: hard
- id: one-step-equations
  type: hard
builds-toward:
- mechanical-advantage-quantitative
- linkages-and-mechanisms
tags:
- gears
- gear-ratio
- torque
- speed
- mechanical-systems
stage: abstract-reasoning
status: validated
---
# Gear Ratios and Calculations

## Core Idea
A gear ratio describes the relationship between two meshing gears based on their number of teeth. If a driving gear with 20 teeth meshes with a driven gear with 40 teeth, the gear ratio is 40/20 = 2:1. The driven gear rotates at half the speed of the driving gear but with twice the torque. Gear ratios allow engineers to trade speed for torque or vice versa: a low gear ratio (large driving gear, small driven gear) increases speed at the expense of torque, while a high gear ratio (small driving gear, large driven gear) increases torque at the expense of speed. The product of speed and torque -- the power transmitted -- remains approximately constant.

## How It's Best Learned
Use physical or simulated gears and count teeth. Rotate the driving gear one full turn and count how many turns the driven gear makes. Calculate the ratio from tooth counts and verify it matches the rotation count. Connect to bicycle gears: low gear (small front, large rear) = easy pedaling, slow speed; high gear (large front, small rear) = hard pedaling, fast speed.

## Common Misconceptions
- A larger gear always spins faster. (A larger gear has more teeth and spins slower when driven by a smaller gear. Size and speed are inversely related in meshing gears.)
- Gear ratios create free energy by increasing torque. (When torque increases, speed decreases proportionally. The total power -- torque times speed -- stays approximately the same. Gears redirect energy, not create it.)
- The gear ratio depends on the physical size of the gears. (It depends on the number of teeth, which correlates with size for gears of the same pitch, but the tooth count is what determines the exact ratio.)
- You need exactly two gears to create a gear ratio. (Compound gear trains use multiple pairs of gears to achieve very large or very small ratios. Each pair multiplies the overall ratio.)

## Questions

```yaml
- question: "A motor gear with 12 teeth drives a wheel gear with 48 teeth. What is the gear ratio?"
  type: multiple-choice
  options: ["1:4", "4:1", "12:48", "60:1"]
  answer: 1
  explanation: "Gear ratio = driven teeth / driving teeth = 48/12 = 4:1. The wheel gear turns 4 times slower than the motor gear but with 4 times the torque."

- question: "If a gear ratio increases torque, it must also increase speed."
  type: true-false
  answer: false
  explanation: "Gears trade speed for torque. A higher gear ratio (more torque) means lower output speed. The relationship is inverse: torque × speed is approximately constant (equal to the input power)."

- question: "A bicycle's front gear has 44 teeth and the rear gear has 11 teeth. How many times does the rear wheel rotate for each pedal revolution?"
  type: short-answer
  answer: "4 times. The gear ratio is 44/11 = 4, so for every one turn of the pedals, the rear wheel turns 4 times. This is a high gear -- fast but requires more pedaling force."
  explanation: "The front gear (driving) has more teeth than the rear gear (driven), so the rear wheel spins faster than the pedals. Each pedal revolution turns the rear wheel 44/11 = 4 times. This high gear ratio favors speed over ease of pedaling."
```

## Explainer
Gears are one of the oldest and most important mechanical inventions. Two toothed wheels mesh together so that when one turns, the other must turn too -- the teeth interlock and force coordinated rotation. But gears do much more than just transmit rotation: by using gears of different sizes, engineers can control the **speed** and **torque** of the output.

The **gear ratio** is determined by counting teeth. If the driving gear (connected to the motor or pedals) has 20 teeth and the driven gear (connected to the output) has 60 teeth, the gear ratio is 60/20 = 3:1. This means the driven gear turns 3 times slower but with 3 times the torque. Think of it as a lever wrapped in a circle: a longer lever arm (bigger gear) gives more force but moves more slowly.

On a bicycle, this is what gear shifting does. When you shift to a **low gear** (small front chainring, large rear sprocket), you get a low gear ratio -- perhaps 1:1 or even lower. Your legs spin fast but the rear wheel turns slowly with high torque, perfect for climbing hills. When you shift to a **high gear** (large front chainring, small rear sprocket), the ratio might be 4:1 -- each pedal revolution turns the rear wheel four times. You can go fast on flat ground, but pushing the pedals is much harder because you must produce more force.

The crucial insight is that **gears do not create power**. Power is the product of torque and rotational speed. When a gear train increases torque by a factor of 3, it decreases speed by a factor of 3, so the power stays the same (minus small friction losses). This is the mechanical equivalent of a conservation law -- you cannot get something for nothing. You can redistribute torque and speed, but the total power passing through the gears is determined by the motor or muscles driving them.

**Compound gear trains** chain multiple gear pairs together to achieve extreme ratios. A clock, for example, uses a series of gears to convert the slow unwinding of a spring or weight into the precise rotations of the hour, minute, and second hands -- each turning at a different speed. The total gear ratio of the compound train equals the product of all individual ratios. A pair with ratio 3 followed by a pair with ratio 4 gives a total ratio of 12. This stacking principle lets engineers achieve almost any desired ratio.
