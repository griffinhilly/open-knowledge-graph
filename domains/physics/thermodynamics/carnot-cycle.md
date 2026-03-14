---
id: carnot-cycle
title: The Carnot Cycle
domain: physics
course: thermodynamics
prerequisites:
- id: isothermal-processes
  type: hard
- id: adiabatic-processes
  type: hard
- id: second-law-of-thermodynamics
  type: hard
builds-toward:
- carnot-efficiency
tags:
- Carnot
- reversible-cycle
- ideal-engine
- isothermal
- adiabatic
- thermodynamic-cycle
stage: formal-systems
status: validated
---

# The Carnot Cycle

## Core Idea
The Carnot cycle is the most efficient possible thermodynamic cycle operating between two temperatures T_H and T_C. It consists of four reversible steps: (1) isothermal expansion at T_H (absorbs Q_H), (2) adiabatic expansion (temperature drops to T_C), (3) isothermal compression at T_C (rejects Q_C), (4) adiabatic compression (temperature returns to T_H). Because every step is reversible, the Carnot cycle generates no net entropy. It is an idealization — real cycles are irreversible and less efficient.

## How It's Best Learned
Sketch the Carnot cycle on both a PV diagram and a TS (temperature-entropy) diagram. On the TS diagram, the cycle is a perfect rectangle, making it immediately clear that the enclosed area represents net work and the efficiency depends only on the two temperatures.

## Common Misconceptions
- The Carnot cycle is not a practical engine design — it requires infinitely slow quasi-static processes and produces zero power (work per unit time) in the limit.
- Reversibility in the Carnot cycle means the cycle can run forwards as an engine or backwards as a refrigerator with no entropy generated either way.
