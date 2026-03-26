---
id: neighborhoods-topology-definition
title: Neighborhoods and Neighborhood Bases
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
builds-toward:
- continuity-topological-definition
- limit-points-topology-definition
tags:
- neighborhoods
- local-structure
stage: formal-systems
status: validated
---

# Neighborhoods and Neighborhood Bases

## Core Idea
A neighborhood of a point x is any set N containing an open set U with x ∈ U. A neighborhood base at x is a collection {Bᵢ} of neighborhoods such that every neighborhood of x contains some Bᵢ. Neighborhoods encode local topological structure; a set is open iff it is a neighborhood of each of its points.

## Questions

```yaml
- question: "Is the closed interval [0.9, 1.1] a neighborhood of the point 1 in ℝ with the standard topology?"
  type: multiple-choice
  options:
    - "No — a neighborhood must itself be an open set, and [0.9, 1.1] is closed"
    - "Yes — [0.9, 1.1] contains the open interval (0.95, 1.05) which contains 1"
    - "No — only open balls qualify as neighborhoods in metric spaces"
    - "Yes — but only after redefining the topology to include closed sets"
  answer: 1
  explanation: "A neighborhood of x is any set N containing an open set U with x ∈ U ⊆ N. The closed interval [0.9, 1.1] is a neighborhood of 1 because it contains the open interval (0.95, 1.05), which is open and contains 1. Neighborhoods do not need to be open — that is the point of the definition. Option A expresses the most common misconception: that 'neighborhood' and 'open set' are synonyms. The whole power of the neighborhood concept is precisely that it allows non-open sets to capture local structure."

- question: "The open balls {B(x, 1/n) : n ∈ ℕ} form a neighborhood base at x in any metric space. What property of the space does this imply?"
  type: multiple-choice
  options:
    - "The space is second-countable: a single countable base covers the entire topology"
    - "The space is first-countable: every point has a countable neighborhood base"
    - "Sequences are insufficient to detect closure, so nets or filters are required"
    - "Every neighborhood of x can be expressed as a finite union of these balls"
  answer: 1
  explanation: "A countable neighborhood base at every point is exactly the definition of a first-countable space. All metric spaces are first-countable because the balls B(x, 1/n) form such a base: any neighborhood of x must contain some ball of this form. First-countability matters because it ensures sequences are sufficient to detect topological structure — x is in the closure of A iff some sequence in A converges to x. Option A confuses first-countability (countable base at each point) with second-countability (one countable base for the whole topology, a strictly stronger condition)."

- question: "A neighborhood of a point x should itself be an open set."
  type: true-false
  answer: false
  explanation: "This is the central misconception about neighborhoods. A neighborhood of x is any set N that contains an open set U with x ∈ U ⊆ N — N itself need not be open. Closed intervals, half-open sets, or any set that 'wraps around' an open set containing x qualify. For example, [0, 1] is a neighborhood of 0.5 because it contains the open interval (0.3, 0.7). The definition is deliberately flexible: neighborhoods absorb boundary behavior while preserving the local information encoded in the open sets they contain."

- question: "A set U is open in a topological space if and only if U is a neighborhood of each of its points."
  type: true-false
  answer: true
  explanation: "This is a theorem connecting global and local perspectives on openness. If U is open, then U itself witnesses that U is a neighborhood of every x ∈ U (since U is open and x ∈ U ⊆ U). Conversely, if every point x ∈ U has some open set Uₓ with x ∈ Uₓ ⊆ U, then U = ∪{Uₓ : x ∈ U} is a union of open sets, hence open. This local characterization is useful because it lets you prove openness point-by-point rather than checking a global condition all at once."

- question: "Why does first-countability matter for the relationship between sequences and topological structure?"
  type: short-answer
  answer: "In a first-countable space, sequences are sufficient to capture all closure information: a point x is in the closure of a set A if and only if some sequence in A converges to x. The countable neighborhood base allows you to construct a sequence by picking one point from each ball B(x, 1/n) ∩ A. In spaces that fail first-countability, this construction breaks down — there can be points in the closure of A that no sequence in A approaches. In those spaces, the more general tools of nets or filters are required to detect topological structure."
  explanation: "The connection between sequences and topology is one reason metric spaces behave so much more tractably than general topological spaces: every metric space is first-countable, so the intuitions built up in real analysis (where sequences do all the work) transfer directly. Failure of first-countability is the precise obstruction that forces analysts working in function spaces or spaces of distributions to abandon sequences in favor of nets."
```

## Explainer

Open sets, from your prerequisite, are defined globally: a set is either in the topology or it isn't. **Neighborhoods** reframe the same information locally — they let you talk about "what the space looks like near this particular point" without specifying the whole topology at once. A neighborhood of x is any set N that contains an open set U with x ∈ U ⊆ N. The key flexibility is that N itself need not be open: the closed interval [0.9, 1.1] is a neighborhood of 1 in ℝ, because the open interval (0.95, 1.05) sits inside it and contains 1. Neighborhoods are "open sets with wiggle room" — they absorb boundaries without losing the local information.

The equivalence "U is open iff U is a neighborhood of each of its points" is not a definition but a theorem, and it repackages the definition of open sets in local terms. If U is open and x ∈ U, then U itself witnesses that U is a neighborhood of x. Conversely, if every point of U has some open set around it inside U, you can take the union of all these open sets to reconstruct U itself — so U is open. This local characterization is useful because it lets you prove openness point by point, which is often easier than verifying the global condition directly.

A **neighborhood base** (local base) at x is a collection {Bᵢ} of neighborhoods of x such that every neighborhood of x contains some Bᵢ. In a metric space, the open balls {B(x, 1/n) : n ∈ ℕ} form a countable neighborhood base at every point: any neighborhood of x must contain some ball, and you only need to check ball-sized neighborhoods to understand the local structure completely. Spaces where every point has a *countable* neighborhood base are called **first-countable**; all metric spaces are first-countable. This property is important because first-countability is exactly what allows sequences to detect topological structure — a point x is in the closure of A if and only if some sequence in A converges to x. In spaces that fail first-countability, sequences are insufficient and the more general tools of nets or filters are required.

Neighborhoods provide the sharpest formulation of **continuity at a point**. A function f: X → Y is continuous at x if and only if for every neighborhood V of f(x), there is a neighborhood U of x with f(U) ⊆ V. Compare this to the ε-δ definition from calculus: ε defines a neighborhood (x − ε, x + ε) of the output, and δ defines a neighborhood (x − δ, x + δ) of the input. The neighborhood version is identical in structure but works in any topological space with no distance function needed. This is how the intuition from calculus carries over wholesale into the abstract setting.
