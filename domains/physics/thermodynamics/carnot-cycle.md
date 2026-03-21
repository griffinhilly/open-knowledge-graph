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

## Questions

```yaml
- question: "A Carnot engine operates between a hot reservoir at 800 K and a cold reservoir at 200 K. If the working substance is changed from an ideal gas to steam, what happens to the efficiency?"
  type: multiple-choice
  options:
    - "Efficiency increases because steam has a higher heat capacity and can absorb more heat"
    - "Efficiency decreases because steam is harder to compress at low temperatures"
    - "Efficiency stays the same — Carnot efficiency depends only on the two reservoir temperatures"
    - "Efficiency changes because reversibility depends on the properties of the working substance"
  answer: 2
  explanation: "The Carnot efficiency η_C = 1 − T_C/T_H depends only on the temperatures of the two reservoirs, not on the working substance. For 800 K and 200 K, η_C = 1 − 200/800 = 75%, regardless of whether the working fluid is an ideal gas, steam, or any other substance. This follows from the derivation: because every step is reversible, zero entropy is generated, and the entropy bookkeeping gives Q_C/Q_H = T_C/T_H — a relation involving only temperatures. The identity of the working substance never enters."

- question: "An inventor claims to have built a heat engine that operates between reservoirs at 1000 K and 300 K and achieves 80% efficiency. The maximum Carnot efficiency between these temperatures is 70%. What does thermodynamics say about this claim?"
  type: multiple-choice
  options:
    - "The claim is plausible if the working substance is chosen carefully enough"
    - "The claim is impossible — it would allow construction of a device that transfers heat from cold to hot with no other effect, violating the second law"
    - "The claim is fine as long as the engine operates slowly enough to be quasi-static"
    - "The claim could work if the engine uses an irreversible process that generates negative entropy"
  answer: 1
  explanation: "No engine operating between two temperatures can exceed Carnot efficiency. The proof is by contradiction: if such an engine existed, you could run a Carnot refrigerator (powered by this engine) that pumps more heat from cold to hot than the engine requires. The net result would be spontaneous heat flow from cold to hot — the Clausius violation. Entropy cannot be negative, and real engines generate additional entropy through irreversibility, pushing them further below the Carnot limit."

- question: "The Carnot cycle is the most efficient practical engine design and should be used whenever maximum efficiency is required."
  type: true-false
  answer: false
  explanation: "The Carnot cycle is a theoretical ideal, not a practical design. Its steps must be quasi-static (infinitely slow) to remain reversible. In the limit of reversibility, the power output — work per unit time — approaches zero. A perfectly efficient engine that produces no power is useless for engineering. Real engines sacrifice some thermodynamic efficiency to operate at finite speed and deliver actual power. Carnot efficiency is a theoretical upper bound, not an engineering blueprint."

- question: "In a Carnot cycle, because every step is reversible, the total entropy of the universe does not change — the entropy gained from the hot reservoir exactly equals the entropy delivered to the cold reservoir."
  type: true-false
  answer: true
  explanation: "Reversibility is precisely defined as producing no net entropy. In the Carnot cycle: the hot reservoir loses entropy ΔS_H = −Q_H/T_H (heat flows out), and the cold reservoir gains entropy ΔS_C = +Q_C/T_C (heat flows in). Since no entropy is generated internally, total entropy change is zero, which requires Q_H/T_H = Q_C/T_C. This relationship is the key step in deriving the Carnot efficiency formula η_C = 1 − T_C/T_H. Real engines generate entropy internally (due to friction, heat flow across finite temperature differences, etc.), so Q_C/Q_H > T_C/T_H, and their efficiency falls below Carnot."

- question: "Why does the efficiency of a Carnot cycle depend only on the two reservoir temperatures and not on the nature of the working substance or the details of the cycle steps?"
  type: short-answer
  answer: "Because the Carnot cycle is reversible at every step, no entropy is generated anywhere in the cycle. The only entropy changes are the heat exchanges with the reservoirs: entropy flows in from the hot reservoir (Q_H/T_H) and flows out to the cold reservoir (Q_C/T_C). Zero net entropy change requires these to be equal: Q_H/T_H = Q_C/T_C. This relation — derived purely from the constraint of reversibility — gives Q_C/Q_H = T_C/T_H, and therefore efficiency η = 1 − Q_C/Q_H = 1 − T_C/T_H. The working substance never appears in this argument."
  explanation: "The T-S diagram makes this especially vivid: the Carnot cycle is a perfect rectangle on T-S axes. The heat absorbed is the area under the top edge (Q_H = T_H × ΔS), the heat rejected is the area under the bottom edge (Q_C = T_C × ΔS), and the net work is the enclosed area. The ratio Q_C/Q_H = T_C/T_H follows immediately from the geometry of the rectangle."
```

## Explainer

You know from the **second law of thermodynamics** that heat flows spontaneously from hot to cold, and that any irreversible process generates entropy. You also know from **isothermal** and **adiabatic processes** what happens to a gas during each type of step individually. The Carnot cycle chains four of these steps together in a particular order to construct the most efficient possible heat engine — and the argument for why it is most efficient is itself a proof by contradiction using the second law.

The cycle runs as follows. The gas starts at temperature T_H. Step 1 (**isothermal expansion**): the gas expands while in thermal contact with the hot reservoir at T_H, absorbing heat Q_H and doing work. Temperature stays at T_H because the process is quasi-static and isothermal. Step 2 (**adiabatic expansion**): thermal contact is broken and the gas continues expanding with no heat flow, doing more work as its temperature drops from T_H to T_C. Step 3 (**isothermal compression**): the gas is placed in contact with the cold reservoir at T_C and compressed, rejecting heat Q_C while temperature stays at T_C. Step 4 (**adiabatic compression**): thermal contact is broken again and the gas is compressed back to the starting state as temperature rises from T_C to T_H. Net result: work W = Q_H − Q_C was extracted, and the gas has returned to its initial state (it is a cycle).

The efficiency η = W/Q_H = 1 − Q_C/Q_H. For the Carnot cycle specifically, because every step is **reversible**, no entropy is generated anywhere. Entropy enters with the hot reservoir (ΔS_H = −Q_H/T_H) and leaves with the cold reservoir (ΔS_C = +Q_C/T_C). Zero net entropy means Q_H/T_H = Q_C/T_C, so Q_C/Q_H = T_C/T_H, giving **Carnot efficiency** η_C = 1 − T_C/T_H. This depends only on the two reservoir temperatures, not on the working substance.

Why is this the maximum? Suppose a better engine existed with efficiency η > η_C. Run the Carnot cycle backwards as a refrigerator (pumping heat from cold to hot using work) and power it with the hypothetical better engine. The net effect would be a machine that transfers heat from a cold reservoir to a hot one with no other effect — a violation of the second law's Clausius statement. Therefore no engine operating between T_H and T_C can exceed Carnot efficiency. The T-S diagram makes this especially clean: on T-S axes, the Carnot cycle is a perfect rectangle, net work equals the enclosed area, and the efficiency is immediately visible as (T_H − T_C)/T_H = 1 − T_C/T_H. Every real engine's cycle, when plotted on T-S axes, will have less enclosed area relative to the heat input, confirming the Carnot bound.
