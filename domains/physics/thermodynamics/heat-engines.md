---
id: heat-engines
title: Heat Engines
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: thermodynamic-processes
  type: hard
- id: isobaric-and-isochoric-processes
  type: soft
builds-toward:
- thermal-efficiency
- refrigerators-and-heat-pumps
- second-law-of-thermodynamics
- carnot-cycle
tags:
- heat-engine
- thermodynamic-cycle
- work-output
- hot-reservoir
- cold-reservoir
stage: formal-systems
status: validated
---
# Heat Engines

## Core Idea
A heat engine is a device that converts thermal energy into mechanical work by operating in a cycle between a hot reservoir (at temperature T_H) and a cold reservoir (at temperature T_C). In each cycle, the engine absorbs heat Q_H from the hot reservoir, converts some to work W, and rejects the remainder Q_C to the cold reservoir. By the first law for a complete cycle (ΔU = 0): W = Q_H − Q_C. No heat engine converts heat entirely into work — some is always rejected.

## How It's Best Learned
Draw an energy flow diagram (Sankey diagram) for a heat engine showing Q_H flowing in, W exiting, and Q_C flowing out. Apply this to familiar examples: steam turbines, internal combustion engines, jet engines. The constraint that Q_C > 0 is a consequence of the Second Law, not the First.

## Common Misconceptions
- A heat engine does not 'use up' heat — it degrades high-quality thermal energy into lower-quality rejected heat plus useful work.
- 100% efficiency is impossible not because of friction or practical limitations, but due to a fundamental thermodynamic principle (Second Law).

## Questions

```yaml
- question: "An inventor claims to have built a heat engine that absorbs 1000 J from a hot reservoir and converts exactly 1000 J into useful work, rejecting nothing to a cold reservoir. Which law of physics does this violate?"
  type: multiple-choice
  options:
    - "The First Law of Thermodynamics — energy is not conserved if nothing is rejected"
    - "The Second Law of Thermodynamics — complete conversion of heat to work is forbidden even when energy is conserved"
    - "Both the First and Second Laws — such a device is doubly impossible"
    - "Neither law, in principle — this would require only a perfectly frictionless engine"
  answer: 1
  explanation: "The First Law is satisfied: 1000 J in, 1000 J out as work, 0 J rejected — energy is conserved. The violation is of the Second Law, which forbids any engine from converting heat entirely into work in a cyclic process. Such a device would be a perpetual motion machine of the second kind. The Second Law is about direction and quality of energy, not quantity — heat cannot be fully upgraded to work without rejecting some to a cold reservoir, regardless of engineering perfection."

- question: "A heat engine absorbs Q_H = 800 J from its hot reservoir in one cycle and does W = 300 J of mechanical work. How much heat Q_C is rejected to the cold reservoir?"
  type: multiple-choice
  options:
    - "300 J — the rejected heat equals the work output"
    - "500 J — the rejected heat equals Q_H minus W"
    - "800 J — all the absorbed heat must eventually be rejected to maintain the cycle"
    - "It cannot be determined without knowing the temperatures of the reservoirs"
  answer: 1
  explanation: "For a complete cycle, ΔU = 0 (the working substance returns to its initial state). The first law gives W = Q_H − Q_C, so Q_C = Q_H − W = 800 − 300 = 500 J. The energy flow is: 800 J in from the hot reservoir, 300 J out as work, 500 J out to the cold reservoir. These three quantities always satisfy Q_H = W + Q_C. The temperature information determines maximum efficiency but not the energy balance, which follows from the first law alone."

- question: "For a heat engine operating in a complete thermodynamic cycle, the change in internal energy of the working substance over one full cycle is zero."
  type: true-false
  answer: true
  explanation: "This is the key property of a cyclic process: after one complete cycle, the working substance (steam, gas, etc.) returns to exactly its original thermodynamic state — same temperature, pressure, and volume. Internal energy is a state function, so ΔU = 0 for any process that returns to the starting state. This is what allows the First Law to simplify to W = Q_H − Q_C for a full cycle, making the energy accounting straightforward."

- question: "A sufficiently well-engineered heat engine — one with perfectly smooth bearings, no friction losses, and ideal gas behavior — could in principle achieve 100% thermal efficiency."
  type: true-false
  answer: false
  explanation: "100% efficiency requires Q_C = 0: all absorbed heat converted to work with nothing rejected. The Second Law of Thermodynamics forbids this regardless of engineering quality. It is not a matter of friction or practical limitations — a completely frictionless, ideal engine still must reject heat to a cold reservoir. The fundamental reason is that heat naturally flows from hot to cold, and completely reversing this direction for all the energy in the system is thermodynamically prohibited. The Carnot efficiency 1 − T_C/T_H gives the absolute maximum, which is always less than 1 whenever T_C > 0 K."

- question: "A heat engine operates between two reservoirs with no friction and ideal thermodynamic processes. Explain why it still cannot convert all absorbed heat into work — what fundamental principle prevents 100% efficiency?"
  type: short-answer
  answer: "The Second Law of Thermodynamics requires that any cyclic process transferring energy from a hot reservoir must reject some heat to a cold reservoir. A complete conversion would require entropy to decrease in the universe — which the Second Law forbids. Equivalently, such a device would be a perpetual motion machine of the second kind: it would spontaneously convert disordered thermal energy (heat) entirely into ordered mechanical energy (work) without any compensating change elsewhere. The direction of heat flow — always from hot to cold — is itself the Second Law's content, and no engineering improvement can circumvent it."
  explanation: "This is fundamentally different from the First Law. The First Law (energy conservation) is satisfied by a 100%-efficient engine: energy in = energy out. The Second Law adds a constraint on the direction and quality of that energy transformation. The Carnot efficiency 1 − T_C/T_H shows that efficiency approaches 1 only as T_C → 0 K (absolute zero) or T_H → ∞, neither of which is physically achievable. Real engines fall short even of this theoretical maximum due to irreversibilities."
```

