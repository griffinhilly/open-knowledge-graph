---
id: first-countability-definition
title: First Countability and Bases
domain: mathematics
course: topology
prerequisites:
- id: neighborhoods-topology-definition
  type: hard
- id: first-countable-spaces
  type: soft
builds-toward:
- second-countable-spaces
tags:
- first-countability
- countability
stage: formal-systems
status: validated
---
# First Countability and Bases

## Core Idea
A space is first-countable if every point has a countable neighborhood base. Metric spaces are first-countable. In first-countable spaces, sequential properties determine topology: f is continuous iff it preserves sequential limits. First-countability is weaker than second-countability but sufficient for many purposes.

## Questions

```yaml
- question: "In a first-countable topological space, a function f: X → Y is continuous if and only if which of the following holds?"
  type: multiple-choice
  options:
    - "f maps open sets to open sets"
    - "f maps every convergent sequence (xₙ → x) to a convergent sequence (f(xₙ) → f(x))"
    - "f is uniformly continuous on every compact subset of X"
    - "f has a countable range"
  answer: 1
  explanation: "First-countability is precisely the condition that makes sequences sufficient to detect continuity. In an arbitrary topological space, you need nets or filters to characterize continuity — a function can be sequentially continuous without being truly continuous. But in a first-countable space, the countable neighborhood base at each point means that every convergence question can be answered by sequences alone. Sequential continuity and continuity coincide. This is the central power of first-countability."

- question: "Which of the following topological spaces is NOT first-countable?"
  type: multiple-choice
  options:
    - "The real line ℝ with the standard (metric) topology"
    - "Any finite topological space"
    - "An uncountable product ℝᴵ where I is an uncountable index set"
    - "Any metric space with countably many points"
  answer: 2
  explanation: "The uncountable product ℝᴵ fails first-countability. At any point x, a neighborhood base must accommodate constraints on all possible finite coordinate subsets — but since I is uncountable, no countable collection of neighborhoods can probe every local constraint. In contrast, metric spaces (including ℝ) are always first-countable via the balls B(x, 1/n), and finite spaces have finite (hence countable) neighborhood bases. The uncountable product is the canonical example where sequences become genuinely insufficient."

- question: "Every metric space is first-countable, because the open balls B(x, 1/n) for n = 1, 2, 3, … form a countable neighborhood base at each point x."
  type: true-false
  answer: true
  explanation: "In any metric space, if U is any open set containing x, then by definition of openness there exists some ε > 0 with B(x, ε) ⊆ U. Choose n large enough that 1/n < ε; then B(x, 1/n) ⊆ U. So the collection {B(x, 1/n) : n ∈ ℕ} is a countable neighborhood base at x — every neighborhood of x contains some member of this collection. This confirms that all metric spaces satisfy first-countability, which is why metric-space intuition about sequences carries over to first-countable spaces generally."

- question: "In any topological space, a point p is in the closure of a set A if and only if p is the limit of a sequence of points in A."
  type: true-false
  answer: false
  explanation: "This characterization of closure via sequences holds in first-countable spaces but fails in general topological spaces. In a space that is not first-countable, a point can be in the closure of A without being the limit of any sequence from A — you need nets or filters to detect closure correctly. For example, in the uncountable product ℝᴵ, sequences are insufficient and nets are required. First-countability is exactly the condition that restores this sequential characterization of closure."

- question: "Why does first-countability allow sequences to replace nets and filters in describing convergence, continuity, and closure?"
  type: short-answer
  answer: "First-countability guarantees that each point x has a countable neighborhood base {Uₙ} — a countable collection of neighborhoods of x such that every neighborhood of x contains some Uₙ. This means that any topological fact about x (whether a function is continuous at x, whether x is a limit point of a set, whether a net converges to x) can be 'witnessed' by a sequence: you can always construct a sequence xₙ ∈ Uₙ that converges to x, and test every relevant property using that sequence. Without first-countability, no countable probe suffices — you need uncountably many 'directions' of approach simultaneously, which only nets or filters can capture."
  explanation: "The intuition is that a countable neighborhood base gives you enough resolution to detect the entire local structure at a point using sequences. Metric spaces are first-countable precisely because the balls B(x, 1/n) provide this resolution. When no countable base exists (as in uncountable products), sequences are blind to some topological features — a sequence might fail to converge to x even though every net-theoretic neighborhood of x is eventually entered. First-countability is the minimum condition to use 'metric-space thinking' about sequences in a purely topological setting."
```

## Explainer

From your study of neighborhoods in topology, you know that a **neighborhood base** at a point x is a collection of neighborhoods of x such that every neighborhood of x contains some member of the collection. Think of a neighborhood base as a set of "probes" of decreasing size around x — if you can detect everything about the local topology of x using just those probes, the base captures the full local picture. **First-countability** imposes one requirement: this base can be chosen to be countable.

In a metric space, the canonical example is the collection of open balls B(x, 1/n) for n = 1, 2, 3, …. These form a countable neighborhood base at x because every open set containing x contains some B(x, 1/n). This is why all metric spaces are first-countable. The intuition is that in a metric space, shrinking balls of radii 1, 1/2, 1/3, … give you enough resolution to detect all local structure — you never need uncountably many probes.

The power of first-countability is that it lets sequences do all the work of general nets or filters. In an arbitrary topological space, sequential convergence may not detect the full topology: a function can be "sequentially continuous" (preserves limits of sequences) without being truly continuous. But in a first-countable space, these notions coincide — a function is continuous if and only if it sends convergent sequences to convergent sequences. Similarly, a point is in the closure of a set A if and only if it is the limit of a sequence in A. This makes first-countable spaces feel much more like metric spaces, even when no actual metric is present.

The standard example of a space that fails first-countability is the **uncountable product** ℝᴵ where I is uncountable. At any point x, every basic open set is determined by restrictions on finitely many coordinates. To form a neighborhood base at x, you would need to accommodate all possible finite coordinate constraints — but since there are uncountably many coordinates, no countable collection of neighborhoods can serve as a base. In such spaces, sequences are genuinely insufficient: you must work with nets or filters to correctly describe continuity and closure.

**First-countability** sits between the general topological setting and the full strength of second-countability (which requires a countable base for the entire topology, not just at each point). It is the minimal condition that lets you use "sequence-based intuition" from calculus and metric space analysis in a purely topological setting. Whenever a theorem says "in a first-countable space, we can use sequences to characterize…," it is invoking the guarantee that countable probes at each point suffice to detect the local topology.
