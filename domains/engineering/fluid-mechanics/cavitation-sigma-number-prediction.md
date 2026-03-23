---
id: cavitation-sigma-number-prediction
title: Cavitation Number and Cavitation Prediction
domain: engineering
course: fluid-mechanics
prerequisites:
- id: cavitation-inception-vapor-formation
  type: hard
- id: bernoullis-equation
  type: soft
- id: stagnation-pressure-and-total-head
  type: soft
tags:
- cavitation
- sigma-number
- npsh
stage: formal-systems
status: validated
---

# Cavitation Number and Cavitation Prediction

## Core Idea
The cavitation number σ = (P - P_vapor)/(0.5ρV²) quantifies the margin between local pressure and vapor pressure relative to dynamic pressure. Cavitation inception occurs when σ drops below a critical value σ_i, which depends on geometry and Reynolds number. Predicting and avoiding cavitation requires monitoring inlet conditions (absolute pressure, temperature), flow velocity, and system design. The NPSH (net positive suction head) requirement of a pump must be less than NPSH available to prevent cavitation damage.

## How It's Best Learned
Set up a cavitation tunnel or pump system where inlet pressure can be reduced. Observe cavitation inception at different flow rates and speeds. Measure onset conditions and relate to cavitation number calculations. Record acoustic signals and erosion patterns to visualize cavitation bubble collapse.

## Questions

```yaml
- question: "A water pump operating at sea level (atmospheric pressure ~101 kPa) is relocated to a mountain site at 2000 m altitude where atmospheric pressure is ~80 kPa. All other installation conditions remain the same. What happens to cavitation risk?"
  type: multiple-choice
  options:
    - "Risk decreases — thinner air at altitude reduces the density of the fluid, lowering dynamic pressure"
    - "Risk increases — lower atmospheric pressure reduces NPSH_available, shrinking the margin above vapor pressure"
    - "Risk is unchanged — NPSH_required is a pump property set by the manufacturer, independent of installation"
    - "Risk decreases — the cooler temperatures at altitude reduce vapor pressure, providing more margin"
  answer: 1
  explanation: "NPSH_available = (P_inlet/ρg + V²/2g) − P_vapor/ρg. If atmospheric pressure drops by 21 kPa (≈ 2.1 m of water head), the absolute pressure at the pump inlet falls by the same amount, directly reducing NPSH_available. The vapor pressure of water at the same temperature is essentially unchanged. The safety margin against cavitation shrinks by 2.1 m of head. Option C is wrong because NPSH_required is indeed a pump property, but NPSH_available depends on the installation — and it's the comparison between the two that determines cavitation risk."

- question: "A pump handling water at 80°C (vapor pressure ≈ 47 kPa) instead of 20°C (vapor pressure ≈ 2.3 kPa) operates at the same inlet pressure. What is the primary effect on cavitation risk?"
  type: multiple-choice
  options:
    - "Risk decreases — hot water is less viscous, reducing frictional losses at the pump inlet"
    - "Risk is essentially unchanged — vapor pressure is a material property, not an operational variable"
    - "Risk increases significantly — the margin between inlet pressure and vapor pressure has shrunk by roughly 45 kPa"
    - "Risk increases slightly — higher temperature causes minor changes in fluid density"
  answer: 2
  explanation: "NPSH_available includes the term −P_vapor/ρg. At 20°C, P_vapor ≈ 2.3 kPa, contributing roughly 0.23 m to the head subtracted. At 80°C, P_vapor ≈ 47 kPa, contributing about 4.8 m. NPSH_available drops by roughly 4.6 m of head — a dramatic reduction in margin even though nothing changed about the piping system. This is why pumps handling hot fluids, boiler feed water, or liquids near their boiling points require careful NPSH analysis and often need to be positioned with significant positive suction head."

- question: "A higher cavitation number σ indicates that the system is closer to the cavitation threshold and at greater risk of bubble formation."
  type: true-false
  answer: false
  explanation: "The cavitation number σ = (P − P_vapor) / (½ρV²) measures the pressure margin above vapor pressure, normalized by dynamic pressure. A higher σ means there is more pressure 'headroom' before the local pressure drops to vapor pressure — a larger safety margin, lower cavitation risk. Cavitation inception occurs when σ falls below the critical value σᵢ. The misconception of reversing this direction is common; remember that σ is a ratio of available margin to dynamic pressure, so more is safer."

- question: "For a centrifugal pump at fixed inlet conditions, increasing the flow rate typically increases cavitation risk."
  type: true-false
  answer: true
  explanation: "Two effects combine to worsen cavitation as flow rate increases. First, NPSH_required (a property of the pump) increases with flow rate — the pump demands more inlet head to operate without cavitation at higher throughput. Second, higher flow velocities at the inlet lower local static pressure via Bernoulli's principle, reducing the actual margin above vapor pressure. Both effects simultaneously narrow the gap between NPSH_available and NPSH_required, pushing the system toward the cavitation threshold."

- question: "Why does operating temperature matter so much when assessing cavitation risk, and what physical property makes pumps handling hot fluids especially vulnerable?"
  type: short-answer
  answer: "Vapor pressure increases rapidly — and nonlinearly — with temperature. At 20°C, water's vapor pressure is about 2.3 kPa; at 100°C it equals atmospheric pressure (101 kPa). NPSH_available subtracts the vapor pressure head from the absolute inlet pressure, so higher vapor pressure directly reduces NPSH_available. For hot fluids, this subtraction becomes large, leaving little or no margin above cavitation threshold even when inlet pressures seem adequate. Pumps near the boiling point of the working fluid are most vulnerable because virtually any local pressure drop will trigger vaporization."
  explanation: "The physical mechanism is that vapor pressure represents the pressure at which the liquid spontaneously vaporizes at that temperature. Any local pressure minimum in the flow (over a blade, at a throat, around an impeller tip) that dips below vapor pressure causes immediate bubble nucleation. As temperature rises, vapor pressure rises, so the 'danger zone' of pressures expands — the entire pressure range between vapor pressure and the operating pressure becomes safe territory that shrinks with temperature."
```

