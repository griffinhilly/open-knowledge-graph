---
id: iterating-over-collections
title: Iterating Over Collections
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: for-loop-patterns-and-iteration
  type: hard
- id: accessing-and-modifying-elements
  type: hard
builds-toward:
- immutability-and-mutation
- nested-loops-and-deep-iteration
tags:
- loops
- iteration
- collections
stage: formal-systems
status: draft
---

# Iterating Over Collections

## Core Idea
Looping through a collection processes each element. Index-based loops are traditional; many languages provide for-each/enhanced-for loops that iterate directly over elements. Choosing the right loop style improves clarity.

## How It's Best Learned
Write loops using both index-based and for-each styles; count total iterations to verify loops process all elements; test with empty collections.

## Common Misconceptions
That all loops work the same way (index-based, for-each, while each have tradeoffs); that modifying a collection while iterating is safe (it can cause elements to be skipped or revisited); that loop variables after iteration have a defined value (it varies).

## Questions

```yaml
- question: "You have a list [1, 2, 3, 4, 5] and write a loop to remove all even numbers by calling remove() on each even element directly during the iteration. What is the most likely outcome?"
  type: multiple-choice
  options:
    - "All even numbers are correctly removed, leaving [1, 3, 5]"
    - "The loop crashes immediately with an index error on the first removal"
    - "Some even numbers are silently skipped, producing incorrect output"
    - "The list is unchanged because remove() is not allowed inside loops"
  answer: 2
  explanation: "When you remove an element at index i, all subsequent elements shift left by one. The loop then advances to index i+1, which now points to what was previously at i+2 — silently skipping the element that just moved into position i. In this case, removing 2 (index 1) shifts 3 into index 1, but the loop advances to index 2 (now 4), skipping 3. The safe alternatives are: build a new list with desired elements, collect indices after the loop, or iterate in reverse."

- question: "You need to process every element in a list and also need to know the index of each element. Which approach is most idiomatic in Python?"
  type: multiple-choice
  options:
    - "A while loop with a manually managed counter variable"
    - "A plain for-each loop (for item in items) and track the index separately"
    - "enumerate() to get both index and value in each iteration"
    - "An index-based loop using range(len(items)) and items[i]"
  answer: 2
  explanation: "enumerate() is the idiomatic Python solution: 'for i, item in enumerate(items)' gives both the index and value cleanly. An index-based range(len(items)) loop works but is more verbose and reintroduces off-by-one risk. A while loop with a manual counter is even more error-prone. The plain for-each loop alone cannot provide the index without a workaround."

- question: "A for-each loop (e.g., 'for item in items') eliminates off-by-one errors because you never manage an index variable manually."
  type: true-false
  answer: true
  explanation: "Off-by-one errors — starting at 1 instead of 0, writing i <= len(items) instead of i < len(items) — arise specifically from manually managing the index variable. For-each loops hand control of iteration to the language runtime, so you cannot accidentally misconfigure the bounds. The tradeoff is that you lose direct index access and the ability to skip, reverse, or access neighboring elements."

- question: "It is safe to remove elements from a list while iterating over it with an index-based for loop, because the index variable always tracks your current position correctly."
  type: true-false
  answer: false
  explanation: "The index variable correctly tracks your position in the current array — but the current array changes when you remove an element. Removing the element at index i shifts all subsequent elements left by one. When the loop increments to i+1, it now points to what was previously at i+2, silently skipping one element. The index is correct relative to the modified array, but the modified array is no longer the same structure the loop was initialized against."

- question: "Why is it dangerous to modify a collection while iterating over it, and what is the standard safe alternative?"
  type: short-answer
  answer: "When elements are removed during iteration, subsequent elements shift in memory, causing the iterator to skip positions. When elements are added, the loop may visit them unexpectedly or run indefinitely. The collection's structure changes beneath an iterator that assumed it was stable. Safe alternatives are: (1) build a new collection with the desired elements using a comprehension or filter, (2) collect elements or indices to modify and apply changes after the loop completes, or (3) iterate in reverse for removal, so shifts don't affect unvisited (earlier) positions."
  explanation: "This applies to both index-based and for-each loops, though the failure modes differ. For-each loops in many languages (Java) raise an explicit ConcurrentModificationException, making the bug visible. Index-based loops silently skip elements, making the bug harder to detect. The silent failure mode of index loops is arguably more dangerous because it produces wrong output with no error."
```

## Explainer

You already know how to write for loops that count through a range of numbers, and you know how to access individual elements in a collection by index. **Iterating over a collection** combines these skills: instead of manually accessing `items[0]`, then `items[1]`, then `items[2]`, you use a loop to process every element automatically. This is one of the most common patterns in all of programming — nearly every program that works with data needs to examine, transform, or filter a collection of items.

The **index-based** approach uses a counting loop to step through positions: `for i in range(len(items))` in Python, or `for (int i = 0; i < items.length; i++)` in Java/C. Inside the loop, you access each element as `items[i]`. This gives you full control — you know exactly which position you are at, you can skip elements, go backwards, or access neighboring elements like `items[i-1]`. But it is also verbose and error-prone: off-by-one errors (starting at 1 instead of 0, or using `<=` instead of `<`) are among the most common bugs in programming.

The **for-each** style (also called an enhanced for loop or iterator-based loop) simplifies this: `for item in items` in Python, or `for (String item : items)` in Java. You get each element directly without managing an index variable. The code is shorter, clearer, and eliminates off-by-one errors entirely. The tradeoff is that you lose direct access to the index — you cannot easily say "give me the element two positions ahead" or "replace the current element." When you need both the element and its position, many languages offer a compromise like Python's `enumerate()`: `for i, item in enumerate(items)` gives you both.

One critical rule: **do not modify a collection while iterating over it**. If you remove an element from a list mid-loop, the remaining elements shift positions, causing the loop to skip the next element or crash with an error. If you add elements, the loop may process them unexpectedly or run forever. The safe approach is to build a new collection with the desired elements (filtering), or collect indices to modify and apply changes after the loop finishes. This constraint applies to both index-based and for-each loops, though the failure modes differ — index loops silently skip elements while for-each loops in many languages raise an explicit error.
