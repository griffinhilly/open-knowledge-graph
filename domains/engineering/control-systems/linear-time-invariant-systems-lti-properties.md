---
id: linear-time-invariant-systems-lti-properties
title: Linear Time-Invariant (LTI) Systems and Properties
domain: engineering
course: control-systems
prerequisites:
- id: laplace-transform-fundamentals
  type: soft
builds-toward:
- transfer-function-derivation-differential-equations
- frequency-response-magnitude-phase-basics
- impulse-response-and-convolution-control
tags:
- fundamentals
- lti
- linearity
- time-invariance
stage: formal-systems
status: validated
---

# Linear Time-Invariant (LTI) Systems and Properties

## Core Idea
LTI systems are fundamental to control theory because their behavior can be fully characterized by impulse response and frequency response. A system is linear if it satisfies superposition and homogeneity; time-invariant if its parameters do not change with time. These properties enable use of Laplace transforms and frequency-domain analysis.

## Questions

```yaml
- question: "A sinusoidal input at 10 Hz with amplitude 2 V is applied to an LTI system. What can you guarantee about the steady-state output?"
  type: multiple-choice
  options:
    - "The output is a sinusoid at some frequency determined by the system's natural frequencies, not necessarily 10 Hz"
    - "The output is a sinusoid at exactly 10 Hz, with amplitude and phase determined by the system's frequency response at 10 Hz"
    - "The output is a sinusoid at 10 Hz, and its amplitude equals 2 V because LTI systems are energy-conserving"
    - "The output could be any waveform — LTI systems only preserve linearity, not frequency content"
  answer: 1
  explanation: "A fundamental property of LTI systems is that a sinusoidal input at frequency ω always produces a sinusoidal output at the same frequency ω. The system cannot create new frequencies. The amplitude and phase of the output are determined by the system's transfer function evaluated at the input frequency: |G(jω)| scales the amplitude and ∠G(jω) shifts the phase. This is the foundation of Bode plot analysis — you sweep input frequency and measure how the system modifies amplitude and phase. Option A describes resonance phenomena but misidentifies how LTI systems process sinusoids. Option C incorrectly assumes energy conservation."

- question: "System A is defined by y(t) = 2x(t) (doubles the input). System B is defined by y(t) = x(t) + 5 (adds a constant offset). Which system is LTI, and why is the other not?"
  type: multiple-choice
  options:
    - "Both are LTI — both produce predictable outputs for any input"
    - "System A is LTI; System B is not, because it violates superposition (the zero input produces nonzero output, so the system has a bias)"
    - "System B is LTI; System A is not, because scaling the input by 2 changes the system's gain"
    - "Neither is LTI — true LTI systems only exist as mathematical idealizations"
  answer: 1
  explanation: "System A satisfies both linearity tests: α·x(t) → α·2x(t) = 2αx(t) = αy(t) (homogeneity), and x₁(t)+x₂(t) → 2x₁(t)+2x₂(t) = y₁(t)+y₂(t) (superposition). System B fails linearity: if x(t)=0 then y(t)=5≠0, which means a zero input produces nonzero output. More formally, adding an offset violates superposition: y(x₁+x₂) = x₁+x₂+5, but y(x₁)+y(x₂) = x₁+5+x₂+5 = x₁+x₂+10 ≠ y(x₁+x₂). System B is actually an affine system — linear plus a constant bias — not a linear system. This distinction matters in practice whenever a system has a non-zero operating point or bias."

- question: "A system described by the differential equation dy/dt + t·y(t) = x(t) (where the coefficient of y is the time variable t) is time-invariant."
  type: true-false
  answer: false
  explanation: "Time-invariance requires that the system's differential equation have constant coefficients — if you apply the same input at a different time, you get the same output, just time-shifted. Here, the coefficient of y(t) is 't' itself, which changes with time. If you apply input x(t−t₀), the governing equation at time t uses coefficient 't', not 't−t₀', so the system responds differently depending on when the input is applied. This is a time-varying system and cannot be analyzed with standard Laplace/transfer function methods. Such systems arise in practice — e.g., a pendulum with a moving pivot, or a process with temperature-dependent rate constants — and require more advanced techniques."

- question: "The impulse response h(t) of an LTI system fully determines the system's output for any arbitrary input x(t) through the convolution integral."
  type: true-false
  answer: true
  explanation: "This is one of the most powerful results in LTI theory. Because of linearity, any input x(t) can be decomposed into a weighted sum of shifted Dirac delta impulses: x(t) = ∫ x(τ)δ(t−τ)dτ. Because of time-invariance, each shifted impulse δ(t−τ) produces the shifted impulse response h(t−τ). Superposition then gives y(t) = ∫ x(τ)h(t−τ)dτ — the convolution integral. The impulse response h(t) encodes the system's complete behavior: natural frequencies, damping, DC gain, everything. Knowing h(t) is equivalent to knowing the transfer function G(s) (they are a Laplace transform pair), and either one completely characterizes the system."

- question: "Why do the linearity and time-invariance properties together make the Laplace transform such a powerful tool for analyzing control systems?"
  type: short-answer
  answer: "Linearity means the system satisfies superposition, so complex inputs can be analyzed as sums of simple components. Time-invariance means the system has constant coefficients in its differential equation. Together, applying the Laplace transform converts the constant-coefficient differential equation into an algebraic equation in s, where differentiation becomes multiplication by s. The ratio of output to input in the s-domain is the transfer function G(s) — a simple algebraic expression. Without LTI, the differential equation would have time-varying coefficients and the Laplace transform would not produce a clean algebraic form. LTI is the necessary precondition for transfer function analysis."
  explanation: "The key insight is that the Laplace transform trades the difficulty of solving differential equations for the simpler task of algebra and partial fractions — but only if the coefficients are constant. LTI guarantees constant coefficients. If either property fails (nonlinearity or time-variance), the system must be analyzed by other means: linearization, numerical simulation, or specialized techniques for specific system classes."
```

