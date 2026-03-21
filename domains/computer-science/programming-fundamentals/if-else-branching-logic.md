---
id: if-else-branching-logic
title: 'If-Else: Branching Logic'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: conditional-statements
  type: hard
- id: comparison-operators-and-boolean-tests
  type: hard
builds-toward:
- conditional-logic-chains
- loop-design-and-invariants
tags:
- control-flow
- branching
- conditionals
stage: formal-systems
status: draft
---

# If-Else: Branching Logic

## Core Idea
If-else statements execute different code based on a condition. Only one branch executes. The condition must be a boolean or evaluate to one. Proper if-else structure prevents logic errors and makes intent clear.

## How It's Best Learned
Trace if-else execution on paper with different inputs; test both branches (true and false conditions) to verify behavior.

## Common Misconceptions
That both branches execute; that the condition can be any expression (it must be boolean-valued); that if without else is incomplete.

## Questions

```yaml
- question: "Consider: `if score >= 60: grade = 'Pass'` / `else: grade = 'Fail'`. What grade does `score = 60` receive?"
  type: multiple-choice
  options:
    - "'Fail', because 60 is the threshold value, not above it"
    - "'Pass', because 60 >= 60 evaluates to True"
    - "Both 'Pass' and 'Fail', since 60 is a boundary value"
    - "An error, because boundary values require special handling"
  answer: 1
  explanation: "The condition `60 >= 60` evaluates to `True`, so the if-block runs (grade = 'Pass') and the else-block is completely skipped. This is a common source of off-by-one confusion: >= includes the boundary value, while > would exclude it. Tracing the exact comparison operator and applying it to the boundary input is essential — option A is the mistake of confusing >= with >."

- question: "What happens when the if-condition is True in an if-else statement?"
  type: multiple-choice
  options:
    - "The if-block executes first, then the else-block executes as a fallback"
    - "The if-block executes and the else-block is completely skipped"
    - "Both blocks execute in parallel, and the last one wins"
    - "The else-block is checked first to see if it should override the if-block"
  answer: 1
  explanation: "In an if-else, exactly one branch runs — never both, never neither. When the condition is True, the if-block executes and the else-block is entirely skipped. When the condition is False, the if-block is skipped and the else-block executes. Think of it as a fork in a road: choosing one path means not taking the other. This mutual exclusivity is the defining property of if-else branching."

- question: "If an if-condition evaluates to True, the else block does not execute at all."
  type: true-false
  answer: true
  explanation: "True. This is the fundamental guarantee of if-else: exactly one branch executes. When the condition is True, execution enters the if-block and then jumps past the else-block entirely. There is no partial or conditional execution of the else branch — it is completely bypassed. This mutual exclusivity is what makes if-else useful for distinguishing two cases."

- question: "An if statement without an else clause is always a programming error that should be fixed."
  type: true-false
  answer: false
  explanation: "False. An if without else is completely legitimate — it means 'if the condition is true, do this; otherwise, do nothing and continue.' This is correct whenever you only need to act in one case: `if temperature > 100: send_alert()` needs no else because there is nothing special to do at normal temperatures. Adding a meaningless empty else block would be clutter, not an improvement. The else clause should only appear when there is a meaningful action for the false case."

- question: "Why should you test both the true and false branches when debugging if-else logic, and what inputs are most revealing?"
  type: short-answer
  answer: "Testing only one branch leaves the other branch unverified — bugs often hide in the untested path. Boundary inputs are the most revealing: they sit exactly at the threshold of the condition and are the values most likely to expose off-by-one errors. For a condition like `x > 0`, test x = 1 (if-branch), x = -1 (else-branch), and x = 0 (boundary — which branch does it take, and is that the intended behavior?)."
  explanation: "This is the minimal form of branch coverage testing. A correct if-else must behave correctly for ALL inputs, not just the ones you expected. The condition `if x > 0: print('positive')` / `else: print('negative')` has a latent bug when x = 0 — it prints 'negative' for zero. This bug is invisible if you only test positive and negative values, but immediately visible when you test the boundary. Systematic boundary testing is the single most effective technique for catching branching bugs."
```

## Explainer

From conditional statements and comparison operators, you know that a program can test whether a condition is true or false, and that comparisons like `x > 10` or `name == "Alice"` produce boolean values. **If-else branching** takes this a step further: it lets your program choose between two different actions based on the result of such a test. This is the fundamental mechanism that makes programs behave differently under different circumstances, rather than always doing the same thing regardless of input.

The structure is straightforward: `if condition: do_this` / `else: do_that`. When the program reaches the if-else statement, it evaluates the condition. If the condition is `True`, the if-block executes and the else-block is skipped entirely. If the condition is `False`, the if-block is skipped and the else-block executes. **Exactly one branch runs — never both, never neither** (assuming both blocks are present). Think of it as a fork in a road: you must go left or right, and going left means you do not go right.

The `else` clause is optional. A standalone `if` without `else` means "do this if the condition is true; otherwise, do nothing and continue." This is appropriate when you only need to act in one case — for example, `if temperature > 100: print("Warning: overheating!")` does not need an else because there is nothing special to do when the temperature is normal. However, when you have two distinct actions for the two cases (like "if the user is logged in, show the dashboard; otherwise, show the login page"), the if-else pair makes the mutual exclusivity of the two paths explicit and readable.

A common source of bugs is writing conditions that do not properly cover the intended cases. If you write `if x > 0: print("positive")` / `else: print("negative")`, you have a bug: zero is not positive, but your code labels it negative because the else catches *everything* that is not greater than zero. Tracing through your if-else logic with specific test values — including edge cases like 0, empty strings, or boundary values — is the single most effective debugging technique for branching code. Start with at least one value that should take the if-branch and one that should take the else-branch, then test boundary inputs where the behavior might be ambiguous.
