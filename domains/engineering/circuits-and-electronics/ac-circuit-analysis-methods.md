---
id: ac-circuit-analysis-methods
title: AC Circuit Analysis Using Phasors
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-analysis
  type: hard
- id: node-voltage-method
  type: hard
- id: mesh-current-method
  type: soft
- id: thevenin-norton-equivalents
  type: soft
- id: operations-with-complex-numbers
  type: hard
- id: ac-circuits-fundamentals
  type: soft
- id: sinusoidal-steady-state-analysis
  type: hard
- id: complex-numbers-intro
  type: hard
- id: complex-exponential-form
  type: soft
builds-toward:
- ac-power-analysis-circuits
- frequency-response-and-bode-plots
- passive-filter-design
- operational-amplifier-fundamentals
tags:
- AC-analysis
- phasor-domain
- nodal-analysis
- mesh-analysis
- superposition-AC
stage: advanced
status: validated
---

# AC Circuit Analysis Using Phasors

## Core Idea
All DC analysis techniques — node voltage, mesh current, superposition, Thevenin/Norton — apply directly to AC circuits by replacing element resistances with complex impedances and sources with their phasor representations. The result is a system of complex algebraic equations whose solution gives phasor voltages and currents. The transfer function H(jω) = Y(jω)/X(jω) describes the ratio of output to input phasors and captures all frequency-domain behavior. When multiple source frequencies are present, superposition must be applied separately at each frequency.

## How It's Best Learned
Solve the same RLC circuit first in the time domain (differential equations) and then with phasors to appreciate the efficiency gain. Draw phasor diagrams to visualize phase relationships between voltages and currents. Practice finding Thevenin equivalents in the frequency domain with complex Z_th.

## Common Misconceptions
- Mixing time-domain quantities with phasor quantities in the same equation — all variables must be in the same domain.
- Analyzing circuits with two different source frequencies simultaneously using a single phasor analysis — each frequency requires a separate analysis.
- Forgetting to convert sources at different phases correctly before applying node or mesh equations.

## Questions

```yaml
- question: "A circuit has two sinusoidal voltage sources: one at 60 Hz and one at 1000 Hz. Which approach correctly applies phasor analysis?"
  type: multiple-choice
  options: ["Represent both sources as phasors and solve the combined node equations simultaneously", "Analyze the circuit at 60 Hz with phasors, then separately at 1000 Hz, then add the time-domain results", "Use the magnitudes of both phasors in KVL without tracking phase angle", "Average the two frequencies and perform a single phasor analysis at 530 Hz"]
  answer: 1
  explanation: "Phasor analysis assumes a single sinusoidal frequency — impedances of inductors (jωL) and capacitors (1/jωC) are defined at a specific ω and take different values at different frequencies. With two source frequencies, the correct method is superposition: analyze the circuit once using only the 60 Hz source (with 60 Hz impedances), then again using only the 1000 Hz source (with 1000 Hz impedances), and sum the resulting time-domain waveforms. Combining them in a single phasor analysis yields incorrect impedance values."

- question: "When writing KCL in the phasor domain for a node connected to a capacitor, it is valid to use the time-domain expression i = C dv/dt alongside phasor currents from other branches in the same equation."
  type: true-false
  answer: false
  explanation: "Phasor analysis requires all quantities in an equation to be in the same domain. In the phasor domain the capacitor relationship becomes I = jωC·V — a complex algebraic equation, not a differential equation. Mixing phasor voltages with the time-domain expression i = C dv/dt produces a mathematically inconsistent equation. You must commit to one domain throughout the analysis."

- question: "What information does the transfer function H(jω) = V_out(jω) / V_in(jω) encode, and why is it more useful than a single time-domain solution?"
  type: short-answer
  answer: "H(jω) is a complex function of frequency encoding both the amplitude ratio |H(jω)| (how the circuit scales the input magnitude) and the phase shift ∠H(jω) (how much the output leads or lags the input) at every frequency ω. A single time-domain solution gives the response to one specific input. H(jω) characterizes the circuit's behavior across all sinusoidal inputs simultaneously, enabling filter design and frequency-response analysis without re-solving the circuit."
  explanation: "Once H(jω) is known, the phasor output for any sinusoidal input at frequency ω is simply V_in · H(jω). This is far more powerful than solving a differential equation anew for each input. The magnitude and phase of H(jω) as functions of frequency are the Bode plot — the standard tool for filter design and stability analysis."
```

## Explainer

When you first learned node voltage or mesh current analysis, you solved DC circuits where every quantity was a real number. Then AC circuits introduced differential equations governing inductors (v = L di/dt) and capacitors (i = C dv/dt), which seemed to demand entirely different techniques. Phasor analysis makes a striking claim: no new techniques are needed. Every DC analysis method — node voltage, mesh current, superposition, Thevenin/Norton — applies directly to AC circuits once you replace resistance with complex impedance and represent sinusoidal sources as phasors.

The foundation is the phasor transform. A sinusoidal signal v(t) = V_m cos(ωt + φ) is represented by the phasor V = V_m∠φ — a complex number that encodes amplitude and phase but discards the common factor e^(jωt) that all quantities share in steady state. When the circuit operates at a single frequency ω, the differential relationships for reactive elements collapse into algebraic ones: the capacitor's i = C dv/dt becomes I = jωC·V, and the inductor's v = L di/dt becomes V = jωL·I. Combined with the resistor's V = IR, these define complex impedances: Z_R = R, Z_C = 1/(jωC), Z_L = jωL. KVL and KCL hold for phasors exactly as they hold for DC quantities, because both are linear superposition relations.

With impedances replacing resistances, you can write node voltage or mesh current equations in the phasor domain by direct inspection — the same procedure as DC analysis, but with complex arithmetic. The solution gives complex phasor voltages; their magnitudes are peak amplitudes and their angles are phase shifts relative to the reference. Thevenin and Norton equivalents generalize to a complex Thevenin impedance Z_th and a frequency-dependent phasor V_th. The entire DC analysis toolkit transfers intact.

The transfer function H(jω) = V_out/V_in (or any output-to-input phasor ratio) is the principal payoff of this approach. Because H(jω) is a function of frequency, it encodes the circuit's behavior for all sinusoidal inputs — not just the one you happen to be analyzing. |H(jω)| gives the magnitude response (does the circuit amplify or attenuate at this frequency?) and ∠H(jω) gives the phase response. A low-pass filter has |H| ≈ 1 at low frequencies and |H| → 0 at high frequencies, which is immediately visible in the transfer function expression but obscured in any particular time-domain solution.

The hard constraint to remember is that phasor analysis assumes a single excitation frequency throughout. Inductor and capacitor impedances (jωL and 1/jωC) depend on ω; they take different numerical values at different frequencies. If a circuit has sources at two different frequencies, you cannot combine them in one phasor analysis — the impedances cannot simultaneously be correct at both frequencies. The correct procedure is superposition: analyze the circuit at each frequency separately using the appropriate impedances, convert each phasor result back to a time-domain sinusoid, then add the time-domain waveforms. This is not an approximation; it is exact for linear circuits.
