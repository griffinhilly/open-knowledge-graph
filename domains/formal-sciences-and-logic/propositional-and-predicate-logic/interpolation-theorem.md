---
id: interpolation-theorem
title: Craig Interpolation Theorem
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: fol-compactness
  type: hard
- id: model-theory-basics
  type: hard
builds-toward:
- lowenheim-skolem-theorem
tags:
- Craig-interpolation
- Beth-definability
- implicit-definition
- explicit-definition
- interpolant
stage: formal-systems
status: validated
---

# Craig Interpolation Theorem

## Core Idea
Craig's interpolation theorem states that if φ ⊨ ψ (φ logically implies ψ), then there exists a sentence θ — the interpolant — whose non-logical vocabulary (predicate, function, and constant symbols) is contained in both φ and ψ, such that φ ⊨ θ and θ ⊨ ψ. The interpolant captures exactly the "common content" that mediates the entailment. Beth's definability theorem follows as a corollary: if a predicate is implicitly defined by a theory (its extension is uniquely determined), then it is explicitly definable by a formula in the theory's language. Together, these results reveal deep structural properties of first-order logic connecting semantics, syntax, and definability.

## How It's Best Learned
Take a concrete entailment (e.g., ∀x(P(x) → Q(x)) ⊨ ∀x(P(x) → Q(x) ∨ R(x))) and find the interpolant by hand — it must use only the shared vocabulary. Then study how Beth's theorem uses interpolation to convert implicit definitions into explicit ones.

## Common Misconceptions
- The interpolant is not unique — many different sentences can serve as the interpolant for a given entailment.
- Craig interpolation holds for standard first-order logic but fails for some extensions (e.g., certain fragments of second-order logic or logics with generalized quantifiers).
- Beth definability is not trivial — the fact that implicit definability implies explicit definability is a substantive result, not a tautology.

## Questions

```yaml
- question: "Suppose φ ⊨ ψ, where φ uses predicate symbols {P, Q, R} and ψ uses predicate symbols {Q, R, S}. What can be said about the vocabulary of any interpolant θ?"
  type: multiple-choice
  options:
    - "θ must use all symbols from both φ and ψ: {P, Q, R, S}"
    - "θ's vocabulary must be a subset of {Q, R} — the symbols shared by φ and ψ"
    - "θ must be logically equivalent to φ, so it uses exactly {P, Q, R}"
    - "θ may use any symbols since its purpose is to bridge different vocabularies"
  answer: 1
  explanation: "Craig's theorem guarantees an interpolant whose non-logical vocabulary is contained in the intersection of φ's and ψ's vocabularies — here {Q, R}. The symbols P (unique to φ) and S (unique to ψ) cannot appear in θ. The key insight is that when φ ⊨ ψ, the logical connection between them must be expressible entirely in terms of what they share. P is relevant to φ's internal structure, but whatever role it plays in implying ψ can be captured by a formula using only Q and R."

- question: "Beth's definability theorem states that if a predicate P is implicitly defined by a theory T, then:"
  type: multiple-choice
  options:
    - "P cannot be eliminated from T without changing which sentences T proves"
    - "P is explicitly definable by a formula in T's vocabulary not containing P"
    - "T must be categorical — having only one model up to isomorphism"
    - "P appears essentially in every axiom of T"
  answer: 1
  explanation: "Beth's theorem: implicit definability implies explicit definability. If T implicitly defines P (any two models of T agreeing on all non-P symbols must also agree on P's extension), then there is a formula φ(x) in T's P-free vocabulary such that T ⊢ ∀x(P(x) ↔ φ(x)). The proof uses Craig interpolation: implicit definability yields an entailment between two copies of T (one using P, one using renamed P'), and the shared vocabulary is everything except P and P'. The interpolant provides the explicit definition. This is the theorem's non-trivial content — semantic uniqueness forces syntactic expressibility."

- question: "For a given entailment φ ⊨ ψ, Craig's theorem guarantees exactly one interpolant — a unique sentence in the shared vocabulary mediating the entailment."
  type: true-false
  answer: false
  explanation: "The interpolant is not unique. Any sentence θ in the shared vocabulary satisfying φ ⊨ θ and θ ⊨ ψ qualifies. You could strengthen or weaken θ within the shared vocabulary and still have a valid interpolant, as long as it remains between φ and ψ in logical strength. Craig's theorem guarantees existence, not uniqueness. In practice, interpolants can vary enormously in complexity and form, which is why constructive interpolation proofs (extracting an interpolant from a proof of φ ⊨ ψ) are valuable — they produce a specific witness, but other witnesses also exist."

- question: "Craig's interpolation theorem applies to standard first-order logic but fails for some extensions, such as logics with generalized quantifiers."
  type: true-false
  answer: true
  explanation: "Craig interpolation is a property that first-order logic has and many of its extensions do not. Logics with generalized quantifiers (e.g., 'there exist infinitely many x such that...'), certain fragments of second-order logic, and various modal logics can fail interpolation — meaning there exist entailments φ ⊨ ψ for which no interpolant exists in the shared vocabulary. This failure is significant: it indicates that the entailment cannot be fully decomposed into shared content, revealing a structural difference between these logics and FOL. Interpolation is often treated as a robustness property that makes a logic well-behaved."

- question: "In your own words, what does Craig's interpolation theorem say about the 'common content' mediating a logical entailment between two sentences?"
  type: short-answer
  answer: "If φ logically implies ψ, then the connection between them can be fully expressed using only the vocabulary they share. There is always an intermediate sentence θ — the interpolant — that uses only the shared predicate, function, and constant symbols, such that φ implies θ and θ implies ψ. The symbols unique to φ and unique to ψ play no essential role in the logical relationship between them; the entailment is entirely 'carried' by the shared vocabulary."
  explanation: "This theorem reveals that logical entailment is local to shared content — two sentences cannot be logically connected through vocabulary that only one of them uses. It has practical applications in computer science (modular verification, where you check components share sufficient interface to guarantee a system property) and in philosophy of science (showing that theoretical terms linking two theories must have a common empirical content)."
```

