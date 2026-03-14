---
id: methods-and-attributes
title: Methods and Attributes
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: objects-and-instances
  type: hard
builds-toward:
- algorithm-design-basics
tags:
- methods
- attributes
- self
- dot notation
- encapsulation
stage: abstract-reasoning
status: validated
---

# Methods and Attributes

## Core Idea
Attributes are the data stored in an object (accessed with dot notation: obj.attribute). Methods are functions defined inside a class that operate on the object's data, receiving the object itself as their first argument (self). Getter methods expose attribute values; setter methods validate and update them. The combination of attributes and methods implements the object's interface — what the outside world can ask the object to do or report.

## How It's Best Learned
Add deposit(), withdraw(), and get_balance() methods to a BankAccount class. Enforce invariants in setters (e.g., balance cannot be negative). Access attributes via methods rather than directly to practice encapsulation.

## Common Misconceptions
- Forgetting self when defining a method, causing a 'positional argument' error at call time.
- Accessing instance attributes without self inside a method (uses local variable instead).
- Thinking methods and functions are completely different — methods are functions that receive the object implicitly.
