---
id: ac-impedance
title: AC Circuits and Complex Impedance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lenz-law
  type: soft
- id: rl-transient-response
  type: hard
- id: complex-numbers-intro
  type: hard
- id: operations-with-complex-numbers
  type: hard
builds-toward:
- rlc-resonance
tags:
- ac
- impedance
- phasor
stage: formal-systems
status: draft
---

# AC Circuits and Complex Impedance

## Core Idea
For sinusoidal AC signals at frequency ω, impedance Z relates voltage to current. For a resistor: Z = R; capacitor: Z = 1/(iωC); inductor: Z = iωL. Complex impedances combine like resistances: series adds Z, parallel adds 1/Z. Impedance captures both magnitude and phase relationship between voltage and current. AC power includes real (P = IV cos φ) and reactive components.

## Explainer

From your work on RL transient circuits, you know that inductors and capacitors create time delays — voltage and current don't peak at the same moment. In DC transient analysis you tracked this with exponentials. In AC circuits, the input is sinusoidal and persists forever, so you need a tool that captures steady-state phase relationships compactly. That tool is **complex impedance**.

The key insight is that complex numbers encode both magnitude and phase in one object. A sinusoidal voltage V(t) = V₀cos(ωt + φ) is represented as the real part of V₀e^(i(ωt + φ)) — a complex exponential. When you differentiate or integrate a complex exponential, you just multiply by iω or divide by iω, turning calculus into algebra. This is why the capacitor's relation V = Q/C becomes, in terms of current I = dQ/dt, the impedance Z_C = V/I = 1/(iωC). Similarly, the inductor's V = L dI/dt gives Z_L = iωL. The resistor has no time dependence, so Z_R = R — a purely real number with no phase shift.

The **phasor** is the complex amplitude itself (dropping the e^(iωt) factor). Once you represent every voltage and current as a phasor, Kirchhoff's laws still hold — but now in the complex plane. This means you can solve AC circuits using exactly the same series and parallel combination rules you learned for resistors, just with complex numbers. The magnitude |Z| gives the ratio of peak voltage to peak current, and the angle arg(Z) gives the phase by which voltage leads current. For an inductor (Z = iωL), arg(Z) = +90°, meaning voltage leads current by a quarter cycle. For a capacitor (Z = 1/iωC = -i/ωC), arg(Z) = −90°, so current leads voltage.

**AC power** adds one more subtlety. When voltage and current are in phase (as in a resistor), all power goes into heat — this is **real power** P = (1/2)V₀I₀. When they are 90° out of phase (pure inductor or capacitor), energy sloshes back and forth between source and element each cycle but averages to zero — this is **reactive power**. The **power factor** cos φ (where φ is the phase angle between voltage and current) interpolates between these extremes, so P = (1/2)V₀I₀ cos φ. A circuit with a low power factor draws large peak currents to deliver modest real power, which matters enormously in electrical engineering. The complex impedance framework makes all of this computable from the circuit topology without ever writing down a differential equation.
