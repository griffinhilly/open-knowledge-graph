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
builds-toward:
- homeomorphisms-topological-equivalence
- topological-invariants
tags:
- continuity
- continuous-functions
- preimages
stage: advanced
status: draft
---

# Continuity in Topological Spaces

## Core Idea
A function f: X → Y between topological spaces is continuous if the preimage of every open set is open (equivalently, preimages of closed sets are closed, or preimages of neighborhoods are neighborhoods). This topological definition removes reliance on distance and applies to any pair of topological spaces, unifying continuity across algebra, analysis, and geometry.

## Explainer

You learned continuity in calculus through the epsilon-delta definition: f is continuous at x₀ if for every ε > 0 there exists δ > 0 such that |x − x₀| < δ implies |f(x) − f(x₀)| < ε. This definition is intuitive and practical, but it is built around the idea of distance — the absolute values measure how far two points are from each other. Topology's goal is to study properties that don't depend on distance at all, only on which sets are "open." To work in that more general setting, you need a definition of continuity that uses only open sets.

The key insight is that the epsilon-delta condition can be rephrased entirely in terms of open sets: f is continuous at x₀ if and only if for every open set V containing f(x₀), the **preimage** f⁻¹(V) = {x ∈ X : f(x) ∈ V} is an open set containing x₀. Asking for "every such open V" to have an open preimage is exactly what the global definition says: f is continuous if and only if f⁻¹(V) is open in X whenever V is open in Y. Notice that the arrow is backward — you pull sets back through f, not forward. The image f(U) of an open set need not be open (think of f(x) = constant, where every open set maps to a single point), but the preimage of an open set must be open.

Why does this matter? Because the preimage definition works in any topological space, even ones where there is no meaningful notion of distance. A function between two abstract topological spaces — say, two different spaces of functions, or a space built from combinatorial data — can be declared continuous using only the topology (the collection of open sets) on each space. This unifies the continuity you know from real analysis, the continuity of paths in topology, the continuity of group homomorphisms in algebra, and the continuity of probability measures — all instances of the same definition.

The preimage characterization also has a useful equivalent in terms of **neighborhoods**: f is continuous at x if and only if for every neighborhood N of f(x), f⁻¹(N) is a neighborhood of x. This version is closer in spirit to the epsilon-delta definition and is often easier to work with in concrete cases. You can also rephrase everything in terms of closed sets: f is continuous if and only if the preimage of every closed set is closed, since preimages commute with complements and complements of open sets are closed. All three characterizations — open sets, closed sets, neighborhoods — say the same thing in different languages, and knowing all three makes it easier to choose the right one for any particular proof.
