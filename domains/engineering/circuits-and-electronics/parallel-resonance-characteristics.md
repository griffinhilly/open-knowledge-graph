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
stage: formal-systems
status: draft
---

# Parallel Resonance Characteristics

## Core Idea
In a parallel RLC circuit, resonance also occurs at ω₀ = 1/√(LC), but with opposite characteristics: impedance is maximum, current is minimum, and the circuit presents maximum impedance to the source. Parallel resonance is used in tank circuits for oscillators, AM radio tuners, and notch filters. At resonance, the reactive currents in the inductor and capacitor are equal and opposite, circulating internally.

## Explainer

From your study of impedance and admittance, you know that capacitors and inductors respond oppositely to frequency — a capacitor's impedance falls with frequency (Z_C = 1/jωC) while an inductor's rises (Z_L = jωL). This creates a frequency where their effects exactly cancel. The behavior at that cancellation point is what resonance is about, and whether the components are in series or parallel determines whether cancellation means maximum or minimum impedance.

In a **parallel RLC circuit**, the resistor, inductor, and capacitor all share the same terminal voltage. The total admittance of the parallel combination is Y = 1/R + 1/jωL + jωC. At resonance, the imaginary parts of the admittance cancel: the inductive susceptance 1/jωL and the capacitive susceptance jωC sum to zero when ω₀ = 1/√(LC) — the same resonant frequency as series resonance. But the circuit-level consequence is the opposite: at resonance, total admittance equals just 1/R, which is *minimum* admittance and therefore *maximum* impedance. A parallel resonant circuit looks like a large resistor to an external source at the resonant frequency, drawing minimum current from that source.

The physical reason is energy storage and circulation. At resonance, the inductor and capacitor exchange energy back and forth in a closed loop — current swings from flowing through the inductor to flowing through the capacitor each half-cycle, with no net reactive current drawn from the external source. This circulating current can be much larger than the source current; the **quality factor Q = R/ω₀L = ω₀RC** measures how much larger. A high-Q parallel resonant circuit (often called a **tank circuit**) stores energy efficiently, oscillating with little loss per cycle. The bandwidth — the frequency range over which the impedance remains near its peak — is BW = ω₀/Q, the inverse of Q. High Q means narrow bandwidth and sharp frequency selectivity.

This selectivity is what makes parallel resonance practically powerful. An **AM radio tuner** uses a variable capacitor in a parallel LC circuit: adjusting C shifts ω₀ to match a station's carrier frequency, at which point the tank circuit presents high impedance and passes the selected signal preferentially. A **notch filter** exploits the same property in reverse: by placing the parallel resonant circuit in a shunt path, maximum impedance at resonance is avoided, and frequencies near resonance are blocked. Oscillator circuits use the tank circuit's energy storage to sustain oscillation — the capacitor and inductor naturally trade energy at ω₀, and a small amplifier replaces the losses. In every case, the key parameters are the resonant frequency ω₀ and the quality factor Q, which together determine where the circuit's behavior is centered and how sharply it discriminates against other frequencies.


