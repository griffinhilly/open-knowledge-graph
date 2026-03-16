---
id: open-mapping-theorem
title: Open Mapping Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
builds-toward:
- closed-graph-theorem
tags:
- functional-analysis
stage: abstract-reasoning
status: draft
---

# Open Mapping Theorem

## Core Idea
The open mapping theorem states that a continuous surjective linear operator between Banach spaces is open (maps open sets to open sets). This deep result relies on the Baire category theorem and implies the bounded inverse theorem.

## Explainer

An **open mapping** is a function that sends open sets to open sets. Continuous functions go in the other direction — they pull open sets back to open sets — so openness and continuity are distinct properties. For general nonlinear functions, there is no reason to expect both: a continuous function can easily collapse an open interval to a single point (not open). The open mapping theorem says that for continuous *linear* operators between *Banach spaces*, surjectivity alone forces the map to be open. This is a remarkable structural rigidity.

To see why this is surprising, consider the analogous finite-dimensional statement: a surjective linear map from ℝᵐ to ℝⁿ maps open sets to open sets. In finite dimensions this is almost obvious — a surjective linear map on finite-dimensional spaces has a right inverse (just pick a basis). But in infinite-dimensional Banach spaces, surjectivity does not automatically come with nice inverse properties, and "openness" is a much more delicate condition. The theorem says that completeness — the Banach space assumption — makes surjectivity strong enough to guarantee it.

The proof uses the **Baire category theorem**, which says a complete metric space cannot be written as a countable union of nowhere-dense sets. The argument runs roughly as follows: write the Banach space X as a union of scaled closed balls, apply T to get a union covering T(X) = Y, invoke the Baire category theorem to conclude that some image ball has nonempty interior, and then use linearity and the group structure to show the image of *every* ball around the origin has nonempty interior. This last step is the technical heart of the proof. Once you know T maps balls to sets with nonempty interior, you can show that T maps open sets to open sets.

The most important consequence is the **bounded inverse theorem**: if T: X → Y is a continuous bijective linear operator between Banach spaces, then T⁻¹ is also continuous. In other words, a continuous bijection between Banach spaces is automatically a homeomorphism. In finite dimensions, this is trivial — every linear bijection on ℝⁿ is a homeomorphism. But in infinite dimensions, it requires proof, and the open mapping theorem provides it. The bounded inverse theorem is the tool analysts use to conclude that two natural norms on the same space are equivalent whenever they define complete spaces.

The open mapping theorem also has a useful reformulation: T: X → Y is open if and only if there exists δ > 0 such that the open unit ball in Y is contained in the image of the open unit ball of X scaled by 1/δ. This "ball-covering" version is often the most practical way to verify openness in applications — you need to quantify how much T can shrink things, and surjectivity of a Banach space operator provides exactly that control.
