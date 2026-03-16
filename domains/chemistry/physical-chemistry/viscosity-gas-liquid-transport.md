---
id: viscosity-gas-liquid-transport
title: Viscosity and Transport Properties
domain: chemistry
course: physical-chemistry
prerequisites:
- id: diffusion-coefficients-molecular-kinetics
  type: hard
- id: transport-phenomena-gases
  type: soft
tags:
- viscosity
- transport
- rheology
- molecular
stage: advanced
status: draft
---

# Viscosity and Transport Properties

## Core Idea
Viscosity η measures resistance to flow, resulting from momentum transfer between molecular layers. In gases, viscosity arises from molecular collisions carrying momentum; surprisingly, viscosity is nearly independent of pressure (unlike density). In liquids, viscosity is much higher due to intermolecular attractions. Temperature dependence of viscosity reveals activation energy for flow. Kinetic theory relates viscosity to molecular parameters like collision cross-section and mass.

## Explainer

From your work on diffusion and transport phenomena in gases, you understand that molecules in motion carry properties — mass, energy, momentum — from one region to another. **Viscosity** is the transport property associated with momentum transfer between adjacent layers of fluid moving at different speeds. Imagine two parallel plates with gas between them: the top plate moves to the right, the bottom plate is stationary. The gas layer touching the top plate moves with it; the layer touching the bottom plate is still. In between, each layer drags on the one below it, creating a velocity gradient. The force required to maintain this gradient is proportional to viscosity.

In gases, the molecular mechanism is beautifully simple. Molecules constantly fly between layers, carrying momentum with them. A molecule that jumps from a faster-moving layer to a slower one brings extra forward momentum, speeding up the slow layer. One that jumps from slow to fast carries a momentum deficit, slowing down the fast layer. The net effect is a friction-like force between layers — viscosity. Kinetic theory gives the result η = ⅓ρ⟨c⟩λ, where ρ is density, ⟨c⟩ is mean molecular speed, and λ is mean free path. Here is the surprising part: when you increase pressure, ρ goes up but λ goes down by the same factor (molecules collide more often), so η stays roughly constant. Maxwell predicted this counterintuitive result in 1860, and it was experimentally confirmed — gas viscosity is essentially independent of pressure over a wide range.

Temperature affects gas and liquid viscosity in opposite directions, revealing fundamentally different molecular mechanisms. In gases, raising temperature increases molecular speed, which means molecules carry momentum across layers more effectively — **gas viscosity increases with temperature**, roughly as T^(1/2) from kinetic theory (real gases show a slightly stronger dependence due to intermolecular forces). In liquids, the picture inverts completely. Liquid molecules are packed closely and must overcome intermolecular attractions to flow past each other. Raising temperature gives molecules more kinetic energy to overcome these barriers, so **liquid viscosity decreases with temperature**, following an Arrhenius-like relationship: η = A·exp(Eₐ/RT), where Eₐ is the activation energy for viscous flow. Honey flows readily when heated but sluggishly when cold — that is activation-energy-controlled viscosity in action.

The connection between viscosity and molecular structure is direct and practically useful. Larger molecules with more surface area for intermolecular contact have higher liquid viscosities — compare water (η ≈ 1 mPa·s) with glycerol (η ≈ 1500 mPa·s). Stronger intermolecular forces (hydrogen bonding, dipole-dipole) increase viscosity. For gases, larger collision cross-sections mean shorter mean free paths and more effective momentum transfer, but the relationship with molecular size is more nuanced because heavier molecules move slower. These molecular-level connections make viscosity measurements a probe of intermolecular interactions, useful in applications from lubricant design to blood rheology to polymer characterization.
