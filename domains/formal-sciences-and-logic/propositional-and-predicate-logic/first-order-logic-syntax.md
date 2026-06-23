---
id: first-order-logic-syntax
title: First-Order Logic Syntax
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
- id: predicates-and-quantifiers
  type: hard
- id: negation-of-quantifiers
  type: hard
- id: set-membership-and-notation
  type: soft
- id: set-fundamentals
  type: soft
- id: functions-and-function-properties
  type: soft
- id: relations-as-set-subsets
  type: soft
- id: predicate-logic-introduction
  type: soft
builds-toward:
- first-order-semantics
- natural-deduction-fol
- formal-arithmetic-and-expressibility
tags:
- first-order-logic
- quantifiers
- variables
- terms
- formulas
- FOL
stage: formal-systems
status: validated
---

# First-Order Logic Syntax

## Core Idea
First-order logic (FOL) extends propositional logic with terms (variables, constants, function symbols applied to terms) and atomic formulas (predicate symbols applied to terms). Quantifiers ∀ (for all) and ∃ (there exists) bind variables, giving rise to the distinction between free and bound occurrences. A sentence is a formula with no free variables. The language of a first-order theory is specified by its signature: a collection of constant, function, and predicate symbols with their arities. Different signatures yield different logical languages (e.g., the language of arithmetic vs. the language of set theory).

## How It's Best Learned
Practice translating English statements into FOL and back. Carefully track variable scope to distinguish bound and free occurrences. Build formulas of increasing complexity from simple atomic predicates.

## Common Misconceptions
- Quantifiers bind variables, not predicates — ∀x P(x) quantifies over the domain, not over predicates.
- Free variables in a formula are implicitly universally quantified in some contexts but not others; always be explicit about scope.

## Questions

```yaml
- question: "In the formula ∀x (P(x) → Q(x, y)), which variables are free?"
  type: multiple-choice
  options: ["x only", "y only", "both x and y", "neither — both are bound"]
  answer: 1
  explanation: "The quantifier ∀x binds every occurrence of x within its scope (the entire subformula P(x) → Q(x, y)). The variable y appears inside that scope but is not bound by any quantifier, so y is free. A variable is bound if and only if it falls within the scope of a quantifier that names it."

- question: "In the formula ∃x P(x) ∧ Q(x), nearly every occurrence of x is bound by the existential quantifier."
  type: true-false
  answer: false
  explanation: "The scope of ∃x is only the immediately following formula P(x), not the entire conjunction. The x in Q(x) is outside that scope and is therefore free. If you wanted to bind both occurrences, you would write ∃x (P(x) ∧ Q(x)) with explicit parentheses to extend the scope."

- question: "What distinguishes a sentence from an open formula in first-order logic?"
  type: short-answer
  answer: "A sentence has no free variables — every variable is bound by a quantifier. An open formula has at least one free variable."
  explanation: "Sentences have definite truth values relative to a model because they make no unresolved reference to external variable assignments. Open formulas like P(x) can only be evaluated once x is assigned a value from the domain. This distinction is crucial: logical consequence and validity are defined for sentences."
```

## Explainer

In propositional logic, the basic units were atomic propositions like P and Q — whole claims that were either true or false. First-order logic is more expressive: it lets you talk about *objects*, their *properties*, and *relations* between them, and it lets you make claims about *all* or *some* objects in a domain. To do this, it introduces a new kind of syntax built from three layers: terms, atomic formulas, and compound formulas with quantifiers.

Terms are the expressions that refer to objects. A constant like `alice` or `0` refers to a specific object. A variable like `x` is a placeholder that can range over objects in the domain. A function symbol applied to terms — like `father(alice)` or `s(0)` — builds a new term by applying an operation to existing ones. Terms are *not* true or false; they just denote things. Predicates, by contrast, take terms as arguments and produce truth values: `Loves(alice, bob)` or `Prime(3)` are atomic formulas — the smallest units that can be true or false.

Quantifiers are what make first-order logic genuinely more powerful than propositional logic. ∀x φ(x) asserts that φ holds for every object in the domain; ∃x φ(x) asserts that at least one object satisfies φ. The critical concept is *scope*: the quantifier ∀x binds occurrences of x within the subformula it governs. If you write ∀x P(x) ∧ Q(x), the scope of ∀x is only P(x) — the x in Q(x) is *free* (unbound). This is identical to the scoping rules for variables in programming languages, and that analogy is a reliable guide.

The signature of a first-order theory specifies what vocabulary is available: which constant, function, and predicate symbols exist and how many arguments each takes (its arity). The same syntax rules apply to every first-order language, but different signatures yield different languages — the language of arithmetic uses 0, s (successor), +, × and =; the language of set theory uses only ∈. Understanding the signature tells you which atomic formulas are even well-formed before you worry about what they mean.

A formula is a *sentence* if it has no free variables. Sentences have definite truth values in a model; open formulas only acquire truth values once the free variables are assigned values. When you read or write FOL, always track which variables are bound and which are free — this is the most common source of syntax errors and the foundation for everything in semantics and proof theory that follows.
