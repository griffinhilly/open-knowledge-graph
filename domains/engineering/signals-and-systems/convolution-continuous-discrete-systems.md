---
id: convolution-continuous-discrete-systems
title: Convolution in Continuous and Discrete Time
domain: engineering
course: signals-and-systems
prerequisites:
- id: lti-systems-and-impulse-response
  type: hard
- id: integral-calculus
  type: soft
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
status: draft
---

# Convolution in Continuous and Discrete Time

## Core Idea
Convolution y(t) = ∫ x(τ)h(t−τ)dτ (continuous) or y[n] = Σ x[k]h[n−k] (discrete) computes the output of an LTI system by sliding and multiplying the impulse response with the input. Convolution is commutative, associative, and distributive over addition.

## Explainer

You know from your prerequisite on LTI systems that any linear time-invariant system is completely characterized by its **impulse response** h(t) — the output when the input is a unit impulse δ(t). Convolution answers the natural follow-up question: if you know h(t), how do you compute the output for *any* arbitrary input x(t)? The answer rests on two properties you already rely on: linearity (superposition holds) and time-invariance (a delayed input produces a proportionally delayed output).

The key insight is that any input signal can be decomposed into a continuum of scaled, shifted impulses. Think of x(t) as a stack of infinitesimally thin slices, each a scaled impulse at a different time: x(t) ≈ Σ x(τ)·δ(t−τ)·dτ. By linearity, the output is the sum of the system's responses to each of these elementary inputs. By time-invariance, the response to a shifted impulse δ(t−τ) is the shifted impulse response h(t−τ). Therefore the total output is the sum (integral) of scaled, shifted impulse responses: y(t) = ∫ x(τ)·h(t−τ)dτ. This is the **convolution integral** — not an arbitrary formula, but a direct consequence of LTI properties.

The **sliding interpretation** makes this concrete. Fix a time t. The kernel h(t−τ) is the impulse response flipped and shifted by t. As τ runs from −∞ to +∞, you are multiplying x(τ) against this flipped, shifted copy of h and integrating the product. Slide t forward, and the kernel slides along x: the value of the output at time t is determined by how much of the past input (weighted by h in reverse) has accumulated up to that moment. A long impulse response h with slow decay means the output at time t is influenced by inputs from far in the past — a system with long memory. A short impulsive h means the output depends almost entirely on the present input — a system with short memory.

The **discrete-time** version y[n] = Σ x[k]·h[n−k] is structurally identical: flip h, shift by n, multiply pointwise by x, and sum. The main practical difference is that the sum has finitely many terms when both x and h have finite length — an **FIR (finite impulse response)** filter has an h that is zero after some finite number of samples, making discrete convolution directly computable. In continuous time the integral may require numerical evaluation, but in discrete time convolution is just multiply-and-accumulate, which is the core operation of every digital filter and the foundation of digital signal processing hardware. The commutativity property (x * h = h * x) means you can always swap which one you call the "signal" and which the "filter" — a symmetry that is genuinely useful in theoretical derivations even when it lacks physical meaning.
