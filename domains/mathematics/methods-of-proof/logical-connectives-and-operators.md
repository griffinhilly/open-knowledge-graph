---
id: logical-connectives-and-operators
title: Logical Connectives and Operators
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-values-and-statements
  type: hard
builds-toward:
- truth-tables-and-evaluation
- logical-equivalence
- conditional-implication-statements
tags:
- logic
- connectives
- and
- or
- not
stage: formal-systems
status: draft
---

# Logical Connectives and Operators

## Core Idea
Logical connectives (AND, OR, NOT) combine or modify statements to form new statements. AND (∧) is true when both statements are true; OR (∨) is true when at least one is true; NOT (¬) reverses the truth value. These are the basic building blocks for constructing complex logical expressions.

## How It's Best Learned
Use truth tables and real examples to see how each connective works. Practice building compound statements from simple ones.

## Common Misconceptions
- Confusing AND with OR in everyday language.
- Thinking NOT applies only to the first word of a statement.
- Misunderstanding that OR is inclusive (both can be true).

## Explainer

You already know that statements have truth values — every proposition is either true or false. Logical connectives are the tools for building compound statements out of simpler ones. Think of them as operations on truth values, just as addition and multiplication are operations on numbers. The three fundamental connectives — AND, OR, and NOT — are enough to express any logical relationship, and understanding them precisely is the first step toward rigorous mathematical reasoning.

**Negation** (NOT, written ¬P) simply flips a statement's truth value. If P is the statement "n is even," then ¬P is "n is not even," which is "n is odd." Negation applies to the entire statement it prefixes, not just the first word. When you negate "n is even and positive," you get "it is not the case that n is even and positive" — equivalently, "n is odd or non-positive." This is De Morgan's law in disguise, and the subtlety is that negation distributes through AND and OR in a non-obvious way.

**Conjunction** (AND, written P ∧ Q) asserts that both P and Q are true simultaneously. The truth table has exactly one row where the output is true: the row where both inputs are true. In everyday mathematics, AND appears in conditions like "x > 0 and x < 5" — both inequalities must hold. The key precision: P ∧ Q is false if either component is false. This seems obvious, but it matters when constructing definitions. "A function is continuous and differentiable" requires both properties to hold, and a single counterexample to either one defeats the whole claim.

**Disjunction** (OR, written P ∨ Q) asserts that at least one of P or Q is true. Mathematical OR is **inclusive**: P ∨ Q is true even when both P and Q are true. This differs from everyday English, where "or" often implies exclusivity ("you can have cake or pie" usually means not both). In logic and mathematics, "p is even or p is divisible by 3" is true for p = 6 even though both conditions hold. There is a separate connective for exclusive-or (XOR), but ordinary mathematical practice uses inclusive OR by default.

These three connectives are the vocabulary of logical expressions. Every compound statement you encounter in proofs — "if P then Q," "P if and only if Q," "there exists x such that P(x)" — ultimately unpacks into combinations of AND, OR, and NOT applied to atomic statements. Mastering their precise truth conditions now prevents cascading errors later, especially when negating complex hypotheses (the step that starts many proof-by-contradiction and contrapositive arguments).
