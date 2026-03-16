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
stage: abstract-reasoning
status: draft
---

# Loop Control: Break and Continue

## Core Idea
Break exits a loop immediately, skipping remaining iterations. Continue skips the current iteration but continues looping. These statements allow fine-grained control over loop execution.

## Explainer

You already know how while loops work: they repeat a block of code as long as a condition is true. But sometimes the logic you need does not fit neatly into a single loop condition. Suppose you are searching a list for a specific value. The loop condition says "keep going while there are elements left to check," but once you find the value, continuing to check the rest is wasted work. This is exactly where **break** comes in — it immediately exits the loop, jumping execution to the first line after the loop body. Think of it as an emergency exit: regardless of whether the loop condition is still true, `break` ends the loop right now.

**Continue** is subtler. Rather than exiting the loop entirely, it skips the rest of the current iteration and jumps back to the loop's condition check. Imagine you are processing a list of numbers and want to skip negative values. Instead of wrapping the entire loop body in an `if` block, you can put `if value < 0: continue` at the top. When a negative value is encountered, `continue` skips straight to the next iteration. The loop itself keeps running — only the current pass is cut short. This leads to flatter, more readable code because it avoids deeply nested conditional blocks inside loops.

A useful mental model is to think of a conveyor belt in a factory. Each item on the belt is one loop iteration. **Continue** is like an inspector who spots a defective item and pushes it off the belt — the belt keeps moving, and the next item comes along. **Break** is someone hitting the emergency stop button — the belt halts entirely. Both give you finer control than the loop condition alone provides, and you will find them especially useful when working with search patterns, input validation, and filtering — the kind of loop patterns you will encounter next.
