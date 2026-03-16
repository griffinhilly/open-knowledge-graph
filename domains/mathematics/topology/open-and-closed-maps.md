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

## Explainer

You know that a function f : X → Y between topological spaces is **continuous** if preimages of open sets are open: for every open V ⊆ Y, f⁻¹(V) is open in X. Open maps and closed maps reverse the direction: they make claims about *images* rather than preimages. A function is an **open map** if for every open U ⊆ X, the image f(U) is open in Y. A function is a **closed map** if for every closed C ⊆ X, f(C) is closed in Y. These three properties — continuity, openness, closedness — are logically independent. None implies either of the others in general.

The simplest open map to internalize is the projection π : ℝ² → ℝ defined by π(x, y) = x. If U is an open set in ℝ², then π(U) is open in ℝ: informally, projecting an open "blob" in the plane produces an open interval (or union of intervals) on the line, since removing boundary points in the x-direction can't suddenly create a boundary in ℝ. Yet π is not a closed map: the hyperbola {(x, y) : xy = 1} is a closed subset of ℝ², but its projection onto the x-axis is (−∞, 0) ∪ (0, ∞) — open, not closed. The y = 1/x curve "escapes to infinity," and its shadow on the x-axis misses 0 without being able to include it.

A **homeomorphism** is a bijective map that is both continuous and has a continuous inverse — it is an isomorphism of topological spaces. An equivalent characterization: f is a homeomorphism if and only if it is continuous, bijective, *and* open (or equivalently, continuous, bijective, and closed). The continuous+bijective alone is not enough: the map [0, 1) → S¹ (wrapping the half-open interval onto the circle) is a continuous bijection that is not a homeomorphism, because its inverse is not continuous. It fails to be an open map: the set [0, 0.5) is open in [0, 1) but its image is not open in S¹, since the image includes the "join point" of the circle with no surrounding open arc entirely in the image.

Open and closed maps arise naturally wherever you need to control the topology of images, not just preimages. **Quotient maps** — the topological workhorse for constructing new spaces by identification — are often open maps, and being able to certify that a map is open or closed lets you verify that the quotient topology has the right properties. In analysis, the open mapping theorem for Banach spaces (a continuous surjective linear map between Banach spaces is open) is a deep result with far-reaching consequences, including the closed graph theorem. Learning to distinguish these three properties — continuous, open, closed — and identify which combinations arise in natural constructions is essential for working fluently with topological and functional-analytic arguments.

