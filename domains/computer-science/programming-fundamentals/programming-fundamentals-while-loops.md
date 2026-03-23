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
stage: formal-systems
status: draft
---

# While Loops

## Core Idea
A while loop repeatedly executes a block of code as long as a condition is true. The condition is checked before each iteration, so the loop may never execute if the condition is false.

## Questions

```yaml
- question: "A student writes: x = 10 followed by while x > 0: print(x). What happens when this program runs?"
  type: multiple-choice
  options:
    - "It prints 10 once and stops, because the condition is only checked once"
    - "It prints 10, 9, 8, ... down to 1, then stops"
    - "It runs forever, printing 10 repeatedly, because x is never changed inside the loop"
    - "It never prints anything because x starts at 10, which is greater than 0"
  answer: 2
  explanation: "This is an infinite loop. x starts at 10, the condition x > 0 is true, so the body executes and prints 10. Then the condition is re-checked — x is still 10, still > 0 — so the body executes again. This repeats forever because nothing inside the loop body changes x. The fix is to add x -= 1 inside the loop so x decrements toward 0. Forgetting to advance toward the exit condition is the primary while-loop bug."

- question: "Which scenario is BEST suited to a while loop rather than a for loop?"
  type: multiple-choice
  options:
    - "Printing every number from 1 to 10"
    - "Processing each item in a list of known length"
    - "Repeatedly prompting a user to enter a valid password until they succeed"
    - "Adding up exactly 5 numbers entered by the user"
  answer: 2
  explanation: "While loops excel when the number of iterations is unknown in advance — you keep looping until a condition changes. A password prompt could resolve in 1 attempt or 20 — you can't know ahead of time. The other options all have a known, fixed iteration count (1–10, list length, exactly 5 numbers), which makes them natural candidates for for loops. This 'unknown count' pattern is the defining use case for while."

- question: "A while loop always executes its body at least once, because the condition is only checked after the first iteration."
  type: true-false
  answer: false
  explanation: "A while loop is a pre-test loop — the condition is evaluated BEFORE each iteration, including the very first one. If the condition is false at the start, the body never executes at all. (The loop that guarantees at least one execution is a do-while loop, which tests the condition after the first run.) A common mistake is assuming the body always runs at least once."

- question: "If a while loop's condition is false the very first time it is evaluated, the body of the loop will never execute."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of a pre-test loop. The while statement evaluates its condition before doing anything else. If that condition is immediately false, execution skips the entire loop body and continues with the code that follows. This means a while loop can execute zero times — which is often the correct behavior when there's nothing to process."

- question: "What is an infinite loop, and what must every while loop include to prevent one?"
  type: short-answer
  answer: "An infinite loop occurs when the condition never becomes false, causing the loop to run forever. To prevent one, the loop body must contain a statement that eventually makes the condition false — advancing a counter, reading new input, or moving through data toward a stopping point."
  explanation: "Every while loop implicitly answers: 'What changes each iteration to bring us closer to stopping?' If nothing in the body affects the condition, the loop will run forever. For a counter loop, that means incrementing the counter. For a search, advancing through the data. For a user-input loop, reading new input each time. Identifying the 'termination mechanism' before writing the loop is a good habit."
```

## Explainer

You already know how if-else statements let your program choose between paths based on a condition. A **while loop** takes that same idea — test a condition, then act — and adds repetition. Instead of executing the body once and moving on, the program jumps back to the condition after each execution. If the condition is still true, the body runs again. This continues until the condition becomes false, at which point execution moves past the loop. The condition is checked *before* each iteration (called a **pre-test loop**), which means if the condition is false from the start, the body never executes at all.

Consider a concrete example: suppose you want to keep asking a user for a password until they enter the correct one. You cannot know in advance how many attempts it will take — it might be one, it might be twenty. A while loop handles this naturally: `while (password != correct)` keeps prompting. Each time through the loop, the user enters a new value, the condition is re-evaluated, and the loop either continues or exits. This is the while loop's strength: it handles situations where the number of repetitions is unknown ahead of time.

The most important discipline with while loops is ensuring **termination**. Every while loop needs something inside its body that eventually makes the condition false. If you write `while (x < 10)` but never change `x`, the loop runs forever — an **infinite loop** that freezes your program. The fix is straightforward: make sure the body contains a statement that moves you toward the exit condition. For a counter, that means incrementing it. For user input, that means reading new input each iteration. For a search, that means advancing through the data.

While loops form the foundation for all repetitive computation. Once you are comfortable with them, you will encounter for loops (which add structure for counted iteration) and loop control statements like `break` and `continue` (which give you finer-grained control over when to exit or skip). But every loop, no matter how fancy, is fundamentally a while loop in disguise: check a condition, do some work, check again.
