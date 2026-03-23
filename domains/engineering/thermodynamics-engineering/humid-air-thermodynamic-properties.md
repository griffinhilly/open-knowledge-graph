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
stage: formal-systems
status: validated
---

# Thermodynamic Properties of Humid Air Mixtures

## Core Idea
Enthalpy of humid air per unit mass of dry air: h = h_da + ω*h_g, where ω is humidity ratio (kg water / kg dry air) and h_g is saturated vapor enthalpy. Entropy calculations account for the low partial pressure of water vapor. Psychrometric processes like adiabatic saturation and evaporative cooling relate wet-bulb temperature to mixture state.

## Questions

```yaml
- question: "An HVAC engineer is analyzing a humidification process where steam is injected into a duct at constant temperature. Why is enthalpy expressed per kilogram of dry air rather than per kilogram of total mixture?"
  type: multiple-choice
  options:
    - "Dry air enthalpy is always larger, so it gives more convenient numerical values"
    - "The total mixture mass changes as water vapor is added, but dry air mass is conserved, making it the natural accounting basis"
    - "The water vapor enthalpy is negligible compared to dry air enthalpy and can be ignored"
    - "Psychrometric charts are defined on a per-mole basis, and dry air has a simpler molar mass"
  answer: 1
  explanation: "In psychrometric processes, water vapor is added or removed while dry air mass stays constant. If you normalized by total mixture mass, the reference unit itself would change during humidification (the denominator grows as vapor is added), making energy balances confusing. Using dry air as the reference mass is like using a fixed accounting unit — it simplifies all energy calculations because the baseline never changes. Every term in h = h_da + ω·h_g is per kg of that fixed dry air mass."

- question: "At typical atmospheric conditions, the enthalpy of water vapor in humid air is evaluated using steam tables at the mixture temperature. This is valid because:"
  type: multiple-choice
  options:
    - "Water vapor in air behaves as a saturated liquid at low concentrations"
    - "The total pressure of the air-vapor mixture is always equal to the saturation pressure of water"
    - "At the low partial pressures of water vapor in air, it behaves nearly as an ideal gas and its enthalpy depends on temperature alone"
    - "The psychrometric chart assumes all humidity is in liquid form until the dew point is reached"
  answer: 2
  explanation: "Water vapor in atmospheric air exists at very low partial pressure (typically well below 0.1 atm) — far below its saturation pressure at typical temperatures. At such low pressures, vapor behavior closely approximates an ideal gas, for which enthalpy depends only on temperature, not pressure. This allows us to look up h_g from steam tables at the mixture temperature and use that value regardless of the actual partial pressure of the vapor in the mixture."

- question: "In a humidification process, adding water vapor to dry air always increases the total entropy of the mixture, consistent with the second law of thermodynamics."
  type: true-false
  answer: true
  explanation: "Water vapor in air exists at a partial pressure well below its saturation pressure — lower pressure always corresponds to higher specific entropy at fixed temperature (from the relation ds = -dP/T at constant T). When vapor is added to air, it enters a low-pressure environment where its entropy is high. The mixing process is irreversible — the vapor expands and mixes — and the combined system's entropy increases. This is consistent with the second law and explains why evaporative cooling and humidification are irreversible processes."

- question: "The wet-bulb temperature and dew point temperature represent the same thermodynamic state variable, just measured by different instruments."
  type: true-false
  answer: false
  explanation: "These are distinct state variables that convey different information. The dew point is the temperature to which air must be cooled (at constant pressure and humidity ratio) before condensation begins — it is a direct measure of the vapor partial pressure and humidity ratio. The wet-bulb temperature is the equilibrium temperature of a water-wetted surface exposed to the air — it depends on the adiabatic saturation process and is related to the enthalpy of the air-vapor mixture. Both are read from a psychrometric chart but along different lines and represent different physical quantities."

- question: "Why is dry air — rather than total humid air mass — used as the reference mass in psychrometric enthalpy calculations, and why does this simplify HVAC energy balances?"
  type: short-answer
  answer: "Dry air mass is conserved in essentially all psychrometric processes: when you heat, cool, humidify, dehumidify, or mix airstreams, the dry air mass stays constant while water vapor mass changes. If enthalpy were expressed per kilogram of total mixture, the reference unit would change every time moisture is added or removed, complicating energy balances. By anchoring all properties to a fixed mass of dry air, the energy balance for any process reduces to tracking changes in h = h_da + ω·h_g: the h_da term accounts for sensible heat changes, and the ω·h_g term accounts for the latent heat of added or removed vapor."
  explanation: "This choice of reference unit is analogous to using solvent mass rather than solution mass in solution thermodynamics — the solvent is the conserved component, so it provides a stable accounting baseline. In practice, it means that for any psychrometric process, you compute the enthalpy change per kg dry air at inlet and outlet states, multiply by the dry air mass flow rate, and get the total energy transfer directly — without needing to track changing mixture masses."
```

