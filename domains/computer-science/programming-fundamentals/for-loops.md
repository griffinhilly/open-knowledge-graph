---
id: for-loops
title: For Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: while-loops
  type: hard
builds-toward:
- loop-control-statements
- arrays-and-lists
- nested-loops
- list-comprehensions
tags:
- for
- iteration
- range
- traversal
- sequences
stage: abstract-reasoning
status: validated
---

# For Loops

## Core Idea
A for loop iterates over a sequence (a range of numbers, a list, a string, etc.), executing the loop body once for each element. In most modern languages, for-each style loops bind the loop variable to each element in turn, making traversal cleaner than equivalent while loops. Range-based iteration (e.g., range(n)) generates a sequence of integers, enabling counted repetition. For loops are preferred when the number of iterations or the sequence to traverse is known ahead of time.

## How It's Best Learned
Convert while loops to for loops and vice versa to understand their equivalence. Iterate over strings, lists, and ranges. Count elements, accumulate sums, and search for values.

## Common Misconceptions
- Modifying a list while iterating over it with a for loop, causing skipped or repeated elements.
- Confusing the loop variable (element) with the index.
- Assuming range(n) includes n (it stops at n-1).

## Explainer

You already know how while loops work: set up a condition, repeat the body as long as the condition is true, and make sure something inside the body eventually makes the condition false. A **for loop** packages this pattern more concisely for the most common case — iterating over a known sequence of items. Instead of initializing a counter, checking a condition, and incrementing manually, a for loop handles all three in a single line. In Python, `for item in [10, 20, 30]:` binds `item` to `10`, runs the body, then binds `item` to `20`, runs the body again, and finally binds `item` to `30`. No counter to manage, no off-by-one risk from a wrong condition, no forgotten increment.

The most common way to generate a sequence of numbers is with **range()**. `range(5)` produces the integers 0, 1, 2, 3, 4 — five values starting at 0 and stopping *before* 5. This half-open convention (`start <= value < stop`) is ubiquitous in programming because it makes the count of iterations equal to `stop - start`. You can also specify a start and step: `range(2, 10, 3)` produces 2, 5, 8. To repeat an action exactly *n* times without caring about the value, the pattern `for _ in range(n):` is idiomatic — the underscore signals that the loop variable is unused.

For loops truly shine when you iterate over **collections** — lists, strings, dictionaries, files. `for char in "hello":` visits each character. `for line in open("data.txt"):` visits each line. This is cleaner than the equivalent while loop because there is no index to manage and no risk of going past the end. When you *do* need the index alongside the element, use `enumerate`: `for i, item in enumerate(my_list):` gives you both. This avoids the common mistake of using `range(len(my_list))` and then indexing with `my_list[i]`, which is more error-prone and harder to read.

One important pitfall to understand early: **never modify a collection while iterating over it with a for loop**. If you remove an element from a list during iteration, the loop's internal counter shifts, causing it to skip the next element or produce surprising results. If you need to filter a list, build a new list with the elements you want to keep, or iterate over a copy. This is one of the few cases where a while loop with manual index management may actually be clearer, because you have explicit control over when the index advances.
