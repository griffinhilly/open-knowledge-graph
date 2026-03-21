---
id: sequential-compactness
title: Sequential Compactness
domain: mathematics
course: topology
prerequisites:
- id: compact-spaces-open-covers
  type: hard
builds-toward:
- metrization-theorems
tags:
- sequential-compactness
- convergent-subsequences
stage: advanced
status: draft
---

# Sequential Compactness

## Core Idea
A space is sequentially compact if every sequence has a convergent subsequence. In metric spaces, sequential compactness is equivalent to compactness, but in general topology they differ. Sequential compactness characterizes compactness using sequences, the more intuitive notion from calculus.

## Questions

```yaml
- question: "You want to prove that a continuous function f: X → ℝ achieves its maximum on X. You take a maximizing sequence (xₙ) with f(xₙ) → sup f. What property of X allows you to extract a convergent subsequence and complete the proof?"
  type: multiple-choice
  options:
    - "X must be connected, so f cannot skip values on the way to its supremum"
    - "X must be path-connected, allowing continuous curves between any two points"
    - "X must be sequentially compact, guaranteeing a subsequence xₙₖ → x* in X so continuity gives f(x*) = sup f"
    - "X must be bounded so the sequence cannot escape to infinity"
  answer: 2
  explanation: "Boundedness alone is insufficient — a bounded sequence can still converge outside the set (e.g., in an open interval). Sequential compactness guarantees two things: first, a convergent subsequence exists; second, the limit is in X. Then continuity of f gives f(x*) = lim f(xₙₖ) = sup f. This argument pattern — take a sequence, extract a convergent subsequence, identify the limit as a solution — is the core technique that makes sequential compactness practically valuable in analysis."

- question: "In which setting are sequential compactness and compactness (open-cover definition) guaranteed to be equivalent?"
  type: multiple-choice
  options:
    - "In all topological spaces — the two definitions always describe the same property"
    - "In metric spaces — the metric structure allows sequences to capture the full topology"
    - "In Hausdorff spaces — the separation axiom is sufficient for the equivalence"
    - "Only in finite topological spaces — infinite spaces can always be constructed to separate the two"
  answer: 1
  explanation: "The equivalence holds in metric spaces, where the metric allows sequences to detect all open-set behavior through total boundedness and completeness arguments. In general topological spaces, the equivalence fails: there exist compact spaces that are not sequentially compact, and sequentially compact spaces that are not compact. Without a metric, sequences are too coarse an instrument to fully detect the topology — you need nets or filters to capture everything open covers can express."

- question: "A space can be sequentially compact without being compact (in the open-cover sense) when considered as a general topological space."
  type: true-false
  answer: true
  explanation: "The equivalence between sequential compactness and compactness is a theorem specific to metric spaces, not a universal truth. In general topological spaces, there are sequentially compact spaces that are not compact (uncountable products can exhibit this), and compact spaces that are not sequentially compact. This is why topology distinguishes the two concepts: each captures a different aspect of 'finiteness' in a space, and they only coincide when the metric provides enough structure for sequences to do the full job."

- question: "The open interval (0, 1) fails to be sequentially compact because it contains unbounded sequences."
  type: true-false
  answer: false
  explanation: "Every sequence in (0, 1) is bounded — the issue is not boundedness but whether limit points stay in the space. The sequence 1/n is bounded (all terms lie in (0, 1)) but converges to 0, which is outside (0, 1). So no subsequence of 1/n can converge within (0, 1). Sequential compactness requires that the limit of the convergent subsequence belongs to the space itself. Closedness is the missing property here — (0, 1) lacks its boundary points, which are exactly where sequences can 'escape.'"

- question: "Why is it insufficient to know a sequence in (0, 1) is bounded in order to conclude that (0, 1) is sequentially compact?"
  type: short-answer
  answer: "Sequential compactness requires that every sequence has a convergent subsequence whose limit is in the space. A bounded sequence in (0, 1) may have a convergent subsequence, but the limit might be 0 or 1 — points outside (0, 1). The space must be closed to guarantee limit points stay inside. Boundedness ensures subsequences exist (by Bolzano-Weierstrass in ℝ), but closedness ensures the limit is in the space. Sequential compactness requires both."
  explanation: "The Bolzano-Weierstrass theorem guarantees convergent subsequences for bounded sequences in ℝ, but sequential compactness is a property of the space, not of ℝ. The closed interval [0, 1] is sequentially compact precisely because it is both bounded (so subsequences converge in ℝ) and closed (so the limits stay inside). Remove closedness by taking (0, 1) and the boundary points 0 and 1 become escape routes. This is why 'closed and bounded' (Heine-Borel) characterizes compact sets in ℝⁿ."
```

## Explainer

You already know that **compactness** — defined via open covers — is one of the most powerful properties a topological space can have. But the open cover definition is notoriously abstract: a space is compact if every open cover has a finite subcover. It tells you what compactness does (any covering has a finite reduction), but it doesn't say anything about how individual points or sequences behave. Sequential compactness offers a different perspective using the language of sequences, which is more directly intuitive for anyone who has studied calculus.

A space X is **sequentially compact** if every sequence (xₙ) in X has a **convergent subsequence** — a subsequence (xₙₖ) that converges to some point in X. Think about what this means in ℝ: the Bolzano-Weierstrass theorem says every bounded sequence in ℝ has a convergent subsequence. The closed interval [0, 1] is sequentially compact because no sequence in [0, 1] can escape to infinity, and by Bolzano-Weierstrass, some subsequence must converge — and since [0, 1] is closed, the limit must land back in [0, 1]. The open interval (0, 1) is not sequentially compact: the sequence 1/n converges to 0, which is outside (0, 1), so no subsequence converges within the space.

In metric spaces, sequential compactness and compactness are equivalent — they capture the same property in two different vocabularies. This equivalence is not obvious to prove; it requires showing that in a metric space, having the Bolzano-Weierstrass property (convergent subsequences) is the same as having no infinite open cover that can't be reduced to a finite one. The proof goes through the concept of **total boundedness** (the space can be covered by finitely many ε-balls for any ε > 0) and uses the metric structure in an essential way. This is why the equivalence breaks down in general topological spaces — without a metric, sequences don't capture the full complexity of the topology. There exist compact spaces that are not sequentially compact, and sequentially compact spaces that are not compact, in the general topological setting.

The practical value of sequential compactness is that it gives you a hands-on tool for proving things about compact metric spaces. To show a function achieves its maximum on a compact metric space, you can take a maximizing sequence (f(xₙ) → sup f) and extract a convergent subsequence (xₙₖ → x*) — then continuity shows f(x*) = sup f. To show a set is compact, you can produce convergent subsequences from arbitrary sequences. Many existence proofs in analysis follow exactly this pattern: take a sequence of approximate solutions, extract a convergent subsequence, and identify the limit as an exact solution. Sequential compactness makes these arguments rigorous.
