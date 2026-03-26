---
id: kinetic-theory-of-gases
title: Kinetic Theory of Gases
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
- id: kinetic-energy
  type: hard
- id: conservation-of-momentum
  type: soft
builds-toward:
- rms-speed-and-kinetic-energy
- equipartition-theorem
- maxwell-boltzmann-distribution
tags:
- kinetic-theory
- molecular-model
- pressure
- temperature
- gas-molecules
stage: formal-systems
status: validated
---

# Kinetic Theory of Gases

## Core Idea
Kinetic theory provides a microscopic explanation for macroscopic gas properties. A gas consists of vast numbers of particles in random, rapid motion; pressure arises from the collective force of molecular collisions with container walls. By analyzing the average momentum transfer per collision and collision frequency, one derives PV = NkT (where N is molecule count and k = 1.38 × 10⁻²³ J/K is Boltzmann's constant). This links the macro quantity temperature to the average microscopic kinetic energy: (1/2)mv²_avg = (3/2)kT.

## How It's Best Learned
Derive the pressure formula step by step from Newton's laws applied to a single molecule bouncing between walls, then extend to an ensemble. The result — that temperature is a measure of average kinetic energy — should feel surprising and illuminating, not arbitrary.

## Common Misconceptions
- All molecules in a gas do not have the same speed; kinetic theory gives the average kinetic energy, but molecules have a distribution of speeds.
- Temperature being proportional to average kinetic energy applies only to translational motion — rotational and vibrational modes contribute separately.

## Questions

```yaml
- question: "According to kinetic theory, what does the temperature of a gas actually measure at the molecular level?"
  type: multiple-choice
  options: ["The speed of the fastest molecule", "The total kinetic energy of all molecules", "The average translational kinetic energy per molecule", "The pressure exerted by molecular collisions"]
  answer: 2
  explanation: "Temperature is proportional to the average kinetic energy per molecule: (1/2)mv²_avg = (3/2)kT. It is not the total energy (which depends on how many molecules there are), not the speed of any single molecule, and not pressure directly (though pressure and temperature are related through PV = NkT)."

- question: "In a gas at a fixed temperature, most molecules are moving at the same speed."
  type: true-false
  answer: false
  explanation: "Kinetic theory gives the *average* kinetic energy, but individual molecules have a wide distribution of speeds — some moving very slowly, others very fast. This distribution (the Maxwell-Boltzmann distribution) is a key result built on kinetic theory. The temperature fixes the average, not each individual molecule's speed."

- question: "Explain in molecular terms why compressing a gas into a smaller container (at constant temperature) increases its pressure."
  type: short-answer
  answer: "Smaller volume means molecules hit the walls more frequently, because they travel shorter distances between collisions. With more collisions per second per unit area of wall, the average force on the walls — which is pressure — increases."
  explanation: "Pressure arises from the rate of momentum transfer from molecules to the container walls. Reducing volume while keeping temperature constant (so molecular speeds stay the same) increases the collision rate per unit wall area, directly increasing pressure. This is the microscopic origin of Boyle's Law."
```

## Explainer

The ideal gas law PV = nRT tells you *that* pressure, volume, and temperature are related — but it says nothing about *why*. Kinetic theory answers the why by building a model from scratch: forget about P, V, and T as abstract quantities and instead imagine what is actually happening inside a gas. You have an enormous number of molecules (around 10²³ in a mole) moving in random directions at high speeds, constantly colliding with each other and with the walls of the container.

Start with a single molecule bouncing back and forth between two walls. Every time it hits a wall, it exerts a tiny force. Now multiply this by 10²³ molecules hitting every square centimeter of every wall billions of times per second. The average force per unit area across all those collisions is what we measure as pressure. By carefully tracking the momentum each molecule transfers to the wall — using Newton's second law, which you already know from mechanics — and averaging over all molecules, the algebra yields: PV = NkT, where N is the number of molecules and k is Boltzmann's constant.

The most profound result of this derivation is what temperature *is*. It turns out that the absolute temperature T is directly proportional to the average translational kinetic energy per molecule: (1/2)mv²_avg = (3/2)kT. Temperature is not a vague property of "hotness" — it is a precise measure of how hard the molecules are moving on average. This connects the macroscopic (thermometer reading) to the microscopic (molecular motion) in a single equation.

One critical misconception to avoid: kinetic theory gives the *average* kinetic energy, not the energy of every molecule. Molecules in a real gas have a broad distribution of speeds — the Maxwell-Boltzmann distribution. At any instant, some molecules are nearly stationary after a collision while others are moving extremely fast. Temperature characterizes the middle of this distribution, not a fixed speed. This will become important when you study evaporation (it is the fast-moving molecules at the surface that escape) and chemical reaction rates.
