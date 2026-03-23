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
status: validated
---

# Viscosity and Transport Properties

## Core Idea
Viscosity η measures resistance to flow, resulting from momentum transfer between molecular layers. In gases, viscosity arises from molecular collisions carrying momentum; surprisingly, viscosity is nearly independent of pressure (unlike density). In liquids, viscosity is much higher due to intermolecular attractions. Temperature dependence of viscosity reveals activation energy for flow. Kinetic theory relates viscosity to molecular parameters like collision cross-section and mass.

## Questions

```yaml
- question: "A gas is compressed to five times its original pressure at constant temperature. What happens to its viscosity?"
  type: multiple-choice
  options:
    - "It increases five-fold because there are five times as many molecules per unit volume to transfer momentum between layers"
    - "It remains essentially unchanged because the increase in density is exactly offset by a decrease in mean free path"
    - "It decreases because molecules collide more frequently and cannot travel far enough between layers to transfer momentum"
    - "It doubles because both density and collision frequency increase proportionally with pressure"
  answer: 1
  explanation: "This is Maxwell's counterintuitive result from 1860. At higher pressure, gas density ρ increases (more molecules per volume), but mean free path λ decreases by the same factor — molecules collide more often and travel shorter distances. In the kinetic theory expression η = ⅓ρ⟨c⟩λ, the product ρλ stays constant, so η is independent of pressure. This was a testable prediction that Maxwell made before experimental confirmation, and its verification was a major triumph of kinetic theory."

- question: "Why does raising temperature increase gas viscosity but decrease liquid viscosity?"
  type: multiple-choice
  options:
    - "Temperature increases molecular spacing in both phases, but viscosity depends on spacing only in gases"
    - "In gases, faster-moving molecules carry momentum more effectively between layers; in liquids, higher thermal energy helps molecules overcome attractive forces that impede flow"
    - "Gas viscosity decreases at high temperature due to reduced collision frequency; liquid viscosity increases because thermal expansion reduces molecular mobility"
    - "Temperature affects only polar molecules; the difference between gas and liquid behavior reflects differences in molecular polarity"
  answer: 1
  explanation: "The mechanisms are fundamentally different. In gases, viscosity comes from momentum transport — molecules jumping between layers carry momentum with them. Faster molecules (higher T) carry momentum more effectively, so η increases as roughly T^(1/2). In liquids, molecules are densely packed and viscosity arises from needing to overcome intermolecular attractions to flow past neighbors. Higher temperature gives molecules energy to clear these barriers, so η decreases following an Arrhenius relation η = A·exp(Eₐ/RT). The opposite temperature dependencies reflect completely different physical origins."

- question: "The viscosity of a gas increases with temperature because faster-moving molecules are more effective at transferring momentum between adjacent fluid layers."
  type: true-false
  answer: true
  explanation: "In kinetic theory, viscosity arises from molecules exchanging momentum between layers moving at different speeds. Molecules from a fast-moving layer carry extra forward momentum when they collide with a slow-moving layer, and vice versa. Higher temperature means higher mean molecular speed, which means more effective momentum transfer — so gas viscosity increases with temperature. This is opposite to everyday intuition built on liquids (which thin when heated), so it surprises many students on first encounter."

- question: "Since liquid viscosity decreases with increasing temperature, a highly viscous liquid like glycerol must have weaker intermolecular forces than a low-viscosity liquid like water."
  type: true-false
  answer: false
  explanation: "High viscosity in liquids reflects strong or extensive intermolecular forces, not weak ones. Glycerol has three hydroxyl groups, enabling extensive hydrogen bonding across a large molecule, giving it viscosity roughly 1500 times that of water. The correct relationship is the opposite: stronger intermolecular forces → higher activation energy Eₐ for flow → higher viscosity at a given temperature. Temperature decreases viscosity in all liquids because thermal energy helps overcome these forces, but the starting level is set by the strength of those forces."

- question: "Explain why Maxwell's prediction that gas viscosity is nearly independent of pressure seems counterintuitive, and provide a molecular-level explanation for why it is correct."
  type: short-answer
  answer: "It seems counterintuitive because higher pressure means more molecules per unit volume, and more molecules should mean more momentum transfer and therefore greater viscous drag. The error is forgetting that higher pressure also reduces mean free path: molecules collide more frequently and cannot travel as far between layers. In the kinetic theory expression η = ⅓ρ⟨c⟩λ, increasing pressure raises ρ but reduces λ by exactly the same factor, leaving their product — and therefore viscosity — unchanged. The result only breaks down at very high pressures (where molecular volume and interactions matter) or very low pressures (where the mean free path approaches the container size)."
  explanation: "Maxwell's prediction was remarkable because it implied a testable consequence that ran against intuition: pumping more gas into a container should not change how hard it is to stir. His prediction was experimentally confirmed, and the result convinced many physicists of the value of kinetic theory. The practical consequence is important: lubricants in pressurized environments (engines, hydraulic systems) that are gas-phase need not be reformulated for pressure effects, whereas liquid lubricant viscosity is more weakly pressure-dependent but more strongly temperature-dependent — a key engineering consideration."
```

