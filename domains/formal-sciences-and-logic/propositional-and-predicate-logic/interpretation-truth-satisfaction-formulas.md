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
