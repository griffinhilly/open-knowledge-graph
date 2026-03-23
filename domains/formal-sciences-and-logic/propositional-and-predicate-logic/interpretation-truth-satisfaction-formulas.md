---
id: interpretation-truth-satisfaction-formulas
title: Interpretation, Truth, and Satisfaction of Formulas
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: model-interpretation-and-satisfaction
  type: hard
- id: first-order-semantics
  type: hard
builds-toward:
- logical-consequence-and-entailment
tags:
- semantics
- interpretation
- truth
- satisfaction
stage: advanced
status: validated
---

# Interpretation, Truth, and Satisfaction of Formulas

## Core Idea
An interpretation (or structure) assigns meaning to the non-logical symbols of a language: each constant is assigned an element of the domain, each function symbol is assigned a function, and each predicate symbol is assigned a set of tuples. Given an interpretation and a variable assignment (for formulas with free variables), every formula has a truth value (true or false). A formula is satisfied by an interpretation if it's true under all variable assignments consistent with that interpretation. Satisfaction is the core semantic notion linking syntax (formulas) to models (interpretations).

## How It's Best Learned
Use small, concrete models and manually evaluate formulas. Understand that predicates map to sets, and satisfaction is defined recursively on formula structure. Practice with formulas involving quantifiers and free variables. Relate to truth tables in propositional logic as a special case.

