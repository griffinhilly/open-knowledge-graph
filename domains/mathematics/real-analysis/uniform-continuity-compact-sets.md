---
id: uniform-continuity-compact-sets
title: Uniform Continuity on Compact Sets
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-continuity
  type: hard
- id: compact-sets
  type: hard
- id: heine-borel-theorem
  type: soft
tags:
- uniform-continuity
- compact
- compactness
stage: advanced
status: validated
---

# Uniform Continuity on Compact Sets

## Core Idea
Every continuous function on a compact set is uniformly continuous. This is a theorem with profound implications: on [a,b], all continuous functions are uniformly continuous, justifying the integral's existence. The proof uses compactness via contradiction: a failure of uniform continuity produces a non-convergent sequence with no convergent subsequence, violating Bolzano-Weierstrass.

## Questions

```yaml
- question: "Why is f(x) = 1/x not uniformly continuous on (0, 1), even though it is continuous at every point in (0, 1)?"
  type: multiple-choice
  options:
    - "Because 1/x is unbounded on (0, 1), making it impossible to control globally"
    - "Because (0, 1) is not compact — sequences approaching 0 have no convergent subsequence inside the domain, allowing f to vary without bound near the missing endpoint"
    - "Because f is discontinuous at x = 0, which contaminates behavior on (0, 1)"
    - "Because f has an unbounded derivative everywhere, and any function with an unbounded derivative fails uniform continuity"
  answer: 1
  explanation: "The key is that (0, 1) is not compact — the endpoint 0 is missing. Sequences approaching 0 leave the domain, so there is no point in (0, 1) where continuity can constrain the function's behavior there. This is precisely what Bolzano-Weierstrass needs: a convergent subsequence whose limit is still in the domain. Without compactness, that fails and the contradiction argument collapses. Option A is a symptom, not the root cause — the theorem's proof hinges on compactness, not boundedness per se."

- question: "A student claims: 'f(x) = sin(1/x) is uniformly continuous on [0.1, 1] because it is periodic.' What is the correct analysis?"
  type: multiple-choice
  options:
    - "The student is right — periodic functions are always uniformly continuous on closed intervals"
    - "The student reaches the right conclusion for the wrong reason: sin(1/x) is uniformly continuous on [0.1, 1] because [0.1, 1] is compact, and every continuous function on a compact set is uniformly continuous"
    - "The student is wrong: sin(1/x) is not uniformly continuous on [0.1, 1] because it oscillates rapidly"
    - "The student is wrong: uniform continuity requires monotonicity, which sin(1/x) lacks"
  answer: 1
  explanation: "sin(1/x) is continuous on [0.1, 1] (no singularity in this range), and [0.1, 1] is closed and bounded, hence compact by Heine-Borel. Therefore by the theorem, it is uniformly continuous. The student's justification (periodicity) is irrelevant and wrong — periodicity alone guarantees nothing about uniform continuity. The correct reason is the Heine-Cantor theorem: compact domain + continuity = uniform continuity."

- question: "The function f(x) = x² is uniformly continuous on [0, 100] but not uniformly continuous on [0, ∞)."
  type: true-false
  answer: true
  explanation: "[0, 100] is closed and bounded, hence compact by Heine-Borel. Since x² is continuous, the theorem guarantees uniform continuity there. On [0, ∞), which is not compact, x² fails uniform continuity: as x grows large, |f(x + δ) − f(x)| = |2xδ + δ²| ≈ 2xδ can exceed ε for any fixed δ by choosing x large enough. Compactness is what makes the difference."

- question: "Uniform continuity on a compact set is 'obvious' from continuity — no special proof is needed, because compact sets are inherently well-behaved."
  type: true-false
  answer: false
  explanation: "This is a common intuitive shortcut that obscures real mathematical content. The proof requires a genuine argument using Bolzano-Weierstrass. Without it, you cannot rule out the possibility that the required δ shrinks to zero across the domain. Compactness is needed precisely to guarantee that every sequence has a convergent subsequence whose limit is in the domain — so that continuity at the limit gives a contradiction. Compactness is doing essential logical work, not just making things 'nicer.'"

- question: "Explain in your own words why compactness is essential to this theorem — what goes wrong when the domain is not compact?"
  type: short-answer
  answer: "Without compactness, sequences in the domain can 'escape' toward a missing boundary point or toward infinity. The contradiction proof produces sequences (xₙ), (yₙ) with |xₙ − yₙ| → 0 but |f(xₙ) − f(yₙ)| ≥ ε. Bolzano-Weierstrass (which requires compactness) gives a convergent subsequence xₙₖ → p with p still in the domain. Continuity at p then forces both f(xₙₖ) and f(yₙₖ) to converge to f(p), producing the contradiction. Without compactness, the limit p might not be in the domain, and continuity at p cannot be invoked."
  explanation: "The failure of uniform continuity on (0, 1) for f(x) = 1/x illustrates this exactly: take xₙ = 1/n and yₙ = 1/(n+1). Then |xₙ − yₙ| → 0 but |f(xₙ) − f(yₙ)| = |n − (n+1)| = 1. The sequence xₙ → 0, but 0 is not in the domain — so we cannot use continuity at 0 to close the argument. Compactness plugs precisely this gap."
```

## Explainer

You've already wrestled with the difference between pointwise and **uniform continuity**. Recall the distinction: pointwise continuity says that for each point x and each ε > 0, you can find a δ that works *at x*; but δ can depend on x, so it might shrink to zero as x moves. Uniform continuity demands one δ that works simultaneously *everywhere* on the domain. The function f(x) = 1/x on (0, 1) is continuous at every point but not uniformly continuous — as x approaches 0, you need ever-tinier δ to keep the function within ε.

The key theorem connects uniform continuity to compactness: **if f is continuous on a compact set K, then f is uniformly continuous on K**. On a closed bounded interval [a, b] — compact by Heine-Borel — every continuous function automatically gets the stronger uniform continuity property for free. The intuition is that compactness prevents the "runaway" behavior that destroys uniform continuity. On (0, 1), the trouble is that the endpoint 0 is missing; sequences approaching 0 have no limit *inside* the domain. On [0, 1], that endpoint is included, so every sequence has its limit inside the set, and the function's behavior at the limit controls the behavior nearby.

The formal proof works by contradiction. Suppose f is continuous on compact K but not uniformly continuous. Then there exists ε > 0 such that for every δ > 0, there exist points xₙ, yₙ with |xₙ − yₙ| < 1/n yet |f(xₙ) − f(yₙ)| ≥ ε. This gives a sequence (xₙ) in K. Because K is compact (equivalently, because K is closed and bounded by Heine-Borel), **Bolzano-Weierstrass** guarantees a convergent subsequence x_{nₖ} → p ∈ K. The corresponding y_{nₖ} also converges to p (since |xₙ − yₙ| → 0). But then continuity of f at p forces f(x_{nₖ}) → f(p) and f(y_{nₖ}) → f(p), making |f(x_{nₖ}) − f(y_{nₖ})| → 0 — contradicting that it stays ≥ ε. Compactness is what gives you the convergent subsequence; without it, the argument collapses.

The theorem's payoff reaches across analysis. The Riemann integral's definition requires that continuous functions on [a, b] can be uniformly approximated by step functions — which is exactly what uniform continuity guarantees. Without this theorem, the integral's existence for continuous functions would require a much more painful argument. Whenever you see a theorem that works on closed bounded intervals but fails on open ones, compactness is usually the invisible reason.
