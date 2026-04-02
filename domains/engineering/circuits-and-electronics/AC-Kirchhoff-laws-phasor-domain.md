---
id: AC-Kirchhoff-laws-phasor-domain
title: AC Kirchhoff's Laws in the Phasor Domain
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-conversion-and-representation
  type: hard
- id: complex-impedance-networks-ac
  type: hard
- id: complex-exponential-form
  type: soft
builds-toward:
- AC-power-calculation-and-factor
- passive-filter-transfer-function-analysis
tags:
- Kirchhoff-laws
- phasor-domain
- AC-analysis
stage: advanced
status: validated
---

# AC Kirchhoff's Laws in the Phasor Domain

## Core Idea
Kirchhoff's voltage and current laws apply directly to phasors: ΣV̅ = 0 around a loop and ΣI̅ = 0 at a node. Nodal and mesh analysis, superposition, and Thévenin/Norton equivalents all work in the phasor domain. This unified approach eliminates the need to solve differential equations for AC steady state.

## Questions

```yaml
- question: "An AC circuit has three impedances in a loop: Z₁ = 10Ω (resistor), Z₂ = j15Ω (inductor), Z₃ = −j5Ω (capacitor), and a source phasor V̅_s = 100∠0° V. Using KVL in the phasor domain, what equation describes the loop?"
  type: multiple-choice
  options:
    - "V̅_s = I̅(Z₁ + Z₂ + Z₃) = I̅(10 + j10) — the phasor current times the total complex impedance"
    - "V̅_s = I̅·Z₁ + I̅·Z₂ + I̅·Z₃ only after converting each phasor back to a sinusoidal time-domain expression"
    - "KVL doesn't apply directly to AC circuits because voltage and current are out of phase"
    - "V̅_s = |Z₁| + |Z₂| + |Z₃| multiplied by the peak current amplitude"
  answer: 0
  explanation: "KVL in the phasor domain works exactly as in DC: the sum of phasor voltage drops around a loop equals the source phasor. Since the same phasor current I̅ flows through each series impedance, the voltage across each element is I̅·Zₙ, and their sum equals V̅_s. The total impedance is Z₁ + Z₂ + Z₃ = 10 + j15 − j5 = 10 + j10 Ω. No time-domain conversion is needed — the phasor domain turns what would be a differential equation problem into straightforward complex algebra."

- question: "What is the fundamental reason that DC circuit analysis techniques — nodal analysis, mesh analysis, Thévenin equivalents — transfer directly to AC circuits in the phasor domain?"
  type: multiple-choice
  options:
    - "AC circuits are mathematically identical to DC circuits when operating at steady state"
    - "The phasor transform converts time-domain differential equations (governing inductors and capacitors) into algebraic equations over complex numbers, restoring the same mathematical structure as DC analysis"
    - "KVL and KCL only hold for DC circuits, but phasors allow engineers to approximate them for AC"
    - "Phasors eliminate the imaginary parts of impedance, reducing AC circuits to equivalent resistive networks"
  answer: 1
  explanation: "The reason these techniques transfer is structural, not accidental. In the time domain, inductors and capacitors introduce derivatives (v = L di/dt, i = C dv/dt), making circuit equations differential equations. The phasor transform, applied to sinusoidal steady state, converts differentiation to multiplication by jω — turning differential equations into algebraic equations. Once the equations are algebraic, all standard linear circuit analysis techniques (which are fundamentally algebraic methods for solving linear systems) apply directly, with complex numbers instead of real ones."

- question: "Kirchhoff's voltage and current laws hold for phasors: the sum of phasor voltages around a closed loop is zero, and the sum of phasor currents into a node is zero."
  type: true-false
  answer: true
  explanation: "KVL and KCL are conservation laws — conservation of energy (voltage) and conservation of charge (current) — and they apply to instantaneous values of voltage and current at every moment in time. Since phasors represent sinusoidal steady-state signals and the conservation laws hold at every instant, they must also hold for phasors (the complex amplitudes encoding magnitude and phase). The arithmetic is complex rather than real, but the structure of the equations is identical."

- question: "Thévenin's theorem can seldom be applied in the phasor domain because the equivalent circuit is expected to capture phase relationships between voltages that a simple phasor source and series impedance cannot represent."
  type: true-false
  answer: false
  explanation: "Thévenin's theorem applies fully in the phasor domain. The Thévenin equivalent consists of an open-circuit phasor voltage V̅_th (a complex number encoding both amplitude and phase) in series with a Thévenin impedance Z_th (also complex). The phase relationships between the original circuit's sources and elements are fully captured in V̅_th and Z_th. The procedure is identical to DC: find the open-circuit voltage phasor and the input impedance with independent sources deactivated. There is no information loss."

- question: "A student solves an AC steady-state circuit problem in the time domain by writing and solving differential equations. How would solving the same problem in the phasor domain differ, and why is the phasor approach preferred for AC steady-state analysis?"
  type: short-answer
  answer: "In the time domain, inductors and capacitors introduce derivatives (v_L = L di/dt, i_C = C dv/dt), making KVL and KCL yield coupled differential equations. For sinusoidal steady state, these must be solved, then matched to the forcing frequency. In the phasor domain, these derivatives become algebraic multiplications (jωL for an inductor, 1/jωC for a capacitor), turning the differential equations into a linear algebraic system over complex numbers. The same nodal or mesh equations are then solved using standard linear algebra, yielding phasors directly. The phasor approach is preferred because it reduces the mathematical complexity by an entire level — differential equations become algebraic — while capturing all steady-state amplitude and phase information in the complex numbers."
  explanation: "The key insight is that the phasor transform exploits the specific structure of sinusoidal steady state: when inputs are sinusoidal and the circuit is linear and time-invariant, all voltages and currents are sinusoidal at the same frequency. This allows the frequency-dependent part (the derivative operator d/dt) to be replaced by the constant jω. The transform is exact for steady-state analysis — no approximation is made."
```

