---
id: compact-sets-heine-borel
title: Compact Sets and the Heine-Borel Theorem
domain: mathematics
course: real-analysis
prerequisites:
- id: open-closed-sets-real-line
  type: hard
- id: bolzano-weierstrass-theorem
  type: soft
- id: uniform-continuity-compact-sets
  type: soft
builds-toward:
- extreme-value-theorem-rigorous
- uniform-continuity-compact-sets
tags:
- compactness
- heine-borel
- closed-bounded
- covering
stage: advanced
status: validated
---
# Compact Sets and the Heine-Borel Theorem

## Core Idea
A set K in ℝ is compact if every open cover has a finite sub-cover. The Heine-Borel Theorem states that a set is compact if and only if it is closed and bounded. Compact sets have many excellent properties: continuous images are compact, and continuous functions attain extrema on compact sets.

## Questions

```yaml
- question: "The half-open interval [0, 1) is bounded. Is it compact?"
  type: multiple-choice
  options:
    - "Yes — it is bounded, and boundedness is sufficient for compactness in ℝ"
    - "No — it is not closed, so it fails the Heine-Borel condition; an open cover can slide off the missing boundary at 1"
    - "Yes — it is connected and contains its left endpoint, which is sufficient"
    - "No — it contains infinitely many points, so no finite subcover can work"
  answer: 1
  explanation: "Heine-Borel requires BOTH closed and bounded. [0, 1) is bounded but not closed — the limit point 1 is missing. Concretely, the open cover {[0, 1 − 1/n) : n = 1, 2, 3, …} covers [0, 1) but no finite subcollection does, since any finite sublist leaves a neighborhood of 1 uncovered. Option D is a common misunderstanding: containing infinitely many points has nothing to do with compactness — [0, 1] is also infinite and is compact."

- question: "A student claims that every closed set in ℝ is compact. Which example best refutes this?"
  type: multiple-choice
  options:
    - "The empty set ∅ — it is closed but trivially has no points"
    - "The entire real line ℝ — it is closed but unbounded, and the cover {(−n, n) : n = 1, 2, …} has no finite subcover"
    - "The rationals ℚ — they are not closed in ℝ, so this is not a counterexample"
    - "The open interval (0, 1) — it is not closed, so this is not a counterexample"
  answer: 1
  explanation: "ℝ itself is closed (it contains all its limit points) but is not bounded — you can cover it with {(−n, n) : n = 1, 2, 3, …}, and no finite subcollection covers all of ℝ. This shows that closedness alone is insufficient: you also need boundedness. Options C and D are not counterexamples to the student's claim because they fail to be closed; you need a set that IS closed but fails compactness."

- question: "A set in ℝ is compact if and only if it is bounded."
  type: true-false
  answer: false
  explanation: "Boundedness alone is not sufficient. The Heine-Borel Theorem requires the set to be both closed AND bounded. The open interval (0, 1) is bounded but not compact (it is not closed). Conversely, [0, ∞) is closed but not compact (it is not bounded). Both conditions are independently necessary."

- question: "The Extreme Value Theorem — that a continuous function on a closed interval [a, b] attains its maximum and minimum — holds precisely because [a, b] is compact."
  type: true-false
  answer: true
  explanation: "This is the key application of Heine-Borel. The proof runs: [a, b] is compact (closed and bounded, by Heine-Borel). Continuous images of compact sets are compact. Therefore f([a, b]) is compact in ℝ — closed and bounded — so it contains its supremum and infimum. The EVT is not a standalone result; it is a corollary of compactness and the continuity of f."

- question: "Why does the open interval (0, 1) fail to be compact, even though it is bounded? Use the open-cover definition."
  type: short-answer
  answer: "The open cover {(1/n, 1) : n = 1, 2, 3, …} covers every point in (0, 1) — any x > 0 eventually satisfies x > 1/n. But no finite subcollection covers (0, 1): any finite sub-list has a largest n, say N, and the set (1/N, 1) leaves points in (0, 1/N] uncovered. The failure occurs because 0 is a limit point of (0, 1) that is not in the set — the cover can 'slide' toward the missing boundary point without ever being trapped by finitely many sets."
  explanation: "Closedness in the Heine-Borel theorem plays exactly this role: it prevents the escape toward missing boundary points. Adding 0 to get [0, 1] traps the cover — any open set covering 0 covers a neighborhood of 0, and from there finitely many of the (1/n, 1) suffice. The open interval's incompactness is a direct consequence of its missing boundary."
```

## Explainer

You already know the distinction between open and closed sets on the real line, and you may know the Bolzano-Weierstrass theorem — every bounded sequence has a convergent subsequence. Compactness is the structural property that explains *why* results like Bolzano-Weierstrass hold, and it does so through a deceptively elegant definition: a set K is **compact** if every **open cover** of K has a **finite subcover**. An open cover is any collection of open sets whose union contains K; the definition demands that no matter how many (even infinitely many) open sets you choose to cover K, you can always discard all but finitely many and still cover K.

The definition sounds abstract until you see it fail. Consider the open interval (0, 1). Cover it with the open sets (1/n, 1) for n = 1, 2, 3, … Every point in (0, 1) is eventually in one of these sets, so this is a valid cover. But no finite subcollection works — any finite sublist misses a neighborhood of 0. This is why (0, 1) is not compact: it's bounded but not closed. Now try the same trick on [0, 1]. You can't: any open cover of [0, 1] must include a set covering 0 and a set covering 1, and once those are in, finitely many more sets suffice. Closedness is what "traps" the boundary and prevents the cover from sliding away to infinity.

The **Heine-Borel Theorem** makes this precise: in ℝⁿ, a set is compact *if and only if* it is closed and bounded. This is a characterization unique to Euclidean space — the equivalence fails in general metric spaces. Boundedness ensures you can't escape to infinity; closedness ensures limit points are included. Together they make every open cover reducible to a finite one. The real payoff comes from what compact sets guarantee: if f is continuous on a compact set K, then f(K) is also compact (hence closed and bounded), and f attains its maximum and minimum on K. The Extreme Value Theorem you know from calculus is a corollary — it works *because* [a, b] is compact.

The Bolzano-Weierstrass theorem is the sequential counterpart: every sequence in a compact set has a convergent subsequence whose limit is also in the set. This sequential compactness characterization is equivalent to open-cover compactness in ℝⁿ, and it's often easier to apply in proofs. Think of compactness as a finiteness property dressed in topological clothing: it limits how "infinite" the structure of a set can be, forcing any description of its neighborhoods to reduce to something manageable. That finiteness is what makes compact sets the preferred domain for analysis — it is much easier to prove theorems when you cannot escape to infinity or sneak out through a missing boundary point.
