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

## Explainer

From linearity and superposition — your prerequisite circuit theorems — you know that any linear network behaves predictably at its terminals regardless of internal complexity. Thévenin's theorem gave you one canonical form: a voltage source in series with a resistance. Norton's theorem gives you the **dual** form: a current source I_N in parallel with a resistance R_N. Both are exact representations of the same network, and they are related by a simple source transformation.

To find the Norton equivalent of a network at a pair of terminals, you need two quantities. First, **short-circuit the terminals** (connect a wire directly across them) and measure the current that flows through that short — this is I_N. Intuitively, the Norton current is the maximum current the network can deliver to a zero-resistance load. Second, **kill all independent sources** (replace voltage sources with short circuits, current sources with open circuits) and measure the resistance seen looking back into the terminals from outside — this is R_N, which equals R_th exactly. The two theorems describe the same network in different languages: Thévenin says "here is how much voltage I can produce at open circuit," while Norton says "here is how much current I can deliver into a short circuit." The conversion I_N = V_th / R_th relates the two directly, so knowing either form gives you the other instantly.

The choice between Thévenin and Norton is a matter of analytical convenience, not correctness. When you are connecting networks in **series**, Thévenin is natural — voltage sources add directly. When you are connecting networks in **parallel**, Norton is natural — current sources add directly and parallel resistances combine easily. This is the practical value of duality: it lets you choose whichever equivalent makes the algebra cleaner. For example, to find the total short-circuit current from two Norton sources in parallel, you simply add their Norton currents and combine their Norton resistances in parallel — a one-line calculation. The same problem with Thévenin equivalents would require converting back to Norton, combining, then converting again.

These theorems are also the conceptual foundation for thinking about **source loading** — how connecting a load changes what a source delivers. A Thévenin source with large R_th drops a lot of voltage when current flows; a Norton source with small R_N loses a lot of current when voltage builds up. An ideal voltage source has R_th = 0 (no internal drop); an ideal current source has R_N = ∞ (no internal diversion). Every real source sits between these ideals, and Norton and Thévenin equivalents give you the exact two-parameter model needed to predict behavior under any load — including the maximum power transfer condition that follows directly from these equivalent circuits.
