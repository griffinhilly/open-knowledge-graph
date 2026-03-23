---
id: quantification-and-scope-formal
title: Quantification and Scope in Formal Semantics
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: lambda-calculus-for-linguistics
  type: hard
- id: montague-semantics
  type: hard
- id: quantifiers-and-scope
  type: hard
builds-toward:
- de-re-de-dicto-distinction
- type-theory-semantics
tags:
- semantics
- quantification
- scope
stage: expert
status: draft
---

# Quantification and Scope in Formal Semantics

## Core Idea
In formal semantics, quantifiers like 'all' and 'some' are treated as generalized quantifiers—functions from properties to truth values. Scope relationships determine the logical form of sentences: whether 'some' or 'all' takes wider scope changes truth conditions (e.g., 'Everyone loves someone' is ambiguous depending on which has wider scope). Formal accounts explain scope ambiguity, scope islands, and licensing of negative polarity items through the syntax-semantics interface.

## How It's Best Learned
Work through scope ambiguities with multiple quantifiers, computing truth conditions under each scope reading. Use lambda calculus to represent different scope assignments and verify when readings are equivalent or distinct.

## Common Misconceptions
- Scope is not purely linear left-to-right; surface word order does not determine all scope relations—structural position does.
- Not all apparent scope ambiguities are genuine; some depend on pragmatic or world-knowledge factors rather than semantic ambiguity.

## Questions

```yaml
- question: "Consider the sentence 'Every student read some book.' Under the inverse scope reading (some > every), which scenario would make this sentence TRUE while the surface scope reading (every > some) would be FALSE?"
  type: multiple-choice
  options:
    - "Each student read a different book, with no overlap among the books read"
    - "There is one specific book that every single student read"
    - "Some students read no books at all"
    - "Every student read at least two books"
  answer: 1
  explanation: "Surface scope (every > some) is true if each student read *some* book — possibly a different one for each student. Inverse scope (some > every) requires *one particular* book that every student read. Scenario B is true under inverse scope (there's a specific book all students read) but false under surface scope only when students DON'T all read the same book. This is why the two readings are genuinely distinct truth conditions, not paraphrases. The inverse scope reading is stronger — it entails the surface scope reading but not vice versa."

- question: "In generalized quantifier theory, what is the semantic type of an expression like 'every linguist'?"
  type: multiple-choice
  options:
    - "An individual of type e, referring to the set of linguists"
    - "A predicate of type ⟨e,t⟩, true of each individual linguist"
    - "A function from properties to truth values, of type ⟨⟨e,t⟩,t⟩"
    - "A second-order predicate that ranges over sets of individuals"
  answer: 2
  explanation: "Generalized quantifier theory treats quantifier phrases as functions from properties (type ⟨e,t⟩) to truth values (type t). 'Every linguist' denotes: λP. ∀x[linguist(x) → P(x)]. This function takes any property P and returns true iff every linguist has that property. This type-theoretic treatment is what allows quantifiers to compose uniformly with the rest of the grammar and is the foundation for analyzing scope ambiguity. Option D (second-order predicate) describes the Fregean approach, which generalized quantifier theory supersedes."

- question: "The two scope readings of 'Every student read some book' — every > some and some > every — are merely stylistic paraphrases that express the same truth conditions."
  type: true-false
  answer: false
  explanation: "This is the key misconception to avoid. The readings have genuinely different truth conditions. Under every > some (surface): for each student, there exists some book they read (different students may have read different books). Under some > every (inverse): there is one particular book that every student read. These can differ in truth value — surface scope can be true while inverse scope is false (if every student read different books). The readings are logically independent, not paraphrases."

- question: "Scope relationships in natural language sentences are fully determined by surface word order — the leftmost quantifier always takes widest scope."
  type: true-false
  answer: false
  explanation: "Surface word order correlates with scope preferences but does not determine scope. Quantifier Raising (QR) at Logical Form allows quantifiers to move covertly and take scope over elements to their left in surface structure. Scope islands (relative clauses, that-clauses, adjuncts) can prevent expected scope taking by trapping quantifiers inside syntactic boundaries — independent of word order. Left-to-right linearity is a default, not a rule."

- question: "Why can scope not simply be read off from surface word order, and what syntactic mechanism do formal semanticists posit to account for inverse scope readings?"
  type: short-answer
  answer: "Surface order reflects where quantifiers appear in the phonological string, but scope is determined at Logical Form (LF), a covert syntactic level. At LF, quantifiers can undergo Quantifier Raising (QR): they move out of their surface position and adjoin higher in the tree, leaving a trace behind. The relative height of two quantifiers at LF — not their surface linear order — determines which takes wider scope. QR is a genuine syntactic operation constrained by the same island conditions that govern overt movement, which is why scope islands (relative clauses, embedded questions) block inverse scope just as they block overt wh-movement."
  explanation: "The connection between scope islands and movement islands is the strongest evidence that QR is a real syntactic operation. If scope were purely semantic (a pragmatic phenomenon with no syntax), there would be no reason for it to respect the same syntactic boundaries that constrain overt movement. The fact that it does suggests that the grammar computes scope through actual (covert) structural manipulation, not just semantic combination."
```

