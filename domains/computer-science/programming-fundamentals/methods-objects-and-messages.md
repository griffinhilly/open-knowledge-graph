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

## Explainer

From your work with methods and attributes, you know that objects bundle data (attributes) with functions (methods) that operate on that data. From introducing objects and classes, you understand that a class is a blueprint and objects are instances built from it. This topic connects those ideas by focusing on *how* methods work and what it means to "send a message" to an object.

Consider a real-world analogy. A bank account has data (balance, account number, owner name) and operations you can perform on it (deposit, withdraw, check balance). You do not reach into the bank's database and manually change numbers — you *ask* the account to perform an operation. `my_account.deposit(500)` is like walking up to a teller and saying "please deposit $500 into this account." The account object knows its own balance and knows how to update it. You, the caller, do not need to know the internal details. This "asking" is what object-oriented programming calls **sending a message** — the method call `my_account.deposit(500)` sends the message "deposit" with the argument 500 to the object `my_account`.

Inside the `deposit` method, the code needs a way to refer to the specific account that received the message. That is what **`self`** (Python) or **`this`** (Java, JavaScript, C++) provides — it is a reference to the particular object the method was called on. When you write `self.balance += amount` inside `deposit`, `self` refers to whichever account object received the call. If you call `account_a.deposit(500)`, `self` is `account_a`. If you call `account_b.deposit(200)`, `self` is `account_b`. The method code is shared — there is only one copy of the `deposit` instructions — but `self`/`this` routes it to the right object's data each time.

This is the essence of **encapsulation**: the object's data and the methods that manipulate it are packaged together, and outside code interacts only through the method interface. You cannot accidentally overdraw `account_a` by modifying `account_b`, because each method call is scoped to one object via `self`/`this`. As you move toward object-oriented design, this message-passing mental model becomes the foundation — objects are not passive data containers but active entities that receive requests and decide how to respond based on their own state.
