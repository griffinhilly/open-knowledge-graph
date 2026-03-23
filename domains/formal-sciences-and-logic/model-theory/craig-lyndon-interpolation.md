---
id: craig-lyndon-interpolation
title: Craig-Lyndon Interpolation Theorem
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: logical-consequence-and-entailment
  type: hard
- id: interpolation-theorem
  type: soft
builds-toward:
- beth-definability-implicit-explicit
tags:
- Craig
- interpolation
- interpolant
- consequence
stage: formal-systems
status: validated
---

# Craig-Lyndon Interpolation Theorem

## Core Idea
If φ → ψ is a tautology, there exists an interpolant θ (using only symbols common to φ and ψ) such that φ → θ and θ → ψ are both tautologies. The Lyndon version strengthens this: the interpolant can be chosen to preserve the direction of implications in formulas. Interpolation theorems are fundamental for studying definability and relationships between formulas.

## Questions

```yaml
- question: "Craig interpolation guarantees an interpolant θ using only shared vocabulary when φ ⊨ ψ. What does the Lyndon strengthening add to this guarantee?"
  type: multiple-choice
  options:
    - "The interpolant θ may use vocabulary from φ or ψ exclusively, relaxing the shared-vocabulary requirement"
    - "The Lyndon version guarantees the interpolant is logically equivalent to both φ and ψ, not merely implied by one and implying the other"
    - "The interpolant can be chosen so that any predicate occurring positively in θ occurs positively in both φ and ψ, and any predicate occurring negatively in θ occurs negatively in both"
    - "The Lyndon version eliminates the need for an interpolant by providing a direct constructive proof of φ → ψ"
  answer: 2
  explanation: "Craig's theorem restricts vocabulary: θ uses only symbols shared by φ and ψ. Lyndon adds a polarity constraint on top of this: shared symbols must appear in θ with the same directional role they have in both φ and ψ. A predicate appearing positively in θ must appear positively in both φ and ψ; similarly for negative occurrences. This is strictly stronger — every Lyndon interpolant is a Craig interpolant, but not every Craig interpolant satisfies the Lyndon polarity condition."

- question: "Why does polarity preservation in the Lyndon interpolant matter beyond being a technical refinement of Craig's theorem?"
  type: multiple-choice
  options:
    - "It reduces the computational complexity of finding the interpolant from exponential to polynomial"
    - "It ensures the interpolant is always a Horn clause, making it efficiently computable"
    - "Controlled polarity enables sharper definability results: explicit definitions derived from implicit ones can be chosen with controlled monotonicity properties that Craig interpolation alone cannot guarantee"
    - "It eliminates quantifier alternations in the interpolant, simplifying its logical structure"
  answer: 2
  explanation: "Polarity encodes monotonicity: a predicate appearing only positively is monotone increasing in that position — adding elements to its extension can only help the formula hold. The Lyndon theorem guarantees the interpolant preserves this structure. This has direct consequences for Beth definability: when constructing an explicit definition from an implicit one, the Lyndon version guarantees the definition has controlled monotonicity properties. Craig interpolation restricts vocabulary but leaves the directional behavior of that vocabulary unconstrained."

- question: "Craig interpolation applies only to propositional logic and cannot be extended to first-order logic."
  type: true-false
  answer: false
  explanation: "Craig interpolation applies to first-order logic. Craig's original 1957 result was proven for first-order logic; propositional logic is a special case. Both the Craig and Craig-Lyndon versions hold in first-order settings, where the theorem is fundamental to model theory — connecting to Beth definability, completeness results, and the structural properties of logical entailment between theories."

- question: "The Craig-Lyndon theorem is strictly stronger than Craig's theorem: every Lyndon interpolant satisfies Craig's vocabulary condition, but a Craig interpolant need not satisfy the Lyndon polarity condition."
  type: true-false
  answer: true
  explanation: "This is the precise logical relationship between the two results. Craig guarantees: an interpolant exists using only shared vocabulary. Lyndon guarantees: an interpolant exists using shared vocabulary AND with polarity constraints respected. Any interpolant satisfying the Lyndon condition automatically satisfies Craig (it uses shared vocabulary), but an interpolant guaranteed only by Craig might have predicates appearing in the wrong polarity. The Lyndon theorem makes strictly more promises about the interpolant's internal logical structure."

- question: "In your own words, what does it mean for a predicate symbol to appear 'positively' in a formula, and why does the Lyndon theorem's polarity constraint make it a stronger result than Craig's original theorem?"
  type: short-answer
  answer: "A predicate occurs positively in a formula if it appears in a context where extending its interpretation (adding more elements that satisfy it) can only help the formula be satisfied — roughly, not under an odd number of negations. It occurs negatively when restricting its interpretation helps. Craig's theorem constrains only which symbols appear in the interpolant (shared vocabulary). Lyndon additionally constrains how they appear: positively-occurring symbols in the interpolant must occur positively in both φ and ψ. This preserves the monotonicity structure of the entailment, which Craig interpolation leaves unconstrained."
  explanation: "The practical consequence: in formal verification and definability theory, monotonicity (positive polarity) is a useful structural property. A formula monotone in predicate P is preserved when P's extension grows, enabling certain inference rules and optimizations. The Lyndon theorem guarantees the 'common content' of an entailment can be expressed while respecting these directional constraints. This is what enables the stronger Beth-definability applications mentioned in the explainer — the explicit definition can be chosen with controlled monotonicity, not merely with controlled vocabulary."
```

## Explainer

You already understand Craig interpolation from your prerequisite: when φ logically entails ψ, there is an interpolant θ using only the vocabulary shared by both, with φ ⊨ θ and θ ⊨ ψ. The **Craig-Lyndon theorem** refines this result by imposing an additional constraint on the interpolant — one that encodes not just *which* predicate symbols appear, but *how* they appear directionally.

The Lyndon strengthening concerns **polarity**. In a formula, a predicate symbol can appear **positively** (in a context where increasing its extension can only help the formula hold — for instance, not under any negation), **negatively** (where decreasing its extension helps), or both. The Lyndon refinement says the interpolant θ can be chosen so that any predicate occurring positively in θ occurs positively in both φ and ψ, and any predicate occurring negatively in θ occurs negatively in both. This is a strictly stronger claim than bare Craig interpolation: the vocabulary constraint remains, but now the *directional role* of each shared symbol is also preserved.

Why does this refinement matter? In formal verification, modal logic, and definability theory, polarity carries semantic weight: a predicate appearing only positively is monotone in that position. The Lyndon version guarantees that the interpolant's logical structure mirrors the polarity structure of the original entailment, which enables stronger applications. For example, the Lyndon version implies sharper definability results than Craig's version alone — when constructing an explicit definition from an implicit one, the definition can be chosen with controlled monotonicity properties.

Both versions connect to **Beth definability**: if a theory implicitly defines a predicate (its extension is uniquely determined by the rest of the theory in any model), then that predicate is explicitly definable using the theory's existing vocabulary. The Craig-Lyndon version strengthens this: the explicit definition can be chosen with controlled polarity. Together, these results reveal that the vocabulary-mediated structure of logical entailment is not arbitrary — there is always a principled "common content" mediating any entailment, and its internal directional structure can be isolated and expressed precisely.
