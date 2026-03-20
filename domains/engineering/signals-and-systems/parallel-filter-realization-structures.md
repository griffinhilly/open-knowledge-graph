---
id: parallel-filter-realization-structures
title: Parallel Filter Realization Structures
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-functions-control
  type: hard
builds-toward:
- iir-filter-design-realization
- cascade-filter-realization-structures
tags:
- filters
- realization
- parallel
- structure
stage: advanced
status: draft
---

# Parallel Filter Realization Structures

## Core Idea
Parallel realization decomposes a transfer function into partial fractions, creating multiple sections whose outputs are summed. Each section can be a 1st or 2nd-order IIR filter. Parallel form minimizes coefficient sensitivity, allows independent section design, and distributes computation across paths. The common input and summed output require careful scaling to avoid overflow.

## How It's Best Learned
Perform partial fraction decomposition on a 4th-order rational function and realize each fraction as a 1st or 2nd-order section. Verify that outputs sum to the original transfer function.

## Common Misconceptions
- Thinking parallel sections are independent (they share input).
- Assuming parallel form eliminates quantization effects.
- Not accounting for output scaling when summing multiple sections.

## Explainer

From transfer functions, you know that an LTI system's input-output relationship in the z-domain (or s-domain) is H(z) = Y(z)/X(z) = N(z)/D(z) — a ratio of polynomials whose roots are the system's zeros (roots of N) and poles (roots of D). Implementing this as an actual computation requires choosing a **realization structure** — a specific network of delays, multipliers, and adders. The same transfer function can be realized in many structurally different ways. Cascade form strings second-order sections in series. Direct form implements the difference equation directly. **Parallel realization** uses a different decomposition entirely: partial fractions.

**Partial fraction decomposition** writes H(z) as a sum of simpler terms: H(z) = A₁/(1 − p₁z⁻¹) + A₂/(1 − p₂z⁻¹) + ... + constant terms, where p₁, p₂, ... are the system poles. You may have seen partial fractions in calculus as a technique for integrating rational functions — here it serves an architectural purpose. Each fractional term is an independent first-order (or second-order, for complex-conjugate pole pairs combined to keep real-valued coefficients) filter. The parallel structure feeds the same input signal to all sections simultaneously and sums their outputs: Y = H₁(X) + H₂(X) + ... + H_k(X). Because addition distributes over the individual transfer functions, the combined output equals H(z)X, which is exactly what is required.

The key advantage over direct-form realization is **reduced sensitivity to coefficient quantization**. In a high-order direct-form filter, the denominator polynomial is D(z) = 1 + a₁z⁻¹ + a₂z⁻² + ... + aₙz⁻ⁿ. All N poles are determined collectively by these N coefficients. When coefficients are stored in finite-precision arithmetic (fixed-point DSP), small rounding errors perturb all the roots simultaneously — poles near the unit circle can shift outside it, making the filter unstable. In parallel form, each section has its own local coefficients governing only its own poles. A quantization error in section 3 shifts section 3's poles but leaves sections 1, 2, and 4 untouched. This locality makes parallel realization especially attractive for high-order filters in fixed-point environments such as embedded DSP chips and hardware implementations.

The critical implementation challenge is **scaling**. All sections receive the same input, but their frequency-domain gains may differ dramatically — section 1 might produce large output at low frequencies while section 2 is active mainly at high frequencies. If the peak gain of any section exceeds the available numeric range, overflow occurs; if a section has a very small peak gain, its output is quantized to nearly zero (underflow rounding noise dominates). The standard remedy is to normalize each section so its maximum output magnitude equals the full-scale value, then compensate at the summing node. Getting scaling right is what separates a textbook partial fraction decomposition from a working fixed-point implementation. The trade-off relative to cascade structures: cascade can be scaled section-by-section in sequence (each section's output feeds the next); parallel sections all operate at full input level simultaneously, making the scaling analysis slightly more complex but the pole sensitivity strictly localized.
