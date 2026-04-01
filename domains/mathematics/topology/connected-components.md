---
id: connected-components
title: Connected Components
domain: mathematics
course: topology
prerequisites:
- id: connectedness-definition-examples
  type: hard
builds-toward:
- fundamental-group-definition
tags:
- components
- equivalence-classes
- decomposition
stage: advanced
status: validated
---

# Connected Components

## Core Idea
The connected component of a point x is the largest connected subset containing x—formally, the union of all connected subsets that contain x. Connected components partition any topological space into maximal connected pieces, and they are always closed sets. This decomposition reveals the global structure of a space: a space is connected if and only if it has exactly one component. In totally disconnected spaces like the Cantor set, every component is a single point. The number and nature of connected components provide a coarse but powerful topological invariant.

## How It's Best Learned
Draw examples: identify the components of the real line minus a few points, then of a union of disjoint circles. Move to the topologist's sine curve to see that components can be connected but not path-connected, sharpening the distinction.

## Common Misconceptions
Students often assume connected components must be open—they are always closed but not necessarily open. Also, path-components and connected components can differ; path-connectedness is strictly stronger than connectedness.

## Explainer

Given a topological space X, the **connected component** of a point x is the largest connected subset of X that contains x. Formally, it is the union of all connected subsets of X that contain x. Since any union of connected sets sharing a common point is connected, this union is itself connected and is maximal: no strictly larger connected subset of X contains x. Every point of X belongs to exactly one connected component, and distinct connected components are disjoint, so the connected components **partition** X into maximal connected pieces.

Connected components are always **closed** sets. To see why: the closure of a connected set is connected, so if C is the connected component of x, then the closure cl(C) is a connected set containing x. By maximality of C, we must have cl(C) ⊆ C, which means C = cl(C) — the component is closed. However, connected components are not necessarily open. In the rational numbers ℚ with the subspace topology from ℝ, every connected component is a single point (since between any two rationals lies an irrational, allowing a disconnection). These singletons are closed but not open in ℚ. Components are guaranteed to be open only when the space is **locally connected** — a separate condition beyond basic connectedness.

The component decomposition reveals the global structure of a space at a coarse level. A space is connected if and only if it has exactly one component. The real line minus two points, ℝ \ {0, 1}, has three components: (−∞, 0), (0, 1), and (1, ∞). At the other extreme, a **totally disconnected** space like the Cantor set has every component equal to a single point — the space is maximally fragmented. The number and nature of connected components form a topological invariant: homeomorphic spaces have the same component structure.

It is important to distinguish connected components from **path-components**. The path-component of x is the set of all points that can be joined to x by a continuous path. Every path-component is contained in a connected component, and in most familiar spaces (manifolds, CW complexes, locally path-connected spaces) the two notions coincide. But they can diverge: the topologist's sine curve — the closure of the graph of sin(1/x) for x > 0 — is connected (one connected component) but has two path-components, because no continuous path can cross the infinitely oscillating accumulation at the y-axis. This distinction matters in algebraic topology, where path-connectedness rather than connectedness is typically the relevant condition.

## Questions

```yaml
- question: "Consider the topologist's sine curve: the closure of the graph of sin(1/x) for x > 0, which includes the segment {0} × [−1, 1]. How many connected components does this space have?"
  type: multiple-choice
  options:
    - "2 — the graph portion and the vertical segment are separate components"
    - "1 — the entire set is a single connected component"
    - "Infinitely many — each oscillation of the sine curve is its own component"
    - "0 — it has no components since it is not path-connected"
  answer: 1
  explanation: "The topologist's sine curve is connected — the closure of any connected set is connected, and the graph {(x, sin(1/x)) : x > 0} is the continuous image of a connected set. Therefore the entire space is one connected component. The classic confusion (option A) is mistaking 'not path-connected' for 'not connected.' The space cannot be joined by a path across the accumulation segment, but it is still topologically connected — it cannot be split into two disjoint open sets. Path-connectedness is strictly stronger than connectedness."

- question: "The space X = ℝ \\ {0, 1} (the real line with two points removed). What are its connected components?"
  type: multiple-choice
  options:
    - "Two components: (−∞, 0) ∪ (0, 1) and (1, ∞)"
    - "Three components: (−∞, 0), (0, 1), and (1, ∞)"
    - "One component, since ℝ is connected and removal of finitely many points doesn't disconnect it"
    - "Infinitely many, since every rational is a boundary point"
  answer: 1
  explanation: "Removing 0 and 1 from ℝ creates three maximal connected pieces: (−∞, 0), (0, 1), and (1, ∞). Each open interval is connected and cannot be merged with another without crossing a removed point. Option A is wrong because (−∞, 0) and (0, 1) are separated by the missing point 0 — they cannot be joined in X. Option C is wrong: removing even a single point from ℝ disconnects it (ℝ \\ {0} has two components)."

- question: "Connected components of a topological space are generally open sets."
  type: true-false
  answer: false
  explanation: "Connected components are always closed — the closure of a connected set is connected, so the closure of a component is still connected and contained in the component by maximality, meaning the component equals its own closure. However, components are not necessarily open. In the rational numbers ℚ with the subspace topology, every component is a single point — closed but not open. Components are open only when the space is locally connected, which is an additional assumption not required by the definition."

- question: "If two points in a topological space cannot be connected by a continuous path, they should lie in different connected components."
  type: true-false
  answer: false
  explanation: "The topologist's sine curve is the canonical counterexample. The point (0, 0) on the vertical accumulation segment and any point on the sine graph cannot be connected by a path — the curve oscillates infinitely fast near the y-axis, preventing a continuous path from crossing. Yet the entire space is connected, so all points lie in the same connected component. Path-connectedness implies connectedness, but not conversely; failing to be path-connected does not imply lying in different connected components."

- question: "Why is the connected component of a point defined as the union of all connected subsets containing that point, rather than by requiring a path between points?"
  type: short-answer
  answer: "Paths are not always available — a space can be connected (one component) even when no path joins certain point pairs. Defining components via paths yields path-components, which can be strictly finer than connected components. The definition via 'union of all connected subsets' is purely topological and does not require any notion of a continuous curve through the space."
  explanation: "The subtlety matters in spaces like the topologist's sine curve, where path-components and connected components diverge. In locally path-connected spaces (most familiar geometric objects), the two notions coincide. But in general topology — and especially in algebraic topology, where one studies spaces with exotic local behavior — the distinction is essential. The connected component is the maximal connected subset; the path-component is the maximal path-connected subset. The former is always closed; the latter need not be."
```

