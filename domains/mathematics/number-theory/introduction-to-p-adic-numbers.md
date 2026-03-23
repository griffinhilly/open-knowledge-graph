---
id: introduction-to-p-adic-numbers
title: Introduction to p-adic Numbers
domain: mathematics
course: number-theory
prerequisites:
- id: p-adic-valuation
  type: hard
builds-toward:
- arithmetic-in-p-adic-numbers
tags:
- p-adic
- completion
- metric-spaces
stage: advanced
status: validated
---

# Introduction to p-adic Numbers

## Core Idea
The p-adic numbers ℚ_p are the completion of ℚ with respect to the p-adic metric. They provide an alternative geometric intuition where 'closeness' is measured by divisibility: two numbers are close if their difference is highly divisible by p. This enables new perspectives on solving Diophantine equations.

## Questions

```yaml
- question: "In ℚ₅ (the 5-adic numbers), which pair of integers is closest under the 5-adic metric |·|₅?"
  type: multiple-choice
  options:
    - "1 and 2, because they differ by 1 and are adjacent integers"
    - "1 and 6, because they differ by 5"
    - "1 and 126, because they differ by 5³ = 125"
    - "1 and 3126, because they differ by 5⁵ = 3125"
  answer: 3
  explanation: "|1 − 3126|₅ = |3125|₅ = |5⁵|₅ = 5^{−5} = 1/3125, which is the smallest of the four distances. In the 5-adic metric, a larger power of 5 dividing the difference means the numbers are *closer*, the opposite of ordinary intuition. |1−2|₅ = 1 (no factor of 5), |1−6|₅ = 1/5, |1−126|₅ = 1/125, |1−3126|₅ = 1/3125. Numbers we think of as 'far apart' can be extremely close p-adically if their difference is highly divisible by p."

- question: "The p-adic numbers ℚ_p and the real numbers ℝ are both completions of the rationals ℚ. What is the key difference between these two completions?"
  type: multiple-choice
  options:
    - "ℝ adds algebraic numbers to ℚ, while ℚ_p adds p-adic power series"
    - "Both complete ℚ by adding limits of Cauchy sequences, but under different metrics — the ordinary absolute value for ℝ, and the p-adic norm for ℚ_p"
    - "ℝ uses Dedekind cuts while ℚ_p uses equivalence classes of Cauchy sequences — they are fundamentally different constructions"
    - "ℝ is the unique completion of ℚ; ℚ_p is a different kind of object, not a completion in the metric space sense"
  answer: 1
  explanation: "Both ℝ and ℚ_p are constructed by exactly the same process — taking Cauchy sequences of rationals and identifying sequences with the same limit — but using different notions of distance. The ordinary absolute value makes rationals 'close' when their numerical difference is small; the p-adic norm makes rationals close when their difference is divisible by a high power of p. Ostrowski's theorem makes this precise: every non-trivial absolute value on ℚ is either the ordinary one (giving ℝ) or a p-adic one (giving ℚ_p) for some prime p."

- question: "In the 3-adic metric, the number 3^100 is very large — much larger than 1."
  type: true-false
  answer: false
  explanation: "|3^100|₃ = 3^{−100}, which is extremely small — not large. In the p-adic metric, high powers of p are *close to zero*, not far from zero. This is the complete reversal of ordinary intuition: the p-adic norm measures divisibility by p, so numbers highly divisible by p are tiny. 3^100 is as small as you can get in ℚ₃."

- question: "The infinite sum −1 = (p−1) + (p−1)p + (p−1)p² + ··· converges in the p-adic metric because each successive term is smaller under |·|_p than the previous one."
  type: true-false
  answer: true
  explanation: "The k-th term is (p−1)p^k, and |(p−1)p^k|_p = p^{−k} → 0 as k → ∞. In a complete ultrametric space like ℚ_p, a series converges if and only if its terms tend to 0 (a much simpler criterion than in ℝ). The sum really does equal −1: partial sums are 1 + p + p² + ··· + p^n = (p^{n+1} − 1)/(p − 1) · (p − 1) ... actually the sum (p−1)(1 + p + ··· + p^n) = p^{n+1} − 1, and p^{n+1} → 0 p-adically, so the sum converges to −1."

- question: "What does it mean for two integers to be 'close' in the p-adic metric, and how does this differ from ordinary closeness on the number line?"
  type: short-answer
  answer: "Two integers are close in the p-adic metric if their difference is divisible by a high power of p. The p-adic distance is |a − b|_p = p^{−v_p(a−b)}, so high divisibility by p means small distance. This is the opposite of ordinary closeness: on the real number line, 1 and 2 are very close (differ by 1), but in ℚ₅, 1 and 3126 are far closer (differ by 5⁵). Large powers of p are p-adically tiny, not large. The p-adic metric is measuring arithmetic structure (divisibility) rather than magnitude."
  explanation: "This reversal — large powers of p being small, high divisibility meaning closeness — is the core intuition that makes p-adic numbers feel alien at first but becomes natural once you internalize that distance is being defined by arithmetic structure rather than geometric separation."
```

## Explainer

From your study of the p-adic valuation, you know that vₚ(n) counts how many times p divides n, and that this valuation satisfies the ultrametric inequality. The p-adic numbers ℚ_p are what you get when you take this valuation seriously as a notion of *distance*. Define |x|ₚ = p^{−vₚ(x)}. Under this metric, two integers are close if their difference is highly divisible by p. For example, in ℚ₅, the numbers 1 and 126 = 1 + 5³ are only 1/125 apart, because 5³ divides their difference. Numbers we think of as "large" — like 5^{100} — are tiny in the p-adic world; numbers we think of as "close to 1" in the usual sense — like 2/3 — may be perfectly well-behaved p-adically.

The **completion** of ℚ with respect to the p-adic metric works exactly as you would construct the real numbers: take all Cauchy sequences of rationals (sequences where terms eventually get arbitrarily close under | · |ₚ) and identify sequences that converge to the same limit. The resulting space ℚ_p is complete — every Cauchy sequence converges — and contains ℚ as a dense subfield. This mirrors how ℝ is the completion of ℚ under the usual absolute value. The key difference is that while there is only one completion under the standard metric (up to equivalence), Ostrowski's theorem tells us that for every prime p, the p-adic metric gives a genuinely different, inequivalent completion.

One of the most striking features of p-adic numbers is their expansion: every element of ℤ_p (the p-adic integers, the "unit ball" of ℚ_p) can be written uniquely as a₀ + a₁p + a₂p² + ··· where each aᵢ ∈ {0, 1, ..., p−1}. This looks like a power series in p, and it converges p-adically because higher powers of p are smaller in | · |ₚ. This is the reverse of ordinary positional notation, where high powers of 10 are large. In ℚ_p, you can even make sense of "infinite series going left" — for instance, −1 = (p−1) + (p−1)p + (p−1)p² + ··· (the p-adic expansion of −1), a fact that is deeply counterintuitive from a real-number perspective.

The payoff for Diophantine equations comes through the **Hasse-Minkowski theorem** and the general principle of local-global reasoning: to understand integer solutions to a polynomial equation, one studies solutions in ℝ and in ℚ_p for every prime p (these are the "local" fields). A solution over all these completions is a necessary condition for a rational solution. Working p-adically is often much easier — p-adic numbers satisfy a strong form of Hensel's lemma, which lifts solutions mod p to full p-adic solutions under mild conditions — while the global (rational) problem is hard. The p-adics thus serve as tractable local test cases for the global arithmetic question.
