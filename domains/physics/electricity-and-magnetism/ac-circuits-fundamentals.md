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

## Questions

```yaml
- question: "A household outlet in the United States is rated at 120 V. An engineer needs to calculate the average power dissipated by a 10-ohm resistor connected to this outlet. Which voltage should she use in P = V²/R?"
  type: multiple-choice
  options:
    - "85 V — divide 120 V by √2 to get the RMS value first"
    - "120 V — this is already the RMS voltage; use it directly"
    - "170 V — multiply by √2 to find the peak voltage before calculating power"
    - "60 V — use half the peak voltage for average power calculations"
  answer: 1
  explanation: "The 120 V rating of a household outlet is already the RMS voltage — not the peak. RMS values are defined precisely so that average power calculations use the standard P = V²/R formula, identical to DC. The peak voltage is actually 120√2 ≈ 170 V. Using P = V_rms²/R = 120²/10 = 1440 W gives the correct average power. The common mistake is thinking 120 V is the peak and trying to convert it downward."

- question: "In a purely capacitive AC circuit, how does the phase of the current compare to the phase of the voltage across the capacitor?"
  type: multiple-choice
  options:
    - "Current and voltage are in phase — they reach their peak values simultaneously"
    - "Current leads voltage by 90° — current reaches its peak before voltage does"
    - "Voltage leads current by 90° — voltage peaks before the current does"
    - "Current and voltage are 180° out of phase — they peak at opposite moments"
  answer: 1
  explanation: "For a capacitor, current I = C · dV/dt. When voltage is at its peak, dV/dt = 0 and current is zero; when voltage is crossing zero (changing fastest), current is at its maximum. This 90° offset means current peaks before voltage — current leads voltage. An inductor has the opposite relationship: voltage leads current by 90°. Memory aid: in a Capacitor, Current leads (ICE); in an inductor, Voltage leads (ELI)."

- question: "In a purely resistive AC circuit, current and voltage reach their peak values at the same instant."
  type: true-false
  answer: true
  explanation: "Ohm's law V = IR applies instantaneously in a resistive circuit. When voltage is at its peak, I = V/R is also at its peak. When voltage crosses zero, so does the current. There is no storage mechanism (no capacitor or inductor) to shift the timing. Resistors are in-phase elements — they are the AC reference against which phase leads and lags for capacitors and inductors are measured."

- question: "The peak voltage of a standard 120 V AC outlet is 120 V."
  type: true-false
  answer: false
  explanation: "The 120 V rating is the RMS (root-mean-square) voltage, not the peak. The peak voltage is V₀ = V_rms × √2 = 120√2 ≈ 170 V. RMS values are used for ratings because they correspond directly to power-delivering capability — a 120 V RMS AC supply delivers the same average heating power as a 120 V DC supply. The peak is higher but does not represent steady power delivery."

- question: "Why do we use RMS values rather than peak values when calculating the average power delivered by an AC source to a resistive load?"
  type: short-answer
  answer: "Because average power depends on the time average of V(t)·I(t) over a full cycle, not the peak values. For a sinusoidal voltage, the instantaneous power oscillates; its time average is V₀²/(2R). The RMS voltage is defined as V_rms = V₀/√2, which makes V_rms²/R = V₀²/(2R) — matching the time-averaged power exactly. This is why P_avg = V_rms²/R works with the standard DC formula."
  explanation: "Peak values overstate the power — a sinusoid spends most of its time below its peak. The RMS value is the DC-equivalent voltage that delivers the same average power. It is computed as the square root of the mean of the squared voltage, which for a pure sinusoid yields V₀/√2. This is why all AC appliances are rated in RMS and why power calculations use the same familiar formulas as for DC."
```

## Explainer

In your study of RLC circuits, you saw how a circuit containing resistance, inductance, and capacitance can oscillate like a mechanical spring-mass system. AC circuits extend this insight: instead of a one-time kick that produces decaying oscillations, an AC source continuously drives the circuit at a chosen frequency ω. The source voltage V(t) = V₀ sin(ωt) is the same sinusoidal function you know from trigonometry — it simply oscillates between +V₀ and −V₀, completing ω/(2π) full cycles per second.

The key new concept is **phase**. In a purely resistive circuit, Ohm's law V = IR holds instantaneously, so current and voltage rise and fall together — they are **in phase**. But a capacitor stores charge, and a capacitor's current is proportional to the *rate of change* of voltage (I = C dV/dt). When voltage is at its peak (momentarily flat), the rate of change is zero and current is zero; when voltage is crossing zero (changing fastest), current is at its peak. This 90° offset means current *leads* voltage in a capacitor. An inductor does the opposite: it opposes changes in current, so voltage peaks 90° before the current catches up — voltage *leads* current.

**Phasors** make these phase relationships visual. A phasor is a rotating vector in the complex plane whose length is the amplitude and whose angle is the phase. The instantaneous value of V(t) or I(t) is the projection of the phasor onto the real axis. Because all quantities in a linear AC circuit oscillate at the same frequency, you can represent them as arrows at fixed angles relative to each other. This transforms AC circuit analysis into vector addition — you can add voltages across components by adding their phasors tip-to-tail, without solving differential equations at every step. If you've studied complex numbers, phasors are simply complex amplitudes: V = V₀e^(iωt), and arithmetic follows the same algebra.

The final essential tool is **RMS values**. Instantaneous power is P(t) = V(t)·I(t), which oscillates between positive and negative values in a reactive (capacitive or inductive) circuit. Average power is what matters for heating and work done, and it depends on the average of V(t)·I(t) over a full cycle. For a sinusoid, the root-mean-square value — the square root of the mean of the square — is V₀/√2. So V_rms = V₀/√2 and I_rms = I₀/√2. Average power delivered to a resistive load is simply P_avg = V_rms · I_rms, the same formula as DC. This is why your household outlet is rated at 120 V RMS: a 120 V AC supply delivers the same average heating power to a resistor as 120 V DC would.
