---
id: phase-equilibrium-clausius-clapeyron-detailed
title: Phase Equilibrium and Clausius-Clapeyron Equation
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: clausius-clapeyron-vapor-pressure
  type: hard
- id: pure-substance-phase-diagrams
  type: soft
- id: clausius-clapeyron-equation
  type: hard
builds-toward:
- saturated-superheated-property-regions
- psychrometric-analysis-humid-air
- vapor-compression-refrigeration-cycles
tags:
- phase-equilibrium
- clausius-clapeyron
- saturation
- transitions
stage: formal-systems
status: draft
---

# Phase Equilibrium and Clausius-Clapeyron Equation

## Core Idea
The Clausius-Clapeyron equation dp/dT = h_fg / (T(v_g - v_f)) describes saturation pressure change with temperature during phase transitions. It enables vapor pressure calculation from latent heat and underpins all two-phase thermodynamic processes. For small pressure changes near saturation, vapor pressure grows approximately exponentially with temperature.

## Questions

```yaml
- question: "A pressure cooker operates at approximately 2 atm (twice atmospheric pressure). Food cooks significantly faster than in an open pot. Why?"
  type: multiple-choice
  options:
    - "Higher pressure forces heat to transfer more rapidly from the steam into the food"
    - "At higher pressure, the saturation temperature is higher (per the Clausius-Clapeyron equation), so water remains liquid above 100°C and cooks food at a higher temperature"
    - "Compressed steam at 2 atm has twice the thermal energy of atmospheric steam at the same temperature"
    - "Higher pressure increases the specific heat of water, allowing it to store and release more energy"
  answer: 1
  explanation: "The Clausius-Clapeyron equation dp/dT = h_fg/(T·Δv) tells us that saturation pressure increases with temperature. Equivalently, fixing higher pressure forces the saturation temperature higher — at 2 atm, water boils at about 121°C instead of 100°C. Food chemistry (enzymatic breakdown, protein denaturation, starch gelatinization) proceeds much faster at 121°C than 100°C — roughly doubling for every 10°C increase. The cooking speed advantage comes entirely from the elevated temperature, enabled by the higher pressure keeping water liquid above its atmospheric boiling point."

- question: "The solid-liquid phase boundary for water on a P-T diagram has a negative slope — pressure increases as temperature decreases along the boundary. Which statement correctly identifies why this is unusual and what causes it?"
  type: multiple-choice
  options:
    - "Water has an unusually high latent heat of fusion, making dp/dT very negative"
    - "Water expands on freezing, so Δv = v_liquid − v_ice is negative; since dp/dT = h_fus/(T·Δv), the slope is negative"
    - "The entropy change on melting is negative for water, reversing the Clausius-Clapeyron sign"
    - "Ice has a higher specific heat than water, which inverts the Clausius-Clapeyron relationship"
  answer: 1
  explanation: "Most substances contract on freezing (solid denser than liquid), giving a positive Δv at melting and a positive dp/dT slope for the solid-liquid boundary. Water is anomalous: ice is less dense than liquid water (ice floats), so Δv = v_liquid − v_ice < 0. In the Clausius-Clapeyron equation dp/dT = h_fus/(T·Δv), both h_fus and T are positive, so the sign of dp/dT is determined by Δv — which is negative for water. This means the melting point decreases under pressure (ice melts under pressure), a property with important consequences for ice skating physics and glacial flow."

- question: "According to the Clausius-Clapeyron equation, saturation pressure grows approximately linearly with temperature for typical liquid-vapor transitions over moderate temperature ranges."
  type: true-false
  answer: false
  explanation: "Saturation pressure grows approximately exponentially with temperature, not linearly. The integrated approximate form is ln(P₂/P₁) ≈ (h_fg/R)(1/T₁ − 1/T₂), which means P grows exponentially with 1/T (or equivalently, exponentially with temperature in a linearized approximation). For water near 100°C, saturation pressure roughly doubles for every 20°C rise — a much faster-than-linear growth. This exponential relationship is why small changes in temperature near a saturation point produce large changes in pressure, and why pressure cookers and steam turbines operate in the regimes they do."

- question: "The Clausius-Clapeyron equation can be derived by requiring that the Gibbs free energies of the two coexisting phases are equal, and that this equality must be maintained as pressure and temperature change together along the phase boundary."
  type: true-false
  answer: true
  explanation: "At any point on a phase boundary, the two phases coexist in equilibrium, which requires equal Gibbs free energies: G_liquid = G_vapor (for liquid-vapor). As we move along the boundary (changing P and T together), this equality must remain satisfied: dG_liquid = dG_vapor. Using the thermodynamic identity dG = V dP − S dT and equating the differentials gives (V_g − V_f)dP = (S_g − S_f)dT, or dp/dT = ΔS/ΔV. Substituting ΔS = h_fg/T yields the Clausius-Clapeyron equation. The derivation thus follows directly from the condition of thermodynamic equilibrium along the phase boundary."

- question: "What does the Clausius-Clapeyron equation tell us about how saturation pressure changes with temperature, and why does this make pressure cookers work more effectively at cooking food?"
  type: short-answer
  answer: "The Clausius-Clapeyron equation dp/dT = h_fg/(T·Δv) gives the slope of the liquid-vapor boundary on a P-T diagram — i.e., how much the saturation pressure changes for a given change in saturation temperature. The integrated form shows vapor pressure grows approximately exponentially with temperature. Reading this in reverse: fixing a higher pressure (by sealing the cooker) forces the boiling point to a higher temperature. Water in a sealed pressure cooker at ~2 atm does not boil until about 121°C. At this temperature, chemical reactions in food — protein denaturation, starch gelatinization, collagen breakdown — proceed much faster (reaction rates roughly double per 10°C). The food therefore cooks in a fraction of the time. Without the Clausius-Clapeyron relationship, the water would simply boil away at 100°C regardless of pressure, which would not allow higher-temperature cooking."
  explanation: "The key conceptual point: pressure and saturation temperature are linked (not independent), so imposing higher pressure imposes higher temperature for the phase transition. The Clausius-Clapeyron equation quantifies this linkage."
```

