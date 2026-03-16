---
id: while-loops
title: While Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: conditional-statements
  type: hard
- id: boolean-logic-programming
  type: soft
builds-toward:
- for-loops
- loop-control-statements
- recursion-basics
tags:
- while
- iteration
- loops
- control flow
- termination
stage: abstract-reasoning
status: validated
---

# While Loops

## Core Idea
A while loop repeatedly executes a block of code as long as its condition remains true. Before each iteration the condition is evaluated; when it becomes false the loop exits and execution continues after the loop body. The loop body must eventually cause the condition to become false, or the loop runs forever (an infinite loop). While loops are best used when the number of iterations is not known in advance.

## How It's Best Learned
Trace loops by hand, updating a variable table after each iteration. Deliberately create an infinite loop, observe the behavior, and fix it. Implement classic examples: countdown, sum of digits, user input validation.

## Common Misconceptions
- Forgetting to update the loop variable inside the body, causing an infinite loop.
- Off-by-one errors in the condition (< vs <=).
- Assuming the condition is checked continuously rather than only at the top of each iteration.

## Explainer

You already understand conditional statements — the idea that a program can check a condition and decide what to do. A **while loop** extends this idea by adding repetition: instead of checking the condition once, the program checks it *before every iteration* and keeps executing the loop body as long as the condition remains true. The structure is `while (condition) { body }`. The computer evaluates the condition; if true, it runs the body, then goes back and evaluates the condition again. This cycle repeats until the condition is false, at which point the loop exits and the program continues with whatever comes after.

The critical design requirement is that **something inside the loop body must eventually make the condition false**. If nothing changes the variables involved in the condition, the condition stays true forever and the loop never exits — this is an **infinite loop**, and it is one of the most common bugs beginners encounter. Typically, the loop body updates a counter, advances through a data structure, or receives new input. For example, in a countdown loop, you decrement a counter each iteration: `while (count > 0) { print(count); count = count - 1; }`. The counter decreases each time, eventually reaching zero, at which point `count > 0` is false and the loop ends.

While loops are the right tool when you **do not know in advance how many iterations you need**. Reading user input until they type "quit," searching a list until you find a match, or repeatedly halving a number until it drops below a threshold — in all these cases, the number of repetitions depends on data you do not have until the program is running. This distinguishes while loops from for loops (which you will learn next), where the iteration count is typically known or bounded at the start.

One subtle point: the condition is checked only at the **top** of each iteration, not continuously during the body. If the condition becomes false partway through the body, the rest of the body still finishes executing before the loop checks again. This means a while loop always completes its current iteration in full. Understanding this timing is essential for avoiding off-by-one errors — the most common mistake is using `<` when you meant `<=` (or vice versa), causing the loop to run one too many or one too few times. When in doubt, trace through the first two and last two iterations by hand, tracking every variable, to verify your loop does exactly what you intend.
