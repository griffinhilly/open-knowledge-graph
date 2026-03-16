---
id: combustion-thermodynamic-analysis
title: Combustion Thermodynamics and Adiabatic Flame Temperature
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-open-systems
  type: hard
- id: combustion-stoichiometry-energy-release
  type: soft
tags:
- combustion
- heat-release
- adiabatic-flame-temperature
stage: advanced
status: draft
---

# Combustion Thermodynamics and Adiabatic Flame Temperature

## Core Idea
Combustion releases chemical energy stored in fuel, converting it to sensible heat and increased temperature of products; the heat of reaction (enthalpy of combustion) is the energy available for engine or power plant output. The first law applied to an open, steady-flow combustor relates reactant inlet enthalpy to product outlet enthalpy and any heat loss to surroundings. Adiabatic flame temperature (no heat loss) is the maximum achievable for any combustion temperature.

## How It's Best Learned
Write the combustion equation balancing atoms and molecules for stoichiometric or excess air conditions. Apply the first law to a control volume around the combustor: Σ n_i h_i(T_in) = Σ n_j h_j(T_out) + Q_loss. Calculate adiabatic flame temperature by setting Q_loss = 0 and solving for product temperature. Recognize that real flame temperatures are lower due to heat losses and incomplete combustion.

## Common Misconceptions
- All the heat released in combustion is available for useful work; heat losses in the combustor and subsequent cooling irreversibly destroy exergy.
- Combustion is a reversible process with maximum work output at Carnot efficiency; combustion is highly irreversible; exergy destruction is large despite large heat release.
- Adiabatic flame temperature is the same as actual flame temperature; adiabatic is an upper limit; actual temperatures are lower due to cooling and heat losses.

## Explainer

From your study of the first law for open systems, you know that for a steady-flow control volume, energy enters and leaves with mass (carrying enthalpy h = u + Pv) and via heat and shaft work. Applying this to a combustor means treating the reaction zone as a control volume: fuel and air enter, combustion products exit, and the difference in total enthalpy between inlet and outlet is accounted for by heat transfer to the surroundings. The chemical reaction is just the mechanism by which energy stored in molecular bonds is converted to thermal energy of the products — the first law does not care about the mechanism, only the accounting.

The **enthalpy of combustion** (or heat of reaction) quantifies the chemical energy release. Using formation enthalpies — tabulated values measuring enthalpy relative to stable elements at standard conditions — the energy released equals the sum of product formation enthalpies minus reactant formation enthalpies, all evaluated at the same reference temperature. For a steady-flow combustor, the first-law energy balance is: Σ(ṁᵢ · h̄ᵢ(T_in)) = Σ(ṁⱼ · h̄ⱼ(T_out)) + Q̇_loss, where h̄ includes both the formation enthalpy (chemical energy stored in that species) and the sensible enthalpy change from the reference temperature. This single equation governs all the thermodynamics of the combustor.

**Adiabatic flame temperature** is the special case Q̇_loss = 0: all chemical energy goes into heating the products, giving the theoretical maximum outlet temperature. To find it, you set the equation to Σ(ṁᵢ · h̄ᵢ(T_in)) = Σ(ṁⱼ · h̄ⱼ(T_adiabatic)) and solve for T_adiabatic. Because specific heats vary with temperature, this requires iteration: guess T_adiabatic, evaluate product enthalpies from tables, check if the balance closes, and adjust. The result depends strongly on the fuel-to-air ratio — near stoichiometric combustion, essentially all fuel reacts and peak temperatures are highest; rich or lean mixtures have diluents (unburned fuel or excess air) that absorb energy and lower the adiabatic temperature.

Real combustors always fall below the adiabatic limit due to heat losses through walls, radiation from hot gases, and incomplete combustion. Engineers use the gap between adiabatic and actual flame temperature as a diagnostic: large gaps indicate significant heat losses or poor mixing. For gas turbine designers, this matters acutely — peak combustor temperature is limited by turbine blade materials, and running lean (excess air) is the primary strategy to reduce flame temperature below the adiabatic limit while staying within material constraints. Understanding the thermodynamic analysis lets you trace exactly where the chemical energy goes and why combustion is inherently irreversible despite releasing large amounts of energy.
