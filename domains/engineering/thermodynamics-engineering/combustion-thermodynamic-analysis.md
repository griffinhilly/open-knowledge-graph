---
id: combustion-thermodynamic-analysis
title: Combustion Thermodynamics and Adiabatic Flame Temperature
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: first-law-open-systems
  type: hard
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
