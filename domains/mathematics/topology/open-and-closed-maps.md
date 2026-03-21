---
id: open-and-closed-maps
title: Open and Closed Maps
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-spaces
  type: hard
builds-toward:
- quotient-maps-and-identification
tags:
- open-maps
- closed-maps
- open-mapping-theorem
stage: advanced
status: draft
---

# Open and Closed Maps

## Core Idea
A function is open if images of open sets are open, and closed if images of closed sets are closed. Neither property implies continuity, nor does continuity imply either; homeomorphisms are continuous open maps. Open maps arise naturally in topology when studying quotient constructions and projections.

## How It's Best Learned
Work through explicit examples: show that the projection map ℝ² → ℝ is open but not closed; find a continuous map that is neither open nor closed; verify that a homeomorphism must be both continuous and open (or closed). These contrasts build intuition for the independence of the three properties.

## Common Misconceptions
- Assuming continuous maps must be open or closed; projection maps are open but sin : ℝ → [-1,1] is neither.
- Confusing open maps with open functions in the complex analysis sense (holomorphic non-constant functions).
- Thinking open and closed maps are "dual" in the same way open and closed sets are — the two properties are independent.

## Questions

```yaml
- question: "Consider the projection π : ℝ² → ℝ defined by π(x, y) = x, and the closed set C = {(x, y) : xy = 1} (the hyperbola). What is π(C) in ℝ, and what does this reveal about π?"
  type: multiple-choice
  options:
    - "π(C) = ℝ, which is both open and closed — showing π is both open and closed"
    - "π(C) = (−∞, 0) ∪ (0, ∞), which is open in ℝ — showing that π is continuous but not closed"
    - "π(C) = ℝ \\ {0}, which is closed in ℝ — showing π is a closed map"
    - "π(C) = [−1, 1], since the hyperbola is bounded — showing π is neither open nor closed"
  answer: 1
  explanation: "The hyperbola C approaches but never reaches (0, y) for any y — as x → 0, y = 1/x → ∞. So the projection misses 0: π(C) = (−∞, 0) ∪ (0, ∞). This set is open in ℝ, not closed (0 is a limit point not in the set). This shows π fails to be a closed map — it sends a closed set to an open set. Yet π is continuous (a basic fact) and open (projections of open sets in ℝ² are open in ℝ). This example is the canonical demonstration that continuity and openness do not imply closedness."

- question: "The map f : [0, 1) → S¹ that wraps the half-open interval onto the circle is a continuous bijection. Why is it not a homeomorphism?"
  type: multiple-choice
  options:
    - "It is not injective — two distinct points in [0, 1) map to the same point on the circle"
    - "It is not continuous — there is a discontinuity at the endpoint 0"
    - "Its inverse is not continuous, which means f fails to be an open map — open sets in [0, 1) near 0 do not map to open sets in S¹"
    - "Every continuous bijection between compact spaces is automatically a homeomorphism, so this map must be a homeomorphism"
  answer: 2
  explanation: "The set [0, 0.5) is open in [0, 1) (in the subspace topology), but its image in S¹ includes the 'join point' of the circle without an open arc entirely surrounding it — so the image is not open in S¹. This means f is not an open map, and therefore its inverse is not continuous. The continuous+bijective combination is insufficient for a homeomorphism; you need also openness (or closedness). Option D is a common error: the theorem that continuous bijections from compact spaces to Hausdorff spaces are homeomorphisms requires compactness of the domain — [0, 1) is not compact."

- question: "Continuity of f : X → Y is defined in terms of preimages of open sets, while openness of f is defined in terms of images of open sets."
  type: true-false
  answer: true
  explanation: "This is the precise distinction between the two properties, and it explains why they are logically independent. Continuity: for every open V ⊆ Y, f⁻¹(V) is open in X. Openness: for every open U ⊆ X, f(U) is open in Y. The direction is reversed. A map can be continuous but not open (e.g., sin : ℝ → [−1, 1]), open but not continuous (a bijection between a discrete and an indiscrete space), both, or neither."

- question: "A map that is both continuous and open must be a homeomorphism."
  type: true-false
  answer: false
  explanation: "A homeomorphism requires continuous + open + bijective. Continuous and open alone are not enough. The projection π : ℝ² → ℝ is both continuous and open, but it is not bijective (many points map to the same value), so it is not a homeomorphism. You need bijectivity as well. The equivalent characterization of a homeomorphism is: bijective, continuous, and either open or closed (since for a bijection, openness and closedness are equivalent)."

- question: "Give an example of a continuous map that is not an open map, and explain what structural feature prevents open sets from having open images."
  type: short-answer
  answer: "The function f : ℝ → ℝ defined by f(x) = x² is continuous but not open. The image of the open set (−1, 1) is [0, 1), which is not open in ℝ — it includes 0 as a minimum boundary point. The structural reason: f is not injective (it folds ℝ over the origin), so the image of a symmetric open interval around 0 includes 0 as an endpoint without an open neighborhood around it in the image."
  explanation: "More broadly, open maps tend to arise for 'quotient-like' maps that spread points out, rather than maps that fold or collapse them. Projections, quotient maps, and open linear maps are open because they don't create boundary points in the image. Maps that collapse sets (like x² folding negative numbers onto positive ones) can create boundary points in images even from open sets. The sin function is another standard example: sin(ℝ) = [−1, 1], and images of most open sets touch the endpoints ±1 without including an open neighborhood of them in [−1, 1]."
```

