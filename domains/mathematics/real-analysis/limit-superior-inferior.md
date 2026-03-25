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
- id: interchange-limit-derivative
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
status: validated
---
# Limit Superior and Inferior

## Core Idea
For a bounded sequence (aₙ), the limit superior (limsup aₙ) is the limit of the decreasing sequence of suprema {sup{aₖ : k ≥ n}}, and the limit inferior (liminf aₙ) is the limit of the increasing sequence of infima {inf{aₖ : k ≥ n}}. A sequence converges if and only if limsup aₙ = liminf aₙ.

## Questions

```yaml
- question: "For the sequence aₙ = (−1)ⁿ + 1/n, what are the limsup and liminf?"
  type: multiple-choice
  options:
    - "limsup = 1, liminf = −1"
    - "limsup = 1, liminf = −1, and therefore the sequence converges"
    - "limsup and liminf do not exist because the sequence does not converge"
    - "limsup = 2, liminf = 0"
  answer: 0
  explanation: "The sequence oscillates between values near +1 (odd terms: −1 + 1/n → −1) wait — even terms give +1 + 1/n → 1, odd terms give −1 + 1/n → −1. So the sequence approaches 1 and −1 infinitely often. limsup = 1 (the largest accumulation point) and liminf = −1 (the smallest). Since limsup ≠ liminf, the sequence diverges. Option C reflects the common misconception that limsup/liminf require convergence — they are defined precisely for sequences that do *not* converge. Option B wrongly concludes convergence from the values."

- question: "A bounded sequence has limsup aₙ = liminf aₙ = 5. What can you conclude?"
  type: multiple-choice
  options:
    - "The sequence is eventually constant, equal to 5"
    - "The sequence converges to 5"
    - "The sequence has 5 as its supremum but may not converge"
    - "The sequence converges to 5 only if it is monotone"
  answer: 1
  explanation: "The fundamental theorem connecting limsup, liminf, and convergence states: a bounded sequence converges if and only if its limsup equals its liminf, in which case both equal the ordinary limit. If limsup = liminf = 5, the sequence converges to 5 — by definition, the tail suprema and infima both squeeze to 5, trapping all eventual terms arbitrarily close to 5. The sequence need not be eventually constant (e.g., aₙ = 5 + sin(n)/n satisfies this). Monotonicity is irrelevant; the squeeze is the whole argument."

- question: "For any bounded sequence, limsup aₙ ≥ liminf aₙ."
  type: true-false
  answer: true
  explanation: "This follows directly from the definitions. For every n, sup{aₖ : k ≥ n} ≥ inf{aₖ : k ≥ n} (the supremum of a set is always ≥ its infimum). Taking limits preserves this inequality: the decreasing sequence Sₙ converges to limsup, the increasing sequence Iₙ converges to liminf, and Sₙ ≥ Iₙ for every n implies limsup ≥ liminf. Equality is the special case of convergence; strict inequality signals oscillation."

- question: "If a bounded sequence does not converge, its limsup and liminf do not exist."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Limsup and liminf are *always* defined for any bounded sequence — that is their entire purpose. The sequences Sₙ = sup{aₖ : k ≥ n} and Iₙ = inf{aₖ : k ≥ n} are monotone (decreasing and increasing respectively) and bounded, so the Monotone Convergence Theorem guarantees their limits exist. The ordinary limit fails for an oscillating sequence precisely because limsup ≠ liminf; but both individual values exist. Limsup and liminf are tools for sequences that fail to converge."

- question: "The root test for series uses limsup |aₙ|^(1/n) rather than lim |aₙ|^(1/n). Why is the limsup version more useful?"
  type: short-answer
  answer: "The ordinary limit lim |aₙ|^(1/n) may not exist for all sequences, but limsup always exists for bounded sequences. If the root test used lim, it would be inapplicable whenever the sequence oscillates or has irregular behavior. Using limsup makes the test universally applicable: whenever limsup |aₙ|^(1/n) < 1, the series converges absolutely, regardless of whether the ordinary limit exists. The limsup captures the 'worst-case eventual growth rate' of the terms, which is exactly what determines convergence."
  explanation: "This is the practical payoff of limsup and liminf: they are precision tools for exactly the irregular, non-convergent sequences where blunter tools like ordinary limits fail. The root test is most needed precisely when |aₙ|^(1/n) oscillates — and limsup is defined even then."
```

## Explainer

Limit superior and inferior give you a way to describe the "eventual behavior" of a sequence even when it does not converge. Recall from epsilon-N convergence that a sequence converges to L if its tail can be kept arbitrarily close to L. But what about a sequence that oscillates forever, like aₙ = (−1)ⁿ? The standard limit does not exist, yet there is clearly something systematic: the sequence bounces between −1 and 1 indefinitely. Limsup and liminf capture precisely this behavior — the extremes that the sequence approaches infinitely often.

The construction uses the tools you already have. Define Sₙ = sup{aₖ : k ≥ n} — the supremum of all terms from position n onward. As n increases, you are taking suprema over smaller sets (dropping early terms), so Sₙ is a **decreasing** sequence. Since it is bounded below (assuming the original sequence is bounded), the Monotone Convergence Theorem guarantees it converges. That limit is the **limsup** of aₙ — the largest value the sequence reaches infinitely often. Similarly, define Iₙ = inf{aₖ : k ≥ n}; this is increasing and bounded above, and its limit is the **liminf**. For aₙ = (−1)ⁿ: limsup = 1 and liminf = −1, reflecting the two accumulation points.

The convergence criterion ties everything together: a bounded sequence converges if and only if limsup aₙ = liminf aₙ, and in that case both equal the ordinary limit. Any gap between them signals persistent oscillation. You can think of limsup as the "ceiling the sequence keeps touching" and liminf as the "floor the sequence keeps touching" — convergence means these squeeze to the same level.

The practical power of limsup and liminf appears in convergence tests for series. The **root test** uses limsup |aₙ|^(1/n): if this value is less than 1, the series ∑aₙ converges absolutely; if greater than 1, it diverges. Using limsup instead of an ordinary limit makes the test valid even when the ordinary limit does not exist — which is exactly the situation where you need a more robust tool. Limsup and liminf are the precision instruments for cases where blunter tools like ordinary limits break down.