## Explainer

You have studied FOL compactness — the theorem that a set of sentences has a model if every finite subset does — and the basics of model theory, including the connection between syntactic provability and semantic truth. **Craig's interpolation theorem** combines these to reveal something fundamental about how logical entailment works at the vocabulary level.

Start with an entailment: suppose φ ⊨ ψ (every model of φ is also a model of ψ). The vocabulary of φ might include predicate symbols P, Q, R, while ψ uses Q, R, S. The shared vocabulary is {Q, R}. Craig's theorem guarantees the existence of a sentence θ — the **interpolant** — using *only* the shared symbols Q and R, such that φ ⊨ θ and θ ⊨ ψ. The entailment from φ to ψ is mediated entirely through what they have in common; the symbols unique to each side play no essential role in the logical connection between them.

To appreciate why this is non-trivial, consider that φ might use P extensively in its internal structure. Yet when it comes to implying ψ, all the "work" that P does can be captured by a formula in the shared language. The proof typically proceeds by showing that the set of sentences in the shared vocabulary that φ implies and the set that ψ refutes are inconsistent — then using compactness or cut-elimination to extract the interpolant. The interpolant is not unique: many different sentences in the shared vocabulary can serve as the mediating step.

**Beth's definability theorem** is perhaps the most useful consequence. Suppose a predicate symbol P is **implicitly defined** by a theory T: any two models of T that agree on all non-P symbols must also agree on P's extension. Intuitively, P's meaning is "locked in" by the rest of the theory. Beth's theorem says P is then **explicitly definable** — there exists a formula in T's non-P vocabulary whose extension equals P's in every model. The proof uses Craig interpolation: implicit definability yields an entailment between two copies of T (one using P, one using a renamed copy P'), sharing only non-P vocabulary; the interpolant provides the explicit definition. Together, Craig and Beth show that first-order logic has no "hidden vocabulary" — any symbol that is semantically determined by a theory can be syntactically defined within that theory's language.
