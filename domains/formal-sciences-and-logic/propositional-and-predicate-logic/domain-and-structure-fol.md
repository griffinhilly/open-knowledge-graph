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

## Questions

```yaml
- question: "The sentence 'every element has a predecessor' is false in ℕ (natural numbers) but true in ℤ (integers). What does this illustrate about first-order logic?"
  type: multiple-choice
  options:
    - "The sentence is ambiguous — its meaning depends on how 'predecessor' is informally defined"
    - "Truth in first-order logic is relative to a structure — the same sentence can be true in one structure and false in another"
    - "ℕ and ℤ use different logical systems, so comparison between them is invalid"
    - "Universal quantifier sentences are always harder to satisfy than existential ones"
  answer: 1
  explanation: "In ℕ, the element 0 has no predecessor (there is no natural number y with y + 1 = 0), so the sentence is false. In ℤ, every integer n has a predecessor n − 1, so the sentence is true. The sentence hasn't changed; only the structure (domain + interpretation of the function and predicate symbols) has changed. This is the defining feature of first-order model theory: truth is not absolute but always relative to a structure. A sentence defines a *class* of structures in which it is true, not a single truth value."

- question: "What components are required to define a first-order structure M for a language with a binary predicate symbol P, a unary function symbol f, and a constant symbol c?"
  type: multiple-choice
  options:
    - "A domain set |M|, a truth assignment for P, and numerical values for f and c"
    - "A non-empty domain |M|, a set of pairs P^M ⊆ |M|², a function f^M : |M| → |M|, and an element c^M ∈ |M|"
    - "A non-empty domain |M| and a single interpretation function mapping all symbols to domain elements"
    - "A domain |M|, axioms governing P, and a recursive definition of f in terms of P"
  answer: 1
  explanation: "A structure must provide the domain and a concrete interpretation for every symbol. For binary predicate P: the interpretation P^M is a set of ordered pairs from the domain — the set of (a, b) pairs for which P holds. For unary function f: f^M is a total function from the domain to itself. For constant c: c^M is a specific element of the domain. Without all components, quantified statements like ∀x P(x, f(x)) have no meaning — you cannot evaluate whether P holds of x and its f-image without knowing what f and P denote."

- question: "The same first-order sentence can be true in one structure and false in another structure for the same language."
  type: true-false
  answer: true
  explanation: "This is the fundamental fact about first-order semantics. The sentence 'there exists an element with no additive inverse' is true in (ℕ, +) — the number 0 has no additive inverse in ℕ — but false in (ℤ, +) — every integer n has the inverse −n. The sentence is syntactically identical in both cases; the structure provides the interpretation of the domain and operation that determines truth. This is why logicians ask 'in which structures is this formula satisfied?' rather than 'is this formula true?'"

- question: "The domain of a first-order structure can be the empty set."
  type: true-false
  answer: false
  explanation: "By definition, the domain of a first-order structure must be non-empty. This is a technical requirement with logical consequences: the universal quantifier ∀x φ(x) would be vacuously true over an empty domain (no elements to violate it), while the existential quantifier ∃x φ(x) would be vacuously false (no elements to witness it). These vacuous truth values create complications in standard first-order logic, so the convention requires at least one element in the domain. Some systems (free logic) relax this, but standard FOL maintains the non-emptiness requirement."

- question: "Explain why a first-order sentence like '∀x ∃y (x < y)' has no absolute truth value and must always be evaluated relative to a structure."
  type: short-answer
  answer: "The sentence contains quantifiers ranging over a domain and a predicate symbol <, but neither the domain nor the meaning of < is specified by the sentence itself. A structure must provide: (1) the domain (the set of objects x and y range over), and (2) the interpretation of < (which pairs (a, b) satisfy 'a < b' in that structure). In (ℕ, <), the sentence is true — every natural number has a larger one. In the structure ({1, 2, 3}, <), it is false — 3 has no element greater than it. The sentence's truth depends entirely on the structure."
  explanation: "This is the key contrast with propositional logic, where atomic propositions are assigned truth values directly. In first-order logic, atomic formulas involve variables ranging over a domain and predicates denoting relations on that domain. Without fixing the domain and the predicate interpretations, the formula is an open semantic object — it defines a property of structures (those in which it is true), not a single truth value. Model theory exploits this: the set of all structures satisfying a collection of sentences defines a mathematical theory, and studying which structures satisfy it reveals the content of the axioms."
```

## Explainer

In propositional logic, truth values are assigned directly to atomic propositions — P is simply true or false, with no further explanation needed. First-order logic is different: it quantifies *over objects*. To give meaning to "every x is mortal" or "there exists an x greater than 0," you need to specify what objects x ranges over and what the predicates mean. A **structure** provides exactly this: it pairs a **domain** (a non-empty set of objects) with interpretations of all the predicates, function symbols, and constants in the language. Without a structure, a first-order formula has no truth value — it is purely syntactic.

Consider the language of arithmetic: it has a constant 0, a unary function S (successor), binary functions + and ·, and a binary predicate <. The **standard structure** ℕ interprets 0 as zero, S as "add 1," + and · as standard arithmetic, and < as the usual ordering. But the same language admits *other* structures: the integers ℤ, or a finite ring ℤ/nℤ, or even a structure built from strings if we define the operations artificially. The formula ∀x ∃y (y = S(x)) — "every element has a successor" — is true in ℕ and ℤ, but its meaning depends entirely on what S^M means in the structure M. This separation of *syntax* (the language, fixed) from *semantics* (the structure, variable) is the foundation of model theory.

A structure M consists of: a non-empty set |M| called the **domain** (also written M or U), an **interpretation** P^M ⊆ |M|ⁿ for each n-ary predicate symbol P (a set of n-tuples satisfying the property), an interpretation f^M : |M|ⁿ → |M| for each n-ary function symbol f, and an element c^M ∈ |M| for each constant symbol c. The domain is the universe of discourse; the interpretations assign concrete meaning to the abstract symbols. Notice the move from predicate to relation: the predicate symbol < becomes a set of pairs {(a, b) : a < b} in ℕ. This set-theoretic representation of properties is what makes formal semantics compositional and precise.

Understanding structures clarifies why the same sentence can be true in one model and false in another. "There exists an element with no predecessor" is true in ℕ (the number 0) but false in ℤ (every integer has one). "Every element has an additive inverse" is false in ℕ but true in ℤ. The structure is the *context* that determines truth — there is no absolute truth for non-logical statements, only truth-in-a-structure. This is why **model theory** asks not "is this formula true?" but "in which structures is this formula true?" The formula defines a class of structures (its *models*), and the theory of those structures is the set of all sentences true in all of them. Every first-order reasoning task — satisfiability, validity, proof — is ultimately a question about which structures satisfy which formulas.
