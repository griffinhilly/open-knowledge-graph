---
id: two-step-word-problems
title: Two-Step Word Problems
domain: mathematics
course: 2nd-grade
prerequisites:
- id: addition-subtraction-word-problems
  type: hard
- id: addition-within-100
  type: hard
- id: subtraction-within-100
  type: hard
- id: three-digit-addition
  type: soft
- id: three-digit-subtraction
  type: soft
- id: subtraction-word-problems-2nd
  type: soft
builds-toward:
- multi-digit-addition
- multi-digit-subtraction
tags:
- word-problems
- two-step
- addition
- subtraction
- problem-solving
stage: concrete-operations
status: validated
---
# Two-Step Word Problems

## Core Idea
A two-step word problem requires two separate calculations to find the answer. For example: 'Maria had 45 stickers. She gave 18 to a friend and then bought 12 more. How many does she have now?' — requires first subtracting (45 − 18 = 27), then adding (27 + 12 = 39). Students must identify what is known, what is asked, and plan the two operations before computing.

## How It's Best Learned
Teach students to underline key information and write a plan: 'First I will… then I will…' Draw a bar model or tape diagram to represent the problem structure. Have students write intermediate answers and label them so the sequence of steps is visible.

## Common Misconceptions
- Solving only one of the two required steps.
- Choosing the wrong operations — addition when subtraction is needed, or vice versa.
- Losing track of intermediate results when not writing them down.

## Questions

```yaml
- question: "A baker made 48 muffins. She sold 23 in the morning and then baked 15 more. A student writes: 48 − 23 = 25 and stops. What is wrong?"
  type: multiple-choice
  options:
    - "The student chose the wrong operation — it should be 48 + 23 first"
    - "The student found only the intermediate result; the second step (adding 15 more muffins) was never completed"
    - "The student used the wrong numbers — the 15 and 23 should be added first"
    - "Nothing is wrong — 25 is the correct final answer"
  answer: 1
  explanation: "The problem has two events: selling 23 muffins (subtraction) and then baking 15 more (addition). The student completed only the first operation and stopped. The intermediate result — 25 muffins remaining after the morning sale — is not the final answer. The second step (25 + 15 = 40) must still be done. This is the most common error in two-step problems: stopping after the first calculation."

- question: "In the muffin problem above, what does the number 25 represent?"
  type: multiple-choice
  options:
    - "The final answer — how many muffins the baker has at the end"
    - "The total number of muffins sold and baked combined"
    - "An intermediate result — muffins remaining after the morning sale, which becomes the starting number for step two"
    - "The number of muffins baked in the second batch"
  answer: 2
  explanation: "An intermediate result is an answer to the first step that is not the final answer — it is the starting point for the second step. Identifying it correctly is what makes two-step problems work. In this problem, 25 is the number of muffins left after selling 23; it is not a final answer but a necessary stepping stone to find how many remain after baking 15 more."

- question: "In a two-step word problem, the answer to the first step becomes the starting number for the second step."
  type: true-false
  answer: true
  explanation: "This is the defining feature of a two-step problem. The two operations are chained: you use the result of step one as input for step two. In the playground example (45 students, 18 go inside, 12 come back out), you cannot compute the final count until you first know how many stayed when 18 left. That intermediate result (27) feeds directly into the second operation."

- question: "If a word problem contains two numbers, it should be a two-step problem."
  type: true-false
  answer: false
  explanation: "The number of numbers in a problem does not determine whether it is one-step or two-step. A one-step problem like 'Maria has 45 stickers and gives 18 away — how many does she have?' contains two numbers but requires only one operation. What makes a problem two-step is that two separate operations are needed to find the answer, not how many numbers appear in the story."

- question: "Why is writing out the intermediate result (the answer to step one) important when solving a two-step word problem?"
  type: short-answer
  answer: "The intermediate result is the answer to the first step and the starting number for the second step. Writing it down makes the chain of reasoning visible and prevents errors: you can check that step one is right before using it in step two. Students who do both steps mentally often lose track of the intermediate result, use the wrong number in step two, or confuse it with the final answer."
  explanation: "Externalizing the intermediate result is a study habit that scales to more complex problems. Tape diagrams and bar models work on the same principle — they make the problem's structure visible before any calculation happens. The written intermediate answer is not just bookkeeping; it is evidence that the student correctly identified what the first step was asking for."
```

## Explainer

You already know how to solve one-step word problems — you read the situation, figure out whether to add or subtract, and compute. A **two-step word problem** is simply two of those problems chained together. The answer to the first step becomes the starting point for the second step. The trick is recognizing that two separate questions are hiding inside one story.

Consider this problem: "There are 45 students on the playground. 18 go inside for lunch, then 12 more come out to play. How many students are on the playground now?" You can't answer this in one operation. First you have to find how many remained after 18 left (45 − 18 = 27), then find how many there are after 12 more arrived (27 + 12 = 39). The 27 is an **intermediate result** — it is not the final answer, but you must find it before you can take the next step.

The most important habit is to make your plan before you calculate. Ask yourself: what happens first in the story? What happens second? Write it out: "First: subtract 18 from 45. Then: add 12 to the result." Many students rush to compute and end up solving only one step, or picking the wrong operations. Slowing down to identify the two actions in the story — and the order they happen — prevents most errors.

Drawing a **tape diagram** or bar model is a powerful way to see the structure. Draw a bar for the starting amount, show what is removed or added in step one, and then show what changes in step two. The visual makes it obvious how the two operations fit together. As you encounter more complex problems, this habit of mapping the story before computing becomes even more valuable.
