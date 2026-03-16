---
id: substitution-and-unification
title: Substitution and Unification
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: first-order-logic-syntax
  type: hard
- id: term-and-atom-fol
  type: hard
builds-toward:
- resolution-fol
- natural-deduction-fol
tags:
- substitution
- unification
- most-general-unifier
- variable-capture
- automated-reasoning
stage: formal-systems
status: draft
---

# Substitution and Unification

## Core Idea
Substitution replaces free occurrences of a variable x in a formula with a term t, written φ[t/x]. The operation must be capture-avoiding: if t contains a variable y that would become bound in φ, the bound variable must first be renamed (alpha-conversion) to prevent the substituted variable from being inadvertently captured. Unification is the inverse problem — given two terms or atoms, find a substitution (called a unifier) that makes them syntactically identical. The most general unifier (MGU) is the least committal such substitution. Robinson's unification algorithm computes the MGU in near-linear time, and it is the engine behind resolution-based theorem proving and logic programming.

## How It's Best Learned
Perform substitutions by hand on formulas with nested quantifiers, deliberately encountering variable-capture problems and fixing them. Then unify pairs of atomic formulas step by step using Robinson's algorithm, building the MGU incrementally.

## Common Misconceptions
- Substitution only replaces free occurrences — bound occurrences of the same variable name are untouched.
- Variable capture is a real and common bug, not an edge case — failing to rename bound variables before substitution can silently change a formula's meaning.
- Not all pairs of terms are unifiable (e.g., f(x) and g(x) cannot unify if f ≠ g); unification can fail, and recognizing failure is part of the algorithm.

## Explainer

From your work on **first-order logic syntax** and **terms and atoms**, you know that a first-order formula is built from terms (variables, constants, function applications) and atomic formulas (predicate applications to terms), combined with logical connectives and quantifiers. **Substitution** is the operation of systematically replacing a variable with a term throughout a formula — it is how you instantiate general claims and how inference rules like universal instantiation are formally defined.

The notation φ[t/x] means "replace every **free** occurrence of variable x in φ with term t." The critical qualifier is *free*: bound occurrences of x (those under a quantifier ∀x or ∃x) are not touched, because they are not the same x — they are a different, locally scoped variable that happens to share the same name. The danger is **variable capture**: if t contains a free variable y, and y happens to be bound in φ at the location where x appears, substituting naively makes y's free occurrence "fall under" a quantifier it didn't before. For example, substituting y for x in ∃y (x = y) should give ∃y (y = y) — but naive substitution captures the free y under the ∃y, silently changing the formula's meaning. The fix is **alpha-conversion**: rename the bound variable first (∃y (x = y) → ∃z (x = z)), then substitute safely (∃z (y = z)).

**Unification** is the inverse problem: given two terms or atomic formulas s and t, find a substitution σ such that σ(s) = σ(t) — they become syntactically identical after applying σ. Such a σ is a **unifier**. The **most general unifier (MGU)** is the least committal one: it makes the minimum commitments necessary to achieve identity, leaving all other variables free to be instantiated later. For example, to unify P(f(x), y) with P(f(a), g(b)), the MGU sets x ↦ a and y ↦ g(b). Any other unifier for these two atoms could be obtained by composing the MGU with a further substitution.

**Robinson's unification algorithm** computes the MGU (or reports failure) by walking two terms in parallel. At each step, if both sides have the same function symbol or constant, recurse on subterms. If one side is a variable x not appearing in the other term t, extend the unifier with x ↦ t. If x appears in t (the **occurs check**), the algorithm fails — there is no finite term satisfying x = f(x). The algorithm runs in near-linear time (with path compression) and is the computational heart of **resolution theorem proving** and **logic programming** (Prolog). Every resolution step finds the MGU of two complementary literals and applies it before cancellation; every Prolog goal is solved by finding the MGU between the goal and a clause head.

Together, substitution and unification transform first-order inference from a semantic matching task — "does this formula follow from those?" — into a syntactic computation over term structure. The MGU is the minimal syntactic bridge between two expressions, and its minimality is essential: using a more specific unifier than necessary forecloses future flexibility, while the MGU commits only to what logic forces.
