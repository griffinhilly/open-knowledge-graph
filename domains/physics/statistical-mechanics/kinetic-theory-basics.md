---
id: kinetic-theory-basics
title: Kinetic Theory of Gases
domain: physics
course: statistical-mechanics
prerequisites:
- id: maxwell-boltzmann-distribution
  type: hard
- id: ensemble-theory-fundamentals
  type: hard
builds-toward:
- boltzmann-equation-kinetic
- brownian-motion
tags:
- kinetic-theory
- gases
- transport
stage: expert
status: validated
---

# Kinetic Theory of Gases

## Core Idea
Kinetic theory derives macroscopic gas properties from the microscopic Maxwell-Boltzmann distribution. By modeling particles as hard spheres undergoing random thermal motion and binary collisions, it yields transport coefficients for viscosity, thermal conductivity, and diffusion, demonstrating why these properties depend on temperature but not pressure.

## Questions

```yaml
- question: "A laboratory doubles the pressure of a gas at constant temperature. According to kinetic theory, what happens to the gas's viscosity?"
  type: multiple-choice
  options:
    - "Viscosity doubles — more molecules per unit volume means more momentum transfer per collision"
    - "Viscosity halves — higher pressure compresses the mean free path so molecules deposit momentum more locally"
    - "Viscosity is unchanged — the density increase is exactly offset by the decrease in mean free path, so the net momentum transport is the same"
    - "Viscosity increases with pressure, but not proportionally — the relationship is logarithmic"
  answer: 2
  explanation: "Viscosity scales as ρ⟨v⟩ℓ. Doubling pressure at constant temperature doubles the number density n (and hence ρ ~ nm), but it also halves the mean free path ℓ ~ 1/(√2πd²n). These factors cancel exactly: more molecules, each traveling half as far. The net momentum transport is unchanged. This pressure-independence was a famous and initially counterintuitive prediction of kinetic theory, later confirmed experimentally."

- question: "Why does gas viscosity increase with temperature while liquid viscosity decreases with temperature?"
  type: multiple-choice
  options:
    - "Gases expand at higher temperature, reducing the density and therefore the number of momentum-transferring collisions"
    - "In gases, higher temperature means faster molecules (⟨v⟩ ~ √T) that transport momentum more effectively — more viscous; in liquids, viscosity is dominated by intermolecular attractions that weaken with temperature — less viscous"
    - "The question is based on a false premise — both gas and liquid viscosities decrease with temperature, just at different rates"
    - "Gas molecules are lighter than liquid molecules, so temperature affects them differently"
  answer: 1
  explanation: "The mechanisms are opposite. In a gas, molecules transport momentum by traveling between collision points; higher temperature means faster molecules (⟨v⟩ ~ √T) carrying momentum more effectively — so viscosity increases as √T. In a liquid, molecules are densely packed and resistance to flow is governed by intermolecular attractions; as temperature rises, these attractions weaken and the liquid flows more easily. Kinetic theory thus makes a qualitative prediction that reveals the fundamental difference between dilute-gas and dense-liquid behavior."

- question: "Doubling the pressure of a gas at constant temperature will double its viscosity, because there are twice as many molecules available to transport momentum between fluid layers."
  type: true-false
  answer: false
  explanation: "This intuition misses the cancellation. More molecules (higher density) means more carriers of momentum, but higher pressure also shortens the mean free path — each molecule deposits its momentum closer to where it picked it up. Viscosity ~ ρ⟨v⟩ℓ, and since ρ ~ n while ℓ ~ 1/n, these factors cancel and viscosity is independent of pressure. This is one of the most elegant and counterintuitive results in kinetic theory."

- question: "The mean free path is the key intermediate concept in kinetic theory because it sets the length scale over which molecules transport momentum, energy, and mass before a collision interrupts the transfer."
  type: true-false
  answer: true
  explanation: "All transport coefficients — viscosity, thermal conductivity, diffusion — share the same dimensional structure: a density factor times a mean speed times the mean free path. The mean free path is what bridges the microscopic Maxwell-Boltzmann distribution to macroscopic, measurable properties. It quantifies how far a molecule 'carries' a property before depositing it in a collision, which is precisely why pressure-independence emerges when ℓ ~ 1/n cancels the density factor."

- question: "Explain why kinetic theory predicts that gas viscosity is independent of pressure, even though higher pressure means more molecules per unit volume."
  type: short-answer
  answer: "Viscosity scales as ρ⟨v⟩ℓ. Higher pressure increases number density n, which raises ρ ~ nm. But the mean free path ℓ ~ 1/(√2πd²n) decreases inversely with n. When pressure doubles, ρ doubles and ℓ halves — the product ρℓ remains constant. There are twice as many molecules, but each one travels half as far before depositing its momentum. The net momentum transport per unit area is unchanged, so viscosity is unchanged."
  explanation: "This cancellation is not a coincidence — it reflects the fact that in a dilute gas, viscosity is fundamentally a property of individual molecule transport, not of the number of molecules. The same cancellation applies to thermal conductivity. The result breaks down at very high pressures where the hard-sphere model fails, but it holds remarkably well across a wide range of conditions."
```

## Explainer

You've worked with the Maxwell-Boltzmann distribution, which tells you how molecular speeds are distributed in a gas at equilibrium. Kinetic theory takes that distribution as its starting point and derives the macroscopic, measurable properties of gases — viscosity, thermal conductivity, diffusion — from the microscopic behavior of individual molecules. The connection between scales is made possible by one key intermediate concept: the **mean free path**.

The mean free path ℓ = 1/(√2 πd²n) is the average distance a molecule travels between successive collisions, where d is the molecular diameter and n is the number density. For air at room temperature and pressure, ℓ ≈ 70 nm — far larger than atomic sizes but far smaller than any macroscopic container. This separation of scales is what makes kinetic theory tractable: molecules travel far enough between collisions to transport momentum, energy, or mass significant distances, but collide often enough that local equilibrium is maintained. Between these extremes, the gas behaves predictably.

Transport coefficients all follow a similar dimensional pattern. **Viscosity** η ~ ρ⟨v⟩ℓ, where ρ is the mass density and ⟨v⟩ is the mean speed from the Maxwell-Boltzmann distribution. This says viscosity measures how rapidly momentum diffuses — how far and how fast molecules carry their momentum before depositing it via collision. Now look at what cancels: the mean free path ℓ ~ 1/n, the density ρ ~ nm, and these factors cancel out. The result is that **viscosity is independent of pressure** — a famous and counterintuitive prediction confirmed experimentally. Similarly, **thermal conductivity** κ ~ cv⟨v⟩ℓ (where cv is the heat capacity per molecule) is also pressure-independent for the same reason.

The temperature dependences are more interesting. From the Maxwell-Boltzmann distribution, ⟨v⟩ ~ √(kT/m), so viscosity and thermal conductivity both scale as √T. This is opposite to liquids, where viscosity *decreases* with temperature. In a gas, higher temperature means faster molecules that transport momentum more effectively — greater viscosity. In a liquid, molecules are tightly packed and viscosity is dominated by intermolecular attractions, which weaken with temperature. Kinetic theory thus not only yields quantitative formulas for transport coefficients but makes qualitative predictions — like the √T scaling and pressure independence — that directly reveal the microscopic picture of a dilute gas of hard-sphere molecules in random thermal motion.
