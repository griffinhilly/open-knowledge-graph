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

## Questions

```yaml
- question: "A student writes this method inside a BankAccount class in Python: `def deposit(amount): balance = balance + amount`. When they call account.deposit(100), they get an error. What are the two problems?"
  type: multiple-choice
  options:
    - "`deposit` is not a valid method name — it should be called `add_funds` to follow conventions"
    - "`self` is missing from the parameter list, and `balance` should be accessed as `self.balance` to reach the instance attribute"
    - "The method needs a `return` statement to update the account balance"
    - "`deposit` must be defined outside the class to receive the object as an argument"
  answer: 1
  explanation: "Both errors relate to `self`. Without `self` as the first parameter, Python passes the object as an argument the method doesn't expect, causing a 'takes 1 positional argument but 2 were given' error. Even if `self` were added to the signature, writing `balance = balance + amount` creates or modifies a local variable named `balance`, not the instance attribute — `self.balance` is required to reach the object's stored data."

- question: "Why is calling `account.withdraw(50)` preferable to writing `account.balance -= 50` directly from outside the class?"
  type: multiple-choice
  options:
    - "The dot notation syntax requires method calls — direct attribute modification raises a syntax error"
    - "Methods execute faster than direct attribute access due to Python's internal optimizations"
    - "The method can enforce rules — such as checking for sufficient funds — before modifying the attribute, preventing invalid state"
    - "Direct attribute modification is not allowed in Python; attributes are always read-only from outside the class"
  answer: 2
  explanation: "This is the point of encapsulation. `account.balance -= 50` bypasses any validation and can leave the account in an invalid state (negative balance). A `withdraw` method can check `if amount > self.balance: raise ValueError` before making the change. The object controls how its own data is modified — this is what makes methods more than just convenience wrappers."

- question: "A method is fundamentally a function — the key difference is that a method automatically receives a reference to the object it was called on as its first argument."
  type: true-false
  answer: true
  explanation: "Methods are not a fundamentally different kind of thing from functions — they are functions defined inside a class that receive the object implicitly. In Python this reference is `self`; in Java/C++ it is `this`. When you write `account.deposit(50)`, Python automatically passes `account` as the `self` argument. This is why the misconception that 'methods and functions are completely different' is worth correcting — understanding their relationship makes the `self` parameter logical rather than mysterious."

- question: "In Python, if you define a method without the `self` parameter, the method will still work correctly as long as it doesn't read or write any instance attributes inside it."
  type: true-false
  answer: false
  explanation: "Even if the method body uses no instance attributes, calling it as `obj.method()` will pass the object as the first positional argument. Since the method signature has no parameter to receive it, Python raises 'takes 0 positional arguments but 1 was given.' The `self` parameter must be present in the signature regardless of whether it is used in the body — Python always passes the object when a method is called on an instance."

- question: "What is encapsulation, and how do attributes and methods work together to implement it in a class?"
  type: short-answer
  answer: "Encapsulation is the principle that an object controls access to its own data — outside code interacts with the object through its method interface rather than reading or writing attributes directly. Attributes store the object's state; methods define the operations the outside world can request. By routing access through methods, the class can enforce invariants (e.g., balance cannot go negative), hide internal implementation details, and change how data is stored without breaking code that uses the class."
  explanation: "The BankAccount example makes this concrete: exposing `balance` as a public attribute lets anyone set it to any value, including invalid ones. Providing `deposit()` and `withdraw()` as the interface means every change to balance passes through validation logic. This is the beginning of object-oriented design — the class is not just a data container but a behavioral unit that takes responsibility for maintaining its own valid state."
```

## Explainer

You already know that an object is an instance of a class, carrying its own data. Now let's look at the two building blocks that make objects useful: **attributes** store what an object *knows*, and **methods** define what an object can *do*. Together, they turn a passive data container into something that behaves.

**Attributes** are variables that live inside an object. You access them with **dot notation**: `account.balance`, `player.health`, `car.speed`. Each object has its own copy — changing `car_a.speed` does not touch `car_b.speed`. Attributes are typically set during construction (in the `__init__` method in Python, or the constructor in Java/C++) and then read or modified throughout the object's lifetime. They represent the object's state at any given moment.

**Methods** are functions defined inside the class that operate on that state. The critical difference between a method and a standalone function is that a method automatically receives a reference to the object it was called on — in Python this is the `self` parameter, in Java/C++ it is the implicit `this`. When you write `account.deposit(50)`, the `deposit` method receives `self` pointing to `account`, so it can access `self.balance` and modify it. This is why forgetting `self` in a Python method definition causes confusing errors — without it, the method has no way to reach the object's attributes.

A well-designed class controls access to its attributes through methods rather than letting outside code modify attributes directly. For example, instead of writing `account.balance = account.balance + 50` (which skips any validation), you call `account.deposit(50)`, and the method can check that the amount is positive before updating the balance. A `withdraw` method can verify sufficient funds before reducing the balance. These are examples of **getter** and **setter** patterns: methods that read or update attributes while enforcing rules. This idea — that the object controls how its own data is accessed and changed — is the beginning of **encapsulation**, one of the central ideas in object-oriented programming. The object's methods form its public **interface**: the set of operations the outside world can ask it to perform, without needing to know the internal details of how attributes are stored or managed.