## Explainer

From psychrometric analysis, you already know the key state variables: **humidity ratio** ω (kg water vapor per kg dry air), **relative humidity** φ = p_v / p_sat(T), and how to locate states on the psychrometric chart. Now you need to compute actual thermodynamic properties — enthalpy h and entropy s — so that you can apply the first and second laws to HVAC processes and calculate real energy requirements.

The **enthalpy of humid air** is expressed per unit mass of *dry air*, which is the natural bookkeeping unit because dry air mass is conserved in all typical psychrometric processes (humidification, dehumidification, mixing, sensible heating) while water vapor mass changes. The formula h = h_da + ω × h_g decomposes into two contributions: h_da ≈ c_p,da × T = 1.006T (kJ/kg·K) is the sensible enthalpy of the dry air fraction, and ω × h_g is the enthalpy carried by the water vapor. The vapor enthalpy h_g is taken from saturated steam tables at the mixture temperature — this is valid because at the low partial pressures of water vapor in air (well below 0.1 atm typically), the vapor behaves nearly ideally and its enthalpy depends on temperature alone, not on partial pressure. A convenient approximation: h_g ≈ 2501 + 1.86T (kJ/kg) where T is in °C, combining the latent heat of vaporization at 0°C with the sensible heating of the vapor.

**Entropy** of the mixture requires more care. From gas-mixture-thermodynamics and Dalton's law, each component's entropy is evaluated at its own **partial pressure**, not the total mixture pressure. The dry air entropy is s_da(T, p_da) and the vapor entropy is ω × s_v(T, p_v), where p_v = φ × p_sat(T). Because water vapor in air is at a partial pressure much lower than its saturation pressure, it has *higher* specific entropy than saturated steam at the same temperature — lower pressure always increases entropy at fixed temperature. This has a practical consequence: humidification by evaporation always increases mixture entropy, consistent with the second law.

The **adiabatic saturation process** connects these properties to the wet-bulb temperature. In an adiabatic saturator, unsaturated inlet air contacts a large water surface, evaporating water until the exiting air is saturated at the **adiabatic saturation temperature** T_as. With no heat exchange, an energy balance gives: h_inlet + (ω_s − ω_1) × h_f(T_as) = h_outlet, where ω_s is the saturation humidity ratio at T_as and h_f is the liquid water enthalpy at T_as. Substituting the enthalpy expressions and solving yields ω_1 as a function of T_1 and T_as. This is the working equation for determining the inlet state from wet-bulb and dry-bulb thermometer readings. For air-water mixtures specifically (not general gas-vapor pairs), the wet-bulb temperature is very nearly equal to the adiabatic saturation temperature, which is why psychrometric charts label those slanted lines as both wet-bulb temperature and adiabatic saturation temperature lines.

In HVAC system analysis, these enthalpy calculations let you quantify the energy cost of every process on the psychrometric chart. Heating along a constant ω line costs Δh_da = c_p,da ΔT per kg dry air. Humidification at constant T costs Δh = Δω × h_g. Mixing two airstreams requires a mass-weighted enthalpy balance to find the mixed-state point. Every arrow on the psychrometric chart corresponds to a first-law calculation using h = h_da + ω h_g, making the enthalpy formula the central computational tool for psychrometric engineering.
