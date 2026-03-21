---
id: predicates-and-quantifiers-intro
title: Predicates and Quantifiers
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- negation-of-quantified-statements
- set-fundamentals
tags:
- logic
- predicates
- quantifiers
stage: formal-systems
status: draft
---

# Predicates and Quantifiers

## Core Idea
A predicate is a statement involving a variable that becomes true or false based on the variable's value. The universal quantifier 'for all' (∀) and existential quantifier 'there exists' (∃) specify how claims about predicates apply to sets of objects. These tools formalize statements about entire domains precisely and are indispensable for mathematical discourse.

## Questions

```yaml
- question: "Consider ∀x ∈ ℝ, ∃y ∈ ℝ such that y > x. Now consider ∃y ∈ ℝ, ∀x ∈ ℝ such that y > x. Which statements are true?"
  type: multiple-choice
  options:
    - "Both are true — they both express the idea that ℝ has no upper bound"
    - "Both are false — you need to specify which y before making any comparison"
    - "The first is true; the second is false — for each x a larger y exists, but no single y exceeds all real numbers"
    - "The first is false; the second is true — there must be some y large enough to exceed any given x"
  answer: 2
  explanation: "Quantifier order is critical. In ∀x ∃y, the choice of y is allowed to depend on x — for each specific x, you pick y = x + 1. In ∃y ∀x, a single y must work for every x simultaneously. Since ℝ has no largest element, no fixed y can exceed all x. This is one of the most common sources of logical error: swapping ∀ and ∃ can transform a true statement into a false one."

- question: "The expression 'n is divisible by 3' is neither true nor false as written. What kind of expression is it, and what makes it become a proposition with a definite truth value?"
  type: multiple-choice
  options:
    - "It is a proposition with an indeterminate truth value that becomes determined once context is provided"
    - "It is a predicate — a statement whose truth depends on the value of n. It becomes a proposition when n is bound by a quantifier (∀n or ∃n) or replaced by a specific value"
    - "It is an axiom that holds by definition for all n in the integer domain"
    - "It is a definition and therefore neither true nor false in any circumstances"
  answer: 1
  explanation: "A predicate is like a function from a domain to {true, false} — it takes inputs and returns a truth value, but has no truth value on its own. 'n is divisible by 3' is true for n = 6, false for n = 7, and meaningless without a value for n. It becomes a proposition either by substituting a specific value or by binding n with a quantifier: ∃n (n is divisible by 3) is a true proposition, ∀n (n is divisible by 3) is a false one."

- question: "The negation of the statement 'Every student in the class passed the exam' is 'No student in the class passed the exam.'"
  type: true-false
  answer: false
  explanation: "The negation of ∀x P(x) is ∃x ¬P(x) — 'there exists at least one x for which P is false.' So the negation of 'every student passed' is 'there exists at least one student who did not pass.' The statement 'no student passed' is a much stronger claim (∀x ¬P(x)) and is not the logical negation. This confusion leads to serious errors in proof by contradiction, where you must negate the statement you're disproving precisely."

- question: "To prove ∀x ∈ ℤ, x² ≥ 0, it is sufficient to verify the claim for a large but finite number of integers and conclude the pattern holds."
  type: true-false
  answer: false
  explanation: "A universal quantifier over an infinite domain cannot be proved by checking cases — the domain contains infinitely many values, and unchecked cases might fail. To prove ∀x P(x), you must show P holds for an arbitrary, unspecified x in the domain. (For this particular claim, the proof is: x² = x·x; whether x is positive, negative, or zero, the product of a number with itself is ≥ 0.) Finite verification is evidence, not proof."

- question: "Why does swapping the order of unlike quantifiers (∀ and ∃) matter? Give a clear mathematical example where swapping them changes a true statement to a false one."
  type: short-answer
  answer: "In ∀x ∃y, the existential witness y can be chosen to depend on x — a different y for each x. In ∃y ∀x, a single y must simultaneously satisfy the condition for every x. Example: ∀x ∈ ℤ, ∃y ∈ ℤ such that y > x is true (for each x, choose y = x + 1). But ∃y ∈ ℤ, ∀x ∈ ℤ such that y > x is false — there is no single integer that exceeds every integer."
  explanation: "This is one of the most important distinctions in mathematical logic. The order encodes a crucial dependency: ∀x ∃y says the choice of y may depend on x, while ∃y ∀x requires a universal choice that works for all x regardless. Many theorems in analysis and algebra hinge on this distinction — for example, pointwise continuity (∀ε ∀x ∃δ) versus uniform continuity (∀ε ∃δ ∀x) differ only in quantifier order but are genuinely different properties."
```

## Explainer

In propositional logic — your prerequisite — every statement has a fixed truth value. "It is raining" is either true or false as a whole. But most interesting mathematical statements aren't like that: "n is even," "x² > 0," and "f is continuous" are neither true nor false on their own. They are **predicates**: statements whose truth depends on the value of one or more variables. Write P(n) for "n is even"; then P(2) is true and P(3) is false. A predicate is like a function from a domain of objects to {true, false}.

Predicates become full propositions — statements with definite truth values — when you **bind the variables** using quantifiers. The **universal quantifier** ∀ asserts that a predicate is true for every element in the domain: ∀n ∈ ℤ, (n is even or n is odd) is a true proposition. The **existential quantifier** ∃ asserts that at least one element satisfies the predicate: ∃n ∈ ℤ, n² = 4 is also true (take n = 2 or n = −2). Notice that neither quantifier tells you *which* element witnesses the existential — just that one exists. To prove ∀x P(x) you must show P holds for an arbitrary x; to prove ∃x P(x) you typically exhibit a specific x.

A single predicate can carry multiple variables, and **nested quantifiers** apply them one at a time. ∀x ∃y, y > x says "for every x, there is some y larger than it" — true over the integers (take y = x + 1). But ∃y ∀x, y > x says "there is some y larger than every x" — false over the integers (no largest integer exists). Swapping ∀ and ∃ can change a true statement to a false one. The order of unlike quantifiers is crucial and is one of the most common sources of logical error in beginning proof-writing.

Negating quantified statements follows precise rules that are the logical analog of De Morgan's laws. The negation of ∀x P(x) is ∃x ¬P(x): "not all x satisfy P" means "there is some x that does not." The negation of ∃x P(x) is ∀x ¬P(x): "there is no x satisfying P" means "all x fail P." These rules nest: negating ∀x ∃y P(x, y) gives ∃x ∀y ¬P(x, y). Every quantifier flips, every connective follows De Morgan, and all the variable bindings stay in place. Mastering negation of quantified statements is essential — every proof by contradiction and every counterexample argument starts by correctly negating the claim you're trying to disprove.
