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
status: draft
---

# Compact Sets

## Core Idea
A set K is compact if every open cover has a finite subcover: if K ⊆ ∪ᵢUᵢ with each Uᵢ open, then K ⊆ Uᵢ₁ ∪ ... ∪ Uᵢₙ for some finite selection. Intuitively, compact sets are 'closed and bounded' in ℝ and generalize finite sets to infinite settings. They are the workhorse of real analysis.

## Explainer

From your work on open sets, you know that an open interval like (0, 1) has no "edge" — every point has a neighborhood contained entirely within the set. From your work on subsequences, you know that every sequence in a bounded set has a convergent subsequence (Bolzano-Weierstrass). Compact sets bring these two threads together: a set is compact when it is "tight enough" that infinite processes on it cannot escape. The formal definition — every open cover has a finite subcover — captures this tightness in a way that turns out to be extraordinarily powerful.

To feel why the definition matters, try to cover [0, 1] with open sets. Take any collection of open intervals whose union contains every point of [0, 1]. The compactness claim is that some finite subcollection already covers [0, 1]. Now try the same for (0, 1). Cover it with the intervals (1/n, 1) for n = 1, 2, 3, …. Each point of (0, 1) is eventually inside some (1/n, 1) — so this is a valid cover. But no finite subcollection works: dropping any finitely many intervals leaves some neighborhood of 0 uncovered. The set (0, 1) "escapes" toward 0, which it never reaches. Closed sets prevent this escape at their boundary; bounded sets prevent escape to infinity. Together — closed and bounded in ℝ — they give you compactness. This is the content of the Heine–Borel theorem.

The **sequential characterization** of compactness connects directly to your subsequence prereq: K is compact if and only if every sequence in K has a subsequence converging to a point also in K. This is often the more intuitive definition to work with. Consider why [0, 1] satisfies it: take any sequence in [0, 1]; by Bolzano-Weierstrass it has a convergent subsequence; since [0, 1] is closed, the limit point also lies in [0, 1]. Both conditions — boundedness (so Bolzano-Weierstrass gives a convergent subsequence) and closedness (so the limit stays in the set) — are essential and mirror each other.

Compact sets are the natural domain for three of analysis's most important results. The **extreme value theorem** holds because a continuous function on a compact set achieves its maximum and minimum — the function cannot "approach" a supremum without actually hitting it. **Uniform continuity** holds because a continuous function on a compact set cannot vary "faster and faster" at different places — the compactness forces a single δ to work everywhere. **Sequential convergence results** become tractable because you can always extract convergent subsequences. Whenever a theorem in analysis begins "let K be compact," read it as: "let K be a set with no way to escape, so every infinite process is forced to converge within it." That forcing is what makes the powerful conclusions possible.

The concept generalizes beyond ℝ. In metric spaces, compactness is still equivalent to sequential compactness (every sequence has a convergent subsequence). In general topological spaces, the open cover definition is primary — "closed and bounded" has no meaning without a metric. This is why the open cover definition is the right one to remember: it works everywhere. But for all your work in ℝ and ℝⁿ, translating between the open cover definition, the closed-and-bounded characterization, and the sequential characterization is a core skill — each formulation is the right tool for different proofs.
