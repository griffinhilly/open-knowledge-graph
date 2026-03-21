---
id: predicates-and-quantifiers
title: Predicates and Quantifiers
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- negation-of-quantifiers
- direct-proof
tags:
- quantifiers
- predicates
- first-order-logic
stage: formal-systems
status: draft
---

# Predicates and Quantifiers

## Core Idea
A predicate is a statement with variables whose truth depends on variable values. Quantifiers specify scope: ∀ (universal) means all values satisfy the predicate; ∃ (existential) means at least one does. These express mathematical theorems precisely.

## Questions

```yaml
- question: "The statement ∀x ∈ ℝ, x² ≥ 0 is claimed to be false. What is the minimum needed to refute it?"
  type: multiple-choice
  options:
    - "Show that x² < 0 for most real numbers"
    - "Provide a single real number x where x² < 0"
    - "Show that no real number satisfies x² ≥ 0"
    - "Demonstrate that the claim fails for infinitely many values"
  answer: 1
  explanation: "Disproving a universal claim ∀x P(x) requires exactly one counterexample — one value of x that makes P(x) false. 'Most' or 'infinitely many' is far more than necessary. Conversely, to *prove* a universal claim, you need an argument that works for an arbitrary x — checking any finite number of cases is never enough, no matter how many."

- question: "Compare ∀ε>0 ∃δ>0 [P(ε,δ)] with ∃δ>0 ∀ε>0 [P(ε,δ)]. Why does the order of quantifiers matter?"
  type: multiple-choice
  options:
    - "The order doesn't matter — ∀ and ∃ always commute when they involve different variables"
    - "In ∀ε ∃δ, δ may depend on ε; in ∃δ ∀ε, one fixed δ must work for all ε — these express genuinely different claims"
    - "The first form is just notational convention; both mean the same thing logically"
    - "The second form is always stronger because the universal quantifier appears last"
  answer: 1
  explanation: "Order is critical because inner quantifiers can depend on outer ones. In ∀ε ∃δ, you choose δ after seeing ε, so δ is allowed to depend on ε. In ∃δ ∀ε, one fixed δ must serve every ε simultaneously — a strictly stronger claim that is usually false. This is exactly the distinction in the epsilon-delta limit definition: the δ must respond to each ε, not be chosen in advance for all of them."

- question: "A predicate P(x) = 'x is prime' has a definite truth value even before x is specified."
  type: true-false
  answer: false
  explanation: "A predicate with a free variable is not a proposition — it has no fixed truth value until a specific value is substituted for x. P(7) is true, P(4) is false, but P(x) by itself is neither true nor false. Quantifying the variable (∀x P(x) or ∃x P(x)) converts the predicate into a proposition with a definite truth value."

- question: "To prove an existential statement ∃x P(x), it suffices to exhibit one concrete value of x that makes P(x) true."
  type: true-false
  answer: true
  explanation: "Existential claims are proved by witness. Since ∃x P(x) only asserts that at least one value works, showing any single concrete example is a complete proof. This contrasts with universal claims, which require an argument valid for an arbitrary x. The asymmetry — ∀ needs general argument, ∃ needs one example — is essential to proof strategy."

- question: "Why does swapping the order of ∀ and ∃ in a mathematical statement change its meaning? Give an example that illustrates the difference."
  type: short-answer
  answer: "In ∀x ∃y ..., the value of y can depend on x (you choose y after seeing x). In ∃y ∀x ..., one fixed y must work for every x simultaneously. Example: ∀x ∈ ℝ ∃y ∈ ℝ (y > x) is true — for any x, pick y = x + 1. But ∃y ∈ ℝ ∀x ∈ ℝ (y > x) is false — no single real number exceeds every real number."
  explanation: "The key is whether inner variables can depend on outer ones. When ∀ comes first, its variable is 'given,' and subsequent ∃ witnesses can be tailored to it. When ∃ comes first, its witness must be fixed before the ∀ variable is known. This distinction underlies virtually every definition in analysis and topology that uses nested quantifiers."
```

## Explainer

The propositional logic you've learned so far deals with statements that have fixed truth values — "Paris is in France" is true, "2 + 2 = 5" is false. But mathematics rarely works with fixed facts alone. Most mathematical claims involve *variables*: "x is even," "n² > 0," "the function f is continuous." These are **predicates** — statement-templates that become true or false only once you substitute a value for the variable. P(x) = "x is even" is neither true nor false until you specify x; P(4) is true, P(7) is false.

To turn a predicate into a definite statement, you need a **quantifier** that says which values of x you mean. The **universal quantifier** ∀ ("for all") produces a claim that holds for every element of the domain: ∀x P(x) asserts that P(x) is true for every x you could substitute. To *prove* a universal claim, you must give an argument that works for an arbitrary x. To *disprove* it, you need only exhibit a single **counterexample** — one value of x for which P(x) is false.

The **existential quantifier** ∃ ("there exists") makes the weaker claim that at least one value works: ∃x P(x) asserts that some specific x makes P(x) true. To *prove* an existential claim, you exhibit a concrete witness. To *disprove* it, you must show P(x) fails for every x — a much harder task. The asymmetry between proving and disproving is opposite for the two quantifiers, and keeping this straight is essential for constructing correct proofs.

Order of quantifiers is critical when multiple quantifiers are nested. Consider "for every ε > 0, there exists δ > 0 such that if |x − a| < δ then |f(x) − L| < ε" — the definition of a limit. The ∀ε ∃δ order means δ is allowed to depend on ε (you choose δ after seeing ε). Reversing to ∃δ ∀ε would mean a single δ works for all ε simultaneously — a far stronger, usually false claim. Reading a statement with nested quantifiers is a skill in itself: track the order, note which variables depend on which, and the logical structure of theorems becomes precise and unambiguous.
