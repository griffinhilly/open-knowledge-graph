---
id: resonance-circuits
title: Resonance in RLC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-analysis
  type: hard
- id: second-order-transient-circuits
  type: soft
- id: ac-power-analysis-circuits
  type: soft
builds-toward:
- frequency-response-and-bode-plots
- passive-filter-design
tags:
- resonance
- quality-factor
- bandwidth
- series-resonance
- parallel-resonance
- selectivity
stage: formal-systems
status: validated
---

# Resonance in RLC Circuits

## Core Idea
Resonance occurs at ω₀ = 1/√(LC) where inductive and capacitive reactances are equal in magnitude and cancel. In a series RLC circuit at resonance, impedance is purely resistive (minimum), and current is maximum. In a parallel RLC circuit, admittance is minimum (impedance maximum), and the circuit draws minimum current from the source. The quality factor Q = ω₀L/R (series) measures sharpness of the resonance peak; the −3 dB bandwidth BW = ω₀/Q. High-Q circuits exhibit strong frequency selectivity and are used in filters, oscillators, and impedance matching networks.

## How It's Best Learned
Plot impedance magnitude versus frequency for series and parallel RLC circuits on the same graph. Compute ω₀, Q, and bandwidth from component values and locate the half-power frequencies on the plot. Explore how varying R changes Q and bandwidth while keeping ω₀ fixed.

## Common Misconceptions
- Using the same Q formula for series and parallel circuits — Q = ω₀L/R for series but Q = R/(ω₀L) = Rω₀C for parallel.
- Expecting voltages across individual reactive elements to equal the source voltage at resonance — in a high-Q series circuit, they can greatly exceed the source voltage by a factor of Q.
- Confusing bandwidth (frequency interval between half-power points) with the resonant frequency itself.

## Questions

```yaml
- question: "A series RLC circuit has R = 10 Ω, L = 100 mH, C = 100 μF, and is driven by a 1V sinusoidal source at resonance. The quality factor Q ≈ 10. What is the approximate voltage across the capacitor at resonance?"
  type: multiple-choice
  options:
    - "1 V — the capacitor voltage equals the source voltage at resonance"
    - "0 V — the capacitor and inductor voltages cancel, so the capacitor contributes nothing"
    - "10 V — the capacitor voltage is Q times the source voltage"
    - "0.707 V — the half-power condition applies at resonance"
  answer: 2
  explanation: "In a series RLC circuit at resonance, the voltages across the inductor and capacitor are each Q times the source voltage — but they are equal in magnitude and opposite in phase, so they cancel in the total circuit voltage. With Q = 10 and V_source = 1V, V_C = V_L = QV_source = 10V. This voltage magnification is the subtlest and most counterintuitive result in resonance analysis. Option A reflects the common misconception that 'the voltages cancel, so they must each be 1V.' They cancel in *sum* but individually they are Q times larger. This is why high-Q resonant circuits in power systems can be dangerous."

- question: "Below the resonant frequency, a series RLC circuit behaves like which type of load?"
  type: multiple-choice
  options:
    - "Inductive — current lags the source voltage"
    - "Capacitive — current leads the source voltage"
    - "Purely resistive — the reactive elements cancel exactly at all sub-resonant frequencies"
    - "Open circuit — no current flows below resonance"
  answer: 1
  explanation: "Below resonance (ω < ω₀), the capacitive reactance 1/(ωC) is large and dominates over the inductive reactance ωL, so the net reactance is capacitive (negative imaginary). In a capacitive circuit, current leads voltage. Above resonance (ω > ω₀), the inductive reactance dominates, the net reactance is inductive, and current lags voltage. At resonance, the reactances cancel exactly and the circuit is purely resistive, with current in phase with voltage and at maximum magnitude."

- question: "In a series RLC circuit at resonance, the voltages across the inductor and capacitor individually exceed the source voltage by a factor equal to the quality factor Q."
  type: true-false
  answer: true
  explanation: "This is the voltage magnification property of resonant circuits. At resonance, the current is I = V/R (maximum). The voltage across the inductor is V_L = IωL = (V/R)ω₀L = V × (ω₀L/R) = QV. Similarly, V_C = I/(ωC) = QV. Both V_L and V_C equal QV, but they are 180° out of phase with each other, so they cancel in the KVL loop. A high-Q series circuit is effectively an AC voltage amplifier for the reactive elements, even though the source 'sees' only the resistance R."

- question: "In a parallel RLC circuit at resonance, the impedance is at a minimum and the circuit draws maximum current from the source."
  type: true-false
  answer: false
  explanation: "This describes series resonance, not parallel resonance. The parallel circuit is the dual of the series circuit: at resonance, the parallel impedance is at a MAXIMUM (the admittance is minimum), and the circuit draws MINIMUM current from the source. Internally, large circulating currents flow between L and C — they exchange energy back and forth — but these cancel in the external circuit, so the source 'sees' only a high resistance load. This is why parallel resonant circuits are used as tank circuits in oscillators and as high-impedance notch elements in filter design."

- question: "Explain the physical mechanism of resonance in an RLC circuit in terms of energy exchange between the inductor and capacitor."
  type: short-answer
  answer: "At resonance, the inductor and capacitor exchange energy back and forth at exactly the resonant frequency ω₀ = 1/√(LC). When the capacitor is fully charged, it begins to discharge through the inductor, building up a magnetic field. When the capacitor is discharged, the inductor's collapsing magnetic field drives current that recharges the capacitor with opposite polarity. This oscillation continues at the natural frequency set by L and C. At resonance, the energy stored in the electric field of the capacitor and the magnetic field of the inductor are equal on average. The only energy actually consumed comes from the resistance, which dissipates the circulating energy as heat."
  explanation: "The quality factor Q measures how much energy is stored relative to how much is lost per cycle: Q = 2π × (peak energy stored)/(energy dissipated per cycle). High Q means the circuit stores much more energy than it loses per oscillation — the energy sloshes back and forth many times before being significantly dissipated. This is why high-Q circuits have narrow bandwidth and sharp frequency selectivity: they 'remember' the resonant frequency strongly and reject off-resonance excitation."
```

