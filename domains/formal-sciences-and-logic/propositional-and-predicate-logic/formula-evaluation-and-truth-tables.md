---
id: formula-evaluation-and-truth-tables
title: Formula Evaluation and Truth Tables
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-functions-and-interpretation
  type: hard
- id: propositional-syntax
  type: hard
- id: truth-tables-and-evaluation
  type: soft
- id: boolean-functions-and-circuits
  type: soft
builds-toward:
- logical-equivalence-formulas
tags:
- propositional-logic
- truth-tables
- semantic-analysis
stage: formal-systems
status: validated
---

# Formula Evaluation and Truth Tables

## Core Idea
A truth table systematically lists all possible truth assignments to atomic formulas and computes the resulting truth value of a complex formula. This mechanical method makes it easy to determine whether a formula is always true (tautology), sometimes true (contingent), or never true (contradiction).

## How It's Best Learned
Build truth tables by hand for increasingly complex formulas, working column by column. Use software tools to verify your work and explore patterns in larger formulas.

## Common Misconceptions
- Errors in operator precedence when building truth tables—always clarify parentheses.
- Thinking a truth table proves something rather than just computing truth values for all cases.

## Questions

```yaml
- question: "A propositional formula contains 4 distinct atomic propositions (P, Q, R, S). How many rows does its complete truth table have?"
  type: multiple-choice
  options:
    - "4 rows — one row per atomic proposition"
    - "8 rows — 2 × 4"
    - "16 rows — 2⁴"
    - "256 rows — 4⁴"
  answer: 2
  explanation: "Each atomic proposition is independently assigned either T or F. With n atomic propositions, there are 2ⁿ possible combinations: 2 × 2 × ... × 2 (n times). For 4 propositions: 2⁴ = 16 rows. Option A confuses the number of rows with the number of atoms. Option D (4⁴) would apply if each atom had 4 possible values rather than 2. The exponential growth of truth table size with the number of atoms is why propositional tautology-checking becomes computationally expensive for large formulas — it is a coNP-complete problem."

- question: "A student builds a truth table for ¬(P ∧ Q) → (¬P ∨ ¬Q) and finds the final column is all T (true in every row). What can she conclude?"
  type: multiple-choice
  options:
    - "The formula is contingent — it happens to be true for all current truth values of P and Q"
    - "The formula is a tautology — it is true under every possible interpretation, demonstrating De Morgan's Law as a logical truth"
    - "The formula is a contradiction — all-true final columns indicate unsatisfiability"
    - "The formula is valid only when P and Q are both true"
  answer: 1
  explanation: "A formula is a tautology if and only if its truth table final column contains all T. This formula — which expresses De Morgan's Law — is indeed a tautology: ¬(P ∧ Q) and ¬P ∨ ¬Q are logically equivalent, so the biconditional (and therefore the implication in both directions) holds under every interpretation. Option A misuses 'contingent': contingent means SOMETIMES true, SOMETIMES false. All-T means true regardless of what P and Q mean — it's a logical truth, not a fact about any particular domain."

- question: "A formula that is true in 15 out of 16 rows of its truth table is a tautology."
  type: true-false
  answer: false
  explanation: "A tautology must be true in ALL rows — every possible truth assignment yields T. A formula that is false in even a single row is not a tautology; it is contingent (sometimes true, sometimes false). There is no 'almost tautology' classification in classical logic. The single false row is enough to show that there exists an interpretation under which the formula fails, disqualifying it from tautological status. This is why truth tables are a complete decision procedure: you cannot conclude a formula is a tautology without checking every row."

- question: "Two propositional formulas are logically equivalent if and only if they produce identical columns in their joint truth table."
  type: true-false
  answer: true
  explanation: "Logical equivalence is defined semantically: two formulas φ and ψ are logically equivalent (φ ⟺ ψ) if they have the same truth value under every possible interpretation. The truth table directly tests this: identical columns mean they agree on all 2ⁿ possible assignments. An equivalent formal characterization: φ ↔ ψ is a tautology. Both characterizations are equivalent. This semantic notion of equivalence is what makes truth tables useful for verifying logical laws like De Morgan's, double negation, and distribution — each law is just a claim that two formula schemas have identical truth tables."

- question: "What is the difference between a tautology, a contradiction, and a contingent formula? Give a simple example of each."
  type: short-answer
  answer: "A tautology is true under every possible truth assignment — its truth table final column is all T. Example: P ∨ ¬P (the law of excluded middle — P is either true or false, so one of P or ¬P is always true). A contradiction is false under every possible truth assignment — its truth table final column is all F. Example: P ∧ ¬P (P cannot be both true and false simultaneously). A contingent formula is sometimes true and sometimes false — its truth table final column contains both T and F. Example: P ∧ Q (true when both P and Q are true, false otherwise)."
  explanation: "These three categories are exhaustive and mutually exclusive — every propositional formula falls into exactly one of them. The practical importance: tautologies are logical truths that hold regardless of interpretation (useful as inference rules); contradictions are always false (their negations are tautologies, a useful proof technique); contingent formulas make substantive claims that could be true or false depending on the world. Truth tables settle the classification mechanically and definitively."
```

## Explainer

You already know from propositional syntax how to read a formula's structure: connectives (¬, ∧, ∨, →, ↔) combine atomic propositions according to a grammar. You know from truth functions and interpretation that each connective is a function from truth values to truth values — ¬ flips T to F, ∧ outputs T only when both inputs are T, and so on. **Formula evaluation** is just the process of applying these functions layer by layer to compute the overall truth value of a complex formula under a specific assignment.

A **truth table** is the systematic method for doing this across *all possible* assignments at once. If a formula contains n distinct atomic propositions, there are 2ⁿ possible rows — one for each assignment of T or F to every atom. The table has columns for each atom, columns for each intermediate subformula, and a final column for the whole formula. You fill it in left to right, bottom up through the formula's parse tree, because each subformula's value depends only on its children's values.

The payoff is a complete classification of the formula. If the final column is all T, the formula is a **tautology** — it is true under every interpretation, regardless of what the atoms mean. The formula (P → P) is a tautology: whether P is true or false, the implication holds. If the final column is all F, the formula is a **contradiction** — unsatisfiable. If the column has both T and F entries, the formula is **contingent**: sometimes true, sometimes false, depending on how you interpret the atoms.

The key skill to build is working column by column through subformulas before reaching the main connective. For a formula like ¬(P ∧ Q) → (¬P ∨ ¬Q), you first compute P ∧ Q, then ¬(P ∧ Q), then ¬P, then ¬Q, then ¬P ∨ ¬Q, then the full implication. Skipping steps and trying to evaluate the whole formula at once is where errors enter. The mechanical discipline of the column-by-column approach is not busywork — it mirrors the recursive structure of the formula's syntax tree and makes correctness checkable.

Truth tables are finite, complete, and decision-procedure: for any propositional formula, the table always terminates and definitively answers whether it is a tautology, contradiction, or contingency. This is the semantic approach to logic. Later, you will meet proof-theoretic methods (derivations, sequent calculi) that establish the same results by symbol manipulation rather than exhaustive enumeration. The equivalence of these two methods — that semantic tautology coincides with provability — is what soundness and completeness theorems establish.
