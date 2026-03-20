---
id: direct-form-transversal-filter-realization
title: Direct Form and Transversal Filter Realizations
domain: engineering
course: signals-and-systems
prerequisites:
- id: cascade-filter-realization-structures
  type: hard
builds-toward:
- fir-filter-design-realization
- iir-filter-design-realization
tags:
- filters
- realization
- direct-form
- transversal
stage: advanced
status: draft
---

# Direct Form and Transversal Filter Realizations

## Core Idea
Direct form realizations implement a transfer function by computing the numerator (zeros) and denominator (poles) separately, creating feedback and feedforward paths. Transversal form (tapped-delay-line) is the FIR equivalent: a shift register with tap coefficients and adders. Both forms require many multipliers but allow direct coefficient implementation. Numerical stability and coefficient sensitivity vary significantly between direct forms (I vs II).

## How It's Best Learned
Draw the direct form I and II signal flow graphs for a 2nd-order IIR filter. Compare the number of delay elements and the order in which computations occur.

## Common Misconceptions
- Thinking all direct forms have identical numerical properties.
- Confusing direct form I and II error propagation.
- Not recognizing why transversal is used despite requiring more multipliers.

## Explainer

From your prerequisite on cascade filter realization structures, you know that a given transfer function H(z) can be implemented in multiple mathematically equivalent ways — same input-output relationship, but different internal signal routing, number of delay elements, and numerical behavior. **Direct form** realizations implement H(z) directly from its difference equation, without factoring it into second-order sections. Understanding them requires seeing how the transfer function's numerator and denominator relate to physical signal flow.

A general IIR transfer function H(z) = B(z)/A(z) has both numerator coefficients bₖ (zeros) and denominator coefficients aₖ (poles). **Direct Form I** implements these separately in sequence: first an all-zero filter (FIR section, computing the numerator polynomial on the input), then an all-pole filter (recursive section, computing the denominator on the intermediate output). The signal flow graph has two banks of delays — one for the input history, one for the output history — requiring 2N delay elements for an Nth-order filter. **Direct Form II** rearranges the computation by noting that the two delay banks can be merged: since both sections are linear, the order can be swapped. The shared delay line stores the "state" of both sections simultaneously, cutting the number of delays to N (the minimum possible). Direct Form II is said to use the **canonical** number of delays.

Despite being mathematically identical, Direct Form I and II differ critically in finite-precision arithmetic. In fixed-point hardware, multiplications introduce rounding errors, and these errors propagate differently through the two structures. In Direct Form II, the internal state variable (the summing node before the delay line) can take very large values even when the input and output are small — a phenomenon called **overflow** in the adder. Direct Form I doesn't have this problem because the two sections process separately. Engineers developing audio DSP on low-word-length processors often prefer Direct Form I or transpose structures precisely to control overflow and coefficient sensitivity.

The **transversal filter** (also called tapped-delay-line) is the natural realization for FIR filters, where A(z) = 1 (no poles, no feedback). The structure is a shift register: the input sample advances through a series of unit delays, and at each tap, it is multiplied by a coefficient bₖ and accumulated. The output is a weighted sum of present and past inputs: y[n] = Σ bₖ · x[n−k]. This is computationally straightforward, unconditionally stable (no feedback), and has linear phase if the coefficients are symmetric — a property cascade IIR structures cannot offer. The cost is that achieving sharp frequency selectivity requires many taps (many multiplications per output sample), which is why FIR filters are more computationally expensive than IIR filters of comparable performance, but are preferred whenever linear phase or guaranteed stability is non-negotiable.
