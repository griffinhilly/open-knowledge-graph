---
id: programming-fundamentals-loop-patterns
title: Common Loop Patterns
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-for-loops
  type: hard
builds-toward:
- programming-fundamentals-iteration-collections
tags:
- loops
- patterns
- algorithms
stage: abstract-reasoning
status: draft
---

# Common Loop Patterns

## Core Idea
Common loop patterns solve recurring problems: accumulating sums, searching for elements, filtering values, and transforming data. Recognizing these patterns makes code cleaner and less error-prone.

## Questions

```yaml
- question: "A student writes the following code to sum a list of numbers:\n\n    for item in numbers:\n        total = 0\n        total += item\n    print(total)\n\nWhat is wrong with this code?"
  type: multiple-choice
  options:
    - "'total += item' should be 'total = item' to assign rather than accumulate"
    - "'total' is re-initialized to 0 inside the loop, so it resets on every iteration instead of accumulating across iterations"
    - "The 'print' statement should be inside the loop to show intermediate totals"
    - "'total' should be initialized to 1, not 0, to avoid losing the first value"
  answer: 1
  explanation: "The accumulator pattern requires three steps in order: initialize BEFORE the loop, update INSIDE the loop, use AFTER the loop. Placing 'total = 0' inside the loop means it resets to zero at the start of every iteration — the previous sum is discarded. After the loop completes, 'total' holds only the last item, not their sum. Moving 'total = 0' to before the loop fixes the problem."

- question: "A programmer writes: result = [x * 2 for x in numbers if x > 0]. Which pair of loop patterns does this implement?"
  type: multiple-choice
  options:
    - "Accumulator followed by search"
    - "Search followed by sentinel"
    - "Filter (keep only positive values) followed by transform (double each kept value)"
    - "Transform followed by accumulator"
  answer: 2
  explanation: "The 'if x > 0' condition is a filter: it excludes elements that don't pass the test. The 'x * 2' operation is a transform: it changes each remaining element. These two patterns commonly appear together — filter first to select relevant data, then transform what remains. Recognizing this structure lets you understand the code's intent at a glance without tracing every step."

- question: "In the accumulator pattern, the accumulator variable should be initialized inside the loop so it starts fresh for each element."
  type: true-false
  answer: false
  explanation: "Initializing inside the loop is the most common accumulator bug. Each iteration resets the variable, destroying all previously accumulated work. The accumulator must be initialized BEFORE the loop so that it persists across iterations and each update builds on previous ones. After the loop, the final accumulated value is ready to use."

- question: "Recognizing that a loop follows the filter pattern — a result list initialized before the loop, with elements appended conditionally inside — lets a programmer understand the loop's purpose without reading every line."
  type: true-false
  answer: true
  explanation: "This is the practical value of pattern recognition: structural cues (result = [] before the loop, result.append(item) inside, with a condition) immediately signal 'this is a filter.' Experienced programmers process these patterns as units, reducing cognitive load. The same cue system applies to accumulators (running variable + update), searches (early return or flag), and transforms (every element changed). Patterns are a shared vocabulary for reading and writing code efficiently."

- question: "What are the three structural steps of the accumulator pattern, and why must they occur in that specific order?"
  type: short-answer
  answer: "1) Initialize the accumulator before the loop (e.g., total = 0). 2) Update it inside the loop on each iteration (e.g., total += item). 3) Use the result after the loop ends. The order is necessary: the variable must exist before the loop starts, each iteration's contribution must build on previous ones (not overwrite them), and the fully accumulated value is only available once all iterations have completed."
  explanation: "Each step's position is load-bearing. Initialization before the loop creates the variable and sets a neutral starting value. Updating inside the loop ensures every element contributes. Reading the result after the loop ensures you see the complete accumulated value, not a partial one. Violating any of these three positions breaks the pattern: initializing inside resets the accumulator; reading inside gives intermediate values; updating before or after the loop means elements never contribute."
```

## Explainer

Now that you can write a `for` loop that iterates a known number of times, the next step is recognizing that most loops you write will fall into a handful of recurring shapes. Rather than reinventing the logic each time, experienced programmers identify the **pattern** first and then fill in the details. Learning these patterns is like learning chord progressions in music — once you recognize the structure, you can apply it to any content.

The **accumulator pattern** is the most common. You initialize a variable before the loop (often to zero or an empty collection), then update it on each iteration. Summing a list of numbers is the classic example: start with `total = 0`, then `total += item` for each element. But accumulation is not limited to addition — you can accumulate a running product, build up a string by concatenation, or collect items into a new list. The key is the structure: initialize, iterate, update, and use the result after the loop ends.

The **search pattern** scans through data looking for something specific. You iterate through elements, check a condition, and either return the found item or set a flag. A linear search for the first negative number, for instance, checks each element and breaks out of the loop when it finds one. A variation is the **sentinel pattern**, where you track whether any element (or every element) satisfies a condition using a boolean flag initialized before the loop. For "does any element exceed 100?", set `found = false`, then flip it to `true` when you find one.

The **filter pattern** builds a new collection containing only elements that pass a test. You iterate through the original data, apply a condition to each element, and append those that pass to a result list. The **transform (map) pattern** is similar but keeps every element while changing each one — for example, converting every string in a list to uppercase, or squaring every number. These two patterns often appear together: filter the data, then transform what remains.

Recognizing these patterns matters because it reduces cognitive load. When you see a loop with `result = []` before it and `result.append(...)` inside it, you immediately know it is a filter or transform without reading every line. As you progress to iterating over collections and eventually to higher-order functions like `map`, `filter`, and `reduce`, you will see that these patterns are so fundamental that most languages provide built-in abstractions for them. But understanding the loop-level mechanics first ensures you know what those abstractions are actually doing.
