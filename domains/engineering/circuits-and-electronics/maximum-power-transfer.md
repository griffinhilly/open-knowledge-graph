---
id: maximum-power-transfer
title: Maximum Power Transfer Theorem
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: thevenin-circuit-equivalent
  type: hard
- id: power-energy-in-circuits
  type: hard
builds-toward:
- sinusoidal-steady-state-analysis
tags:
- maximum-power
- impedance-matching
- power-transfer
stage: formal-systems
status: draft
---

# Maximum Power Transfer Theorem

## Core Idea
Maximum power is delivered to a load when load resistance equals the Thévenin resistance of the source (impedance matching condition). The maximum power available is P_max = V_th²/(4R_th). This result is important for signal transmission systems, though maximum efficiency (R_load >> R_source) is preferred in power delivery applications.

## Explainer

From your study of Thévenin equivalents, you know that any linear source network — no matter how complex — reduces to a voltage source V_th in series with a resistance R_th. This simplification sets up a clean optimization problem: given this fixed source, what load resistance R_L extracts the most power?

The analysis is a single-variable calculus problem. Power delivered to the load is P = I²R_L, where current I = V_th/(R_th + R_L). Substituting: P = V_th² × R_L / (R_th + R_L)². Setting dP/dR_L = 0 and solving yields R_L = R_th — the **impedance matching condition**. At this point, P_max = V_th²/(4R_th). The factor of 4 in the denominator reveals something important: when matched, exactly half the total power is dissipated in R_th and half in R_L. The source is only 50% efficient at the maximum-power operating point.

This 50% efficiency exposes the fundamental tension between **maximum power transfer** and **maximum efficiency**. When R_L >> R_th, current is small and little power is lost in R_th — efficiency approaches 100%, but total power delivered is tiny. When R_L = R_th, efficiency is exactly 50%, but power delivered is maximized for the given source. These goals serve different engineering contexts: power delivery systems (electrical grids, motor drives, battery chargers) prioritize efficiency and operate with R_L >> R_th; communication and signal systems (antennas, RF amplifiers, audio transmission lines) want maximum signal extraction and use impedance matching.

A critical subtlety: the theorem assumes R_th is fixed by the source — you are optimizing only over R_L. If R_th could be freely reduced to zero, you would deliver maximum power to any load, which is why low-output-impedance sources are prized in power electronics. In AC circuits, the condition generalizes to complex impedances: maximum power transfer requires Z_L = Z_th* (the complex conjugate of the Thévenin impedance). This cancels the reactive parts and matches the resistive parts, ensuring all available source power is absorbed by the load rather than bounced back — the foundation of transmission line and antenna matching theory.
