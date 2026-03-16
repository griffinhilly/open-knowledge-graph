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

## Explainer

You already know that an object is an instance of a class, carrying its own data. Now let's look at the two building blocks that make objects useful: **attributes** store what an object *knows*, and **methods** define what an object can *do*. Together, they turn a passive data container into something that behaves.

**Attributes** are variables that live inside an object. You access them with **dot notation**: `account.balance`, `player.health`, `car.speed`. Each object has its own copy — changing `car_a.speed` does not touch `car_b.speed`. Attributes are typically set during construction (in the `__init__` method in Python, or the constructor in Java/C++) and then read or modified throughout the object's lifetime. They represent the object's state at any given moment.

**Methods** are functions defined inside the class that operate on that state. The critical difference between a method and a standalone function is that a method automatically receives a reference to the object it was called on — in Python this is the `self` parameter, in Java/C++ it is the implicit `this`. When you write `account.deposit(50)`, the `deposit` method receives `self` pointing to `account`, so it can access `self.balance` and modify it. This is why forgetting `self` in a Python method definition causes confusing errors — without it, the method has no way to reach the object's attributes.

A well-designed class controls access to its attributes through methods rather than letting outside code modify attributes directly. For example, instead of writing `account.balance = account.balance + 50` (which skips any validation), you call `account.deposit(50)`, and the method can check that the amount is positive before updating the balance. A `withdraw` method can verify sufficient funds before reducing the balance. These are examples of **getter** and **setter** patterns: methods that read or update attributes while enforcing rules. This idea — that the object controls how its own data is accessed and changed — is the beginning of **encapsulation**, one of the central ideas in object-oriented programming. The object's methods form its public **interface**: the set of operations the outside world can ask it to perform, without needing to know the internal details of how attributes are stored or managed.
