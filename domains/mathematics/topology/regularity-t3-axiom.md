---
id: regularity-t3-axiom
title: Regularity and T₃ Spaces
domain: mathematics
course: topology
prerequisites:
- id: separation-axioms-t0-t1-t2
  type: hard
- id: regular-spaces
  type: soft
builds-toward:
- normality-t4-axiom
tags:
- regularity
- t3-axiom
stage: advanced
status: validated
---

# Regularity and T₃ Spaces

## Core Idea
A space is regular if for every closed set F and x ∉ F, there exist disjoint open sets separating them. T₃ = regular + T₀. Regular spaces separate points from closed sets; metric spaces are regular. Products of regular spaces are regular; regularity is preserved under continuous images (unlike T₂).

## Explainer

A topological space X is **regular** if, given any closed set F and any point x not in F, there exist disjoint open sets U and V with x ∈ U and F ⊆ V. In other words, a point and a closed set that does not contain it can always be "separated" by open neighborhoods that do not overlap. The **T₃ axiom** combines regularity with the T₀ condition (topological distinguishability of points), yielding a space where both point-from-point and point-from-closed-set separation are guaranteed. Some authors define T₃ as regular + T₁ instead; in either convention, the substantive content is the regularity condition itself.

Regularity sits one level above the Hausdorff condition in the separation hierarchy. The Hausdorff axiom (T₂) requires separating two points by disjoint open sets; regularity requires separating a single point from an entire closed set. This is a strictly stronger demand: a closed set can be infinite and its points can cluster near x, making the construction of disjoint open neighborhoods harder. Every regular T₁ space is Hausdorff — since singletons are closed in a T₁ space, regularity applied to x and the closed set {y} gives the T₂ separation. But T₂ does not imply regularity: there exist Hausdorff spaces where a point and a disjoint closed set cannot be separated by open sets, though such spaces are somewhat pathological.

Metric spaces are always regular, and the proof is constructive. If F is closed and x ∉ F, then d(x, F) = inf{d(x, y) : y ∈ F} > 0 (since F is closed and x is outside it). Setting r = d(x, F)/2, the open ball B(x, r) and the open set ∪{B(y, r) : y ∈ F} separate x from F: any point in both would be within r of x and within r of some point of F, giving d(x, y) < 2r = d(x, F), a contradiction. This argument illustrates a recurring theme: in metric spaces, the distance function provides explicit constructions for topological separation, which is why metric spaces satisfy all the standard separation axioms.

Regularity is preserved under several important constructions. Products of regular spaces are regular (in the product topology), and subspaces of regular spaces are regular. This makes regularity a robust property that persists as you build new spaces from existing ones. Regularity is the gateway to the stronger separation axiom of **normality** (T₄), which requires separating two disjoint closed sets from each other — a strictly harder task. The hierarchy T₂ ⊂ T₃ ⊂ T₄ represents progressively stronger geometric richness, with each level unlocking new theorems about the existence of continuous functions and extensions.

## Questions

```yaml
- question: "A topological space X is called regular if:"
  type: multiple-choice
  options:
    - "Any two distinct points can be separated by disjoint open sets"
    - "Any point and any closed set not containing it can be separated by disjoint open sets"
    - "Any two disjoint closed sets can be separated by disjoint open sets"
    - "Every open cover of X has a finite subcover"
  answer: 1
  explanation: "Regularity separates a point from a closed set. Option A is the Hausdorff (T₂) axiom — separating two points. Option C is normality (T₄) — separating two closed sets. Option D is compactness. The hierarchy T₂ < T₃ < T₄ represents successively stronger separation requirements: from two points, to a point and a closed set, to two closed sets."

- question: "A topological space X is Hausdorff (T₂) but fails to be regular. Which configuration would witness this failure?"
  type: multiple-choice
  options:
    - "Two distinct points that cannot be separated by open sets"
    - "A point x and a closed set F with x ∉ F such that every open set containing x intersects every open set containing F"
    - "An open set whose complement is not closed"
    - "A continuous bijection from X to another space that is not a homeomorphism"
  answer: 1
  explanation: "Regularity fails when a point and a disjoint closed set cannot be placed in disjoint open neighborhoods. Option B directly describes this: x and F cannot be separated, even though they are topologically distinct objects (x is not in F). A space can be T₂ (separating any two points) while failing this stronger condition — there exist pathological spaces that separate points but cannot separate a point from a closed set."

- question: "Every metric space is regular: given a point x and a closed set F with x ∉ F, open balls of radius r < d(x, F)/2 around x and around points of F provide the required disjoint open separation."
  type: true-false
  answer: true
  explanation: "In a metric space, d(x, F) = inf_{y ∈ F} d(x, y) > 0 because F is closed and x ∉ F. Open balls B(x, r) and ∪_{y∈F} B(y, r) for r = d(x,F)/2 are disjoint: any point in both would satisfy d(x, z) < r and d(z, y) < r for some y ∈ F, giving d(x, y) < 2r = d(x, F) — a contradiction. This is why metric spaces are well-behaved topologically: the metric provides the geometric tools to construct separation."

- question: "A regular topological space automatically satisfies the Hausdorff (T₂) axiom — that any two distinct points can be separated by disjoint open sets."
  type: true-false
  answer: false
  explanation: "Regularity alone does not imply T₂. Consider an indiscrete space with two points: every 'closed set' is either empty or the whole space, so the regularity condition is vacuously satisfied (there's no closed set disjoint from any point that you need to separate). But the two points cannot be separated by open sets. The T₃ axiom adds the T₀ condition (distinct points are topologically distinguishable), and together T₀ + regular does imply T₂. The subscript naming matters: T₃ = regular + T₀, not just regular."

- question: "What is the key difference between the T₂ (Hausdorff) axiom and the regularity axiom, and why does this make regularity a stronger form of separation?"
  type: short-answer
  answer: "T₂ separates two points: given distinct x, y, there exist disjoint open sets U ∋ x and V ∋ y. Regularity separates a point from a closed set: given x and closed F with x ∉ F, there exist disjoint open sets U ∋ x and V ⊇ F. Separating a point from an entire closed set is a more demanding task than separating two points, because a closed set can be infinite and its points can cluster arbitrarily close to x. Regularity (combined with T₀) implies T₂ — since {y} is closed in a T₁ space, regularity of x from {y} gives the T₂ separation — but T₂ does not in general imply regularity."
  explanation: "The progression T₀ ⊂ T₁ ⊂ T₂ ⊂ T₃ ⊂ T₄ represents a strict hierarchy of separation strength, with each level solving a harder separation problem. Regular + T₀ = T₃ sits above T₂ because it separates points from closed sets rather than just pairs of points."
```
