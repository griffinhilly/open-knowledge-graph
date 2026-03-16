---
id: programming-fundamentals-array-indexing
title: Array Indexing and Bounds
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-arrays-and-lists
  type: hard
builds-toward:
- programming-fundamentals-iteration-collections
tags:
- arrays
- indexing
- bounds
stage: abstract-reasoning
status: draft
---

# Array Indexing and Bounds

## Core Idea
Indexing accesses array elements by position using bracket notation (e.g., arr[0]). Valid indices range from 0 to length-1. Accessing an out-of-bounds index causes an error.

## Explainer

Now that you understand arrays as ordered collections of elements, the next question is: how do you get at a specific element? The answer is **indexing** — using a number inside bracket notation to specify which position you want. If you have an array `fruits = ["apple", "banana", "cherry"]`, then `fruits[0]` gives you `"apple"`, `fruits[1]` gives you `"banana"`, and `fruits[2]` gives you `"cherry"`. The number inside the brackets is called the **index**.

The critical detail that trips up nearly every beginner is that indexing starts at zero, not one. The first element is at position 0, the second at position 1, and so on. This is called **zero-based indexing**, and it means the last element in an array of length `n` sits at index `n - 1`. Think of the index as an offset from the beginning: the first element is zero steps from the start, the second is one step from the start. Once this clicks, zero-based indexing feels natural.

What happens when you use an index that doesn't exist? If your array has three elements (indices 0, 1, 2) and you try to access `fruits[3]` or `fruits[-1]` (in languages without negative indexing), the program raises an **out-of-bounds error**. The array simply has no element at that position, so there is nothing to return. This is one of the most common runtime errors in programming, and it almost always means your index math is off by one — often because you forgot that the last valid index is `length - 1`, not `length`.

Understanding indexing also unlocks a powerful pattern: you can use a variable as the index. Instead of writing `fruits[0]`, you can write `fruits[i]` where `i` is a variable that changes. This is the foundation of iterating through arrays — stepping through each element by incrementing the index from 0 up to `length - 1`. Getting comfortable with index arithmetic now will make loops over collections feel straightforward when you encounter them next.
