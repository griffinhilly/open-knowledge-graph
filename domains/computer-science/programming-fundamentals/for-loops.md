---
id: for-loops
title: For Loops
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: while-loops
  type: hard
- id: program-structure
  type: hard
- id: variables-and-assignment
  type: hard
builds-toward:
- loop-control-statements
- arrays-and-lists
- nested-loops
- list-comprehensions
- iterating-over-collections
- loop-design-and-invariants
tags:
- for
- iteration
- range
- traversal
- sequences
stage: formal-systems
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

## Questions

```yaml
- question: "What sequence of integers does range(1, 10, 3) produce?"
  type: multiple-choice
  options:
    - "1, 4, 7, 10"
    - "1, 4, 7"
    - "0, 3, 6, 9"
    - "1, 3, 6, 9"
  answer: 1
  explanation: "range(start, stop, step) generates values starting at 1, incrementing by 3, and stopping before 10. So: 1, 4, 7 — the next value would be 10, which is excluded because range's stop is a half-open bound (start <= value < stop). Option A is the classic off-by-one error: including the stop value as if the bound were closed. Option C applies the step incorrectly and starts at 0. The half-open convention means the count of values equals (stop - start) / step, rounded down."

- question: "A programmer writes: `for item in my_list: if item < 0: my_list.remove(item)`. What problem can this cause?"
  type: multiple-choice
  options:
    - "A syntax error — you cannot call remove() on a list during iteration"
    - "The loop variable 'item' becomes undefined after the first removal"
    - "Elements may be silently skipped — removing an item shifts subsequent elements to earlier positions, causing the loop's internal index to jump past the next element"
    - "The condition item < 0 is only evaluated once, before the loop begins, so only the first negative item is removed"
  answer: 2
  explanation: "When you remove an element from a list mid-iteration, Python's internal index advances normally — but the list has shrunk by one. The element that was immediately after the removed item slides into the removed item's old position, and the loop skips over it. For example, in [-1, -2, 3], removing -1 shifts -2 to index 0; the loop then moves to index 1 (which is 3) and never sees -2. The fix is to iterate over a copy (`my_list[:]`) or build a new filtered list."

- question: "range(5) produces the sequence 1, 2, 3, 4, 5."
  type: true-false
  answer: false
  explanation: "range(5) produces 0, 1, 2, 3, 4 — five integers starting at 0 and stopping before 5. This half-open, zero-indexed convention is consistent throughout Python: range(n) always produces exactly n values. Starting at 1 instead of 0 is a persistent misconception, likely carried over from everyday counting. To get 1 through 5, use range(1, 6)."

- question: "A Python for loop can iterate directly over a string, binding the loop variable to each character in sequence."
  type: true-false
  answer: true
  explanation: "In Python, strings are iterable sequences of characters. Writing `for char in 'hello':` binds char to 'h', then 'e', then 'l', 'l', 'o' — one character per iteration. This is the same mechanism used for lists, tuples, files, and any other iterable. The for loop's power is precisely this generality: it doesn't care what kind of sequence it traverses, only that the object is iterable."

- question: "Describe a situation where a while loop is clearly more appropriate than a for loop, and explain why."
  type: short-answer
  answer: "A while loop is more appropriate when you don't know in advance how many iterations are needed — for example, reading user input until a valid entry is received, or searching for a condition in a data stream of unknown length. For loops are designed for iterating over a known sequence; while loops are designed for 'repeat until this condition is met' logic where the exit condition is determined at runtime."
  explanation: "The for loop abstracts away the counter precisely because traversal over a known sequence is the common case. When the termination condition depends on what happens *during* execution — a user action, a network response, convergence of a computation — a while loop puts that condition front and center, making the logic clearer. Using a for loop in these cases forces awkward workarounds like break statements or flags that obscure the real intent of the code."
```

## Explainer

You already know how while loops work: set up a condition, repeat the body as long as the condition is true, and make sure something inside the body eventually makes the condition false. A **for loop** packages this pattern more concisely for the most common case — iterating over a known sequence of items. Instead of initializing a counter, checking a condition, and incrementing manually, a for loop handles all three in a single line. In Python, `for item in [10, 20, 30]:` binds `item` to `10`, runs the body, then binds `item` to `20`, runs the body again, and finally binds `item` to `30`. No counter to manage, no off-by-one risk from a wrong condition, no forgotten increment.

The most common way to generate a sequence of numbers is with **range()**. `range(5)` produces the integers 0, 1, 2, 3, 4 — five values starting at 0 and stopping *before* 5. This half-open convention (`start <= value < stop`) is ubiquitous in programming because it makes the count of iterations equal to `stop - start`. You can also specify a start and step: `range(2, 10, 3)` produces 2, 5, 8. To repeat an action exactly *n* times without caring about the value, the pattern `for _ in range(n):` is idiomatic — the underscore signals that the loop variable is unused.

For loops truly shine when you iterate over **collections** — lists, strings, dictionaries, files. `for char in "hello":` visits each character. `for line in open("data.txt"):` visits each line. This is cleaner than the equivalent while loop because there is no index to manage and no risk of going past the end. When you *do* need the index alongside the element, use `enumerate`: `for i, item in enumerate(my_list):` gives you both. This avoids the common mistake of using `range(len(my_list))` and then indexing with `my_list[i]`, which is more error-prone and harder to read.

One important pitfall to understand early: **never modify a collection while iterating over it with a for loop**. If you remove an element from a list during iteration, the loop's internal counter shifts, causing it to skip the next element or produce surprising results. If you need to filter a list, build a new list with the elements you want to keep, or iterate over a copy. This is one of the few cases where a while loop with manual index management may actually be clearer, because you have explicit control over when the index advances.
