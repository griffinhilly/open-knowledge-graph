---
id: system-causality-and-realizability
title: System Causality and Realizability Constraints
domain: engineering
course: signals-and-systems
prerequisites:
- id: orthogonal-signal-decomposition-basis
  type: soft
builds-toward:
- lti-systems-and-impulse-response
- transfer-functions-control
tags:
- systems
- causality
- realizability
- constraints
stage: abstract-reasoning
status: validated
---
# System Causality and Realizability Constraints

## Core Idea
A causal system's output depends only on present and past inputs, not future inputs—a fundamental physical requirement. Realizability requires the impulse response to be zero for t<0. For frequency-domain systems, causality imposes a relationship between magnitude and phase (Kramers-Kronig relations) that constrains the achievable performance.

## How It's Best Learned
Compare a non-causal filter (symmetric FIR with center tap) to a causal version; observe the required delay. Examine how pole-zero locations must satisfy causality constraints.

## Common Misconceptions
- Thinking stable systems are automatically causal.
- Assuming any transfer function can be realized causally.
- Misunderstanding that causality limits achievable magnitude response slopes.

## Questions

```yaml
- question: "A signal processing system produces its output at time t = 5 s using input values sampled at t = 3 s, t = 5 s, and t = 8 s. What can be said about this system?"
  type: multiple-choice
  options:
    - "It is causal — it uses two past values and only one future value, so it is mostly causal"
    - "It is non-causal — using input at t = 8 s to produce output at t = 5 s requires knowledge of a future input"
    - "It is stable — averaging multiple samples prevents unbounded output"
    - "It is realizable — it uses a finite number of input samples, so it can be implemented"
  answer: 1
  explanation: "Causality is a strict requirement: the output at any time t may only depend on inputs at times ≤ t. Using even one future input value (t = 8 > t = 5) makes the system non-causal. There is no such thing as 'mostly causal.' Realizability (option D) is related but distinct — a system can use a finite number of inputs and still be non-causal if any input is in the future. Stability (option C) is a separate property entirely and cannot be inferred from the number of input samples."

- question: "An ideal low-pass filter has a perfectly flat passband magnitude and perfectly linear phase. What does causality theory imply about implementing it in real time?"
  type: multiple-choice
  options:
    - "It is realizable in real time because it has finite passband gain"
    - "It is realizable in real time because linear phase is easier to implement than nonlinear phase"
    - "It cannot be implemented causally in real time — it requires access to future input samples and must introduce delay"
    - "It violates stability constraints, making any implementation impossible"
  answer: 2
  explanation: "An ideal low-pass filter has a symmetric impulse response centered at t = 0, meaning it requires samples from both before and after the current moment — it is non-causal. To run it in real time, you must introduce a delay equal to half the filter length, buffering 'future' samples so they are available when needed. This is exactly why audio and communication processing systems have latency: they are buffering future input to enable non-causal filtering. The filter is not unstable (option D) — it is perfectly stable; it is simply non-causal."

- question: "A stable system is always causal, because any system that responds to inputs indefinitely in time must eventually incorporate future input knowledge."
  type: true-false
  answer: false
  explanation: "Stability and causality are independent properties. An ideal low-pass filter is stable (bounded input produces bounded output) but non-causal (its symmetric impulse response extends into negative time). Conversely, a system with a right-half-plane pole is causal (h(t) = 0 for t < 0) but unstable (its output grows without bound). You can have any combination of the two properties: stable-causal, stable-non-causal, unstable-causal, and unstable-non-causal all exist."

- question: "For a causal system, the magnitude and phase of the frequency response are not independently choosable — specifying the magnitude constrains the achievable phase, and vice versa."
  type: true-false
  answer: true
  explanation: "This follows from the Kramers-Kronig relations: the real and imaginary parts of the frequency response of a causal system are Hilbert transform pairs of each other. In filter design terms, you cannot have both a perfectly flat passband and perfectly linear phase in a causal filter — the two goals are in tension. Minimum-phase filters achieve the sharpest magnitude roll-off but with highly nonlinear phase. Linear-phase FIR filters have excellent phase but require a delay to be made causal. Engineers must choose which degradation to accept."

- question: "Why does audio processing software often add latency, and what does this have to do with causality?"
  type: short-answer
  answer: "Many desirable audio filters (such as linear-phase FIR filters) are non-causal — their impulse response is symmetric around t = 0, meaning they need to 'see' both past and future samples to compute the output. To run a non-causal filter on a live audio stream, the software buffers incoming audio, introducing a delay equal to the 'look-ahead' needed (half the filter length for a symmetric FIR). This delay is the latency. It is the engineering price of using non-causal filter designs that would otherwise require future input knowledge."
  explanation: "This trade-off appears throughout real-time signal processing: more filter sophistication (flatter magnitude, more linear phase, sharper cutoffs) generally requires more look-ahead, which means more buffer and more latency. Low-latency applications like phone calls tolerate less processing; offline applications like music mastering can use arbitrarily non-causal filters because the entire recording is already available."
```

## Explainer

**Causality** is the principle that a system's present output cannot depend on inputs that haven't happened yet. This is not a mathematical convenience — it is a physical necessity for any system that must operate in real time. A recording played back through a filter can be non-causal (you can look ahead in the stored waveform), but a live microphone feeding a speaker cannot: you cannot process a sound before it arrives. Mathematically, this means the system's **impulse response** h(t) must satisfy h(t) = 0 for all t < 0. The output at time t is a weighted sum only of past and present inputs, never future ones.

The relationship between causality and stability is an easy place to stumble. A system can be stable but non-causal (ideal low-pass filter with a symmetric h(t)), or causal but unstable (a pole in the right half-plane). These are independent properties. Realizability is the engineering version of causality: a transfer function H(s) is realizable if it corresponds to a causal, finite-order system — meaning the degree of the numerator polynomial cannot exceed that of the denominator, because a higher-numerator degree implies derivatives of the input, which anticipate future input behavior.

The deeper consequence of causality lives in the frequency domain. For a causal system, the real and imaginary parts of the frequency response H(jω) are not independent — they are related through the **Kramers-Kronig relations**, which are Hilbert transform pairs. In practice this means: you cannot freely choose both the magnitude and phase of a transfer function. If you specify the magnitude response |H(jω)|, the phase response ∠H(jω) is largely determined (and vice versa for minimum-phase systems). This constrains filter design: a perfectly flat passband magnitude with a perfectly linear phase requires a non-causal filter. Real causal filters trade off sharpness of cutoff against phase distortion, and designers choose which degradation to accept.

Non-causal filters can still be useful offline. A symmetric finite-impulse-response (FIR) filter with coefficients centered at index zero has perfect linear phase but requires knowing future samples. To run it causally, you introduce a **delay** equal to half the filter length, shifting the center tap to the present moment. This is why audio software adds latency: it is buffering "future" input so the non-causal filter has access to it. Understanding this delay is essential for designing real-time audio, control, and communications systems where latency budgets are tight.
