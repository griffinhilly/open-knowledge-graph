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
stage: abstract-reasoning
status: draft
---

# Immutability and Mutation

## Core Idea
Immutable data cannot be changed after creation; mutable data can. Strings are immutable in many languages (operations return new strings). Arrays are mutable (operations modify them in place). Understanding mutability prevents unexpected side effects.

## How It's Best Learned
Attempt to modify immutable objects and observe errors; modify mutable collections and trace changes; compare performance of creating new objects vs modifying in place.

## Common Misconceptions
That all data is mutable (strings are often immutable); that immutable data is inefficient (it can enable optimizations); that immutability means the variable can't change (the variable can reference a new object).