## Explainer

From the first law of thermodynamics, you know that energy is conserved: ΔU = Q − W for any process. A heat engine is a device that exploits this relationship cyclically. "Cyclically" is the key word — after one full cycle, the working substance (steam, gas, or whatever) returns to its original state, so ΔU = 0 for the full cycle. The first law then gives W = Q_net = Q_H − Q_C: the net work output equals the heat absorbed from the hot reservoir minus the heat rejected to the cold reservoir. This is not an approximation or an idealization — it is just energy conservation.

The efficiency η = W/Q_H = 1 − Q_C/Q_H measures how much of the input heat is converted to useful work. The constraint Q_C > 0 (some heat must always be rejected) is not a consequence of friction or engineering imperfection — it is required by the Second Law. A machine that absorbed Q_H and converted all of it to work would be a **perpetual motion machine of the second kind**, impossible not because it violates energy conservation (the first law is satisfied) but because it would require heat to flow spontaneously from cold to hot or entropy to decrease. The direction of heat flow — always from hot to cold — is itself the Second Law's content.

Visualizing the engine as an energy flow diagram helps: Q_H flows into the engine from the hot reservoir, the engine outputs W upward (as mechanical work, electricity, or other useful forms), and Q_C flows downward to the cold reservoir. The three quantities satisfy Q_H = W + Q_C at all times. Common real engines — steam turbines in power plants, the gasoline engine in a car, jet engines in aircraft — all fit this template. In a car engine, the hot reservoir is the burning fuel mixture (~2000 K), the cold reservoir is the exhaust (~700 K), and W drives the crankshaft. The actual efficiency of a car engine (typically 20–35%) is much less than the theoretical maximum because of friction, non-ideal processes, and heat losses.

The theoretical maximum efficiency for any engine operating between T_H and T_C is the **Carnot efficiency** η_Carnot = 1 − T_C/T_H, which you will derive when studying the Carnot cycle. The Carnot limit shows that efficiency increases as the temperature ratio T_H/T_C grows larger. This is why power plant engineers work hard to raise steam temperatures (T_H) and use cooling towers to lower rejection temperatures (T_C) — every degree of improvement in the ratio means more work out per unit of fuel consumed.
