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

## Explainer

Now that you can write a `for` loop that iterates a known number of times, the next step is recognizing that most loops you write will fall into a handful of recurring shapes. Rather than reinventing the logic each time, experienced programmers identify the **pattern** first and then fill in the details. Learning these patterns is like learning chord progressions in music — once you recognize the structure, you can apply it to any content.

The **accumulator pattern** is the most common. You initialize a variable before the loop (often to zero or an empty collection), then update it on each iteration. Summing a list of numbers is the classic example: start with `total = 0`, then `total += item` for each element. But accumulation is not limited to addition — you can accumulate a running product, build up a string by concatenation, or collect items into a new list. The key is the structure: initialize, iterate, update, and use the result after the loop ends.

The **search pattern** scans through data looking for something specific. You iterate through elements, check a condition, and either return the found item or set a flag. A linear search for the first negative number, for instance, checks each element and breaks out of the loop when it finds one. A variation is the **sentinel pattern**, where you track whether any element (or every element) satisfies a condition using a boolean flag initialized before the loop. For "does any element exceed 100?", set `found = false`, then flip it to `true` when you find one.

The **filter pattern** builds a new collection containing only elements that pass a test. You iterate through the original data, apply a condition to each element, and append those that pass to a result list. The **transform (map) pattern** is similar but keeps every element while changing each one — for example, converting every string in a list to uppercase, or squaring every number. These two patterns often appear together: filter the data, then transform what remains.

Recognizing these patterns matters because it reduces cognitive load. When you see a loop with `result = []` before it and `result.append(...)` inside it, you immediately know it is a filter or transform without reading every line. As you progress to iterating over collections and eventually to higher-order functions like `map`, `filter`, and `reduce`, you will see that these patterns are so fundamental that most languages provide built-in abstractions for them. But understanding the loop-level mechanics first ensures you know what those abstractions are actually doing.
