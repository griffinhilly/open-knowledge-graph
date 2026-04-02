---
id: parallel-resonance-characteristics
title: Parallel Resonance Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-admittance-networks
  type: hard
builds-toward:
- quality-factor-bandwidth-tradeoff
- frequency-response-analysis-bode
tags:
- resonance
- parallel-circuits
- frequency-response
stage: advanced
status: validated
---

# Parallel Resonance Characteristics

## Core Idea
In a parallel RLC circuit, resonance also occurs at ω₀ = 1/√(LC), but with opposite characteristics: impedance is maximum, current is minimum, and the circuit presents maximum impedance to the source. Parallel resonance is used in tank circuits for oscillators, AM radio tuners, and notch filters. At resonance, the reactive currents in the inductor and capacitor are equal and opposite, circulating internally.

## Questions

```yaml
- question: "A parallel RLC circuit is driven by an AC current source. As the driving frequency sweeps from low to high, what happens to the voltage across the circuit as it passes through the resonant frequency?"
  type: multiple-choice
  options:
    - "Voltage drops to a minimum at resonance because the reactive currents cancel, reducing total impedance"
    - "Voltage reaches a maximum at resonance because impedance is maximum at that frequency"
    - "Voltage remains constant because a current source maintains fixed current regardless of impedance"
    - "Voltage reaches a maximum because the capacitor and inductor simultaneously draw maximum current"
  answer: 1
  explanation: "At parallel resonance, the imaginary parts of the admittance cancel (inductive susceptance and capacitive susceptance sum to zero), leaving only the real admittance 1/R. Total admittance is minimum, so total impedance is maximum. For a current source driving the circuit, V = I × Z, so maximum impedance means maximum voltage. This is the direct opposite of series resonance, where impedance is minimum and current is maximum. The parallel resonant circuit's defining characteristic is its maximum impedance at ω₀ — it looks like a large pure resistor to the source."

- question: "An AM radio tuner uses a parallel LC circuit with a variable capacitor. The engineer wants the tuner to sharply distinguish the 1000 kHz station from the 1010 kHz station. What circuit property is most critical?"
  type: multiple-choice
  options:
    - "Low resonant frequency, so the LC values are large enough to tune precisely"
    - "High Q factor, because narrow bandwidth allows the tuner to select one station while rejecting adjacent ones"
    - "Low Q factor, so the tuner's frequency response is flat and captures the entire AM band equally"
    - "High resistance R, because more resistance dissipates unwanted frequencies more effectively"
  answer: 1
  explanation: "Q = R/(ω₀L) = ω₀RC for a parallel circuit, and bandwidth BW = ω₀/Q. High Q means narrow bandwidth — the impedance peak is sharp, so only frequencies very close to ω₀ receive the high-impedance selectivity that passes the signal. A 10 kHz channel separation in the AM band requires a narrow enough bandwidth to reject the adjacent station; a low-Q circuit with wide bandwidth would pass multiple stations simultaneously. Higher resistance R increases Q (less energy is dissipated per cycle), producing a sharper, more selective peak. This is why tank circuit Q is a primary specification in RF design."

- question: "At resonance in a parallel RLC circuit, the circulating current between the inductor and capacitor can be much larger than the current supplied by the external source."
  type: true-false
  answer: true
  explanation: "True, and this is the physical meaning of Q. The inductor current I_L = V/(ω₀L) and capacitor current I_C = Vω₀C are equal in magnitude and opposite in phase at resonance — they circulate internally between L and C each half-cycle. The source only needs to supply the energy lost in the resistance. The ratio of circulating current to source current is exactly Q = R/(ω₀L). A Q of 100 means the internal reactive currents are 100 times larger than the source current. This energy-storage-and-circulation property is why parallel resonant circuits are called 'tank circuits' — they act as reservoirs of oscillating energy."

- question: "A series RLC and a parallel RLC circuit with identical L, C, and R values will reach resonance at different frequencies because their energy storage configurations differ."
  type: true-false
  answer: false
  explanation: "False. Both series and parallel RLC circuits resonate at ω₀ = 1/√(LC), regardless of R. The resonant frequency is determined purely by the reactive elements L and C — it is the frequency at which their reactances are equal in magnitude (ω₀L = 1/ω₀C). What differs dramatically between series and parallel resonance is the behavior AT resonance: series resonance gives minimum impedance and maximum current, while parallel resonance gives maximum impedance and minimum current. Same frequency, opposite impedance characteristics."

- question: "Explain why a parallel resonant circuit (tank circuit) draws minimum current from the source at resonance, even though the inductor and capacitor each carry large reactive currents at that same instant."
  type: short-answer
  answer: "At resonance, the inductor current and capacitor current are equal in magnitude and exactly 180° out of phase (one leads, one lags the voltage by 90°). They cancel each other at the circuit terminals — no net reactive current is visible to the external source. The source only needs to replenish the energy dissipated in the resistance R; all the reactive energy is already circulating internally between L and C each half-cycle. The source current is therefore just V/R (the resistive component), which is minimum when V = I_source × Z is expressed correctly — at resonance Z = R (maximum), so for a given voltage, source current = V/R (minimum). The large internal currents are sustained by the stored energy being continuously exchanged between the magnetic field of the inductor and the electric field of the capacitor."
  explanation: "The tank circuit analogy is apt: like a pendulum swinging between kinetic and potential energy, the LC tank swings energy between magnetic (inductor) and electric (capacitor) forms. Each full cycle, energy flows L→C→L→C with minimal external replenishment needed. The higher Q, the more cycles the energy completes per unit of dissipation, and the smaller the source current relative to the internal currents."
```