## Explainer

You've already seen that phasors convert sinusoidal voltages and currents into complex numbers, and that impedance Z = R + jX generalizes resistance to inductors and capacitors. The payoff for all that setup arrives now: **Kirchhoff's laws work on phasors exactly as they work on DC values**, except you use complex arithmetic instead of real arithmetic. KVL says the sum of phasor voltages around any closed loop is zero; KCL says the sum of phasor currents into any node is zero. The fundamental conservation principles don't change — only the numbers become complex.

The practical power of this is enormous. Every DC analysis technique you've learned — nodal analysis, mesh analysis, superposition, voltage dividers, Thévenin equivalents — transfers directly to AC circuits with one substitution: replace resistance R with complex impedance Z. A voltage divider with two resistors becomes a voltage divider with two impedances, and the output phasor is simply Z₂/(Z₁ + Z₂) times the input phasor. The algebra looks identical; the result is a complex number encoding both amplitude and phase. This is far easier than solving the differential equations that describe inductor and capacitor behavior in the time domain.

For nodal analysis in the phasor domain, assign node voltage phasors as unknowns, write KCL at each node using V̅/Z for each branch current, and solve the resulting system of linear equations — now over the complex numbers. The node voltages you find are phasors: their magnitudes are the AC amplitudes at that node, and their angles are the phase shifts relative to your reference. Thévenin equivalents work the same way: find the open-circuit phasor voltage V̅_th and the Thévenin impedance Z_th by deactivating independent sources (short voltage sources, open current sources), then replace the circuit with V̅_th in series with Z_th.

The key conceptual move here is recognizing that the phasor domain doesn't just make calculation easier — it reveals the structure of AC circuits. A circuit's response at a given frequency is completely described by complex numbers (phasors and impedances). As you extend this to analyze filters and power, you'll be asking how the ratio V̅_out/V̅_in depends on frequency ω. That ratio — the **transfer function** — is the bridge from phasor-domain analysis to frequency-response analysis, and it is built directly from the KVL and KCL equations you write here.
