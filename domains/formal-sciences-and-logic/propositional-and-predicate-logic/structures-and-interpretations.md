---
id: structures-and-interpretations
title: Structures and Interpretations
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: formulas-and-well-formed-expressions
  type: hard
- id: set-membership-and-notation
  type: soft
builds-toward:
- satisfaction-in-structures
- model-interpretation-and-satisfaction
tags:
- semantics
- models
- first-order-logic
stage: formal-systems
status: validated
---

# Structures and Interpretations

## Core Idea
A structure M consists of a non-empty domain D and an interpretation function I assigning to each constant a member of D, to each n-ary function symbol a function D^n → D, and to each n-ary predicate a relation on D^n. An interpretation specifies what symbols mean. The same formula can be true in some structures and false in others.

## How It's Best Learned
Construct small explicit models with finite domains. Evaluate formulas in them. Observe how changing a predicate's interpretation changes which formulas are satisfied.

## Questions

```yaml
- question: "The formula ∀x ∀y (R(x,y) → R(y,x)) is evaluated in two structures over the same domain D = {1, 2}. In structure M₁, R = {(1,2), (2,1)}. In structure M₂, R = {(1,2)}. What are the truth values?"
  type: multiple-choice
  options:
    - "True in both M₁ and M₂, because the formula is a logical tautology"
    - "False in both, because R is a binary relation and symmetry cannot be guaranteed"
    - "True in M₁ (R is symmetric) and false in M₂ (R(1,2) holds but R(2,1) does not)"
    - "The formula has no truth value until a domain is specified"
  answer: 2
  explanation: "In M₁, every pair (x,y) with R(x,y) has its mirror (y,x) also in R, so the formula is true. In M₂, R(1,2) holds but R(2,1) does not, making R(1,2) → R(2,1) false, so the universal is false. The same formula can be true or false depending on the structure — this is the core semantic fact of predicate logic. The formula is not a tautology; it expresses a contingent property (symmetry) that some structures satisfy and others do not."

- question: "A logician says: 'The formula ∀x P(x) is true.' What information is missing before you can agree or disagree?"
  type: multiple-choice
  options:
    - "The proof system being used to derive the formula"
    - "Whether P is a unary or binary predicate"
    - "Which structure is being used — the domain D and the interpretation of P"
    - "Whether the formula is in prenex normal form"
  answer: 2
  explanation: "∀x P(x) has no truth value until you specify a structure: a domain D and an interpretation of the predicate P as some subset of D. In the structure where D = {2,4,6} and P means 'is even,' the formula is true. In the structure where D = {1,2,3} and P means 'is even,' it is false (P(1) fails). Asking 'is the formula true?' without naming a structure is like asking 'is x > 0?' without specifying x."

- question: "A closed first-order formula is either true in all structures or false in all structures — there is no middle ground."
  type: true-false
  answer: false
  explanation: "Only logical tautologies (valid formulas) are true in every structure, and only contradictions are false in every structure. Most formulas are contingent — true in some structures and false in others. For example, ∃x ∃y (x ≠ y) is true in any domain with at least two elements but false in a singleton domain. The distinction between tautology, contingency, and contradiction is central to model theory."

- question: "Changing the interpretation of a predicate symbol in a structure can change whether a formula is satisfied in that structure."
  type: true-false
  answer: true
  explanation: "The satisfaction relation M ⊨ φ depends on both the domain and the interpretation function. If you change what predicate P means — that is, change which elements of D satisfy P — formulas involving P may flip from true to false or vice versa. This is why 'structure' bundles together both the domain and the interpretation: together they fully determine the truth value of every formula, and changing either component can change the outcome."

- question: "Explain why the formula ∀x ∀y (R(x,y) → R(y,x)) is not simply 'true' or 'false.' What determines its truth value? Give an example of one structure where it is true and one where it is false."
  type: short-answer
  answer: "The formula has no intrinsic truth value; it is only true or false relative to a specific structure — a non-empty domain D together with an interpretation of R as a binary relation on D. In a structure where D = {1,2} and R = {(1,2),(2,1)}, R is symmetric and the formula is true. In a structure where D = {1,2} and R = {(1,2)}, R is not symmetric (R(1,2) holds but R(2,1) does not), so the formula is false. The formula expresses the property of symmetry — whether R happens to be symmetric depends entirely on how R is interpreted."
  explanation: "This relativization of truth to structures is the defining move of model-theoretic semantics. It separates the syntactic formula (which is fixed) from its semantic evaluation (which depends on the structure). The same insight underlies the satisfiability and validity questions that drive much of formal logic and computer science."
```

## Explainer

When you first learned propositional logic, a truth assignment gave meaning to variables: "let P be true, let Q be false." In predicate logic, formulas talk about *objects* — "there exists an x such that..." or "for all x, if P(x) then Q(x)." To evaluate such formulas, you need to know what the objects are and what the predicates mean. That is precisely what a **structure** provides.

A **structure** M has two components. First, a **domain** D — a non-empty set of objects, the "universe" of discourse. This can be anything: the natural numbers, a set of five people, an abstract set {a, b, c}. Second, an **interpretation function** I that assigns concrete meanings to the non-logical symbols. For each constant symbol c, I(c) is a specific element of D. For each n-ary function symbol f, I(f) is an actual function Dⁿ → D. For each n-ary predicate symbol P, I(P) is a relation — a subset of Dⁿ. Together, D and I determine whether any closed formula is true or false.

Consider the formula ∀x ∀y (R(x,y) → R(y,x)). Over the domain D = {1, 2, 3} with R interpreted as the "less than" relation {(1,2), (1,3), (2,3)}, this formula is *false* — R(1,2) holds but R(2,1) does not. Change the interpretation of R to the equality relation {(1,1), (2,2), (3,3)}, and the same formula becomes *true*. The formula itself has not changed; only the structure has. This is the key insight: a formula is not true or false on its own — it is true or false *in a specific structure*.

From your prerequisite on well-formed expressions, you know how formulas are built syntactically from variables, connectives, and quantifiers. A structure provides the semantic layer that gives those formulas meaning. **Satisfaction** (M ⊨ φ) is the technical relation connecting structures and formulas: M satisfies φ when φ is true in M under the given interpretation. This opens the door to the central questions of model theory and formal semantics: which structures satisfy a given formula? Can we construct a structure that satisfies all the axioms of a given theory? Can two different structures satisfy exactly the same formulas? All of these questions are answered by reasoning carefully about how structures and interpretations work.
