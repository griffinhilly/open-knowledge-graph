---
id: potential-difference-voltage
title: Potential Difference and Voltage
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential
  type: hard
- id: electric-field
  type: hard
builds-toward:
- equipotential-surfaces
- capacitance
tags:
- electrostatics
- energy
- circuit concept
stage: formal-systems
status: draft
---

# Potential Difference and Voltage

## Core Idea
Potential difference between two points is the work per unit charge to move between them: V_AB = -(∫_B^A E·dl). Voltage is the practical term for potential difference. It is path-independent and depends only on endpoints, a consequence of the conservative nature of electrostatic fields.

## How It's Best Learned
Calculate potential difference for simple geometries by direct integration and by using potential functions. Measure voltages in circuits to build intuition for typical voltage scales.

## Common Misconceptions
- Potential and potential difference are the same (potential is absolute; difference is relative).
- Current flows from high to low potential magnitude (direction depends on charge sign).
- Voltage magnitude is always positive (sign depends on reference direction).

## Questions

```yaml
- question: "A positive test charge is moved from point B to point A along three different paths through an electrostatic field. Which result should you expect?"
  type: multiple-choice
  options:
    - "The three paths give different work values — longer paths involve more field interaction and therefore more work"
    - "All three paths give the same work done by the field, because the electrostatic field is conservative and work depends only on the endpoints"
    - "The straight-line path gives the minimum work; curved or longer paths always give more"
    - "The work values differ unless the field happens to be uniform"
  answer: 1
  explanation: "Electrostatic fields are conservative — they derive from a scalar potential. A defining property of conservative fields is path independence: the work done on a charge moving between two fixed endpoints is the same regardless of the route. This is not a special case; it holds for any electrostatic configuration. Path independence is what allows potential difference V_A − V_B to be defined as a property of the two points alone, not of the path between them."

- question: "A student measures 5 V between points A and B with a voltmeter and concludes: 'Point A must be at 5 V.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — a voltmeter directly reads the absolute electric potential at each probe"
    - "The voltmeter measures only the potential difference between A and B; A could be at 105 V with B at 100 V, or A at 5 V with B at 0 V — any pair differing by 5 V is consistent with the reading"
    - "The reading should be divided by the charge of the test particle to get the voltage"
    - "Voltmeters measure current; a different instrument is needed for voltage"
  answer: 1
  explanation: "A voltmeter measures potential difference, not absolute potential. Absolute potential at a single point is only defined relative to an arbitrary reference (infinity, ground, or a chosen node). The difference between A and B is always 5 V regardless of that reference choice — that's what the voltmeter captures. This is why circuits use 'voltage across' a component (a potential difference) rather than 'voltage at' a single node (which requires specifying a reference)."

- question: "The work done by the electric field in moving a charge between two points in an electrostatic field depends on the path taken between those points."
  type: true-false
  answer: false
  explanation: "Electrostatic fields are conservative — the work done on a charge moving between two endpoints is path-independent. Whether you take the direct route or a complicated detour, the field does the same work. This follows from the fact that electrostatic fields satisfy ∇ × E = 0, the mathematical statement that they are conservative. Path independence is what justifies defining potential difference as a property of the two endpoints alone."

- question: "Potential difference between two points is path-independent, meaning any route between the same two endpoints gives the same voltage value."
  type: true-false
  answer: true
  explanation: "This is a direct consequence of the conservative nature of electrostatic fields. The integral V_AB = −∫(B to A) E · dl gives the same result for any path from B to A. This path-independence is what makes potential difference physically meaningful: you can attach a voltmeter between two points in a circuit and get a definite reading, without needing to specify which 'path' the measurement traced through the field."

- question: "Why is potential difference (voltage) path-independent? What property of the electric field is responsible for this, and why does it matter?"
  type: short-answer
  answer: "Potential difference is path-independent because the electrostatic field is conservative — it is derivable from a scalar potential, and equivalently its curl is zero (∇ × E = 0). For any conservative field, the work done between two endpoints is the same regardless of path, because any closed path returns zero net work. This matters because it allows voltage to be defined as a property of two points alone, not of the route between them. Without path-independence, there would be no well-defined 'voltage across' a resistor or capacitor, and circuit analysis would be impossible."
  explanation: "The conservative property traces back to the Coulomb origin of electrostatic fields: Coulomb's law is a central force law, and central force fields are always conservative. This is why we can define electric potential V at each point in space and get potential difference simply by subtracting: V_A − V_B. The entire framework of circuit analysis — Kirchhoff's voltage law, Ohm's law, capacitance — depends on this path-independence holding."
```

## Explainer

You already know that the electric potential V at a point is the potential energy per unit charge placed there, and that the electric field **E** at a point gives the force per unit charge. **Potential difference** is the physically measurable quantity connecting these two ideas: it is the work done by the electric field per unit positive charge as that charge moves between two specific points in space.

The formula V_AB = −∫(B to A) **E** · d**l** captures this. Imagine carrying a small positive test charge from point B to point A along any path you choose. The electric field either helps or hinders your journey at each step; the total work done by the field per unit charge, accumulated over the entire path, is the potential difference V_A − V_B. Because electrostatic fields are **conservative** — a consequence of their Coulomb origin that you studied when learning about electric potential — this work depends only on the starting and ending points, not on the route taken. A straight path, a curved detour, and a zigzag all give the same answer. This path-independence is what makes voltage a well-defined property of a pair of locations.

The word **voltage** is the practical term for potential difference. A 9-volt battery maintains a 9 V difference between its terminals, doing 9 joules of work per coulomb of charge that moves from the negative to the positive terminal inside it. That energy is then available to drive current through an external circuit — flowing from the high-potential terminal through resistors, LEDs, or motors, losing energy along the way, and returning to the low-potential terminal. Ohm's law connects voltage and current: the potential difference across a resistor equals the current through it times the resistance, V = IR.

A subtle but important distinction: potential (V at a single point) is only defined relative to an arbitrary reference, typically chosen to be zero at infinity or at a ground node. Potential difference (ΔV between two points) is absolute and physically meaningful regardless of that reference choice — you cannot measure absolute potential with a voltmeter, but you can always measure the difference between two probes. This is why voltage is the natural language of circuits: every component has a voltage *across* it, and the sum of voltage drops around any closed loop must equal zero (Kirchhoff's voltage law). The path-independence you establish here is the foundation for equipotential surfaces, capacitance, and eventually the relationship between **E** and **V** via the gradient.
