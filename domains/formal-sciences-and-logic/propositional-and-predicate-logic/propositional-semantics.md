---
id: propositional-semantics
title: Propositional Semantics and Valuations
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
- id: truth-tables
  type: hard
builds-toward:
- tautologies-and-contradictions
- propositional-soundness-completeness
- modal-logic-intro
tags:
- semantics
- valuation
- truth-assignment
- satisfaction
stage: formal-systems
status: draft
---

# Propositional Semantics and Valuations

## Core Idea
Propositional semantics assigns meaning to WFFs via a valuation: a function mapping each atomic proposition to a truth value (true or false). The valuation extends compositionally to all WFFs — the truth value of a compound formula is determined entirely by the truth values of its parts and the semantics of the connective. A formula φ is satisfied by a valuation v (written v ⊨ φ) if v makes φ true. This compositional definition is the formal foundation underlying every truth table.

## How It's Best Learned
Evaluate formulas on explicit valuations before using full truth tables. Map the recursive evaluation to tree traversal: assign values at leaves (atoms), then propagate upward through connectives.

## Common Misconceptions
- Thinking semantics is the same as syntax — valuations live outside the formula.
- Confusing 'satisfiable' (true under some valuation) with 'valid' (true under all valuations).
