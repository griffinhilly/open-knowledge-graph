---
id: domain-and-structure-fol
title: Domain and Structure in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: models-and-interpretation-basic
  type: hard
- id: set-membership-and-notation
  type: soft
- id: set-fundamentals
  type: hard
- id: functions-and-mappings-formal
  type: hard
builds-toward:
- satisfaction-relation-fol
tags:
- first-order-logic
- domain
- structures
stage: formal-systems
status: draft
---

# Domain and Structure in First-Order Logic

## Core Idea
The domain of a structure is the non-empty set of objects over which variables range; the structure also assigns to each predicate a relation on the domain and to each function symbol an operation on the domain. Understanding domains and structures is essential for moving from propositional to predicate logic—it transforms logic from dealing with abstract propositions to dealing with objects and their properties.

## How It's Best Learned
Work with concrete examples: natural numbers with plus and less-than, strings with concatenation, sets with membership. Draw diagrams showing the domain and relations.

## Common Misconceptions
- Confusing the domain (a set of objects) with predicates (relations on that domain).
- Thinking there is only one correct domain rather than considering different possible domains.

## Explainer

In propositional logic, truth values are assigned directly to atomic propositions — P is simply true or false, with no further explanation needed. First-order logic is different: it quantifies *over objects*. To give meaning to "every x is mortal" or "there exists an x greater than 0," you need to specify what objects x ranges over and what the predicates mean. A **structure** provides exactly this: it pairs a **domain** (a non-empty set of objects) with interpretations of all the predicates, function symbols, and constants in the language. Without a structure, a first-order formula has no truth value — it is purely syntactic.

Consider the language of arithmetic: it has a constant 0, a unary function S (successor), binary functions + and ·, and a binary predicate <. The **standard structure** ℕ interprets 0 as zero, S as "add 1," + and · as standard arithmetic, and < as the usual ordering. But the same language admits *other* structures: the integers ℤ, or a finite ring ℤ/nℤ, or even a structure built from strings if we define the operations artificially. The formula ∀x ∃y (y = S(x)) — "every element has a successor" — is true in ℕ and ℤ, but its meaning depends entirely on what S^M means in the structure M. This separation of *syntax* (the language, fixed) from *semantics* (the structure, variable) is the foundation of model theory.

A structure M consists of: a non-empty set |M| called the **domain** (also written M or U), an **interpretation** P^M ⊆ |M|ⁿ for each n-ary predicate symbol P (a set of n-tuples satisfying the property), an interpretation f^M : |M|ⁿ → |M| for each n-ary function symbol f, and an element c^M ∈ |M| for each constant symbol c. The domain is the universe of discourse; the interpretations assign concrete meaning to the abstract symbols. Notice the move from predicate to relation: the predicate symbol < becomes a set of pairs {(a, b) : a < b} in ℕ. This set-theoretic representation of properties is what makes formal semantics compositional and precise.

Understanding structures clarifies why the same sentence can be true in one model and false in another. "There exists an element with no predecessor" is true in ℕ (the number 0) but false in ℤ (every integer has one). "Every element has an additive inverse" is false in ℕ but true in ℤ. The structure is the *context* that determines truth — there is no absolute truth for non-logical statements, only truth-in-a-structure. This is why **model theory** asks not "is this formula true?" but "in which structures is this formula true?" The formula defines a class of structures (its *models*), and the theory of those structures is the set of all sentences true in all of them. Every first-order reasoning task — satisfiability, validity, proof — is ultimately a question about which structures satisfy which formulas.
