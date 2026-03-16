---
id: impedance-admittance-networks
title: Impedance and Admittance in AC Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-algebra-complex-impedance
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- ac-power-analysis-circuits
- series-resonance-characteristics
- parallel-resonance-characteristics
- frequency-response-analysis-bode
tags:
- impedance
- admittance
- ac-networks
stage: formal-systems
status: draft
---

# Impedance and Admittance in AC Networks

## Core Idea
Admittance Y = 1/Z is the reciprocal of impedance, with conductance G (real part) and susceptance B (imaginary part). Like impedances, parallel admittances sum directly and series admittances combine reciprocally. AC network analysis using impedance-admittance relationships parallels DC resistive analysis, allowing application of voltage/current dividers, mesh analysis, and nodal analysis to AC circuits.

## How It's Best Learned
Calculate impedance values for RC, RL, and RLC circuits at several frequencies. Plot real and imaginary parts of impedance versus frequency to visualize how reactance dominates at different frequency ranges.

## Common Misconceptions
Students often forget that impedance is frequency-dependent, unlike resistance. Some mistakenly add impedances as if they were purely real numbers, ignoring the reactive component and resulting phase shifts.

## Explainer

From phasor algebra, you know that **impedance** Z is the complex-valued generalization of resistance: Z = R + jX, where R is resistance and X is reactance. Impedances combine in circuits just as resistances do in DC circuits — series impedances add, parallel impedances combine via the reciprocal formula. **Admittance** Y = 1/Z is simply the reciprocal of impedance, and it plays a symmetric role. Just as resistance is the opposition to current flow, admittance is the *ease* of current flow. Its real part is **conductance** G and its imaginary part is **susceptance** B: Y = G + jB.

The motivation for introducing admittance is practical efficiency. When analyzing parallel circuits, impedances combine via 1/Z_total = 1/Z₁ + 1/Z₂ + ... — a formula requiring tedious reciprocals. In the admittance picture, parallel elements have admittances that simply add: Y_total = Y₁ + Y₂ + .... This mirrors exactly the way series impedances add. The symmetry is complete: series circuits are natural in the impedance domain; parallel circuits are natural in the admittance domain. Complex networks often mix both, and skilled analysts switch between representations to keep the algebra as clean as possible.

For individual elements, impedance and admittance express the same physics from opposite perspectives. A resistor has Z = R, so Y = 1/R = G (pure conductance, no susceptance). A capacitor has Z = 1/(jωC), so Y = jωC (pure susceptance, positive, increasing with frequency). An inductor has Z = jωL, so Y = 1/(jωL) (pure susceptance, negative, decreasing with frequency). Notice that susceptance and reactance have opposite signs for the same element: an inductor's positive reactance corresponds to a negative susceptance. This sign flip is a common source of errors, so track it carefully.

With impedances and admittances in hand, every DC circuit analysis technique extends directly to AC circuits. Nodal analysis in AC circuits uses admittances at each node (summing currents in terms of admittance times voltage). Mesh analysis uses impedances (summing voltages in terms of impedance times current). Voltage and current dividers work identically — just replace R with Z or G with Y. The entire toolkit you built for resistive circuits is reusable; only the elements are now complex and frequency-dependent. When you encounter series resonance and parallel resonance in later topics, you will see exactly how the real and imaginary parts of Z and Y compete and cancel at specific frequencies, producing the resonant behavior that underlies filters, oscillators, and tuned amplifiers.
