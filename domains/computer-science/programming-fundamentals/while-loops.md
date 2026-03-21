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
stage: formal-systems
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

## Questions

```yaml
- question: "Consider this loop: `count = 3; while (count > 0) { print(count); }`. What happens when it runs?"
  type: multiple-choice
  options:
    - "It prints 3, 2, 1 then stops"
    - "It prints 3 once, because the condition is checked after the body"
    - "It runs forever, printing 3 indefinitely"
    - "It prints nothing, because count starts at 3 which is greater than 0"
  answer: 2
  explanation: "The loop body never modifies `count`, so the condition `count > 0` remains true forever — this is an infinite loop. The most common while-loop bug is forgetting to update the variable controlling the condition. The loop should include `count = count - 1` (or `count--`) inside the body. Option A is what the corrected version would do; option B gets the condition-checking timing wrong (it is checked at the top, not after the body)."

- question: "A loop starts with `count = 0` and has the condition `while (count < 5)`. How many times does the body execute?"
  type: multiple-choice
  options:
    - "4 times (0, 1, 2, 3)"
    - "5 times (0, 1, 2, 3, 4)"
    - "6 times (0, 1, 2, 3, 4, 5)"
    - "It depends on what is inside the body"
  answer: 1
  explanation: "With `count` starting at 0 and incrementing by 1 each iteration, the body executes when count = 0, 1, 2, 3, 4 — five times. When count reaches 5, the condition `count < 5` is false and the loop exits without running. This is the classic off-by-one question: `< 5` gives five iterations (0 through 4), while `<= 5` would give six iterations (0 through 5). Tracing through the first and last iterations by hand is the reliable way to resolve these."

- question: "A while loop checks its condition continuously — if the condition becomes false in the middle of the loop body, the loop exits immediately at that point."
  type: true-false
  answer: false
  explanation: "The condition is checked only at the TOP of each iteration, not continuously during the body. Once the loop body starts executing, it runs to completion before the condition is checked again. This means a while loop always finishes its current iteration in full, even if the condition would be false halfway through. Understanding this timing is essential for reasoning about loop behavior and avoiding subtle bugs."

- question: "A while loop may execute its body zero times if its condition is false when the loop is first reached."
  type: true-false
  answer: true
  explanation: "The condition is evaluated BEFORE the first execution of the body. If the condition is already false, the loop body never runs at all — execution jumps immediately to whatever code follows the loop. This is different from a do-while loop, which executes the body at least once before checking the condition. This behavior is intentional and useful: it means you can safely enter a while loop even when the data might already satisfy the exit condition."

- question: "Why must something inside a while loop's body eventually make the condition false? What happens if it doesn't, and how do you design against it?"
  type: short-answer
  answer: "If nothing in the body changes the variables in the condition, the condition evaluates to the same value every iteration and the loop never exits — this is an infinite loop. To prevent it, identify which variable(s) the condition depends on, and ensure the body contains code that moves those variables toward the exit condition. Common patterns: decrement a counter, advance an index, read new input, or narrow a search range. Tracing the first few and last iteration by hand verifies the loop terminates correctly."
  explanation: "A while loop is essentially a contract: 'keep going as long as this is true.' If the body never changes what 'this' evaluates to, the contract is never renegotiated and the loop is stuck. Infinite loops are especially insidious because the program doesn't crash — it just hangs, consuming CPU. Good loop design always makes the termination condition explicit: after writing the condition, ask 'what code in the body guarantees this eventually becomes false?'"
```

## Explainer

You already understand conditional statements — the idea that a program can check a condition and decide what to do. A **while loop** extends this idea by adding repetition: instead of checking the condition once, the program checks it *before every iteration* and keeps executing the loop body as long as the condition remains true. The structure is `while (condition) { body }`. The computer evaluates the condition; if true, it runs the body, then goes back and evaluates the condition again. This cycle repeats until the condition is false, at which point the loop exits and the program continues with whatever comes after.

The critical design requirement is that **something inside the loop body must eventually make the condition false**. If nothing changes the variables involved in the condition, the condition stays true forever and the loop never exits — this is an **infinite loop**, and it is one of the most common bugs beginners encounter. Typically, the loop body updates a counter, advances through a data structure, or receives new input. For example, in a countdown loop, you decrement a counter each iteration: `while (count > 0) { print(count); count = count - 1; }`. The counter decreases each time, eventually reaching zero, at which point `count > 0` is false and the loop ends.

While loops are the right tool when you **do not know in advance how many iterations you need**. Reading user input until they type "quit," searching a list until you find a match, or repeatedly halving a number until it drops below a threshold — in all these cases, the number of repetitions depends on data you do not have until the program is running. This distinguishes while loops from for loops (which you will learn next), where the iteration count is typically known or bounded at the start.

One subtle point: the condition is checked only at the **top** of each iteration, not continuously during the body. If the condition becomes false partway through the body, the rest of the body still finishes executing before the loop checks again. This means a while loop always completes its current iteration in full. Understanding this timing is essential for avoiding off-by-one errors — the most common mistake is using `<` when you meant `<=` (or vice versa), causing the loop to run one too many or one too few times. When in doubt, trace through the first two and last two iterations by hand, tracking every variable, to verify your loop does exactly what you intend.
