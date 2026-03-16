---
id: programming-fundamentals-iteration-collections
title: Iterating Over Collections
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-for-loops
  type: hard
- id: programming-fundamentals-array-indexing
  type: hard
tags:
- loops
- collections
- iteration
stage: abstract-reasoning
status: draft
---

# Iterating Over Collections

## Core Idea
Iterating over a collection accesses each element in sequence. Index-based loops use a counter to access elements by index; for-each loops iterate directly over elements. Many languages offer both approaches.

## Explainer

You already know two things that combine here: for loops let you repeat a block of code a controlled number of times, and array indexing lets you access any element by its position. Iterating over a collection is what happens when you bring these together — you use a loop to visit every element in an array (or list, or other collection) one at a time.

The most explicit approach is an **index-based loop**. You set a counter variable to 0, loop while it's less than the collection's length, and use the counter as an index: `for i in range(len(items)): print(items[i])`. This gives you full control — you know exactly which position you're at, you can skip elements, go backwards, or access neighboring elements. But it's also verbose, and off-by-one errors (starting at 1 instead of 0, or using `<=` instead of `<`) are a constant hazard.

Most modern languages offer a cleaner alternative: the **for-each loop** (called `for...in` in Python, `for...of` in JavaScript, or enhanced `for` in Java). Instead of managing an index yourself, you simply say `for item in items: print(item)`. The language handles the indexing internally. The variable `item` takes on each element's value in sequence. This is less error-prone and more readable when you just need to process every element. The tradeoff is that you don't automatically know the index — if you need it, you either switch back to index-based iteration or use a construct like Python's `enumerate()`.

Choosing between these two styles is a judgment call that depends on what you need. If you only need each element's value — to sum numbers, print names, or check a condition — a for-each loop is simpler and less error-prone. If you need the index itself — to modify elements in place, compare adjacent elements, or iterate over two collections in parallel — an index-based loop gives you that control. As you encounter more collection types beyond arrays (dictionaries, sets, linked lists), you'll find that for-each iteration generalizes to all of them, while index-based access does not. This is why for-each is the default idiom in most production code.
