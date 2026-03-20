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
stage: formal-systems
status: draft
---

# Accessing and Modifying Array Elements

## Core Idea
Elements are accessed by index using bracket notation. Assignment to an index modifies that element. Out-of-bounds access is an error. Understanding indexing is necessary for working with any collection.

## How It's Best Learned
Practice accessing elements with different indices; deliberately access out-of-bounds to see the error; modify elements and verify changes persist.

## Common Misconceptions
That accessing an element changes it (it doesn't without assignment); that negative indices are always invalid (Python and others support them); that modifying an element in a loop affects the iteration (depends on the loop and collection).

## Explainer

You already know that arrays and lists store multiple values in a single named container. Accessing and modifying elements is how you actually *use* that container — reading individual items out and changing them in place. The fundamental mechanism is **indexing**: you specify which position you want using a number inside square brackets, and the language gives you the value stored there.

In most languages, indices start at **zero**, not one. If you have a list `colors = ["red", "green", "blue"]`, then `colors[0]` is `"red"`, `colors[1]` is `"green"`, and `colors[2]` is `"blue"`. The last valid index is always the length of the collection minus one. Accessing `colors[3]` would be an **index out of bounds** error because no element exists at that position. This off-by-one boundary is one of the most common sources of bugs in programming, so it is worth building a reflex: if a list has *n* items, valid indices run from 0 to *n* − 1.

**Modification** uses the same bracket syntax on the left side of an assignment. Writing `colors[1] = "yellow"` replaces `"green"` with `"yellow"` — the list is now `["red", "yellow", "blue"]`. This is an important distinction: merely *reading* `colors[1]` does not change the list. Only an explicit assignment through the index mutates the data. Some languages also support **negative indexing** as a convenience — in Python, `colors[-1]` gives you the last element (`"blue"`), `colors[-2]` the second-to-last, and so on. Negative indices count backward from the end, which saves you from writing `colors[len(colors) - 1]` every time you want the last item.

Understanding indexing also prepares you for **slicing**, which extracts a range of elements (like `colors[0:2]` to get the first two items), and for iteration, where a loop variable takes on each index or element in turn. Every operation on a collection — searching, sorting, filtering, transforming — ultimately reduces to accessing elements by position, comparing or computing with their values, and sometimes modifying them in place. Getting comfortable with zero-based indexing and the read-versus-write distinction is the gateway to all of that.
