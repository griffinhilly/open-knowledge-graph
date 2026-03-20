---
id: unknown-factor-problems
title: Unknown Factor Problems
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-within-100
  type: hard
- id: fact-families
  type: soft
builds-toward:
  - division-facts-within-100
  - one-step-equations
tags:
- unknown-factor
- multiplication
- division
- algebra-readiness
stage: concrete-operations
status: validated
---
# Unknown Factor Problems

## Core Idea
An unknown factor problem presents a multiplication equation with one factor missing: 3×? = 12 or ?×5 = 35. Students solve these by thinking about what number times the known factor gives the product, which is equivalent to dividing. These problems build the bridge between multiplication and division and introduce algebraic thinking.

## How It's Best Learned
Connect to fact families — if students know 3×4=12 and 4×3=12, they should also be able to state 12÷3=4 and 12÷4=3. Use the same fact family triangle or table.

## Common Misconceptions
- Students may try to subtract rather than divide when facing unknown factor problems.
- When the unknown is the first factor (?×5=35), some students struggle more than when it is the second.

## Questions

```yaml
- question: "A student needs to solve 4 × ? = 28. She tries subtracting: 28 − 4 = 24, and writes 24 as her answer. What is wrong with her approach?"
  type: multiple-choice
  options:
    - "Subtraction is the right operation, but she should keep subtracting 4 until she reaches 0"
    - "An unknown factor problem asks what multiplies by 4 to give 28 — that's a division relationship, not subtraction. She should think: 28 ÷ 4 = ?"
    - "She should add 4 repeatedly until she reaches 28"
    - "Subtraction works here, but she made an arithmetic error; she needs to subtract again"
  answer: 1
  explanation: "Unknown factor problems are division in disguise. '4 × ? = 28' asks: 'What number, multiplied by 4, gives 28?' This is exactly 28 ÷ 4 = ?. Subtracting once gives 24, which is not the answer — there is no meaningful connection between a single subtraction and finding a missing factor. The most direct path is to recall the multiplication fact: 4 × 7 = 28, so ? = 7."

- question: "A student correctly solves ? × 6 = 42 and gets 7. Her classmate says she's wrong because 'the unknown must come second.' Is the classmate correct?"
  type: multiple-choice
  options:
    - "Yes — unknown factors must always appear in the second position for the equation to be solvable"
    - "No — multiplication is commutative, so ? × 6 and 6 × ? are equivalent; 7 is correct either way"
    - "Yes — when the unknown comes first, it is a different type of problem with a different answer"
    - "No, but she must rewrite it as 6 × ? = 42 and solve again to confirm"
  answer: 1
  explanation: "The commutative property guarantees that ? × 6 = 6 × ? for any value of ?. The position of the unknown — first or second — does not change the answer or the strategy. Verify: 7 × 6 = 42 ✓. If the first-position setup feels uncomfortable, mentally rewrite ? × 6 = 42 as 6 × ? = 42, then solve. The answer remains 7. Practicing both positions builds the flexibility that algebra will later require."

- question: "The equation 3 × ? = 18 and the division problem 18 ÷ 3 = ? are two different questions with different answers."
  type: true-false
  answer: false
  explanation: "They are the same question expressed two different ways. Both ask: 'What number, when multiplied by 3, gives 18?' The unknown factor approach uses multiplication knowledge (3 × 6 = 18). The division approach computes 18 ÷ 3 = 6. Both arrive at ? = 6 because an unknown factor problem IS division — the link between multiplication and division is the entire key insight of this topic."

- question: "Knowing the multiplication fact 9 × 7 = 63 immediately gives you the answer to the unknown factor problem ? × 7 = 63."
  type: true-false
  answer: true
  explanation: "? × 7 = 63 asks for the number that, multiplied by 7, gives 63. Since 9 × 7 = 63, the answer is ? = 9. The fact family connects everything: 9 × 7 = 63 and 7 × 9 = 63 both answer unknown factor problems for the same three numbers. This is why building multiplication fact fluency is the direct path to solving unknown factor problems — no additional procedures are needed."

- question: "Explain why an unknown factor problem like 5 × ? = 40 is the same as a division problem. What is the connection between the two?"
  type: short-answer
  answer: "An unknown factor problem asks: 'What number multiplied by 5 gives 40?' Division asks exactly the same thing: 40 ÷ 5 = ?. Both seek the same unknown. The connection is that multiplication and division are inverse operations. If 5 × 8 = 40, then 40 ÷ 5 = 8, and ? = 8 in 5 × ? = 40. They are three ways of expressing the same relationship among the numbers 5, 8, and 40."
  explanation: "This equivalence is the bridge from multiplication to division and eventually to algebra. Recognizing that 'find the missing factor' and 'divide' describe the same operation is a conceptual milestone. The same fact family (5 × 8 = 40, 8 × 5 = 40, 40 ÷ 5 = 8, 40 ÷ 8 = 5) captures all the relationships among those three numbers — a pattern that extends into every equation-solving situation students will encounter later."
```

## Explainer

You already know your multiplication facts and you understand fact families — the idea that the same three numbers connect in two multiplication equations and two division equations. Unknown factor problems take that same idea and write it as an equation with a missing piece: 3 × ? = 12. Your job is to find the missing number. This is the first time you are doing something that looks like algebra, even if it doesn't have that name yet.

The key insight is that an unknown factor problem is the same as a division problem in disguise. Asking "3 × ? = 12" is exactly the same question as asking "12 ÷ 3 = ?" Both questions are asking: how many groups of 3 fit into 12? Because you know 3 × 4 = 12, you know immediately that ? = 4. Your multiplication fact knowledge is the tool you use to solve for the unknown.

The position of the unknown — first or second — does not change the answer, because multiplication is **commutative**: 3 × 4 = 4 × 3. So ? × 5 = 35 is the same as 5 × ? = 35, and the answer is still 7. When the unknown comes first, it can feel strange because we usually write "known × known = product." The remedy is to swap the order mentally: rewrite ? × 5 = 35 as 5 × ? = 35, which may feel more natural, and then recall the fact.

This kind of problem is important because it introduces the concept of an **equation** — a statement that two expressions are equal — and the idea that a symbol can hold a place for an unknown value you are trying to find. Everything you learn later about solving equations in algebra is built on this same logic: use what you know about the relationship between numbers to find what you don't know.
