---
id: arrays-lists-and-collections
title: Arrays, Lists, and Collections
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arrays-and-lists
  type: hard
builds-toward:
- accessing-and-modifying-elements
- iterating-over-collections
tags:
- data-structures
- arrays
- lists
stage: abstract-reasoning
status: draft
---

# Arrays, Lists, and Collections

## Core Idea
Arrays and lists store multiple values in sequence. Arrays have fixed size; lists are dynamic. Both are indexed starting at 0. Understanding collections is essential for processing multiple related values efficiently.

## How It's Best Learned
Create arrays/lists of different sizes; practice indexing (including negative indices if supported); use built-in methods to add, remove, and query elements.

## Common Misconceptions
That arrays and lists have no difference (they do in many languages); that index 1 is the first element (it's 0); that negative indices are invalid (some languages support them as from-the-end indexing).

## Explainer

Once you can store a single value in a variable, the next question is: what if you need to store many related values? You could create separate variables — `score1`, `score2`, `score3` — but this becomes unmanageable when you have hundreds of values or when you do not know the count in advance. **Collections** solve this problem by letting you store multiple values under a single name and access each one by its position.

An **array** is the simplest collection: a fixed-size sequence of elements stored in contiguous memory. When you create an array of size 5, the computer reserves five adjacent slots, and you access each one using an **index** — a number indicating its position. Critically, indexing starts at 0, not 1. The first element is at index 0, the second at index 1, and the last element of a size-5 array is at index 4. This zero-based convention confuses many beginners, but it has a logical basis: the index represents the *offset* from the start of the array. The first element is zero steps from the beginning, so its index is 0.

A **list** (sometimes called a dynamic array or ArrayList) works similarly but removes the fixed-size constraint. When you add an element beyond the current capacity, the list automatically allocates more space. This makes lists more flexible for situations where you don't know how many elements you'll need — reading lines from a file, collecting user inputs, or building results during a computation. The tradeoff is that lists carry a small overhead for managing their size, while arrays, because they never resize, can be slightly more efficient when the size is known in advance.

Both arrays and lists support the same core operations: accessing an element by index (`scores[3]`), modifying an element by index (`scores[3] = 95`), and determining how many elements the collection contains (its **length** or **size**). Lists additionally support operations like **append** (add to the end), **insert** (add at a specific position), and **remove** (delete an element). These operations are the foundation for nearly all data processing — once you can store values in a collection and retrieve them by position, you can sort them, search through them, filter them, and transform them. Almost every nontrivial program you write will use arrays or lists as its primary way of organizing data.
