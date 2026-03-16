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
- id: logical-equivalences
  type: soft
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
status: validated
---

# Propositional Semantics and Valuations

## Core Idea
Propositional semantics assigns meaning to WFFs via a valuation: a function mapping each atomic proposition to a truth value (true or false). The valuation extends compositionally to all WFFs — the truth value of a compound formula is determined entirely by the truth values of its parts and the semantics of the connective. A formula φ is satisfied by a valuation v (written v ⊨ φ) if v makes φ true. This compositional definition is the formal foundation underlying every truth table.

## How It's Best Learned
Evaluate formulas on explicit valuations before using full truth tables. Map the recursive evaluation to tree traversal: assign values at leaves (atoms), then propagate upward through connectives.

## Common Misconceptions
- Thinking semantics is the same as syntax — valuations live outside the formula.
- Confusing 'satisfiable' (true under some valuation) with 'valid' (true under all valuations).

## Questions

```yaml
- question: "Consider the formula P ∧ ¬P. Under propositional semantics, this formula is:"
  type: multiple-choice
  options:
    - "Satisfiable but not valid"
    - "Valid but not satisfiable"
    - "Neither satisfiable nor valid"
    - "Both satisfiable and valid"
  answer: 2
  explanation: "P ∧ ¬P is a contradiction: for any valuation, exactly one of P and ¬P is false, so the conjunction is always false. It is not satisfiable (no valuation makes it true) and therefore certainly not valid (which would require truth under all valuations). Options A and D require at least one satisfying valuation, which does not exist. Option B is impossible — validity implies satisfiability."

- question: "A formula that is true under every possible valuation is called satisfiable."
  type: true-false
  answer: false
  explanation: "A formula true under every valuation is called valid (or a tautology). Satisfiable means only that there exists at least one valuation making it true. Every valid formula is satisfiable (if it is true under all valuations, it is certainly true under some), but not every satisfiable formula is valid. For example, P is satisfiable (true when v(P) = true) but not valid (false when v(P) = false)."

- question: "Using compositionality, evaluate the formula (P → Q) ∧ ¬R under the valuation v(P) = true, v(Q) = false, v(R) = false. What is the truth value, and how does compositionality determine it step by step?"
  type: short-answer
  answer: "The formula is false. Step 1: v(¬R) = ¬false = true. Step 2: v(P → Q) = v(¬P ∨ Q) = false (since P is true and Q is false, the implication is false). Step 3: v((P → Q) ∧ ¬R) = false ∧ true = false."
  explanation: "Compositionality means we never need to inspect the internal structure of a subformula once we know its truth value — we only combine truth values using the connective's truth table. Each step takes the values of immediate subformulas as inputs and produces the value of the compound formula as output, working from atoms up through the parse tree."
```

## Explainer

From propositional syntax, you know that well-formed formulas (WFFs) are built recursively from atomic propositions using connectives like ¬, ∧, ∨, →, and ↔. Syntax gives you the grammar — the rules for forming valid expressions. Semantics is the separate question of what those expressions *mean*, and propositional semantics answers it via valuations.

A valuation is a function v that assigns exactly one of {true, false} to each atomic proposition. Once you fix a valuation, the truth value of every compound formula is completely determined. This is compositionality: the truth value of ¬φ depends only on the truth value of φ; the truth value of φ ∧ ψ depends only on the truth values of φ and ψ; and so on for each connective. You evaluate a formula bottom-up through its parse tree — assign values at the leaves (atoms), then propagate up through the connective nodes using the standard truth tables.

The satisfaction relation v ⊨ φ (read: "v satisfies φ" or "φ is true under v") is just the statement that the compositional evaluation of φ under v yields true. This is the formal underpinning of every truth table: a row in a truth table is precisely one valuation, and the final column records whether that valuation satisfies the formula.

The two most important semantic properties of a formula are satisfiability and validity. A formula is satisfiable if there exists at least one valuation that satisfies it — at least one row of the truth table comes out true. A formula is valid (a tautology) if every valuation satisfies it — every row is true. These are not the same, and confusing them is the most common error at this stage. P ∨ ¬P is valid (always true — try it). P ∧ Q is satisfiable but not valid (true only when both are true). P ∧ ¬P is not even satisfiable — a contradiction. These four categories (valid, satisfiable-but-not-valid, unsatisfiable, and their overlaps) exhaust all possibilities.

The final point to internalize is that valuations are external to formulas — they are not part of the syntax but are applied to it. A formula by itself is just a string of symbols. It takes on a truth value only relative to a valuation. When we say "this formula is true," we always mean true under some specified or implied valuation. This separation between the syntactic object (the formula) and the semantic judgment (its truth under a valuation) is foundational for everything that follows in soundness and completeness theory.
