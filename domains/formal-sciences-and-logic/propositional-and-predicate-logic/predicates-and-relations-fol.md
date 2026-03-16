---
id: predicates-and-relations-fol
title: Predicates and Relations in First-Order Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: predicate-logic-introduction
  type: hard
- id: binary-relations
  type: soft
- id: functions-and-function-properties
  type: soft
builds-toward:
- quantifier-notation-and-basics
- terms-and-atomic-formulas
tags:
- semantics
- first-order-logic
- predicates
stage: formal-systems
status: draft
---

# Predicates and Relations in First-Order Logic

## Core Idea
A predicate is a function from objects to truth values. Unary predicates express properties (e.g., Red(x)); binary predicates express relations (e.g., Loves(x, y)). Predicates represent the internal structure of propositions and allow reasoning about shared properties across objects.

## Explainer

In propositional logic — your prerequisite — the atomic unit is a proposition like P or Q, which is just a letter that is either true or false. This works fine for isolated claims, but it is blind to internal structure. The sentence "Alice is tall" and the sentence "Bob is tall" share something: both assert the same property of different objects. Propositional logic treats them as completely unrelated atomic symbols. **First-order logic** (FOL) breaks sentences open by separating the **predicate** (the property or relation being asserted) from the **terms** (the objects it is asserted about).

A **unary predicate** like Tall(x) is a template with one slot. Fill the slot with "Alice" and you get the proposition Tall(Alice), which is either true or false depending on the interpretation. Fill it with "Bob" and you get a different proposition. Formally, a predicate of arity n is a function from n-tuples of domain objects to {true, false} — equivalently, it picks out the subset of all n-tuples for which it holds. Tall picks out the set of tall things; Red picks out the set of red things. The extension of a predicate is this set; the predicate symbol itself is just a name for it within the language.

**Binary predicates** introduce **relations** between objects. Loves(Alice, Bob) differs from Loves(Bob, Alice) — order matters, and this is where your prerequisite knowledge of binary relations connects directly. A binary relation, as you have seen, is a set of ordered pairs. In FOL, a binary predicate symbol denotes a relation — specifically, the set of pairs (a, b) for which the predicate is true. GreaterThan(x, y) picks out pairs where x > y; Parent(x, y) picks out pairs where x is a parent of y. The same object can appear in multiple positions, and the relation need not be symmetric.

The real power of predicates comes from combining them with **quantifiers** (covered in your next topics). Where propositional logic is stuck with finite lists of atomic propositions, first-order logic with predicates can express universal patterns: "everything that is Red is also Colored," "there exists someone who Loves everyone." These statements do not name specific objects — they use predicate structure to make general claims across an entire domain. The predicate is the bridge between the structure of the world (which objects exist and which relations hold) and the structure of the language (which symbols we use to reason about them).

One subtlety worth noting: a predicate symbol like Red has no meaning until it is given an **interpretation** — a domain of objects and an assignment of each predicate symbol to an actual set or relation on that domain. The same formula Red(x) is true in an interpretation where "x" refers to a fire engine but false in one where "x" refers to the sky. This separation between the formal language and its interpretations is the core insight of model-theoretic semantics, and it starts here, with the concept of predicates and their extensions.

