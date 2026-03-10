---
id: objects-and-instances
title: Objects and Instances
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: intro-to-classes
  type: hard
builds-toward:
- methods-and-attributes
tags:
- objects
- instances
- instantiation
- constructors
- __init__
stage: abstract-reasoning
status: draft
---

# Objects and Instances

## Core Idea
An object is a specific instance of a class, created by calling the class as a function (e.g., obj = MyClass()). The constructor method (__init__ in Python, or similar in other languages) runs automatically at instantiation to initialize the object's attributes. Each instance maintains its own independent copy of instance attributes, even though all instances share the class's method definitions. Objects are the fundamental unit of computation in object-oriented programs.

## How It's Best Learned
Create multiple instances of the same class with different initial data and print their attributes. Modify one instance's attribute and verify the other is unaffected. Step through a constructor call in a debugger.

## Common Misconceptions
- Thinking instances share attribute values — each has its own.
- Calling __init__ explicitly rather than letting instantiation trigger it.
- Confusing class attributes (shared across all instances) with instance attributes (unique per object).
