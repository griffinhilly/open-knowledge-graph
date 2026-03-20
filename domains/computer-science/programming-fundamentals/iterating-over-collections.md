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

## Explainer

You already know how to write for loops that count through a range of numbers, and you know how to access individual elements in a collection by index. **Iterating over a collection** combines these skills: instead of manually accessing `items[0]`, then `items[1]`, then `items[2]`, you use a loop to process every element automatically. This is one of the most common patterns in all of programming — nearly every program that works with data needs to examine, transform, or filter a collection of items.

The **index-based** approach uses a counting loop to step through positions: `for i in range(len(items))` in Python, or `for (int i = 0; i < items.length; i++)` in Java/C. Inside the loop, you access each element as `items[i]`. This gives you full control — you know exactly which position you are at, you can skip elements, go backwards, or access neighboring elements like `items[i-1]`. But it is also verbose and error-prone: off-by-one errors (starting at 1 instead of 0, or using `<=` instead of `<`) are among the most common bugs in programming.

The **for-each** style (also called an enhanced for loop or iterator-based loop) simplifies this: `for item in items` in Python, or `for (String item : items)` in Java. You get each element directly without managing an index variable. The code is shorter, clearer, and eliminates off-by-one errors entirely. The tradeoff is that you lose direct access to the index — you cannot easily say "give me the element two positions ahead" or "replace the current element." When you need both the element and its position, many languages offer a compromise like Python's `enumerate()`: `for i, item in enumerate(items)` gives you both.

One critical rule: **do not modify a collection while iterating over it**. If you remove an element from a list mid-loop, the remaining elements shift positions, causing the loop to skip the next element or crash with an error. If you add elements, the loop may process them unexpectedly or run forever. The safe approach is to build a new collection with the desired elements (filtering), or collect indices to modify and apply changes after the loop finishes. This constraint applies to both index-based and for-each loops, though the failure modes differ — index loops silently skip elements while for-each loops in many languages raise an explicit error.