## Common Misconceptions
- Confusing the domain (set of objects) with the interpretation (assignment of meaning to symbols).
- Thinking truth value is absolute (it's relative to an interpretation).
- Assuming free variables have truth values (they don't — truth requires either binding or a variable assignment).

## Questions

```yaml
- question: "Consider the formula 'x > 0' evaluated in the structure M = (ℝ, <). What is the truth value of this formula in M?"
  type: multiple-choice
  options:
    - "True, because most real numbers are positive"
    - "False, because x could be assigned a negative value"
    - "It has no truth value in M without specifying a variable assignment for x"
    - "True, because ℝ is an ordered field and positivity is well-defined"
  answer: 2
  explanation: "The formula 'x > 0' contains a free variable x. Free variables do not have truth values in isolation — truth requires either a quantifier binding x or a variable assignment s specifying which element of ℝ the variable x refers to. Under assignment s with s(x) = 3, the formula is true. Under s with s(x) = −5, it is false. The formula is neither 'true in M' nor 'false in M' because it depends on what x refers to. Option A misapplies a probabilistic intuition. Option B correctly identifies that x could be negative but draws the wrong conclusion — the formula isn't false, it's indeterminate without an assignment."

- question: "The formula ∀x P(x) is evaluated in a structure M with domain D = {1, 2, 3} and P^M = {1, 2}. What is the truth value?"
  type: multiple-choice
  options:
    - "True, because most elements of D satisfy P"
    - "False, because element 3 is not in P^M, so P(3) fails"
    - "True, because ∀x is a universal quantifier and D is finite"
    - "Undefined, because P is not total over D"
  answer: 1
  explanation: "∀x P(x) is satisfied in M if and only if P(d) is true for every element d in the domain D. Since D = {1, 2, 3} and P^M = {1, 2}, we must check P(1), P(2), and P(3). P(1) and P(2) are true (1 and 2 are in P^M), but P(3) is false (3 is not in P^M). Because ∀x demands the formula hold for all elements and it fails at 3, the universal statement is false. Option A applies a majority rule that is not the definition of universal quantification. Option C introduces an irrelevant special case about finite domains. Option D is wrong: predicates are total by definition — P^M is a subset of D, so every element either is or is not in P^M."

- question: "A closed formula (one with no free variables) has a definite truth value — either true or false — in any given structure, without specifying a variable assignment."
  type: true-false
  answer: true
  explanation: "A closed formula has no free variables; all variables are bound by quantifiers. Since there is nothing left unspecified, the satisfaction relation M ⊨ φ (without mentioning any assignment s) is well-defined. You can evaluate it by tracing through the recursive satisfaction clauses: for each quantifier, check all elements of the domain; for atomic formulas, check whether the tuples are in the predicate extension. The result is a definite true or false. This is why sentences (closed formulas) in first-order logic are the objects that can be true or false 'in a model,' while open formulas with free variables are only satisfied or not satisfied relative to variable assignments."

- question: "The truth value of a formula in first-order logic is determined by its syntactic structure alone, without reference to any particular interpretation or variable assignment."
  type: true-false
  answer: false
  explanation: "This confuses syntax with semantics. Syntactic structure determines whether a string is a well-formed formula, but truth values are entirely semantic — they depend on which interpretation is being used. The formula P(a) could be true in one structure (where P^M contains the element assigned to a) and false in another (where it does not). Even a formula like '∀x (x = x)' which is logically valid (true in every interpretation) gets its truth value from the semantic rule that identity is reflexive in every structure — this is a semantic fact, not a syntactic one. In first-order logic, there is no truth without interpretation."

- question: "Why can't we assign a truth value to a formula with free variables without specifying a variable assignment, and how does this differ from propositional logic?"
  type: short-answer
  answer: "In first-order logic, a formula like 'P(x)' contains the free variable x, which acts as a placeholder that could refer to any element of the domain. Without a variable assignment specifying which element x refers to, the formula has no definite meaning — it might be true of some elements and false of others. A variable assignment s maps each free variable to a specific domain element, completing the interpretation and enabling truth evaluation. In propositional logic, this issue doesn't arise: sentence letters like P and Q are already zero-ary (they take no arguments and refer to no objects), so a truth assignment directly gives them a truth value with no further specification needed. First-order logic's expressive power — the ability to quantify over objects and express properties of arbitrary domain elements — is exactly what creates this dependence on variable assignments for open formulas."
  explanation: "The key contrast is between propositional sentence letters (complete bearers of truth values under a truth assignment) and first-order predicate formulas with free variables (incomplete bearers requiring a variable assignment to specify what the variables denote). The answer should explain what free variables are (placeholders), why they create the dependence (they could refer to any domain element), and why propositional logic avoids this (sentence letters have no arguments)."
```

## Explainer

In propositional logic, formulas built from sentence letters get truth values directly from a truth assignment. First-order logic is more expressive — its language can talk about objects, their properties, and relationships — so the semantics must be correspondingly richer. An **interpretation** (or **structure**) M consists of a non-empty **domain** D and an **interpretation function** that gives meaning to every non-logical symbol: each constant c gets an element c^M ∈ D, each n-ary function symbol f gets a function f^M: D^n → D, and each n-ary predicate symbol P gets a set P^M ⊆ D^n. The domain is what we're talking about; the interpretation function tells us what the symbols mean within that universe.

Because first-order formulas can contain **free variables** (variables not bound by any quantifier), a truth value for a formula requires both a structure M and a **variable assignment** s: the function mapping each variable to some element of D. The satisfaction relation M ⊨ φ[s] — "formula φ is satisfied in M under assignment s" — is defined recursively on the structure of φ. For an atomic formula like P(x, y): evaluate the terms at the given assignment to get elements of D, then check whether that tuple is in P^M. For ¬φ: satisfied iff φ is not satisfied. For φ ∧ ψ: satisfied iff both are satisfied. For ∀xφ: satisfied iff for *every* element d ∈ D, the formula φ is satisfied under the assignment s modified to map x to d.

The quantifier clause is where the real power lives. ∀xφ is satisfied under s if no matter which element of the domain you use for x, φ comes out true. ∃xφ is satisfied if *some* element of the domain makes φ true. Notice that after processing ∀x or ∃x, the variable x is no longer free — the quantifier bound it. This is why a **closed formula** (no free variables) has an absolute truth value in a structure: M ⊨ φ (without any mention of an assignment s) means φ is true in M period. A formula with free variables, like x > 0, is not true or false in (ℝ, <) by itself — it depends on what x refers to, which is exactly what the variable assignment provides.

The recursive definition of satisfaction is the semantic counterpart to the recursive definition of well-formed formulas in the syntax. Every formula is built by finitely many applications of the formation rules; every formula's truth value is determined by finitely many applications of the satisfaction clauses, bottoming out at atomic formulas evaluated directly against the interpretation. This recursion is why you can always mechanically evaluate a formula in a finite structure: enumerate the domain, check all combinations, apply the rules. It also connects back to your propositional prerequisites: a propositional truth assignment is exactly the special case where the domain is implicit and all "predicates" are zero-ary (the sentence letters), so satisfaction reduces to the familiar truth table computation.
