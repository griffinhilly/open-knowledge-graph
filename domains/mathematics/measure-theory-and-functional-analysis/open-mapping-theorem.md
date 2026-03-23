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
stage: expert
status: validated
---

# Open Mapping Theorem

## Core Idea
The open mapping theorem states that a continuous surjective linear operator between Banach spaces is open (maps open sets to open sets). This deep result relies on the Baire category theorem and implies the bounded inverse theorem.

## Questions

```yaml
- question: "A continuous surjective linear operator T: X → Y is given, where X is a Banach space and Y is only a normed space (not complete). Which conclusion is guaranteed by the open mapping theorem?"
  type: multiple-choice
  options:
    - "T maps open sets to open sets, since T is continuous and surjective"
    - "T maps open sets to open sets only if T is also injective"
    - "The theorem does not apply — both spaces must be Banach for the conclusion to hold"
    - "T maps open sets to open sets, but T⁻¹ may not be continuous"
  answer: 2
  explanation: "The open mapping theorem requires *both* domain and codomain to be Banach spaces. If Y is not complete, the Baire category theorem argument breaks down and counterexamples exist. Option A is the tempting error — continuity plus surjectivity feel sufficient, but completeness is the hidden engine of the proof."

- question: "Suppose T: X → Y is a continuous bijective linear operator between Banach spaces. What does the bounded inverse theorem (a corollary of the open mapping theorem) guarantee?"
  type: multiple-choice
  options:
    - "T⁻¹ exists but may be unbounded"
    - "T⁻¹ is continuous (bounded) automatically"
    - "T⁻¹ is continuous only if T is also an isometry"
    - "T⁻¹ is continuous only in finite dimensions"
  answer: 1
  explanation: "The bounded inverse theorem says a continuous bijection between Banach spaces automatically has a continuous inverse. Since T is open (by the open mapping theorem), T sends open sets to open sets, which is precisely what continuity of T⁻¹ means. In finite dimensions this is trivial; in infinite dimensions it requires the full force of completeness and is genuinely surprising."

- question: "In infinite-dimensional Banach spaces, a continuous bijective linear operator is automatically a homeomorphism."
  type: true-false
  answer: true
  explanation: "This is the bounded inverse theorem, a direct corollary of the open mapping theorem. A continuous bijection T: X → Y between Banach spaces has a continuous inverse T⁻¹. The proof uses surjectivity to apply the open mapping theorem, which gives T maps open sets to open sets — precisely continuity of T⁻¹."

- question: "The open mapping theorem applies to any continuous surjective linear map between normed spaces — completeness is a convenience, not a necessity."
  type: true-false
  answer: false
  explanation: "Completeness is essential. The proof fundamentally uses the Baire category theorem, which holds for complete metric spaces. Without completeness, continuous surjective linear maps between normed spaces exist that are not open. The Banach space assumption on both domain and codomain cannot be dropped."

- question: "Why does surjectivity, combined with completeness of both spaces, force a continuous linear operator to be an open map? What is the key mechanism in the proof?"
  type: short-answer
  answer: "The key mechanism is the Baire category theorem applied to the surjection. Since T is surjective, Y is covered by scaled images of unit balls in X. The Baire category theorem (requiring completeness of Y) guarantees some image ball has nonempty interior. Linearity then propagates this to every ball around the origin, showing T maps every open ball to a set with nonempty interior — which is exactly what openness means."
  explanation: "The proof has two steps: use Baire to get nonempty interior of a ball image, then use linearity to extend this globally. Both require completeness (for Baire), surjectivity (to cover Y), and linearity (to propagate local openness). All three hypotheses are doing real work."
```

## Explainer

An **open mapping** is a function that sends open sets to open sets. Continuous functions go in the other direction — they pull open sets back to open sets — so openness and continuity are distinct properties. For general nonlinear functions, there is no reason to expect both: a continuous function can easily collapse an open interval to a single point (not open). The open mapping theorem says that for continuous *linear* operators between *Banach spaces*, surjectivity alone forces the map to be open. This is a remarkable structural rigidity.

To see why this is surprising, consider the analogous finite-dimensional statement: a surjective linear map from ℝᵐ to ℝⁿ maps open sets to open sets. In finite dimensions this is almost obvious — a surjective linear map on finite-dimensional spaces has a right inverse (just pick a basis). But in infinite-dimensional Banach spaces, surjectivity does not automatically come with nice inverse properties, and "openness" is a much more delicate condition. The theorem says that completeness — the Banach space assumption — makes surjectivity strong enough to guarantee it.

The proof uses the **Baire category theorem**, which says a complete metric space cannot be written as a countable union of nowhere-dense sets. The argument runs roughly as follows: write the Banach space X as a union of scaled closed balls, apply T to get a union covering T(X) = Y, invoke the Baire category theorem to conclude that some image ball has nonempty interior, and then use linearity and the group structure to show the image of *every* ball around the origin has nonempty interior. This last step is the technical heart of the proof. Once you know T maps balls to sets with nonempty interior, you can show that T maps open sets to open sets.

The most important consequence is the **bounded inverse theorem**: if T: X → Y is a continuous bijective linear operator between Banach spaces, then T⁻¹ is also continuous. In other words, a continuous bijection between Banach spaces is automatically a homeomorphism. In finite dimensions, this is trivial — every linear bijection on ℝⁿ is a homeomorphism. But in infinite dimensions, it requires proof, and the open mapping theorem provides it. The bounded inverse theorem is the tool analysts use to conclude that two natural norms on the same space are equivalent whenever they define complete spaces.

The open mapping theorem also has a useful reformulation: T: X → Y is open if and only if there exists δ > 0 such that the open unit ball in Y is contained in the image of the open unit ball of X scaled by 1/δ. This "ball-covering" version is often the most practical way to verify openness in applications — you need to quantify how much T can shrink things, and surjectivity of a Banach space operator provides exactly that control.
