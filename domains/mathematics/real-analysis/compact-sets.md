---
id: compact-sets
title: Compact Sets
domain: mathematics
course: real-analysis
prerequisites:
- id: open-sets-real-line
  type: hard
- id: subsequences
  type: hard
- id: closed-sets-real-line
  type: hard
builds-toward:
- heine-borel-theorem
- uniform-continuity-compact-sets
- extreme-value-theorem-rigorous
tags:
- compact
- compactness
- topology
- sequences
stage: advanced
status: validated
---

# Compact Sets

## Core Idea
A set K is compact if every open cover has a finite subcover: if K ⊆ ∪ᵢUᵢ with each Uᵢ open, then K ⊆ Uᵢ₁ ∪ ... ∪ Uᵢₙ for some finite selection. Intuitively, compact sets are 'closed and bounded' in ℝ and generalize finite sets to infinite settings. They are the workhorse of real analysis.

## Questions

```yaml
- question: "Which of the following sets in ℝ is compact?"
  type: multiple-choice
  options:
    - "(0, 1) — an open interval, bounded but not closed"
    - "[0, ∞) — a closed set that extends to infinity"
    - "[0, 1] — a closed and bounded interval"
    - "ℤ (the integers) — a closed set with isolated points"
  answer: 2
  explanation: "By the Heine-Borel theorem, a subset of ℝ is compact if and only if it is both closed AND bounded. [0, 1] satisfies both conditions. (0, 1) is bounded but not closed — it fails to contain its boundary points 0 and 1, allowing sequences to converge outside the set. [0, ∞) is closed but unbounded — sequences can escape to infinity. ℤ is closed (it contains all its limit points, vacuously — integers have no limit points in ℝ) but unbounded, so not compact. Both conditions are essential."

- question: "Consider the open cover of (0, 1) given by the intervals (1/n, 1) for n = 1, 2, 3, … . Why does this cover prove (0, 1) is not compact?"
  type: multiple-choice
  options:
    - "Because infinitely many intervals are needed to cover (0, 1), and compact sets can only be covered by finitely many open sets"
    - "Because this is a valid open cover of (0, 1) with no finite subcover — every finite subcollection fails to cover points near 0"
    - "Because the intervals overlap, violating the compactness condition"
    - "Because (0, 1) has infinitely many points, and compact sets must be finite"
  answer: 1
  explanation: "Compactness requires that *every* open cover has a finite subcover — not that some covers are finite, but that *all* of them are. The collection {(1/n, 1) : n ∈ ℕ} is a valid open cover of (0, 1): every point x ∈ (0, 1) lies in (1/n, 1) for sufficiently large n. But any finite subcollection {(1/n₁, 1), …, (1/nₖ, 1)} has a minimum 1/nₘₐₓ, and the points in (0, 1/nₘₐₓ) are not covered. Since this one cover has no finite subcover, (0, 1) fails the compactness definition. Option A confuses 'an infinite cover exists' (true for all infinite sets) with 'no finite subcover exists for this cover' (the actual failure)."

- question: "Nearly every closed subset of ℝ is compact."
  type: true-false
  answer: false
  explanation: "Compactness in ℝ requires *both* closed and bounded (Heine-Borel). A closed set can be unbounded and therefore not compact. For example, ℝ itself is closed (it contains all its limit points) but clearly not compact — the open cover {(−n, n) : n ∈ ℕ} has no finite subcover. Similarly, [0, ∞) is closed but not compact: the cover {[0, n) : n ∈ ℕ} has no finite subcover. Closedness prevents sequences from escaping through the boundary; boundedness prevents them from escaping to infinity. Both are needed."

- question: "Every sequence in a compact set K ⊆ ℝ has a subsequence that converges to a point in K."
  type: true-false
  answer: true
  explanation: "This is the sequential characterization of compactness, and it holds in all metric spaces (not just ℝ). The proof uses two properties of compact sets in ℝ: boundedness (guarantees a convergent subsequence exists by Bolzano-Weierstrass) and closedness (guarantees the limit of any convergent sequence in K stays in K). If K were only bounded, the subsequential limit might lie outside K. If K were only closed, Bolzano-Weierstrass might not apply (the sequence could be unbounded). The conjunction is precisely what compact sets provide."

- question: "Explain in your own words why the extreme value theorem — a continuous function on a compact set attains its maximum — requires compactness rather than just closedness or just boundedness."
  type: short-answer
  answer: "A continuous function on a closed but unbounded set can fail to attain its supremum by 'escaping to infinity' — for example, f(x) = x on [0, ∞) has no maximum. A continuous function on a bounded but open set can fail by approaching but never reaching a boundary value — for example, f(x) = 1/x on (0, 1] approaches infinity as x→0 without attaining it. Compactness (closed AND bounded) rules out both failure modes: boundedness keeps the function from escaping to infinity, and closedness ensures the supremum is actually achieved within the set."
  explanation: "The proof runs: since f is continuous and K is compact, the image f(K) is also compact (continuous images of compact sets are compact). A compact subset of ℝ is closed and bounded, hence contains its supremum. So the supremum of f(K) is in f(K), meaning some point in K achieves it. Each piece of compactness blocks one escape route: boundedness keeps f(K) from going to ±∞, and closedness keeps the sup from being a limit that f never actually hits."
```

