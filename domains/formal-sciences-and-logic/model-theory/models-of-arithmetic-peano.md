---
id: models-of-arithmetic-peano
title: Models of Peano Arithmetic and Non-Standard Models
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: formal-arithmetic-and-expressibility
  type: hard
- id: complete-first-order-theories
  type: soft
- id: arithmetic-functions-and-multiplicativity
  type: soft
builds-toward:
- undecidability-and-godel
- omitting-types-theorem-countable
tags:
- peano-arithmetic
- non-standard-models
- arithmetic
stage: advanced
status: draft
---

# Models of Peano Arithmetic and Non-Standard Models

## Core Idea
Peano arithmetic (PA) has non-standard models: countably infinite models satisfying all PA axioms but containing infinite integers beyond all standard numerals. Every non-standard model contains a copy of the standard natural numbers followed by a densely ordered structure of infinitely large elements. Non-standard models demonstrate that first-order logic cannot axiomatize arithmetic uniquely.

## How It's Best Learned
Construct a non-standard model using the compactness theorem by adding a constant c and axioms c > n for all numerals n. Study the structure of the infinite part.

## Questions

```yaml
- question: "A student argues: 'If we take all first-order sentences that are true in the standard natural numbers ℕ and add them as axioms, the resulting theory will be categorical — its only model will be ℕ.' What does model theory say about this claim?"
  type: multiple-choice
  options:
    - "The claim is correct — a complete first-order theory with a unique infinite model is categorical"
    - "The claim fails: even adding all true sentences of ℕ produces a complete theory, but the Löwenheim-Skolem theorem guarantees it still has models of every infinite cardinality — including non-standard countable models"
    - "The claim fails because no consistent first-order theory can have ℕ as a model"
    - "The claim is correct for countable models, but uncountable non-standard models would still exist"
  answer: 1
  explanation: "The theory of 'true arithmetic' — all first-order sentences true in ℕ — is complete (every sentence is decided) but not categorical. The upward Löwenheim-Skolem theorem guarantees models of every uncountable cardinality, and compactness (plus downward L-S) guarantees countable non-standard models. Categoricity in first-order logic requires finiteness — no infinite structure is characterizable up to isomorphism by a first-order theory. The standard model ℕ is unique up to isomorphism only in second-order logic, not first-order logic. This is the fundamental limitation being exposed."

- question: "Using the compactness theorem, a logician builds a non-standard model M of PA containing a non-standard element c greater than all standard naturals. What can be said about the element c + 1 in M?"
  type: multiple-choice
  options:
    - "c + 1 = 0, since PA arithmetic wraps around at infinite elements — non-standard models have modular structure"
    - "c + 1 is another non-standard element, greater than all standard naturals and greater than c"
    - "c + 1 is undefined, since PA's successor function is only defined for finite elements"
    - "c + 1 = c, since adding 1 to an infinite element leaves it unchanged"
  answer: 1
  explanation: "M is a model of PA, so all PA axioms hold in M — including the axiom that every element has a successor, and that the successor of x is x+1 > x. Since c > n for all standard naturals n, and c+1 > c, it follows that c+1 > n for all standard naturals as well. c+1 is a distinct non-standard element larger than c. The non-standard elements don't wrap around (that would violate the PA axiom that no element equals its own successor) and they don't collapse (that would violate the strict ordering axioms). The non-standard part forms a dense collection of ℤ-copies extending infinitely in both directions."

- question: "Every model of Peano Arithmetic is isomorphic to the standard natural numbers ℕ."
  type: true-false
  answer: false
  explanation: "This is the central misconception the topic addresses. Non-standard models of PA exist — they satisfy every PA axiom but contain elements greater than all standard naturals. The compactness construction (add constant c with axioms c > n for each standard numeral n) proves this directly. The standard naturals form an initial segment of any model of PA, but non-standard models extend beyond this with a dense collection of 'blocks' isomorphic to ℤ. First-order logic cannot categorically axiomatize ℕ — only second-order PA (with genuine set-quantification in induction) achieves categoricity."

- question: "Non-standard models of Peano Arithmetic satisfy all theorems provable in PA, but they may disagree with ℕ on sentences that are true in ℕ but unprovable from PA."
  type: true-false
  answer: true
  explanation: "A model of PA, by definition, satisfies every consequence of the PA axioms — including every provable theorem. Non-standard models are models, so they satisfy everything PA proves. The disagreement with ℕ occurs precisely on the sentences that PA cannot prove or disprove: unprovable truths of ℕ. Gödel's incompleteness theorem guarantees such sentences exist (in fact, there are true sentences of ℕ that no consistent recursively axiomatizable extension of PA can prove). Non-standard models witness this incompleteness — they are alternative models where those unprovable sentences happen to be false."

- question: "Why can't the induction schema in Peano Arithmetic rule out non-standard models? What limitation of first-order logic does this expose?"
  type: short-answer
  answer: "First-order induction only quantifies over properties expressible by first-order formulas in the language of PA. To rule out non-standard elements, you would need to express: 'the set of natural numbers is exactly the smallest set containing 0 and closed under successor.' But 'smallest set' requires second-order quantification over all subsets. First-order induction gives you: for each specific first-order formula φ, if φ(0) and φ(n) → φ(n+1), then ∀n φ(n). A non-standard element c satisfies all these individual induction instances, because no single first-order formula can define 'the standard naturals' in a way that excludes c."
  explanation: "This exposes the expressive limitation of first-order logic: it cannot quantify over all subsets of the domain, only over individual elements. The 'intended model' argument — that ℕ is the unique minimal model of PA — requires second-order reasoning about what the 'smallest' closure under successor is. First-order logic cannot capture minimality of infinite structures. This is why second-order PA (where the induction axiom genuinely quantifies over all subsets) is categorical for ℕ, while first-order PA is not. The gap between these two is the gap between categoricity and incompleteness."
```

