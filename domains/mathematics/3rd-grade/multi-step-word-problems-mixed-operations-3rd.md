---
id: multi-step-word-problems-mixed-operations-3rd
title: Solving Multi-Step Word Problems
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multi-step-word-problems-3rd
  type: hard
- id: multi-step-word-problems-addition-subtraction-3rd
  type: hard
tags:
- word-problems
- multi-step
- problem-solving
stage: concrete-operations
status: validated
---

# Solving Multi-Step Word Problems

## Core Idea
Multi-step word problems require multiple operations and decisions about which numbers to use and in what order. Students draw pictures, write equations, and solve step-by-step, checking that their answer makes sense.

## Questions

```yaml
- question: "Maria has 3 bags with 6 apples each. She gives 7 apples to her friends. How many does she have left? A student writes 6 − 7 = −1 as their first step. What went wrong?"
  type: multiple-choice
  options:
    - "The student used the wrong numbers from the problem"
    - "The student should have divided instead of subtracted"
    - "The student subtracted before multiplying, skipping the necessary first step of finding the total apples before any can be given away"
    - "The student got the correct answer; negative numbers are valid here"
  answer: 2
  explanation: "This problem requires two steps in a specific order: first, find the total apples (3 × 6 = 18), then subtract the ones given away (18 − 7 = 11). The subtraction step depends on the multiplication result — you cannot subtract from a quantity you haven't yet calculated. Performing the subtraction first uses a partial number (just 6, one bag's worth) instead of the full total, producing a nonsensical result. The order of steps is dictated by logic, not choice."

- question: "When beginning a multi-step word problem, what should you do first?"
  type: multiple-choice
  options:
    - "Identify the largest numbers in the problem and work with those first"
    - "Write a number sentence immediately so you can start calculating"
    - "Read the question carefully to identify what the final answer must be, then determine what intermediate steps are needed to get there"
    - "Find all the addition in the problem before looking for multiplication or division"
  answer: 2
  explanation: "The final question is your destination. Identifying it first lets you work backward to determine what intermediate results you need. Without this step, students often grab nearby numbers and apply a familiar operation rather than thinking through the logical sequence. In a multi-step problem, the question at the end of the paragraph determines which calculations are necessary — and in what order."

- question: "In a multi-step word problem, you can solve the steps in any order and still arrive at the correct final answer."
  type: true-false
  answer: false
  explanation: "Steps must follow a logical sequence because later steps depend on the results of earlier ones. If a problem requires finding a total before subtracting from it, performing the subtraction first uses the wrong number. The order of operations in word problems is determined by the dependencies between quantities — some results must exist before others can be computed."

- question: "Drawing a picture or diagram before calculating is a useful strategy for any student solving a multi-step word problem, not just students who struggle with arithmetic."
  type: true-false
  answer: true
  explanation: "Diagrams and pictures make the problem's structure visible — they show what quantities are known, what is unknown, and how the pieces relate. This planning step helps all students, including strong ones, by ensuring they understand the problem before committing to calculations. Writing equations with labeled unknowns (□ or a letter) also keeps thinking visible and makes errors easier to find. The diagram is not a crutch; it is part of correct problem-solving process."

- question: "After solving a multi-step word problem, why is it important to check whether your answer makes sense within the context of the story?"
  type: short-answer
  answer: "The context sets boundaries on what is reasonable. If a problem says there are 25 students in a class and your answer is that 40 students received something, the story itself tells you that is impossible — your check caught an error before it was accepted as correct. Arithmetic can be executed correctly step by step and still produce a contextually impossible answer if the wrong operations were applied or the wrong numbers were used. Checking the answer against the story verifies that the plan was correct, not just the calculations."
  explanation: "This check is sometimes called a 'reasonableness check' and is distinct from checking the arithmetic. A student can recheck 4 × 8 = 32 and 32 − 9 = 23 perfectly and still have the wrong answer if they used the wrong operation at the first step. Only asking 'does this make sense in the story?' catches that kind of structural error."
```

## Explainer

You have already solved multi-step problems using only addition and subtraction. Now the challenge expands: problems can mix any operations — addition, subtraction, multiplication, and division — and you must decide which operation belongs at each step. The skill is not just arithmetic; it is reading carefully and building a plan before you calculate anything.

Start by reading the whole problem once, then ask: **what is the question asking for?** That final goal is your destination. Then identify all the information given and ask what you need to find *before* you can answer the final question. Often there is an intermediate result — a quantity the problem does not ask for directly but that you must calculate first. For example: "There are 4 boxes of crayons with 8 crayons each. Maya gives away 9 crayons. How many does she have left?" The question asks for crayons left, but first you need the total crayons: 4 × 8 = 32. Then: 32 − 9 = 23. The multiplication happens before the subtraction because the subtraction depends on that result.

Drawing a picture or writing a diagram before calculating is not slowing you down — it is the fastest path to the right answer. Label what each number represents. When you write an equation, use a box or letter for the unknown: 4 × 8 = □, then □ − 9 = 23. Writing equations step by step keeps your thinking visible and makes it easy to spot where you went wrong if the answer looks off.

Always check your final answer against the story. If a problem says a class has 25 students and your answer says 40 students received something, that is impossible — your check caught an error before you moved on. A useful question is: "Is this answer the right size for what was asked?" Problems with mixed operations are really problems in **logical sequencing**: figure out the order of steps, execute each one, and verify the result makes sense in context. That reasoning skill applies to every multi-step situation you will encounter, in math and far beyond it.
