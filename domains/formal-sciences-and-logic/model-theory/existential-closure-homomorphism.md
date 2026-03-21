---
id: existential-closure-homomorphism
title: Existential Closure Under Homomorphisms
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: embedding-and-preservation-properties
  type: hard
- id: diagram-expansion-by-constants
  type: hard
- id: existential-formulas-embeddings
  type: soft
builds-toward:
- extension-lemma-embeddings
tags:
- existential
- closure
- preservation
- homomorphism
stage: advanced
status: draft
---

# Existential Closure Under Homomorphisms

## Core Idea
If f: M → N is a homomorphism and φ(x) is an existential formula satisfied by some a in M, then φ(f(a)) is satisfied in N. This is the key property allowing us to push existential properties forward through homomorphisms, and it justifies why embeddings (injective homomorphisms reflecting existentials) are natural in model theory.

## Questions

```yaml
- question: "A student argues: 'Since f: M → N is a homomorphism and M ⊨ ∀x R(x), we can conclude N ⊨ ∀x R(x).' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — homomorphisms preserve all first-order formulas, including universal ones"
    - "The student is correct only if f is surjective"
    - "N may contain elements with no preimage under f; these elements need not satisfy R, destroying the universal claim"
    - "Universal formulas are never preserved because homomorphisms are not embeddings"
  answer: 2
  explanation: "Homomorphisms only guarantee that atomic (and existential) facts about *images* of M-elements hold in N. If N has elements outside the image of f, those elements are unconstrained — they might not satisfy R. A surjective homomorphism maps every N-element from some M-element, which helps somewhat, but even then negated atomics can fail. Only embeddings (injective homomorphisms that also reflect atomic truth) give the control needed for universal preservation."

- question: "Suppose M ⊨ ∃x φ(x, a) where φ is quantifier-free, and f: M → N is a homomorphism. Why does N ⊨ ∃x φ(x, f(a)) follow?"
  type: multiple-choice
  options:
    - "Because f is injective, so the witness cannot be collapsed away"
    - "Because φ involves only existential quantifiers, and homomorphisms preserve the entire existential theory"
    - "The witness b ∈ M satisfies M ⊨ φ(b, a); since φ is quantifier-free, f preserves each atomic subformula involving b and a, so N ⊨ φ(f(b), f(a)); and f(b) exists in N, witnessing the existential"
    - "Because homomorphisms are bijections, every element of M has a unique image that preserves all properties"
  answer: 2
  explanation: "The key is that φ is quantifier-free: it is a Boolean combination of atomic formulas. Homomorphisms preserve atomic truth (if M ⊨ R(b, a) then N ⊨ R(f(b), f(a))). Boolean combinations of preserved atomics remain preserved. So φ(b, a) holding in M implies φ(f(b), f(a)) holds in N. The image f(b) then serves as the witness for the existential in N. No injectivity is required — we just need f(b) to exist, which it does."

- question: "If f: M → N is a homomorphism and M ⊨ ∃x∃y(R(x, a) ∧ ¬R(y, a)), then N ⊨ ∃x∃y(R(x, f(a)) ∧ ¬R(y, f(a)))."
  type: true-false
  answer: false
  explanation: "Homomorphisms preserve positive existential formulas — those built from atomic formulas using ∧, ∨, and ∃ — but NOT negated atomics. The formula here contains ¬R(y, a), a negated atomic. A homomorphism can collapse elements or make new atomic facts true: if f(y) = f(x) in N and R(f(x), f(a)) holds, then ¬R(f(y), f(a)) fails. Homomorphisms only push witnesses of *positive* existential claims forward; negation is not preserved."

- question: "The diagram technique in model theory works because the existence of a homomorphism from the diagram of M into N corresponds precisely to N satisfying the existential consequences of M's theory."
  type: true-false
  answer: true
  explanation: "This is exactly what existential closure under homomorphisms establishes. The diagram of M records all atomic facts about M's elements (expressed as sentences using new constants). A model of those sentences gives you a structure in which those atomic facts hold, and hence a homomorphism from M into that structure. Existential closure then guarantees that everything M existentially asserts — every ∃-formula true in M — is also true in N via the images of the witnesses. This is the foundational justification for diagram-based model constructions."

- question: "Explain in your own words why the image of a witness under a homomorphism is a valid witness for the same existential formula in the target structure."
  type: short-answer
  answer: "An existential formula ∃x φ(x, a) is witnessed in M by some element b with M ⊨ φ(b, a). Since φ is quantifier-free, it is built from atomic subformulas by Boolean connectives without negation of non-atomic parts. Homomorphisms preserve atomic truth: every positive atomic fact about b and a that holds in M also holds about f(b) and f(a) in N. So N ⊨ φ(f(b), f(a)), and since f(b) exists in N, it witnesses ∃x φ(x, f(a)) there."
  explanation: "The critical insight is that existential witnesses are concrete elements, and their images are still present in N. The quantifier-free matrix φ only makes positive atomic claims about those witnesses — and homomorphisms, by definition, preserve positive atomic claims. Universal formulas fail because they make claims about *all* elements of N, including those with no preimage in M, which the homomorphism says nothing about."
```

## Explainer

You already know that a homomorphism f: M → N between structures in the same language preserves atomic formulas: if M ⊨ R(a₁, …, aₙ), then N ⊨ R(f(a₁), …, f(aₙ)). Existential closure under homomorphisms extends this one step: homomorphisms also preserve **existential formulas** — formulas of the form ∃x₁ … ∃xₙ φ(x₁, …, xₙ, y) where φ is quantifier-free. The key insight is that an existential claim says "there exists something witnessing this property." If witnesses exist in M, their images under f exist in N and satisfy the same atomic conditions, because f preserves atomic truth.

To see why this works, trace through the logic. Suppose M ⊨ ∃x φ(x, a), witnessed by some element b ∈ M with M ⊨ φ(b, a). The formula φ is built from atoms using conjunctions, disjunctions, and negations — but not universal quantifiers. Since f preserves each atomic statement about b and a, and since existential-free Boolean combinations of preserved atomic facts remain preserved, we get N ⊨ φ(f(b), f(a)). Since f(b) exists in N, we get N ⊨ ∃x φ(x, f(a)). The existential witness is simply the image of the original witness.

Crucially, homomorphisms do *not* in general preserve **universal formulas** or **negated atomic formulas**. A homomorphism can collapse distinct elements (two elements of M may map to the same element of N), which can destroy universal claims and make false atoms true. For example, if M models "¬R(a,b)" and f(a) = f(b) in N, then N might model R(f(a), f(b)) anyway. This asymmetry explains why **embeddings** — injective homomorphisms — are more powerful: they reflect as well as preserve atomic facts, and thus preserve and reflect all quantifier-free formulas.

This property is not merely an abstract curiosity. It is the foundation for the diagram technique in model theory: the diagram of a structure M records all atomic facts about its elements, and the existence of a homomorphism from the diagram into N precisely corresponds to satisfying the existential consequences of M's theory. From your prerequisite work on diagram expansion, you know that adding constant symbols for each element of M allows you to state these facts as sentences — and a model of those sentences gives you a homomorphic image of M inside N. Existential closure under homomorphisms is what makes this technique work.
