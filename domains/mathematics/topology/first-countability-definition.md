---
id: first-countability-definition
title: First Countability and Bases
domain: mathematics
course: topology
prerequisites:
- id: neighborhoods-topology-definition
  type: hard
builds-toward:
- second-countable-spaces
tags:
- first-countability
- countability
stage: formal-systems
status: draft
---

# First Countability and Bases

## Core Idea
A space is first-countable if every point has a countable neighborhood base. Metric spaces are first-countable. In first-countable spaces, sequential properties determine topology: f is continuous iff it preserves sequential limits. First-countability is weaker than second-countability but sufficient for many purposes.

## Explainer

From your study of neighborhoods in topology, you know that a **neighborhood base** at a point x is a collection of neighborhoods of x such that every neighborhood of x contains some member of the collection. Think of a neighborhood base as a set of "probes" of decreasing size around x — if you can detect everything about the local topology of x using just those probes, the base captures the full local picture. **First-countability** imposes one requirement: this base can be chosen to be countable.

In a metric space, the canonical example is the collection of open balls B(x, 1/n) for n = 1, 2, 3, …. These form a countable neighborhood base at x because every open set containing x contains some B(x, 1/n). This is why all metric spaces are first-countable. The intuition is that in a metric space, shrinking balls of radii 1, 1/2, 1/3, … give you enough resolution to detect all local structure — you never need uncountably many probes.

The power of first-countability is that it lets sequences do all the work of general nets or filters. In an arbitrary topological space, sequential convergence may not detect the full topology: a function can be "sequentially continuous" (preserves limits of sequences) without being truly continuous. But in a first-countable space, these notions coincide — a function is continuous if and only if it sends convergent sequences to convergent sequences. Similarly, a point is in the closure of a set A if and only if it is the limit of a sequence in A. This makes first-countable spaces feel much more like metric spaces, even when no actual metric is present.

The standard example of a space that fails first-countability is the **uncountable product** ℝᴵ where I is uncountable. At any point x, every basic open set is determined by restrictions on finitely many coordinates. To form a neighborhood base at x, you would need to accommodate all possible finite coordinate constraints — but since there are uncountably many coordinates, no countable collection of neighborhoods can serve as a base. In such spaces, sequences are genuinely insufficient: you must work with nets or filters to correctly describe continuity and closure.

**First-countability** sits between the general topological setting and the full strength of second-countability (which requires a countable base for the entire topology, not just at each point). It is the minimal condition that lets you use "sequence-based intuition" from calculus and metric space analysis in a purely topological setting. Whenever a theorem says "in a first-countable space, we can use sequences to characterize…," it is invoking the guarantee that countable probes at each point suffice to detect the local topology.
