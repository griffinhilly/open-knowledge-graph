---
id: resonance-and-peaking-response
title: Resonance, Peaking, and Bandwidth Relationships
domain: engineering
course: control-systems
prerequisites:
- id: bandwidth-and-cutoff-frequencies
  type: hard
- id: natural-frequency-damping-second-order
  type: soft
- id: bandwidth-resonance-frequency-selection
  type: soft
builds-toward:
- lead-lag-compensation-design
tags:
- resonance
- peaking
- bandwidth
- frequency-response
stage: advanced
status: validated
---
# Resonance, Peaking, and Bandwidth Relationships

## Core Idea
Resonance occurs when system natural frequency aligns with input frequency, causing amplitude amplification above DC gain. Peak resonance magnitude (Mr, resonance peak) and resonant frequency (ωr) depend on damping: lower damping yields higher peaks and sharpened resonance. The relationship between Mr, bandwidth, and damping provides design insight: reducing damping increases bandwidth but increases peaking and overshoot—a fundamental design trade-off.

## Questions

```yaml
- question: "A control engineer reduces the damping ratio of a second-order system from ζ = 0.7 to ζ = 0.4 in order to increase bandwidth. What else unavoidably happens?"
  type: multiple-choice
  options:
    - "Only the cutoff frequency changes; step response overshoot is unaffected by damping ratio"
    - "The resonance peak M_r increases and step response percent overshoot increases — all three are manifestations of the same pole locations"
    - "The natural frequency ω_n automatically decreases to compensate, keeping overshoot constant"
    - "Bandwidth and overshoot change in opposite directions, so overall response quality remains constant"
  answer: 1
  explanation: "Bandwidth, peaking (M_r), and step-response overshoot are not independent — they are all governed by the same damping ratio ζ and the same closed-loop pole locations. Moving poles closer to the imaginary axis (reducing ζ) simultaneously widens bandwidth, raises M_r, and increases percent overshoot. There is no free lunch: you cannot widen bandwidth without also accepting more peaking and overshoot. This interconnection is the central design trade-off in second-order system synthesis."

- question: "At ζ = 0.707 (the 'Butterworth' or 'critically flat' condition), what is special about the system's behavior?"
  type: multiple-choice
  options:
    - "The system is at the boundary of stability — any further reduction in ζ causes instability"
    - "The resonance peak M_r reaches its maximum value, providing the most amplification"
    - "There is no resonance peaking in the frequency response, step overshoot is minimized (~4%), and the response is maximally flat before rolloff"
    - "The bandwidth is exactly equal to the natural frequency ω_n, providing the simplest design relationship"
  answer: 2
  explanation: "At ζ = 0.707, M_r ≈ 1 (no magnitude peak above the DC gain), and step overshoot is approximately 4% — often a good starting point for design. This is called the 'maximally flat' or Butterworth condition. It is not the stability boundary (that is ζ = 0); stability requires ζ > 0. Option B is exactly backwards: M_r is maximized as ζ → 0, not at ζ = 0.707."

- question: "A control system designer can independently choose to increase bandwidth (for faster tracking) while also decreasing percent overshoot (for less peaking), by selecting different values of the natural frequency ω_n and damping ratio ζ."
  type: true-false
  answer: false
  explanation: "Bandwidth and overshoot are both tied to the same parameter ζ, so they cannot be tuned independently by changing ζ alone. Reducing ζ raises both bandwidth and overshoot simultaneously. The partial workaround is to increase ω_n while holding ζ fixed — this speeds up the response without changing the overshoot percentage — but even this strategy eventually hits limits from actuator saturation, noise amplification, and higher-order dynamics. The fundamental trade-off between speed and damping cannot be eliminated."

- question: "An undamped second-order system (ζ = 0) driven continuously at its natural frequency will grow to an unbounded amplitude over time."
  type: true-false
  answer: true
  explanation: "From the resonance peak formula M_r = 1/(2ζ√(1−ζ²)), as ζ → 0, M_r → ∞. With zero damping, every cycle of forcing adds energy that cannot escape, so oscillation amplitude grows without bound. In physical systems this manifests as structural failure — the classic example being a bridge or aircraft component driven at its resonant frequency. In control systems, a plant with a lightly damped resonant mode can cause the loop to saturate or oscillate destructively if the controller excites that frequency."

- question: "A spec requires fast settling time AND small overshoot. Using the resonance-damping-bandwidth relationship, explain the fundamental design tension this creates and how you would reason about resolving it."
  type: short-answer
  answer: "Fast settling requires wide bandwidth, which requires low ζ. Small overshoot requires high ζ. Since both bandwidth and overshoot decrease together as ζ increases, the two specs pull in opposite directions on the same parameter. The standard resolution is to first select ζ to satisfy the overshoot constraint (e.g., ζ ≈ 0.6 for ~10% overshoot), then increase ω_n to meet the speed requirement — because raising ω_n scales up the response speed without changing the overshoot percentage. This separates the two specs onto different parameters: ζ controls overshoot shape, ω_n controls absolute speed."
  explanation: "This is the core two-parameter design procedure for second-order systems: (1) set ζ from the overshoot (or M_r) specification, (2) set ω_n from the settling time or bandwidth specification. The trade-off is real but manageable because the two parameters control largely orthogonal aspects of response quality. Recognizing that simultaneous tight specs on both speed and overshoot may require accepting some compromise — or adding a compensator — is the practical skill this topic develops."
```

## Explainer

You know from bandwidth and cutoff frequency analysis that a system's frequency response has a characteristic shape — flat at low frequencies, then rolling off. You also know from second-order system theory that the **natural frequency ω_n** and **damping ratio ζ** together define how a system responds. Resonance is the phenomenon that connects these: when the driving frequency is close to ω_n, the system amplifies the input rather than attenuating it — the output is *larger* than the input, not smaller.

The physical mechanism is energy exchange. An underdamped second-order system stores energy in two forms (think of a spring-mass system: kinetic and potential, or an LC circuit: magnetic and electric). Near the natural frequency, energy sloshes back and forth between the two storage elements in synchrony with the driving signal. If damping is low, little energy escapes each cycle, and the oscillation grows large. At exactly the resonant frequency ω_r = ω_n √(1 − 2ζ²), the magnitude of the frequency response reaches its peak **M_r** = 1 / (2ζ√(1 − ζ²)). Notice that as ζ → 0, M_r → ∞ — an undamped system driven at resonance grows without bound.

The damping ratio governs a direct trade-off between three related quantities: **peaking**, **bandwidth**, and **time-domain overshoot**. Reducing ζ (less damping) increases M_r (more peaking in frequency domain), increases bandwidth (the −3 dB frequency rises), and increases percent overshoot in the step response. These are not independent consequences you can pick among — they are manifestations of the same underlying system pole locations moving closer to the imaginary axis. A system with ζ = 0.707 ("critically flat" or Butterworth response) has M_r ≈ 1 (no peaking) and about 4% step overshoot — often a good starting point for design. A system with ζ = 0.5 has M_r ≈ 1.15 and about 16% overshoot.

For control design, this trade-off is a central constraint. You can make a system respond faster (wider bandwidth, lower ζ), but you pay with peaking and overshoot — the system overshoots its target and may oscillate before settling. You can make a system well-damped (high ζ, low overshoot), but it becomes sluggish and slow to reject disturbances. Real specifications typically constrain both: a step response must settle within X% of final value in time T, *and* peak no more than Y% above — translating directly into constraints on ζ and ω_n. Understanding the resonance-damping-bandwidth relationship is what lets you read those specs and immediately reason about whether they are achievable and at what cost.
