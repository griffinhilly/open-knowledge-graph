---
id: extreme-value-theorem-rigorous
title: Extreme Value Theorem (Proof via Compactness)
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: compact-sets
  type: hard
- id: compact-sets-heine-borel
  type: hard
- id: completeness-axiom
  type: soft
- id: heine-borel-theorem
  type: hard
builds-toward:
- uniform-continuity-compact-sets
tags:
- extreme-value
- compactness
- maxima-minima
stage: advanced
status: validated
---

# Extreme Value Theorem (Proof via Compactness)

## Core Idea
The Extreme Value Theorem states that a continuous function on a compact set attains its maximum and minimum values. The proof proceeds in two steps: first, the continuous image of a compact set is compact (since compactness is preserved under continuous maps); second, compact subsets of ℝ are closed and bounded by the Heine-Borel theorem, so they contain their supremum and infimum. This theorem is fundamental because it guarantees that optimization problems on closed bounded intervals have solutions. Without compactness, continuous functions may approach a supremum without attaining it, as shown by f(x) = 1/x on (0, 1].

## How It's Best Learned
First prove the supporting lemma that continuous images of compact sets are compact, then assemble the full proof. Studying counterexamples—continuous functions on open or unbounded domains that fail to attain extrema—solidifies understanding of why each hypothesis is necessary.

## Common Misconceptions
Students sometimes think continuity alone guarantees extrema, forgetting that the domain must be compact. The theorem also does not say where the extrema occur—they might be at interior points or boundary points.

## Explainer

From your study of ε-δ continuity and compact sets, you have the two ingredients needed for one of the most important existence theorems in analysis. The **Extreme Value Theorem** (EVT) states: if f is continuous on a compact set K, then f attains its maximum and minimum values — there exist points x_max, x_min ∈ K such that f(x_min) ≤ f(x) ≤ f(x_max) for all x ∈ K. This is the theorem that guarantees optimization problems on closed bounded intervals have solutions, and its proof is a showcase for the power of compactness.

The proof has two clean steps. First, the continuous image of a compact set is compact. If K is compact and f is continuous, then f(K) is compact — this follows from the open-cover characterization of compactness (every open cover of f(K) pulls back to an open cover of K, which has a finite subcover, which maps forward to a finite subcover of f(K)). Second, compact subsets of ℝ are closed and bounded by the Heine-Borel theorem. Being bounded means f(K) has a finite supremum M = sup f(K). Being closed means M ∈ f(K) — the supremum is actually achieved as a value of f. Therefore some x_max ∈ K satisfies f(x_max) = M. The argument for the minimum is identical.

Both hypotheses — continuity and compactness — are genuinely necessary, and studying their failure clarifies what each contributes. If you drop compactness: f(x) = 1/x on (0, 1] is continuous but unbounded above (f(x) → ∞ as x → 0⁺), so no maximum exists. The domain (0, 1] is bounded but not closed, hence not compact. If you drop continuity: the function f(x) = x for x ∈ [0, 1) with f(1) = 0 is defined on the compact set [0, 1], but it is discontinuous at x = 1. Its supremum is 1 (approached but never reached), so the maximum is not attained. Each hypothesis does specific work: compactness ensures the image is bounded and closed; continuity ensures the image of a compact set is compact.

