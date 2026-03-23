---
id: proof-by-contradiction-introduction
title: Introduction to Proof by Contradiction
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: direct-proof-introduction
    type: hard
  - id: converse-inverse-contrapositive-intro
    type: hard
  - id: counterexamples-in-reasoning
    type: soft
builds-toward:
  - when-is-something-proven
  - proof-by-contradiction
  - proving-by-contradiction
tags: [proof, contradiction, indirect-proof, reasoning]
stage: abstract-reasoning
status: draft
---

# Introduction to Proof by Contradiction

## Core Idea
Proof by contradiction works by assuming the opposite of what you want to prove and showing that this assumption leads to a logical impossibility — a contradiction. Since a contradiction cannot be true, the assumption must be false, which means the original statement must be true. This is an indirect proof strategy: instead of building toward the conclusion directly, you show that denying the conclusion breaks logic itself. It is especially useful when direct proof seems difficult or when the statement involves nonexistence or impossibility.

## How It's Best Learned
Start with a classic: proving that the square root of 2 is irrational. Assume it is rational (p/q in lowest terms), derive that both p and q must be even (contradicting "lowest terms"), conclude the assumption was false. Then practice with simpler examples: "Prove there is no largest integer." Assume there is a largest integer N; then N + 1 > N, contradicting the assumption. Emphasize the three-step structure: (1) assume the negation, (2) derive a contradiction, (3) conclude the original statement is true.

## Common Misconceptions
- Confusing proof by contradiction with proof by contrapositive. Contrapositive proves ¬Q → ¬P as a direct proof; contradiction assumes ¬(conclusion) and derives any absurdity — not necessarily ¬(hypothesis).
- Not identifying a clear contradiction. The derivation must reach a statement that is logically impossible (like "N is both even and odd"), not just surprising or unlikely.
- Thinking contradiction is always needed. Many statements that students prove by contradiction can be proven more simply by direct proof. Contradiction is a tool of last resort, not first resort.

## Questions

```yaml
- question: "In a proof by contradiction of 'There is no largest even number,' what do you assume?"
  type: multiple-choice
  options:
    - "There is no largest even number"
    - "There is a largest even number"
    - "All even numbers are larger than all odd numbers"
    - "The largest even number is 100"
  answer: 1
  explanation: "In proof by contradiction, you assume the negation of what you want to prove. The negation of 'there is no largest even number' is 'there is a largest even number.' You then show this leads to a contradiction — if N is the largest even number, then N + 2 is even and larger than N, contradicting the assumption."

- question: "In a proof by contradiction, if you successfully derive a contradiction, the original statement you wanted to prove is false."
  type: true-false
  answer: false
  explanation: "It is the opposite: deriving a contradiction means your ASSUMPTION (the negation of the original statement) is false. Since the negation is false, the original statement must be true. The contradiction proves the original statement, not disproves it."

- question: "Prove by contradiction that the sum of a rational number and an irrational number is irrational."
  type: short-answer
  answer: "Assume for contradiction that a is rational, b is irrational, and a + b = c is rational. Since a and c are rational, c - a is rational (rationals are closed under subtraction). But c - a = b, so b is rational. This contradicts our assumption that b is irrational. Therefore a + b must be irrational."
  explanation: "The proof assumes the negation (the sum is rational) and uses closure properties of rational numbers to derive that b must be rational — directly contradicting the given that b is irrational. The contradiction forces us to reject the assumption, proving the original claim."
```

## Explainer

Some statements resist direct proof. When you cannot see a clear path from hypothesis to conclusion, proof by contradiction offers an alternative: instead of proving the statement true, show that it cannot possibly be false. You do this by temporarily assuming it is false and demonstrating that this assumption collapses into nonsense.

The logic is rigorous. Every meaningful statement is either true or false. If assuming it is false leads to a contradiction — a statement that is logically impossible, like "1 = 0" or "N is both even and odd" — then the assumption of falsehood must itself be wrong. And if the statement is not false, it must be true. This is the law of excluded middle at work: there is no third option between true and false.

The most famous proof by contradiction is the proof that the square root of 2 is irrational, attributed to the ancient Greeks. Assume the opposite: suppose the square root of 2 is rational, meaning it can be written as a fraction p/q in lowest terms (where p and q share no common factors). Then (p/q)² = 2, so p² = 2q². This means p² is even, which means p is even (since the square of an odd number is odd). Write p = 2k. Then (2k)² = 2q², so 4k² = 2q², so q² = 2k². But this means q² is even, so q is even. Now both p and q are even — they share the factor 2, contradicting our assumption that p/q was in lowest terms. The assumption that the square root of 2 is rational has destroyed itself. Therefore, the square root of 2 is irrational.

You can also use contradiction for simpler claims. "There is no largest integer." Assume there is: call it N. Then N + 1 is also an integer (integers are closed under addition) and N + 1 > N. But we assumed N was the largest integer, so no integer can be larger — contradiction. Therefore there is no largest integer. The proof is three sentences long.

A practical guideline: try direct proof first. If that does not work, ask yourself what the negation of the conclusion looks like. If the negation gives you something concrete to work with — an object that should not exist, a property that should not hold — then contradiction is the right tool. If the statement is of the form "there is no X such that..." or "X is impossible," contradiction is often the natural choice, because assuming the negation gives you the very object or property you need to reason about.
