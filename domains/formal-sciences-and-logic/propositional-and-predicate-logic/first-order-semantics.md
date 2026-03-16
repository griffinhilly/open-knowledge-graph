---
id: first-order-semantics
title: First-Order Logic Semantics and Structures
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: set-theory-basics
  type: soft
builds-toward:
- natural-deduction-fol
- fol-soundness-completeness
- model-theory-basics
tags:
- structure
- interpretation
- satisfaction
- model
- domain
stage: formal-systems
status: validated
---

# First-Order Logic Semantics and Structures

## Core Idea
A first-order structure (or interpretation) for a signature consists of a non-empty domain D and an assignment of: each constant to an element of D, each n-ary function symbol to an n-ary function on D, and each n-ary predicate symbol to an n-ary relation on D. A variable assignment maps each variable to a domain element. Satisfaction (M, s ⊨ φ) is defined recursively: atomic formulas by checking relations, Boolean connectives compositionally, and quantifiers by ranging over all domain elements. A sentence is true in M (written M ⊨ φ) if it is satisfied under any variable assignment.

## How It's Best Learned
Work through small finite structures (sets of 2–4 elements) and evaluate FOL sentences by hand. Verify that the same formula can be true in one structure and false in another to build intuition for model-dependence.

## Common Misconceptions
- The domain is not fixed; every structure chooses its own domain, which need not be the natural numbers or any canonical set.
- Quantifier evaluation is not about logical connectives alone — ∀x φ(x) is true only if φ(a) holds for every element a in the domain.

## Questions

```yaml
- question: "Consider a structure M with domain {a, b} where the predicate Happy holds only of element a. What is the truth value of ∀x Happy(x) in M?"
  type: multiple-choice
  options: ["True, because Happy(a) holds", "False, because Happy does not hold of every domain element", "True, because a is the only named constant", "Undefined, because b has no truth value assigned"]
  answer: 1
  explanation: "∀x Happy(x) requires Happy to hold of every element in the domain. Since Happy does not hold of b, the sentence is false in M. This illustrates a key point: universal quantifiers range over all domain elements, not just those for which the predicate happens to hold."

- question: "The sentence ∃x P(x) has the same truth value in every first-order structure with the same signature."
  type: true-false
  answer: false
  explanation: "Truth in first-order logic is model-relative. ∃x P(x) is true in a structure where at least one domain element satisfies P, and false in a structure where no element does. The same formula can be true in one structure and false in another — this is the fundamental insight of model-theoretic semantics."

- question: "What is the difference between a formula φ(x) being satisfied by an element a in structure M, and the sentence ∀x φ(x) being true in M?"
  type: short-answer
  answer: "φ(x) is satisfied by a when the variable assignment mapping x to a makes φ true in M. The sentence ∀x φ(x) is true in M when every element in the domain satisfies φ — satisfaction of the universal sentence requires checking every possible assignment."
  explanation: "Satisfaction is element-relative; truth of a universal sentence requires that satisfaction hold across the entire domain. This distinction underlies the recursive definition of satisfaction and is why quantifiers are the semantically distinctive feature of first-order logic compared to propositional logic."
```

## Explainer

First-order logic syntax gives you a language — variables, constants, predicate symbols, quantifiers — but syntax alone doesn't tell you what sentences *mean*. Semantics is the bridge between symbols and meaning: it defines what it takes for a formula to be *true* in a given context. That context is called a **structure** (or interpretation).

A structure M for a given signature has two parts. First, a non-empty **domain** D — the set of objects the variables will range over. Second, an **interpretation function** that assigns meaning to every symbol: each constant is assigned a specific element of D, each function symbol is assigned a function on D, and each predicate symbol is assigned a relation on D. Nothing in the syntax forces the domain to be the natural numbers or any familiar set — a structure for arithmetic could have domain {●, ▲, ■} if you wanted. The domain is your choice.

Given a structure, satisfaction is defined recursively. An atomic formula like P(x, y) is satisfied when the pair (s(x), s(y)) — where s is the current variable assignment — falls inside the relation interpreting P. Boolean connectives work compositionally: φ ∧ ψ is satisfied when both are. Quantifiers are where the semantics becomes truly powerful: ∃x φ(x) is satisfied when *some* element of D satisfies φ when assigned to x; ∀x φ(x) is satisfied when *every* element does. This means evaluating a universally quantified sentence requires, in principle, checking every domain element.

The key philosophical payoff is **model-dependence**: the same sentence can be true in one structure and false in another. The sentence ∀x∀y (x = y) is true in any one-element structure and false in any structure with two or more elements. A **model** of a sentence φ is simply a structure M such that M ⊨ φ. Model theory — the study of which structures satisfy which sentences — grows directly from these definitions. When you move on to soundness and completeness theorems, you will be asking exactly whether the provability relation and the satisfaction relation track each other.

A common stumbling block is confusing the domain with some canonical set. In practice, textbook examples often use ℕ or ℝ because they are familiar, but this is purely for convenience. Another stumbling block is handling variables: a formula with free variables (like P(x)) isn't true or false on its own — it is satisfied (or not) relative to a specific variable assignment. Only sentences — formulas with no free variables — have a definite truth value in a structure independent of any assignment.

## Notes

The satisfaction relation (M, s ⊨ φ) was formalized by Alfred Tarski in the 1930s, giving logic a rigorous compositional semantics. The approach here — structures, domains, variable assignments — is standard across model theory, database theory (where relations in a database are exactly first-order structures), and formal verification.
