---
id: thermal-conductivity-kinetic
title: Thermal Conductivity from Kinetic Theory
domain: physics
course: statistical-mechanics
prerequisites:
- id: chapman-enskog-expansion
  type: hard
builds-toward:
- green-kubo-formula
tags:
- transport
- kinetic-theory
- heat
stage: advanced
status: draft
---

# Thermal Conductivity from Kinetic Theory

## Core Idea
Thermal conductivity describes heat flow in response to temperature gradients. Kinetic theory shows that hot molecules carry more energy than cold ones; their random motion transports thermal energy. The Chapman-Enskog approach yields κ from first principles, accounting for both translational and internal degrees of freedom.

## Explainer

**Fourier's law** states that the heat flux q (energy per unit area per unit time) flowing through a material is proportional to the temperature gradient: q = -κ ∇T, where κ is the thermal conductivity. This is a macroscopic, empirical law — but kinetic theory provides its microscopic derivation. The Chapman-Enskog expansion you've studied produces κ as a systematic result of solving the Boltzmann equation to first order in the gradient. Understanding where κ comes from builds intuition for why different materials conduct heat so differently.

The physical picture starts with a simple thought experiment. Imagine a gas with a temperature gradient in the x-direction: the left side is hotter and the right side cooler. Molecules on the left side have, on average, higher kinetic energy than those on the right. Because molecules are in constant random thermal motion, they travel across the temperature gradient and mix. When a fast (hot) molecule from the left collides with slower (cool) molecules on the right, it transfers energy, carrying heat in the direction of decreasing temperature. The **mean free path** λ — the average distance a molecule travels between collisions — determines how far across the gradient a molecule can carry its excess energy before thermalizing. The **mean thermal speed** v̄ sets how fast this transport happens. Simple mean-free-path analysis gives κ ~ (1/3) ρ c_v v̄ λ, where ρ is mass density and c_v is the specific heat capacity.

The Chapman-Enskog method refines this estimate rigorously by solving the Boltzmann equation perturbatively in the small parameter (λ/L), where L is the macroscopic length scale of the temperature variation. The result for a monatomic ideal gas is κ = (5/2)(k_B / σ_eff) √(k_B T / πm), where σ_eff is an effective collision cross section determined by the intermolecular potential. Several predictions follow immediately: κ is independent of pressure (because higher pressure increases molecular density but decreases λ proportionally — the two effects cancel), it increases with temperature (as v̄ ~ √T grows), and it is larger for lighter gases (which move faster). These are all borne out experimentally.

For polyatomic molecules, the treatment becomes richer because **internal degrees of freedom** — rotation, vibration — also store and transport energy. A rotating molecule can absorb translational energy from a collision and then carry it across the gradient as rotational energy, an additional channel not present for monatomic gases. The Chapman-Enskog calculation must then account for the coupling between translational and internal modes through inelastic collisions, giving a correction factor (the Eucken correction) that modifies the monatomic result. The full result, κ = (1/4)(9γ - 5)(c_v η), where η is viscosity and γ = c_p/c_v, connects thermal conductivity directly to viscosity — both emerge from the same kinetic transport process, differing only in whether molecules carry energy or momentum across the gradient.