## Explainer

You know that a function f : X → Y between topological spaces is **continuous** if preimages of open sets are open: for every open V ⊆ Y, f⁻¹(V) is open in X. Open maps and closed maps reverse the direction: they make claims about *images* rather than preimages. A function is an **open map** if for every open U ⊆ X, the image f(U) is open in Y. A function is a **closed map** if for every closed C ⊆ X, f(C) is closed in Y. These three properties — continuity, openness, closedness — are logically independent. None implies either of the others in general.

The simplest open map to internalize is the projection π : ℝ² → ℝ defined by π(x, y) = x. If U is an open set in ℝ², then π(U) is open in ℝ: informally, projecting an open "blob" in the plane produces an open interval (or union of intervals) on the line, since removing boundary points in the x-direction can't suddenly create a boundary in ℝ. Yet π is not a closed map: the hyperbola {(x, y) : xy = 1} is a closed subset of ℝ², but its projection onto the x-axis is (−∞, 0) ∪ (0, ∞) — open, not closed. The y = 1/x curve "escapes to infinity," and its shadow on the x-axis misses 0 without being able to include it.

A **homeomorphism** is a bijective map that is both continuous and has a continuous inverse — it is an isomorphism of topological spaces. An equivalent characterization: f is a homeomorphism if and only if it is continuous, bijective, *and* open (or equivalently, continuous, bijective, and closed). The continuous+bijective alone is not enough: the map [0, 1) → S¹ (wrapping the half-open interval onto the circle) is a continuous bijection that is not a homeomorphism, because its inverse is not continuous. It fails to be an open map: the set [0, 0.5) is open in [0, 1) but its image is not open in S¹, since the image includes the "join point" of the circle with no surrounding open arc entirely in the image.

Open and closed maps arise naturally wherever you need to control the topology of images, not just preimages. **Quotient maps** — the topological workhorse for constructing new spaces by identification — are often open maps, and being able to certify that a map is open or closed lets you verify that the quotient topology has the right properties. In analysis, the open mapping theorem for Banach spaces (a continuous surjective linear map between Banach spaces is open) is a deep result with far-reaching consequences, including the closed graph theorem. Learning to distinguish these three properties — continuous, open, closed — and identify which combinations arise in natural constructions is essential for working fluently with topological and functional-analytic arguments.

