---
id: systems-classification-properties
title: System Classification and Properties
domain: engineering
course: signals-and-systems
prerequisites:
- id: signal-classification-continuous-discrete
  type: hard
builds-toward:
- lti-systems-and-impulse-response
- transfer-function-poles-zeros
tags:
- systems
- classification
- properties
stage: advanced
status: draft
---

# System Classification and Properties

## Core Idea
Systems are classified by properties such as linearity (superposition), time-invariance, causality, and stability. LTI (Linear Time-Invariant) systems are particularly important because their behavior is completely determined by the impulse response, enabling convolution-based analysis.

## Explainer

You already know how to classify signals as continuous or discrete, periodic or aperiodic, and energy or power signals. System classification is the parallel exercise for the boxes those signals pass through. The properties you assign to a system — linearity, time-invariance, causality, stability — determine which mathematical tools you can use to analyze it. Get these classifications right and the rest of the course opens up; get them wrong and every subsequent analysis rests on false assumptions.

**Linearity** means the system satisfies two sub-conditions simultaneously: **scaling** (if you scale the input by a constant, the output scales by the same constant) and **additivity** (if you feed in the sum of two signals, the output is the sum of the individual outputs). Together, these are called the **superposition principle**: y(a·x₁ + b·x₂) = a·y(x₁) + b·y(x₂). A resistor is linear — double the voltage, double the current. A diode is nonlinear — the relationship between voltage and current is exponential. To test linearity formally, assume two inputs and their outputs, form a linear combination of the inputs, and check whether the system produces the same linear combination of the outputs.

**Time-invariance** means the system's behavior doesn't change with time: if you delay the input by T, the output is simply delayed by T — the shape is identical. A fixed resistor is time-invariant; an amplifier whose gain drifts over temperature is not. **Causality** means the output at any time depends only on past and present inputs, never on future ones. Every real-time physical system is causal; many signal processing operations (like non-causal filters applied to pre-recorded data) are not. **BIBO stability** (Bounded-Input Bounded-Output) means every bounded input produces a bounded output — the system doesn't blow up. An unstable system produces a growing output even from a finite input, which corresponds to poles in the right half of the s-plane or outside the unit circle in the z-domain.

The reason **LTI (Linear Time-Invariant)** systems get special treatment is that satisfying both linearity and time-invariance makes the impulse response h(t) a complete description of the system. Once you know how the system responds to an impulse, you can compute the output to any input by convolution: y(t) = x(t) * h(t). This is why the course devotes so much attention to LTI systems — they admit analytical solutions that nonlinear or time-varying systems generally do not. The upcoming topics on transfer functions, poles and zeros, and frequency response all follow directly from this foundation. When you classify a system as LTI, you are essentially unlocking a full toolkit; when you find it violates linearity or time-invariance, you know those tools no longer apply and you need a different approach.
