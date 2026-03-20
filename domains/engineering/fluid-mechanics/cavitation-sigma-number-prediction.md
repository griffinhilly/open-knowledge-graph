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
stage: advanced
status: draft
---

# Cavitation Number and Cavitation Prediction

## Core Idea
The cavitation number σ = (P - P_vapor)/(0.5ρV²) quantifies the margin between local pressure and vapor pressure relative to dynamic pressure. Cavitation inception occurs when σ drops below a critical value σ_i, which depends on geometry and Reynolds number. Predicting and avoiding cavitation requires monitoring inlet conditions (absolute pressure, temperature), flow velocity, and system design. The NPSH (net positive suction head) requirement of a pump must be less than NPSH available to prevent cavitation damage.

## How It's Best Learned
Set up a cavitation tunnel or pump system where inlet pressure can be reduced. Observe cavitation inception at different flow rates and speeds. Measure onset conditions and relate to cavitation number calculations. Record acoustic signals and erosion patterns to visualize cavitation bubble collapse.

## Explainer

The **cavitation number** σ = (P − P_vapor) / (½ρV²) is a dimensionless ratio that compares the margin of safety above vapor pressure against the kinetic energy per unit volume of the flow. You already know from studying Bernoulli's equation that as a fluid accelerates — around a propeller blade, through a pump impeller, or over a hydrofoil — its local pressure drops. The cavitation number tells you how close that pressure has come to the vapor pressure at which the liquid flashes into vapor. A high σ means abundant pressure margin; a low σ means the flow is approaching the threshold for bubble formation.

Cavitation inception — the onset of bubble formation — occurs when σ falls below a **critical cavitation number** σᵢ, which is a property of the flow geometry and Reynolds number. Every body shape has its own σᵢ determined by how aggressively it accelerates the flow locally. This is why streamlining a propeller blade or impeller reduces the velocity peaks, raises the minimum local pressure, and thus raises the σ required to avoid cavitation. When you know σᵢ for a design, you ensure the operating σ exceeds it with an appropriate safety margin.

For pumps and turbines, the same concept appears as **NPSH** (net positive suction head). **NPSH_available** is the absolute total head at the pump inlet minus the vapor head, calculated from the piping system: NPSH_A = (P_inlet/ρg + V²/2g) − P_vapor/ρg. **NPSH_required** is the manufacturer-specified minimum inlet head, below which cavitation will damage the impeller. Safe operation requires NPSH_A > NPSH_R, with typical practice adding a margin of 10–20%. When you lower the suction pressure (by raising the pump above the reservoir, for example), NPSH_A falls; when flow rate increases, NPSH_R increases — both effects push toward cavitation simultaneously.

Predicting cavitation in a design problem follows a checklist: determine the lowest absolute pressure in the system (often at pump inlet or the throat of a constriction using Bernoulli), compare to the vapor pressure at the operating temperature, compute σ, and compare to σᵢ. Temperature matters because vapor pressure increases rapidly with temperature — water at 100°C has P_vapor equal to atmospheric pressure, leaving zero margin for any acceleration. This is why hot-water pumps and pumps handling liquids near their boiling points are especially vulnerable and require careful NPSH analysis.
