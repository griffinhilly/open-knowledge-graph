---
id: most-general-unifier
title: Most General Unifier (MGU)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: substitution-and-unification
  type: hard
builds-toward:
- ground-instances-and-instantiation
tags:
- first-order-logic
- unification
- automated-reasoning
stage: formal-systems
status: draft
---

# Most General Unifier (MGU)

## Core Idea
A substitution θ is a unifier of two terms if θ(s) = θ(t); a most general unifier (MGU) is a unifier such that any other unifier is an instance of it. The MGU, when it exists, is unique up to variable renaming and is the key operation enabling the resolution rule in first-order logic to work effectively.

## Explainer

You already know what a **substitution** is — a mapping from variables to terms — and you know that **unification** is the process of finding a substitution that makes two terms syntactically identical. For example, the terms f(x, b) and f(a, y) can be unified by the substitution {x ↦ a, y ↦ b}, because applying it gives f(a, b) and f(a, b). But there may be many unifiers: {x ↦ a, y ↦ b, z ↦ c} also works if z doesn't appear in either term. The **most general unifier** is the one that commits the least — the one that makes the minimum number of additional assignments.

Formally, θ is a **most general unifier (MGU)** of s and t if (1) θ(s) = θ(t) (it is a unifier), and (2) every other unifier σ factors through θ: there exists a substitution λ such that σ = λ ∘ θ. In other words, any unifier is an "instance" of the MGU obtained by further specializing it. The MGU preserves the most freedom — it unifies just enough and no more. For f(x, b) and f(a, y), the MGU is {x ↦ a, y ↦ b} exactly. A substitution like {x ↦ a, y ↦ b, x ↦ a} with redundant bindings is the same MGU up to trivialities; what you *cannot* have in an MGU is {x ↦ a, y ↦ b, z ↦ c} when z is unconstrained — that adds information not required for unification.

**Martelli and Montanari's algorithm** (and the earlier Robinson unification algorithm) compute the MGU systematically: decompose the unification problem into a set of equations, repeatedly applying rules like "both terms are the same constant — remove the equation" or "variable x appears on one side — substitute x throughout." The **occurs check** is the critical safety test: before substituting x ↦ t, verify that x does not appear in t. Without this check, you could create a circular binding like x ↦ f(x), which has no finite solution. With the occurs check, the algorithm terminates and either produces an MGU or reports failure (no unifier exists).

The MGU is the engine of **resolution-based theorem proving**. The resolution rule takes two clauses, finds a literal in one that is the negation of a literal in the other, and cancels them — but for first-order logic, the two literals may not match syntactically. The MGU bridges this gap: it is the substitution that makes the two literals match, and applying it to the full clauses gives the resolvent. For example, resolving P(x) and ¬P(f(a)) requires unifying x with f(a) via {x ↦ f(a)}, giving the MGU that makes resolution possible. Using the MGU (rather than any specific unifier) ensures the resolvent is as general as possible — no unnecessary commitments about the values of other variables.

The uniqueness property (up to variable renaming) is what makes the MGU well-defined as an algorithm output. There isn't an arbitrary choice being made — the MGU is a canonical object. This is why unification-based inference systems are **deterministic in their inference steps**, even though they may explore many branches in proof search. Every step in the resolution refutation has a unique MGU, and the proof's correctness doesn't depend on which renaming you use.
