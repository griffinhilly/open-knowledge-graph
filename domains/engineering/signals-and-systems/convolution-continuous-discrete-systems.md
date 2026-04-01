---
id: convolution-continuous-discrete-systems
title: Convolution in Continuous and Discrete Time
domain: engineering
course: signals-and-systems
prerequisites:
- id: lti-systems-and-impulse-response
  type: hard
- id: convolution-theorem-and-applications
  type: hard
builds-toward:
- convolution-theorem-and-applications
- fourier-transform-definition-properties
tags:
- convolution
- systems
- lti
stage: advanced
status: validated
---

# Convolution in Continuous and Discrete Time

## Core Idea
Convolution y(t) = ∫ x(τ)h(t−τ)dτ (continuous) or y[n] = Σ x[k]h[n−k] (discrete) computes the output of an LTI system by sliding and multiplying the impulse response with the input. Convolution is commutative, associative, and distributive over addition.

## Questions

```yaml
- question: "An LTI system has an impulse response h(t) that decays slowly over several seconds. What does this imply about how the system computes its output at any given time t?"
  type: multiple-choice
  options:
    - "The output at time t depends only on the input at that exact moment, since the impulse response value at t=0 dominates"
    - "The output at time t is a weighted sum of all past inputs, with each past input weighted by the corresponding value of h — meaning the system has long memory"
    - "The output cannot be computed by convolution because the integral would not converge for a slowly decaying h"
    - "A slowly decaying impulse response means the system is not LTI and convolution does not apply"
  answer: 1
  explanation: "The convolution y(t) = ∫ x(τ)·h(t−τ)dτ sums contributions from all past inputs, each weighted by h evaluated at the corresponding lag. A slowly decaying h(t) means contributions from inputs far in the past still have significant weight — the system retains a long memory of its input history. A very brief h (near-impulse) means only the present input matters much. The impulse response encodes the system's memory structure: its duration directly determines how far into the past the output depends on. Option A is the misconception that the system is memoryless."

- question: "The convolution integral requires forming h(t−τ) — a flipped, shifted version of h — before multiplying by x. Why is this flip necessary rather than just multiplying h(τ) directly by x(τ)?"
  type: multiple-choice
  options:
    - "It is a mathematical convention with no physical meaning"
    - "Direct multiplication h(τ)·x(τ) would compute the wrong operation — it would be pointwise multiplication, not accounting for the superposition of time-shifted responses"
    - "The flip arises from time-invariance: the response to a delayed impulse δ(t−τ) is h(t−τ), which reverses h's time axis when viewed as a function of τ"
    - "The flip ensures the output y(t) remains causal by preventing contributions from future inputs"
  answer: 2
  explanation: "The flip is a direct consequence of time-invariance. When decomposing x(t) into scaled, shifted impulses, the system's response to the component at time τ is h(t−τ) — the impulse response shifted to start at τ. Written as a function of τ (with output time t fixed), h(t−τ) reverses h's time axis. This is not a convention but a physical statement: h(t−τ) represents how much influence the input at past time τ exerts on the present output at time t. Direct multiplication h(τ)·x(τ) and integration would compute something entirely different — a cross-correlation of the two signals."

- question: "Convolution is commutative: (x * h)(t) = (h * x)(t) for any two LTI-compatible signals. This means you can swap which signal you call the 'input' and which you call the 'impulse response' without changing the output."
  type: true-false
  answer: true
  explanation: "Commutativity is a provable algebraic property of convolution and holds for LTI systems. This means filtering signal x with filter h produces the same output as filtering h with filter x — a genuine mathematical symmetry even when it lacks an obvious physical interpretation. Commutativity is useful in theoretical derivations (e.g., showing that two LTI systems in series can be reordered without changing the composite output), and it confirms that 'input' and 'filter' are not mathematically privileged roles."

- question: "For a time-varying system (one whose response to an impulse depends on when the impulse is applied), you can still characterize the system using a single impulse response h(t) and compute the output via convolution."
  type: true-false
  answer: false
  explanation: "The convolution formula y(t) = ∫ x(τ)·h(t−τ)dτ relies on time-invariance: it assumes that the response to a delayed impulse δ(t−τ) is simply h(t−τ) — the same shape, shifted. For a time-varying system, the response to an impulse at time τ depends on τ itself, requiring a two-dimensional kernel h(t, τ) rather than a single h(t−τ). Convolution with a single h is valid only for LTI systems. This is why the LTI assumption is fundamental: it is precisely what makes the single impulse response a complete characterization of the system."

- question: "Why is convolution the correct operation for computing the output of an LTI system, rather than simply multiplying the input signal by the impulse response? What two properties of LTI systems make convolution necessary?"
  type: short-answer
  answer: "Linearity allows the input to be decomposed into scaled impulses and the output computed as the superposition of scaled impulse responses. Time-invariance ensures that the response to each delayed impulse component is simply the impulse response delayed by the same amount. Together, these properties mean the output is the integral of scaled, time-shifted copies of h — which is exactly the convolution integral."
  explanation: "Without linearity, superposition fails and you cannot add scaled responses. Without time-invariance, the response to a delayed impulse would not simply be a delayed h(t), and a different impulse response would be needed for each input time. Convolution is not an arbitrary computational choice; it is the unique operation that correctly combines linearity and time-invariance. This is why 'characterized by an LTI system' and 'output computable by convolution with a single h' are equivalent descriptions."
```

## Explainer

You know from your prerequisite on LTI systems that any linear time-invariant system is completely characterized by its **impulse response** h(t) — the output when the input is a unit impulse δ(t). Convolution answers the natural follow-up question: if you know h(t), how do you compute the output for *any* arbitrary input x(t)? The answer rests on two properties you already rely on: linearity (superposition holds) and time-invariance (a delayed input produces a proportionally delayed output).

The key insight is that any input signal can be decomposed into a continuum of scaled, shifted impulses. Think of x(t) as a stack of infinitesimally thin slices, each a scaled impulse at a different time: x(t) ≈ Σ x(τ)·δ(t−τ)·dτ. By linearity, the output is the sum of the system's responses to each of these elementary inputs. By time-invariance, the response to a shifted impulse δ(t−τ) is the shifted impulse response h(t−τ). Therefore the total output is the sum (integral) of scaled, shifted impulse responses: y(t) = ∫ x(τ)·h(t−τ)dτ. This is the **convolution integral** — not an arbitrary formula, but a direct consequence of LTI properties.

The **sliding interpretation** makes this concrete. Fix a time t. The kernel h(t−τ) is the impulse response flipped and shifted by t. As τ runs from −∞ to +∞, you are multiplying x(τ) against this flipped, shifted copy of h and integrating the product. Slide t forward, and the kernel slides along x: the value of the output at time t is determined by how much of the past input (weighted by h in reverse) has accumulated up to that moment. A long impulse response h with slow decay means the output at time t is influenced by inputs from far in the past — a system with long memory. A short impulsive h means the output depends almost entirely on the present input — a system with short memory.

The **discrete-time** version y[n] = Σ x[k]·h[n−k] is structurally identical: flip h, shift by n, multiply pointwise by x, and sum. The main practical difference is that the sum has finitely many terms when both x and h have finite length — an **FIR (finite impulse response)** filter has an h that is zero after some finite number of samples, making discrete convolution directly computable. In continuous time the integral may require numerical evaluation, but in discrete time convolution is just multiply-and-accumulate, which is the core operation of every digital filter and the foundation of digital signal processing hardware. The commutativity property (x * h = h * x) means you can always swap which one you call the "signal" and which the "filter" — a symmetry that is genuinely useful in theoretical derivations even when it lacks physical meaning.
