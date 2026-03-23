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
status: validated
---

# Most General Unifier (MGU)

## Core Idea
A substitution θ is a unifier of two terms if θ(s) = θ(t); a most general unifier (MGU) is a unifier such that any other unifier is an instance of it. The MGU, when it exists, is unique up to variable renaming and is the key operation enabling the resolution rule in first-order logic to work effectively.

## Questions

```yaml
- question: "Given the terms f(x, g(a)) and f(b, g(y)), what is the most general unifier (MGU)?"
  type: multiple-choice
  options:
    - "{x ↦ b, y ↦ a, z ↦ c} — binding an extra free variable z to c for completeness"
    - "{x ↦ b, y ↦ a} — binding only what is strictly required to make the terms identical"
    - "{x ↦ a, y ↦ b} — swapping the bindings to match argument positions"
    - "No unifier exists because f has arguments of different structure in each term"
  answer: 1
  explanation: "The MGU binds the minimum necessary: x must become b (to match the first arguments: x and b), and y must become a (to match g(a) and g(y): the arguments a and y). Applying {x↦b, y↦a} gives f(b, g(a)) and f(b, g(a)) — identical. Option A adds a binding for z that is unconstrained and unnecessary — it is a valid unifier but not the most general one. The MGU commits the least, leaving all non-required variables free for subsequent inference steps."

- question: "A student argues that for resolution-based theorem proving, any unifier will work — there is no reason to prefer the most general one. Why is using the MGU specifically important?"
  type: multiple-choice
  options:
    - "The MGU is always the most specific substitution and produces the most instantiated resolvent"
    - "Using the MGU keeps the resolvent as general as possible — unnecessary variable bindings in a more specific unifier restrict what subsequent inference steps can do with those variables"
    - "The MGU is required by Prolog syntax but has no logical significance"
    - "More specific unifiers are computationally harder to compute than the MGU"
  answer: 1
  explanation: "If you use a more specific unifier that binds extra variables unnecessarily, the resulting resolvent carries those commitments through the entire proof. Subsequent resolution steps that might need those variables to take different values are blocked. The MGU leaves the maximum freedom: it binds only what the current step requires, and all other variables remain available. This is not just efficiency — it is what makes the resolution proof system complete: using only MGUs guarantees you explore all possible inferences."

- question: "The occurs check — verifying that variable x does not appear in term t before creating the binding x ↦ t — is merely an optimization that can safely be skipped in most practical theorem provers."
  type: true-false
  answer: false
  explanation: "Skipping the occurs check can create unsound circular bindings. Without it, a unifier might bind x ↦ f(x), creating a circular term with no finite solution. An algorithm without the occurs check may loop forever trying to construct this infinite term, or produce a substitution that makes the unification 'succeed' with a non-terminating circular structure — leading to unsound inferences. Many Prolog implementations skip the occurs check for speed, which makes them technically unsound, but for a correct theorem prover the occurs check is required for soundness."

- question: "For any two unifiable terms, the MGU is unique up to variable renaming — it is a canonical object determined by the terms themselves, not an arbitrary choice among unifiers."
  type: true-false
  answer: true
  explanation: "This uniqueness is what makes the MGU well-defined as an algorithm output and why resolution is deterministic in its inference steps. If multiple MGUs existed that were genuinely different (not just renamings of each other), resolution would be non-deterministic in a way that could affect completeness. The uniqueness theorem guarantees that any correct unification algorithm will produce the same canonical answer (up to renaming), so the resolvent produced by a resolution step is unique regardless of which algorithm computed the MGU."

- question: "In resolution-based theorem proving, why must the MGU substitution be applied to all literals in both clauses being resolved, not just to the specific literals that were matched?"
  type: short-answer
  answer: "The MGU may bind variables that appear in other literals of the same clause, not just in the matched pair. Applying the substitution only to the matched literals would leave those other literals with the old variable names, creating an inconsistency: the same variable would have one value in the matched literal (already resolved away) and a different, unsubstituted form in the remaining literals. The resolvent must be logically coherent — all occurrences of each variable must be uniformly substituted — and as general as possible, which requires applying the MGU throughout both clauses."
  explanation: "For example, if clause 1 is P(x) ∨ Q(x) and clause 2 is ¬P(f(a)), the MGU for P(x) and P(f(a)) is {x ↦ f(a)}. The resolvent is Q(x) with the substitution applied: Q(f(a)). If we only applied the MGU to the P-literals and left Q(x) untouched, we'd have an unsubstituted x floating in the resolvent that was supposed to be bound to f(a) — an incoherent clause. Uniform application preserves the meaning of the variables across the clause."
```

## Explainer

You already know what a **substitution** is — a mapping from variables to terms — and you know that **unification** is the process of finding a substitution that makes two terms syntactically identical. For example, the terms f(x, b) and f(a, y) can be unified by the substitution {x ↦ a, y ↦ b}, because applying it gives f(a, b) and f(a, b). But there may be many unifiers: {x ↦ a, y ↦ b, z ↦ c} also works if z doesn't appear in either term. The **most general unifier** is the one that commits the least — the one that makes the minimum number of additional assignments.

Formally, θ is a **most general unifier (MGU)** of s and t if (1) θ(s) = θ(t) (it is a unifier), and (2) every other unifier σ factors through θ: there exists a substitution λ such that σ = λ ∘ θ. In other words, any unifier is an "instance" of the MGU obtained by further specializing it. The MGU preserves the most freedom — it unifies just enough and no more. For f(x, b) and f(a, y), the MGU is {x ↦ a, y ↦ b} exactly. A substitution like {x ↦ a, y ↦ b, x ↦ a} with redundant bindings is the same MGU up to trivialities; what you *cannot* have in an MGU is {x ↦ a, y ↦ b, z ↦ c} when z is unconstrained — that adds information not required for unification.

**Martelli and Montanari's algorithm** (and the earlier Robinson unification algorithm) compute the MGU systematically: decompose the unification problem into a set of equations, repeatedly applying rules like "both terms are the same constant — remove the equation" or "variable x appears on one side — substitute x throughout." The **occurs check** is the critical safety test: before substituting x ↦ t, verify that x does not appear in t. Without this check, you could create a circular binding like x ↦ f(x), which has no finite solution. With the occurs check, the algorithm terminates and either produces an MGU or reports failure (no unifier exists).

The MGU is the engine of **resolution-based theorem proving**. The resolution rule takes two clauses, finds a literal in one that is the negation of a literal in the other, and cancels them — but for first-order logic, the two literals may not match syntactically. The MGU bridges this gap: it is the substitution that makes the two literals match, and applying it to the full clauses gives the resolvent. For example, resolving P(x) and ¬P(f(a)) requires unifying x with f(a) via {x ↦ f(a)}, giving the MGU that makes resolution possible. Using the MGU (rather than any specific unifier) ensures the resolvent is as general as possible — no unnecessary commitments about the values of other variables.

The uniqueness property (up to variable renaming) is what makes the MGU well-defined as an algorithm output. There isn't an arbitrary choice being made — the MGU is a canonical object. This is why unification-based inference systems are **deterministic in their inference steps**, even though they may explore many branches in proof search. Every step in the resolution refutation has a unique MGU, and the proof's correctness doesn't depend on which renaming you use.
