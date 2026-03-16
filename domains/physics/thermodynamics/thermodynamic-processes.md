---
id: thermodynamic-processes
title: Thermodynamic Processes and the PV Diagram
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: ideal-gas-law
  type: hard
builds-toward:
- isothermal-processes
- adiabatic-processes
- isobaric-and-isochoric-processes
- heat-engines
tags:
- PV-diagram
- thermodynamic-processes
- isothermal
- adiabatic
- isobaric
- isochoric
stage: formal-systems
status: validated
---

# Thermodynamic Processes and the PV Diagram

## Core Idea
A thermodynamic process describes how a system transitions between equilibrium states, typically represented on a P-V (pressure-volume) diagram. The four idealized processes are: isothermal (constant T), adiabatic (Q = 0), isobaric (constant P), and isochoric or isovolumetric (constant V). Each traces a distinct curve on the PV diagram with a specific relationship between Q, W, and ΔU. Real engines and refrigerators approximate combinations of these idealized processes.

## How It's Best Learned
Sketch all four process types on a single PV diagram starting from the same state. For each, identify which terms in ΔU = Q − W are zero and compute the others. This visual fluency on PV diagrams is essential for analyzing heat engines.

## Common Misconceptions
- An adiabatic process is not isothermal — in an adiabatic expansion the temperature drops because work is done with no heat input.
- Isothermal does not mean no work or no heat — for an ideal gas, Q = W in an isothermal process since ΔU = 0.

## Questions

```yaml
- question: "An ideal gas undergoes isothermal expansion. Which relationship correctly describes the heat Q, work W, and internal energy change ΔU for this process?"
  type: multiple-choice
  options:
    - "Q = 0 and W = 0, so ΔU = 0"
    - "ΔU = 0 and Q = W, so heat absorbed equals work done by the gas"
    - "Q = 0 and W = −ΔU, so work comes entirely from internal energy"
    - "ΔU > 0 and Q = 0, so all work input goes into internal energy"
  answer: 1
  explanation: "For an ideal gas, internal energy depends only on temperature. If temperature is constant (isothermal), ΔU = 0. The first law then gives 0 = Q − W, so Q = W. The gas does absorb heat — that heat is entirely converted into work done on the surroundings. This is why isothermal ≠ Q = 0."

- question: "An adiabatic expansion of an ideal gas necessarily occurs at constant temperature."
  type: true-false
  answer: false
  explanation: "Adiabatic means Q = 0, not T = constant. With no heat input, the first law gives ΔU = −W. When the gas expands and does positive work on its surroundings, its internal energy decreases — and for an ideal gas, that means temperature drops. Adiabatic and isothermal are distinct processes; conflating them is a common error."

- question: "On a PV diagram, why is an adiabatic curve steeper than an isothermal curve passing through the same point?"
  type: short-answer
  answer: "For an isothermal process, PV = constant, giving a slope of −P/V. For an adiabatic process, PV^γ = constant (where γ = Cp/Cv > 1), giving a slope of −γP/V. Since γ > 1, the adiabatic curve falls more steeply. Physically, in an adiabatic expansion the temperature drops (no heat input), so pressure falls faster than it would at constant temperature."
  explanation: "The steepness difference is a direct consequence of the adiabatic temperature drop. On an isothermal curve, T stays fixed so the ideal gas law keeps pressure proportional to 1/V. On the adiabatic, the gas cools as it expands, compounding the pressure drop — hence the steeper descent."
```

## Explainer

You already know the first law of thermodynamics — ΔU = Q − W — and the ideal gas law PV = nRT. Thermodynamic processes are where these two equations meet: they describe specific paths a gas can take as it changes state, and each path has a different signature for how Q, W, and ΔU relate to one another.

The PV diagram is the essential visual tool. Plot pressure on the vertical axis and volume on the horizontal axis. Every equilibrium state of a gas is a point on this diagram, and every quasi-static process is a curve connecting two points. The area under the curve on a PV diagram equals the work done by the gas during that process — a geometric fact you should internalize, because it makes comparing processes visual and immediate.

The four idealized processes each constrain one variable. In an **isochoric** (constant volume) process, the curve is a vertical line; no volume change means no work done, so ΔU = Q entirely. In an **isobaric** (constant pressure) process, the curve is horizontal; work W = PΔV, and both Q and ΔU are generally nonzero. In an **isothermal** process, temperature is fixed, so for an ideal gas ΔU = 0 and Q = W — heat flows in and is entirely converted to work. In an **adiabatic** process, no heat is exchanged (Q = 0), so any work done comes at the cost of internal energy: ΔU = −W. A gas expanding adiabatically cools, which is why diesel engines ignite fuel without a spark — the adiabatic compression heats the air enough to combust.

A common trap: students hear "isothermal" and assume no heat flows, or hear "adiabatic" and assume constant temperature. The names are clues: "iso-thermal" means same temperature; "a-diabatic" means no heat passage (from the Greek for "not passable"). Keep these definitions sharp. On a PV diagram, the adiabatic curve through any point is always steeper than the isothermal curve through the same point, because in an adiabatic expansion the temperature falls, causing pressure to drop faster than it would at constant temperature.

Real engines — the Carnot cycle, diesel engines, refrigerators — are sequences of these four idealized processes stitched together. The enclosed area on a PV diagram for a complete cycle equals the net work output of the engine. Building fluency with individual process types now is what makes heat engine analysis tractable later.
