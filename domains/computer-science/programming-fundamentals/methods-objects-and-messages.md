---
id: methods-objects-and-messages
title: Methods, Objects, and Messages
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: methods-and-attributes
  type: hard
- id: introducing-objects-and-classes
  type: hard
builds-toward:
- object-oriented-thinking-and-design
tags:
- methods
- objects
- behavior
stage: abstract-reasoning
status: draft
---

# Methods, Objects, and Messages

## Core Idea
Methods are functions associated with objects that operate on the object's data. Calling a method on an object is like sending a message. The this/self keyword inside methods refers to the specific object. Methods enable encapsulation and state management.

## How It's Best Learned
Write methods that read and modify object state; understand this/self by printing it; call methods on different objects and trace behavior.

## Common Misconceptions
That methods are just functions (they're functions with access to object state); that this/self is optional (it's implicit in most languages but essential for understanding); that all objects share method behavior (they do) and data (they don't).
