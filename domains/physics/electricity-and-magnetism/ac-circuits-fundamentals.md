---
id: ac-circuits-fundamentals
title: 'AC Circuits: Fundamentals'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lc-and-rlc-circuits
  type: hard
- id: amplitude-period-phase-shift
  type: hard
- id: graphing-sine-and-cosine
  type: soft
- id: complex-numbers-intro
  type: soft
builds-toward:
- impedance-and-reactance
- ac-power-and-resonance
tags:
- AC-circuits
- phasors
- RMS
- frequency
- alternating-current
stage: formal-systems
status: validated
---

# AC Circuits: Fundamentals

## Core Idea
Alternating current (AC) circuits use sources with time-varying voltage V(t) = V₀ sin(ωt). In a purely resistive circuit, current and voltage are in phase. In a capacitor, current leads voltage by 90°; in an inductor, voltage leads current by 90°. Phasors — rotating vectors whose projections give instantaneous values — provide a powerful graphical method to track phase relationships. The root-mean-square (RMS) values V_rms = V₀/√2 and I_rms = I₀/√2 relate peak values to average power.

## How It's Best Learned
Start with a purely resistive AC circuit, then add a capacitor and inductor separately. Use phasor diagrams to visualize phase differences. Master the RMS relationship before computing power in AC circuits.

## Common Misconceptions
- AC voltage and current are not always in phase — phase difference depends on the load.
- RMS values, not peak values, determine average power delivered.
- Household '120V AC' refers to the RMS voltage; the peak is 120√2 ≈ 170V.

## Explainer

In your study of RLC circuits, you saw how a circuit containing resistance, inductance, and capacitance can oscillate like a mechanical spring-mass system. AC circuits extend this insight: instead of a one-time kick that produces decaying oscillations, an AC source continuously drives the circuit at a chosen frequency ω. The source voltage V(t) = V₀ sin(ωt) is the same sinusoidal function you know from trigonometry — it simply oscillates between +V₀ and −V₀, completing ω/(2π) full cycles per second.

The key new concept is **phase**. In a purely resistive circuit, Ohm's law V = IR holds instantaneously, so current and voltage rise and fall together — they are **in phase**. But a capacitor stores charge, and a capacitor's current is proportional to the *rate of change* of voltage (I = C dV/dt). When voltage is at its peak (momentarily flat), the rate of change is zero and current is zero; when voltage is crossing zero (changing fastest), current is at its peak. This 90° offset means current *leads* voltage in a capacitor. An inductor does the opposite: it opposes changes in current, so voltage peaks 90° before the current catches up — voltage *leads* current.

**Phasors** make these phase relationships visual. A phasor is a rotating vector in the complex plane whose length is the amplitude and whose angle is the phase. The instantaneous value of V(t) or I(t) is the projection of the phasor onto the real axis. Because all quantities in a linear AC circuit oscillate at the same frequency, you can represent them as arrows at fixed angles relative to each other. This transforms AC circuit analysis into vector addition — you can add voltages across components by adding their phasors tip-to-tail, without solving differential equations at every step. If you've studied complex numbers, phasors are simply complex amplitudes: V = V₀e^(iωt), and arithmetic follows the same algebra.

The final essential tool is **RMS values**. Instantaneous power is P(t) = V(t)·I(t), which oscillates between positive and negative values in a reactive (capacitive or inductive) circuit. Average power is what matters for heating and work done, and it depends on the average of V(t)·I(t) over a full cycle. For a sinusoid, the root-mean-square value — the square root of the mean of the square — is V₀/√2. So V_rms = V₀/√2 and I_rms = I₀/√2. Average power delivered to a resistive load is simply P_avg = V_rms · I_rms, the same formula as DC. This is why your household outlet is rated at 120 V RMS: a 120 V AC supply delivers the same average heating power to a resistor as 120 V DC would.
