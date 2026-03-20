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

## Explainer

From your study of connected spaces, you know that a space is connected when it cannot be split into two disjoint nonempty open pieces. That's a **global** property — it depends on the shape of the entire space at once. **Local connectedness** is a weaker, **local** version: the space looks connected in a small neighborhood around every point, even if the whole space might fall apart globally.

Formally, X is locally connected at a point x if every open neighborhood of x contains a smaller open connected neighborhood of x. The whole space is locally connected if this holds at every point. Think of it this way: if you zoom in close enough around any point, what you see should be connected. Contrast this with connectedness: a connected space might fail to be locally connected, and a locally connected space might fail to be globally connected.

The canonical example separating the two concepts is the **topologist's sine curve**: the closure of the graph of sin(1/x) for x > 0. This space is connected — you cannot split it into two open disjoint pieces — but it is not locally connected. Near the origin, every small neighborhood contains infinitely many disconnected arcs of the sine wave oscillating faster and faster; no small connected neighborhood of the origin exists. On the other hand, the disjoint union of two open intervals (0,1) ∪ (2,3) is locally connected (every point has an obvious small connected neighborhood within its interval) but globally disconnected.

The key structural payoff of local connectedness is that **connected components become open sets**. In an arbitrary topological space, connected components are always closed but not necessarily open — they can be dense, complicated, or nowhere open (as in the rationals ℚ). But when the space is locally connected, each component is an open neighborhood of each of its points, making the components a clean partition of the space into open connected pieces. This openness of components is what makes locally connected spaces well-behaved for algebraic topology: it ensures that universal covers exist, that path-lifting is manageable, and that the local-to-global arguments that power covering space theory go through smoothly.
