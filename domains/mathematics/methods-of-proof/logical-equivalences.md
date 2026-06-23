---
id: logical-equivalences
title: Logical Equivalences
domain: mathematics
course: methods-of-proof
prerequisites:
- id: truth-tables
  type: hard
- id: conditional-and-biconditional
  type: soft
- id: logical-equivalence-intro
  type: hard
- id: propositional-logic-basics
  type: hard
builds-toward:
- de-morgans-laws
- proof-structure-and-terminology
tags:
- equivalence
- transformation
- logic
stage: formal-systems
status: validated
---

# Logical Equivalences

## Core Idea
Two statements are logically equivalent if they have identical truth values in all cases. Key equivalences like p → q ≡ ¬p ∨ q allow rewriting statements in different forms, essential for proof construction.

## Questions

```yaml
- question: "You want to prove 'If a number is divisible by 4, then it is divisible by 2' but find a direct proof difficult. Which of the following is logically equivalent and might offer a cleaner approach?"
  type: multiple-choice
  options:
    - "If a number is divisible by 2, then it is divisible by 4 — the converse"
    - "A number is not divisible by 4 and not divisible by 2 — negation of both parts"
    - "If a number is not divisible by 2, then it is not divisible by 4 — the contrapositive"
    - "A number is divisible by 4 or not divisible by 2 — a disjunction"
  answer: 2
  explanation: "The contrapositive of 'if p then q' is 'if not q then not p,' and they are logically equivalent — they have identical truth tables. This means proving the contrapositive is not a workaround or an approximation; it proves the original statement exactly. The converse (option A) is a different claim entirely and is not equivalent to the original. The contrapositive is a valid proof strategy specifically because of this logical equivalence."

- question: "A student negates the statement 'It is raining and it is cold' by writing 'It is not raining and it is not cold.' Is this correct?"
  type: multiple-choice
  options:
    - "Yes — negation distributes directly over 'and,' so each part is negated"
    - "No — by De Morgan's law, the correct negation is 'It is not raining or it is not cold'"
    - "Yes — negating each part separately always gives the correct negation"
    - "No — negating a conjunction always requires negating the entire statement without changing the connective"
  answer: 1
  explanation: "De Morgan's law states that ¬(p ∧ q) ≡ ¬p ∨ ¬q. When you negate a conjunction, the 'and' becomes 'or' — the connective flips. The statement 'It is raining and it is cold' is false as soon as either condition fails, which is exactly what 'It is not raining OR it is not cold' captures. The student's error — keeping 'and' while negating each part — produces a stronger statement that requires both conditions to fail simultaneously, which is incorrect."

- question: "Two statements are logically equivalent if there is at least one row in their truth tables where they have the same truth value."
  type: true-false
  answer: false
  explanation: "Logical equivalence requires that the statements match in every row of their truth tables — not just some. Two completely unrelated statements might happen to be both true in some cases without being equivalent. Equivalence is a much stronger condition: P ≡ Q means P and Q have identical truth values for every possible combination of truth values of their component variables. Anything less than complete agreement across all rows is not equivalence."

- question: "Proving the contrapositive of a conditional statement is a legitimate proof strategy because the contrapositive is logically equivalent to the original statement."
  type: true-false
  answer: true
  explanation: "Logical equivalence means the two statements have identical truth values in every case, so any proof of one is automatically a proof of the other. The contrapositive of p → q is ¬q → ¬p, and their truth tables are identical — both are false only when p is true and q is false. This is not a trick or a shortcut but a genuine substitution: when two statements are equivalent, you can replace one with the other anywhere in a proof."

- question: "Why does the equivalence p → q ≡ ¬p ∨ q explain why assuming the hypothesis in a direct proof is a valid strategy?"
  type: short-answer
  answer: "The equivalence says 'if p then q' means the same thing as 'either p is false or q is true.' To prove this disjunction, the only interesting case is when p is true — because if p is false, the disjunction ¬p ∨ q is immediately true regardless of q. So you only need to handle the case where p holds. Assuming the hypothesis p in a direct proof is exactly this: you are focusing on the one case that requires proof, and showing q follows. The equivalence explains why this suffices."
  explanation: "This rewriting also explains why a conditional with a false hypothesis is vacuously true: if p is false, ¬p is true, so ¬p ∨ q is true regardless of q. The logical equivalence between implication and disjunction is the foundation for understanding why conditional proofs work the way they do."
```

## Explainer

From your work with truth tables, you know how to determine whether a compound statement is true or false for any specific combination of truth values. Logical equivalence takes that one step further: two statements are **logically equivalent** if their truth tables are identical column by column — they match in every single row, not just some. When P ≡ Q, you can replace one with the other anywhere in a proof without changing whether the proof is valid.

The most important equivalence in proof writing is the **contrapositive**: the statement "if p then q" (p → q) is logically equivalent to "if not q then not p" (¬q → ¬p). You can verify this with a truth table — both are false only when p is true and q is false, and true in every other case. Why does this matter? Because sometimes "if p then q" is hard to prove directly, while "if not q then not p" has a clear attack. Proving the contrapositive is not a trick or an approximation — it is exactly the same claim, just phrased differently.

A second critical equivalence rewrites implication as disjunction: p → q ≡ ¬p ∨ q. Reading it aloud: "if p then q" says the same thing as "either p is false, or q is true." This equivalence shows up constantly when manipulating logical expressions and when converting between different proof strategies. For example, to prove p → q, it suffices to assume p is true and show q follows — because if p is false, the disjunction ¬p ∨ q is already true. The equivalence explains why proof by assuming the hypothesis is valid: you're simply exploiting this rewriting.

A third family of equivalences is **De Morgan's laws**: ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q. These tell you how negation distributes over "and" and "or" — and the distribution flips the connective. Negating "it's raining and it's cold" yields "it's not raining or it's not cold," not "it's not raining and it's not cold." Fluency with these transformations is what allows you to negate complex mathematical statements correctly — an essential skill for proof by contradiction and proof by contrapositive that you'll use throughout mathematics.
