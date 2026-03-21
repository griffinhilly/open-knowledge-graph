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

## Questions

```yaml
- question: "You have two BankAccount objects: account_a with a balance of $100 and account_b with a balance of $500. You call account_a.deposit(200). What is account_b's balance afterward?"
  type: multiple-choice
  options:
    - "$700 — both accounts share state because they were created from the same class"
    - "$500 — the method only operated on account_a's data via self/this"
    - "$300 — the deposit was averaged across both accounts"
    - "Undefined — you must call deposit on both accounts to keep them synchronized"
  answer: 1
  explanation: "Each object instance has its own separate copy of the data (attributes). When deposit is called on account_a, the self/this reference inside the method points to account_a, so only account_a's balance changes. account_b is completely unaffected. The class blueprint is shared, but the data each object holds is independent. This is the core of encapsulation: outside code cannot accidentally change the wrong object's state."

- question: "What does 'self' (Python) or 'this' (Java/JavaScript) refer to inside a method?"
  type: multiple-choice
  options:
    - "The class definition from which the object was created"
    - "The specific object instance on which the method was called"
    - "All instances of the class that currently exist in memory"
    - "The method that is currently executing"
  answer: 1
  explanation: "self/this is a reference to the particular object that received the method call — not the class, not all instances, and not the method itself. When account_a.deposit(500) is called, self inside deposit refers to account_a. When account_b.deposit(200) is called, self refers to account_b. The same method code runs in both cases, but self routes it to the correct object's data each time."

- question: "Each object instance of a class has its own separate copy of the class's method code."
  type: true-false
  answer: false
  explanation: "Method code is defined once in the class and shared by all instances — there is only one copy of the deposit method, for example. What each instance has separately is its own data (attributes). When you call a method on an object, you are running the shared code with self/this pointing to that specific object's data. Storing separate method copies for each instance would be enormously wasteful and is not how object-oriented languages work."

- question: "Calling a method on an object — such as my_account.deposit(500) — can be understood as sending the object a message, asking it to perform a specific operation on its own data."
  type: true-false
  answer: true
  explanation: "The 'message-passing' metaphor is the conceptual foundation of object-oriented programming. my_account.deposit(500) is a request directed at a specific object: 'please deposit 500 into your own balance.' The object receives the message and handles it internally using self/this to access and modify its own state. The caller does not need to know how the balance is stored — that internal detail is hidden. This is encapsulation in action."

- question: "Two BankAccount objects are created from the same class. Explain why each maintains its own balance independently, even though they share the same method code."
  type: short-answer
  answer: "When a class creates an instance, each instance gets its own allocated memory for its attributes — including balance. The method code (like deposit) is stored once in the class, but self/this inside each method call refers to the specific instance that received the call. So when deposit runs for account_a, self.balance accesses account_a's memory slot; when it runs for account_b, self.balance accesses account_b's memory slot. Shared method code + separate instance data + self/this routing = fully independent behavior per object."
  explanation: "The confusion often arises from thinking that because objects come from the same class, they share everything. The class is better understood as a factory: the factory design (class) is shared, but each product (instance) that comes off the line has its own independent set of attributes. The self/this mechanism is what makes a shared method operate on one specific instance's data at a time rather than all instances at once."
```

## Explainer

From your work with methods and attributes, you know that objects bundle data (attributes) with functions (methods) that operate on that data. From introducing objects and classes, you understand that a class is a blueprint and objects are instances built from it. This topic connects those ideas by focusing on *how* methods work and what it means to "send a message" to an object.

Consider a real-world analogy. A bank account has data (balance, account number, owner name) and operations you can perform on it (deposit, withdraw, check balance). You do not reach into the bank's database and manually change numbers — you *ask* the account to perform an operation. `my_account.deposit(500)` is like walking up to a teller and saying "please deposit $500 into this account." The account object knows its own balance and knows how to update it. You, the caller, do not need to know the internal details. This "asking" is what object-oriented programming calls **sending a message** — the method call `my_account.deposit(500)` sends the message "deposit" with the argument 500 to the object `my_account`.

Inside the `deposit` method, the code needs a way to refer to the specific account that received the message. That is what **`self`** (Python) or **`this`** (Java, JavaScript, C++) provides — it is a reference to the particular object the method was called on. When you write `self.balance += amount` inside `deposit`, `self` refers to whichever account object received the call. If you call `account_a.deposit(500)`, `self` is `account_a`. If you call `account_b.deposit(200)`, `self` is `account_b`. The method code is shared — there is only one copy of the `deposit` instructions — but `self`/`this` routes it to the right object's data each time.

This is the essence of **encapsulation**: the object's data and the methods that manipulate it are packaged together, and outside code interacts only through the method interface. You cannot accidentally overdraw `account_a` by modifying `account_b`, because each method call is scoped to one object via `self`/`this`. As you move toward object-oriented design, this message-passing mental model becomes the foundation — objects are not passive data containers but active entities that receive requests and decide how to respond based on their own state.
