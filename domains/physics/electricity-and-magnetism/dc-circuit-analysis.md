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

## Questions

```yaml
- question: "At a circuit node, three branches meet. Branch 1 carries 3 A flowing into the node, Branch 2 carries 5 A flowing into the node, and Branch 3's current is unknown. What is Branch 3's current, and which direction does it flow?"
  type: multiple-choice
  options:
    - "2 A, flowing into the node"
    - "8 A, flowing out of the node"
    - "8 A, flowing into the node"
    - "2 A, flowing out of the node"
  answer: 1
  explanation: "KCL states that the sum of currents into a node equals the sum out: 3 + 5 = I₃. Therefore I₃ = 8 A flowing out of the node. This follows from charge conservation — charge cannot accumulate at a node in steady state. Option A incorrectly subtracts; option C would violate charge conservation by having all three currents flow in. The direction (out of the node) is determined by the requirement that inflow equals outflow."

- question: "A student applies KVL to a loop containing a 12 V battery and two resistors (4 Ω and 8 Ω) in series, with all current flowing clockwise. Traversing the loop clockwise, they record +12 V for the battery. What should they record for each resistor?"
  type: multiple-choice
  options:
    - "+IR for each resistor, since current flows clockwise and so does the traversal"
    - "−IR for each resistor, since crossing a resistor with the current direction is a voltage drop"
    - "+IR for one resistor and −IR for the other, depending on resistor size"
    - "0 V for each resistor, since resistors don't affect voltage in a series loop"
  answer: 1
  explanation: "When traversing a resistor in the direction of conventional current flow, you experience a voltage drop: the voltage decreases by IR, so you record −IR. Since current flows clockwise and the traversal is also clockwise, both resistors are crossed with the current direction, giving −I(4) and −I(8). KVL then gives: 12 − 4I − 8I = 0, so I = 1 A. The sign convention is: crossing a resistor with the current = voltage drop (−IR); crossing against the current = voltage rise (+IR)."

- question: "Kirchhoff's Voltage Law states that the sum of currents entering a node equals the sum of currents leaving that node."
  type: true-false
  answer: false
  explanation: "This is Kirchhoff's Current Law (KCL), not KVL. Kirchhoff's Voltage Law states that the sum of all voltage changes around any closed loop is zero: ∮V = 0. KVL follows from the conservative nature of the electrostatic field — if you start and end at the same point, the net change in electric potential must be zero. Confusing KCL with KVL is a common error; remember: KCL is about currents at a node; KVL is about voltages around a loop."

- question: "Kirchhoff's laws are approximations that work well for simple circuits but break down for complex networks with many branches."
  type: true-false
  answer: false
  explanation: "Kirchhoff's laws are exact consequences of Maxwell's equations in the low-frequency (lumped-circuit) approximation — they are not approximations themselves. KCL follows exactly from charge conservation; KVL follows exactly from the conservative nature of the electrostatic field. They apply to arbitrarily complex networks — indeed, the node voltage and mesh current methods use them to solve systems with dozens of unknowns. The only regime where Kirchhoff's laws break down is at very high frequencies where the lumped-circuit approximation fails and electromagnetic wave effects become significant."

- question: "Explain in your own words why KVL guarantees that the sum of voltages around any closed loop is zero. What physical principle underlies this?"
  type: short-answer
  answer: "KVL follows from the fact that the electric field in a circuit is conservative. A conservative field means that the work done moving a charge from point A back to point A along any closed path is zero — the path doesn't matter, only the endpoints, and if you end where you started, the net energy change is zero. Voltage is electric potential energy per unit charge, so traversing a closed loop and returning to the starting point must yield zero net change in voltage. Every element either adds potential (like a battery) or drops it (like a resistor), and these must exactly cancel around any closed loop."
  explanation: "Grounding KVL in the conservative nature of the electrostatic field makes it clear why it is an exact law rather than an empirical rule. This understanding also explains why KVL holds for any closed loop you choose to draw through a circuit — not just the 'obvious' ones — which is what makes the mesh current method so powerful."
```

## Explainer

Kirchhoff's laws are simply conservation laws wearing circuit clothing. **Kirchhoff's current law (KCL)** says charge cannot accumulate at a node: every electron that flows in must flow out. This is charge conservation applied locally — whatever current enters a junction, the same total current must leave it. **Kirchhoff's voltage law (KVL)** says the electrostatic field is conservative: if you walk around any closed loop in a circuit, the net change in potential is zero, because you end where you started. These are not approximations — they are exact consequences of Maxwell's equations in the low-frequency limit.

The power of KCL and KVL is that they let you write a system of simultaneous equations for an arbitrarily complex network. In the **node voltage method**, you pick one node as a reference (ground, V = 0), assign unknown voltages to every other node, and apply KCL at each: sum of currents leaving the node equals zero. Ohm's law converts each current to a voltage difference divided by resistance. In the **mesh current method**, you assign a circulating current to each independent loop and apply KVL: sum of voltage drops around the loop equals zero. Both methods produce a linear system you already know how to solve from your algebra prerequisites.

The key skill is setting up the equations correctly. For KCL at a node: write (V_node − V_neighbor)/R for each branch, sum them, and set equal to zero (or to the current injected by a source). For KVL around a loop: traverse the loop in a consistent direction; a resistor drop is +IR if you cross it against the current, −IR if with it; a voltage source is ±V depending on polarity. Getting signs consistent is the main source of errors — always define your current directions and stick to them.

To build intuition: think of a circuit as a network of water pipes. Voltage is pressure, current is flow rate, and resistance is pipe narrowness. KCL says water doesn't pile up at pipe junctions. KVL says if you trace a closed loop of pipes, the net pressure change is zero — a pump raises pressure, a narrow pipe drops it, and they balance. A complex circuit is just a system of such constraints, and linear algebra is the tool that solves them simultaneously. Once you can write and solve these equations, you have the foundation for analyzing all DC networks, regardless of complexity.