## Explainer

From your study of formal arithmetic and first-order logic, you know that Peano Arithmetic (PA) is a first-order theory with axioms for zero, successors, addition, and multiplication, plus an induction schema. You may have hoped these axioms uniquely pin down the natural numbers ℕ. The existence of **non-standard models** is the fundamental theorem showing they do not — and cannot.

The construction of a non-standard model is a direct application of the **compactness theorem**. Extend the language of PA with a new constant symbol c, and add the sentences c > 0, c > 1, c > 2, ... for every standard numeral. Each finite subset of these axioms is satisfiable (interpret c as a sufficiently large standard number). By compactness, the entire extended theory is satisfiable, producing a model M in which c is an "infinite integer" — greater than every standard natural number, yet satisfying all PA axioms. The elements corresponding to standard natural numbers form an initial segment isomorphic to ℕ, but M contains additional **non-standard elements** beyond this segment.

The structure of the non-standard part is illuminating. Every non-standard element z satisfies z > n for all standard n, yet z − 1, z − 2, ... are also elements of M, stretching infinitely in both directions within the non-standard region. The non-standard elements form a **densely ordered collection of copies of ℤ** — each "block" is isomorphic to the integers, and the blocks themselves have no least or greatest element. This contrasts sharply with the discrete, well-ordered structure of the standard naturals. PA's induction schema does not rule this out, because first-order induction only quantifies over properties *expressible in first-order logic* — and first-order logic cannot single out the standard model from among all its non-standard cousins.

The philosophical consequence is profound: **first-order logic cannot categorically axiomatize arithmetic**. No matter what first-order sentences you add to PA (as long as they are all true in ℕ), the resulting theory will still have non-standard models. This follows from the Löwenheim-Skolem theorem and compactness: any first-order theory with an infinite model has models of every infinite cardinality, and even among countable models, non-standard ones exist. The "true arithmetic" — the set of all first-order sentences true in ℕ — is not recursively axiomatizable (by Gödel's incompleteness theorem), and non-standard models witness exactly this gap: they satisfy every provable sentence but disagree with ℕ on some unprovable truths.
