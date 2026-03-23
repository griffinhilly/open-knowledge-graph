---
id: kirchhoff-circuit-laws-rules
title: 'Kirchhoff''s Circuit Laws: Voltage and Current'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electromotive-force-batteries
  type: hard
builds-toward:
- network-circuit-analysis-methods
tags:
- kirchhoff-laws
- circuit-rules
- conservation
stage: formal-systems
status: validated
---

# Kirchhoff's Circuit Laws: Voltage and Current

## Core Idea
Kirchhoff's voltage law (KVL): sum of potential changes around a closed loop is zero, ΣV = 0. Kirchhoff's current law (KCL): sum of currents into a node equals sum leaving, ΣI_in = ΣI_out. Both follow from energy conservation and charge conservation.

## Questions

```yaml
- question: "At a circuit node, three branches meet. Branch 1 carries 3 A into the node and Branch 2 carries 2 A into the node. What does KCL require for Branch 3?"
  type: multiple-choice
  options:
    - "Branch 3 carries 1 A into the node, since currents distribute evenly"
    - "Branch 3 carries 5 A out of the node, since total current in must equal total current out"
    - "Branch 3 carries 5 A into the node, to balance the incoming current"
    - "KCL cannot determine the current in Branch 3 without knowing the resistances"
  answer: 1
  explanation: "KCL states that current into a node equals current out. Currents in: 3 + 2 = 5 A. For no charge to accumulate, exactly 5 A must leave through Branch 3. KCL is charge conservation made local: charge cannot pile up at a node in steady state. No resistance information is needed — KCL applies to currents regardless of what circuit elements produce them."

- question: "Traversing a loop, you cross a resistor in the direction opposite to the assumed current flow. What voltage term do you write for this resistor in your KVL equation?"
  type: multiple-choice
  options:
    - "−IR, because you are going against the current and losing potential"
    - "+IR, because going against the current means moving from low to high potential"
    - "0, because the direction of traversal doesn't affect the voltage"
    - "−IR/2, because crossing against the current gives half the normal voltage drop"
  answer: 1
  explanation: "Conventional current flows from high potential to low potential through a resistor. If you traverse the resistor against the current direction, you move from low to high potential — a gain — so you write +IR. If you traverse with the current (downhill), you write −IR. This sign convention is the key discipline in KVL: keeping it consistent throughout a loop ensures the equation correctly captures that total potential change around the loop is zero."

- question: "KCL is fundamentally a statement of charge conservation: in steady-state DC circuits, charge cannot accumulate at a node, so current in must equal current out."
  type: true-false
  answer: true
  explanation: "KCL is not an arbitrary circuit rule — it is conservation of charge applied locally to each node. In steady state, if more charge flowed in than out, charge would accumulate at the node, creating an increasing electric field that would alter currents until equilibrium. KCL states that equilibrium condition. Similarly, KVL is conservation of energy per unit charge: the work done on a charge going around any closed loop must be zero."

- question: "If you assume the wrong direction for a current when setting up KCL/KVL equations, the solution is invalid and you must restart with the correct assumed direction."
  type: true-false
  answer: false
  explanation: "Choosing the 'wrong' direction is not an error — it is part of the method. If your assumed direction is incorrect, the algebra will yield a negative value for that current. The negative sign tells you the actual current flows opposite to your assumption; the magnitudes and all other quantities are still correct. KCL/KVL is systematic precisely because you don't need to know directions in advance: the algebra discovers them."

- question: "What physical conservation law underlies each of Kirchhoff's two laws, and why does understanding this matter beyond just memorizing the rules?"
  type: short-answer
  answer: "KCL expresses conservation of charge: charge cannot accumulate at a node in steady state, so current in equals current out. KVL expresses conservation of energy per unit charge: the work done per unit charge around any closed loop is zero, because electric potential is path-independent. Understanding the conservation-law basis clarifies when the laws apply and makes the sign conventions interpretable rather than arbitrary."
  explanation: "Students who memorize 'voltages sum to zero around a loop' without the energy-conservation basis often apply the rule incorrectly when sign conventions become tricky. Knowing that you're tracking potential (altitude) as you traverse a circuit — and that returning to your starting node must leave you at the same potential — makes every sign choice interpretable. Conservation laws are the 'why' behind KCL and KVL."
```

## Explainer

Kirchhoff's laws are conservation laws in disguise. **Kirchhoff's current law (KCL)** says that charge cannot pile up at a circuit node: whatever current flows in must flow out. Think of it like water at a pipe junction — if 5 liters per second arrive through two pipes, exactly 5 liters per second must leave through the others. In circuit terms, currents flowing into a node sum to zero when you assign a sign convention: currents in are positive, currents out are negative. KCL is charge conservation made local.

**Kirchhoff's voltage law (KVL)** says that electric potential is a single-valued function. If you walk around any closed path in a circuit and return to your starting point, your net change in altitude (potential) must be zero — just as hiking around a mountain and returning to base camp leaves your elevation unchanged. Each battery raises the potential (a gain), each resistor drops it (a loss). Going around a loop in one direction, these gains and losses must cancel exactly. KVL is energy conservation per unit charge.

To apply the laws systematically: label unknown currents with directions (guessing a wrong direction just gives a negative answer, which is fine). Write one KCL equation per independent node, and one KVL equation per independent loop. A circuit with N nodes gives N−1 independent KCL equations; a circuit with B branches and N nodes gives B−(N−1) independent loop equations. Together they produce exactly enough equations to solve for all unknown currents and voltages. This systematic approach — choose directions, write equations, solve — replaces the hit-or-miss intuition that works for simple series/parallel circuits but breaks down for complex networks with multiple loops.

A practical note on sign conventions: when you traverse a resistor in the direction of assumed current flow, the voltage *drops* (write −IR); against the current, it *rises* (write +IR). For a battery, traverse from − to + terminal gives a rise (+ε); from + to − gives a drop (−ε). Keeping these conventions consistent is the difference between getting the right answer and making an error that no amount of algebra can fix. Kirchhoff's laws provide the framework; discipline with signs provides the execution.
