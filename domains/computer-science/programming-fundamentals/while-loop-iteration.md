---
id: while-loop-iteration
title: While Loops and Condition-Controlled Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: program-structure-and-flow
  type: hard
builds-toward:
- loop-control-statements
- nested-loops
tags:
- loops
- iteration
- while
stage: formal-systems
status: draft
---

# While Loops and Condition-Controlled Iteration

## Core Idea
A while loop repeats as long as a condition is true. The condition is checked before each iteration (pre-test). While loops are flexible and handle unknown iteration counts, such as processing until a sentinel value is read.

## How It's Best Learned
Write while loops that process data until a condition changes. Ensure loop guards prevent infinite loops.

## Common Misconceptions
- While loops always exit (an incorrect guard can cause infinite loops).
- While and for loops are equivalent (they have different strengths; for is clearer for counted loops, while for condition-based).

## Questions

```yaml
- question: "What does the following code print?\n\n    count = 5\n    while count < 3:\n        print(count)\n        count += 1"
  type: multiple-choice
  options:
    - "It prints 5, 6, 7 and then stops when count reaches some limit"
    - "It prints nothing — the condition is false before the loop begins"
    - "It runs forever because count keeps increasing away from 3"
    - "It prints 5 exactly once and then exits"
  answer: 1
  explanation: "A while loop is a pre-test loop: the condition is evaluated before the body executes. Here, count = 5 and the condition is count < 3, which is immediately false (5 is not less than 3). Because the condition fails on the very first check, the body never runs at all — the loop executes zero times. This distinguishes while loops from do-while loops, which always run at least once."

- question: "A programmer wants to find the first multiple of 7 greater than 50. They write:\n\n    n = 0\n    while n <= 50:\n        n += 7\n\nWhat is the value of n after the loop exits?"
  type: multiple-choice
  options:
    - "49 — the last multiple of 7 that is not greater than 50"
    - "50 — the loop stops when n reaches 50"
    - "56 — the loop exits when n first exceeds 50"
    - "7 — the loop runs only once"
  answer: 2
  explanation: "Tracing the loop: n goes 0, 7, 14, 21, 28, 35, 42, 49, then adds 7 to get 56. At n = 49, the condition 49 <= 50 is true, so the loop body runs once more, making n = 56. Now 56 <= 50 is false, so the loop exits. The key is that the condition is checked after each update — the loop doesn't stop the moment n exceeds 50, but after the body has already run."

- question: "A while loop is guaranteed to execute its body at least once."
  type: true-false
  answer: false
  explanation: "This is the defining characteristic of a pre-test loop: the condition is evaluated before the body runs. If the condition is false initially, the body is skipped entirely and the loop executes zero times. This is an intentional design feature — it lets while loops safely guard against executing when they should not. Do-while loops (in languages like C or Java) guarantee at least one execution, but standard while loops do not."

- question: "An infinite loop can occur if the variable that the while loop's condition depends on is never updated inside the loop body."
  type: true-false
  answer: true
  explanation: "For a while loop to terminate, something must change each iteration that moves the condition toward becoming false. If the condition checks x < 10 but the body never changes x, the condition will always be true and the loop runs forever. Even subtler bugs arise when the update moves in the wrong direction (e.g., the condition checks x < 10 but the body decrements x, moving it further away from 10). Building the habit of asking 'what changes each iteration?' prevents this entire class of bugs."

- question: "What question should you ask yourself about any while loop to verify it will eventually terminate, and why is that the right question?"
  type: short-answer
  answer: "Ask: 'What changes each iteration, and does that change bring the condition closer to being false?' This is the right question because a while loop terminates only when its condition becomes false. If nothing in the loop body affects the variables the condition depends on — or if the change moves them in the wrong direction — the condition never becomes false and the loop runs forever. Identifying the 'progress variable' and confirming it moves toward termination is the core safety check for any while loop."
  explanation: "This is an informal version of the loop invariant principle. Beyond just avoiding infinite loops, this question helps you reason about correctness: the loop will exit with the right result only if each iteration makes meaningful progress toward the goal and the condition accurately captures 'we're done.' When debugging a while loop that runs longer than expected, the first thing to check is whether the update is actually happening and in the right direction."
```

## Explainer

From your understanding of program structure and flow, you know that code normally executes sequentially — one statement after another, top to bottom. A **while loop** introduces controlled repetition by combining a condition test with a jump backward. The structure is simple: evaluate a boolean condition, execute the body if the condition is true, then return to the condition and evaluate again. This cycle continues until the condition evaluates to false, at which point the program resumes with the statement after the loop.

The "pre-test" nature of while loops is a key detail. Because the condition is checked *before* the body executes, a while loop can execute zero times. If you write `while (count < 0)` and count starts at 5, the body is skipped entirely. This distinguishes while loops from do-while loops (which you may encounter later), where the body always runs at least once. The pre-test design makes while loops safe for situations where you need to guard against executing the body when it should not run.

While loops are the natural choice when the number of repetitions is **not known in advance**. Classic examples include reading input until a user types "quit," searching a data structure until a target is found, or running a simulation until it converges. In each case, some event inside the loop body eventually makes the condition false. This is the **loop invariant** principle in informal terms: something must change each iteration that brings you closer to termination. A **sentinel value** — a special marker like -1 or "EOF" — is a common pattern for signaling when to stop. The loop reads data, checks for the sentinel, and exits when it appears.

The most dangerous mistake with while loops is the **infinite loop**: a loop whose condition never becomes false. This happens when the body fails to update the variables the condition depends on, or when the update moves in the wrong direction. For example, if the condition checks `x < 10` but the body decrements `x`, the value moves further from 10 with each iteration. Building the habit of asking "what changes each iteration, and does it move toward termination?" will prevent this class of bugs. As you advance to loop control statements and nested loops, you will gain tools like `break` to exit a loop early and `continue` to skip to the next iteration — but the fundamental while-loop pattern of condition-check-then-execute remains the backbone of all iterative computation.
