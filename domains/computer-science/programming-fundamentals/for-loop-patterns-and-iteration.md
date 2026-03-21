---
id: for-loop-patterns-and-iteration
title: For-Loop Patterns and Iteration
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loops
  type: hard
- id: variables-and-assignment
  type: hard
builds-toward:
- loop-design-and-invariants
- nested-loops-and-deep-iteration
tags:
- loops
- iteration
- control-flow
stage: formal-systems
status: draft
---

# For-Loop Patterns and Iteration

## Core Idea
For loops iterate a fixed number of times, controlled by an index variable that changes each iteration. Common patterns: counting up (i = 0 to n), counting down, iterating over collections. Understanding the loop variable and termination condition is key.

## How It's Best Learned
Trace loop execution by hand, tracking the index variable each iteration; experiment with off-by-one errors (start at 0 vs 1, iterate while i < n vs i <= n).

## Common Misconceptions
That the loop variable persists after the loop (scope varies by language); that the loop index must be an integer; that i = i + 1 inside the loop conflicts with i++ in the loop header.

## Questions

```yaml
- question: "A student writes code to sum a list of numbers. She initializes 'total = 0' inside the loop body instead of before the loop. What bug does this introduce?"
  type: multiple-choice
  options:
    - "An off-by-one error — the loop processes one extra element because of the extra initialization step"
    - "The accumulator resets to 0 on every iteration, discarding all previous work — the final result equals only the last element added to 0"
    - "A termination error — the loop will run infinitely because total never reaches the expected value"
    - "A scope error that causes a compile-time crash in most languages"
  answer: 1
  explanation: "The accumulation pattern requires the accumulator to be initialized *before* the loop so it persists across iterations. If 'total = 0' is inside the loop body, it executes on every iteration, wiping out the running sum. The loop still terminates correctly, but the final result is just 0 + (last element), not the true sum. This is a logic error, not a crash — it fails silently, which makes it especially dangerous."

- question: "You need to scan a list of prices and return the first price above $100, then stop processing. The most appropriate for-loop pattern is:"
  type: multiple-choice
  options:
    - "Accumulation — maintain a running total until the condition is met"
    - "Search with early exit — iterate through elements and break out of the loop as soon as the condition is satisfied"
    - "Counting — count how many prices exceed $100, then use that count to find the first"
    - "Nested iteration — use an outer loop for the list and an inner loop to check the threshold"
  answer: 1
  explanation: "The search pattern is designed for exactly this situation: scan through a collection, check a condition on each element, and stop as soon as you find a match. Breaking early is important for correctness (you want the *first* match, not the last) and for efficiency (no need to process the rest of the list). Accumulation is for building up a result; counting is for tallying occurrences — neither matches the goal here."

- question: "Hand-tracing a loop — writing down the value of each variable at every iteration — is one of the most effective defenses against off-by-one errors."
  type: true-false
  answer: true
  explanation: "Off-by-one errors often show up only at the boundary conditions: the first iteration, the last iteration, and the total count. Hand-tracing makes these boundaries explicit and visible. By writing out the loop variable and accumulators for a small input (say, n=3 or n=4), you can immediately see whether the loop starts at the right index, ends at the right index, and runs the correct number of times."

- question: "The loop variable in a for loop must always be an integer."
  type: true-false
  answer: false
  explanation: "The loop variable takes on whatever values the iteration provides. In Python, 'for char in my_string' gives a string character each iteration; 'for item in my_list' gives whatever type the list contains. Even in C-style languages, while integer indices are most common, the variable itself is not restricted to integers by any fundamental rule — floats, characters, and objects can all serve as loop variables depending on the context and language."

- question: "Describe the accumulation pattern for a for loop: what must be set up before the loop, what happens inside the loop body, and where is the final result?"
  type: short-answer
  answer: "Before the loop, initialize an accumulator variable to a neutral starting value — 0 for sum, 1 for product, an empty string for concatenation, an empty list for collection. Inside the loop body, update the accumulator using each iteration's value (e.g., total += numbers[i]). After the loop finishes, the accumulator holds the final result."
  explanation: "The accumulation pattern generalizes across many problems: summing, multiplying, counting matches, concatenating strings, building lists. The key insight is that the accumulator must survive across iterations, which is why it must be initialized outside the loop. Placing it inside the loop (a common mistake) resets it each time, destroying the accumulated result."
```

## Explainer

You already know how for loops work mechanically — a loop variable is initialized, a condition is checked before each iteration, and the variable is updated after each iteration. Now the question is: what can you *do* with this structure? **For-loop patterns** are the reusable recipes that show up again and again in programming, and recognizing them is the key to writing loops confidently instead of reinventing them each time.

The most basic pattern is **counting**, where you iterate from a start value to an end value. `for i in range(5)` in Python or `for (int i = 0; i < 5; i++)` in C/Java counts from 0 to 4. This pattern shows up whenever you need to do something a known number of times — print 10 stars, process 100 records, repeat an experiment 1000 times. A variant is **counting down**: `for i in range(10, 0, -1)` counts from 10 to 1. Counting down is useful for countdowns, reverse traversal, or any situation where you need to work backward through a sequence.

The **accumulation** pattern uses a loop to build up a result across iterations. You initialize a variable before the loop (like `total = 0` or `result = ""`), then update it inside the loop body (`total += numbers[i]` or `result += char`). Summation, product, counting matches, and string building all follow this template. The closely related **search** pattern scans through data looking for a specific condition: iterate through elements, and when you find what you are looking for, record it and (often) break out of the loop early.

The **collection iteration** pattern walks through every element of a list, array, or other data structure. In Python, `for item in my_list` directly gives you each element; in C-style languages, you use an index: `for (int i = 0; i < length; i++)` and access `array[i]`. A critical detail in all for-loop patterns is the **off-by-one error** — starting at 1 when you should start at 0, or using `<=` when you should use `<`. The best defense is to trace your loop by hand for small inputs: write down the value of the loop variable and any accumulators at each iteration, and verify that the first iteration, last iteration, and total count are all correct. This hand-tracing habit will save you more debugging time than any other single practice.
