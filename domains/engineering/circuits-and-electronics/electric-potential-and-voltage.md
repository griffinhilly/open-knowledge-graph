---
id: electric-potential-and-voltage
title: Electric Potential and Voltage
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: charge-and-current-flow
  type: hard
- id: electric-potential-and-potential-energy
  type: soft
builds-toward:
- power-energy-in-circuits
- ohms-law-and-conductance
tags:
- voltage
- potential
- potential-difference
- emf
stage: formal-systems
status: validated
---

# Electric Potential and Voltage

## Core Idea
Electric potential is the work per unit charge needed to move charge in an electric field. Voltage is the potential difference between two points and represents energy per unit charge provided by a source. In circuits, voltages are defined relative to a reference node (ground) and measured across components using two-point measurements.

## Questions

```yaml
- question: "An engineer measures a node in a circuit and says 'this node is at 5 volts.' What crucial piece of information is missing from this statement?"
  type: multiple-choice
  options:
    - "The frequency of the voltage signal at that node"
    - "The current flowing through the node"
    - "The reference point — 5 volts relative to which node?"
    - "The type of source driving the circuit (AC or DC)"
  answer: 2
  explanation: "Voltage is always a potential *difference* between two points, never an absolute quantity. Saying a node is at '5 volts' is meaningless without specifying the reference. By convention, we designate one node as ground (0 V) and measure all other node voltages relative to it — but this reference assignment is arbitrary. A 9-volt battery doesn't mean the positive terminal is at 9 V in some cosmic sense; it means it is 9 V higher than the negative terminal. Without a reference, a voltage measurement has no physical content."

- question: "Kirchhoff's Voltage Law states that the sum of all voltage rises and drops around any closed loop equals zero. Why does this follow directly from the nature of voltage?"
  type: multiple-choice
  options:
    - "Because current must be conserved at every node in the circuit"
    - "Because voltage is a potential difference, and a path that returns to its starting node must have zero net change in potential"
    - "Because all resistors in a loop must dissipate equal power"
    - "Because voltage sources always equal the sum of the resistor voltage drops in series"
  answer: 1
  explanation: "Voltage is potential difference — the energy per unit charge to move from point A to point B. If you travel around a closed loop and return to your starting node, your net change in potential must be zero: you ended where you started. KVL is simply this fact stated as a circuit equation. It is conservation of energy expressed in terms of potential difference — just as you cannot gain gravitational potential energy by walking in a loop and returning to your starting elevation."

- question: "The node designated as 'ground' (0 V) in a circuit analysis is chosen by the engineer as a convenient reference — it does not have any special physical property that makes it inherently zero volts."
  type: true-false
  answer: true
  explanation: "Ground is a reference convention, not a physical absolute. Any node in the circuit can be declared ground; all other node voltages are then expressed relative to that choice. Different engineers analyzing the same circuit may choose different ground nodes — they will get different node voltage values, but all circuit behavior (currents, power, component voltages) will be identical. Choosing ground wisely (usually the most connected node or the negative terminal of the supply) simplifies the equations without changing the physics."

- question: "A circuit node 'at 5 volts' possesses 5 joules of electrical energy per coulomb in an absolute sense — this energy is a property of that node alone, independent of any reference."
  type: true-false
  answer: false
  explanation: "There is no such thing as absolute electric potential in a circuit — only potential *differences* have physical meaning. '5 volts' means 5 joules per coulomb of work would be done moving charge between this node and the reference node. Change the reference, and the number changes — but no actual physics changes. This is directly analogous to gravitational potential energy: saying an object is 'at 100 joules' is meaningless without specifying a height reference. Only the *difference* in height (and therefore energy) has physical content."

- question: "Explain why voltage is always a two-point measurement, using the analogy of gravitational potential energy to illustrate why absolute potential has no physical meaning in circuits."
  type: short-answer
  answer: "Voltage, like gravitational potential energy, is defined relative to a reference. A book 'at 10 joules of gravitational energy' is meaningless — 10 joules relative to the table? The floor? Sea level? Only the energy *difference* between two heights drives motion. Similarly, a node 'at 5 volts' only tells us something useful if we know the reference node (ground). The voltage *between* two nodes — the difference — is what determines how much energy a charge gains or loses traveling between them, and therefore what drives current. Absolute potential is a bookkeeping convenience, not a physical quantity; potential difference is the physically real thing."
  explanation: "This analogy reveals why KVL works (loops return to the same potential, like returning to the same height) and why voltage sources are defined by the difference between their terminals, not by the absolute potential of either terminal alone."
```

## Explainer

You already understand charge and current flow — charges moving through a conductor constitute current. But what makes charges move in the first place? The answer is energy differences, and **electric potential** is the tool that quantifies that energy on a per-charge basis. Think of it as the "electrical height" of a point in a circuit: just as water flows downhill from high gravitational potential to low, positive charges tend to flow from high electric potential to low.

**Electric potential** at a point is defined as the work per unit charge required to bring a positive test charge from a reference point (usually infinity in field theory, or ground in circuit analysis) to that point. Its unit is the **volt** (V), which equals one joule per coulomb. When we say a point in a circuit is at 5 V, we mean that moving one coulomb of positive charge from ground to that point requires 5 joules of work done by an external agent against the electric field. The field itself would do that same 5 joules of work if the charge moved from that point back to ground — that's the energy available to do useful work.

**Voltage** — more precisely, **potential difference** — is what appears in circuit analysis. It is always the difference between the potentials at two points: V_AB = V_A − V_B. This matters because absolute potential has no physical meaning in circuits; only differences do. A 9-volt battery doesn't mean the positive terminal is at 9 V in some absolute sense — it means the positive terminal is 9 V higher than the negative terminal. By convention, we assign one node in the circuit the label **ground** (0 V) and express all other node potentials relative to it. This choice is arbitrary but necessary: it gives us a consistent reference for writing and solving circuit equations.

A crucial distinction is between a **voltage source** (which maintains a fixed potential difference between its terminals, doing whatever work is necessary to sustain it) and the **voltage across a passive component** (which is the result of current flowing through it and energy being dissipated or stored). When current flows through a resistor, the resistor has a voltage drop across it — work is done on the charge by the field, and that work is converted to heat. When current charges a capacitor, work is stored as electric field energy between the plates. In both cases, the potential difference is the bookkeeping tool that tracks how energy is distributed around the circuit. Kirchhoff's Voltage Law — the sum of voltage rises and drops around any closed loop equals zero — is simply conservation of energy stated in these potential-difference terms.


