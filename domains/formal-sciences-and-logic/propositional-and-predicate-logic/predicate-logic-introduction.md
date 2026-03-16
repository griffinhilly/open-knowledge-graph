---
id: predicate-logic-introduction
title: Introduction to Predicate Logic (First-Order Logic)
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-logic-introduction
  type: hard
- id: set-fundamentals
  type: hard
- id: functions-and-function-properties
  type: hard
- id: domain-and-range
  type: soft
builds-toward:
- predicates-and-relations-fol
- quantifier-notation-and-basics
- first-order-logic-syntax
tags:
- foundations
- first-order-logic
- introduction
stage: formal-systems
status: draft
---

# Introduction to Predicate Logic (First-Order Logic)

## Core Idea
Predicate logic extends propositional logic by introducing predicates (properties and relations), variables, and quantifiers. Instead of treating 'Socrates is mortal' as atomic, predicate logic breaks it into a predicate applied to an individual. This enables formal reasoning about all objects with a property or about objects' existence.

## How It's Best Learned
Compare propositional and predicate formulations of the same statements. Practice translating English sentences with 'all' and 'some' into formal notation. Examine why propositional logic cannot express 'All humans are mortal; Socrates is human; therefore, Socrates is mortal.'

## Common Misconceptions
Thinking predicate logic is just different notation. Confusing when to use universal vs. existential quantifiers. Assuming quantifiers don't change fundamental decidability properties.

## Explainer

Propositional logic treats statements like "Socrates is mortal" as indivisible atoms — the letter P either stands for the whole claim or it doesn't. This works for reasoning about fixed named facts, but breaks down the moment you want to say something about *all* members of a class or about the *existence* of something. "All humans are mortal" and "There exists a prime number greater than 1000" cannot be expressed in propositional logic, because they involve quantification over a domain of objects. **Predicate logic** — also called first-order logic — extends propositional logic by introducing exactly the machinery needed to express these patterns.

The core additions are three: **predicates**, **variables**, and **quantifiers**. A predicate like Human(x) expresses a *property* that an object x may or may not have. A function like mother(x) maps one object to another. Variables range over a **domain** — the set of objects you're talking about — and quantifiers bind those variables. You already know what a domain and range of a function are; the domain in predicate logic plays the same role: it is the universe of discourse over which variables take values. The universal quantifier ∀x Human(x) → Mortal(x) says: for every object x in the domain, if x is human, then x is mortal. No single atomic proposition in propositional logic can capture this.

The classical syllogism "All humans are mortal; Socrates is human; therefore, Socrates is mortal" exposes exactly why propositional logic is insufficient. In propositional logic you'd need three unrelated atoms P, Q, R and no formal connection between them. In predicate logic you have: (1) ∀x Human(x) → Mortal(x), (2) Human(socrates), and from these you derive (3) Mortal(socrates) by instantiating the universal with x = socrates. The proof is valid *because of the logical structure*, not by coincidence. The connection between your set-theory prerequisite and predicate logic is direct: ∀x P(x) is essentially a claim about every element of the domain set; ∃x P(x) is a claim that the extension of P (the subset of domain elements satisfying P) is nonempty.

A critical insight — noted in your common misconceptions — is that predicate logic is not merely different notation. It is fundamentally more expressive and fundamentally harder. Propositional logic is **decidable**: there is an algorithm (truth tables) that determines, for any formula, whether it is a tautology. Predicate logic is **undecidable**: no algorithm can determine for an arbitrary first-order formula whether it is valid. This is not a shortcoming of current technology — it is a theorem (the negative answer to Hilbert's Entscheidungsproblem, proved by Church and Turing independently in 1936). You can enumerate valid formulas, but you cannot systematically check all formulas for validity. This greater expressive power — the ability to talk about all objects in a domain, about relations between objects, and about existence — comes with this fundamental computational cost.

