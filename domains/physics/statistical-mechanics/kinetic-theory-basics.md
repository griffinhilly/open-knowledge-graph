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
stage: advanced
status: draft
---

# Kinetic Theory of Gases

## Core Idea
Kinetic theory derives macroscopic gas properties from the microscopic Maxwell-Boltzmann distribution. By modeling particles as hard spheres undergoing random thermal motion and binary collisions, it yields transport coefficients for viscosity, thermal conductivity, and diffusion, demonstrating why these properties depend on temperature but not pressure.

## Explainer

You've worked with the Maxwell-Boltzmann distribution, which tells you how molecular speeds are distributed in a gas at equilibrium. Kinetic theory takes that distribution as its starting point and derives the macroscopic, measurable properties of gases — viscosity, thermal conductivity, diffusion — from the microscopic behavior of individual molecules. The connection between scales is made possible by one key intermediate concept: the **mean free path**.

The mean free path ℓ = 1/(√2 πd²n) is the average distance a molecule travels between successive collisions, where d is the molecular diameter and n is the number density. For air at room temperature and pressure, ℓ ≈ 70 nm — far larger than atomic sizes but far smaller than any macroscopic container. This separation of scales is what makes kinetic theory tractable: molecules travel far enough between collisions to transport momentum, energy, or mass significant distances, but collide often enough that local equilibrium is maintained. Between these extremes, the gas behaves predictably.

Transport coefficients all follow a similar dimensional pattern. **Viscosity** η ~ ρ⟨v⟩ℓ, where ρ is the mass density and ⟨v⟩ is the mean speed from the Maxwell-Boltzmann distribution. This says viscosity measures how rapidly momentum diffuses — how far and how fast molecules carry their momentum before depositing it via collision. Now look at what cancels: the mean free path ℓ ~ 1/n, the density ρ ~ nm, and these factors cancel out. The result is that **viscosity is independent of pressure** — a famous and counterintuitive prediction confirmed experimentally. Similarly, **thermal conductivity** κ ~ cv⟨v⟩ℓ (where cv is the heat capacity per molecule) is also pressure-independent for the same reason.

The temperature dependences are more interesting. From the Maxwell-Boltzmann distribution, ⟨v⟩ ~ √(kT/m), so viscosity and thermal conductivity both scale as √T. This is opposite to liquids, where viscosity *decreases* with temperature. In a gas, higher temperature means faster molecules that transport momentum more effectively — greater viscosity. In a liquid, molecules are tightly packed and viscosity is dominated by intermolecular attractions, which weaken with temperature. Kinetic theory thus not only yields quantitative formulas for transport coefficients but makes qualitative predictions — like the √T scaling and pressure independence — that directly reveal the microscopic picture of a dilute gas of hard-sphere molecules in random thermal motion.
