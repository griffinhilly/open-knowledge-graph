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
stage: abstract-reasoning
status: draft
---

# Iterating Over Collections

## Core Idea
Looping through a collection processes each element. Index-based loops are traditional; many languages provide for-each/enhanced-for loops that iterate directly over elements. Choosing the right loop style improves clarity.

## How It's Best Learned
Write loops using both index-based and for-each styles; count total iterations to verify loops process all elements; test with empty collections.

## Common Misconceptions
That all loops work the same way (index-based, for-each, while each have tradeoffs); that modifying a collection while iterating is safe (it can cause elements to be skipped or revisited); that loop variables after iteration have a defined value (it varies).
