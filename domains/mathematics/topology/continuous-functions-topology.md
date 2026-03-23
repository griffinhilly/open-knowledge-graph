---
id: continuous-functions-topology
title: Continuous Functions in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- homeomorphisms-topological-equivalence
- quotient-topology
tags:
- continuity
- fundamental
stage: formal-systems
status: validated
---

# Continuous Functions in Topological Spaces

## Core Idea
A function f: X → Y is continuous if for every open set V in Y, the preimage f⁻¹(V) is open in X. This generalizes ε-δ continuity and works in any topological context.

## Questions

```yaml
- question: "A student claims that if f: X → Y is continuous, then the image of every open set in X must be open in Y. Which example directly refutes this claim?"
  type: multiple-choice
  options:
    - "The identity function f(x) = x on ℝ, since it maps closed sets to closed sets"
    - "The constant function f(x) = 0 on ℝ, since it maps every open set to the single point {0}, which is not open"
    - "The squaring function f(x) = x² on ℝ, since it maps (−1, 1) to [0, 1), which is neither open nor closed"
    - "Any discontinuous function, since discontinuous functions violate all open-set conditions"
  answer: 1
  explanation: "The constant function f(x) = 0 is continuous (preimage of any open set V containing 0 is all of ℝ; preimage of any open set not containing 0 is ∅ — both open), yet it maps every open set in ℝ to the single-point set {0}, which is closed, not open. This shows that continuous functions need not send open sets to open sets. The topological definition of continuity is one-directional on purpose. Functions that do map open sets to open sets are called 'open maps' and satisfy a strictly stronger condition than continuity."

- question: "Why does the topological definition of continuity use preimages of open sets rather than images?"
  type: multiple-choice
  options:
    - "Because preimages are easier to compute than images in abstract spaces"
    - "Because continuous functions preserve open-set structure when pulling back from codomain to domain, but need not do so in the forward direction"
    - "Because the definition was chosen arbitrarily and either direction would work equally well"
    - "Because images only work for bijective functions, while preimages work for all functions"
  answer: 1
  explanation: "The choice is not arbitrary — it reflects the actual structure of continuous functions. Continuous functions preserve open-set structure when you pull back along f (preimage direction), but not when you push forward (image direction). The constant function counterexample makes this vivid: it is continuous by the preimage definition yet maps open sets to non-open sets. The preimage definition correctly captures what it means for f to 'respect' the topology on the codomain: if V is declared open in Y, then f must present an open region in X that maps into V."

- question: "A continuous function f: X → Y always maps open sets in X to open sets in Y."
  type: true-false
  answer: false
  explanation: "False. This is the most common confusion about topological continuity. The correct statement is the reverse: f is continuous if and only if the *preimage* of every open set in Y is open in X. The constant function f(x) = 0 from ℝ to ℝ is continuous but maps every open interval to the single point {0}, which is not open. Functions that map open sets to open sets are called 'open maps' — a strictly stronger and entirely separate condition from continuity."

- question: "When X = Y = ℝ with the standard metric topology, the topological definition of continuity (preimages of open sets are open) is equivalent to the ε-δ definition of continuity."
  type: true-false
  answer: true
  explanation: "True. The ε-δ condition says: for every ε > 0 and every x, there exists δ > 0 such that B(x, δ) maps into B(f(x), ε). In other words, every open ball around f(x) has an open ball around x that maps into it — meaning the preimage of any open interval around f(x) contains an open neighborhood of x, which means the preimage of any open set contains an open neighborhood of each of its points, which means the preimage is open. The two definitions coincide exactly on metric spaces with their standard topology."

- question: "Explain why the topological definition of continuity uses preimages rather than images of open sets, and give a concrete example illustrating the necessity."
  type: short-answer
  answer: "Continuity means the function respects open-set structure when pulling back from the codomain to the domain: if V is open in Y, then f⁻¹(V) must be open in X. The reverse direction fails in general: continuous functions can collapse open sets to single points. The constant function f(x) = 0 maps every open set to {0}, which is not open, yet f is continuous by the preimage definition. Functions that do preserve open sets in the forward direction are called open maps — a strictly stronger property."
  explanation: "The asymmetry is a genuine feature of continuous functions. Continuity is about the function not 'tearing' open structure when approached from the output side: for any open neighborhood of a target point, there must be an open neighborhood of every source point mapping into it. This is precisely what preimages capture. The preimage definition also unlocks structural tools — the initial topology and quotient topology are both defined via this same condition — making it not just a generalization of ε-δ continuity but the right structural concept for all of topology."
```

## Explainer

Your prerequisite, open sets in topology, defined what it means for a collection of subsets to constitute a topology: the whole space and the empty set are open, arbitrary unions of open sets are open, and finite intersections of open sets are open. Now, with two topological spaces X and Y, you need a notion of "continuous function" that captures the same idea as ε-δ continuity but without distances. The topological definition does this elegantly: **f: X → Y is continuous if for every open set V ⊆ Y, the preimage f⁻¹(V) = {x ∈ X : f(x) ∈ V} is open in X**.

To see why this generalizes ε-δ, consider X = Y = ℝ with the standard (metric) topology. An open set in ℝ is a union of open intervals. The ε-δ condition says: for every ε > 0 and every x, there exists δ > 0 such that |x − y| < δ implies |f(x) − f(y)| < ε. In other words, every open ball around f(x) (the set (f(x)−ε, f(x)+ε)) has an open ball around x mapping into it — which is exactly saying that the preimage of any open interval around f(x) contains an open interval around x, which is exactly saying that preimages of open sets are open. The two definitions coincide on ℝ.

The preimage definition is asymmetric in a way that demands explanation: why preimages, not images? The answer is that **continuous functions need not send open sets to open sets**. The constant function f(x) = 0 sends every open set to the single point {0}, which is not open in ℝ. Functions that do map open sets to open sets — called **open maps** — are a separate, strictly stronger condition. The topological definition of continuity is correctly one-directional: open sets pull back to open sets.

Thinking in terms of preimages reframes what continuity means: a function is continuous when the topology on the *domain* is at least as fine as the topology induced by the *codomain* via f. If V is "declared open" in Y, then f⁻¹(V) must be "declared open" in X — the topology on X must respect what f sees as open structure in Y. This perspective makes it easy to compare topologies (the coarser the topology on Y, the easier continuity is to achieve) and to define new topologies from functions (the **initial topology** and **quotient topology** are both defined via this preimage condition). The definition you have here is not just a generalization of ε-δ; it is the right structural concept that makes the rest of topology work.
