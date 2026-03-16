---
id: humid-air-thermodynamic-properties
title: Thermodynamic Properties of Humid Air Mixtures
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: psychrometric-analysis-humid-air
  type: hard
- id: gas-mixture-thermodynamics-daltons
  type: soft
builds-toward:
- combustion-stoichiometry-energy-release
tags:
- humid-air
- mixtures
- enthalpy
- entropy
stage: advanced
status: draft
---

# Thermodynamic Properties of Humid Air Mixtures

## Core Idea
Enthalpy of humid air per unit mass of dry air: h = h_da + ω*h_g, where ω is humidity ratio (kg water / kg dry air) and h_g is saturated vapor enthalpy. Entropy calculations account for the low partial pressure of water vapor. Psychrometric processes like adiabatic saturation and evaporative cooling relate wet-bulb temperature to mixture state.

## Explainer

From psychrometric analysis, you already know the key state variables: **humidity ratio** ω (kg water vapor per kg dry air), **relative humidity** φ = p_v / p_sat(T), and how to locate states on the psychrometric chart. Now you need to compute actual thermodynamic properties — enthalpy h and entropy s — so that you can apply the first and second laws to HVAC processes and calculate real energy requirements.

The **enthalpy of humid air** is expressed per unit mass of *dry air*, which is the natural bookkeeping unit because dry air mass is conserved in all typical psychrometric processes (humidification, dehumidification, mixing, sensible heating) while water vapor mass changes. The formula h = h_da + ω × h_g decomposes into two contributions: h_da ≈ c_p,da × T = 1.006T (kJ/kg·K) is the sensible enthalpy of the dry air fraction, and ω × h_g is the enthalpy carried by the water vapor. The vapor enthalpy h_g is taken from saturated steam tables at the mixture temperature — this is valid because at the low partial pressures of water vapor in air (well below 0.1 atm typically), the vapor behaves nearly ideally and its enthalpy depends on temperature alone, not on partial pressure. A convenient approximation: h_g ≈ 2501 + 1.86T (kJ/kg) where T is in °C, combining the latent heat of vaporization at 0°C with the sensible heating of the vapor.

**Entropy** of the mixture requires more care. From gas-mixture-thermodynamics and Dalton's law, each component's entropy is evaluated at its own **partial pressure**, not the total mixture pressure. The dry air entropy is s_da(T, p_da) and the vapor entropy is ω × s_v(T, p_v), where p_v = φ × p_sat(T). Because water vapor in air is at a partial pressure much lower than its saturation pressure, it has *higher* specific entropy than saturated steam at the same temperature — lower pressure always increases entropy at fixed temperature. This has a practical consequence: humidification by evaporation always increases mixture entropy, consistent with the second law.

The **adiabatic saturation process** connects these properties to the wet-bulb temperature. In an adiabatic saturator, unsaturated inlet air contacts a large water surface, evaporating water until the exiting air is saturated at the **adiabatic saturation temperature** T_as. With no heat exchange, an energy balance gives: h_inlet + (ω_s − ω_1) × h_f(T_as) = h_outlet, where ω_s is the saturation humidity ratio at T_as and h_f is the liquid water enthalpy at T_as. Substituting the enthalpy expressions and solving yields ω_1 as a function of T_1 and T_as. This is the working equation for determining the inlet state from wet-bulb and dry-bulb thermometer readings. For air-water mixtures specifically (not general gas-vapor pairs), the wet-bulb temperature is very nearly equal to the adiabatic saturation temperature, which is why psychrometric charts label those slanted lines as both wet-bulb temperature and adiabatic saturation temperature lines.

In HVAC system analysis, these enthalpy calculations let you quantify the energy cost of every process on the psychrometric chart. Heating along a constant ω line costs Δh_da = c_p,da ΔT per kg dry air. Humidification at constant T costs Δh = Δω × h_g. Mixing two airstreams requires a mass-weighted enthalpy balance to find the mixed-state point. Every arrow on the psychrometric chart corresponds to a first-law calculation using h = h_da + ω h_g, making the enthalpy formula the central computational tool for psychrometric engineering.
