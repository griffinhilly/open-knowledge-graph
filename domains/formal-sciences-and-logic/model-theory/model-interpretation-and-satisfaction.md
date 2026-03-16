---
id: model-interpretation-and-satisfaction
title: Model Interpretation and Satisfaction
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: structures-and-formal-languages
  type: hard
- id: first-order-semantics
  type: hard
- id: set-membership-and-notation
  type: soft
- id: set-fundamentals
  type: soft
- id: relations-as-set-subsets
  type: soft
- id: set-theory-basics
  type: soft
- id: functions-and-mappings-formal
  type: soft
builds-toward:
- elementary-equivalence-indistinguishability
- complete-first-order-theories
tags:
- semantics
- satisfaction
- truth
- Tarski
- valuation
stage: advanced
status: draft
---

# Model Interpretation and Satisfaction

## Core Idea
Satisfaction formalizes what it means for a formula to be true in a structure through recursive definition: atomic formulas are satisfied by checking the actual interpretation; logical connectives and quantifiers are evaluated inductively. A model of a set of sentences is a structure in which all sentences are satisfied. This Tarskian framework unifies logic and mathematics under a single unified notion of truth.

## Questions

```yaml
- question: "According to Tarski's definition, the existential sentence ∃x P(x) is satisfied in a structure M if and only if:"
  type: multiple-choice
  options:
    - "The predicate symbol P appears in M's signature"
    - "Every element of M's domain satisfies P(x)"
    - "At least one element of M's domain satisfies P(x) under some variable assignment"
    - "P names a non-empty set in every structure with the same signature"
  answer: 2
  explanation: "Tarski's clause for the existential quantifier says ∃x φ(x) is satisfied in M iff there exists some element d in the domain of M such that M satisfies φ(x) with x assigned to d. Only one witness is needed. Option B describes universal quantification (∀x P(x)). Options A and D are not truth conditions for satisfaction in a specific structure."

- question: "A structure M is a model of sentence φ if and only if φ is logically valid — that is, true in all structures."
  type: true-false
  answer: false
  explanation: "M ⊨ φ (M models φ) means φ is satisfied specifically in M — the actual objects of M's domain, under M's interpretation of symbols, make φ true. Logical validity (⊨ φ) is a strictly stronger condition meaning φ holds in every structure. A sentence like 'the domain has exactly 3 elements' can be true in some structures and false in others — it is satisfiable but not valid."

- question: "What distinguishes the satisfaction clause for an atomic formula from the satisfaction clause for a compound formula in Tarski's framework?"
  type: short-answer
  answer: "An atomic formula is satisfied by directly consulting the interpretation: check whether the tuple of objects denoted by the terms actually stands in the relation that the predicate symbol denotes in M. A compound formula is satisfied inductively: its truth is reduced to the truth of its simpler sub-formulas using the truth conditions of the connective or quantifier at the outermost level."
  explanation: "This reflects the architecture of Tarski's definition: base cases (atomic formulas) anchor the recursion by grounding truth in the actual domain, and the inductive clauses (for ¬, ∧, ∨, →, ∀, ∃) assemble truth for complex formulas from truth values already computed for simpler ones. The recursion bottoms out at atoms — there is no further decomposition possible."
```

## Explainer

From your study of first-order semantics, you know that a structure provides the raw material for evaluating first-order formulas: a non-empty domain, an assignment of domain elements to constant symbols, functions on the domain to function symbols, and relations on the domain to predicate symbols. Model theory's central question is: when exactly does a formula become *true* in a given structure? Tarski's satisfaction relation, written M ⊨ φ, gives a precise, recursive answer.

The definition proceeds in two stages. For atomic formulas — the simplest kind, like P(a) or a = b — satisfaction is checked directly against the interpretation. P(a) is satisfied in M iff the element that a denotes in M is in the set that P denotes in M. This is just checking a fact about the structure itself: does the named object have the named property? There is no logical decomposition to do; truth is read off from the model.

For compound formulas, satisfaction is defined inductively by the outermost connective or quantifier. M ⊨ ¬φ iff M does not satisfy φ. M ⊨ φ ∧ ψ iff M satisfies both φ and ψ. M ⊨ ∃x φ(x) iff there exists at least one element d in the domain such that the structure with x assigned to d satisfies φ. M ⊨ ∀x φ(x) iff every element d in the domain satisfies φ when x is assigned to d. Each clause reduces the truth of a complex formula to truth of simpler subformulas, until atomic cases are reached.

A common confusion is between satisfiability and validity. Saying M ⊨ φ (φ is true in the specific structure M) is different from saying ⊨ φ (φ is true in *every* structure — it is logically valid). A sentence can be true in some structures and false in others. A theory T is a set of sentences; M is a model of T when M ⊨ φ for every φ in T. The existence of a model witnesses that T is consistent — since contradiction is false in every structure, a model shows T cannot derive contradiction.

This framework is more powerful than it first appears. By varying what a structure looks like while holding sentences fixed, or by varying sentences while holding a structure fixed, you can ask questions like: do two structures satisfy exactly the same sentences? Does a theory have a model of every infinite cardinality? These are the questions that drive the deeper theorems of model theory — but they all rest on Tarski's foundational definition of what it means for a formula to be satisfied in a structure.
