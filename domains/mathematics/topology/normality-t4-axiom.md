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
stage: advanced
status: validated
---

# Normality and T₄ Spaces

## Core Idea
A space is normal if for every two disjoint closed sets, there exist disjoint open sets separating them. T₄ = normal + T₁. Normal spaces have strong separation: any continuous function on a closed set extends to the whole space (Tietze extension). Compact Hausdorff spaces and metric spaces are normal.

## Questions

```yaml
- question: "A topologist wants to construct a continuous function f: X → [0,1] that equals 0 on one closed set F₁ and 1 on a disjoint closed set F₂. What is the minimum topological property X must have?"
  type: multiple-choice
  options:
    - "Hausdorff (T₂): any two distinct points can be separated by open sets"
    - "Regularity (T₃): any point and disjoint closed set can be separated by open sets"
    - "Normality (T₄): any two disjoint closed sets can be separated by open sets"
    - "Compactness: every open cover has a finite subcover"
  answer: 2
  explanation: "Urysohn's lemma states precisely this: in a normal space, disjoint closed sets can be separated by a continuous function. Regularity only separates a point from a closed set, which is insufficient. Normality is both necessary and sufficient for Urysohn's lemma."

- question: "In the metric-space proof that all metric spaces are normal, what are the separating open sets constructed for disjoint closed sets F₁ and F₂?"
  type: multiple-choice
  options:
    - "Open balls of radius 1 centered at each point of Fᵢ"
    - "Uᵢ = {x : d(x, Fᵢ) < d(x, Fⱼ)} for i ≠ j"
    - "The complements X \\ Fᵢ, which are open since Fᵢ are closed"
    - "Sets constructed inductively using Zorn's lemma"
  answer: 1
  explanation: "The sets Uᵢ = {x : d(x, Fᵢ) < d(x, Fⱼ)} work: each contains its Fᵢ (since d(x, Fᵢ) = 0 < d(x, Fⱼ) for x ∈ Fᵢ when the sets are disjoint closed), they are open (the distance function is continuous), and they are disjoint (a point can't be closer to each set than to the other simultaneously)."

- question: "In a normal space, any continuous function defined on a closed subspace can be extended to a continuous function on the entire space."
  type: true-false
  answer: true
  explanation: "This is the Tietze extension theorem, which follows directly from normality via Urysohn's lemma. The proof iteratively constructs extensions with geometrically shrinking error. This is one of the primary reasons normality matters in analysis."

- question: "Every regular (T₃) space is also normal (T₄), because if you can separate a point from a closed set, you can separate two closed sets from each other."
  type: true-false
  answer: false
  explanation: "Regularity does not imply normality. Separating a point from a closed set is easier than separating two arbitrary closed sets. There exist regular spaces that are not normal (e.g., the Sorgenfrey plane). The implication goes the other way: compact Hausdorff spaces are normal, but compact Hausdorff implies more than T₃."

- question: "Why is normality the key hypothesis in Urysohn's lemma, and what does the lemma produce that makes normality so valuable for analysis?"
  type: short-answer
  answer: "Normality guarantees that two disjoint closed sets can be surrounded by disjoint open sets, which lets you build a nested family of open sets U_r indexed by rationals in [0,1] with F₁ ⊂ U_r and cl(U_r) ⊂ U_s for r < s. Defining f(x) = inf{r : x ∈ U_r} gives a continuous function separating F₁ and F₂. The lemma produces a continuous real-valued function with prescribed values on closed sets — bridging purely topological separation to the analytic tools of continuous functions."
  explanation: "Without normality you cannot build the required nesting of open sets, so the construction breaks down. The value of the lemma is that it converts a topological condition (open-set separation) into an analytic object (a continuous function), which then enables the Tietze extension theorem and makes normal spaces behave well in functional analysis."
```

## Explainer

Recall from your study of T₃ (regularity) that a regular space can separate any closed set from any point outside it by disjoint open sets. **Normality** (the T₄ axiom) upgrades this: instead of separating a point from a closed set, you must be able to separate two entire closed sets from each other. Given disjoint closed sets F₁ and F₂, normality guarantees open sets U₁ ⊇ F₁ and U₂ ⊇ F₂ with U₁ ∩ U₂ = ∅. This is a strictly stronger requirement: separating two extended, potentially complex closed sets is harder than just separating a point from a set.

The canonical examples of normal spaces are metric spaces and compact Hausdorff spaces. In a metric space, you can construct the separating open sets explicitly: for disjoint closed F₁ and F₂, let Uᵢ = {x : d(x, Fᵢ) < d(x, Fⱼ)/2}. These sets are open, contain their respective closed sets, and are disjoint (if a point were in both, it would be closer to each F than to the other, a contradiction). Compact Hausdorff spaces are normal by a different route: compactness lets you take finite subcovers of the open covers that Hausdorff separation gives for each point.

The most important consequence of normality is **Urysohn's lemma**: if F₁ and F₂ are disjoint closed sets in a normal space, then there exists a continuous function f : X → [0,1] with f|F₁ = 0 and f|F₂ = 1. This is striking — normality, which is a purely topological condition about open sets, produces actual continuous functions. The construction runs through a careful argument: build open sets U_r for each rational r ∈ [0,1] with F₁ ⊂ U_r and cl(U_r) ⊂ U_s whenever r < s and cl(U_s) avoids F₂. Then define f(x) = inf{r : x ∈ U_r}. The density of rationals and the nesting of the sets combines to force continuity.

Building directly on Urysohn's lemma is the **Tietze extension theorem**: any continuous function defined on a closed subspace F of a normal space X extends to a continuous function on all of X. This is an enormously useful tool in analysis and topology. It says that normal spaces have no "obstructions" to extending continuous functions — the geometry is rich enough to always find an extension. The proof constructs the extension iteratively, using Urysohn functions to approximate the original function with ever-smaller error on the remaining domain.

Normality thus sits at the heart of the relationship between topology and analysis. It is the minimum condition under which you can reliably produce continuous functions with prescribed values on specified closed sets. This is why normality appears as a hypothesis in so many extension and separation theorems: without it, the topological structure may be too thin to support the continuous functions that analysis requires. A T₄ space is one where not only points and closed sets can be separated from each other (T₃), but where closed sets can be separated from closed sets — a much richer geometric property that unlocks the full machinery of Urysohn and Tietze.
