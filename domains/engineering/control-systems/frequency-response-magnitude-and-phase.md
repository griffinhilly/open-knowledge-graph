---
id: frequency-response-magnitude-and-phase
title: 'Frequency Response: Magnitude and Phase'
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: bode-plot-construction
  type: hard
- id: magnitude-phase-spectrum-representation
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- bandwidth-and-cutoff-frequencies
- gain-phase-margins-stability-robustness
tags:
- frequency-response
- magnitude
- phase
- bode
stage: expert
status: validated
---

# Frequency Response: Magnitude and Phase

## Core Idea
Frequency response describes how a system responds to sinusoidal inputs across all frequencies: magnitude response |G(jω)| shows amplitude attenuation or amplification, while phase response ∠G(jω) shows timing lag or lead. Bode plots (log magnitude vs log frequency, phase vs log frequency) visualize these relationships and reveal bandwidth, resonance, and high-frequency behavior essential for control design.

## Questions

```yaml
- question: "The Bode magnitude plot of a system shows a sharp peak of +12 dB near ω = 50 rad/s, followed by a steep roll-off. What does this peak indicate about the system's physical behavior?"
  type: multiple-choice
  options:
    - "The system strongly amplifies all input signals at frequencies near 50 rad/s and has high bandwidth"
    - "The system has low damping near its natural frequency — it will oscillate significantly when disturbed near ω = 50 rad/s"
    - "The system's phase margin is +12° at this frequency, indicating marginal stability"
    - "The system rejects disturbances at 50 rad/s and will suppress them effectively in closed-loop operation"
  answer: 1
  explanation: "A resonant peak in the magnitude response indicates a lightly damped system. Near the natural frequency ω_n, the system's denominator passes through near-zero, producing large output amplification. The peak height relates to damping ratio by peak ≈ 1/(2ζ) — a +12 dB peak (factor ~4) corresponds to ζ ≈ 0.125, which is very lightly damped. Physically, the system will ring — produce oscillatory transient responses — when disturbed. This is not a measure of bandwidth (option A) or phase margin (option C, which has different units); a lightly damped system is typically a problem to be addressed by the controller, not a sign of good disturbance rejection."

- question: "A control designer wants to increase the closed-loop bandwidth of a system. Reading the Bode plot, what change to the open-loop frequency response would achieve this?"
  type: multiple-choice
  options:
    - "Decrease the phase at the current gain crossover frequency to reduce the system's response time"
    - "Shift the gain crossover frequency to a higher value by adding gain at higher frequencies"
    - "Reduce the magnitude at low frequencies to flatten the frequency response"
    - "Eliminate the resonant peak by adding damping, which will extend the bandwidth"
  answer: 1
  explanation: "Bandwidth — the frequency at which |G(jω)| drops to −3 dB in closed loop — is closely related to the gain crossover frequency ω_c of the open-loop Bode plot (where |G(jω_c)| = 0 dB = 1). Moving ω_c to higher frequencies by boosting high-frequency gain extends the bandwidth: the system can now track faster-changing inputs. This is the basic action of a lead compensator. Reducing low-frequency gain (option C) would degrade steady-state tracking. Eliminating the resonance (option D) improves damping but doesn't directly increase bandwidth — it might decrease it if the resonance was helping."

- question: "A linear time-invariant system driven by a sinusoidal input at frequency ω can produce output components at frequencies other than ω, including harmonics at 2ω and 3ω."
  type: true-false
  answer: false
  explanation: "Linearity and time-invariance together guarantee that a sinusoidal input at frequency ω produces a sinusoidal output at exactly the same frequency ω — no other frequencies. The output differs only in amplitude (scaled by |G(jω)|) and phase (shifted by ∠G(jω)). Harmonic generation (outputs at 2ω, 3ω) is a signature of nonlinear systems. This LTI property is the foundation of frequency response analysis: it means knowing |G(jω)| and ∠G(jω)| for all ω is sufficient to predict the steady-state output for any input, since any signal can be decomposed into sinusoids via Fourier analysis."

- question: "A system with a phase margin of 10° at its gain crossover frequency is closed-loop stable, but a small increase in loop gain could cause it to become unstable."
  type: true-false
  answer: true
  explanation: "Phase margin is the additional phase lag (beyond −180°) at the frequency where open-loop gain crosses 0 dB. A phase margin of 10° means the system is 10° away from the −180° threshold that marks the onset of regenerative feedback and instability. Increasing the loop gain raises the magnitude plot, moving the gain crossover frequency to a higher frequency where the phase is typically more negative — potentially pushing phase beyond −180° and destabilizing the closed-loop system. A healthy design typically targets phase margins of 45–60°. At 10°, the system is stable but barely so — any gain increase, component variation, or high-frequency unmodeled dynamics could push it over the edge."

- question: "Why is the Bode plot — showing magnitude and phase versus frequency — sufficient to completely describe how a linear time-invariant system responds to any arbitrary input signal?"
  type: short-answer
  answer: "By Fourier analysis, any bounded, well-behaved signal can be decomposed into a sum (or integral) of sinusoids at different frequencies and amplitudes. The defining property of LTI systems is that a sinusoidal input at frequency ω produces a sinusoidal output at the same frequency ω, scaled by |G(jω)| and shifted by ∠G(jω)|. Therefore, the response to any input can be computed by: (1) decomposing the input into its frequency components, (2) scaling each component's amplitude by the system's magnitude response at that frequency, (3) shifting each component's phase by the system's phase response, and (4) superimposing (by linearity). The Bode plot is thus a complete transfer function for arbitrary inputs — it contains all information about steady-state behavior across all possible signals."
  explanation: "This argument relies on two pillars: the completeness of Fourier representation (any signal = sum of sinusoids) and the linearity of the LTI response (superposition holds). Together, they reduce any input-output calculation to reading off amplitude and phase at each frequency from the Bode plot. This is also why frequency domain methods are so powerful for control design: rather than reasoning about the time-domain response to arbitrary inputs directly, you design the system to have the right Bode plot shape (correct bandwidth, adequate phase margin, good low-frequency gain), and the time-domain behavior follows."
```

