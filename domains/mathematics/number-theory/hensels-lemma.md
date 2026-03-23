---
id: hensels-lemma
title: Hensel's Lemma
domain: mathematics
course: number-theory
prerequisites:
- id: introduction-p-adic-numbers
  type: hard
- id: quadratic-congruences
  type: soft
tags:
- hensels-lemma
- lifting-solutions
- p-adic-numbers
stage: advanced
status: validated
---

# Hensel's Lemma

## Core Idea
If f(x) ≡ 0 (mod p) has a solution a with f'(a) ≢ 0 (mod p), then a lifts uniquely to a solution in ℤ_p. This enables solving congruences modulo p^k iteratively and extends to polynomial equations over p-adic numbers.

## Questions

```yaml
- question: "Suppose f(x) = x² − 2 and you find that f(3) ≡ 0 (mod 7), with f'(3) = 6 ≢ 0 (mod 7). What does Hensel's Lemma guarantee?"
  type: multiple-choice
  options:
    - "There exists at least one solution to f(x) ≡ 0 (mod 49), but it may not be unique"
    - "There exists exactly one solution to f(x) ≡ 0 (mod 7^k) for every k ≥ 1, congruent to 3 mod 7"
    - "The solution lifts to mod 49 but further lifting requires checking again whether the derivative remains nonzero"
    - "There is no guarantee of a lift unless 2 divides p − 1"
  answer: 1
  explanation: "When f'(a) ≢ 0 (mod p), Hensel's Lemma guarantees a *unique* lift at every stage: from mod p to mod p², from mod p² to mod p³, and so on indefinitely. The nonzero derivative condition does not need to be re-verified at each stage — once it holds mod p, the lifting works all the way up, yielding a unique element of ℤ_p. Option A is too weak (uniqueness is guaranteed), and option C misunderstands the iterative structure."

- question: "Suppose f(a) ≡ 0 (mod p) and f'(a) ≡ 0 (mod p). What does Hensel's Lemma say about lifting a to a solution mod p²?"
  type: multiple-choice
  options:
    - "The lift is guaranteed to exist but may not be unique"
    - "The lift is guaranteed to be unique but may not exist"
    - "Hensel's Lemma gives no guarantee: there may be no lift, or multiple lifts"
    - "The lift always exists because the original solution is valid mod p"
  answer: 2
  explanation: "The nonzero derivative condition is precisely what makes Hensel's Lemma work. When f'(a) ≡ 0 (mod p), the argument breaks down: the linear equation for the lift t has no solution (if f(a)/p ≢ 0 mod p there is no lift), or infinitely many solutions (if f(a)/p ≡ 0 mod p, any t works, giving p distinct lifts). This parallels Newton's method failing at a repeated real root. The lesson: the derivative condition is not a technicality but the essential mechanism of uniqueness."

- question: "Hensel's Lemma applies to a polynomial f over ℤ, and we find a solution a mod p. Under the conditions of the lemma, this solution lifts to a unique solution in ℤ_p — the p-adic integers."
  type: true-false
  answer: true
  explanation: "This is exactly the content of Hensel's Lemma. When f(a) ≡ 0 (mod p) and f'(a) ≢ 0 (mod p), the iterative lifting process gives a unique sequence a, a₁, a₂, ... where aₖ ≡ a (mod p) and f(aₖ) ≡ 0 (mod p^{k+1}). This sequence is coherent (aₖ ≡ a_{k-1} mod p^k) and thus defines a unique element of ℤ_p — the inverse limit of the system ℤ/p^k ℤ."

- question: "If f'(a) ≡ 0 (mod p) at a solution a, then Hensel's Lemma still guarantees a lift exists, just without uniqueness."
  type: true-false
  answer: false
  explanation: "When f'(a) ≡ 0 (mod p), Hensel's Lemma gives no guarantee at all — not existence, not uniqueness. The Taylor expansion mod p² gives f(a + tp) ≡ f(a) + tp·f'(a) ≡ f(a) (mod p²), so whether a lift exists depends entirely on whether f(a) ≡ 0 (mod p²). If f(a) ≢ 0 (mod p²), there is no lift; if f(a) ≡ 0 (mod p²), then any choice of t works (p lifts exist). The vanishing derivative is not just a uniqueness problem — it signals a complete failure of the Newton's-method mechanism."

- question: "Why is the condition f'(a) ≢ 0 (mod p) the key to Hensel's Lemma, and what role does it play in the lifting argument?"
  type: short-answer
  answer: "The nonzero derivative condition guarantees that the linear equation for the correction term t has a unique solution mod p. In the lifting step, writing b = a + tp and expanding f(b) ≡ f(a) + tp·f'(a) (mod p²), setting this to zero requires t ≡ −[f(a)/p]·[f'(a)]⁻¹ (mod p). For this to have a unique solution, two things must hold: f(a) must be divisible by p (the hypothesis), and f'(a) must be invertible mod p (the derivative condition). The derivative condition ensures the inverse exists, yielding a unique t and hence a unique lift."
  explanation: "This mirrors Newton's method for real roots: the tangent line at a near-root gives a unique improved estimate, provided the derivative is nonzero (so the tangent line isn't horizontal). A zero derivative would mean the tangent line is flat — it never crosses zero, or is identically zero, giving no information about where the root is. Hensel's Lemma is this same geometric intuition transported to the p-adic world."
```

## Explainer

Hensel's Lemma is the p-adic analog of Newton's method. Recall how Newton's method finds real roots: start near a root, use the tangent line (the derivative) to get a better approximation, repeat. Hensel's Lemma is the same idea, but working modulo increasing powers of p rather than over the real line. The key principle is **lifting**: a solution mod p can be refined to a solution mod p², then mod p³, and so on — as long as the derivative is nonzero at the solution.

Concretely, suppose f(a) ≡ 0 (mod p) and f'(a) ≢ 0 (mod p). Can we find b ≡ a (mod p) with f(b) ≡ 0 (mod p²)? Write b = a + tp for some integer t. Taylor-expanding modulo p²: f(a + tp) ≡ f(a) + tp · f'(a) (mod p²). Setting this to zero gives t ≡ −f(a)/p · (f'(a))⁻¹ (mod p). Since f(a) ≡ 0 (mod p), the quantity f(a)/p is an integer; and since f'(a) ≢ 0 (mod p), its inverse exists modulo p. So t is uniquely determined mod p, and b = a + tp is the unique lift of a to a solution mod p². The same argument applies repeatedly, lifting from mod p^k to mod p^{k+1} at each stage.

The condition f'(a) ≢ 0 (mod p) is what makes uniqueness possible. When the derivative vanishes at the solution, lifting may fail entirely (no solution mod p²) or branch into multiple lifts — exactly as Newton's method fails near a repeated real root. When the condition holds, the lift is unique at every stage, meaning the single root in ℤ/pℤ extends to a unique element of ℤ_p — a p-adic integer. Hensel's Lemma is thus a constructive bridge from your knowledge of p-adic numbers to concrete computations: a root that "looks good" mod p (with nonvanishing derivative) extends all the way into the p-adic integers with no ambiguity.

A classic application connects directly to quadratic congruences: does x² ≡ a (mod p^k) have a solution for all k ≥ 1? By Hensel, it suffices to check that x² ≡ a (mod p) has a solution x₀ and that the derivative 2x₀ is nonzero mod p — i.e., x₀ ≢ 0 (mod p). When p is odd and a is a quadratic residue mod p, both conditions hold, so the solution lifts to all p-adic levels. Hensel's Lemma therefore turns the question "does this congruence have solutions at arbitrarily high powers of p?" into a single computation mod p.
