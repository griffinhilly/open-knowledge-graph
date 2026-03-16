---
id: loop-control-statements
title: 'Loop Control: Break and Continue'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loop-iteration
  type: hard
- id: while-loop-iteration
  type: hard
builds-toward:
- nested-loops
tags:
- loops
- control
- break-continue
stage: abstract-reasoning
status: draft
---

# Loop Control: Break and Continue

## Core Idea
Break exits a loop immediately; continue skips the rest of the current iteration and proceeds to the next. These statements provide fine-grained control over loop execution without restructuring the loop condition.

## How It's Best Learned
Write loops that use break (e.g., to exit early on a match) and continue (e.g., to skip invalid values). Compare with conditional guards.

## Common Misconceptions
- Break and continue affect all enclosing loops (they only affect the innermost enclosing loop).
- Overusing break and continue is clearer (excessive use makes control flow harder to follow).

## Explainer

Your for loops and while loops already let you repeat code, but sometimes you need to deviate from the normal iteration pattern. Maybe you are searching a list for a specific value and want to stop as soon as you find it — there is no point continuing through the remaining elements. Or maybe you are processing a list of inputs and want to skip invalid entries without stopping the entire loop. **Break** and **continue** give you these two escape hatches.

**Break** immediately exits the loop, jumping to the first statement after the loop body. Consider searching for a name in a list of 1,000 entries. Without break, a for loop would check all 1,000 entries even if the name is the very first one. With break, you add a condition inside the loop: `if (current == target) { found = true; break; }`. The moment the target is found, the loop ends. This is both more efficient and more expressive — the code clearly communicates that finding the item is the stopping condition.

**Continue** is more subtle. Instead of exiting the loop entirely, it skips the rest of the current iteration and jumps back to the loop's condition check (or update step, in a for loop). Imagine processing a list of numbers but wanting to ignore negative values. You could wrap the entire loop body in an `if (value >= 0)` block, but continue provides a flatter structure: `if (value < 0) { continue; }` at the top of the loop, followed by the normal processing code. The effect is the same — negative values are skipped — but the code avoids deeply nested if statements.

The most important rule to remember is that break and continue affect only the **innermost enclosing loop**. If you have a loop inside a loop (nested loops, which you will study soon), a break in the inner loop exits only the inner loop — the outer loop keeps running. This trips up many learners who expect break to exit all enclosing loops at once. Some languages offer labeled breaks to exit an outer loop, but the default behavior is always innermost-only. A second caution: while break and continue are useful tools, overusing them can make your code harder to follow. If a loop has three breaks and two continues scattered throughout, it becomes difficult to reason about when and how the loop terminates. Use them purposefully — for early exit on search or for skipping invalid data — rather than as a substitute for a well-structured loop condition.
