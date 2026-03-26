---
id: predicates-and-quantified-statements
title: Predicates and Quantified Statements
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-values-and-statements
  type: hard
builds-toward:
- universal-quantifier-introduction
- existential-quantifier-introduction
tags:
- logic
- predicates
- quantifiers
- variables
stage: formal-systems
status: validated
---

# Predicates and Quantified Statements

## Core Idea
A predicate is a statement containing variables that becomes true or false when values are substituted for the variables (e.g., 'x > 5'). Quantifiers bind variables: the universal quantifier ∀ means 'for all', and the existential quantifier ∃ means 'there exists'. These are essential for expressing mathematical claims about sets.

## How It's Best Learned
Translate between verbal and symbolic forms. Practice with concrete examples showing how substituting values makes a predicate true or false. Understand that without quantifiers, predicates with free variables are neither true nor false.

## Common Misconceptions
- Treating a predicate with a free variable as a statement.
- Confusing the order of quantifiers (∀∃ vs. ∃∀ have different meanings).
- Thinking quantifiers distribute over all logical connectives (they don't always).

## Questions

```yaml
- question: "Which of the following has a definite truth value?"
  type: multiple-choice
  options:
    - "The predicate P(x): x > 5, with x a free variable"
    - "∀x, x > 5, quantifying over all integers"
    - "∃x, x² > 0, quantifying over all integers"
    - "Both B and C"
  answer: 3
  explanation: "A predicate with a free variable like 'x > 5' is neither true nor false — it's waiting for a specific value of x. Once a quantifier binds the variable, it becomes a statement with a definite truth value. ∀x, x > 5 over the integers is false (x = 3 is a counterexample). ∃x, x² > 0 is true (x = 1 works). Both B and C have definite truth values; the unquantified predicate in A does not."

- question: "Consider both statements over the integers: (A) ∀x ∃y, y > x and (B) ∃y ∀x, y > x. Which are true?"
  type: multiple-choice
  options:
    - "Both A and B are true"
    - "Both A and B are false"
    - "Only A is true — for any integer x there is always a larger y, but no single integer exceeds all integers"
    - "Only B is true — the largest integer exceeds all others"
  answer: 2
  explanation: "∀x ∃y, y > x says: for every x I give you, you can find some y larger than it — just take y = x + 1. This is true. ∃y ∀x, y > x says: there is one fixed y that is simultaneously larger than every integer. This is false — no integer is larger than all integers. The crucial difference is that in A, y can depend on x; in B, one y must work for all x at once. Swapping the quantifiers changes the meaning entirely."

- question: "The expression 'x > 5' has no truth value until a specific value is substituted for x or a quantifier binds the variable."
  type: true-false
  answer: true
  explanation: "This is the fundamental distinction between predicates and statements. 'x > 5' is a predicate — a sentence with a free variable. Without knowing what x is, the expression cannot be evaluated as true or false. It becomes a statement only through substitution (plug in x = 7 → true, x = 3 → false) or through quantification (∀x, x > 5 → false; ∃x, x > 5 → true). Treating a predicate as if it had a truth value is a common and consequential error in proof-writing."

- question: "The negation of ∀x, P(x) is ∀x, ¬P(x) — to deny that most x have property P, we say most x lack property P."
  type: true-false
  answer: false
  explanation: "The negation of ∀x, P(x) is ∃x, ¬P(x) — there exists at least one x that lacks property P. To disprove a universal claim, you only need one counterexample. Saying 'all x lack property P' (∀x, ¬P(x)) is a much stronger claim that asserts a universal negative rather than merely denying the universal positive. This negation rule is one of the most important in proof-writing."

- question: "Explain why ∀x ∃y, y > x and ∃y ∀x, y > x make different claims, using the integers as your domain."
  type: short-answer
  answer: "The first says: for each x you choose, I can find some y larger than it — y is allowed to depend on x (e.g., y = x + 1 always works). The second says: there is one fixed y that is larger than every x simultaneously. No such integer exists — for any candidate y, the integer y itself is not less than y. So A is true and B is false."
  explanation: "This captures the key insight about quantifier order: ∀∃ means 'for each input, a suitable witness exists' (the witness can be tailored to the input); ∃∀ means 'one universal witness exists for all inputs simultaneously.' These are profoundly different claims. The same swap appears in analysis: the definition of pointwise continuity (∀ε ∀x ∃δ) versus uniform continuity (∀ε ∃δ ∀x) — the order of ∃δ and ∀x changes the meaning entirely."
```

## Explainer

A **predicate** is a sentence with a variable hole in it. "x > 5" is a predicate: plug in x = 7 and you get a true statement; plug in x = 3 and you get a false one. With a free variable, the predicate itself is neither true nor false — it is a function waiting for input. This is the key distinction between a predicate and a statement. From your work with truth values and statements, you know that statements have definite truth values. Predicates only become statements when their variables are bound — either by substitution or by quantifiers.

**Quantifiers** do the binding. The **universal quantifier** ∀ means "for all." The sentence ∀x, P(x) claims that P(x) is true for every x in the domain. The **existential quantifier** ∃ means "there exists." The sentence ∃x, P(x) claims that at least one x in the domain makes P(x) true. Together, these two quantifiers are the basic vocabulary for expressing mathematical claims: "every even number has a square that is even" is ∀n, if n is even then n² is even; "some prime is even" is ∃p, p is prime and p is even.

The domain of discourse matters enormously. ∀x, x > 0 is true if the domain is the positive integers, false if the domain is all integers. Always ask: quantifying over what? In a proof, you must fix the domain clearly before interpreting a quantified statement. Negating a quantified statement flips the quantifier and negates the body: the negation of ∀x, P(x) is ∃x, ¬P(x), and the negation of ∃x, P(x) is ∀x, ¬P(x). This is one of the most important rules in proof-writing — to prove "not all x have property P," you just find one counterexample.

The order of quantifiers is critical when multiple quantifiers appear. ∀x ∃y, y > x (for every x, there exists a y larger than it) is a true statement about the integers — just take y = x + 1. But ∃y ∀x, y > x (there exists a y larger than all x) is false — no integer is larger than every integer. The order ∀∃ says "for each x you give me, I can find a y"; the order ∃∀ says "I can find one y that works for every x simultaneously." These are profoundly different claims, and swapping quantifiers changes the meaning in ways that will matter throughout real analysis, topology, and any subject that reasons about limits and convergence.
