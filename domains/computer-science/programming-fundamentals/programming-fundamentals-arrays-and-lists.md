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
stage: formal-systems
status: draft
---

# Arrays and Lists

## Core Idea
Arrays and lists are collections that store multiple values of the same type. Arrays have fixed size; lists grow or shrink dynamically. Both are accessed by index (position), starting at 0.

## Questions

```yaml
- question: "You declare an array of size 6. A teammate writes code that accesses index 6 to retrieve the last element. What will happen?"
  type: multiple-choice
  options:
    - "The code correctly retrieves the last element, since a 6-element array goes from index 1 to index 6"
    - "The code causes an index-out-of-bounds error, because valid indices for a 6-element array are 0 through 5"
    - "The code returns 0 or null, since accessing beyond the array silently returns a default value"
    - "The code works in most languages because arrays automatically expand when you access beyond their declared size"
  answer: 1
  explanation: "Zero-based indexing means a 6-element array has valid indices 0, 1, 2, 3, 4, and 5. Index 6 is beyond the last valid slot — it is an index-out-of-bounds error, one of the most common bugs in programming. The first element is at index 0 (the offset from the start is 0), and the last element of a size-n array is always at index n-1. Accessing index n steps outside the array's allocated memory, which either throws a runtime error or — in lower-level languages — reads whatever happens to be in adjacent memory, producing unpredictable results."

- question: "A program needs to process an unknown number of user inputs, adding each one to a collection as it arrives. Which data structure is more appropriate, and why?"
  type: multiple-choice
  options:
    - "An array, because arrays are faster to access and all collections should prefer arrays for performance"
    - "A list, because it can grow dynamically as new inputs arrive without needing to know the size in advance"
    - "An array, because you can declare a very large array to accommodate any possible number of inputs"
    - "Either structure works equally well since both support the same operations"
  answer: 1
  explanation: "A list (dynamic array) is designed for exactly this scenario: it grows as elements are added, handling the resizing automatically. An array requires knowing the size at declaration time — if you don't know how many inputs will arrive, you would have to either guess a maximum (wasting memory if too large, failing if too small) or write manual resizing logic. The key distinction is that arrays have fixed size while lists grow and shrink dynamically. For collections of known, fixed size, arrays are efficient; for collections of unknown or variable size, lists are the right choice."

- question: "In a list containing 10 elements, the last element is stored at index 10."
  type: true-false
  answer: false
  explanation: "Zero-based indexing means the first element is at index 0, the second at index 1, and so on. In a 10-element list, the last element is at index 9 (which is 10 − 1). Thinking of the index as the element's 'number' (1st element = index 1) is the classic beginner mistake. The index actually represents the *offset* from the start of the collection — how many positions to count from the beginning. The first element is zero positions from the start, so its index is 0. Accessing index 10 on a 10-element list is an index-out-of-bounds error."

- question: "The main practical advantage of a dynamic list over a fixed-size array is that a list can grow and shrink automatically as elements are added or removed."
  type: true-false
  answer: true
  explanation: "This is the defining difference. An array requires its size to be declared in advance; once allocated, that fixed block of memory cannot grow. A list removes this constraint — it automatically manages resizing by replacing the underlying array with a larger one when it fills up, but this process is invisible to the programmer. The tradeoff is that occasional resize operations incur a small performance cost, while arrays offer consistently fast random access. For collections of variable or unknown size, the flexibility of dynamic lists is the right tradeoff; for collections of known fixed size, arrays are simpler and slightly more efficient."

- question: "Why does zero-based indexing make sense from a memory-addressing perspective, even though it feels counterintuitive at first?"
  type: short-answer
  answer: "The index represents an offset — the number of positions to count from the start of the collection's memory block. The first element is zero positions away from the start, so its offset (and therefore its index) is 0. If an array starts at memory address 1000 and each element occupies 4 bytes, element 0 is at address 1000 + (0 × 4) = 1000; element 1 is at 1000 + (1 × 4) = 1004; element 5 is at 1000 + (5 × 4) = 1020. This arithmetic is simpler with zero-based offsets than with one-based counting, and it maps directly to how the processor calculates memory addresses."
  explanation: "Zero-based indexing is not a historical accident or arbitrary convention — it is a natural consequence of how memory addressing works at the hardware level. Languages that use one-based indexing (like MATLAB or Lua) add an implicit subtraction under the hood to convert the 1-based index to a 0-based offset. Once you internalize that 'index = distance from start,' the convention becomes completely natural."
```

## Explainer

Once you know how to store a single value in a variable, the next question is natural: what if you need to store many related values? Imagine tracking the scores of 30 students. You could create thirty separate variables — `score1`, `score2`, `score3` — but that approach collapses under its own weight. You cannot loop over scattered variables, you cannot easily count them, and adding a 31st means editing code everywhere. **Arrays** and **lists** solve this by storing multiple values in a single, ordered collection that you access by position.

An **array** is a fixed-size block of memory where each slot holds one value. When you declare an array of size 5, the computer reserves exactly five contiguous slots. This fixed size is both a strength and a limitation: accessing any element is fast because the computer can calculate its exact memory location, but you must know the size in advance and cannot easily grow the array later. A **list** (sometimes called a dynamic array or ArrayList) removes the size constraint — it grows and shrinks as you add or remove elements. Under the hood, lists typically use an array that gets replaced with a larger one when it fills up, but this resizing is handled automatically.

Both arrays and lists use **zero-based indexing**, meaning the first element sits at position 0, the second at position 1, and so on. This convention comes from how memory addressing works: the index represents the offset from the start of the collection. If the collection starts at memory address 1000 and each element takes 4 bytes, element 0 is at 1000, element 1 is at 1004, element 2 is at 1008. The zero-based convention will feel strange at first, but it becomes second nature quickly — just remember that "first" means index 0, and an array of size *n* has valid indices from 0 to *n* − 1. Trying to access index *n* or beyond is an **index-out-of-bounds error**, one of the most common bugs beginners encounter.

The real power of arrays and lists emerges when you combine them with loops. Instead of writing thirty separate print statements, you can write one loop that visits each element in turn. This combination — a collection of data plus iteration over that collection — is one of the most fundamental patterns in all of programming, and it is exactly where your learning path heads next.
