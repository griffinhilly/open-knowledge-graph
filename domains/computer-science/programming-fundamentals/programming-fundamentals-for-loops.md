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
stage: formal-systems
status: draft
---

# For Loops

## Core Idea
A for loop repeats a block of code a specific number of times using a loop variable (counter). The loop header specifies initialization, condition, and increment, making it ideal for known iteration counts.

## Questions

```yaml
- question: "Which is the best reason to use a for loop instead of a while loop when printing numbers from 1 to 100?"
  type: multiple-choice
  options:
    - "For loops execute faster than while loops at runtime"
    - "The iteration count is known in advance, and bundling initialization, condition, and update in the header makes the loop's bounds immediately visible and prevents forgetting the counter update"
    - "While loops cannot count upward; they can only repeat until a condition becomes false"
    - "For loops automatically manage the counter variable so you do not need to declare it yourself"
  answer: 1
  explanation: "The for loop's advantage is clarity and safety, not speed. By keeping initialization (i = 1), condition (i <= 100), and increment (i++) together in a single header, the loop's structure is immediately visible and the counter update cannot be accidentally omitted — which would cause an infinite loop. While loops can absolutely count upward; the distinction is which structure best expresses the programmer's intent for bounded iteration."

- question: "A student writes `for (int i = 1; i <= 5; i++) { ... }` and then tries to print the value of i after the loop ends. What happens in most languages?"
  type: multiple-choice
  options:
    - "i equals 6 because the loop incremented it one final time before the condition failed"
    - "i equals 5 because that was its last valid value inside the loop"
    - "In most languages, i is out of scope and cannot be accessed outside the for block"
    - "i resets to 1 because the loop variable is reinitialized when the loop completes"
  answer: 2
  explanation: "In most languages (Java, C, C++, Rust), the loop variable is scoped to the for block and does not exist outside it. This is intentional: limiting scope prevents accidentally using a stale counter value in subsequent code. If the student needs to retain the final value, they must declare a variable outside the loop. Scoping the variable to the loop is a feature that reduces bugs, not a limitation."

- question: "The primary structural advantage of a for loop over a while loop is that it places initialization, condition, and update together in one header line, making the loop's bounds immediately visible."
  type: true-false
  answer: true
  explanation: "This is precisely the design purpose of the for loop. The compression is not purely cosmetic: grouping all three pieces of loop machinery together makes it harder to accidentally separate them — for example, burying the increment inside a conditional in the body where it might sometimes be skipped. The intent of bounded iteration is expressed in one place, making the loop easier to read, debug, and verify."

- question: "A for loop is always the best choice for repetition because it is more flexible than a while loop and can handle any repetition scenario."
  type: true-false
  answer: false
  explanation: "Each loop type has its best use case. For loops are ideal when the iteration count is known before the loop starts. When the termination condition depends on something that cannot be determined in advance — user input, reading until end of file, searching for a value — a while loop is clearer and more idiomatic. Forcing all loops into a for structure when the iteration count is unknown produces awkward code and obscures the programmer's intent."

- question: "Why does bundling initialization, condition check, and counter update in the for loop header reduce bugs compared to writing each element separately, as in a while loop?"
  type: short-answer
  answer: "When the three loop control elements are scattered — initialization before the loop, condition at the top, update somewhere in the body — it is easy to forget one or place it incorrectly. Forgetting the update causes an infinite loop; placing the update inside a conditional means it might sometimes be skipped; wrong initialization causes off-by-one errors. The for loop header keeps all three visible in one line, making the loop's complete structure readable at a glance and reducing the number of separate places where something can go wrong."
  explanation: "This is why experienced programmers reach for a for loop when the iteration count is known: not for speed, but for the encapsulated structure. Anyone reading the code can immediately see the starting value, stopping condition, and step size without scanning the full loop body. This makes code reviews and debugging faster and reduces an entire class of loop-related bugs."
```

## Explainer

If you have worked with while loops, you already understand the core mechanic of repetition: check a condition, execute a body, repeat. A **for loop** packages the same idea into a more compact structure designed for situations where you know in advance how many times to repeat. Instead of scattering the initialization, condition check, and counter update across multiple lines, the for loop header bundles all three into a single line — typically written as `for (init; condition; update)`. This makes the loop's intent immediately visible: "start here, stop when this is false, step by this amount each time."

Consider printing the numbers 1 through 10. With a while loop you would declare a counter variable, write the condition, and remember to increment the counter inside the body. With a for loop, all of that fits in the header: `for (int i = 1; i <= 10; i++)`. The body contains only the actual work — the print statement. This compression is not just cosmetic. By keeping the loop machinery in one place, for loops reduce a common class of bugs: forgetting to update the counter (which causes an infinite loop) or initializing it in the wrong place (which causes off-by-one errors).

The **loop variable** (often called `i`, `j`, or `k` by convention) serves as a counter that tracks which iteration you are on. It is initialized once before the loop begins, tested before each iteration, and updated after each iteration completes. In most languages the loop variable is scoped to the loop itself, meaning it does not exist outside the for block. This scoping prevents accidental reuse of a stale counter value later in your program.

For loops shine when the number of iterations is determined before the loop starts — counting from 0 to n, iterating over indices of an array, or repeating an action exactly five times. When the termination condition depends on something unpredictable (user input, a file running out of data, a search finding its target), a while loop is usually clearer. Choosing between the two is a matter of expressing intent: use a for loop when the iteration count is known, and a while loop when it is not. As you move on to iterating over collections, you will see that many languages extend the for loop with a "for-each" variant that removes the counter entirely — but the underlying idea of structured, bounded repetition stays the same.
