---
id: ac-power-analysis-circuits
title: AC Power Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-circuit-analysis-methods
  type: hard
- id: electric-power
  type: soft
- id: ac-power-and-resonance
  type: soft
builds-toward:
- resonance-circuits
tags:
- real-power
- reactive-power
- apparent-power
- power-factor
- complex-power
- RMS
- power-factor-correction
stage: formal-systems
status: validated
---

# AC Power Analysis

## Core Idea
Instantaneous power p(t) = v(t)·i(t) oscillates at twice the source frequency in AC circuits. Average (real) power P = ½Vm·Im·cos(θ) in watts is actually dissipated; reactive power Q = ½Vm·Im·sin(θ) in VARs oscillates between source and reactive elements without dissipation. Complex power S = P + jQ = ½·V·I* (I* = conjugate of current phasor) unifies these. Power factor PF = cos(θ) = P/|S| measures how efficiently real power is delivered; unity PF is ideal. Power factor correction adds reactive elements to minimize reactive power demand from the source.

## How It's Best Learned
Compute complex power for simple RLC loads and verify that the real parts of complex power are conserved across all branches (Tellegen's theorem). Practice power factor correction by computing the required shunt capacitance to bring an inductive load to unity power factor.

## Common Misconceptions
- Equating apparent power |S| with real power P — only P performs useful work; |S| is the product of RMS voltage and current magnitudes.
- Using peak values in power formulas without the ½ factor, or using RMS values with the ½ factor — the two forms are equivalent but must not be mixed.
- Assuming reactive power is wasted — it is exchanged between source and reactive elements, but drawing it stresses generation and transmission equipment.

## Questions

```yaml
- question: "An industrial motor draws 100 kVA of apparent power at a power factor of 0.6. A capacitor bank is added that improves the power factor to 1.0. What happens to the real power delivered to the motor?"
  type: multiple-choice
  options:
    - "Real power increases to 100 kW because the power factor is now 1.0"
    - "Real power decreases to 60 kW because the reactive power is eliminated"
    - "Real power remains at 60 kW — the capacitor corrects the power factor without changing the useful power delivered to the motor"
    - "Real power becomes zero because the capacitor and inductor cancel each other"
  answer: 2
  explanation: "Real power P = |S|·cos(θ) = 100 kVA × 0.6 = 60 kW before correction. The capacitor adds leading reactive power (Q < 0) that cancels the motor's lagging reactive power (Q > 0). When Q_total → 0, the power factor → 1.0 and |S| → 60 kW. The motor still receives exactly 60 kW of real power — its operation is unchanged. What changed is that the source no longer needs to supply reactive current: the capacitor supplies it locally. This is why power factor correction reduces utility bills without affecting how equipment performs."

- question: "A load draws voltage and current that are perfectly in phase (θ = 0). What does this imply about its reactive power?"
  type: multiple-choice
  options:
    - "Reactive power is maximized because the load is purely resistive"
    - "Reactive power Q = 0, because Q = ½Vm·Im·sin(0) = 0"
    - "Apparent power equals zero because no phase difference exists"
    - "Reactive power is undefined when voltage and current are in phase"
  answer: 1
  explanation: "Reactive power Q = ½Vm·Im·sin(θ). When θ = 0 (unity power factor), sin(0) = 0, so Q = 0. This is a purely resistive load — all power delivered is real power. Option A is backwards: a purely resistive load minimizes reactive power (Q = 0), not maximizes it. Apparent power |S| = ½Vm·Im is nonzero (option C is wrong) — it equals real power P when Q = 0."

- question: "Reactive power is wasted power that has no physical significance for power system design, since it averages to zero over a full cycle."
  type: true-false
  answer: false
  explanation: "While reactive power averages to zero in terms of energy delivered to the load, it still flows back and forth between the source and reactive elements — and that flowing current must be carried by generators, transformers, and transmission lines. These are sized by the current they carry (apparent power |S|), not just real power P. A 0.7 power factor load requires 43% more current capacity than a unity PF load delivering the same real power. Power factor correction exists precisely because reactive power, though not 'consumed,' has real economic costs in equipment sizing."

- question: "If voltage leads current by 30° in an AC circuit, the load is capacitive."
  type: true-false
  answer: false
  explanation: "If voltage *leads* current (positive θ, where θ is the angle of voltage minus angle of current), the load is *inductive*, not capacitive. In an inductive load, current lags behind the voltage — equivalently, voltage leads current. In a capacitive load, current leads voltage (negative θ). This distinction is critical for power factor correction: inductive loads (lagging PF) are corrected by adding shunt capacitors; capacitive loads (leading PF) are corrected by adding inductors."

- question: "Explain why apparent power |S| determines the required rating of electrical equipment like transformers and generators, rather than real power P."
  type: short-answer
  answer: "Generators, transformers, and transmission lines are physically limited by the current they can carry without overheating (I²R losses in conductors and windings). The current magnitude is determined by apparent power: I_rms = |S|/V_rms, regardless of the phase angle. A machine must carry the full current corresponding to |S| even if only the P component does useful work — reactive current heats conductors just as much as resistive current. This is why equipment is rated in volt-amperes (VA or kVA), not watts. Power factor correction reduces |S| toward P by eliminating Q, so the source sees less current for the same delivered real power."
  explanation: "This is why utilities charge large industrial customers a power factor penalty: low power factor means the utility must size equipment for large apparent power even when the real load is moderate. The penalty incentivizes customers to install local reactive compensation (capacitor banks) and reduce reactive demand on the grid."
```

## Explainer

In DC circuits, power is simple: P = VI, always positive, always consumed. In AC circuits, voltage and current are sinusoids that oscillate — and when they're out of phase with each other, the power story becomes richer and more useful. Your prerequisite on AC circuit analysis methods gave you phasors and impedance. Now you apply that machinery to power: not just how much energy flows, but what form it takes and how efficiently it's delivered.

Start from first principles. If v(t) = Vm·cos(ωt) and i(t) = Im·cos(ωt − θ), the instantaneous power p(t) = v(t)·i(t). Multiplying out using the product-to-sum trig identity yields a constant term plus a term oscillating at 2ω. The constant term is **real power** P = ½·Vm·Im·cos(θ) — measured in watts, this is the average energy delivered per second and is the only part that does sustained useful work (turns motors, generates heat, lights LEDs). The oscillating term involves **reactive power** Q = ½·Vm·Im·sin(θ), measured in VARs (volt-ampere reactive). Reactive power represents energy sloshing back and forth between the source and the inductors and capacitors in the load — it averages to zero over a full cycle.

**Complex power** S = P + jQ = ½·V̅·Ī* elegantly unifies these into one phasor quantity (where Ī* is the complex conjugate of the current phasor). The magnitude |S| is **apparent power** in volt-amperes — what you'd compute from the product of RMS voltage and RMS current without knowing the phase angle. The ratio P/|S| is the **power factor** (PF = cos θ), a number between 0 and 1 measuring how efficiently apparent power converts to real power. Unity power factor means all power drawn from the source is delivered as useful work. A lagging power factor (typical of inductive loads like motors) means the source must supply extra current to maintain the magnetic fields in the load, even though that current returns to the source each half-cycle.

That "extra current" is why reactive power matters economically. Transmission lines, transformers, and generators are sized for the current they carry — |S|/V — not the useful power P. A large industrial motor drawing current at PF = 0.7 forces the utility to size equipment for 43% more current than a PF = 1.0 load of the same real power. **Power factor correction** fixes this by adding a shunt capacitor in parallel with the inductive load. Capacitors have leading reactive power (Q < 0) that offsets the lagging reactive power of the inductor (Q > 0). If you size the capacitor correctly, Q_total → 0, the power factor approaches unity, and the source only sees the real power load — no reactive current component. The real power delivered to the motor is unchanged; only the reactive demand on the source is eliminated. This is one of the most economically significant circuit design choices in industrial power systems.
