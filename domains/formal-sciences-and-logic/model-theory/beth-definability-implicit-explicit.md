---
id: beth-definability-implicit-explicit
title: 'Beth Definability: From Implicit to Explicit Definitions'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: craig-lyndon-interpolation
  type: hard
builds-toward:
- definable-closure-independence
tags:
- Beth
- definability
- implicit
- explicit
- elimination
stage: formal-systems
status: validated
---

# Beth Definability: From Implicit to Explicit Definitions

## Core Idea
Beth's theorem states that if a predicate is implicitly defined by a theory (uniquely determined up to isomorphism), then it is explicitly definable (there is a formula φ such that the theory entails the predicate equals φ). This theorem bridges implicit definability (uniqueness up to models) and explicit definability (provable equivalence), with deep connections to model-theoretic properties.

## Questions

```yaml
- question: "A theory T in a language with a binary predicate R has the property that any two models of T agreeing on all other symbols must agree on R. This means R is:"
  type: multiple-choice
  options:
    - "Explicitly defined by T — there is already a formula in the language without R that T equates with R"
    - "Implicitly defined by T — R is uniquely determined by the other vocabulary, even without a written-out equivalence formula"
    - "Undefinable, because the theory says nothing explicit about what R is"
    - "Redundant and automatically eliminable without using Beth's theorem"
  answer: 1
  explanation: "Implicit definability is exactly this condition: every model extension that agrees on the base vocabulary must also agree on R. The predicate is pinned down by the theory up to isomorphism, but no explicit formula ∀x∀y(R(x,y) ↔ φ(x,y)) has been written down. Beth's theorem then guarantees that such an explicit formula must exist — but that conclusion requires proof, it does not follow trivially from the definition of implicit definability."

- question: "Beth's theorem is proved by applying which result from earlier in model theory?"
  type: multiple-choice
  options:
    - "The compactness theorem, via a chain of elementary extensions"
    - "Craig's interpolation theorem, applied to two copies of the theory in different vocabularies"
    - "The Löwenheim-Skolem theorem, constructing a countable model in which R collapses"
    - "The completeness theorem, by showing R's extension is axiomatizable"
  answer: 1
  explanation: "The proof encodes implicit definability as: two copies of T (one with predicate R, one with R') together imply R = R'. By Craig interpolation, there must be a formula in the shared vocabulary — which excludes both R and R' — that lies between these two theories. Unpacking this interpolant yields the explicit definition of R in the reduced vocabulary. This is why interpolation is not merely a logical curiosity but a structural bridge between syntactic and semantic aspects of definability."

- question: "According to Beth's theorem in first-order logic, if a predicate R is implicitly defined by a theory T, then there exists a formula φ in the language without R such that T proves ∀x̄(R(x̄) ↔ φ(x̄))."
  type: true-false
  answer: true
  explanation: "This is the content of Beth's theorem: implicit definability (uniqueness across all models of T) entails explicit definability (a provable equivalence formula in the reduced vocabulary). The theorem is non-trivial because implicit definability is a semantic condition (about models) while explicit definability is syntactic (a formula exists). Beth's theorem says these two levels coincide in first-order logic, which is precisely because first-order logic satisfies Craig interpolation."

- question: "Beth's theorem holds in most logical systems, including second-order logic: whenever a predicate is implicitly defined, it is explicitly definable."
  type: true-false
  answer: false
  explanation: "Beth's theorem is a theorem of first-order logic and depends on the Craig interpolation property. Extensions such as second-order logic and many infinitary logics fail the interpolation property, and in those systems implicit and explicit definability can come apart — a predicate can be uniquely determined by all models of a theory without any formula in the reduced vocabulary explicitly capturing it. This is why the failure of Beth's theorem in a logic is itself a diagnostic: it signals that interpolation fails and that the logic has a weaker connection between syntax and semantics."

- question: "What does it mean for a predicate to be eliminable from a theory, and why does Beth's theorem guarantee eliminability whenever a predicate is implicitly defined?"
  type: short-answer
  answer: "A predicate R is eliminable from a theory T if every sentence involving R can be translated into a logically equivalent sentence in the language without R, preserving all provable consequences. Beth's theorem guarantees this because it provides an explicit formula φ (in the R-free vocabulary) such that T ⊢ ∀x̄(R(x̄) ↔ φ(x̄)). This biconditional allows systematic replacement of R by φ in any sentence, translating away every occurrence of R without changing what the theory asserts."
  explanation: "Eliminability is the practical payoff of Beth's theorem: it means that implicitly-defined predicates are genuine abbreviations — they introduce no expressive power beyond what already exists in the base vocabulary. This is important for modularity in formal systems (you can always 'unpack' defined symbols) and for understanding what a theory actually commits to. When implicit and explicit definability come apart (as in logics without interpolation), predicates can be 'defined' in a model-theoretic sense but not eliminable — they add irreducible expressive content."
```

## Explainer

You have already encountered Craig's interpolation theorem, which says that whenever one formula logically implies another, there is an intermediate formula — built from the shared vocabulary — that lies between them. Beth's definability theorem is a striking application of this same machinery to the question of what it means for a theory to "pin down" a predicate.

Start with a concrete example. Suppose you have a theory T in a language that includes a binary relation symbol R, and you notice that any two models of T that agree on all the other symbols must agree on R as well — R is completely determined by the rest. In that case, we say R is **implicitly defined** by T: it is uniquely determined up to the structure of the models, even though you have not written down a formula that says what R actually is. The question Beth's theorem answers is: if R is implicitly defined, can you always make that definition **explicit** — that is, can you find a single formula φ(x, y) in the language without R such that T entails ∀x∀y (R(x,y) ↔ φ(x,y))?

The answer is yes, and the proof proceeds directly from Craig's interpolation theorem. The argument goes roughly like this: implicit definability of R by T is exactly the statement that two copies of T — one in which R plays one role and one in which R' plays another — together imply R = R'. By Craig interpolation, there must be an interpolant, a formula in the shared language (which lacks R and R'), that separates the two. Unpacking what this interpolant says gives the explicit definition of R. The connection illuminates why interpolation is not just a curiosity but a structural fact about how syntax and semantics interact.

**Beth's theorem** matters practically for the question of **eliminability**: when can a defined predicate be removed from a theory without loss? If you introduce a new predicate symbol R as shorthand and your theory implicitly defines R in terms of existing vocabulary, then R is always eliminable — every statement about R translates into a statement about the underlying vocabulary. This is a prerequisite for modularity in formal systems. When implicit and explicit definability come apart (as they do for some extensions of first-order logic), the logic lacks the interpolation property, which is itself a signature of expressive pathology. Beth definability thus serves as a diagnostic tool for measuring how tightly syntax and semantics are coupled in a given logical system.
