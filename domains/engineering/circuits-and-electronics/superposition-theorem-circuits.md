---
id: superposition-theorem-circuits
title: Superposition Theorem
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-variables-and-elements
  type: hard
- id: node-voltage-method
  type: soft
- id: mesh-current-method
  type: soft
builds-toward:
- thevenin-norton-equivalents
tags:
- linearity
- superposition
- multiple-sources
- dependent-sources
stage: formal-systems
status: validated
---

# Superposition Theorem

## Core Idea
In any linear circuit, the voltage or current at any element due to multiple independent sources equals the algebraic sum of the responses produced by each source acting alone. To isolate one independent source, all other independent voltage sources are replaced with short circuits and all other independent current sources with open circuits. Dependent sources are never deactivated — they remain active during every sub-analysis. Superposition follows directly from the linearity of Kirchhoff's laws and is foundational to Thevenin/Norton analysis.

## How It's Best Learned
Apply superposition to circuits with two or three sources and verify by comparing with full nodal or mesh analysis. Track reference directions carefully when summing partial responses — the algebraic sign of each contribution matters.

## Common Misconceptions
- Deactivating dependent sources along with independent sources — dependent sources must remain active throughout.
- Applying superposition to power, which is quadratic and nonlinear — powers from individual source contributions do not add to give total power.
- Forgetting to restore the circuit to its full topology between sub-analyses.

## Explainer

From your study of node voltage and mesh current methods, you know how to solve circuits with multiple sources by assembling and solving a system of linear equations. Superposition offers an alternative route grounded in the same mathematics: because Kirchhoff's laws are linear in voltages and currents, responses from multiple sources add independently. Instead of solving everything at once, you decompose the problem into simpler sub-circuits — one source active at a time — and sum the results.

The procedure is mechanical. To find the contribution of independent source k, **deactivate** all other independent sources: replace every other independent voltage source with a short circuit (zero volts across it) and every other independent current source with an open circuit (zero current through it). Solve the simplified circuit for the desired voltage or current. Repeat for each source. The actual value is the algebraic sum of all contributions, with careful attention to reference directions — a contribution that opposes your reference direction subtracts rather than adds.

The most important rule is that **dependent sources are never deactivated**. A dependent source's value is controlled by a circuit variable (a voltage or current elsewhere in the circuit), so deactivating it would remove a real physical coupling in the device model. Transistors and op-amps are routinely modeled with dependent sources; removing them in a sub-analysis would eliminate the gain mechanism entirely. The practical rule is: independent sources go off one at a time, dependent sources stay on always.

Superposition has both analytical and conceptual value. Analytically, it trades one N-source problem for N single-source problems, each often solvable by inspection using voltage dividers or current dividers. Conceptually, it attributes each contribution to its source — in an amplifier circuit, you can separately calculate the signal component (from the input source) and the DC bias (from the supply), then combine them. The key limitation is power: because P = V²/R = I²·R is quadratic in voltage and current, power is nonlinear and does not obey superposition. Always compute total power from the combined voltages and currents after superposition is complete, never by summing the powers from individual sub-analyses.
