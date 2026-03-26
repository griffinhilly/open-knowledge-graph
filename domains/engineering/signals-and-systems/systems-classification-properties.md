---
id: systems-classification-properties
title: System Classification and Properties
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
- id: system-causality-and-realizability
  type: soft
builds-toward:
- lti-systems-and-impulse-response
- transfer-function-poles-zeros
tags:
- systems
- classification
- properties
stage: expert
status: validated
---
# System Classification and Properties

## Core Idea
Systems are classified by properties such as linearity (superposition), time-invariance, causality, and stability. LTI (Linear Time-Invariant) systems are particularly important because their behavior is completely determined by the impulse response, enabling convolution-based analysis.

## Questions

```yaml
- question: "A system is defined by y(t) = x(t) · sin(2πt). Is this system time-invariant?"
  type: multiple-choice
  options:
    - "Yes — the output depends only on the current input, not on future values"
    - "No — shifting the input by T gives x(t−T)·sin(2πt), which is not equal to the shifted output y(t−T) = x(t−T)·sin(2π(t−T))"
    - "Yes — multiplication by a fixed sinusoid is a linear operation, and linear systems are always time-invariant"
    - "No — all systems involving multiplication fail time-invariance automatically"
  answer: 1
  explanation: "Time-invariance test: if x(t) → y(t), does x(t−T) → y(t−T)? Feeding x(t−T) into the system produces x(t−T)·sin(2πt), but the expected output would be y(t−T) = x(t−T)·sin(2π(t−T)). These are not equal in general (sin(2πt) ≠ sin(2π(t−T)) for arbitrary T). The multiplier sin(2πt) creates an explicit time-dependence — the system 'knows what time it is.' Option C is a common misconception: linearity and time-invariance are completely independent properties. A system can be linear and time-varying, or nonlinear and time-invariant."

- question: "Why does classifying a system as LTI (Linear Time-Invariant) matter so much for subsequent analysis?"
  type: multiple-choice
  options:
    - "LTI systems are the only ones guaranteed to produce bounded outputs for bounded inputs"
    - "Once you know the impulse response h(t) of an LTI system, you can compute the output for any input via convolution — h(t) completely characterizes the system"
    - "LTI systems are physically easier to construct than nonlinear or time-varying systems"
    - "LTI classification means the system is causal and therefore safe to implement in real time"
  answer: 1
  explanation: "The power of LTI is analytical: linearity means outputs superpose, and time-invariance means the response to a delayed impulse δ(t−τ) is simply a delayed impulse response h(t−τ). Since any input can be decomposed into weighted, shifted impulses, the output is their weighted, shifted sum — which is precisely the convolution y(t) = ∫x(τ)h(t−τ)dτ. Break either property and convolution fails. Option A conflates LTI with BIBO stability (stability is a separate property). Option D conflates time-invariance with causality (also independent)."

- question: "A causal system — one whose output at any time depends primarily on present and past inputs — is expected to be BIBO stable."
  type: true-false
  answer: false
  explanation: "False. Causality and BIBO stability are independent properties. A system can be causal and unstable: for example, y(t) = e^t · u(t) * x(t) has an impulse response that grows without bound, producing unbounded output for a bounded input. Conversely, a non-causal system (depending on future inputs) can be perfectly stable. Causality constrains the direction of time dependence; stability constrains whether the output magnitude is bounded. The two conditions involve completely different aspects of the system's behavior."

- question: "To verify that a system satisfies the superposition principle, it is sufficient to confirm that doubling the input usually doubles the output."
  type: true-false
  answer: false
  explanation: "False. Superposition requires both homogeneity (scaling: α·x → α·y) and additivity (x₁ + x₂ → y₁ + y₂). Checking only scaling is insufficient because a system can satisfy homogeneity without being additive. For example, y(t) = x(t)·|x(t)| satisfies homogeneity for real scalars but violates additivity. You must test both conditions independently — or test the combined form y(a·x₁ + b·x₂) = a·y(x₁) + b·y(x₂) directly — to confirm linearity."

- question: "Explain why finding that a system is NOT time-invariant means you cannot use convolution with the impulse response to predict its output."
  type: short-answer
  answer: "The derivation of convolution relies on time-invariance in a critical step. Any input x(t) can be written as a sum (or integral) of weighted, time-shifted impulses. By linearity, the output is the same weighted sum of the system's responses to those impulses. Time-invariance guarantees that the response to δ(t−τ) is simply h(t−τ) — a time-shifted copy of h(t). Without time-invariance, the response to δ(t−τ) could be some entirely different function g(t, τ) that changes depending on when τ occurs. The convolution formula y(t) = ∫x(τ)h(t−τ)dτ breaks down: you would need a two-argument kernel h(t, τ) rather than a single impulse response h(t−τ), dramatically complicating analysis."
  explanation: "This is why the LTI class is so foundational. The moment time-invariance fails, the entire toolkit of convolution, transfer functions, and frequency response no longer applies directly. Time-varying systems — like a communications channel whose properties change with time, or a control system with changing parameters — require more complex analytical frameworks (time-varying state-space models, Volterra series, etc.). LTI is the condition under which the simplest, most powerful analysis tools are valid."
```

## Explainer

You already know how to classify signals as continuous or discrete, periodic or aperiodic, and energy or power signals. System classification is the parallel exercise for the boxes those signals pass through. The properties you assign to a system — linearity, time-invariance, causality, stability — determine which mathematical tools you can use to analyze it. Get these classifications right and the rest of the course opens up; get them wrong and every subsequent analysis rests on false assumptions.

**Linearity** means the system satisfies two sub-conditions simultaneously: **scaling** (if you scale the input by a constant, the output scales by the same constant) and **additivity** (if you feed in the sum of two signals, the output is the sum of the individual outputs). Together, these are called the **superposition principle**: y(a·x₁ + b·x₂) = a·y(x₁) + b·y(x₂). A resistor is linear — double the voltage, double the current. A diode is nonlinear — the relationship between voltage and current is exponential. To test linearity formally, assume two inputs and their outputs, form a linear combination of the inputs, and check whether the system produces the same linear combination of the outputs.

**Time-invariance** means the system's behavior doesn't change with time: if you delay the input by T, the output is simply delayed by T — the shape is identical. A fixed resistor is time-invariant; an amplifier whose gain drifts over temperature is not. **Causality** means the output at any time depends only on past and present inputs, never on future ones. Every real-time physical system is causal; many signal processing operations (like non-causal filters applied to pre-recorded data) are not. **BIBO stability** (Bounded-Input Bounded-Output) means every bounded input produces a bounded output — the system doesn't blow up. An unstable system produces a growing output even from a finite input, which corresponds to poles in the right half of the s-plane or outside the unit circle in the z-domain.

The reason **LTI (Linear Time-Invariant)** systems get special treatment is that satisfying both linearity and time-invariance makes the impulse response h(t) a complete description of the system. Once you know how the system responds to an impulse, you can compute the output to any input by convolution: y(t) = x(t) * h(t). This is why the course devotes so much attention to LTI systems — they admit analytical solutions that nonlinear or time-varying systems generally do not. The upcoming topics on transfer functions, poles and zeros, and frequency response all follow directly from this foundation. When you classify a system as LTI, you are essentially unlocking a full toolkit; when you find it violates linearity or time-invariance, you know those tools no longer apply and you need a different approach.
