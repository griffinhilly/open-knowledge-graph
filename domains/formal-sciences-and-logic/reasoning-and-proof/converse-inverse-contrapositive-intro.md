---
id: converse-inverse-contrapositive-intro
title: Converse, Inverse, and Contrapositive
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: conditional-statements-formal
    type: hard
  - id: true-and-false-statements
    type: soft
builds-toward:
  - biconditional-statements-intro
  - logical-equivalence-intro
  - proof-by-contradiction-introduction
  - converse-inverse-contrapositive
tags: [converse, inverse, contrapositive, conditional, logic]
stage: abstract-reasoning
status: validated
---

# Converse, Inverse, and Contrapositive

## Core Idea
Every conditional statement P → Q has three related forms. The converse swaps hypothesis and conclusion: Q → P. The inverse negates both: ¬P → ¬Q. The contrapositive negates and swaps: ¬Q → ¬P. The critical fact: a conditional and its contrapositive are always logically equivalent (they are true in exactly the same situations), but a conditional and its converse are not. Confusing a statement with its converse is one of the most common logical errors in everyday reasoning.

## How It's Best Learned
Start with a concrete conditional: "If it is a dog, then it is a mammal." Write out all four forms explicitly. Converse: "If it is a mammal, then it is a dog" — clearly false (cats are mammals too). Inverse: "If it is not a dog, then it is not a mammal" — also false. Contrapositive: "If it is not a mammal, then it is not a dog" — true, just like the original. Build a table of several examples and let students discover the equivalence pattern themselves.

## Common Misconceptions
- Assuming the converse is automatically true when the original is true. "If it rains, the ground is wet" does not mean "if the ground is wet, it rained" (someone could have turned on a sprinkler).
- Confusing the inverse with the contrapositive. The inverse negates both parts but keeps the same direction; the contrapositive negates and reverses.
- Thinking all four forms are equivalent. Only the original and contrapositive are always equivalent. The converse and inverse are equivalent to each other but not to the original.

## Questions

```yaml
- question: "What is the contrapositive of 'If a number is divisible by 6, then it is divisible by 3'?"
  type: multiple-choice
  options:
    - "If a number is divisible by 3, then it is divisible by 6"
    - "If a number is not divisible by 6, then it is not divisible by 3"
    - "If a number is not divisible by 3, then it is not divisible by 6"
    - "If a number is divisible by 3, then it is not divisible by 6"
  answer: 2
  explanation: "The contrapositive of P → Q is ¬Q → ¬P: negate both parts and swap their positions. P = 'divisible by 6,' Q = 'divisible by 3.' Contrapositive: 'If not divisible by 3, then not divisible by 6.' This is logically equivalent to the original — and also clearly true (if 3 does not divide a number, 6 certainly cannot). Option A is the converse; option B is the inverse."

- question: "A conditional statement and its converse are always logically equivalent."
  type: true-false
  answer: false
  explanation: "A conditional and its converse can have different truth values. 'If it is a square, then it has four sides' is true, but its converse 'If it has four sides, then it is a square' is false (rectangles have four sides but are not squares). Only the contrapositive is guaranteed to match the original."

- question: "Given the statement 'If an animal is a penguin, then it cannot fly,' write the converse, inverse, and contrapositive, and state which are logically equivalent to the original."
  type: short-answer
  answer: "Converse: 'If an animal cannot fly, then it is a penguin.' Inverse: 'If an animal is not a penguin, then it can fly.' Contrapositive: 'If an animal can fly, then it is not a penguin.' The contrapositive is logically equivalent to the original. The converse and inverse are equivalent to each other but not to the original."
  explanation: "The converse is false (ostriches cannot fly but are not penguins). The inverse is false (ostriches are not penguins but cannot fly). The contrapositive is true — any animal that can fly is definitely not a penguin. This confirms the pattern: original ↔ contrapositive, and converse ↔ inverse."
```

## Explainer

Every conditional statement "If P, then Q" generates three related statements by negating and/or swapping its parts. Understanding which of these are equivalent — and which are not — is fundamental to logical reasoning and proof.

Start with a concrete example. Original: "If a shape is a square, then it has four sides." This is clearly true. Now form the three variants. The converse swaps P and Q: "If a shape has four sides, then it is a square." This is false — a rectangle has four sides but is not a square. The inverse negates both: "If a shape is not a square, then it does not have four sides." Also false — a triangle is not a square and does not have four sides, but a rectangle is not a square and does have four sides. The contrapositive negates and swaps: "If a shape does not have four sides, then it is not a square." This is true — you cannot be a square without four sides.

The pattern that emerges is the most important takeaway: a conditional and its contrapositive are always logically equivalent. They are true in exactly the same situations and false in exactly the same situations. Meanwhile, the converse and inverse are equivalent to each other — but neither is equivalent to the original. This is not a coincidence for certain examples; it is a logical law that holds for every conditional statement, no matter what P and Q are.

Why does this matter practically? Because people constantly confuse a statement with its converse in everyday reasoning. "If you work hard, you will succeed" does not mean "if you succeeded, you must have worked hard" (luck exists). "If a food contains peanuts, it is dangerous for people with peanut allergies" does not mean "if a food is dangerous for people with peanut allergies, it contains peanuts" (other allergens exist). Every time someone makes this swap without justification, they commit the fallacy of affirming the consequent. Recognizing the asymmetry between a conditional and its converse is one of the most practically useful things logic teaches.

The contrapositive equivalence, on the other hand, is a powerful proof tool. To prove "If P, then Q," you can equivalently prove "If not Q, then not P." Sometimes the contrapositive direction is much easier to prove. For example, proving "if n² is even, then n is even" is tricky to do directly — but the contrapositive, "if n is odd, then n² is odd," is straightforward (odd × odd = odd). You will use this technique extensively when you study proof strategies.
