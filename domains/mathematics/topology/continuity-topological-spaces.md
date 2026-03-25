---
id: continuity-topological-spaces
title: Continuity in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
- id: neighborhoods-in-topology
  type: soft
- id: convergence-in-topology
  type: soft
builds-toward:
- homeomorphisms-topological-equivalence
- topological-invariants
tags:
- continuity
- continuous-functions
- preimages
stage: advanced
status: validated
---
# Continuity in Topological Spaces

## Core Idea
A function f: X → Y between topological spaces is continuous if the preimage of every open set is open (equivalently, preimages of closed sets are closed, or preimages of neighborhoods are neighborhoods). This topological definition removes reliance on distance and applies to any pair of topological spaces, unifying continuity across algebra, analysis, and geometry.

## Questions

```yaml
- question: "Consider the constant function f: ℝ → ℝ defined by f(x) = 0. Which of the following correctly applies the topological definition of continuity?"
  type: multiple-choice
  options:
    - "f is not continuous because the image f(ℝ) = {0} is not open in ℝ"
    - "f is continuous because f⁻¹(V) is open in ℝ for every open set V in ℝ"
    - "f is continuous because f sends every open set in ℝ to an open set in ℝ"
    - "f is not continuous because no ε-δ bound exists that works globally"
  answer: 1
  explanation: "For any open set V in ℝ: if 0 ∈ V then f⁻¹(V) = ℝ, which is open; if 0 ∉ V then f⁻¹(V) = ∅, which is also open. So f is continuous. The image {0} being non-open is irrelevant — continuity requires preimages of open sets to be open, not images. Option C describes an 'open map,' a separate and stronger condition."

- question: "The topological definition of continuity uses preimages of open sets rather than epsilon-delta conditions primarily because:"
  type: multiple-choice
  options:
    - "Preimages are easier to compute than epsilon-delta bounds in concrete analysis"
    - "The epsilon-delta definition is incorrect even for functions on ℝ"
    - "The preimage condition can be stated on any topological space, including those with no notion of distance"
    - "Preimages of open sets are always open, making continuity automatic in any space"
  answer: 2
  explanation: "The epsilon-delta definition is built around absolute values — a distance measure — and cannot be stated for a space with no metric. The preimage definition uses only the open sets (the topology), which can be specified on any set regardless of distance. This unifies continuity across real analysis, abstract algebra, geometry, and functional analysis under a single definition."

- question: "If f: X → Y is continuous and C is a closed set in Y, then f⁻¹(C) is closed in X."
  type: true-false
  answer: true
  explanation: "Since C is closed, Y \\ C is open. Continuity means f⁻¹(Y \\ C) is open in X. But f⁻¹(Y \\ C) = X \\ f⁻¹(C), so X \\ f⁻¹(C) is open, which means f⁻¹(C) is closed. The open-set and closed-set characterizations of continuity are fully equivalent — preimages commute with complements."

- question: "If f: X → Y is a continuous function between topological spaces, then the image of every open set in X is open in Y."
  type: true-false
  answer: false
  explanation: "This is the most common confusion about topological continuity. The constant function f(x) = c maps every open set to the single point {c}, which is not open. Continuity only guarantees that preimages — not images — of open sets are open. A function that sends open sets to open sets is called an 'open map,' which is a distinct property that continuous functions need not have."

- question: "Why does the topological definition of continuity use preimages rather than forward images? What would go wrong if we instead defined continuity as 'the image of every open set is open'?"
  type: short-answer
  answer: "Continuity captures the idea that outputs near f(x) come from inputs near x — i.e., f doesn't 'tear' or 'jump.' The preimage f⁻¹(V) asks which inputs lead to outputs in the neighborhood V; requiring this to be open ensures inputs producing outputs near f(x) must themselves be near x. An image-based definition would fail for constant functions, which are continuous in every reasonable sense but send all open sets to single (non-open) points. The image direction defines 'open maps,' a genuinely different property."
  explanation: "The arrow reversal reflects the asymmetry of continuity: you specify an output tolerance and ask how tightly the input must be controlled. That is the preimage direction."
```

## Explainer

You learned continuity in calculus through the epsilon-delta definition: f is continuous at x₀ if for every ε > 0 there exists δ > 0 such that |x − x₀| < δ implies |f(x) − f(x₀)| < ε. This definition is intuitive and practical, but it is built around the idea of distance — the absolute values measure how far two points are from each other. Topology's goal is to study properties that don't depend on distance at all, only on which sets are "open." To work in that more general setting, you need a definition of continuity that uses only open sets.

The key insight is that the epsilon-delta condition can be rephrased entirely in terms of open sets: f is continuous at x₀ if and only if for every open set V containing f(x₀), the **preimage** f⁻¹(V) = {x ∈ X : f(x) ∈ V} is an open set containing x₀. Asking for "every such open V" to have an open preimage is exactly what the global definition says: f is continuous if and only if f⁻¹(V) is open in X whenever V is open in Y. Notice that the arrow is backward — you pull sets back through f, not forward. The image f(U) of an open set need not be open (think of f(x) = constant, where every open set maps to a single point), but the preimage of an open set must be open.

Why does this matter? Because the preimage definition works in any topological space, even ones where there is no meaningful notion of distance. A function between two abstract topological spaces — say, two different spaces of functions, or a space built from combinatorial data — can be declared continuous using only the topology (the collection of open sets) on each space. This unifies the continuity you know from real analysis, the continuity of paths in topology, the continuity of group homomorphisms in algebra, and the continuity of probability measures — all instances of the same definition.

The preimage characterization also has a useful equivalent in terms of **neighborhoods**: f is continuous at x if and only if for every neighborhood N of f(x), f⁻¹(N) is a neighborhood of x. This version is closer in spirit to the epsilon-delta definition and is often easier to work with in concrete cases. You can also rephrase everything in terms of closed sets: f is continuous if and only if the preimage of every closed set is closed, since preimages commute with complements and complements of open sets are closed. All three characterizations — open sets, closed sets, neighborhoods — say the same thing in different languages, and knowing all three makes it easier to choose the right one for any particular proof.