The EVT is purely an **existence theorem** — it guarantees that a maximum and minimum exist but says nothing about where they occur or how to find them. The maximum could be at an interior point (where calculus gives f'(x) = 0 for differentiable functions) or at a boundary point of the domain. Finding extrema requires the separate machinery of critical points and boundary evaluation that you learned in calculus. What the EVT adds is the assurance that this search will succeed: the maximum and minimum are out there to be found, not asymptotically approached but never reached. This guarantee is what makes the closed-interval method of optimization logically sound.

## Questions

```yaml
- question: "The function f(x) = 1/x is continuous on (0, 1]. Does the Extreme Value Theorem guarantee that f attains a maximum on this interval?"
  type: multiple-choice
  options:
    - "Yes, because f is continuous on the interval (0, 1]"
    - "No, because (0, 1] is not compact — it is bounded but not closed, so the EVT does not apply"
    - "No, because f is not differentiable at x = 0"
    - "Yes, because every continuous function on a bounded interval attains its supremum"
  answer: 1
  explanation: "The EVT requires the domain to be compact (closed and bounded in ℝ). The interval (0, 1] is bounded but not closed — it is missing the endpoint 0. As x → 0⁺, f(x) = 1/x → ∞, so f is not even bounded above, much less attaining a maximum. This counterexample shows continuity alone does not suffice; compactness is an essential hypothesis. Option A is the classic misconception: continuity is necessary but not sufficient. Option D is false — f is unbounded above on (0, 1]."

- question: "What are the two key steps in the rigorous proof of the Extreme Value Theorem?"
  type: multiple-choice
  options:
    - "Step 1: Prove f is bounded above; Step 2: Prove the supremum is attained. Connected by the Bolzano-Weierstrass theorem."
    - "Step 1: Prove the continuous image of a compact set is compact; Step 2: Use Heine-Borel to conclude compact subsets of ℝ are closed, hence contain their supremum."
    - "Step 1: Prove the Intermediate Value Theorem; Step 2: Apply it to f − sup(f) to find a zero."
    - "Step 1: Prove f is uniformly continuous on the compact domain; Step 2: Use uniform continuity to construct a maximizing sequence."
  answer: 1
  explanation: "The proof has two essential steps. First: if K is compact and f is continuous, then f(K) is compact (compactness is preserved under continuous maps). Second: compact subsets of ℝ are closed and bounded by Heine-Borel; a closed set contains its own supremum and infimum. Together these guarantee that sup f(K) ∈ f(K) — meaning f actually attains its maximum. Bolzano-Weierstrass (option A) is an equivalent characterization of compactness but is not how the standard proof is structured."

- question: "A continuous function on a bounded open interval (a, b) is highly probable by the Extreme Value Theorem to attain its maximum."
  type: true-false
  answer: false
  explanation: "An open interval is not compact — it is bounded but not closed. The EVT requires the domain to be compact. A continuous function on (a, b) may approach its supremum as x → a or x → b without ever attaining it. For example, f(x) = x on (0, 1) has supremum 1 but attains no maximum on the open interval since x = 1 is not in the domain. The distinction between open and closed intervals is precisely why the closed interval [a, b] — which is compact by Heine-Borel — is the natural domain for optimization in calculus."

- question: "The Extreme Value Theorem guarantees that a continuous function on a compact set attains its maximum, but says nothing about where that maximum is located."
  type: true-false
  answer: true
  explanation: "This is correct and an important limitation to understand. The EVT is an existence theorem: it guarantees that some point x* exists satisfying f(x*) = max f, but says nothing about how to find x*. The maximum might be at an interior point (where calculus provides the tool: f'(x*) = 0 if f is differentiable) or at a boundary point. Locating the extremum requires additional tools; the EVT only guarantees it exists."

- question: "Explain why both hypotheses of the Extreme Value Theorem — continuity of f and compactness of the domain — are necessary. Give a counterexample showing what fails when each is dropped."
  type: short-answer
  answer: "Continuity is necessary: a discontinuous function on [0,1] can fail to attain its supremum (e.g., f(x) = x for x ∈ [0,1) and f(1) = 0 has supremum 1 but never attains it). Compactness is necessary: a continuous function on a non-compact domain can also fail (e.g., f(x) = 1/x on (0,1] is continuous but unbounded, attaining no maximum; g(x) = x on [0, ∞) is continuous but unbounded above). Without compactness, the continuous image need not be compact and so need not contain its own supremum."
  explanation: "Each hypothesis does genuine work in the proof. Continuity ensures that the image of the compact domain is compact. Compactness of the domain ensures the image is compact rather than merely bounded. Compact subsets of ℝ being closed (Heine-Borel) ensures the supremum is actually attained as an element of the image. Remove either hypothesis and one link in the chain 'compact domain + continuity → compact image → closed → contains its supremum' breaks."
```

