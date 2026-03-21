---
id: norton-circuit-equivalent
title: Norton Equivalent Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-theorems-linearity
  type: hard
- id: ideal-voltage-and-current-sources
  type: hard
builds-toward:
- maximum-power-transfer
- sinusoidal-steady-state-analysis
tags:
- norton
- equivalent-circuit
- current-source
- duality
stage: formal-systems
status: draft
---

# Norton Equivalent Circuits

## Core Idea
Norton's theorem is the dual of Thévenin's: any linear circuit simplifies to a current source I_N in parallel with resistance R_N. Norton current is the short-circuit current, and Norton resistance equals Thévenin resistance. The two theorems are interchangeable via I_N = V_th/R_th, providing flexibility in circuit analysis.

## Questions

```yaml
- question: "How is the Norton current I_N determined when finding the Norton equivalent of a linear circuit at a pair of terminals?"
  type: multiple-choice
  options:
    - "By measuring the open-circuit voltage across the terminals with no load connected"
    - "By short-circuiting the terminals with a wire and measuring the current that flows through that short"
    - "By killing all independent sources and measuring the resistance seen from the terminals"
    - "By dividing the open-circuit voltage by the internal source resistance"
  answer: 1
  explanation: "The Norton current is defined as the short-circuit current — the current delivered into a zero-resistance (shorted) load. This is found by connecting a wire directly across the terminals and measuring the resulting current. Intuitively, it represents the maximum current the network can deliver. Note that option A describes how to find V_th (the Thévenin voltage), and option C describes how to find R_N = R_th. Option D is actually the formula I_N = V_th/R_th, which lets you compute I_N from a known Thévenin equivalent."

- question: "An engineer has two identical Thévenin equivalents (V_th = 12V, R_th = 4Ω each) that she wants to connect in parallel and analyze as a single source. What is the most efficient approach?"
  type: multiple-choice
  options:
    - "Convert each to its Norton equivalent (I_N = 12/4 = 3A, R_N = 4Ω), add the Norton currents (6A total), and combine the parallel Norton resistances (2Ω combined) — done in two steps"
    - "Add the Thévenin voltages directly (24V total) and keep the same resistance (4Ω)"
    - "Solve the complete combined circuit from scratch using Kirchhoff's voltage law at each node"
    - "You cannot combine Thévenin equivalents in parallel — they must be connected in series"
  answer: 0
  explanation: "This is precisely why Norton equivalents are preferred for parallel combinations. In parallel, Norton current sources add directly (3A + 3A = 6A) and their parallel resistances combine as 4Ω ∥ 4Ω = 2Ω. Attempting this with Thévenin equivalents in parallel requires converting to Norton anyway before you can add them, since voltage sources in parallel with different internal resistances require more careful treatment. Option B is wrong: V_th sources in parallel do not simply add their voltages. The duality principle makes the choice of representation a matter of analytical convenience."

- question: "The Norton resistance R_N of a circuit is generally different from the Thévenin resistance R_th of the same circuit, since one is associated with a current source and the other with a voltage source."
  type: true-false
  answer: false
  explanation: "R_N always equals R_th exactly. Both are found by the same method: kill all independent sources (replace voltage sources with shorts, current sources with open circuits) and measure the resistance seen looking into the terminals from outside. This resistance is a property of the network's passive structure alone — it doesn't depend on whether the circuit is being described as a Thévenin or Norton equivalent. The two forms represent the same network in different languages; only the source element (voltage vs. current) changes."

- question: "Norton equivalents are more analytically convenient than Thévenin equivalents when combining subcircuits connected in parallel."
  type: true-false
  answer: true
  explanation: "In parallel connections, current sources add directly and parallel resistances combine with the standard formula. This makes Norton equivalents natural for parallel networks: you add Norton currents and combine resistances in parallel, both single-step operations. Thévenin equivalents are natural for series connections, where voltage sources add directly and series resistances simply sum. This is the practical meaning of duality — both representations are correct, but choosing the one that matches the topology makes the algebra significantly cleaner."

- question: "A circuit has a Thévenin equivalent of V_th = 10V and R_th = 5Ω. Describe the Norton equivalent and explain why R_N must equal R_th."
  type: short-answer
  answer: "The Norton equivalent is I_N = V_th / R_th = 10V / 5Ω = 2A in parallel with R_N = 5Ω. R_N equals R_th because both resistances are found by the identical procedure: kill all independent sources and measure the resistance seen at the terminals from outside. This resistance depends only on the network's passive topology (resistors and the structure of dependent sources, if any) — it is independent of the source type being described. Since Thévenin and Norton are two descriptions of the same physical network, they must share the same terminal resistance. The only difference between the two forms is whether the independent source is represented as a voltage source in series (Thévenin) or a current source in parallel (Norton)."
  explanation: "The conversion I_N = V_th / R_th is not a formula to memorize as a separate fact — it follows directly from the requirement that both equivalents produce the same short-circuit current and the same open-circuit voltage. Setting up those two conditions immediately gives I_N = V_th / R_th and R_N = R_th."
```

## Explainer

From linearity and superposition — your prerequisite circuit theorems — you know that any linear network behaves predictably at its terminals regardless of internal complexity. Thévenin's theorem gave you one canonical form: a voltage source in series with a resistance. Norton's theorem gives you the **dual** form: a current source I_N in parallel with a resistance R_N. Both are exact representations of the same network, and they are related by a simple source transformation.

To find the Norton equivalent of a network at a pair of terminals, you need two quantities. First, **short-circuit the terminals** (connect a wire directly across them) and measure the current that flows through that short — this is I_N. Intuitively, the Norton current is the maximum current the network can deliver to a zero-resistance load. Second, **kill all independent sources** (replace voltage sources with short circuits, current sources with open circuits) and measure the resistance seen looking back into the terminals from outside — this is R_N, which equals R_th exactly. The two theorems describe the same network in different languages: Thévenin says "here is how much voltage I can produce at open circuit," while Norton says "here is how much current I can deliver into a short circuit." The conversion I_N = V_th / R_th relates the two directly, so knowing either form gives you the other instantly.

The choice between Thévenin and Norton is a matter of analytical convenience, not correctness. When you are connecting networks in **series**, Thévenin is natural — voltage sources add directly. When you are connecting networks in **parallel**, Norton is natural — current sources add directly and parallel resistances combine easily. This is the practical value of duality: it lets you choose whichever equivalent makes the algebra cleaner. For example, to find the total short-circuit current from two Norton sources in parallel, you simply add their Norton currents and combine their Norton resistances in parallel — a one-line calculation. The same problem with Thévenin equivalents would require converting back to Norton, combining, then converting again.

These theorems are also the conceptual foundation for thinking about **source loading** — how connecting a load changes what a source delivers. A Thévenin source with large R_th drops a lot of voltage when current flows; a Norton source with small R_N loses a lot of current when voltage builds up. An ideal voltage source has R_th = 0 (no internal drop); an ideal current source has R_N = ∞ (no internal diversion). Every real source sits between these ideals, and Norton and Thévenin equivalents give you the exact two-parameter model needed to predict behavior under any load — including the maximum power transfer condition that follows directly from these equivalent circuits.