## Explainer

From your work on open sets, you know that an open interval like (0, 1) has no "edge" — every point has a neighborhood contained entirely within the set. From your work on subsequences, you know that every sequence in a bounded set has a convergent subsequence (Bolzano-Weierstrass). Compact sets bring these two threads together: a set is compact when it is "tight enough" that infinite processes on it cannot escape. The formal definition — every open cover has a finite subcover — captures this tightness in a way that turns out to be extraordinarily powerful.

To feel why the definition matters, try to cover [0, 1] with open sets. Take any collection of open intervals whose union contains every point of [0, 1]. The compactness claim is that some finite subcollection already covers [0, 1]. Now try the same for (0, 1). Cover it with the intervals (1/n, 1) for n = 1, 2, 3, …. Each point of (0, 1) is eventually inside some (1/n, 1) — so this is a valid cover. But no finite subcollection works: dropping any finitely many intervals leaves some neighborhood of 0 uncovered. The set (0, 1) "escapes" toward 0, which it never reaches. Closed sets prevent this escape at their boundary; bounded sets prevent escape to infinity. Together — closed and bounded in ℝ — they give you compactness. This is the content of the Heine–Borel theorem.

The **sequential characterization** of compactness connects directly to your subsequence prereq: K is compact if and only if every sequence in K has a subsequence converging to a point also in K. This is often the more intuitive definition to work with. Consider why [0, 1] satisfies it: take any sequence in [0, 1]; by Bolzano-Weierstrass it has a convergent subsequence; since [0, 1] is closed, the limit point also lies in [0, 1]. Both conditions — boundedness (so Bolzano-Weierstrass gives a convergent subsequence) and closedness (so the limit stays in the set) — are essential and mirror each other.

Compact sets are the natural domain for three of analysis's most important results. The **extreme value theorem** holds because a continuous function on a compact set achieves its maximum and minimum — the function cannot "approach" a supremum without actually hitting it. **Uniform continuity** holds because a continuous function on a compact set cannot vary "faster and faster" at different places — the compactness forces a single δ to work everywhere. **Sequential convergence results** become tractable because you can always extract convergent subsequences. Whenever a theorem in analysis begins "let K be compact," read it as: "let K be a set with no way to escape, so every infinite process is forced to converge within it." That forcing is what makes the powerful conclusions possible.

The concept generalizes beyond ℝ. In metric spaces, compactness is still equivalent to sequential compactness (every sequence has a convergent subsequence). In general topological spaces, the open cover definition is primary — "closed and bounded" has no meaning without a metric. This is why the open cover definition is the right one to remember: it works everywhere. But for all your work in ℝ and ℝⁿ, translating between the open cover definition, the closed-and-bounded characterization, and the sequential characterization is a core skill — each formulation is the right tool for different proofs.