## Explainer

From your study of lambda calculus for linguistics, you can represent the meaning of a sentence as a function application: the meaning of a verb phrase is a function, the meaning of a noun phrase argument is an input, and the result is a truth value or a proposition. From Montague semantics, you know how to compose meanings compositionally: complex expressions are interpreted by combining the interpretations of their parts according to their syntactic structure. From your work on quantifiers and scope, you know that expressions like *every*, *some*, and *no* are not referring expressions (they don't pick out specific individuals) but operators that relate sets. This topic puts those tools together to handle the formal treatment of scope ambiguity — one of the most revealing puzzles in the semantics-syntax interface.

The key theoretical move is **generalized quantifier theory**: quantifiers are not treated as second-order predicates in Frege's sense but as **functions from properties to truth values**. "Every student left" is analyzed as: the quantifier *every student* denotes a function that, given the property *left*, returns true iff every individual in the student-set has that property. In lambda notation: `λP. ∀x[student(x) → P(x)]`. This type-theoretic treatment lets quantifiers compose uniformly with the rest of the grammar. "Some professor wrote every book" now involves two quantifiers, each of type `⟨⟨e,t⟩,t⟩`, and their relative **scope** — which takes wider scope — determines the truth conditions.

The ambiguity in "Every student read some book" is the canonical example. Under the **surface scope** reading (every > some): for every student, there is (possibly a different) some book that they read. Under the **inverse scope** reading (some > every): there is one particular book such that every student read it. These are genuinely different truth conditions, not just paraphrases. The mechanism that generates inverse scope in formal accounts is **Quantifier Raising (QR)**: at Logical Form (LF), quantifiers can covertly move out of their surface position, leaving a trace, and bind a variable from an adjoined position. The relative scope of two quantifiers is determined by their positions at LF, not their surface order. This is why scope is not a simple left-to-right affair — it depends on movement in the covert syntactic component.

**Scope islands** are the empirical constraints that prevent QR from applying arbitrarily. A quantifier cannot move out of certain syntactic boundaries: relative clauses, *that*-clauses, questions, and adjuncts tend to be scope islands, meaning a quantifier trapped inside one cannot take scope over something outside. "The man who bought every book left" does not have a reading where *every book* takes scope over the entire sentence — it is frozen inside the relative clause. These constraints are not arbitrary; they correlate with the same boundaries that block overt syntactic movement (island constraints from wh-movement studies), suggesting that QR is a genuine syntactic operation constrained by the same grammar.

**Negative polarity items (NPIs)** like *any* and *ever* show one of the most striking scope-sensitive licensing patterns: they require a **downward-entailing** (DE) context — a context where inferences go from sets to subsets. "She didn't eat anything" is fine because negation creates a DE context. "She ate something" does not license *any* because affirmation is upward-entailing. Formally, a DE context is one where if P entails Q, then DP-operator(Q) entails DP-operator(P). Generalized quantifier theory makes this formally precise and explains why *every* creates a DE context in its restrictor but not its nuclear scope — which correctly predicts that "Every student who ever studied linguistics passed" is fine (*any/ever* licensed in the DE restrictor) while "Every student passed any exam" is not.
