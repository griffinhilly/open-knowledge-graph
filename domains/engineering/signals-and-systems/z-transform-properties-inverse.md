---
id: z-transform-properties-inverse
title: Z-Transform Properties and Inverse Techniques
domain: engineering
course: signals-and-systems
prerequisites:
- id: z-transform-discrete-time-signals
  type: hard
builds-toward:
- iir-filter-design-realization
- fir-filter-design-realization
tags:
- z-transform
- properties
- inverse-transform
stage: advanced
status: draft
---

# Z-Transform Properties and Inverse Techniques

## Core Idea
Z-transform properties (linearity, time shift, convolution, scaling) simplify analysis of discrete-time systems. Inverse Z-transform techniques include partial fractions, long division, and residue calculation to recover time-domain sequences from X(z).

## Explainer

The Z-transform converts a discrete-time sequence x[n] into a rational function X(z) in the complex variable z. The power of this representation comes from its properties, which let you manipulate sequences algebraically in the Z-domain rather than working sample-by-sample in the time domain. You already know how to compute the Z-transform from the definition; now you'll learn to exploit its structure.

The most important properties are **linearity** and the **time-shift property**. Linearity means that if you scale or add sequences, their Z-transforms scale and add identically — this lets you decompose complicated signals into simpler pieces. The time-shift property states that delaying a sequence by k samples multiplies X(z) by z^{-k}. This is the Z-domain analog of the Laplace differentiation property, and it is why difference equations — which relate outputs to delayed inputs — transform into simple polynomial equations in z. The **convolution property** completes the toolkit: convolution of two sequences in time corresponds to multiplication of their Z-transforms. This turns the operation of filtering (a convolution) into a multiplication, which is far easier to analyze.

To go in the other direction — recovering x[n] from X(z) — you need the **inverse Z-transform**. The most practical technique is **partial fraction expansion**. You factor the denominator of X(z)/z into first-order terms, expand into partial fractions, and look up each term in a Z-transform table. For example, a term of the form A/(1 - a·z^{-1}) corresponds to the sequence A·a^n·u[n] when the region of convergence (ROC) is outside the pole at z = a. Getting the ROC right is critical: the same rational function X(z) can correspond to multiple different sequences depending on whether you select causal, anti-causal, or two-sided sequences — the ROC determines which interpretation is correct.

**Long division** provides an alternative when you need the first few terms of x[n] explicitly. Divide the numerator polynomial by the denominator polynomial (using decreasing powers of z for causal sequences, or increasing powers for anti-causal ones), and the coefficients of the quotient are x[0], x[1], x[2], and so on. This is less elegant than partial fractions but useful for checking answers or when the sequence has no closed form. The **residue method** generalizes partial fractions to higher-order poles by computing contour integral residues — it is the formal basis for all inverse Z-transform calculations, though you rarely need it explicitly for simple pole cases.

Together, these tools let you work entirely in the Z-domain: model a filter as a ratio of polynomials H(z), find its response to an input X(z) by computing Y(z) = H(z)·X(z), then invert to get y[n]. This pipeline — transform, multiply, invert — is the Z-transform workflow that underlies all IIR and FIR filter design and analysis you will encounter next.
