---
id: generating-functions-discrete
title: 'Generating Functions: Introduction and Applications'
domain: mathematics
course: discrete-math
prerequisites:
- id: combinations-and-selections
  type: soft
builds-toward:
- recurrence-relations-definition
tags:
- generating-functions
- sequences
stage: formal-systems
status: draft
---

# Generating Functions: Introduction and Applications

## Core Idea
A generating function encodes a sequence a₀, a₁, a₂, … as coefficients of a power series f(x) = a₀ + a₁x + a₂x² + ⋯. Generating functions transform combinatorial counting problems into algebraic manipulations of power series. They provide a systematic method for deriving formulas for complex sequences.

## Explainer

Think of a generating function as a filing system: every slot xⁿ holds the answer aₙ to the question "how many ways are there to do something with n items?" The variable x is just a placeholder — you never actually substitute a number for it (usually). Instead, you manipulate the entire power series algebraically and read off coefficients. The magic is that algebraic operations on generating functions correspond to meaningful combinatorial operations on sequences.

Here is the fundamental example. From your work with combinations, you know that the number of ways to choose k items from n is C(n,k). The **ordinary generating function** for the sequence C(n,0), C(n,1), …, C(n,n) is simply (1+x)ⁿ — that is, the binomial theorem states that (1+x)ⁿ = Σ C(n,k) xᵏ. Now suppose you want to count the number of ways to choose r items total from two independent groups of sizes m and n. You can multiply the generating functions: (1+x)ᵐ · (1+x)ⁿ = (1+x)^{m+n}. The coefficient of xʳ on the left-hand side is Σ C(m,k)·C(n,r-k) (choosing k from the first group and r-k from the second). The coefficient of xʳ on the right-hand side is C(m+n,r). Equality of the coefficients gives you Vandermonde's identity — algebra for free.

The real power of generating functions emerges with **recurrence relations**. Suppose aₙ = aₙ₋₁ + aₙ₋₂ (the Fibonacci recurrence). Define f(x) = Σ aₙ xⁿ. You can translate the recurrence into an algebraic equation for f(x), solve for f(x) as a closed-form expression (a rational function), and then use partial fractions to read off an explicit formula for aₙ. This converts a recursive problem — which requires computing every prior term — into a direct formula. Generating functions essentially let you do algebra on infinite sequences as if they were polynomials.

There are several flavors of generating functions for different situations. **Ordinary generating functions** (OGFs) handle straightforward counting sequences. **Exponential generating functions** (EGFs), which use aₙ/n! as the coefficient of xⁿ, are better suited to permutation problems because division by n! cancels the overcounting from ordering. The choice of which flavor to use depends on whether your combinatorial objects are labeled (use EGF) or unlabeled (use OGF). This choice is a skill developed through practice, but the underlying idea is always the same: encode the sequence, do algebra, decode the answer.
