---
id: specific-heat-capacity
title: Specific Heat Capacity
domain: physics
course: thermodynamics
prerequisites:
- id: heat-and-internal-energy
  type: hard
builds-toward:
- calorimetry
- heat-capacity-of-gases
- latent-heat
tags:
- specific-heat
- heat-capacity
- thermal-mass
stage: formal-systems
status: validated
---

# Specific Heat Capacity

## Core Idea
Specific heat capacity (c) is the amount of heat required to raise the temperature of 1 kg of a substance by 1 K. The relationship is Q = mcΔT. Different materials require vastly different amounts of heat for the same temperature change — water's unusually high specific heat (4186 J/kg·K) makes it a critical moderator of climate and an excellent coolant. Specific heat also depends weakly on temperature for many substances.

## How It's Best Learned
Calculate Q for familiar scenarios: heating water for cooking, cooling metal parts. Compare specific heats of metals versus water and interpret why metal frying pans heat up much faster than the water in them for the same energy input.

## Common Misconceptions
- Specific heat is a property of the material, not the sample — a larger sample doesn't have higher specific heat, it just requires more total heat energy.
- Specific heat and heat capacity are related but different: heat capacity = mc (for the whole object), while specific heat c is per unit mass.

## Explainer

You know that heat Q is the transfer of thermal energy, and that adding energy to a substance raises its temperature. But how much does the temperature rise? That depends on both the mass and what the substance is made of. **Specific heat capacity** c is the material property that tells you: Q = mcΔT. It is measured in J/(kg·K) and represents how much energy must be added to raise 1 kg of the substance by 1 K.

The range of specific heats across materials is striking. Water has c = 4186 J/(kg·K), one of the highest values of any common substance. Iron is about 450 J/(kg·K) — nearly 10 times lower. This means that if you supply the same amount of energy to equal masses of water and iron, the iron heats up about 10 times faster. A cast-iron frying pan and a pot of water sitting on the same burner illustrate this directly: the pan reaches cooking temperature long before the water boils, even though both are absorbing heat at similar rates. In calorimetry problems, this ratio — Q = mcΔT — is the central tool.

At the microscopic level, specific heat reflects how many ways a substance can store thermal energy. You know that internal energy is distributed among the microscopic degrees of freedom of molecules. A monatomic ideal gas (like argon) can only store energy as translational kinetic energy — three directions of motion, so three degrees of freedom. A diatomic molecule (like N₂) can also rotate, adding two more modes. Solids store energy as both kinetic and potential energy of vibration in the lattice (the **equipartition theorem** predicts c ≈ 3R/mol for metals, the **Dulong-Petit law**). Water's high specific heat comes from its ability to store energy in hydrogen bond vibrations and rotations in addition to translational modes. The more ways a molecule can absorb energy, the more energy you must add for a given temperature rise.

Water's anomalously high specific heat has enormous consequences. Oceans and large lakes heat up and cool down much more slowly than the land around them, moderating coastal climates. The human body is ~60% water, which buffers core temperature against external changes. Industrial cooling systems use water as a coolant precisely because large amounts of thermal energy can be absorbed with modest temperature rises. Whenever you see Q = mcΔT in a problem, ask: is the temperature change reasonable given the material? A large ΔT for water means a lot of energy went in — or a lot of mass is involved.