## Explainer

The phrase "linear time-invariant" describes two independent properties, each worth understanding on its own before considering them together. **Linearity** has two components: **superposition** and **homogeneity** (scaling). Superposition means that if input x₁(t) produces output y₁(t), and input x₂(t) produces output y₂(t), then input x₁(t) + x₂(t) produces output y₁(t) + y₂(t). Homogeneity means if x(t) produces y(t), then αx(t) produces αy(t) for any scalar α. Together, these mean the system response to a sum of scaled inputs is the same sum of scaled outputs — you can analyze each input component independently, then add the results. This is the principle of superposition, and it is what makes linear systems analytically tractable.

**Time-invariance** means the system's behavior does not depend on when you apply the input. If input x(t) produces output y(t), then input x(t − t₀) produces output y(t − t₀) — the same response, just shifted in time. Practically, this means the differential equation describing the system has constant coefficients: a resistor's resistance doesn't change over time, a spring's stiffness doesn't change, a control gain doesn't drift. Systems with time-varying parameters (e.g., a pendulum whose pivot is moving, or a process with temperature-dependent reaction rates) are not time-invariant and require significantly more complex analysis.

Why do these two properties matter so much? Because together they unlock the **Laplace transform** and **frequency-domain analysis** — your soft prerequisite. For an LTI system, applying the Laplace transform to the differential equation converts it to an algebraic equation in the complex variable s. The ratio of output to input in this domain is the **transfer function** G(s), which completely characterizes the system. Furthermore, for a sinusoidal input at frequency ω, the output of an LTI system is a sinusoid at the *same* frequency, possibly with different amplitude and phase — the system cannot create new frequencies. This is the foundation of Bode plots, Nyquist analysis, and every frequency-domain design method.

The **impulse response** h(t) is the system output when the input is a Dirac delta function δ(t) — an infinitely brief, unit-area pulse. Because of linearity and time-invariance, any input can be decomposed into a weighted sum of shifted impulses, and the output is the corresponding weighted sum of shifted impulse responses. This operation is **convolution**: y(t) = x(t) * h(t) = ∫ x(τ)h(t−τ)dτ. Knowing h(t) completely determines how the system responds to any input — it is the system's fingerprint. In the Laplace domain, convolution becomes multiplication: Y(s) = X(s)·G(s), which is why transfer functions are so much easier to work with than time-domain convolution. The LTI assumption is what makes this simplification valid, and it is the bedrock assumption underlying virtually every classical control analysis and design technique.
