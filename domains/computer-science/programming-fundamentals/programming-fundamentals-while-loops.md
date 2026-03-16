---
id: programming-fundamentals-while-loops
title: While Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-if-else-statements
  type: hard
builds-toward:
- programming-fundamentals-for-loops
- programming-fundamentals-loop-control-statements
tags:
- control-flow
- loops
- while
stage: abstract-reasoning
status: draft
---

# While Loops

## Core Idea
A while loop repeatedly executes a block of code as long as a condition is true. The condition is checked before each iteration, so the loop may never execute if the condition is false.

## Explainer

You already know how if-else statements let your program choose between paths based on a condition. A **while loop** takes that same idea — test a condition, then act — and adds repetition. Instead of executing the body once and moving on, the program jumps back to the condition after each execution. If the condition is still true, the body runs again. This continues until the condition becomes false, at which point execution moves past the loop. The condition is checked *before* each iteration (called a **pre-test loop**), which means if the condition is false from the start, the body never executes at all.

Consider a concrete example: suppose you want to keep asking a user for a password until they enter the correct one. You cannot know in advance how many attempts it will take — it might be one, it might be twenty. A while loop handles this naturally: `while (password != correct)` keeps prompting. Each time through the loop, the user enters a new value, the condition is re-evaluated, and the loop either continues or exits. This is the while loop's strength: it handles situations where the number of repetitions is unknown ahead of time.

The most important discipline with while loops is ensuring **termination**. Every while loop needs something inside its body that eventually makes the condition false. If you write `while (x < 10)` but never change `x`, the loop runs forever — an **infinite loop** that freezes your program. The fix is straightforward: make sure the body contains a statement that moves you toward the exit condition. For a counter, that means incrementing it. For user input, that means reading new input each iteration. For a search, that means advancing through the data.

While loops form the foundation for all repetitive computation. Once you are comfortable with them, you will encounter for loops (which add structure for counted iteration) and loop control statements like `break` and `continue` (which give you finer-grained control over when to exit or skip). But every loop, no matter how fancy, is fundamentally a while loop in disguise: check a condition, do some work, check again.
