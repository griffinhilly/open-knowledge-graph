---
id: rayleigh-line-flow-stagnation-conditions
title: 'Rayleigh Line Flow: Constant Area with Heat Transfer'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
- id: isentropic-nozzle-flow-choked-conditions
  type: soft
tags:
- heat-transfer
- constant-area
- stagnation
stage: advanced
status: draft
---

# Rayleigh Line Flow: Constant Area with Heat Transfer

## Core Idea
Rayleigh line analysis describes constant-area flow with heat transfer and friction, common in combustor and afterburner flow. Heat addition increases stagnation temperature and pressure, causing stagnation pressure loss due to irreversibility. Velocity changes to satisfy continuity; subsonic flow can be accelerated to sonic conditions by sufficient heat addition. This model applies to engines and industrial combustion systems where geometry and heat input control flow behavior.

## Explainer

In isentropic nozzle flow — your prerequisite — the mechanism changing velocity is area change, with no heat transfer. Rayleigh line analysis poses a different question: what happens when you add heat to a gas flowing through a **constant-area duct**? Area cannot change to accommodate the altered thermodynamic state, so pressure and velocity must do the adjusting instead. The result is a model directly relevant to combustion chambers, jet engine afterburners, and any industrial system where flame or external heat exchange occurs in a duct of fixed cross-section.

The governing constraints are mass conservation (ρV = constant in constant area), momentum (p + ρV² = constant), and the thermodynamic energy equation that connects heat addition to stagnation temperature rise: q = cₚ(T₀₂ − T₀₁). These constraints trace a curve in the T–s or p–V plane called the **Rayleigh line**. The curve has two branches — one subsonic and one supersonic — that both end at M = 1. Heat addition always moves the state toward M = 1 (called **thermal choking**): adding heat to subsonic flow accelerates it (increases M); adding heat to supersonic flow decelerates it (decreases M toward 1). This is the opposite of what intuition about "heating a gas" might suggest in the supersonic case.

The key insight about stagnation pressure is that heat addition is irreversible from a thermodynamic standpoint (it increases entropy), so **stagnation pressure always decreases** when heat is added, regardless of whether the flow is subsonic or supersonic. This is distinct from isentropic flow, where stagnation pressure is conserved. The stagnation temperature, by contrast, increases in exact proportion to the heat added per unit mass. For combustor design, this means the engineer faces an unavoidable tradeoff: adding fuel energy to accelerate the exhaust jet necessarily incurs a stagnation pressure penalty that reduces the thermodynamic efficiency of the cycle.

Thermal choking is the operational limit. If a combustor attempts to add more heat than the **critical** amount (which would bring M to exactly 1 at the exit), the flow cannot accommodate the additional energy within the given duct: a shock system moves upstream and changes the entire flow structure, potentially "unstarting" the engine. The critical heat addition is tabulated from Rayleigh relations as a function of inlet Mach number, giving designers a hard limit on fuel-air ratio for a given combustor geometry and inlet condition. This connects directly to afterburner design, where throttleable heat addition must stay below the thermal choking limit across the full operating envelope.