## Explainer

From your impedance analysis work, you know that Z_L = jωL increases with frequency while Z_C = 1/(jωC) decreases with frequency. Resonance is the frequency at which these two reactive elements cancel each other out. In a series RLC circuit, the total impedance is Z = R + j(ωL − 1/ωC). The imaginary part — the net reactance — equals zero when ωL = 1/ωC, giving the **resonant frequency** ω₀ = 1/√(LC). At this frequency, the circuit looks purely resistive, and current reaches its maximum value V/R, limited only by the resistance.

The physical picture is energy sloshing back and forth. Below resonance, the capacitor dominates — the circuit is capacitive and current leads voltage. Above resonance, the inductor dominates — the circuit is inductive and current lags voltage. At ω₀, the energy stored in the electric field of the capacitor and the magnetic field of the inductor are equal on average, and they exchange energy continuously with no net reactive power drawn from the source. The only real power consumed is in the resistance.

The **quality factor** Q measures how sharply this resonance peaks. Q = ω₀L/R for a series circuit: a high-Q circuit (low R, or high L/C ratio) has a very narrow resonance peak, while a low-Q circuit has a broad, flat response. The −3 dB **bandwidth** BW = ω₀/Q defines the frequency range over which the circuit responds strongly. A radio tuner exploits this: high Q means the circuit responds strongly to a narrow band of frequencies, rejecting adjacent stations. The half-power frequencies are ω₁ = ω₀ − BW/2 and ω₂ = ω₀ + BW/2 (approximately, for high Q).

A subtle consequence of high Q is voltage magnification. In a series RLC circuit at resonance, the voltages across the inductor and capacitor are each Q times the source voltage — they are large and nearly equal in magnitude but opposite in sign, so they cancel in the total. If Q = 50 and the source is 1 V, the voltage across the capacitor alone can be 50 V. This effect is useful in filter design and impedance matching, but dangerous if not anticipated — a high-Q resonant circuit in a power system can produce voltages far exceeding design limits. The parallel RLC circuit is the dual: at resonance, impedance is maximum (not minimum), and the circuit draws minimum current from the source while circulating large currents internally between L and C.
