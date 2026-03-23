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
stage: formal-systems
status: draft
---

# Rayleigh Line Flow: Constant Area with Heat Transfer

## Core Idea
Rayleigh line analysis describes constant-area flow with heat transfer and friction, common in combustor and afterburner flow. Heat addition increases stagnation temperature and pressure, causing stagnation pressure loss due to irreversibility. Velocity changes to satisfy continuity; subsonic flow can be accelerated to sonic conditions by sufficient heat addition. This model applies to engines and industrial combustion systems where geometry and heat input control flow behavior.

## Questions

```yaml
- question: "Heat is added to a supersonic flow (M > 1) in a constant-area duct. What happens to the Mach number?"
  type: multiple-choice
  options:
    - "It increases further above 1, because adding energy always accelerates the flow"
    - "It decreases toward 1, because heat addition in a constant-area duct drives all flows toward M = 1"
    - "It stays constant, because constant area means constant velocity"
    - "It first increases then decreases, passing through a maximum before settling at M = 1"
  answer: 1
  explanation: "This is the most counterintuitive result in Rayleigh flow: heat addition decelerates supersonic flow. All flows in a constant-area duct with heat addition move toward M = 1, whether they start subsonic (M increases toward 1) or supersonic (M decreases toward 1). This follows from the Rayleigh line — the locus of states satisfying mass and momentum conservation in constant-area flow — which has its maximum entropy point at M = 1. Heat addition always increases entropy, so the flow must move along the Rayleigh line toward its entropy maximum at M = 1."

- question: "An engine combustor adds heat to subsonic inlet flow. The combustor is designed for a maximum exit Mach number of 0.5, but significantly more fuel is added than planned. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "The exit Mach number rises above 0.5 but remains subsonic with no other effects"
    - "The stagnation pressure increases, providing more thrust"
    - "The flow approaches thermal choking (M = 1), and adding more fuel beyond this point moves a shock upstream, potentially disrupting the inlet flow"
    - "The flow becomes supersonic at the exit, improving combustion efficiency"
  answer: 2
  explanation: "Thermal choking occurs when heat addition drives the exit Mach number to exactly M = 1. Beyond the critical heat addition, the constant-area duct cannot accommodate more energy for the given mass flow and inlet conditions — the governing equations have no solution. The physical consequence is that a shock system is displaced upstream, altering the inlet flow and potentially 'unstarting' the engine. This is a hard operational limit in combustor design — not a gradual degradation but a discontinuous change in flow structure."

- question: "Adding heat to a flow in a constant-area duct always increases the stagnation temperature and decreases the stagnation pressure, regardless of whether the flow is subsonic or supersonic."
  type: true-false
  answer: true
  explanation: "Stagnation temperature T₀ increases in direct proportion to the heat added per unit mass (q = cₚ·ΔT₀), regardless of Mach number — this follows from the first law of thermodynamics. Stagnation pressure always decreases because heat addition is thermodynamically irreversible (it generates entropy), and entropy generation corresponds to stagnation pressure loss. This contrasts with isentropic flow, where stagnation pressure is conserved. The stagnation pressure loss is an unavoidable performance penalty for any combustion-based propulsion system."

- question: "In Rayleigh flow, heat addition accelerates subsonic flow for the same reason that a converging nozzle accelerates subsonic flow: both are driven by an effective reduction in available cross-sectional area."
  type: true-false
  answer: false
  explanation: "The two mechanisms are physically distinct. In an isentropic converging nozzle, area decrease directly causes acceleration via continuity (smaller area requires higher velocity for the same mass flow). In Rayleigh flow, the area is constant — there is no area change. Acceleration is instead caused by the pressure change required to satisfy both momentum and mass conservation simultaneously when stagnation temperature rises. The processes are not equivalent: isentropic nozzle flow conserves stagnation pressure, while Rayleigh flow with heat addition always loses stagnation pressure due to irreversibility."

- question: "Explain the 'thermal choking' limit in Rayleigh flow: why can adding heat beyond a critical amount not be accommodated within the duct, and what physically happens when this limit is exceeded?"
  type: short-answer
  answer: "The Rayleigh line — the curve of states satisfying mass and momentum conservation in constant-area flow — has its maximum entropy point at M = 1. Each state on the curve corresponds to a unique stagnation temperature. As heat is added, the flow's state moves along the Rayleigh line toward M = 1, with each heat increment corresponding to a specific stagnation temperature increment. When the exit reaches M = 1, the duct has consumed its entire budget of entropy increase available for these inlet conditions. Adding more heat has no solution on the Rayleigh line for the same mass flow and momentum. Physically, the flow adjusts upstream: a normal shock moves into the inlet, reducing the mass flow rate until the remaining flow can again reach thermal choking at the exit under the new conditions."
  explanation: "This is analogous to choked flow in a converging nozzle: once the throat reaches M = 1, further downstream changes cannot propagate upstream, and the nozzle is choked. In Rayleigh flow, the analogous limit is entropy-based: the constant-area duct can only accommodate a finite entropy increase for given inlet conditions. Attempting to exceed this moves the effective choking point upstream, restructuring the entire flow."
```

## Explainer

In isentropic nozzle flow — your prerequisite — the mechanism changing velocity is area change, with no heat transfer. Rayleigh line analysis poses a different question: what happens when you add heat to a gas flowing through a **constant-area duct**? Area cannot change to accommodate the altered thermodynamic state, so pressure and velocity must do the adjusting instead. The result is a model directly relevant to combustion chambers, jet engine afterburners, and any industrial system where flame or external heat exchange occurs in a duct of fixed cross-section.

The governing constraints are mass conservation (ρV = constant in constant area), momentum (p + ρV² = constant), and the thermodynamic energy equation that connects heat addition to stagnation temperature rise: q = cₚ(T₀₂ − T₀₁). These constraints trace a curve in the T–s or p–V plane called the **Rayleigh line**. The curve has two branches — one subsonic and one supersonic — that both end at M = 1. Heat addition always moves the state toward M = 1 (called **thermal choking**): adding heat to subsonic flow accelerates it (increases M); adding heat to supersonic flow decelerates it (decreases M toward 1). This is the opposite of what intuition about "heating a gas" might suggest in the supersonic case.

The key insight about stagnation pressure is that heat addition is irreversible from a thermodynamic standpoint (it increases entropy), so **stagnation pressure always decreases** when heat is added, regardless of whether the flow is subsonic or supersonic. This is distinct from isentropic flow, where stagnation pressure is conserved. The stagnation temperature, by contrast, increases in exact proportion to the heat added per unit mass. For combustor design, this means the engineer faces an unavoidable tradeoff: adding fuel energy to accelerate the exhaust jet necessarily incurs a stagnation pressure penalty that reduces the thermodynamic efficiency of the cycle.

Thermal choking is the operational limit. If a combustor attempts to add more heat than the **critical** amount (which would bring M to exactly 1 at the exit), the flow cannot accommodate the additional energy within the given duct: a shock system moves upstream and changes the entire flow structure, potentially "unstarting" the engine. The critical heat addition is tabulated from Rayleigh relations as a function of inlet Mach number, giving designers a hard limit on fuel-air ratio for a given combustor geometry and inlet condition. This connects directly to afterburner design, where throttleable heat addition must stay below the thermal choking limit across the full operating envelope.
