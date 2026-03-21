---
id: weak-star-convergence
title: Weak* Convergence
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: weak-convergence
  type: hard
- id: dual-spaces-bounded-functionals
  type: hard
builds-toward:
- reflexive-spaces
tags:
- convergence
- weak-topology
stage: advanced
status: draft
---

# Weak* Convergence

## Core Idea
A sequence of functionals (fₙ) in X* converges weak* to f if fₙ(x) → f(x) for every x ∈ X. The weak* topology on X* enables compactness: the closed unit ball is weak* compact (Alaoglu's theorem).

## Questions

```yaml
- question: "In a non-reflexive Banach space X, what is the essential difference between weak convergence and weak* convergence in X*?"
  type: multiple-choice
  options:
    - "Weak* convergence is stronger — it requires fₙ(x) → f(x) for more test functions"
    - "Weak* convergence tests functionals against elements of X; weak convergence in X* tests against all elements of X** (the double dual)"
    - "They are equivalent by the Hahn-Banach theorem for all Banach spaces"
    - "Weak* convergence is defined only for Hilbert spaces, not general Banach spaces"
  answer: 1
  explanation: "Weak* convergence in X* requires fₙ(x) → f(x) for every x ∈ X — testing against the original space. Weak convergence in X* would require testing against every element of (X*)* = X**, the double dual. Since X embeds isometrically into X** but may not equal it (when X is not reflexive), weak* convergence imposes fewer conditions. It is a coarser topology: more sequences converge weak* than weakly. In a reflexive space X = X** and the two coincide."

- question: "A student claims: 'Banach-Alaoglu is unsurprising — any bounded sequence in a Banach space has a convergent subsequence.' What is the critical error in this reasoning?"
  type: multiple-choice
  options:
    - "Bounded sequences only have convergent subsequences in finite-dimensional spaces; Riesz's theorem shows the unit ball is not norm-compact in infinite dimensions"
    - "Alaoglu's theorem applies to weak convergence, not weak* convergence"
    - "Bounded sequences always converge in norm if the space is complete"
    - "The result only holds when the dual space X* is separable"
  answer: 0
  explanation: "Riesz's theorem states that the closed unit ball in an infinite-dimensional normed space is never compact in the norm topology — there always exist sequences with no norm-convergent subsequence. Alaoglu rescues compactness by switching topologies: the closed unit ball in X* IS compact in the weak* topology (a coarser topology, so compactness is easier to achieve). The student's claim confuses the weak* topology with the norm topology. This is why Alaoglu is profound, not trivial."

- question: "In a reflexive Banach space, every weakly convergent sequence in X* is also weak* convergent."
  type: true-false
  answer: true
  explanation: "In a reflexive space, X is isometrically isomorphic to X** via the canonical embedding — every bounded linear functional on X* is represented by an element of X. Therefore the weak topology on X* (testing against X**) and the weak* topology on X* (testing against X) coincide. Any weakly convergent sequence is automatically weak* convergent and vice versa."

- question: "If (fₙ) converges weak* to f in X*, then (fₙ) converges in norm to f."
  type: true-false
  answer: false
  explanation: "Weak* convergence is strictly weaker than norm convergence. Norm convergence requires ‖fₙ − f‖ → 0, meaning the functionals become uniformly close on the entire unit ball. Weak* convergence only requires fₙ(x) → f(x) pointwise for each fixed x ∈ X — there is no uniformity requirement. A sequence can converge weak* while ‖fₙ − f‖ remains bounded away from zero. The Banach-Alaoglu theorem exploits exactly this gap."

- question: "Why is the weak* topology — rather than the norm topology — the right setting for Alaoglu's compactness theorem, and what makes this theorem useful in practice?"
  type: short-answer
  answer: "Riesz's theorem shows the unit ball in an infinite-dimensional space is never norm-compact, so norm topology cannot supply compactness. The weak* topology on X* is defined only by pointwise convergence against elements of X — a coarser topology with fewer open sets — making it easier for sequences to converge and for sets to be compact. Alaoglu's theorem states the closed unit ball in X* is weak* compact. In practice, this lets you take a bounded sequence of approximate solutions (functionals or measures), extract a weak* convergent subnet via Alaoglu, and show the weak* limit is an exact solution — a pattern that drives existence proofs across analysis, PDEs, and variational calculus."
```

## Explainer

You now know two modes of convergence for sequences in a normed space: norm convergence (strong convergence), and **weak convergence**, where xₙ → x weakly if f(xₙ) → f(x) for every bounded linear functional f. Weak* convergence lives one level higher: instead of testing vectors against functionals, it tests **functionals against vectors**. A sequence (fₙ) in the dual space X* converges **weak*** to f if fₙ(x) → f(x) for every fixed x ∈ X. The "star" marks that the dual space X* is now the space being tested, and the original space X provides the test functions.

The distinction between weak and weak* convergence matters when X is not reflexive. Recall from your dual spaces prerequisite that the dual of X is X*, and the double dual is X**. Weak convergence in X* means testing against elements of (X*)* = X** — every functional on X*. Weak* convergence tests only against the elements of X sitting inside X** via the canonical embedding. This is a strictly coarser topology when X is not reflexive: there are more weak* convergent sequences than weakly convergent ones in X*. In a reflexive space, X = X** and the two topologies coincide.

Why does this weaker topology matter? Because it enables compactness. The **Banach-Alaoglu theorem** states that the closed unit ball in X* is compact in the weak* topology — for any normed space X. This is a profound statement because the unit ball in an infinite-dimensional space is never compact in the norm topology (Riesz's theorem). Weak* compactness rescues compactness arguments that would otherwise fail in infinite dimensions, and is the engine behind many existence proofs in analysis, PDEs, and optimization: extract a bounded sequence of approximate solutions, use Alaoglu to find a weak* convergent subnet or subsequence, then show the limit is an exact solution.

A concrete instance: in L^∞([0,1]), the dual of L¹, a bounded sequence of functions (gₙ) in L^∞ with ‖gₙ‖∞ ≤ 1 always has a weak* convergent subnet. Weak* convergence here means ∫gₙh → ∫gh for every h ∈ L¹. This limit g need not be pointwise limit, it need not converge in norm, but it exists and is bounded — which is enough for many applications. This "weak* limit extraction" technique appears throughout harmonic analysis, probability theory (as tightness and vague convergence of measures), and the calculus of variations.