## Explainer

From your work on transfer functions, you know that a system's behavior is captured by G(s), evaluated as a rational function of the Laplace variable s. From Bode plot construction, you know how to sketch the magnitude and phase of G(jω) — the transfer function evaluated along the imaginary axis — as a function of frequency. Now we focus on what this picture actually *tells* you about the system, and why the frequency domain is such a powerful lens for control design.

The core physical insight: a linear time-invariant system driven by a sinusoidal input at frequency ω produces, in steady state, a sinusoidal output at the same frequency ω — scaled by |G(jω)| and shifted in phase by ∠G(jω). No other frequencies are generated. This is the defining property of LTI systems, and it is why the frequency response is complete: knowing |G(jω)| and ∠G(jω)| for all ω tells you everything about how the system processes any signal (since any signal can be decomposed into sinusoids). **Magnitude response** |G(jω)| answers: at this frequency, does the system amplify or attenuate? Values above 1 (positive dB) mean amplification; below 1 (negative dB) mean attenuation. **Phase response** ∠G(jω) answers: how much does the output lag or lead the input? Negative phase (lag) is typical for physical systems with inertia — the output trails the input, reflecting that the system takes time to respond.

Reading the Bode plot tells you immediately where the system can and cannot track signals. The **bandwidth** — typically the frequency where |G(jω)| drops to −3 dB — defines the usable tracking range. Inputs varying faster than bandwidth are attenuated; the system cannot faithfully follow them. A **resonant peak** in the magnitude plot (a bump above 0 dB near the natural frequency ω_n) signals a lightly damped system that will oscillate when disturbed — the peak height is related to the damping ratio: peak ≈ 1/(2ζ) for small ζ. The phase plot is equally critical for stability analysis. As phase approaches −180°, the system's feedback is becoming regenerative rather than stabilizing. The margin of phase above −180° at the gain crossover frequency is the **phase margin** — a direct measure of how close the closed-loop system is to instability. Both bandwidth and phase margin are read directly off the Bode plot.

The frequency response is also a **system identification** tool. If you inject sinusoids of known frequency and amplitude into a physical system and measure the output amplitude and phase shift, you directly measure |G(jω)| and ∠G(jω)| — without needing to know the system's differential equations. The shape of the measured curves tells you the system's order (from the high-frequency roll-off slope), its natural frequencies (from peaks in the magnitude), and its damping (from how sharp those peaks are). For control design, the frequency domain gives you direct design handles: a compensator is chosen to reshape the open-loop Bode plot — raising the gain crossover frequency to increase bandwidth, adding phase lead near crossover to improve phase margin, or adding a notch to suppress a resonance. The frequency response connects the mathematical machinery of transfer functions to the physical behavior you actually need to control.
