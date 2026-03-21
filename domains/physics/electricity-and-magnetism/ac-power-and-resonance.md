---
id: ac-power-and-resonance
title: AC Power and Resonance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: impedance-and-reactance
  type: hard
- id: electric-power
  type: hard
builds-toward:
- electromagnetic-waves
tags:
- AC-power
- resonance
- power-factor
- bandwidth
- transformers
stage: formal-systems
status: validated
---

# AC Power and Resonance

## Core Idea
Average power in an AC circuit is P = V_rms I_rms cos φ, where cos φ is the power factor — only the resistive component dissipates energy. Resonance occurs when X_L = X_C, i.e., ω₀ = 1/√(LC), giving maximum current for a series RLC circuit and minimum impedance. The quality factor Q = ω₀/Δω measures the sharpness of the resonance peak. Transformers use mutual inductance to step voltage up or down while conserving power (V₁/V₂ = N₁/N₂, I₁/I₂ = N₂/N₁).

## How It's Best Learned
Plot impedance |Z| vs. frequency and identify the resonance minimum. Calculate Q for different R values and observe how R broadens the resonance peak. Analyze the transformer equations and explain why high-voltage transmission minimizes resistive losses.

## Common Misconceptions
- Reactive elements (L and C) do not dissipate power on average, even though instantaneous power oscillates.
- A high power factor (cos φ → 1) means the circuit is behaving mostly resistively.
- Transformers only work with AC; they cannot step up or down DC voltages.

## Questions

```yaml
- question: "An inductor and a capacitor are connected in an AC circuit. Which statement best explains why neither element dissipates average power?"
  type: multiple-choice
  options:
    - "Inductors and capacitors have zero resistance, so no power can flow through them"
    - "They store energy in fields during one half-cycle and return it to the circuit during the next, so net energy transfer averages to zero"
    - "Their reactance exactly cancels the applied voltage, preventing any current from flowing"
    - "AC power is imaginary, so reactive elements don't interact with it"
  answer: 1
  explanation: "Inductors store energy in a magnetic field and capacitors in an electric field. On each half-cycle, energy flows into the element as the field builds; on the next half-cycle, the same energy flows back out as the field collapses. The average over a full cycle is zero net energy transfer. This is why reactive elements appear in the imaginary part of impedance — they cause phase shifts without real power dissipation. Only resistance converts electrical energy irreversibly into heat."

- question: "At the resonant frequency ω₀ = 1/√(LC), what is the total impedance of a series RLC circuit?"
  type: multiple-choice
  options:
    - "Zero — the circuit has no opposition to current at resonance"
    - "Equal to R — the inductive and capacitive reactances cancel each other exactly"
    - "Equal to √(R² + (X_L − X_C)²), which is minimized but not zero"
    - "Infinite — energy stored in L and C blocks current at this frequency"
  answer: 1
  explanation: "At resonance, X_L = X_C, so they cancel: the imaginary part of impedance is zero. The remaining impedance is purely resistive: Z = R. Impedance is at its minimum and current is at its maximum. Note that option A ('zero') would require R = 0, which only applies to an ideal superconducting circuit. In any real circuit R > 0, so impedance at resonance equals R, not zero. Option C is the general formula but at resonance it correctly reduces to R."

- question: "A series RLC circuit with a high quality factor Q has a sharper, narrower resonance peak than the same circuit with a low Q factor."
  type: true-false
  answer: true
  explanation: "Q = ω₀/Δω, where Δω is the bandwidth — the range of frequencies where power exceeds half its resonance maximum. High Q means small Δω: the circuit responds strongly only to frequencies very close to ω₀. Physically, high Q corresponds to low R (low damping): energy dissipates slowly, so near-resonant oscillations persist at nearly full amplitude. This selectivity is why high-Q circuits are used in radio tuners to isolate a single station from its neighbors."

- question: "An ideal transformer can step up DC voltage just as effectively as it steps up AC voltage, since the turns ratio N₂/N₁ applies in either case."
  type: true-false
  answer: false
  explanation: "Transformers operate on mutual inductance: a changing magnetic flux in the primary coil induces a voltage in the secondary. DC current produces a constant (not changing) magnetic field, generating no changing flux and therefore no induced voltage in the secondary. A DC source produces no transformer output. This is one of the historic reasons AC was chosen for the electrical grid: it can be efficiently transformed, while DC cannot (without modern solid-state power electronics)."

- question: "Explain why high-voltage AC transmission reduces energy losses compared to transmitting the same power at low voltage."
  type: short-answer
  answer: "Power loss in a transmission line is P_loss = I²R, where R is the line's fixed resistance. For a given power P = VI, increasing voltage V means decreasing current I proportionally. Since losses scale as I², doubling voltage halves current and cuts losses by 75%; multiplying voltage by 10 reduces losses by 99%. Transformers make this lossless voltage conversion possible for AC."
  explanation: "This is the dominant economic argument for AC power transmission. A step-up transformer near the generator raises voltage (and lowers current) for long-distance transmission; a step-down transformer near the end user restores safe voltage levels. The I²R loss formula directly connects transformer operation to resistive dissipation: you want to minimize I for a given power delivered, which means maximizing V."
```

## Explainer

From your study of impedance and reactance, you know that inductors and capacitors present frequency-dependent opposition to current. A key insight carried into AC power is that this opposition — reactance — stores and releases energy rather than consuming it. An inductor builds up a magnetic field on each half-cycle and returns that energy to the circuit; a capacitor charges and then discharges. On average, neither dissipates power. Only resistance absorbs energy irreversibly, converting it to heat. This is the origin of the **power factor**: in a purely resistive circuit, voltage and current are in phase, and all the apparent power does real work. When reactance shifts current out of phase with voltage, some power sloshes back and forth without being consumed, and the power factor cos φ captures exactly what fraction of the apparent power V_rms I_rms actually does work.

**Resonance** arises when the inductive and capacitive reactances exactly cancel: X_L = X_C, i.e., ωL = 1/(ωC). Solving for the resonant frequency gives ω₀ = 1/√(LC). At this frequency, the total impedance of a series RLC circuit collapses to just R — the circuit behaves as if the inductor and capacitor aren't there. Current amplitude is maximized, and the power delivered to R is at its peak. Think of it like a swing: push at the natural frequency and the amplitude grows; push at the wrong frequency and energy fights the swing's stored motion. The LC pair is the mechanical analog of the swing's mass and spring.

The **quality factor** Q = ω₀L/R = ω₀/Δω tells you how sharply tuned the resonance is. High Q means the resonance peak is narrow: only frequencies very close to ω₀ produce large current. Low R (low damping) gives high Q — the circuit is "choosy" about frequency. This is how radio tuners work: by adjusting C, you shift ω₀ to match a particular station's broadcast frequency, while the narrow Q rejects nearby stations. High Q is desirable when selectivity matters; low Q is preferable when you need to pass a broad band of frequencies.

Transformers bring in the power consequences of resonance from a different angle. They exploit mutual inductance between two coils to transfer power while changing voltage and current levels. The ideal transformer conserves power: if V₂ = (N₂/N₁)V₁ steps voltage up, then I₂ = (N₁/N₂)I₁ steps current down proportionally. The reason high-voltage AC transmission is efficient connects directly to your prerequisite knowledge of resistive power dissipation P = I²R: for a given power delivered, transmitting at high voltage means low current, and losses in the transmission line (which have fixed resistance) scale as I². Stepping voltage up by a factor of 10 cuts line losses by a factor of 100. This is why the AC grid operates at hundreds of kilovolts, stepped down locally by distribution transformers before reaching homes.
