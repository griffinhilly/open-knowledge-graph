---
id: richardson-extrapolation
title: Richardson Extrapolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-differentiation
  type: hard
builds-toward:
- romberg-integration
tags:
- extrapolation
- acceleration
- richardson
stage: formal-systems
status: draft
---

# Richardson Extrapolation

## Core Idea
Richardson extrapolation combines numerical estimates at different step sizes to cancel leading-order error terms. If an estimate has error c₁h + c₂h² + ..., combining results at h and h/2 eliminates the O(h) term. This acceleration technique generalizes to any problem with known asymptotic error expansions and is the foundation for Romberg integration.

## Explainer

From numerical differentiation, you know that approximations like the centered difference (f(x+h) - f(x-h))/(2h) have errors that shrink with h. But taking h smaller has a cost: when h is very small, floating-point cancellation makes the numerator inaccurate. Richardson extrapolation offers a smarter route: compute two estimates at different step sizes and combine them algebraically to cancel the dominant error term — improving accuracy without pushing h toward machine precision.

Here is the key insight. Suppose your method produces an estimate A(h) with asymptotic error expansion A(h) = I + c₁h + c₂h² + ···, where I is the true value and c₁, c₂ are unknown constants. Now compute A(h/2) = I + c₁(h/2) + c₂(h/2)² + ··· = I + (c₁/2)h + (c₂/4)h² + ···. Multiply this equation by 2 and subtract the first: 2A(h/2) - A(h) = I + (terms in h² and higher). The O(h) term **cancels exactly**, producing a new estimate with error starting at O(h²). You have gained a full order of accuracy using only two evaluations already in hand — no new function calls required.

The technique applies repeatedly. If the original method has error c₂h² + c₄h⁴ + ··· (as with centered differences, which only have even powers in the expansion), a single Richardson step produces error O(h⁴). Apply the same combination to two O(h⁴) estimates at different spacings to get O(h⁶), and so on. This bootstrapping produces what is called a **Richardson table**: a triangular array where each column is one application of the cancellation formula applied to the previous column. The diagonal entries converge very rapidly.

This is the foundation of **Romberg integration**. Start with the trapezoidal rule for ∫f(x)dx, which has an error expansion in even powers of h (a result called the Euler-Maclaurin formula). Compute the trapezoidal sum at step sizes h, h/2, h/4, ···, then build the Richardson table column by column. The bottom-right entry of the table is an extremely accurate estimate of the integral — often matching hundreds of trapezoidal evaluations with just a handful. The prerequisite that makes this work is knowing the structure of the error expansion. Problems with clean polynomial error expansions respond dramatically to Richardson; problems with singularities or irregular error behavior respond less predictably.
