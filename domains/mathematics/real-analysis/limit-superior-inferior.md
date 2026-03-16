---
id: limit-superior-inferior
title: Limit Superior and Inferior
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: supremum-infimum
  type: hard
- id: monotone-convergence-theorem
  type: soft
builds-toward:
- uniform-convergence
- root-test
- ratio-test
tags:
- limsup
- liminf
- limits
- convergence
stage: advanced
status: draft
---

# Limit Superior and Inferior

## Core Idea
For a bounded sequence (aₙ), the limit superior (limsup aₙ) is the limit of the decreasing sequence of suprema {sup{aₖ : k ≥ n}}, and the limit inferior (liminf aₙ) is the limit of the increasing sequence of infima {inf{aₖ : k ≥ n}}. A sequence converges if and only if limsup aₙ = liminf aₙ.

## Explainer

Limit superior and inferior give you a way to describe the "eventual behavior" of a sequence even when it does not converge. Recall from epsilon-N convergence that a sequence converges to L if its tail can be kept arbitrarily close to L. But what about a sequence that oscillates forever, like aₙ = (−1)ⁿ? The standard limit does not exist, yet there is clearly something systematic: the sequence bounces between −1 and 1 indefinitely. Limsup and liminf capture precisely this behavior — the extremes that the sequence approaches infinitely often.

The construction uses the tools you already have. Define Sₙ = sup{aₖ : k ≥ n} — the supremum of all terms from position n onward. As n increases, you are taking suprema over smaller sets (dropping early terms), so Sₙ is a **decreasing** sequence. Since it is bounded below (assuming the original sequence is bounded), the Monotone Convergence Theorem guarantees it converges. That limit is the **limsup** of aₙ — the largest value the sequence reaches infinitely often. Similarly, define Iₙ = inf{aₖ : k ≥ n}; this is increasing and bounded above, and its limit is the **liminf**. For aₙ = (−1)ⁿ: limsup = 1 and liminf = −1, reflecting the two accumulation points.

The convergence criterion ties everything together: a bounded sequence converges if and only if limsup aₙ = liminf aₙ, and in that case both equal the ordinary limit. Any gap between them signals persistent oscillation. You can think of limsup as the "ceiling the sequence keeps touching" and liminf as the "floor the sequence keeps touching" — convergence means these squeeze to the same level.

The practical power of limsup and liminf appears in convergence tests for series. The **root test** uses limsup |aₙ|^(1/n): if this value is less than 1, the series ∑aₙ converges absolutely; if greater than 1, it diverges. Using limsup instead of an ordinary limit makes the test valid even when the ordinary limit does not exist — which is exactly the situation where you need a more robust tool. Limsup and liminf are the precision instruments for cases where blunter tools like ordinary limits break down.
