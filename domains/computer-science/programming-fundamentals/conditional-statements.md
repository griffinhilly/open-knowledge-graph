---
id: conditional-statements
title: Conditional Statements
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: comparison-operators
  type: hard
- id: boolean-logic
  type: hard
- id: logical-operators
  type: soft
- id: program-structure
  type: soft
builds-toward:
- while-loops
- error-handling-exceptions
- else-if-chains
- switch-statements
tags:
- if
- else
- elif
- branching
- control flow
stage: formal-systems
status: validated
---
# Conditional Statements

## Core Idea
Conditional statements allow a program to choose between different paths of execution based on whether a boolean expression is true or false. An if statement executes a block only when its condition holds; an else clause handles the alternative; elif (or else if) chains allow multiple mutually exclusive branches. Conditionals are the foundation of decision-making in programs and are essential for handling different cases of input or state.

## How It's Best Learned
Trace through if-else chains by hand for several input values, including edge cases. Write a program that classifies input (e.g., grade letter from score) using nested and chained conditionals.

## Common Misconceptions
- Using = instead of == inside a condition.
- Forgetting that only the first true branch executes in an elif chain.
- Accidentally writing overlapping conditions that shadow intended cases.

## Questions

```yaml
- question: "A function assigns letter grades using conditions in this order: if score >= 60 → 'D', elif score >= 70 → 'C', elif score >= 80 → 'B', elif score >= 90 → 'A'. What grade does a score of 95 receive?"
  type: multiple-choice
  options:
    - "'A' — 95 satisfies the >= 90 condition"
    - "'D' — 95 satisfies >= 60, which is the first condition checked, so the chain stops there"
    - "'C' — elif conditions are checked in ascending order of threshold value"
    - "No grade — elif chains only run when all prior conditions are false"
  answer: 1
  explanation: "In an elif chain, the *first* true condition wins and all subsequent branches are skipped. Since 95 >= 60 is true, the function assigns 'D' and never evaluates the remaining conditions. This is why the most restrictive conditions must come first: >= 90, then >= 80, then >= 70, then >= 60 — putting the most permissive condition first intercepts all higher values before they can reach the correct branch."

- question: "A developer needs to print exactly one role-specific message for users who may be 'admin', 'editor', or 'viewer'. Which structure guarantees exactly one branch executes?"
  type: multiple-choice
  options:
    - "Three separate if statements, one for each role"
    - "An if / elif / elif chain with one condition per role"
    - "Three separate if statements each followed by a return statement"
    - "A single if statement containing all three role checks nested inside it"
  answer: 1
  explanation: "An if/elif chain guarantees mutual exclusivity — once a true condition is found, all remaining branches are skipped. Three independent if statements evaluate each condition separately; if the same input satisfied multiple conditions (e.g., through a bug), multiple blocks would execute. The elif structure enforces 'exactly one branch' by design, which is the correct tool whenever categories are mutually exclusive."

- question: "In a Python if/elif/elif chain, if the first condition evaluates to True, the interpreter still evaluates the remaining elif conditions to determine if any others also apply."
  type: true-false
  answer: false
  explanation: "The 'first match wins' rule: once a true condition is found in an if/elif chain, its block executes and the entire chain exits — subsequent conditions are never evaluated. This is a fundamental difference from writing separate if statements, where each condition is checked independently. If you need all matching conditions to be evaluated, you must use separate if statements; if you need exactly one branch to run, you use elif."

- question: "Replacing an if/else structure with two separate if statements can change a program's behavior when both conditions could be true at the same time."
  type: true-false
  answer: true
  explanation: "In an if/else, exactly one branch always executes — the else clause is a guaranteed alternative. Two separate if statements each check their condition independently, so both blocks can execute when both conditions are true. For example, `if x > 3: print('big')` followed by `if x > 5: print('very big')` both execute when x = 10, whereas `if x > 3: ... else: ...` runs exactly one block. The structures are not equivalent when conditions can overlap."

- question: "What is the 'first match wins' rule in an elif chain, and why does the order of conditions matter for correctness?"
  type: short-answer
  answer: "In an if/elif chain, Python evaluates conditions from top to bottom and executes the block of the first condition that is true, then skips all remaining branches. Because evaluation stops at the first match, broader or less restrictive conditions placed early will intercept cases that were intended for more specific conditions lower in the chain. Correct ordering requires placing the most restrictive conditions first."
  explanation: "A classic example: grading ranges must go from highest to lowest (>= 90, then >= 80, etc.). If >= 60 appears first, every score above 60 gets 'D' because that condition is always satisfied before the others are checked. The elif structure is powerful precisely because only one branch runs — but that power requires the programmer to order conditions so that the right condition matches first for every possible input value."
```

## Explainer

Up to this point, your programs have executed every line in order, top to bottom. **Conditional statements** give programs the ability to make decisions — to choose one path of execution over another based on the current state of the data. This is a fundamental leap: programs go from being simple calculators that always do the same thing to being responsive tools that adapt their behavior to different situations.

The basic building block is the **if statement**. It evaluates a boolean expression — a condition that is either true or false — and executes a block of code only when the condition is true. You already know from operators and expressions how to write comparisons like `x > 0` or `name == "Alice"`. The if statement uses these comparisons to control what happens next. If the condition is false, the block is simply skipped, and execution continues after it. Adding an **else** clause provides an alternative path: "if the condition is true, do this; otherwise, do that." Every possible input is now handled — one branch or the other will always execute.

When you have more than two possibilities, **elif** (or `else if`) chains let you test multiple conditions in sequence. The program checks each condition from top to bottom and executes the block of the *first* one that is true, then skips all the rest. This "first match wins" behavior is crucial to understand. If you write `if score >= 90: grade = "A"` followed by `elif score >= 80: grade = "B"`, a score of 95 matches the first condition and gets "A" — it never checks the second condition, even though 95 is also >= 80. This is why the order of conditions matters: put the most specific or restrictive conditions first.

A common beginner mistake is using separate if statements when you meant elif. If you write three independent `if` statements instead of an `if/elif/elif` chain, all three conditions are checked independently, and multiple blocks might execute. Another classic error is writing `if x = 5` (assignment) instead of `if x == 5` (comparison) — some languages catch this as a syntax error, but others silently treat the assignment as a truthy value. When your conditionals behave unexpectedly, the first thing to check is whether your conditions are actually testing what you think they are and whether your branches are properly exclusive.
