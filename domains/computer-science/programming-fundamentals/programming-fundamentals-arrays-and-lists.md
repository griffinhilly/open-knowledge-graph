---
id: programming-fundamentals-arrays-and-lists
title: Arrays and Lists
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-variables-assignment
  type: hard
builds-toward:
- programming-fundamentals-array-indexing
- programming-fundamentals-iteration-collections
tags:
- collections
- arrays
- lists
stage: abstract-reasoning
status: draft
---

# Arrays and Lists

## Core Idea
Arrays and lists are collections that store multiple values of the same type. Arrays have fixed size; lists grow or shrink dynamically. Both are accessed by index (position), starting at 0.

## Explainer

Once you know how to store a single value in a variable, the next question is natural: what if you need to store many related values? Imagine tracking the scores of 30 students. You could create thirty separate variables — `score1`, `score2`, `score3` — but that approach collapses under its own weight. You cannot loop over scattered variables, you cannot easily count them, and adding a 31st means editing code everywhere. **Arrays** and **lists** solve this by storing multiple values in a single, ordered collection that you access by position.

An **array** is a fixed-size block of memory where each slot holds one value. When you declare an array of size 5, the computer reserves exactly five contiguous slots. This fixed size is both a strength and a limitation: accessing any element is fast because the computer can calculate its exact memory location, but you must know the size in advance and cannot easily grow the array later. A **list** (sometimes called a dynamic array or ArrayList) removes the size constraint — it grows and shrinks as you add or remove elements. Under the hood, lists typically use an array that gets replaced with a larger one when it fills up, but this resizing is handled automatically.

Both arrays and lists use **zero-based indexing**, meaning the first element sits at position 0, the second at position 1, and so on. This convention comes from how memory addressing works: the index represents the offset from the start of the collection. If the collection starts at memory address 1000 and each element takes 4 bytes, element 0 is at 1000, element 1 is at 1004, element 2 is at 1008. The zero-based convention will feel strange at first, but it becomes second nature quickly — just remember that "first" means index 0, and an array of size *n* has valid indices from 0 to *n* − 1. Trying to access index *n* or beyond is an **index-out-of-bounds error**, one of the most common bugs beginners encounter.

The real power of arrays and lists emerges when you combine them with loops. Instead of writing thirty separate print statements, you can write one loop that visits each element in turn. This combination — a collection of data plus iteration over that collection — is one of the most fundamental patterns in all of programming, and it is exactly where your learning path heads next.
