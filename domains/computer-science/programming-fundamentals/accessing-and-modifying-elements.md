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

## Questions

```yaml
- question: "A list contains the elements ['a', 'b', 'c', 'd', 'e']. What is the last valid index, and what expression retrieves the last element?"
  type: multiple-choice
  options:
    - "Index 5; expression: list[5]"
    - "Index 4; expression: list[4]"
    - "Index 5; expression: list[-1]"
    - "Index 4; expression: list[length]"
  answer: 1
  explanation: "With 5 elements and zero-based indexing, valid indices run from 0 to 4 (length − 1). Index 5 would be out of bounds and cause an error. list[4] retrieves the last element ('e'). In Python, list[-1] also retrieves the last element using negative indexing, but the last valid positive index is 4, not 5. Option A is the classic off-by-one mistake: confusing the list's length (5) with the last valid index (4)."

- question: "A student writes the following code: `value = colors[1]`. After this line runs, what has changed?"
  type: multiple-choice
  options:
    - "colors[1] has been updated to hold the value of 'value'"
    - "Nothing in the list has changed — the line only reads colors[1] and stores a copy in 'value'"
    - "Both 'value' and colors[1] now point to the same object, so modifying either changes both"
    - "colors[1] is deleted after being read into 'value'"
  answer: 1
  explanation: "Accessing an element by index is a read operation — it does not modify the list in any way. The line retrieves whatever is at colors[1] and assigns that value to the variable 'value'. The list remains unchanged. Only an assignment through an index — like colors[1] = 'yellow' — modifies the list. This read-versus-write distinction is fundamental: the same bracket notation is used for both, but placing the indexed expression on the LEFT side of an assignment is what triggers modification."

- question: "Accessing an element by index does not modify the collection."
  type: true-false
  answer: true
  explanation: "Index access (e.g., colors[1]) is a pure read operation. It retrieves the value at that position but leaves the collection entirely unchanged. Modification requires an explicit assignment using the index on the left side of an assignment operator: colors[1] = 'yellow'. This distinction is important for reasoning about program behavior — reading data never mutates it."

- question: "In a list with 7 elements, index 7 is valid and returns the last element."
  type: true-false
  answer: false
  explanation: "With zero-based indexing, a list of 7 elements has valid indices 0 through 6. Index 7 is out of bounds and will cause an error (IndexError in Python, ArrayIndexOutOfBoundsException in Java, etc.). The last valid index is always length − 1. This off-by-one pattern — confusing the length with the last valid index — is one of the most common sources of bugs in programming."

- question: "What is the difference between accessing and modifying an array element, and what syntax distinguishes the two operations?"
  type: short-answer
  answer: "Accessing an element reads its value without changing the collection: the indexed expression (e.g., colors[1]) appears on the right side of an assignment or in an expression, and the collection remains unchanged. Modifying an element replaces the stored value: the indexed expression appears on the LEFT side of an assignment (e.g., colors[1] = 'yellow'), which overwrites whatever was stored at that position. Both operations use identical bracket-and-index syntax, but the position relative to the assignment operator determines whether it's a read or a write."
  explanation: "The read-versus-write distinction becomes especially important when working with shared references or loop iterations. Reading a value in a loop does not affect the loop or the collection. Writing to an index during iteration can cause unexpected behavior depending on the language and collection type. Recognizing which operation you're performing is foundational to reasoning about collection-manipulating code."
```

## Explainer

You already know that arrays and lists store multiple values in a single named container. Accessing and modifying elements is how you actually *use* that container — reading individual items out and changing them in place. The fundamental mechanism is **indexing**: you specify which position you want using a number inside square brackets, and the language gives you the value stored there.

In most languages, indices start at **zero**, not one. If you have a list `colors = ["red", "green", "blue"]`, then `colors[0]` is `"red"`, `colors[1]` is `"green"`, and `colors[2]` is `"blue"`. The last valid index is always the length of the collection minus one. Accessing `colors[3]` would be an **index out of bounds** error because no element exists at that position. This off-by-one boundary is one of the most common sources of bugs in programming, so it is worth building a reflex: if a list has *n* items, valid indices run from 0 to *n* − 1.

**Modification** uses the same bracket syntax on the left side of an assignment. Writing `colors[1] = "yellow"` replaces `"green"` with `"yellow"` — the list is now `["red", "yellow", "blue"]`. This is an important distinction: merely *reading* `colors[1]` does not change the list. Only an explicit assignment through the index mutates the data. Some languages also support **negative indexing** as a convenience — in Python, `colors[-1]` gives you the last element (`"blue"`), `colors[-2]` the second-to-last, and so on. Negative indices count backward from the end, which saves you from writing `colors[len(colors) - 1]` every time you want the last item.

Understanding indexing also prepares you for **slicing**, which extracts a range of elements (like `colors[0:2]` to get the first two items), and for iteration, where a loop variable takes on each index or element in turn. Every operation on a collection — searching, sorting, filtering, transforming — ultimately reduces to accessing elements by position, comparing or computing with their values, and sometimes modifying them in place. Getting comfortable with zero-based indexing and the read-versus-write distinction is the gateway to all of that.
