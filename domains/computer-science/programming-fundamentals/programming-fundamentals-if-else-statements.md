---
id: programming-fundamentals-if-else-statements
title: If-Else Conditional Statements
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-comparison-operators
  type: hard
builds-toward:
- programming-fundamentals-nested-conditions
- programming-fundamentals-switch-case
tags:
- control-flow
- conditionals
- if-else
stage: abstract-reasoning
status: draft
---

# If-Else Conditional Statements

## Core Idea
If-else statements execute different blocks of code based on a condition. The if block runs if the condition is true; the else block runs if false. Else-if chains check multiple conditions sequentially.

## Explainer

You already know how comparison operators produce boolean values — expressions like `score >= 90` evaluate to either true or false. An **if statement** takes that boolean result and uses it to decide which code to run. Think of it as a fork in the road: the program arrives at the if statement, evaluates the condition, and takes exactly one of two paths. If the condition is true, the code inside the if block executes. If false, the program skips that block entirely and continues after it.

The **else clause** provides an alternative path for when the condition is false. Without else, a false condition simply means "do nothing extra." With else, you guarantee that exactly one of two blocks will always run — never both, never neither. This is useful whenever you have a binary choice: pass or fail, logged in or not, positive or negative. For example, `if (temperature > 100) { print("boiling") } else { print("not boiling") }` always prints exactly one message regardless of the temperature value.

When you have more than two possibilities, **else-if chains** let you test multiple conditions in sequence. The program evaluates each condition from top to bottom and runs the block for the *first* condition that is true, then skips all remaining else-if and else blocks. Order matters: if you check `score >= 60` before `score >= 90`, a score of 95 would match the first condition and never reach the second. Always arrange else-if conditions from most specific to least specific, or from highest threshold to lowest. The final else at the bottom acts as a catch-all for anything that did not match any previous condition.

A common early mistake is writing multiple independent if statements when you meant an else-if chain. If you write three separate if statements, all three conditions are checked independently — multiple blocks could execute. With else-if, the conditions are mutually exclusive by structure: once one matches, the rest are skipped. Choosing between independent ifs and else-if chains is a design decision about whether your conditions can overlap.
