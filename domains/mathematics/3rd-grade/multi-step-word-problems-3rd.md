---
id: multi-step-word-problems-3rd
title: Multi-Step Word Problems
domain: mathematics
course: 3rd-grade
prerequisites:
- id: addition-word-problems-2nd
  type: hard
- id: multiplication-word-problems-3rd
  type: hard
builds-toward:
- systems-word-problems
tags:
- word-problems
- problem-solving
- multi-step
stage: concrete-operations
status: validated
---

# Multi-Step Word Problems

## Core Idea
Multi-step problems require two or more operations. For example: 'Maria has 24 stickers, gives 6 to a friend, and buys 10 more. How many now?' requires subtraction then addition (24 − 6 + 10 = 28). Drawing pictures and identifying the sequence of steps are key strategies.

## Questions

```yaml
- question: "Jake had 30 cards. He gave 8 to his sister and then bought 5 more. How many cards does Jake have now? A student calculates 30 + 5 = 35 and stops. What error did this student make?"
  type: multiple-choice
  options:
    - "The student used addition when they should have used subtraction for the whole problem"
    - "The student used the wrong numbers — they should have used 8 and 5, not 30 and 5"
    - "The student skipped the first step — they needed to subtract 8 from 30 first (getting 22), then add 5 to that intermediate result"
    - "The student made an arithmetic error: 30 + 5 is not 35"
  answer: 2
  explanation: "The student went directly from the original 30 to adding 5, bypassing the first event in the story (giving away 8 cards). The correct sequence: 30 − 8 = 22, then 22 + 5 = 27. The intermediate result (22) is a hidden quantity — it's neither given in the problem nor the final answer, but it must be calculated first. Using the wrong starting number for the second operation is the most common error in multi-step problems."

- question: "What is a 'hidden quantity' in a multi-step word problem?"
  type: multiple-choice
  options:
    - "A number given in the problem that turns out not to be needed for the answer"
    - "The final answer that the problem is asking you to find"
    - "An intermediate result that must be calculated before you can find the final answer — it is neither given in the problem nor the final goal"
    - "A number that is too large to compute mentally and requires written work"
  answer: 2
  explanation: "Hidden quantities are the intermediate steps — the results of earlier operations that become the inputs for later ones. In the sticker example (24 stickers, give away 6, buy 10 more), the result after giving away 6 (18 stickers) is the hidden quantity. It is 'hidden' because the problem doesn't state it; you must discover it. Recognizing that a hidden quantity exists — that you can't go directly from the given numbers to the final answer — is the key insight of multi-step problem solving."

- question: "In a multi-step word problem, performing the operations in the wrong order will produce a wrong answer."
  type: true-false
  answer: true
  explanation: "Order matters in multi-step problems when the result of one step is the starting point for the next. If Jake gives away 8 cards first and then buys 5, the sequence is 30 − 8 = 22, then 22 + 5 = 27. If you add first: 30 + 5 = 35, then 35 − 8 = 27 — in this case the order happens to not matter due to the commutative property of addition and subtraction. But in many problems (especially those with multiplication), order is critical. The habit of following the story's sequence is always correct."

- question: "Multi-step word problems test whether students can perform harder arithmetic than single-step problems."
  type: true-false
  answer: false
  explanation: "The arithmetic operations themselves are exactly the same difficulty — the same addition, subtraction, and multiplication students already know. What multi-step problems test is whether a student can organize a sequence of operations correctly: identifying the right order, finding the hidden intermediate quantity, and making sure the final answer addresses what was actually asked. The challenge is comprehension and planning, not computational difficulty. This is why drawing pictures and writing separate equations for each step are emphasized as strategies."

- question: "What is the most important first step when you encounter a multi-step word problem, and why does doing this before calculating help you find the right answer?"
  type: short-answer
  answer: "Read the entire problem before calculating anything. This lets you identify all the given quantities, understand the complete sequence of events in the story, and figure out what the final question is actually asking. If you start calculating at the first number you see, you may skip steps, use the wrong starting value for a later operation, or solve the wrong question entirely."
  explanation: "Reading first builds a mental model of the whole problem before any numbers are committed to paper. Once you understand the full story, you can identify the hidden intermediate quantities and plan the correct sequence of steps. Re-reading the original question at the end — to verify your final answer actually addresses what was asked — is the complementary habit that catches errors after the fact."
```

## Explainer

When you first learned word problems — "Maria has 8 apples and gets 5 more; how many does she have?" — each problem required exactly one operation. You identified what was happening, chose an operation, and solved. **Multi-step word problems** follow the same pattern, but the story requires at least two operations before you reach the final answer. The challenge is not harder arithmetic — it is figuring out what to do first, and in what order.

The most useful first move is to **read the whole problem before calculating anything**. Identify every quantity given and the quantity being asked for. Then ask: can I calculate the final answer directly from the given numbers? Usually not — there is a missing piece in the middle. In the sticker example (24 stickers, give away 6, buy 10 more), the question asks for the final count. You cannot get there from 24 and 10 directly — you must first find the count after giving some away (24 − 6 = 18), which becomes the input for the second step (18 + 10 = 28). That intermediate result is called a **hidden quantity** — it is neither given in the problem nor the final answer, but you must find it along the way.

A reliable strategy is **drawing a picture for each step of the story**. Show the 24 stickers, cross out 6, then draw 10 being added. Visuals turn abstract words into a concrete scene, making it easier to see what you know and what you still need to find. Another strategy is **writing a separate equation for each step** rather than trying to capture everything in one equation. Treat the problem like a story with chapters: one equation per chapter, using the previous chapter's answer as the next chapter's starting number.

Your earlier work on addition word problems and multiplication word problems gave you the individual operations — you already know how to add, subtract, and multiply. Multi-step problems are testing whether you can **organize a sequence of operations correctly**, not whether you can do harder individual calculations. After you finish, re-read the original question and check that your final answer actually addresses what was asked, not just the last calculation you did. This habit catches most errors before they happen.
