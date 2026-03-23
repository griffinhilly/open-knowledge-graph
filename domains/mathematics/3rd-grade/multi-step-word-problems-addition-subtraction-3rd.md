---
id: multi-step-word-problems-addition-subtraction-3rd
title: Multi-Step Word Problems
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multi-digit-addition-subtraction-3rd
  type: hard
builds-toward:
- problem-solving-strategies
tags:
- word-problems
- multi-step
- operations
stage: concrete-operations
status: validated
---

# Multi-Step Word Problems

## Core Idea
Solve problems requiring multiple operations. Read carefully, identify what's given and what to find, break into steps, solve each step, and check. Example: 'Sarah has 25 apples. She buys 18 more. Then gives 20 to a friend. How many left?'

## How It's Best Learned
Draw pictures or use objects to model. Write equations for each step. Verify reasonableness.

## Common Misconceptions
Not reading carefully; performing wrong operations; forgetting a step; not checking.

## Questions

```yaml
- question: "A school had 125 students. Then 38 new students joined. Then 15 students moved away. A student writes the equation 125 − 38 + 15. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — addition and subtraction can be done in any order."
    - "The operations are reversed: students joining should be addition (+38), and students moving away should be subtraction (−15). The correct expression is 125 + 38 − 15."
    - "This problem requires multiplication, not addition and subtraction."
    - "You cannot mix addition and subtraction in the same equation."
  answer: 1
  explanation: "Reading carefully reveals what each event means as an operation. Students 'joining' increases the total (addition). Students 'moving away' decreases the total (subtraction). Writing 125 − 38 + 15 reverses those operations, giving 102 instead of the correct answer 148. This is a reading error, not an arithmetic error — the key skill in multi-step problems is correctly translating each event into the right operation before calculating."

- question: "Why should you write down an intermediate answer after completing each step in a multi-step problem?"
  type: multiple-choice
  options:
    - "Because the rules of arithmetic require it."
    - "Because the answer from one step becomes the starting number for the next step — recording it creates a clear handoff and a checkpoint where you can verify reasonableness before continuing."
    - "Because teachers want to see your work written out."
    - "Because each step's answer is a final answer to a separate problem."
  answer: 1
  explanation: "In multi-step problems, the output of one step is the input of the next. Recording the intermediate answer makes that handoff explicit and gives you a natural checkpoint: does this intermediate value make sense before I proceed? Students who try to chain all steps in their head in one go frequently lose track and make errors that are hard to locate."

- question: "In a multi-step word problem, checking whether your final answer is reasonable can catch errors where you used the right arithmetic but applied the operations in the wrong order."
  type: true-false
  answer: true
  explanation: "A reasonableness check is the last line of defense against procedural errors. If a problem involves a student who started with 48 cards, gained some, then gave some away, an answer of 200 is obviously unreasonable given the numbers involved — even if the individual arithmetic steps were correct. Reasonableness checking catches order-of-operations errors that the arithmetic itself won't flag."

- question: "A multi-step word problem always requires exactly two steps — one addition and one subtraction."
  type: true-false
  answer: false
  explanation: "Multi-step problems can have any number of steps, and the operations can be any combination of addition and subtraction (or, in later grades, multiplication and division). The defining feature is simply that the problem cannot be solved with a single operation. The number and type of steps depends entirely on the events described in the problem."

- question: "How do you decide which operation (addition or subtraction) to use for each step in a multi-step word problem?"
  type: short-answer
  answer: "Look at what is happening in each event of the story. If something is being gained, added, combined, or increased — use addition. If something is being lost, used up, given away, or decreased — use subtraction. Reading each sentence and asking 'does this make the total bigger or smaller?' helps assign the right operation before calculating. Drawing a quick picture of each event can also make it visible whether the amount is growing or shrinking."
  explanation: "This is the translation skill at the heart of word problems. The arithmetic itself is straightforward; the challenge is mapping real-world language ('joined,' 'spent,' 'gave away') onto mathematical operations. Building this careful, event-by-event reading habit is what makes multi-step problems consistently solvable."
```

## Explainer

A **multi-step word problem** is really just a story where something changes more than once, and your job is to track all those changes accurately. You already know how to add and subtract multi-digit numbers — the new challenge is figuring out *which* operations to perform, *in what order*, and *why*. The arithmetic itself is not the hard part; the hard part is translating a real-world situation into a sequence of math steps.

Here is how to approach any multi-step problem systematically. First, read the whole problem before writing anything. Understand what is happening: who has what, what changes, and what you ultimately need to find. Then re-read and identify the **known quantities** (the numbers the problem gives you) and the **unknown** (what you are solving for). In the example "Sarah has 25 apples. She buys 18 more. Then gives 20 to a friend. How many left?" — the knowns are 25, 18, and 20; the unknown is the final count. Notice that three separate events happen, so three separate calculations are needed.

Now break the story into **individual steps**, one event at a time. Step 1: Sarah starts with 25 and gains 18, so 25 + 18 = 43. Step 2: she gives away 20, so 43 − 20 = 23. Each step produces an intermediate answer that feeds into the next step — the output of step 1 becomes the input of step 2. Writing a separate equation for each step, rather than cramming everything into one line, makes it much easier to track your work and catch errors. Drawing a quick picture or a "before/after" diagram also helps you see whether you should be adding (something is gained) or subtracting (something is lost or given away).

Finally, always **check your answer for reasonableness**. Before you commit to "23 apples," ask: does that make sense? Sarah started with 25, gained some, then gave some away. Ending with fewer than 25 is plausible. Ending with, say, 200 would not make sense given the numbers in the problem. Checking reasonableness catches the most common error — using the right arithmetic but in the wrong order — and it is a habit that makes you a stronger problem-solver at every level of mathematics.
