---
id: second-order-passive-filters
title: Second-Order Passive Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-transfer-function-analysis
  type: hard
- id: rlc-circuit-transient-analysis-overview
  type: hard
builds-toward:
- bandpass-and-bandstop-filter-design
tags:
- RLC-filters
- damping
- resonance
- steeper-rolloff
stage: formal-systems
status: validated
---

# Second-Order Passive Filters

## Core Idea
Second-order filters built from RLC circuits provide -40 dB/decade rolloff and can exhibit resonance peaks or dips depending on damping. The quality factor Q controls the sharpness; low Q gives smooth response while high Q causes peaking. Series and parallel RLC configurations yield different filter characteristics (e.g., series RLC is notch, parallel RLC is peaking).

## Questions

```yaml
- question: "An engineer needs a second-order low-pass filter with a maximally flat passband and no resonance peak. Which Q value achieves this, and what is this condition called?"
  type: multiple-choice
  options:
    - "Q >> 1 — higher Q gives a sharper rolloff and a flatter passband"
    - "Q = 1/√2 ≈ 0.707 — this is the Butterworth condition for maximally flat response"
    - "Q = 1 — unity Q guarantees no peaking by definition"
    - "Q = 0 — no resonance factor means no possibility of peaking"
  answer: 1
  explanation: "Q = 1/√2 (equivalently, damping ratio ζ = 1/√2) produces the Butterworth response: maximally flat in the passband with no amplitude peak before rolloff, and the −3 dB point falls exactly at ω₀. For Q > 1/√2, the magnitude rises above 0 dB near resonance before falling — the filter is peaking. For Q < 1/√2, the response is overdamped: no peak, but the rolloff begins before ω₀. The Butterworth condition is the boundary between these regimes and is widely used as a default design target."

- question: "In a series RLC circuit driven by a voltage source, which output configuration produces a notch (band-reject) filter?"
  type: multiple-choice
  options:
    - "Taking the output across the resistor R"
    - "Taking the output across the capacitor C alone"
    - "Taking the output across the series combination of L and C together"
    - "Taking the output across the inductor L alone"
  answer: 2
  explanation: "At resonance, a series LC combination has impedances that cancel: the inductive reactance jωL equals and opposes the capacitive reactance 1/jωC in magnitude. The net impedance of the series LC is zero at ω₀, making it a short circuit. Therefore no voltage appears across the LC pair at resonance — the output is zero (deep notch) while passing frequencies above and below resonance normally. This is distinct from taking the output across R (bandpass) or across C alone (low-pass)."

- question: "A second-order passive RLC filter with Q > 1/√2 can produce output voltages near resonance that exceed the source voltage, even though no active amplifying elements are present."
  type: true-false
  answer: true
  explanation: "Passive resonance allows voltage magnification across individual reactive components (L or C), even though the total energy in the circuit is conserved. At resonance in a series RLC, the voltage across the capacitor (or inductor) can be Q times the source voltage — this is sometimes called the 'Q-factor voltage magnification.' A high-Q circuit with Q = 10 can produce 10× the source voltage across the capacitor at resonance. This is not a violation of energy conservation; energy oscillates between L and C, with only small losses through R each cycle."

- question: "Taking the output across the resistor in a series RLC circuit produces a low-pass filter response."
  type: true-false
  answer: false
  explanation: "Output across R in a series RLC gives a bandpass response — at DC (ω = 0), the capacitor blocks and no current flows, so no voltage appears across R. At very high frequencies, the inductor blocks and again no current flows. Current (and therefore voltage across R) is maximum at resonance, where the reactive impedances cancel. For a low-pass response, take the output across C (its impedance is high at low frequencies, allowing voltage to develop there). For a high-pass response, take the output across L."

- question: "Explain why the quality factor Q determines both the sharpness of a second-order filter's rolloff and whether a resonance peak appears in the passband."
  type: short-answer
  answer: "Q = ω₀/(R/L) for a series RLC, representing the ratio of energy stored to energy dissipated per radian of oscillation. High Q means little energy is lost each cycle, so the circuit can sustain oscillations near resonance — producing a sharp frequency selectivity and a large amplitude peak before rolloff. In filter terms: high Q creates a tall, narrow resonance peak and a steep transition band. Low Q means heavy damping (energy dissipates quickly), suppressing oscillation — the response rolls off smoothly without any peak. The Butterworth condition Q = 1/√2 is the precise boundary where peaking just disappears while maximizing rolloff steepness."
  explanation: "The same Q governs the time-domain transient: high Q → underdamped ringing; low Q → overdamped sluggish return. The frequency-domain peak and time-domain ringing are two manifestations of the same underlying physics — a system that stores energy relative to its losses will both oscillate in time and selectively amplify near its natural frequency in steady state."
```

## Explainer

From your work with first-order RC and RL filters, you know that a single reactive element produces a -20 dB/decade rolloff above (or below) the cutoff frequency. A second-order filter adds a second reactive element — making it an RLC circuit — and something qualitatively new happens. The rolloff steepens to **-40 dB/decade**, meaning the filter cuts twice as sharply. But the bigger change is that the circuit now has a natural resonance frequency where energy can oscillate between the inductor and capacitor, producing behavior impossible with a single reactive element.

The transfer function of a second-order filter contains a quadratic in the denominator: H(s) = ω₀² / (s² + (ω₀/Q)s + ω₀²) for a low-pass prototype. The two key parameters are the **natural frequency** ω₀ = 1/√(LC), which sets where the rolloff begins, and the **quality factor** Q = ω₀ / (R/L) (for a series RLC), which controls the shape of the response near resonance. Q captures the ratio of energy stored to energy dissipated per cycle — a high-Q circuit stores energy efficiently relative to its losses, and so it can sustain oscillations. In filter terms: low Q produces a smooth, overdamped response; high Q produces a peaked response that amplifies signals near ω₀ before sharply attenuating them.

The Q factor is intimately related to the **damping ratio** ζ = 1/(2Q) from your RLC transient analysis. When ζ > 1 (Q < 0.5), the system is overdamped — no peaking in the frequency response, just a gradual rolloff. When ζ = 1/√2 (Q = 1/√2 ≈ 0.707), you get the **Butterworth** condition — the maximally flat response where there is no peaking and the -3 dB point is exactly at ω₀. When ζ < 1/√2 (Q > 0.707), the magnitude response peaks above 0 dB before rolling off, which can be useful for certain equalizer designs but undesirable for most anti-aliasing filters.

The physical configuration determines what kind of filter you get. In a **series RLC** driven from a voltage source, taking the output across the resistor yields a bandpass response (passes signals near ω₀); taking it across the capacitor yields low-pass; taking it across the inductor yields high-pass. Taking the output across the series LC combination (inductor + capacitor in series) gives a **notch** (band-reject) filter, because at resonance the series LC is a short circuit and no voltage appears across it. A **parallel RLC** tank circuit behaves dually — at resonance the parallel LC presents infinite impedance, so all the source current flows through the resistor, producing a bandpass output. These configurations let you sculpt frequency responses that no single-pole RC filter could approach.
