---
id: programming-fundamentals-for-loops
title: For Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-while-loops
  type: soft
builds-toward:
- programming-fundamentals-iteration-collections
- programming-fundamentals-loop-patterns
tags:
- control-flow
- loops
- for
stage: abstract-reasoning
status: draft
---

# For Loops

## Core Idea
A for loop repeats a block of code a specific number of times using a loop variable (counter). The loop header specifies initialization, condition, and increment, making it ideal for known iteration counts.

## Explainer

If you have worked with while loops, you already understand the core mechanic of repetition: check a condition, execute a body, repeat. A **for loop** packages the same idea into a more compact structure designed for situations where you know in advance how many times to repeat. Instead of scattering the initialization, condition check, and counter update across multiple lines, the for loop header bundles all three into a single line — typically written as `for (init; condition; update)`. This makes the loop's intent immediately visible: "start here, stop when this is false, step by this amount each time."

Consider printing the numbers 1 through 10. With a while loop you would declare a counter variable, write the condition, and remember to increment the counter inside the body. With a for loop, all of that fits in the header: `for (int i = 1; i <= 10; i++)`. The body contains only the actual work — the print statement. This compression is not just cosmetic. By keeping the loop machinery in one place, for loops reduce a common class of bugs: forgetting to update the counter (which causes an infinite loop) or initializing it in the wrong place (which causes off-by-one errors).

The **loop variable** (often called `i`, `j`, or `k` by convention) serves as a counter that tracks which iteration you are on. It is initialized once before the loop begins, tested before each iteration, and updated after each iteration completes. In most languages the loop variable is scoped to the loop itself, meaning it does not exist outside the for block. This scoping prevents accidental reuse of a stale counter value later in your program.

For loops shine when the number of iterations is determined before the loop starts — counting from 0 to n, iterating over indices of an array, or repeating an action exactly five times. When the termination condition depends on something unpredictable (user input, a file running out of data, a search finding its target), a while loop is usually clearer. Choosing between the two is a matter of expressing intent: use a for loop when the iteration count is known, and a while loop when it is not. As you move on to iterating over collections, you will see that many languages extend the for loop with a "for-each" variant that removes the counter entirely — but the underlying idea of structured, bounded repetition stays the same.
