---
id: arrays-and-lists
title: Arrays and Lists
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
- id: for-loops
  type: hard
- id: primitive-data-types
  type: soft
builds-toward:
- list-operations
- nested-loops
- list-comprehensions
tags:
- arrays
- lists
- sequences
- indexing
- mutable collections
stage: formal-systems
status: validated
---

# Arrays and Lists

## Core Idea
A list (or array) is an ordered, indexed collection of values that can be traversed, modified, and grown or shrunk. Elements are accessed by zero-based index; negative indices count from the end. Unlike strings, lists are mutable — elements can be added, removed, or changed in place. Lists are the foundational data structure for representing sequences of related items and are traversed naturally with for loops.

## How It's Best Learned
Build, modify, and traverse lists by hand and in code. Implement accumulation patterns: start with an empty list, append items inside a loop, then process the result. Compare list access patterns to string slicing.

## Common Misconceptions
- Forgetting that list assignment (b = a) does not copy the list — both names point to the same object.
- Modifying a list while iterating over it.
- Assuming lists must hold a single type in dynamically typed languages.

## Questions

```yaml
- question: "Given a = [10, 20, 30, 40], what is the value of a[-2]?"
  type: multiple-choice
  options:
    - "10"
    - "20"
    - "30"
    - "40"
  answer: 2
  explanation: "Negative indices count backward from the end of the list. Index -1 is the last element (40), -2 is second-to-last (30), -3 is 20, and -4 is 10. Negative indexing is a convenience that avoids having to write a[len(a)-2]; it does not create a separate reversed copy of the list."

- question: "After executing b = a (where a is the list [1, 2, 3]), the statement b[0] = 99 will also change a[0] to 99."
  type: true-false
  answer: true
  explanation: "List assignment does not copy the list — it creates a second name that refers to the same object in memory. Both a and b point to the same list, so any mutation through b is visible through a. To get an independent copy, use b = a[:] or b = list(a). This is one of the most common sources of subtle bugs for new programmers coming from a background where assignment always copies the value."

- question: "Describe the accumulation pattern for building a list of the squares of the integers 1 through 5 using a for loop."
  type: short-answer
  answer: "Initialize an empty list before the loop (e.g., squares = []). Inside a for loop over range(1, 6), append i**2 to the list each iteration. After the loop, squares holds [1, 4, 9, 16, 25]."
  explanation: "The accumulation pattern separates creation from computation: start with an empty container, iterate over inputs, and collect results one at a time. It is the foundational pattern for transforming sequences and appears in list comprehensions, map operations, and reduce operations — all of which are built on this same idea."
```

## Explainer

You already know how to store a single value in a variable and how to repeat operations with a for loop. A list is the natural next step: instead of creating five separate variables (`score1`, `score2`, ...), you create one variable that holds an ordered sequence of values. This makes it possible to process collections of unknown or variable size using the same loop code.

Every element in a list has a position called its index, and indexing starts at zero. The first element is at index 0, the second at index 1, and so on. Python (and most languages) also support negative indices that count from the end: index -1 is the last element, -2 is second-to-last. This gives you two symmetric ways to address any position, which is handy when you care about the end of a list but do not know its length in advance.

Lists are *mutable*, which distinguishes them from strings. You can change any element in place (`a[0] = 99`), append new elements (`a.append(5)`), or remove elements — all without creating a new list. This mutability is powerful, but it introduces a subtlety that surprises nearly every new programmer: when you write `b = a`, you are *not* copying the list. You are giving a second name to the same list object. Changes made through `b` are immediately visible through `a`. To get a true independent copy, use `b = a[:]` or `b = list(a)`.

The most important pattern to learn is accumulation: start with an empty list, run a loop, and append each computed value inside the loop. This pattern is how you transform one collection into another — compute the squares of a range, filter out even numbers, or extract every other element. Once you are comfortable writing this as an explicit loop, you will recognize the same structure inside list comprehensions, `map()`, and other higher-level tools.

Finally, unlike arrays in statically typed languages such as Java or C, Python lists can hold values of different types in the same list — integers, strings, and even other lists can coexist. In practice, mixing types in a single list often indicates a design problem, but the language will not stop you. When you do want the performance and type guarantees of a homogeneous fixed-type array, Python's `numpy` arrays are the right tool for that job.


