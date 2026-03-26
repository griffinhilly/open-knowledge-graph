---
id: mach-number-speed-of-sound-compressibility
title: 'Mach Number and Speed of Sound: Compressibility Effects'
domain: engineering
course: fluid-mechanics
prerequisites:
- id: compressible-flow-basics
  type: hard
- id: fluid-properties-and-continuum
  type: soft
builds-toward:
- isentropic-nozzle-flow-choked-conditions
- rayleigh-line-flow-stagnation-conditions
tags:
- mach
- compressibility
- sound
stage: formal-systems
status: validated
---

# Mach Number and Speed of Sound: Compressibility Effects

## Core Idea
The Mach number M = V/a is the ratio of fluid velocity to local speed of sound a = √(γRT) for an ideal gas. For M < 0.3, compressibility effects are typically negligible and incompressible flow assumptions apply. As M increases, density variations become significant and require modification to continuity, momentum, and energy equations. Subsonic (M < 1), transonic (M ≈ 1), and supersonic (M > 1) regimes exhibit qualitatively different behavior.

## How It's Best Learned
Calculate Mach numbers for air flows at different velocities (sea-level and altitude) to understand the speeds at which compressibility becomes important. Solve subsonic and supersonic nozzle problems to see how area, Mach, and pressure relate differently in each regime.

## Questions

```yaml
- question: "A converging-diverging rocket nozzle must accelerate exhaust gas to supersonic speeds. After the throat (where M = 1), what shape is needed to continue accelerating the flow, and why?"
  type: multiple-choice
  options:
    - "Converging (decreasing area), because reducing cross-section always increases velocity by continuity"
    - "Diverging (increasing area), because for M > 1 the area-velocity relation reverses — larger area accelerates supersonic flow"
    - "Constant area, because the throat already established the maximum achievable Mach number"
    - "Converging then diverging again, to create a normal shock that re-accelerates the flow"
  answer: 1
  explanation: "The area-velocity relation for isentropic flow is dA/A = (M² − 1) dV/V. For M < 1, (M² − 1) < 0, so decreasing area (dA < 0) produces increasing velocity (dV > 0) — the familiar converging-nozzle behavior. For M > 1, (M² − 1) > 0, so increasing area (dA > 0) also produces increasing velocity. This reversal is a purely compressible flow effect — it cannot be derived from incompressible Bernoulli. The de Laval (converging-diverging) nozzle is the direct engineering application: converging section accelerates the flow to M = 1 at the throat, then the diverging section continues accelerating it supersonically."

- question: "An engineer uses incompressible Bernoulli's equation to calculate the lift on an aircraft wing. At what flight condition does this approximation first become significantly inaccurate?"
  type: multiple-choice
  options:
    - "Any speed above sea-level standard conditions, because the atmosphere is never perfectly incompressible"
    - "Around M = 0.3, where density changes from stagnation to local conditions reach roughly 5% — the standard engineering threshold for compressibility effects"
    - "Exactly at M = 1.0, when shock waves first appear and fundamentally change the flow"
    - "Above M = 2.0, where supersonic effects fully dominate and linearized approximations fail"
  answer: 1
  explanation: "At M = 0.3, the isentropic density ratio gives roughly 5% density variation from freestream to stagnation — a common engineering threshold for 'acceptable' incompressibility error. Below M = 0.3, treating density as constant introduces less than 5% error in pressure coefficients. Above M = 0.3, errors grow as M², and near M = 1 they become unbounded. The threshold is not M = 1 because compressibility effects are not suddenly 'switched on' — they grow continuously. Commercial aircraft cruise at M ≈ 0.82, well above the incompressible regime, requiring full compressible flow analysis."

- question: "At Mach numbers below 1, a pressure disturbance generated at an aircraft's nose can propagate upstream and warn the oncoming air to divert before the aircraft arrives."
  type: true-false
  answer: true
  explanation: "True. The speed of sound is the speed at which pressure information travels through a medium. When M < 1, the aircraft moves slower than its own pressure signals, so disturbances propagate upstream ahead of the aircraft. The approaching air 'feels' the pressure field and begins to divert before it reaches the aircraft. This upstream communication is what allows the smooth, attached flow around wings at subsonic speeds. When M > 1, the aircraft outruns its own pressure signals — no upstream warning is possible, and the air encounters the aircraft with no prior adjustment, requiring the abrupt property changes of a shock wave."

- question: "A diverging nozzle section usually decelerates a flow because the larger cross-sectional area reduces velocity by conservation of mass, just as water slows in a widening river."
  type: true-false
  answer: false
  explanation: "False for supersonic flow. For incompressible flow (or subsonic compressible flow), continuity ρAV = constant with approximately constant ρ does give A↑ → V↓. But for supersonic compressible flow (M > 1), density decreases so rapidly as the flow accelerates that the mass flux balance requires the cross-sectional area to increase as velocity increases. The area-velocity relation dA/A = (M² − 1) dV/V changes sign at M = 1. The river analogy fails because it assumes incompressible flow. A diverging nozzle after a supersonic throat accelerates the flow — the opposite of the incompressible intuition."

- question: "Explain why the Mach number, not the absolute velocity, is the fundamental parameter that determines compressible flow behavior. Why can two flows at the same velocity but different temperatures be in different flow regimes?"
  type: short-answer
  answer: "The Mach number M = V/a measures velocity relative to the speed of sound a = √(γRT), which is the speed at which pressure information propagates. What matters physically is not how fast the flow moves in absolute terms, but whether it moves faster or slower than pressure disturbances can travel. At the same airspeed, cold air (lower T) has a lower speed of sound, giving a higher Mach number — potentially supersonic — while warm air (higher T) at the same airspeed might still be subsonic. The qualitative physics (shock formation, upstream communication, area-velocity behavior) all flip at M = 1 regardless of the absolute velocity. Mach number is the only quantity that determines which flow regime and which governing equation structure applies."
  explanation: "This is why aircraft reach supersonic flight more easily at high altitude: cold stratospheric air has a lower speed of sound (~295 m/s at 11 km) than sea-level air (~343 m/s), so the same airspeed corresponds to a higher Mach number at altitude. The Concorde cruised at M = 2 at ~55,000 ft. At sea level, the same airspeed would be M ≈ 1.7 — still supersonic, but the lower Mach number means weaker shocks and different aerodynamic properties."
```

