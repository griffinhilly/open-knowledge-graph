---
id: dc-circuit-analysis
title: DC Circuit Analysis with Kirchhoff's Laws
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: resistor-combinations
  type: hard
- id: systems-of-linear-equations
  type: soft
builds-toward:
- rc-transient-response
tags:
- kirchhoff
- analysis
- networks
stage: formal-systems
status: draft
---

# DC Circuit Analysis with Kirchhoff's Laws

## Core Idea
Kirchhoff's current law (KCL): sum of currents at a node is zero, ∑ I_in = ∑ I_out. Kirchhoff's voltage law (KVL): sum of voltages around a closed loop is zero, ∮ V = 0. These laws follow from charge conservation and the conservative nature of the electrostatic field. Combined with Ohm's law, they enable systematic analysis of complex circuits through node voltage or mesh current methods.

## Explainer

Kirchhoff's laws are simply conservation laws wearing circuit clothing. **Kirchhoff's current law (KCL)** says charge cannot accumulate at a node: every electron that flows in must flow out. This is charge conservation applied locally — whatever current enters a junction, the same total current must leave it. **Kirchhoff's voltage law (KVL)** says the electrostatic field is conservative: if you walk around any closed loop in a circuit, the net change in potential is zero, because you end where you started. These are not approximations — they are exact consequences of Maxwell's equations in the low-frequency limit.

The power of KCL and KVL is that they let you write a system of simultaneous equations for an arbitrarily complex network. In the **node voltage method**, you pick one node as a reference (ground, V = 0), assign unknown voltages to every other node, and apply KCL at each: sum of currents leaving the node equals zero. Ohm's law converts each current to a voltage difference divided by resistance. In the **mesh current method**, you assign a circulating current to each independent loop and apply KVL: sum of voltage drops around the loop equals zero. Both methods produce a linear system you already know how to solve from your algebra prerequisites.

The key skill is setting up the equations correctly. For KCL at a node: write (V_node − V_neighbor)/R for each branch, sum them, and set equal to zero (or to the current injected by a source). For KVL around a loop: traverse the loop in a consistent direction; a resistor drop is +IR if you cross it against the current, −IR if with it; a voltage source is ±V depending on polarity. Getting signs consistent is the main source of errors — always define your current directions and stick to them.

To build intuition: think of a circuit as a network of water pipes. Voltage is pressure, current is flow rate, and resistance is pipe narrowness. KCL says water doesn't pile up at pipe junctions. KVL says if you trace a closed loop of pipes, the net pressure change is zero — a pump raises pressure, a narrow pipe drops it, and they balance. A complex circuit is just a system of such constraints, and linear algebra is the tool that solves them simultaneously. Once you can write and solve these equations, you have the foundation for analyzing all DC networks, regardless of complexity.
