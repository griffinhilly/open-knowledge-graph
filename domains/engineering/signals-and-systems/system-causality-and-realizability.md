---
id: system-causality-and-realizability
title: System Causality and Realizability Constraints
domain: engineering
course: signals-and-systems
prerequisites: []
builds-toward:
- lti-systems-and-impulse-response
- transfer-functions-control
tags:
- systems
- causality
- realizability
- constraints
stage: abstract-reasoning
status: draft
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

## Explainer

**Causality** is the principle that a system's present output cannot depend on inputs that haven't happened yet. This is not a mathematical convenience — it is a physical necessity for any system that must operate in real time. A recording played back through a filter can be non-causal (you can look ahead in the stored waveform), but a live microphone feeding a speaker cannot: you cannot process a sound before it arrives. Mathematically, this means the system's **impulse response** h(t) must satisfy h(t) = 0 for all t < 0. The output at time t is a weighted sum only of past and present inputs, never future ones.

The relationship between causality and stability is an easy place to stumble. A system can be stable but non-causal (ideal low-pass filter with a symmetric h(t)), or causal but unstable (a pole in the right half-plane). These are independent properties. Realizability is the engineering version of causality: a transfer function H(s) is realizable if it corresponds to a causal, finite-order system — meaning the degree of the numerator polynomial cannot exceed that of the denominator, because a higher-numerator degree implies derivatives of the input, which anticipate future input behavior.

The deeper consequence of causality lives in the frequency domain. For a causal system, the real and imaginary parts of the frequency response H(jω) are not independent — they are related through the **Kramers-Kronig relations**, which are Hilbert transform pairs. In practice this means: you cannot freely choose both the magnitude and phase of a transfer function. If you specify the magnitude response |H(jω)|, the phase response ∠H(jω) is largely determined (and vice versa for minimum-phase systems). This constrains filter design: a perfectly flat passband magnitude with a perfectly linear phase requires a non-causal filter. Real causal filters trade off sharpness of cutoff against phase distortion, and designers choose which degradation to accept.

Non-causal filters can still be useful offline. A symmetric finite-impulse-response (FIR) filter with coefficients centered at index zero has perfect linear phase but requires knowing future samples. To run it causally, you introduce a **delay** equal to half the filter length, shifting the center tap to the present moment. This is why audio software adds latency: it is buffering "future" input so the non-causal filter has access to it. Understanding this delay is essential for designing real-time audio, control, and communications systems where latency budgets are tight.
