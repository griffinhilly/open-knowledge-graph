---
id: quantifier-notation-and-basics
title: Quantifier Notation and Basic Semantics
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: predicates-and-relations-fol
  type: hard
- id: set-fundamentals
  type: hard
- id: set-operations
  type: hard
- id: domain-and-range
  type: soft
- id: set-membership-and-notation
  type: soft
- id: all-some-none
  type: soft
- id: universal-and-existential-statements
  type: hard
builds-toward:
- universal-quantifier-semantics
- existential-quantifier-semantics
- free-variables-and-bound-variables
tags:
- syntax
- semantics
- quantifiers
stage: formal-systems
status: validated
---

# Quantifier Notation and Basic Semantics

## Core Idea
The universal quantifier ∀ (for all) and existential quantifier ∃ (there exists) express generality and existence. ∀x P(x) means 'for every object x, P holds'; ∃x P(x) means 'there is at least one object x for which P holds'. Quantifiers bind variables and determine scope.

## How It's Best Learned
Translate between English phrases ('all dogs bark', 'some cats are black') and formal quantified formulas. Practice recognizing quantifier scope and how scope affects meaning.

## Questions

```yaml
- question: "Over the domain of integers, which of the following statements is TRUE?"
  type: multiple-choice
  options:
    - "∃y ∀x (y > x) — there exists an integer greater than all integers"
    - "∀x ∃y (y = x + 1) — for every integer, there exists an integer exactly one greater"
    - "∀x ∀y (x < y) — every integer is strictly less than every other integer"
    - "∃x ∀y (x < y) — there exists a smallest integer"
  answer: 1
  explanation: "∀x ∃y (y = x + 1) is true: for any integer x, choose y = x + 1, which satisfies the predicate. The key is that y is chosen after and in terms of x — the existential witness can depend on the universal variable. The other three are false: the integers have no maximum (ruling out option A), no pair satisfies x < y for all y simultaneously (option C), and the integers are unbounded below with no smallest member (option D)."

- question: "The formula ∃x (x² = 2) changes truth value depending on the domain of discourse. Over which domain is it TRUE?"
  type: multiple-choice
  options:
    - "The natural numbers ℕ, since 1² = 1 and 2² = 4 bracket the value 2"
    - "The integers ℤ, since both positive and negative values are available"
    - "The real numbers ℝ, since √2 is a real number satisfying (√2)² = 2"
    - "The rational numbers ℚ, since √2 can be approximated arbitrarily closely by rationals"
  answer: 2
  explanation: "√2 is irrational, so it belongs to neither ℕ, ℤ, nor ℚ. The formula is false over all three of those domains — no element in any of them squares to exactly 2. Over ℝ, the number √2 exists as a real number and satisfies the predicate, making the formula true. This illustrates that quantifiers always range over a specific domain of discourse: the same formula can be true in one domain and false in another, so specifying the domain is part of giving a quantified formula a meaning."

- question: "In the formula ∀x P(x), substituting a different variable name produces a logically different formula — for instance, ∀z P(z) says something distinct from ∀x P(x)."
  type: true-false
  answer: false
  explanation: "False. Bound variables are mere placeholders (dummy variables). The quantifier ∀ binds the variable, and the specific letter chosen carries no semantic content — ∀x P(x) and ∀z P(z) say exactly the same thing: 'for every object in the domain, P holds.' This is analogous to how ∫₀¹ x dx and ∫₀¹ t dt compute the same integral. Only *free* variables — those not bound by any quantifier — carry meaning and affect a formula's truth value under an interpretation."

- question: "Swapping the order of two different quantifiers in a formula (∀ and ∃) can change whether the formula is true or false."
  type: true-false
  answer: true
  explanation: "True, and this is among the most important structural facts about quantifiers. ∀x ∃y (y > x) says 'for every integer, there is a larger one' — true, since for any x choose y = x + 1. ∃y ∀x (y > x) says 'there exists a single integer larger than every integer' — false, since the integers are unbounded. In the first formula, the existential witness y can depend on the specific choice of x; in the second, one fixed y must exceed all x simultaneously. This dependency structure is precisely what quantifier order encodes."

- question: "Explain in your own words why ∀x ∃y (y > x) and ∃y ∀x (y > x) make fundamentally different claims, and identify which is true over the integers."
  type: short-answer
  answer: "∀x ∃y (y > x) says: for each integer x you choose, I can find some y greater than it. The y is allowed to depend on x — for x = 5, pick y = 6; for x = 1000, pick y = 1001. This is true over the integers. ∃y ∀x (y > x) says: there exists a single fixed y that is greater than every integer simultaneously. This is false, because the integers are unbounded — no finite number exceeds all of them. The order controls whether the existential witness can depend on the universal variable."
  explanation: "The key distinction is dependency: in ∀x ∃y φ(x, y), the witness for y is chosen after x is fixed and may depend on x. In ∃y ∀x φ(x, y), y must be fixed before x ranges over the domain, so one y must satisfy the predicate for every possible x at once. This dependence structure is invisible when the formulas are read in loose English ('for all x there exists y' vs 'there exists y for all x') but is exactly what the quantifier order encodes formally."
```

## Explainer

You already know what a predicate is: a property P(x) that is either true or false for each object x in some domain. Predicates by themselves make claims about specific objects — P(alice) says Alice has property P. Quantifiers lift this to claims about *all* or *some* objects in the domain at once, without naming any of them.

The **universal quantifier** ∀ is a logical "for all." The formula ∀x P(x) means: pick any object x from the domain — P holds. It is equivalent to the conjunction of P over every element, but without having to enumerate them. If your domain is the integers, ∀x (x + 0 = x) says that adding zero is a right identity for every integer. The connection to sets you already know: ∀x P(x) is true in a domain D precisely when the extension of P — the set {x ∈ D : P(x)} — equals the entire domain D.

The **existential quantifier** ∃ is the logical "there exists." The formula ∃x P(x) means: at least one object in the domain satisfies P. It is the disjunction of P over every element. If your domain is the integers, ∃x (x² = 2) is false over the integers (no integer squares to 2) but true over the reals. Notice that the *same sentence* changes truth value when the domain changes — quantifiers always range over a specific **domain of discourse**, and specifying that domain is part of giving a formula a meaning.

**Scope** and **variable binding** are the subtlest aspects. In ∀x (P(x) → ∃y Q(x, y)), the variable x is bound by the universal quantifier and y is bound by the existential. A bound variable is just a placeholder: ∀x P(x) and ∀z P(z) say exactly the same thing. A **free variable** — one not bound by any quantifier — makes a formula act like a predicate: it is true or false depending on what value you assign to the free variable. The formula P(x) with free x is open; ∀x P(x) closes it. Quantifier order matters crucially for nested quantifiers: ∀x ∃y (y > x) says "for every number there is a larger one" (true of the integers), while ∃y ∀x (y > x) says "there is a number larger than all numbers" (false). The swap changes the claim entirely.
