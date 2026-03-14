---
id: accessing-and-modifying-elements
title: Accessing and Modifying Array Elements
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arrays-lists-and-collections
  type: hard
builds-toward:
- iterating-over-collections
- immutability-and-mutation
tags:
- arrays
- indexing
- mutation
stage: abstract-reasoning
status: draft
---

# Accessing and Modifying Array Elements

## Core Idea
Elements are accessed by index using bracket notation. Assignment to an index modifies that element. Out-of-bounds access is an error. Understanding indexing is necessary for working with any collection.

## How It's Best Learned
Practice accessing elements with different indices; deliberately access out-of-bounds to see the error; modify elements and verify changes persist.

## Common Misconceptions
That accessing an element changes it (it doesn't without assignment); that negative indices are always invalid (Python and others support them); that modifying an element in a loop affects the iteration (depends on the loop and collection).
