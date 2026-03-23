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
stage: formal-systems
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

## Questions

```yaml
- question: "You need to prompt a user for a positive integer and keep asking until they give one. Which loop structure handles this most cleanly?"
  type: multiple-choice
  options:
    - "A while loop: check the condition first, then prompt inside the loop"
    - "A for loop: iterate a fixed number of times until the input is valid"
    - "A do-while loop: prompt inside the body, then check if the input is valid"
    - "A while loop with the prompt written both before the loop and inside it"
  answer: 2
  explanation: "A do-while loop is the cleanest fit because you must prompt at least once to get any input — you can't test validity before the user has entered anything. With a do-while, you prompt in the body, then test the result. If invalid, the loop repeats. Option D (while loop with duplicated prompt) works but violates DRY — you're writing the same code twice because you need at least one execution before testing. This 'bootstrapping problem' is exactly what do-while is designed to solve."

- question: "What happens when a do-while loop's condition is false the very first time it is evaluated?"
  type: multiple-choice
  options:
    - "The loop body never executes — identical behavior to a while loop with a false condition"
    - "The loop body executes exactly once, then the loop terminates"
    - "A runtime error occurs because the condition was never initialized"
    - "The loop body executes, then the condition is re-evaluated repeatedly until true"
  answer: 1
  explanation: "This is the defining difference between do-while and while. In a do-while loop, the condition is checked AFTER the body executes — so the body always runs at least once, regardless of the condition. Even if the condition is false on first evaluation, the loop body has already completed one iteration. This guaranteed-first-execution is exactly why do-while is the right tool when one pass is unconditionally required."

- question: "A do-while loop and a while loop that contain identical bodies and conditions will always produce identical results."
  type: true-false
  answer: false
  explanation: "They differ when the condition is false before the first iteration. A while loop with an initially false condition executes zero times. A do-while loop with the same condition executes once. This distinction matters in input validation: a while loop requires a 'seed' value or duplicated prompt before entering the loop, while a do-while handles the first iteration naturally. If the condition is always true on first entry, they produce the same results — but that is a special case, not the general rule."

- question: "The do-while loop always executes its body at least once, regardless of whether the condition is true or false."
  type: true-false
  answer: true
  explanation: "This is the core guarantee of the do-while construct. Because the condition check comes after the body (post-test), the body must execute before the condition is ever evaluated. The condition can be false from the start — the loop still completes one iteration before checking. This makes do-while useful precisely in situations where zero iterations is not a valid outcome — you always need at least one run of the code."

- question: "Why is a do-while loop more natural than a while loop for input validation? What problem does it solve?"
  type: short-answer
  answer: "Input validation requires asking the user for input before you can test whether it's valid — you need at least one execution of the prompt unconditionally. A while loop checks the condition first, but the condition depends on input you haven't gathered yet. The workaround is to prompt before the loop and again inside it, duplicating code. A do-while eliminates this by executing the body (which includes the prompt) first, then checking validity. The first prompt is automatic because the body always runs at least once."
  explanation: "This 'bootstrapping problem' — needing to run the body before you can meaningfully test the condition — is the canonical use case for do-while. The same logic applies to menu-driven programs: the menu must appear at least once before the user can choose to quit. Whenever the first iteration is unconditionally required, do-while is the natural fit."
```

## Explainer

You already know how a `while` loop works: it checks a condition *before* each iteration, and if the condition is false from the start, the body never runs at all. A **do-while loop** flips this order — it executes the body first, then checks the condition. The body always runs at least once, no matter what. In pseudocode the structure looks like: `do { ... } while (condition);` — and that trailing semicolon is important in languages like C and Java, because the statement ends after the condition, not after the closing brace.

The classic use case is **input validation**. Suppose you need to ask the user for a number between 1 and 10. With a `while` loop, you face an awkward bootstrapping problem: the condition depends on the user's input, but you haven't asked for input yet. You end up writing the prompt *before* the loop and then again *inside* the loop — duplicating code. A do-while loop eliminates this duplication naturally: prompt the user inside the body, then check whether the input is valid. If it is not, the loop repeats and prompts again. If it is, the loop exits. The first prompt happens automatically because the body always executes once.

Menu-driven programs follow the same pattern. You display a menu, read the user's choice, and process it. Then you check: did the user choose "quit"? If not, show the menu again. The menu must appear at least once for the user to make any choice at all, which is exactly the guarantee a do-while provides. Whenever you find yourself thinking "I need to do this thing, then maybe do it again depending on the result," a do-while loop is probably the cleanest fit. If the condition could reasonably be false before the first iteration — meaning zero iterations is a valid outcome — stick with a regular `while` loop instead.
