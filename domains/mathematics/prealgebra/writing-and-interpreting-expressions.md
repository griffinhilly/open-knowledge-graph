---
id: writing-and-interpreting-expressions
title: Writing and Interpreting Algebraic Expressions
domain: mathematics
course: prealgebra
prerequisites:
- id: variable-expressions
  type: hard
- id: adding-integers
  type: soft
- id: multiplying-integers
  type: hard
builds-toward:
  - one-step-equations
  - two-step-equations
tags: [expressions, translating, verbal-to-algebraic, algebra]
stage: abstract-reasoning
status: validated
---

# Writing and Interpreting Algebraic Expressions

## Core Idea
Translating between verbal descriptions and algebraic expressions is a core algebra skill. "Three more than twice a number" becomes 2n + 3. "The quotient of a number and five, decreased by four" becomes n/5 − 4. This requires knowing which operations correspond to which words (sum = addition, product = multiplication, difference = subtraction, quotient = division) and understanding the order in which they combine. This skill is the bridge from word problems to equations — you cannot solve a word problem algebraically without first writing the correct expression.

## How It's Best Learned
Build a reference chart of key phrases and their operations. Practice one direction at a time (verbal to algebraic, then algebraic to verbal). Use context-rich problems where students must identify the variable and the operations. Emphasize that "less than" and "subtracted from" reverse the order: "5 less than x" is x − 5, not 5 − x.

## Common Misconceptions
- "5 less than a number" written as 5 − n instead of n − 5.
- "Twice a number plus 3" written as 2(n + 3) instead of 2n + 3 — confusing when to use parentheses.
- Not identifying what the variable represents before writing the expression.

## Questions

```yaml
- question: "A student translates 'five less than a number' as 5 − n. What is the correct expression, and what went wrong?"
  type: multiple-choice
  options:
    - "Correct expression: n − 5; the student wrote the numbers in reading order, but 'less than' reverses the subtraction"
    - "Correct expression: 5 − n; the student is actually right"
    - "Correct expression: n + 5; 'less than' should be treated as addition"
    - "Correct expression: −5n; 'less than' signals a negative coefficient"
  answer: 0
  explanation: "'Five less than a number' means: start with the number and remove 5 from it — that's n − 5. The phrase 'less than' describes what the result is relative to n, so n comes first in the subtraction. The student read left-to-right and wrote 5 − n, which would mean something different: a number that is n less than 5. Whenever you see 'less than' or 'subtracted from,' the reading order reverses the operation order."

- question: "Which expression correctly translates 'twice the sum of a number and 4'?"
  type: multiple-choice
  options:
    - "2n + 4"
    - "2(n + 4)"
    - "2n + 8"
    - "n + 8"
  answer: 1
  explanation: "'The sum of a number and 4' signals a grouping — n + 4 must be computed first. 'Twice the sum' means that whole group is multiplied by 2, giving 2(n + 4). Compare this to 'twice a number, plus 4' which gives 2n + 4 — here you double first, then add. The phrase 'the sum of…' acts like parentheses in language, indicating that everything inside belongs together before other operations are applied."

- question: "The phrase 'the quotient of n and 5, decreased by 4' translates to n/5 − 4, not 4 − n/5."
  type: true-false
  answer: true
  explanation: "'The quotient of n and 5' means n divided by 5, giving n/5. 'Decreased by 4' means subtract 4 from what came before: n/5 − 4. If the expression were '4 decreased by the quotient of n and 5,' that would be 4 − n/5. The phrase 'decreased by' follows the same reading-order logic as 'less than' — you subtract from what was stated before, not the other way around."

- question: "In the expression 4(n − 7) + 2, the parentheses are optional because multiplication distributes, so you could write 4n − 7 + 2 instead."
  type: true-false
  answer: false
  explanation: "The parentheses change the meaning. 4(n − 7) + 2 distributes to 4n − 28 + 2 = 4n − 26. Without parentheses, 4n − 7 + 2 = 4n − 5, which is a different expression. Removing the parentheses would only multiply the n by 4, leaving the −7 unchanged. The parentheses indicate that the entire quantity (n − 7) is multiplied by 4 — this is exactly the distinction between 'twice the sum of a number and 7' (2(n+7)) and 'twice a number, plus 7' (2n+7)."

- question: "Explain why 'five less than a number' translates to n − 5 and not 5 − n. What is it about the phrase 'less than' that reverses the order?"
  type: short-answer
  answer: "'Five less than a number' means the result is 5 fewer than the number — so you start with n and subtract 5, giving n − 5. The phrase 'less than' describes the result in relation to the number: the number n is the reference point, and we remove 5 from it. In English, 'less than' reads with the amount first ('five less than') but the math puts the reference quantity first (n − 5). This reversal occurs because 'less than' is a comparison phrase — it identifies the base value that comes second in the sentence but first in the subtraction."
  explanation: "This is one of the most consistently confused translations in algebra. A useful check: substitute a number. 'Five less than 10' should be 5 (ten minus five), not −5 (five minus ten). So n − 5 is correct. The same reversal applies to 'subtracted from': 'n subtracted from 10' is 10 − n, not n − 10."
```

## Explainer

You already know that a **variable** is a letter that stands for an unknown or changing number, and you know how to add, subtract, and multiply integers. Writing and interpreting expressions is the skill that connects those pieces to the language of word problems — it is the translation layer between a sentence in English and a string of symbols a mathematician can work with.

The first step in any translation is to name what you do not know. "A store sells notebooks for $3 each" — what is unknown? Maybe the number of notebooks. Call it n. The total cost is then 3n. This is **multiplication expressed by adjacency**: 3n means 3 × n. You know from multiplying integers that order does not matter for multiplication (3 × n = n × 3), but order matters enormously for subtraction. This is where many students stumble: "5 less than n" means you start with n and remove 5, giving n − 5. Reading it left to right — "5 less than" — the 5 comes first in the sentence but second in the expression. Whenever you see "less than" or "subtracted from," the subtraction is reversed from the reading order.

Addition words — sum, more than, increased by, plus — are symmetric: "n more than 5" and "5 more than n" produce the same result only if we meant the same quantity. But "the sum of n and 5" is n + 5 regardless of order because addition commutes. Multiplication words — product, twice, triple, of, times — also commute. Division words — quotient of, divided by, per — do not: "the quotient of n and 5" is n/5, not 5/n. Building a mental map of these pairings is the core of this skill. Practice it both ways: given a sentence, write the expression; given an expression like 4(n − 7) + 2, write a sentence that describes it — "four times the difference of a number and seven, plus two."

Parentheses carry meaning: they indicate that an operation applies to the result of what is inside, not to individual terms. "Twice the sum of a number and 3" is 2(n + 3) because you add first, then double. "Twice a number, plus 3" is 2n + 3 because you double first, then add. The word "the sum of" signals a grouping — everything in "the sum of…" belongs together inside parentheses. Getting this distinction right is what lets you move to equations next: once you write the correct expression, solving for n is just arithmetic run in reverse.
