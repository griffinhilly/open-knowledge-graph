---
id: normality-t4-axiom
title: Normality and T₄ Spaces
domain: mathematics
course: topology
prerequisites:
- id: regularity-t3-axiom
  type: hard
builds-toward:
- urysohn-metrization-theorem
tags:
- normality
- t4-axiom
stage: abstract-reasoning
status: draft
---

# Normality and T₄ Spaces

## Core Idea
A space is normal if for every two disjoint closed sets, there exist disjoint open sets separating them. T₄ = normal + T₁. Normal spaces have strong separation: any continuous function on a closed set extends to the whole space (Tietze extension). Compact Hausdorff spaces and metric spaces are normal.

## Explainer

Recall from your study of T₃ (regularity) that a regular space can separate any closed set from any point outside it by disjoint open sets. **Normality** (the T₄ axiom) upgrades this: instead of separating a point from a closed set, you must be able to separate two entire closed sets from each other. Given disjoint closed sets F₁ and F₂, normality guarantees open sets U₁ ⊇ F₁ and U₂ ⊇ F₂ with U₁ ∩ U₂ = ∅. This is a strictly stronger requirement: separating two extended, potentially complex closed sets is harder than just separating a point from a set.

The canonical examples of normal spaces are metric spaces and compact Hausdorff spaces. In a metric space, you can construct the separating open sets explicitly: for disjoint closed F₁ and F₂, let Uᵢ = {x : d(x, Fᵢ) < d(x, Fⱼ)/2}. These sets are open, contain their respective closed sets, and are disjoint (if a point were in both, it would be closer to each F than to the other, a contradiction). Compact Hausdorff spaces are normal by a different route: compactness lets you take finite subcovers of the open covers that Hausdorff separation gives for each point.

The most important consequence of normality is **Urysohn's lemma**: if F₁ and F₂ are disjoint closed sets in a normal space, then there exists a continuous function f : X → [0,1] with f|F₁ = 0 and f|F₂ = 1. This is striking — normality, which is a purely topological condition about open sets, produces actual continuous functions. The construction runs through a careful argument: build open sets U_r for each rational r ∈ [0,1] with F₁ ⊂ U_r and cl(U_r) ⊂ U_s whenever r < s and cl(U_s) avoids F₂. Then define f(x) = inf{r : x ∈ U_r}. The density of rationals and the nesting of the sets combines to force continuity.

Building directly on Urysohn's lemma is the **Tietze extension theorem**: any continuous function defined on a closed subspace F of a normal space X extends to a continuous function on all of X. This is an enormously useful tool in analysis and topology. It says that normal spaces have no "obstructions" to extending continuous functions — the geometry is rich enough to always find an extension. The proof constructs the extension iteratively, using Urysohn functions to approximate the original function with ever-smaller error on the remaining domain.

Normality thus sits at the heart of the relationship between topology and analysis. It is the minimum condition under which you can reliably produce continuous functions with prescribed values on specified closed sets. This is why normality appears as a hypothesis in so many extension and separation theorems: without it, the topological structure may be too thin to support the continuous functions that analysis requires. A T₄ space is one where not only points and closed sets can be separated from each other (T₃), but where closed sets can be separated from closed sets — a much richer geometric property that unlocks the full machinery of Urysohn and Tietze.
