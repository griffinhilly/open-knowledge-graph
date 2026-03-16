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

## Explainer

You know from the **second law of thermodynamics** that heat flows spontaneously from hot to cold, and that any irreversible process generates entropy. You also know from **isothermal** and **adiabatic processes** what happens to a gas during each type of step individually. The Carnot cycle chains four of these steps together in a particular order to construct the most efficient possible heat engine — and the argument for why it is most efficient is itself a proof by contradiction using the second law.

The cycle runs as follows. The gas starts at temperature T_H. Step 1 (**isothermal expansion**): the gas expands while in thermal contact with the hot reservoir at T_H, absorbing heat Q_H and doing work. Temperature stays at T_H because the process is quasi-static and isothermal. Step 2 (**adiabatic expansion**): thermal contact is broken and the gas continues expanding with no heat flow, doing more work as its temperature drops from T_H to T_C. Step 3 (**isothermal compression**): the gas is placed in contact with the cold reservoir at T_C and compressed, rejecting heat Q_C while temperature stays at T_C. Step 4 (**adiabatic compression**): thermal contact is broken again and the gas is compressed back to the starting state as temperature rises from T_C to T_H. Net result: work W = Q_H − Q_C was extracted, and the gas has returned to its initial state (it is a cycle).

The efficiency η = W/Q_H = 1 − Q_C/Q_H. For the Carnot cycle specifically, because every step is **reversible**, no entropy is generated anywhere. Entropy enters with the hot reservoir (ΔS_H = −Q_H/T_H) and leaves with the cold reservoir (ΔS_C = +Q_C/T_C). Zero net entropy means Q_H/T_H = Q_C/T_C, so Q_C/Q_H = T_C/T_H, giving **Carnot efficiency** η_C = 1 − T_C/T_H. This depends only on the two reservoir temperatures, not on the working substance.

Why is this the maximum? Suppose a better engine existed with efficiency η > η_C. Run the Carnot cycle backwards as a refrigerator (pumping heat from cold to hot using work) and power it with the hypothetical better engine. The net effect would be a machine that transfers heat from a cold reservoir to a hot one with no other effect — a violation of the second law's Clausius statement. Therefore no engine operating between T_H and T_C can exceed Carnot efficiency. The T-S diagram makes this especially clean: on T-S axes, the Carnot cycle is a perfect rectangle, net work equals the enclosed area, and the efficiency is immediately visible as (T_H − T_C)/T_H = 1 − T_C/T_H. Every real engine's cycle, when plotted on T-S axes, will have less enclosed area relative to the heat input, confirming the Carnot bound.
