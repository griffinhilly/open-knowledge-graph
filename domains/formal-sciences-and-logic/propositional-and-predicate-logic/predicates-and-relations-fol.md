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
status: validated
---

# Predicates and Relations in First-Order Logic

## Core Idea
A predicate is a function from objects to truth values. Unary predicates express properties (e.g., Red(x)); binary predicates express relations (e.g., Loves(x, y)). Predicates represent the internal structure of propositions and allow reasoning about shared properties across objects.

## Questions

```yaml
- question: "A student claims: 'The formula Tall(Alice) is true because Tall means tall and Alice is clearly a tall person.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — predicates in FOL are defined by their English-language meanings"
    - "It is correct for unary predicates but does not generalize to binary predicates"
    - "The truth of Tall(Alice) depends on the interpretation — without a specified domain and assignment of Tall to an extension, the formula has no truth value at all"
    - "The student should have written Tall(x) with a variable, not a constant term"
  answer: 2
  explanation: "This is the core insight of model-theoretic semantics: predicate symbols have no inherent meaning. The symbol 'Tall' is just syntax until an interpretation assigns it a set of domain objects (its extension). In an interpretation where Alice refers to a 5-foot person and Tall picks out people over 6 feet, Tall(Alice) is false. Truth is relative to an interpretation, not to the name of the symbol."

- question: "Which of the following best captures what the 'extension' of a binary predicate like GreaterThan(x, y) is?"
  type: multiple-choice
  options:
    - "A function that takes two number names as input and returns a number"
    - "The set of ordered pairs (a, b) from the domain for which GreaterThan(a, b) holds true"
    - "The meaning of the predicate symbol, fixed independently of any interpretation"
    - "The result of applying the predicate to specific terms, which yields a truth value"
  answer: 1
  explanation: "An n-ary predicate's extension is the set of n-tuples from the domain satisfying the predicate. For a binary predicate, the extension is a set of ordered pairs. This connects directly to your prerequisite on binary relations: a relation is a set of ordered pairs, and a binary predicate in FOL denotes exactly such a relation under a given interpretation. Option C is wrong: the extension is given by the interpretation, not by the symbol itself."

- question: "In FOL, the predicate symbol Red has a fixed meaning: it picks out the set of all red things in the domain."
  type: true-false
  answer: false
  explanation: "Predicate symbols in FOL are uninterpreted — they are just names. The symbol Red gains meaning only when an interpretation assigns it an extension: a specific set of domain objects. Under one interpretation, Red might pick out fire engines; under another, it might pick out nothing at all. This is the fundamental distinction between the formal language (syntax) and its interpretations (semantics)."

- question: "A unary predicate in FOL can be understood as picking out a subset of the domain — the set of all objects for which the predicate holds true under a given interpretation."
  type: true-false
  answer: true
  explanation: "A unary predicate of arity 1 is semantically equivalent to a characteristic function: it classifies each domain object as either in or out of the set it defines. The extension of a unary predicate is exactly this subset. This view generalizes: an n-ary predicate's extension is a set of n-tuples (a relation). The subset/relation view makes the connection between FOL predicates and set-theoretic relations precise."

- question: "Why does first-order logic require a separate 'interpretation' for formulas to have truth values, and what does an interpretation specify?"
  type: short-answer
  answer: "FOL is a formal language: its symbols — predicate names, function symbols, constants — carry no inherent meaning. An interpretation gives them meaning by specifying: (1) a non-empty domain of objects, (2) an assignment of each constant symbol to a specific domain object, (3) an assignment of each predicate symbol to a relation (set of tuples) on the domain, and (4) an assignment of each function symbol to a function on the domain. Without these assignments, formulas are just syntax — neither true nor false. With them, every closed formula has a definite truth value."
  explanation: "This interpretation-dependence is the core insight of model-theoretic semantics: truth is not a property of formulas alone but of formulas relative to models. The same formula can be true in one model and false in another. This framework allows logicians to study validity (true in all interpretations), satisfiability (true in some), and consequence (true in all interpretations satisfying the premises) with mathematical precision."
```

## Explainer

In propositional logic — your prerequisite — the atomic unit is a proposition like P or Q, which is just a letter that is either true or false. This works fine for isolated claims, but it is blind to internal structure. The sentence "Alice is tall" and the sentence "Bob is tall" share something: both assert the same property of different objects. Propositional logic treats them as completely unrelated atomic symbols. **First-order logic** (FOL) breaks sentences open by separating the **predicate** (the property or relation being asserted) from the **terms** (the objects it is asserted about).

A **unary predicate** like Tall(x) is a template with one slot. Fill the slot with "Alice" and you get the proposition Tall(Alice), which is either true or false depending on the interpretation. Fill it with "Bob" and you get a different proposition. Formally, a predicate of arity n is a function from n-tuples of domain objects to {true, false} — equivalently, it picks out the subset of all n-tuples for which it holds. Tall picks out the set of tall things; Red picks out the set of red things. The extension of a predicate is this set; the predicate symbol itself is just a name for it within the language.

**Binary predicates** introduce **relations** between objects. Loves(Alice, Bob) differs from Loves(Bob, Alice) — order matters, and this is where your prerequisite knowledge of binary relations connects directly. A binary relation, as you have seen, is a set of ordered pairs. In FOL, a binary predicate symbol denotes a relation — specifically, the set of pairs (a, b) for which the predicate is true. GreaterThan(x, y) picks out pairs where x > y; Parent(x, y) picks out pairs where x is a parent of y. The same object can appear in multiple positions, and the relation need not be symmetric.

The real power of predicates comes from combining them with **quantifiers** (covered in your next topics). Where propositional logic is stuck with finite lists of atomic propositions, first-order logic with predicates can express universal patterns: "everything that is Red is also Colored," "there exists someone who Loves everyone." These statements do not name specific objects — they use predicate structure to make general claims across an entire domain. The predicate is the bridge between the structure of the world (which objects exist and which relations hold) and the structure of the language (which symbols we use to reason about them).

One subtlety worth noting: a predicate symbol like Red has no meaning until it is given an **interpretation** — a domain of objects and an assignment of each predicate symbol to an actual set or relation on that domain. The same formula Red(x) is true in an interpretation where "x" refers to a fire engine but false in one where "x" refers to the sky. This separation between the formal language and its interpretations is the core insight of model-theoretic semantics, and it starts here, with the concept of predicates and their extensions.

