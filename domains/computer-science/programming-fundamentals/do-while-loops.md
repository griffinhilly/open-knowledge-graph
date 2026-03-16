---
id: do-while-loops
title: Do-While Loops and Post-Test Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: while-loop-iteration
  type: hard
builds-toward:
- loop-control-statements
tags:
- loops
- iteration
- do-while
stage: abstract-reasoning
status: draft
---

# Do-While Loops and Post-Test Iteration

## Core Idea
A do-while loop executes its body at least once before checking the condition (post-test). This is useful for input validation and scenarios where one iteration is guaranteed. The loop repeats while the condition remains true.

## How It's Best Learned
Implement input validation with do-while. Compare do-while with while to see when do-while is clearer.

## Common Misconceptions
- Do-while and while behave identically (the difference is when the condition is tested; do-while always runs once).
- Do-while is rarely useful (it's essential for input validation and menu-driven programs).

## Explainer

You already know how a `while` loop works: it checks a condition *before* each iteration, and if the condition is false from the start, the body never runs at all. A **do-while loop** flips this order — it executes the body first, then checks the condition. The body always runs at least once, no matter what. In pseudocode the structure looks like: `do { ... } while (condition);` — and that trailing semicolon is important in languages like C and Java, because the statement ends after the condition, not after the closing brace.

The classic use case is **input validation**. Suppose you need to ask the user for a number between 1 and 10. With a `while` loop, you face an awkward bootstrapping problem: the condition depends on the user's input, but you haven't asked for input yet. You end up writing the prompt *before* the loop and then again *inside* the loop — duplicating code. A do-while loop eliminates this duplication naturally: prompt the user inside the body, then check whether the input is valid. If it is not, the loop repeats and prompts again. If it is, the loop exits. The first prompt happens automatically because the body always executes once.

Menu-driven programs follow the same pattern. You display a menu, read the user's choice, and process it. Then you check: did the user choose "quit"? If not, show the menu again. The menu must appear at least once for the user to make any choice at all, which is exactly the guarantee a do-while provides. Whenever you find yourself thinking "I need to do this thing, then maybe do it again depending on the result," a do-while loop is probably the cleanest fit. If the condition could reasonably be false before the first iteration — meaning zero iterations is a valid outcome — stick with a regular `while` loop instead.
