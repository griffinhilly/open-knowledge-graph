---
id: logical-equivalence-propositional
title: Logical Equivalence in Propositional Logic
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: truth-assignments-and-valuations
  type: hard
builds-toward:
- normal-forms-cnf-dnf
- logical-equivalences
tags:
- semantics
- equivalence
- propositional
stage: formal-systems
status: draft
---

# Logical Equivalence in Propositional Logic

## Core Idea
Two formulas are logically equivalent if they have the same truth value under every possible truth assignment. Equivalence allows formulas to be substituted for one another and enables simplification. Standard equivalences include De Morgan's laws, double negation, and distributivity.

## How It's Best Learned
Verify equivalences using truth tables. Learn standard equivalence laws and apply them to rewrite and simplify formulas.

## Common Misconceptions
Confusing logical equivalence with material implication. Assuming formulas that 'sound similar' in English are equivalent.

## Explainer

You already know how truth assignments work: a truth assignment maps each propositional variable to true or false, and the truth value of a compound formula is determined compositionally by the connectives. **Logical equivalence** builds directly on this. Two formulas φ and ψ are **logically equivalent**, written φ ≡ ψ, if for every possible truth assignment, φ and ψ receive the same truth value — they always agree, no matter what the variables are set to. The standard way to check this is a joint truth table: if φ and ψ have matching columns across all rows, they are equivalent.

The payoff of equivalence is **substitution**: wherever φ appears in a larger formula, you can replace it with ψ without changing the truth value of the whole. This is what makes equivalence useful for simplification. Consider De Morgan's first law: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q). If you have a complex formula containing ¬(P ∧ Q), you can swap in (¬P ∨ ¬Q) freely. Standard equivalences — double negation (¬¬P ≡ P), commutativity, associativity, distribution, De Morgan's laws, implication as disjunction (P → Q ≡ ¬P ∨ Q) — are the rewrite rules you use to put formulas into simpler or canonical forms.

A key equivalence worth internalizing is the **implication** form: P → Q is not "P causes Q" or "P is similar to Q." It is equivalent to ¬P ∨ Q — the formula is false only when P is true and Q is false. This surprises many students because natural language "if-then" is not purely truth-functional. In logic, "if the moon is made of cheese, then 2+2=4" is true, because the antecedent is false. Recognizing P → Q ≡ ¬P ∨ Q lets you manipulate implications using the toolkit of disjunction.

The difference between **logical equivalence** and **material implication** is critical. φ → ψ says: in every assignment that makes φ true, ψ is also true — but ψ might be false when φ is false. φ ≡ ψ says: in every assignment, φ and ψ have the same truth value — they go up and down together. Equivalence is mutual implication: φ ≡ ψ holds if and only if both φ → ψ and ψ → φ hold. If you ever doubt whether two formulas are equivalent, the truth table test is decisive for propositional logic: equivalence fails if even one assignment produces different truth values for the two formulas.
