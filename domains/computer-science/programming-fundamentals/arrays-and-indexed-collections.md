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
stage: formal-systems
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

## Questions

```yaml
- question: "An array called `scores` contains 7 elements. A student writes `scores[7]` to access the last element. What is wrong with this?"
  type: multiple-choice
  options:
    - "Nothing — array indices start at 1, so index 7 is the last element"
    - "The index should be 7.0, not 7, because arrays use floating-point indices"
    - "Arrays of odd length require a different access syntax"
    - "Array indices start at 0, so valid indices are 0–6; index 7 is out of bounds"
  answer: 3
  explanation: "Array indices start at 0 in virtually all programming languages. An array of length n has valid indices 0 through n−1. For a 7-element array, valid indices are 0–6. Accessing index 7 is an off-by-one error — the classic array pitfall. Some languages (Java, Python) throw an exception; others (C, C++) silently access adjacent memory, causing unpredictable bugs."

- question: "Why can a program access `grades[0]` and `grades[999]` in an array of 1000 elements equally fast?"
  type: multiple-choice
  options:
    - "The computer searches from the beginning until it finds the correct index"
    - "Arrays are pre-sorted so binary search can find any element quickly"
    - "The computer calculates the exact memory address directly using: base_address + index × element_size"
    - "The operating system caches the most recently accessed array elements"
  answer: 2
  explanation: "Because an array stores elements in a contiguous block of memory where every element is the same size, the computer can compute any element's address in a single arithmetic step: base_address + index × element_size. This gives O(1) — constant-time — random access regardless of array size or which index is requested. This is a defining property of arrays that distinguishes them from linked lists."

- question: "A fixed-size array declared with 10 elements automatically expands to hold an 11th element if needed."
  type: true-false
  answer: false
  explanation: "Fixed-size arrays have their length determined at creation and cannot grow. If you need to store more elements, you must declare a larger array and copy the data. Languages like Python (list) and Java (ArrayList) provide dynamic arrays that resize automatically, but they achieve this by allocating a new larger block and copying — the underlying fixed array doesn't expand. Relying on automatic growth when using fixed arrays is a common and dangerous misconception."

- question: "For an array of length n, accessing index n−1 is valid but accessing index n causes an error."
  type: true-false
  answer: true
  explanation: "Because indices start at 0, the last valid index in an array of length n is always n−1. Index n would refer to a position one past the end of the array — a classic off-by-one error. This is one of the most common bugs in programming: a loop running from 0 to n (inclusive) instead of 0 to n−1."

- question: "Why do arrays store elements of the same type, and how does this enable constant-time random access?"
  type: short-answer
  answer: "Arrays store elements of the same type so that every element occupies exactly the same amount of memory. This uniformity lets the computer calculate any element's address instantly using: base_address + index × element_size. If elements had different sizes, the computer would have to scan from the beginning to find where each element starts, making access linear rather than constant-time."
  explanation: "The homogeneous type constraint is not arbitrary — it is the precondition for the arithmetic that makes O(1) access possible. A char array has 1-byte elements; an int array has 4-byte elements. Either way, the stride is fixed, and the formula works. This is why arrays are the most efficient data structure for random access: there is no searching, just arithmetic."
```

## Explainer

From your understanding of memory and data storage, you know that a computer's memory is a long sequence of numbered locations (addresses), each holding a value. A single variable occupies one location and holds one value. But programs routinely need to work with collections of related values — a list of 30 student grades, the daily temperatures for a year, the pixel colors in an image. You could create 30 separate variables (`grade1`, `grade2`, ... `grade30`), but this is unmanageable and impossible to process with a loop. An **array** solves this by storing multiple values of the same type in a contiguous block of memory, accessible through a single name and a numeric **index**.

The key concept is **indexed access**: if you have an array called `scores` with 5 elements, then `scores[0]` is the first element, `scores[1]` is the second, and `scores[4]` is the last. Indices start at **0**, not 1 — this is a universal convention in most programming languages (C, Java, Python, JavaScript) rooted in how memory addressing works. Because the array occupies contiguous memory and every element is the same size, the computer can calculate the exact memory address of any element instantly: `address = base_address + index × element_size`. This makes accessing `scores[0]` exactly as fast as accessing `scores[999]` — a property called **constant-time random access** that distinguishes arrays from many other data structures.

Arrays pair naturally with loops. To compute the average of 100 grades, you write a loop that iterates from index 0 to 99, summing each element — the same three lines of code work whether you have 10 grades or 10,000. This is the practical power of arrays: they turn repetitive data handling into concise, scalable code. To iterate through an array, you typically use a loop variable as the index: `for i in range(len(grades)): total += grades[i]`. Many languages also offer a "for each" syntax that iterates directly over the elements without explicit indexing.

The most important pitfall is the **off-by-one error**, particularly the out-of-bounds access. An array of 5 elements has valid indices 0 through 4 — accessing `scores[5]` is an error because there is no sixth element. Some languages (Java, Python) will throw an exception; others (C, C++) will silently access whatever memory happens to be at that location, causing unpredictable bugs. Always remember: for an array of length *n*, the valid indices are 0 through *n* − 1. Fixed-size arrays have their length determined at creation and cannot grow. If you need a collection that can expand, many languages provide **dynamic arrays** (Python's `list`, Java's `ArrayList`) that automatically resize by allocating a larger block of memory and copying elements over — but the underlying principle of contiguous, indexed storage remains the same.
