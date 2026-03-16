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
stage: formal-systems
status: draft
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

## Explainer

In propositional logic, formulas built from sentence letters get truth values directly from a truth assignment. First-order logic is more expressive — its language can talk about objects, their properties, and relationships — so the semantics must be correspondingly richer. An **interpretation** (or **structure**) M consists of a non-empty **domain** D and an **interpretation function** that gives meaning to every non-logical symbol: each constant c gets an element c^M ∈ D, each n-ary function symbol f gets a function f^M: D^n → D, and each n-ary predicate symbol P gets a set P^M ⊆ D^n. The domain is what we're talking about; the interpretation function tells us what the symbols mean within that universe.

Because first-order formulas can contain **free variables** (variables not bound by any quantifier), a truth value for a formula requires both a structure M and a **variable assignment** s: the function mapping each variable to some element of D. The satisfaction relation M ⊨ φ[s] — "formula φ is satisfied in M under assignment s" — is defined recursively on the structure of φ. For an atomic formula like P(x, y): evaluate the terms at the given assignment to get elements of D, then check whether that tuple is in P^M. For ¬φ: satisfied iff φ is not satisfied. For φ ∧ ψ: satisfied iff both are satisfied. For ∀xφ: satisfied iff for *every* element d ∈ D, the formula φ is satisfied under the assignment s modified to map x to d.

The quantifier clause is where the real power lives. ∀xφ is satisfied under s if no matter which element of the domain you use for x, φ comes out true. ∃xφ is satisfied if *some* element of the domain makes φ true. Notice that after processing ∀x or ∃x, the variable x is no longer free — the quantifier bound it. This is why a **closed formula** (no free variables) has an absolute truth value in a structure: M ⊨ φ (without any mention of an assignment s) means φ is true in M period. A formula with free variables, like x > 0, is not true or false in (ℝ, <) by itself — it depends on what x refers to, which is exactly what the variable assignment provides.

The recursive definition of satisfaction is the semantic counterpart to the recursive definition of well-formed formulas in the syntax. Every formula is built by finitely many applications of the formation rules; every formula's truth value is determined by finitely many applications of the satisfaction clauses, bottoming out at atomic formulas evaluated directly against the interpretation. This recursion is why you can always mechanically evaluate a formula in a finite structure: enumerate the domain, check all combinations, apply the rules. It also connects back to your propositional prerequisites: a propositional truth assignment is exactly the special case where the domain is implicit and all "predicates" are zero-ary (the sentence letters), so satisfaction reduces to the familiar truth table computation.