## Explainer

From your study of phase diagrams, you know that saturation pressure and saturation temperature are not independent: fix one and the other is determined. The Clausius-Clapeyron equation is the quantitative law governing that relationship — it tells you the slope of any phase boundary on a P-T diagram, expressed in terms of properties you can measure.

Deriving it requires one key idea from equilibrium thermodynamics: at a phase boundary, the **Gibbs free energy** of the two phases is equal, and this equality must remain true as you move along the boundary. Differentiating this condition and using the thermodynamic identity dG = V dP − S dT gives dp/dT = ΔS / ΔV between the phases. Substituting ΔS = h_fg / T (where h_fg is the **latent heat of vaporization** and T is the saturation temperature) yields the full Clausius-Clapeyron equation: dp/dT = h_fg / (T Δv), where Δv = v_g − v_f is the specific volume change on vaporization. The physical meaning is clear: the saturation pressure rises steeply with temperature when the latent heat is large (lots of energy in the phase transition) or the volume change is small.

For liquid-vapor transitions over a limited temperature range, Δv ≈ v_g (the liquid volume is negligible compared to vapor), and treating the vapor as ideal gas gives v_g ≈ RT/P. Substituting and integrating yields the **approximate Clausius-Clapeyron relation**: ln(P₂/P₁) ≈ (h_fg/R) × (1/T₁ − 1/T₂). This logarithmic form says that vapor pressure grows roughly exponentially with temperature — which is why a small increase in boiling temperature corresponds to a large increase in pressure, and why pressure cookers cook food faster. Water's saturation pressure roughly doubles for every 20°C rise near 100°C.

The practical reach of this equation is wide. In refrigeration and heat pump cycles, the working fluid cycles between two saturation states, and the Clausius-Clapeyron equation governs where those states sit on the P-T diagram. In meteorology, it underpins the Clausius-Clapeyron scaling of atmospheric water vapor with temperature (roughly +7% per °C warming), which drives changes in precipitation intensity with climate. In engineering property tables, tabulated saturation data is consistent with this equation — you can use it to interpolate between table entries or to check the physical consistency of a new refrigerant's properties. The equation is also the gateway to understanding the solid-liquid boundary slope: for water, Δv is slightly negative on melting (ice is less dense than water), so dp/dT is negative — ice melts under pressure, a fact that has real engineering and geophysical consequences.
