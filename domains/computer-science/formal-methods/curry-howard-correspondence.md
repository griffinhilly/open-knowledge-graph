---
id: curry-howard-correspondence
title: Curry-Howard Correspondence
domain: computer-science
course: formal-methods
prerequisites:
- id: propositional-logic-introduction
  type: hard
- id: type-systems-overview
  type: hard
- id: predicate-logic-introduction
  type: soft
builds-toward:
- interactive-theorem-proving
- dependent-type-theory
tags:
- propositions-as-types
- proofs-as-programs
- isomorphism
- constructive-logic
stage: expert
status: validated
---
# Curry-Howard Correspondence

## Core Idea
The Curry-Howard correspondence is a deep isomorphism between logic and computation: propositions correspond to types, proofs correspond to programs, and proof normalization corresponds to program evaluation. An implication A -> B is a function type; a proof of A -> B is a function that takes a proof of A and produces a proof of B. A conjunction A AND B is a product type (pair); a disjunction A OR B is a sum type (tagged union). Under this correspondence, type-checking IS proof-checking — a well-typed program is simultaneously a valid proof. This insight unifies logic, type theory, and programming language theory into a single framework.

## Questions

```yaml
- question: "Under the Curry-Howard correspondence, what does a value of type A -> B correspond to in logic?"
  type: multiple-choice
  options:
    - "A proof that A is false and B is true"
    - "A proof of the implication 'A implies B' — a function that transforms any proof of A into a proof of B"
    - "A proof that A and B are equivalent"
    - "A disproof of A"
  answer: 1
  explanation: "A function of type A -> B takes an input of type A and produces an output of type B. Under Curry-Howard, this is exactly a proof of 'A implies B': given a proof of A (the input), it constructs a proof of B (the output). The function IS the proof — not a description of a proof, but the proof itself, embodied as a computational object. This is why proof assistants like Coq represent proofs as typed lambda-calculus terms."

- question: "Under the Curry-Howard correspondence, a type with no inhabitants (no values of that type) corresponds to a proposition that is unprovable."
  type: true-false
  answer: true
  explanation: "If a type T has no inhabitants (no well-typed closed terms of type T exist), then under Curry-Howard, the corresponding proposition has no proof — it is unprovable. The empty type (Void, or False in Coq) has no constructors and no values, corresponding to a logical falsehood. Conversely, a type with at least one inhabitant corresponds to a provable proposition. This is why type inhabitation and provability are the same question viewed from different angles."

- question: "Explain why the Curry-Howard correspondence works with constructive (intuitionistic) logic rather than classical logic, and what this means for the law of excluded middle."
  type: short-answer
  answer: "The correspondence naturally aligns with constructive logic because a proof of 'A or B' must provide either a proof of A or a proof of B (corresponding to constructing either a Left or Right value of a sum type). Classical logic's law of excluded middle (A or not A) would require a program that, for any proposition A, decides whether A is true or false — which is not computable in general. Classical reasoning can be recovered by adding axioms (corresponding to non-constructive language features like continuations), but the direct correspondence is with constructive logic."
  explanation: "This is not merely a technical limitation but a philosophical point. Constructive logic requires that existence claims be witnessed by explicit constructions: to prove 'there exists an x such that P(x)', you must produce a specific x. Under Curry-Howard, this means a proof of an existential is a pair (witness, proof), which is a dependent pair type. Classical logic allows proving existence without a witness (by contradiction), which has no direct computational interpretation. The Curry-Howard correspondence reveals that constructive logic IS computation."

- question: "If proof normalization corresponds to program evaluation under Curry-Howard, what does a non-terminating program correspond to in logic?"
  type: short-answer
  answer: "A non-terminating program corresponds to a 'proof' that never reaches a normal form — effectively a circular or infinite argument that does not actually establish its conclusion. In a consistent logic, proofs of false (the empty type) should not exist, but a non-terminating program of type False would inhabit the empty type, making the logic inconsistent. This is why proof assistants like Coq require all functions to terminate (total functions only), ensuring the logic remains consistent."
  explanation: "This is a critical design constraint for proof assistants. General recursion allows writing fix f. f : A for any type A, which would 'prove' any proposition including False. By restricting to terminating programs (via structural recursion, well-founded recursion, or termination checkers), the system ensures that every type inhabitant is a genuine proof. The tension between expressiveness and consistency — between being a useful programming language and a sound logic — is a central challenge in dependent type theory."
```

## Explainer

The Curry-Howard correspondence, discovered independently by Haskell Curry (1930s-1950s) and William Howard (1969), reveals that two seemingly different intellectual traditions — mathematical logic and the theory of computation — are actually the same thing viewed from different perspectives. The correspondence is not a loose analogy but a precise, structural isomorphism: every concept in one domain has an exact counterpart in the other.

The basic dictionary is this: **propositions are types**, **proofs are programs**, and **proof simplification is computation**. The logical connective "A implies B" corresponds to the function type A -> B. A proof of "A implies B" is a function that takes a proof of A and returns a proof of B. The connective "A and B" corresponds to the product type (A, B) — a pair. A proof of a conjunction is a pair of proofs, one for each conjunct. "A or B" corresponds to the sum type A + B (a tagged union). A proof of a disjunction provides one of the two proofs, tagged with which disjunct it proves. "False" corresponds to the empty type (no inhabitants). "True" corresponds to the unit type (one trivial inhabitant).

This correspondence is constructive: it aligns with **intuitionistic (constructive) logic**, not classical logic. In constructive logic, proving "A or B" requires actually producing a proof of A or a proof of B — you cannot just argue by contradiction. Under Curry-Howard, this makes sense: constructing a value of type A + B requires producing either a Left(a) or a Right(b). The classical **law of excluded middle** (A or not A) would require a program that, for any type A, either produces a value of A or a function A -> Void — which is not computable in general. Classical reasoning can be added to the correspondence (it corresponds to control operators like call/cc), but the natural alignment is with constructive logic.

The correspondence extends to quantifiers via **dependent types**. The universal quantifier "for all x : A, B(x)" corresponds to a dependent function type (x : A) -> B(x): a function that takes an x of type A and produces a value of type B(x), where the output type depends on the input value. The existential quantifier "there exists x : A such that B(x)" corresponds to a dependent pair type (x : A, B(x)): a pair of a witness x and a proof that B(x) holds. This extension takes Curry-Howard from propositional logic to full predicate logic and is the foundation of dependent type theory and proof assistants like Coq, Lean, and Agda.

The practical import is profound. **Proof assistants** implement the correspondence directly: you prove theorems by writing programs in a dependently-typed language, and type-checking IS proof-checking. When Coq accepts a term of a given type, it has mechanically verified that the corresponding proposition is true. The correspondence also explains why **termination matters**: a non-terminating program of type A would "prove" A regardless of whether A is actually true, collapsing the logic into inconsistency. This is why proof assistants restrict to total (terminating) functions, ensuring that every type inhabitant is a genuine proof.