## Explainer

From your work on diffusion and transport phenomena in gases, you understand that molecules in motion carry properties — mass, energy, momentum — from one region to another. **Viscosity** is the transport property associated with momentum transfer between adjacent layers of fluid moving at different speeds. Imagine two parallel plates with gas between them: the top plate moves to the right, the bottom plate is stationary. The gas layer touching the top plate moves with it; the layer touching the bottom plate is still. In between, each layer drags on the one below it, creating a velocity gradient. The force required to maintain this gradient is proportional to viscosity.

In gases, the molecular mechanism is beautifully simple. Molecules constantly fly between layers, carrying momentum with them. A molecule that jumps from a faster-moving layer to a slower one brings extra forward momentum, speeding up the slow layer. One that jumps from slow to fast carries a momentum deficit, slowing down the fast layer. The net effect is a friction-like force between layers — viscosity. Kinetic theory gives the result η = ⅓ρ⟨c⟩λ, where ρ is density, ⟨c⟩ is mean molecular speed, and λ is mean free path. Here is the surprising part: when you increase pressure, ρ goes up but λ goes down by the same factor (molecules collide more often), so η stays roughly constant. Maxwell predicted this counterintuitive result in 1860, and it was experimentally confirmed — gas viscosity is essentially independent of pressure over a wide range.

Temperature affects gas and liquid viscosity in opposite directions, revealing fundamentally different molecular mechanisms. In gases, raising temperature increases molecular speed, which means molecules carry momentum across layers more effectively — **gas viscosity increases with temperature**, roughly as T^(1/2) from kinetic theory (real gases show a slightly stronger dependence due to intermolecular forces). In liquids, the picture inverts completely. Liquid molecules are packed closely and must overcome intermolecular attractions to flow past each other. Raising temperature gives molecules more kinetic energy to overcome these barriers, so **liquid viscosity decreases with temperature**, following an Arrhenius-like relationship: η = A·exp(Eₐ/RT), where Eₐ is the activation energy for viscous flow. Honey flows readily when heated but sluggishly when cold — that is activation-energy-controlled viscosity in action.

The connection between viscosity and molecular structure is direct and practically useful. Larger molecules with more surface area for intermolecular contact have higher liquid viscosities — compare water (η ≈ 1 mPa·s) with glycerol (η ≈ 1500 mPa·s). Stronger intermolecular forces (hydrogen bonding, dipole-dipole) increase viscosity. For gases, larger collision cross-sections mean shorter mean free paths and more effective momentum transfer, but the relationship with molecular size is more nuanced because heavier molecules move slower. These molecular-level connections make viscosity measurements a probe of intermolecular interactions, useful in applications from lubricant design to blood rheology to polymer characterization.
