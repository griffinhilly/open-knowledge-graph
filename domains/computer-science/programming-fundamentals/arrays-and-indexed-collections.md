---
id: arrays-and-indexed-collections
title: Arrays and Indexed Collections
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
builds-toward:
- string-text-representation
- arrays-and-lists
tags:
- data-structures
- arrays
- collections
stage: abstract-reasoning
status: draft
---

# Arrays and Indexed Collections

## Core Idea
An array is a contiguous collection of elements of the same type, accessed by a numeric index starting from 0. Arrays provide efficient random access and are fundamental for storing homogeneous data like lists of numbers or grades.

## How It's Best Learned
Create arrays, access elements by index, iterate through arrays with loops, and modify elements.

## Common Misconceptions
- Array indices start at 1 (they start at 0 in most languages).
- Arrays are dynamic and grow automatically (fixed-size arrays cannot grow; some languages provide dynamic arrays separately).

## Explainer

From your understanding of memory and data storage, you know that a computer's memory is a long sequence of numbered locations (addresses), each holding a value. A single variable occupies one location and holds one value. But programs routinely need to work with collections of related values — a list of 30 student grades, the daily temperatures for a year, the pixel colors in an image. You could create 30 separate variables (`grade1`, `grade2`, ... `grade30`), but this is unmanageable and impossible to process with a loop. An **array** solves this by storing multiple values of the same type in a contiguous block of memory, accessible through a single name and a numeric **index**.

The key concept is **indexed access**: if you have an array called `scores` with 5 elements, then `scores[0]` is the first element, `scores[1]` is the second, and `scores[4]` is the last. Indices start at **0**, not 1 — this is a universal convention in most programming languages (C, Java, Python, JavaScript) rooted in how memory addressing works. Because the array occupies contiguous memory and every element is the same size, the computer can calculate the exact memory address of any element instantly: `address = base_address + index × element_size`. This makes accessing `scores[0]` exactly as fast as accessing `scores[999]` — a property called **constant-time random access** that distinguishes arrays from many other data structures.

Arrays pair naturally with loops. To compute the average of 100 grades, you write a loop that iterates from index 0 to 99, summing each element — the same three lines of code work whether you have 10 grades or 10,000. This is the practical power of arrays: they turn repetitive data handling into concise, scalable code. To iterate through an array, you typically use a loop variable as the index: `for i in range(len(grades)): total += grades[i]`. Many languages also offer a "for each" syntax that iterates directly over the elements without explicit indexing.

The most important pitfall is the **off-by-one error**, particularly the out-of-bounds access. An array of 5 elements has valid indices 0 through 4 — accessing `scores[5]` is an error because there is no sixth element. Some languages (Java, Python) will throw an exception; others (C, C++) will silently access whatever memory happens to be at that location, causing unpredictable bugs. Always remember: for an array of length *n*, the valid indices are 0 through *n* − 1. Fixed-size arrays have their length determined at creation and cannot grow. If you need a collection that can expand, many languages provide **dynamic arrays** (Python's `list`, Java's `ArrayList`) that automatically resize by allocating a larger block of memory and copying elements over — but the underlying principle of contiguous, indexed storage remains the same.
