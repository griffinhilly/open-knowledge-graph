---
id: programming-fundamentals-loop-control-statements
title: 'Loop Control: Break and Continue'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-while-loops
  type: hard
builds-toward:
- programming-fundamentals-loop-patterns
tags:
- control-flow
- loops
- break
- continue
stage: formal-systems
status: draft
---

# Loop Control: Break and Continue

## Core Idea
Break exits a loop immediately, skipping remaining iterations. Continue skips the current iteration but continues looping. These statements allow fine-grained control over loop execution.

## Questions

```yaml
- question: "A program searches a list for the first positive number and should stop as soon as it finds one. Which statement correctly completes this logic?\n\n    for num in numbers:\n        if num > 0:\n            print(num)\n            ???"
  type: multiple-choice
  options:
    - "Use `break` — it exits the loop immediately after finding the first positive number"
    - "Use `continue` — it skips to the next number and keeps looking"
    - "Use `break` — it skips the negative numbers and resumes from the top"
    - "Use `continue` — it stops the loop and returns the found value"
  answer: 0
  explanation: "`break` terminates the entire loop immediately, which is exactly what you want when the search is complete. `continue` would skip the current iteration and move to the next one — the opposite of stopping. The common misconception is confusing `continue` (skip this item, keep going) with `break` (stop the entire loop). If you used `continue` here, the loop would keep running through the rest of the list unnecessarily."

- question: "What happens when Python executes `continue` inside a while loop?"
  type: multiple-choice
  options:
    - "The loop terminates immediately and execution resumes after the loop"
    - "The rest of the current iteration is skipped, and execution jumps back to the while condition check"
    - "The loop restarts from the beginning with all variables reset"
    - "The function containing the loop returns to its caller"
  answer: 1
  explanation: "`continue` does not exit the loop — it only skips the remainder of the current iteration. Execution jumps back to the loop's condition check, and if the condition is still true, the loop continues with the next iteration. This is the critical distinction from `break`: `break` ends the loop, `continue` just ends the current pass through the loop body."

- question: "`break` and `continue` both affect loop execution, but only `break` can cause the loop to terminate before its condition becomes false."
  type: true-false
  answer: true
  explanation: "`break` exits the loop immediately regardless of the loop condition's current value. `continue` jumps back to the condition check, so the loop will only stop when the condition becomes false in the normal way (or another `break` is hit). `continue` never terminates the loop itself."

- question: "Using `continue` in a while loop prevents infinite loops, because `continue` always advances the loop toward its termination condition."
  type: true-false
  answer: false
  explanation: "`continue` jumps back to the condition check, but it does not guarantee the condition moves toward false. If the variable that drives the loop condition isn't updated before the `continue`, you can still have an infinite loop. For example, `while True: continue` loops forever. `continue` is about skipping iteration logic, not about advancing toward termination."

- question: "Explain the difference between `break` and `continue`, and describe a situation where each would be the appropriate choice."
  type: short-answer
  answer: "`break` exits the entire loop immediately; `continue` skips the rest of the current iteration and returns to the loop's condition check. `break` is appropriate when you've found what you're looking for and further iterations are unnecessary (e.g., finding the first matching item in a list). `continue` is appropriate when certain items should be skipped but the loop should keep running (e.g., skipping negative numbers while processing a list)."
  explanation: "Both statements give finer control than the loop condition alone, but they operate at different scopes. Think of the conveyor belt analogy: `continue` pushes a defective item off the belt while it keeps moving; `break` hits the emergency stop and halts the belt entirely. Choosing the wrong one is a common bug — using `continue` when you mean `break` causes the loop to run through all remaining iterations unnecessarily."
```

## Explainer

You already know how while loops work: they repeat a block of code as long as a condition is true. But sometimes the logic you need does not fit neatly into a single loop condition. Suppose you are searching a list for a specific value. The loop condition says "keep going while there are elements left to check," but once you find the value, continuing to check the rest is wasted work. This is exactly where **break** comes in — it immediately exits the loop, jumping execution to the first line after the loop body. Think of it as an emergency exit: regardless of whether the loop condition is still true, `break` ends the loop right now.

**Continue** is subtler. Rather than exiting the loop entirely, it skips the rest of the current iteration and jumps back to the loop's condition check. Imagine you are processing a list of numbers and want to skip negative values. Instead of wrapping the entire loop body in an `if` block, you can put `if value < 0: continue` at the top. When a negative value is encountered, `continue` skips straight to the next iteration. The loop itself keeps running — only the current pass is cut short. This leads to flatter, more readable code because it avoids deeply nested conditional blocks inside loops.

A useful mental model is to think of a conveyor belt in a factory. Each item on the belt is one loop iteration. **Continue** is like an inspector who spots a defective item and pushes it off the belt — the belt keeps moving, and the next item comes along. **Break** is someone hitting the emergency stop button — the belt halts entirely. Both give you finer control than the loop condition alone provides, and you will find them especially useful when working with search patterns, input validation, and filtering — the kind of loop patterns you will encounter next.