## Explainer

In most of the fluid problems you have solved so far, density has been a constant. Water is incompressible for all practical purposes, and slow-moving air behaves the same way — the pressures involved are small compared to atmospheric pressure, so density barely changes. The Mach number is the ratio that tells you when to abandon this assumption. It does not measure absolute speed; it measures how fast the flow is moving relative to the medium's own ability to transmit pressure disturbances.

The **speed of sound** a = √(γRT) is a property of the gas, not of the flow. It is the speed at which a small pressure disturbance — a tap on a drum, a conversation, an airplane's pressure wave — propagates through the medium. For air at sea level (T ≈ 293 K, γ = 1.4), a ≈ 343 m/s. At altitude where air is colder, a is lower, which is why aircraft reach supersonic flight more easily at altitude even at the same airspeed. The **Mach number** M = V/a measures whether the flow is slower or faster than this information-propagation speed.

When M < 1, pressure disturbances can run upstream ahead of the flow and warn the fluid that an obstacle is coming. The gas has time to adjust — diverting smoothly around wings and through nozzles. When M > 1, the flow outpaces its own pressure signals. No upstream warning is possible. Information piles up at the nose of an obstacle, forming a **shock wave** — an extremely thin region of near-discontinuous property changes. Across a shock, pressure, temperature, and density jump abruptly while velocity drops. This is a qualitatively different regime, not just a quantitative extension of subsonic behavior.

The threshold M < 0.3 for "incompressible" comes from the isentropic relation for density change: at M = 0.3, density varies by about 5% compared to the stagnation condition — usually acceptable engineering error. As M increases toward 1.0, density variations grow rapidly, and the incompressible Bernoulli equation gives increasingly wrong answers. The **area-velocity relation** for isentropic flow is dA/A = (M² − 1) dV/V. For M < 1, this is negative — a converging nozzle accelerates flow. For M > 1, it is positive — a *diverging* section accelerates supersonic flow. This counterintuitive reversal is the key result of compressible nozzle theory.

Near M = 1.0 (the transonic regime), the flow becomes especially sensitive to geometry. Supersonic patches form locally on airfoils at freestream speeds well below Mach 1 — one reason commercial aircraft are designed to cruise at M ≈ 0.82–0.85 rather than pushing to 0.95. The governing equations change mathematical type (from elliptic to hyperbolic) at M = 1, which is why a new set of analytical tools — method of characteristics, shock relations, isentropic flow tables — is needed for supersonic design. Mach number is the single parameter that determines which regime governs, and every result in compressible flow ultimately branches on whether M is below, at, or above unity.
