---
id: fact-families-multiplication-and-division-3rd
title: 'Fact Families: Multiplication and Division'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: fact-family-relationships
  type: hard
- id: multiplication-division-relationship
  type: hard
- id: estimation-multiplication-division
  type: soft
builds-toward:
- fact-families
tags:
- fact-families
- multiplication
- division
stage: concrete-operations
status: validated
---
# Fact Families: Multiplication and Division

## Core Idea
A fact family connects multiplication and division facts using three numbers. For example, 3, 4, and 12 form the family: 3 × 4 = 12, 4 × 3 = 12, 12 ÷ 3 = 4, 12 ÷ 4 = 3. Learning one fact helps recall the others.

## Questions

```yaml
- question: "A student sees 56 ÷ 7 = ? and doesn't remember this division fact. Their teacher says: 'Think about what you know from multiplication.' Which multiplication fact should the student use?"
  type: multiple-choice
  options:
    - "7 + ? = 56"
    - "7 × ? = 56"
    - "56 × 7 = ?"
    - "56 − 7 = ?"
  answer: 1
  explanation: "Division and multiplication are inverse operations in the same fact family. '56 ÷ 7 = ?' asks the same question as '7 × ? = 56.' If you know that 7 × 8 = 56, then 56 ÷ 7 = 8 immediately. Using multiplication as a lookup table for division is exactly the strategy fact families teach — and why knowing multiplication facts makes division much easier."

- question: "The numbers 6, 7, and 42 form a fact family. Which of the following is NOT a member of that fact family?"
  type: multiple-choice
  options:
    - "6 × 7 = 42"
    - "42 ÷ 6 = 7"
    - "7 × 6 = 42"
    - "6 ÷ 42 = 7"
  answer: 3
  explanation: "The four valid equations in the 6, 7, 42 fact family are: 6 × 7 = 42, 7 × 6 = 42, 42 ÷ 6 = 7, and 42 ÷ 7 = 6. '6 ÷ 42 = 7' is false — 6 ÷ 42 is a tiny fraction, not 7. In a valid fact family, the product (the largest number, 42) is always the starting number in the division equations. You never divide a factor by the product."

- question: "Knowing that 8 × 9 = 72 immediately tells you the answers to both 72 ÷ 8 and 72 ÷ 9."
  type: true-false
  answer: true
  explanation: "The three numbers 8, 9, and 72 form a complete fact family. The single multiplication fact 8 × 9 = 72 gives you both division facts: 72 ÷ 8 = 9 and 72 ÷ 9 = 8. This is the payoff of fact families — one known multiplication fact unlocks two division facts simultaneously, without any separate memorization."

- question: "In a fact family, you can create a valid division equation by dividing any one of the three numbers by either of the other two."
  type: true-false
  answer: false
  explanation: "Only the product (the largest number) can serve as the dividend in a fact family's division equations. For the family 3, 4, 12: you can write 12 ÷ 3 = 4 and 12 ÷ 4 = 3, but 3 ÷ 12 and 4 ÷ 3 are not in the family — they would produce fractions, not whole-number answers. Division equations in a fact family always start with the product."

- question: "Explain why a student who knows all their multiplication facts already knows most of their division facts. How does thinking about fact families make this work?"
  type: short-answer
  answer: "Multiplication and division are inverse operations that undo each other. Every multiplication fact has two corresponding division facts in the same fact family: if 6 × 8 = 48, then 48 ÷ 6 = 8 and 48 ÷ 8 = 6. Fact families make this explicit by grouping all four equations together. So instead of memorizing division facts separately, you can use multiplication as a lookup table: for 48 ÷ 6, ask '6 × ? = 48' and your multiplication knowledge gives the answer."
  explanation: "This is the practical benefit of understanding fact families: division becomes a form of 'missing factor' multiplication rather than a separate set of facts to memorize. The key is understanding that the product (48) plays a special role — it is always the number being divided, and the two factors (6 and 8) are always the divisor and quotient, in either order."
```

## Explainer

You already know that multiplication and division are inverse operations — they undo each other. A **fact family** makes that inverse relationship concrete by showing all the equations you can write with three numbers. Take 3, 4, and 12. The multiplication facts are 3 × 4 = 12 and 4 × 3 = 12 (using the commutative property you already know). Flip the equal sign and the big number becomes the starting point: 12 ÷ 3 = 4 and 12 ÷ 4 = 3. Four equations, three numbers, one tight family.

Think of the three numbers as playing roles: the **product** (the largest number, 12) is the whole; the two **factors** (3 and 4) are the parts. Multiplication builds the whole from the parts. Division breaks the whole into equal parts. Knowing any one of the four equations means you know all the others, because the relationship between the three numbers is the same in every equation — only the question changes. "What is 3 groups of 4?" and "How many groups of 3 fit in 12?" are the same mathematical situation viewed from different directions.

This is why fact families are so useful for learning division. Division facts are harder to memorize in isolation, but if you have already mastered multiplication, division comes nearly for free. When you see 12 ÷ 4, ask yourself: "4 times *what* equals 12?" Your multiplication knowledge (4 × 3 = 12) gives you the answer instantly. You are using multiplication as a lookup table for division — exactly the strategy that mathematicians use when they say multiplication and division are inverses.

The fact family also clarifies a common confusion: 12 ÷ 3 and 12 ÷ 4 give different answers because the *divisor* (the number you divide by) is different, even though the dividend (12) is the same. And 3 ÷ 12 is not in this family at all — it would give a fraction, not a whole number. Recognizing which three numbers form a valid fact family also trains you to see divisibility, a concept that will matter when you study fractions and prime numbers later.

