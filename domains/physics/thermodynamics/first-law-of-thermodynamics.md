---
id: first-law-of-thermodynamics
title: First Law of Thermodynamics
domain: physics
course: thermodynamics
prerequisites:
- id: work-in-thermodynamic-processes
  type: hard
- id: heat-and-internal-energy
  type: hard
- id: conservation-of-energy
  type: hard
builds-toward:
- thermodynamic-processes
- heat-engines
- heat-capacity-of-gases
tags:
- first-law
- energy-conservation
- internal-energy
- heat
- work
stage: formal-systems
status: validated
---

# First Law of Thermodynamics

## Core Idea
The First Law of Thermodynamics is energy conservation applied to thermodynamic systems: ΔU = Q − W, where ΔU is the change in internal energy, Q is heat added to the system, and W is work done by the system. Internal energy is a state function — it depends only on the current state (T, P, V) of the system, not on the path taken. Heat and work are not state functions; they describe energy transfers during a process, not stored quantities.

## How It's Best Learned
Apply the first law to several simple cases: a gas heated at constant volume (W = 0, so Q = ΔU), a gas expanded without heat exchange (Q = 0, adiabatic), and isothermal expansion of an ideal gas (ΔU = 0, so Q = W). These limiting cases build physical intuition.

## Common Misconceptions
- Internal energy is not the same as heat — heat enters or leaves, but the system contains internal energy, not 'heat'.
- The First Law does not forbid any process on energetic grounds alone; the Second Law restricts which energetically possible processes actually occur.
- ΔU = 0 for an isothermal ideal gas process does not mean Q = 0; it means Q = W.

## Questions

```yaml
- question: "An ideal gas undergoes isothermal expansion (temperature stays constant). Which statement correctly describes what happens?"
  type: multiple-choice
  options:
    - "The gas does no work because its temperature does not change"
    - "No heat flows because internal energy is a state function"
    - "The gas does positive work and an equal quantity of heat flows in"
    - "Both heat and work are zero since ΔU = 0"
  answer: 2
  explanation: "For an ideal gas, internal energy depends only on temperature. At constant T, ΔU = 0. From the First Law: ΔU = Q − W gives 0 = Q − W, so Q = W. The gas expands (positive work done by the gas, W > 0), and heat must flow in from the surroundings (Q > 0) to supply that energy. Options A and D incorrectly conclude work or heat are zero from ΔU = 0 — a direct target of the most common misconception."

- question: "Heat and internal energy are essentially the same thing — heat is just the name for the energy stored inside a system."
  type: true-false
  answer: false
  explanation: "Internal energy (U) is a state function — a property of the system's current thermodynamic state (temperature, pressure, volume). Heat (Q) is an energy transfer process, not a stored quantity. A system does not 'contain heat'; it contains internal energy. Heat describes energy crossing the boundary during a process. Conflating them is a foundational error: you can have Q = 0 with large ΔU (adiabatic work), or ΔU = 0 with large Q (isothermal expansion)."

- question: "A gas is compressed adiabatically (Q = 0). What happens to its internal energy, and why? Use the First Law explicitly."
  type: short-answer
  answer: "Internal energy increases. With Q = 0, the First Law gives ΔU = Q − W = 0 − W = −W. Compression means work is done ON the gas, so W < 0 by the system-centric sign convention (the system does negative work). Therefore ΔU = −W > 0: the internal energy — and thus the temperature — rises."
  explanation: "This is why a bicycle pump gets warm and why diesel engines ignite fuel by compression alone: adiabatic compression converts mechanical work entirely into internal energy. The sign convention is critical here — W is work done BY the system, so compression (work done ON the system) is W < 0."
```

## Explainer

The First Law of Thermodynamics is energy conservation reformulated for systems that can exchange energy in two distinct ways: heat and work. You already know energy conservation from mechanics (kinetic plus potential energy is constant in a closed system). The First Law extends that idea to include thermal energy and opens up two new channels for energy transfer.

The statement is ΔU = Q − W, where ΔU is the change in the system's internal energy, Q is heat added to the system, and W is work done by the system. The sign conventions matter enormously. Q is positive when energy flows in as heat; W is positive when the system expands and pushes on its surroundings. A compressed gas that expands (W > 0) is doing work on something external; a pump compressing a gas (W < 0) is having work done on it. Getting these signs wrong is the primary source of error in applying the First Law.

The most important conceptual distinction is between internal energy (a state function) and heat and work (process quantities). Internal energy is a property of the system right now — it depends only on temperature, pressure, and volume, not on the history of how the system got there. Heat and work, by contrast, are not properties of a state; they describe energy transfers that happen during a process. You cannot open a gas cylinder and measure how much "heat" is in the gas — you can measure its internal energy (via temperature), but the heat it absorbed over its history is no longer physically meaningful. Saying a system "contains heat" is like asking how much "walking" is in your legs.

The First Law becomes most useful when applied to limiting cases that build intuition. At constant volume (no expansion possible), W = 0 and ΔU = Q: all the heat goes directly into raising internal energy, which is why heating a gas in a rigid tank raises its temperature predictably. In an adiabatic process (insulated walls, Q = 0), ΔU = −W: any work done on the gas raises its temperature, and any work done by the gas cools it. This is why rapidly expanding gases cool (aerosol cans, refrigeration) and rapidly compressed gases heat up (diesel ignition). For isothermal expansion of an ideal gas, ΔU = 0 forces Q = W — heat flows in to exactly compensate for the work done, keeping temperature constant.

The First Law tells you what energy balance must hold, but it does not tell you which processes are physically possible. Any process satisfying ΔU = Q − W is energetically legal — including a refrigerator running backwards and spontaneously concentrating heat into a hot reservoir. The Second Law is what rules those processes out. The First Law is necessary but not sufficient for predicting which direction thermodynamic processes actually go.