## Explainer

From your study of impedance and admittance, you know that capacitors and inductors respond oppositely to frequency — a capacitor's impedance falls with frequency (Z_C = 1/jωC) while an inductor's rises (Z_L = jωL). This creates a frequency where their effects exactly cancel. The behavior at that cancellation point is what resonance is about, and whether the components are in series or parallel determines whether cancellation means maximum or minimum impedance.

In a **parallel RLC circuit**, the resistor, inductor, and capacitor all share the same terminal voltage. The total admittance of the parallel combination is Y = 1/R + 1/jωL + jωC. At resonance, the imaginary parts of the admittance cancel: the inductive susceptance 1/jωL and the capacitive susceptance jωC sum to zero when ω₀ = 1/√(LC) — the same resonant frequency as series resonance. But the circuit-level consequence is the opposite: at resonance, total admittance equals just 1/R, which is *minimum* admittance and therefore *maximum* impedance. A parallel resonant circuit looks like a large resistor to an external source at the resonant frequency, drawing minimum current from that source.

The physical reason is energy storage and circulation. At resonance, the inductor and capacitor exchange energy back and forth in a closed loop — current swings from flowing through the inductor to flowing through the capacitor each half-cycle, with no net reactive current drawn from the external source. This circulating current can be much larger than the source current; the **quality factor Q = R/ω₀L = ω₀RC** measures how much larger. A high-Q parallel resonant circuit (often called a **tank circuit**) stores energy efficiently, oscillating with little loss per cycle. The bandwidth — the frequency range over which the impedance remains near its peak — is BW = ω₀/Q, the inverse of Q. High Q means narrow bandwidth and sharp frequency selectivity.

This selectivity is what makes parallel resonance practically powerful. An **AM radio tuner** uses a variable capacitor in a parallel LC circuit: adjusting C shifts ω₀ to match a station's carrier frequency, at which point the tank circuit presents high impedance and passes the selected signal preferentially. A **notch filter** exploits the same property in reverse: by placing the parallel resonant circuit in a shunt path, maximum impedance at resonance is avoided, and frequencies near resonance are blocked. Oscillator circuits use the tank circuit's energy storage to sustain oscillation — the capacitor and inductor naturally trade energy at ω₀, and a small amplifier replaces the losses. In every case, the key parameters are the resonant frequency ω₀ and the quality factor Q, which together determine where the circuit's behavior is centered and how sharply it discriminates against other frequencies.


