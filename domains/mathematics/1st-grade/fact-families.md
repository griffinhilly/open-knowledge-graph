---
id: fact-families
title: Fact Families
domain: mathematics
course: 1st-grade
prerequisites:
- id: addition-subtraction-relationship
  type: hard
builds-toward:
- addition-subtraction-word-problems
tags:
- fact-families
- relationships
stage: pre-formal
status: validated
---

# Fact Families

## Core Idea
Fact families group four related addition and subtraction facts using the same three numbers (e.g., 2+3=5, 3+2=5, 5-2=3, 5-3=2). This helps students see number relationships deeply.

## Questions

```yaml
- question: "A student knows that 7 + 5 = 12. Which of the following can they figure out immediately, without doing any new calculation?"
  type: multiple-choice
  options:
    - "Only 5 + 7 = 12, since addition is commutative"
    - "5 + 7 = 12, 12 − 7 = 5, and 12 − 5 = 7 — all three are part of the same fact family"
    - "They would still need to memorize 12 − 7 and 12 − 5 separately"
    - "Nothing — subtraction facts must be learned independently from addition facts"
  answer: 1
  explanation: "A fact family groups all four related facts using the same three numbers. Knowing 7 + 5 = 12 means you instantly know 5 + 7 = 12 (addition is commutative), 12 − 7 = 5, and 12 − 5 = 7. The mistake in option C reflects the common misconception that addition and subtraction facts are separate lists. They are the same number relationship viewed from four different angles."

- question: "A student sees the problem '9 + ? = 15.' What is the most efficient strategy to find the missing number?"
  type: multiple-choice
  options:
    - "Count up from 9 until reaching 15"
    - "Guess and check different numbers until one works"
    - "Think of it as a subtraction problem: 15 − 9 = ?"
    - "Add 9 + 15 and see what the result tells you"
  answer: 2
  explanation: "Missing-addend problems are solved by recognizing the fact family. The three numbers 6, 9, and 15 are related: 9 + 6 = 15, so 15 − 9 = 6. Rewriting the problem as subtraction is the key insight of fact families — addition and subtraction are two views of the same relationship, so you can move between them to solve for the missing piece. Counting up (option A) works but is slower and less reliable for larger numbers."

- question: "A fact family always contains exactly three different numbers and four related equations."
  type: true-false
  answer: true
  explanation: "Every fact family is built from exactly three numbers: two smaller numbers and their sum. Those three numbers generate exactly four equations — two addition facts (in both orders) and two subtraction facts. For example, the numbers 3, 8, and 11 produce: 3 + 8 = 11, 8 + 3 = 11, 11 − 3 = 8, and 11 − 8 = 3. No more, no fewer."

- question: "In the fact family containing 4, 6, and 10, the subtraction facts can start with any of the three numbers."
  type: true-false
  answer: false
  explanation: "Subtraction facts in a family always start with the largest number — the sum — because subtraction means taking a part away from the whole. The two subtraction facts are 10 − 4 = 6 and 10 − 6 = 4. You never subtract starting from 4 or 6 in this family (doing so would produce a negative number or require knowledge beyond this level). The largest number is always the 'parent' from which the two smaller numbers are taken."

- question: "Why does knowing one addition fact in a fact family mean you automatically know all four facts in the family?"
  type: short-answer
  answer: "Because all four facts express the same relationship between three numbers. Addition and subtraction are inverse operations — two ways of describing how the same three numbers fit together. If you know the whole (the sum) and both parts, you can write two addition facts (swapping the order of the parts) and two subtraction facts (removing each part from the whole)."
  explanation: "The power of fact families is that they reduce what seems like four separate things to memorize into one underlying relationship. The fact 3 + 8 = 11 tells you: '3 and 8 combine to make 11.' That single idea, viewed from four angles, gives all four facts. This is why math educators emphasize fact families — they reveal the structure hiding behind what looks like a long list of unrelated facts."
```

## Explainer

You already know that addition and subtraction are connected—that they are in some sense opposites of each other, that you can "undo" addition with subtraction. A **fact family** makes that connection completely explicit, showing all four ways that three numbers relate to each other at once.

Here's how it works. Take three numbers: 3, 4, and 7. These numbers form a family because 3 + 4 = 7. Once you know that, you automatically know three more facts: 4 + 3 = 7 (order doesn't matter in addition), 7 − 3 = 4, and 7 − 4 = 3. That's the whole family: four facts, three numbers. The largest number—the sum—is always the starting point for the two subtraction facts. It gets taken apart; the two smaller numbers take turns being removed.

Why does this matter? Because when you learn one fact, you're actually learning four. If you know that 6 + 8 = 14, you already know 8 + 6 = 14, 14 − 6 = 8, and 14 − 8 = 6. You don't have to memorize each one separately—they're all the same relationship viewed from different angles. Fact families reveal that addition and subtraction facts aren't a huge list of unrelated things to memorize; they're a smaller set of number relationships, each one a family of four.

This is also the key to solving **missing number problems**. If you see "7 + ? = 12," you can think of it as a subtraction: 12 − 7 = ?. The question is asking you to find the missing member of the fact family 5, 7, 12. As you practice fact families, this back-and-forth between addition and subtraction becomes automatic—you stop treating them as separate operations and start seeing them as two ways into the same relationship. That flexibility is what makes you fast and confident with number facts.