## Explainer

The **cavitation number** σ = (P − P_vapor) / (½ρV²) is a dimensionless ratio that compares the margin of safety above vapor pressure against the kinetic energy per unit volume of the flow. You already know from studying Bernoulli's equation that as a fluid accelerates — around a propeller blade, through a pump impeller, or over a hydrofoil — its local pressure drops. The cavitation number tells you how close that pressure has come to the vapor pressure at which the liquid flashes into vapor. A high σ means abundant pressure margin; a low σ means the flow is approaching the threshold for bubble formation.

Cavitation inception — the onset of bubble formation — occurs when σ falls below a **critical cavitation number** σᵢ, which is a property of the flow geometry and Reynolds number. Every body shape has its own σᵢ determined by how aggressively it accelerates the flow locally. This is why streamlining a propeller blade or impeller reduces the velocity peaks, raises the minimum local pressure, and thus raises the σ required to avoid cavitation. When you know σᵢ for a design, you ensure the operating σ exceeds it with an appropriate safety margin.

For pumps and turbines, the same concept appears as **NPSH** (net positive suction head). **NPSH_available** is the absolute total head at the pump inlet minus the vapor head, calculated from the piping system: NPSH_A = (P_inlet/ρg + V²/2g) − P_vapor/ρg. **NPSH_required** is the manufacturer-specified minimum inlet head, below which cavitation will damage the impeller. Safe operation requires NPSH_A > NPSH_R, with typical practice adding a margin of 10–20%. When you lower the suction pressure (by raising the pump above the reservoir, for example), NPSH_A falls; when flow rate increases, NPSH_R increases — both effects push toward cavitation simultaneously.

Predicting cavitation in a design problem follows a checklist: determine the lowest absolute pressure in the system (often at pump inlet or the throat of a constriction using Bernoulli), compare to the vapor pressure at the operating temperature, compute σ, and compare to σᵢ. Temperature matters because vapor pressure increases rapidly with temperature — water at 100°C has P_vapor equal to atmospheric pressure, leaving zero margin for any acceleration. This is why hot-water pumps and pumps handling liquids near their boiling points are especially vulnerable and require careful NPSH analysis.
