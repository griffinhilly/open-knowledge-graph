---
id: locally-connected-spaces
title: Locally Connected Spaces
domain: mathematics
course: topology
prerequisites:
- id: connected-spaces-definition
  type: hard
- id: neighborhoods-topology-definition
  type: soft
tags:
- locally-connected
- local-property
stage: formal-systems
status: draft
---

# Locally Connected Spaces

## Core Idea
A space is locally connected if every point has a neighborhood basis of connected sets. Local connectedness is a local property (each point looks connected nearby). In locally connected spaces, connected components are open. Connected + locally connected implies path-connected. Locally connected spaces have nicer properties for algebraic topology (universal covers exist).

## Questions

```yaml
- question: "Which of the following is connected but NOT locally connected?"
  type: multiple-choice
  options:
    - "The real line ℝ with the standard topology"
    - "The topologist's sine curve (the closure of {(x, sin(1/x)) : x > 0})"
    - "A disjoint union of two open intervals (0,1) ∪ (2,3)"
    - "A circle S¹"
  answer: 1
  explanation: "The topologist's sine curve is connected — you cannot split it into two disjoint nonempty open sets — but it fails local connectedness near the origin. Every small neighborhood of the origin contains infinitely many disconnected arcs of the oscillating sine wave, so no connected open neighborhood of the origin exists. The real line ℝ and the circle S¹ are both connected AND locally connected. The disjoint union (0,1) ∪ (2,3) is locally connected but globally disconnected — the opposite failure."

- question: "In a locally connected topological space, what can be said about the connected components?"
  type: multiple-choice
  options:
    - "They are always closed but not necessarily open"
    - "They are always open sets"
    - "They are always finite in number"
    - "They are always both open and closed only if the space is compact"
  answer: 1
  explanation: "Local connectedness implies that connected components are open. At any point x in a component C, local connectedness provides a connected open neighborhood U of x. Since U is connected and intersects C, U must be entirely contained in C. So every point of C has an open neighborhood inside C, making C open. In an arbitrary topological space, components are closed but not necessarily open — the rationals ℚ, for instance, have components that are single points, which are not open. Local connectedness is exactly the extra condition that forces components to be open."

- question: "Every connected topological space is also locally connected."
  type: true-false
  answer: false
  explanation: "The topologist's sine curve is the canonical counterexample: it is connected (the global space cannot be separated into two disjoint open sets) but not locally connected (near the origin, no small connected open neighborhood exists). Connectedness is a global property — it depends on the whole space. Local connectedness is a local property — it must hold at every point in small neighborhoods. A space can satisfy one without the other."

- question: "A locally connected space can have more than one connected component."
  type: true-false
  answer: true
  explanation: "Local connectedness and global connectedness are independent properties. The disjoint union (0,1) ∪ (2,3) is locally connected — every point has an obvious connected open neighborhood within its interval — but has exactly two connected components. Local connectedness says each point looks connected nearby; it says nothing about whether the whole space is connected. In locally connected spaces, those multiple components will each be open sets."

- question: "What is the key structural consequence of a space being locally connected, and why does this consequence fail for arbitrary topological spaces?"
  type: short-answer
  answer: "In a locally connected space, connected components are open sets. This holds because local connectedness provides a connected open neighborhood at every point, forcing each component to be open. In an arbitrary topological space, components are always closed but can fail to be open — in ℚ for example, components are single points, which are not open in the standard topology."
  explanation: "The openness of components is what makes locally connected spaces well-behaved for algebraic topology. It ensures clean partitions of the space, that path-lifting arguments work, and that universal covers exist. The failure in ℚ illustrates why: components so small they contain no open sets make local-to-global arguments impossible. Local connectedness is thus precisely the condition needed to prevent this pathological behavior."
```

## Explainer

From your study of connected spaces, you know that a space is connected when it cannot be split into two disjoint nonempty open pieces. That's a **global** property — it depends on the shape of the entire space at once. **Local connectedness** is a weaker, **local** version: the space looks connected in a small neighborhood around every point, even if the whole space might fall apart globally.

Formally, X is locally connected at a point x if every open neighborhood of x contains a smaller open connected neighborhood of x. The whole space is locally connected if this holds at every point. Think of it this way: if you zoom in close enough around any point, what you see should be connected. Contrast this with connectedness: a connected space might fail to be locally connected, and a locally connected space might fail to be globally connected.

The canonical example separating the two concepts is the **topologist's sine curve**: the closure of the graph of sin(1/x) for x > 0. This space is connected — you cannot split it into two open disjoint pieces — but it is not locally connected. Near the origin, every small neighborhood contains infinitely many disconnected arcs of the sine wave oscillating faster and faster; no small connected neighborhood of the origin exists. On the other hand, the disjoint union of two open intervals (0,1) ∪ (2,3) is locally connected (every point has an obvious small connected neighborhood within its interval) but globally disconnected.

The key structural payoff of local connectedness is that **connected components become open sets**. In an arbitrary topological space, connected components are always closed but not necessarily open — they can be dense, complicated, or nowhere open (as in the rationals ℚ). But when the space is locally connected, each component is an open neighborhood of each of its points, making the components a clean partition of the space into open connected pieces. This openness of components is what makes locally connected spaces well-behaved for algebraic topology: it ensures that universal covers exist, that path-lifting is manageable, and that the local-to-global arguments that power covering space theory go through smoothly.
