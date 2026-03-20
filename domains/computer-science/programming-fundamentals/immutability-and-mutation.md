---
id: immutability-and-mutation
title: Immutability and Mutation
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: accessing-and-modifying-elements
  type: hard
builds-toward:
- introducing-objects-and-classes
tags:
- mutation
- immutability
- data
stage: formal-systems
status: draft
---

# Immutability and Mutation

## Core Idea
Immutable data cannot be changed after creation; mutable data can. Strings are immutable in many languages (operations return new strings). Arrays are mutable (operations modify them in place). Understanding mutability prevents unexpected side effects.

## How It's Best Learned
Attempt to modify immutable objects and observe errors; modify mutable collections and trace changes; compare performance of creating new objects vs modifying in place.

## Common Misconceptions
That all data is mutable (strings are often immutable); that immutable data is inefficient (it can enable optimizations); that immutability means the variable can't change (the variable can reference a new object).

## Explainer

Now that you understand how to access and modify elements in collections, it is time to examine a deeper question: should data be changeable at all? **Mutation** means altering data in place — changing an array element from 5 to 10, for example. The original value is gone, replaced by the new one. **Immutability** means data cannot be changed after creation. When you need a different value, you create a new piece of data rather than modifying the existing one.

The clearest example is strings in many popular languages. When you write `name = "Alice"` and then `name = name + " Smith"`, you might think you modified the original string. But you did not — the string `"Alice"` still exists unchanged somewhere in memory. The `+` operation created an entirely new string `"Alice Smith"` and the variable `name` now points to this new string. The old string becomes unreachable and will eventually be cleaned up. This is what it means for strings to be **immutable**: there is no operation that changes the characters inside an existing string object. Contrast this with arrays, which in most languages are **mutable**: `scores[2] = 95` genuinely overwrites the value at position 2 in the same array — no new array is created.

Why does this distinction matter? Because mutation introduces the possibility of **side effects**. If two parts of your program hold references to the same mutable array and one part modifies it, the other part sees the change — possibly without expecting it. Imagine passing your array of scores to a function that is supposed to compute an average. If that function also sorts the array as a side effect, your original data is now in a different order. With immutable data, this surprise is impossible: since no one can change the data, everyone who holds a reference sees the same values forever.

The subtlety that trips up many learners is the difference between a variable and the data it refers to. When we say a string is immutable, we mean the string *object* cannot change — but the *variable* holding a reference to it can be reassigned to point to a different string. You can write `name = "Bob"` after `name = "Alice"` — the variable changed, but neither string object was altered. Understanding this distinction between the container (the variable) and its contents (the data) is fundamental. It clarifies when you are making a new copy versus modifying in place, which directly affects both correctness and performance as your programs grow more complex.
