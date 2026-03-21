---
id: intro-to-classes
title: Introduction to Classes
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: variable-scope
  type: hard
builds-toward:
- objects-and-instances
- methods-and-attributes
tags:
- classes
- OOP
- blueprints
- object-oriented
- encapsulation
stage: abstract-reasoning
status: validated
---

# Introduction to Classes

## Core Idea
A class is a blueprint that defines the structure and behavior shared by a family of objects. It bundles data (attributes) and functions that operate on that data (methods) into a single unit. Defining a class does not create an object; instantiating it does. Classes support encapsulation — hiding internal data and exposing only a clean interface — which reduces the surface area of bugs and makes programs easier to maintain.

## How It's Best Learned
Design a simple class for a real-world concept (e.g., BankAccount, Student, Rectangle) with a few attributes and methods. Instantiate multiple objects from the same class and verify that each has independent state.

## Common Misconceptions
- Confusing the class definition with an instance — the class is the template, the instance is the object.
- Forgetting to include self as the first parameter of every method.
- Thinking all data must be hidden — begin with understanding the concept before worrying about access modifiers.

## Questions

```yaml
- question: "A programmer defines a class Dog with an attribute `name`. She then creates two instances: dog1 = Dog('Rex') and dog2 = Dog('Luna'). She later runs dog1.name = 'Max'. What happens to dog2.name?"
  type: multiple-choice
  options:
    - "dog2.name also changes to 'Max' because both objects share the same class"
    - "dog2.name remains 'Luna' because each instance has its own independent state"
    - "dog2.name becomes None because the class definition was modified"
    - "An error is raised because you cannot modify one instance without modifying all"
  answer: 1
  explanation: "Each instance created from a class has its own independent copy of its attributes. The class is a blueprint — when you instantiate it twice, you get two separate objects with separate memory for their attributes. Modifying dog1.name changes only dog1's copy; dog2 is completely unaffected. This independence is a fundamental property of object-oriented design and is why creating 1,000 Dog objects from the same class results in 1,000 independent objects, not 1,000 references to the same data."

- question: "What does `self` refer to inside a class method, and why is it necessary?"
  type: multiple-choice
  options:
    - "It refers to the class itself, allowing methods to access the class definition"
    - "It is a keyword that marks the method as belonging to the class rather than being a standalone function"
    - "It refers to the specific instance the method was called on, connecting the method to that object's data"
    - "It refers to the parent class, enabling inheritance from built-in types"
  answer: 2
  explanation: "When you call my_account.deposit(50), Python automatically passes my_account as the first argument to the method — this is what `self` receives. Without `self`, a method would have no way to know *which* object it should act on. Writing `self.balance += amount` means 'modify this particular object's balance attribute,' not some global variable. Every instance method needs `self` as its first parameter for this reason. The class definition is shared, but `self` gives each method call access to the specific instance's unique data."

- question: "Defining a class in Python immediately creates an object in memory that you can use."
  type: true-false
  answer: false
  explanation: "Defining a class only creates the blueprint — it does not create any objects. No memory is allocated for instance attributes, and no code inside __init__ is executed. An object is only created when you instantiate the class by calling it like a function (e.g., my_dog = Dog('Rex')). This distinction matters: you can define class BankAccount without any accounts existing yet. Only the act of calling BankAccount() — instantiation — produces an actual object with its own memory and state."

- question: "Two different instances created from the same class can have different values for their attributes."
  type: true-false
  answer: true
  explanation: "This is precisely the point of classes: one blueprint, many independent objects. The class defines which attributes will exist, but each instance gets its own copy of those attributes with its own values. dog1.name = 'Rex' and dog2.name = 'Luna' are two separate attribute slots in two separate objects in memory. The class is like the cookie cutter (always the same shape), while instances are like individual cookies (each can have different frosting)."

- question: "Why does every instance method in Python require `self` as its first parameter? What would break if `self` were omitted?"
  type: short-answer
  answer: "Without `self`, a method has no reference to the specific instance it is operating on. It cannot access or modify that instance's attributes. If you wrote `def deposit(amount): balance += amount`, it would fail because `balance` is not defined as a local variable — it lives on the instance. `self.balance` is the correct reference, and `self` is how the method receives that instance. Without it, Python would treat the method like a plain function with no connection to any object's data."
  explanation: "The need for explicit `self` is a design choice Python made (many other OOP languages implicitly pass `this`). It makes the connection between method and instance visible and explicit. When Python calls my_account.deposit(50), it translates this internally to BankAccount.deposit(my_account, 50) — the instance is always the first argument, and `self` is the parameter that receives it. Omitting `self` would cause the method to receive its first real argument (like `amount`) as `self`, producing confusing errors, and the method would have no way to access the instance's attributes."
```

## Explainer

From your work with functions and variable scope, you know how to organize code into reusable blocks and how variables live within defined boundaries. Classes take this organization one level higher by **bundling related data and the functions that operate on that data into a single unit**. Imagine you're writing a program to manage bank accounts. Without classes, you'd have separate variables (`account_balance`, `account_owner`, `account_number`) and separate functions (`deposit()`, `withdraw()`, `get_balance()`), all floating independently. With a class, these belong together as a coherent whole.

A **class** is a blueprint or template — it describes what data an object will hold (its **attributes**) and what it can do (its **methods**). Think of a cookie cutter: the cutter itself is the class, and each cookie you stamp out is an **instance** (an object). Defining `class BankAccount:` creates the template. Calling `my_account = BankAccount()` creates an actual object from that template — this is called **instantiation**. Each instance has its own independent copy of the attributes. If you create two BankAccount objects, depositing into one doesn't affect the other, just as two cookies cut from the same cutter are separate physical objects.

Methods are functions that live inside a class and operate on a specific instance's data. In Python, every method takes `self` as its first parameter, which refers to the particular object the method was called on. When you write `my_account.deposit(50)`, Python automatically passes `my_account` as `self`, so the method knows *which* account to update. This is what connects the function to the data — `self.balance += amount` modifies this particular account's balance, not some global variable. The `__init__` method (the constructor) runs automatically when you create a new instance, setting up the object's initial state.

The deeper principle at work is **encapsulation**: grouping data with the operations that make sense for that data, and presenting a clean interface to the rest of the program. Other code doesn't need to know *how* the BankAccount tracks its balance internally — it just calls `deposit()` and `withdraw()`. This separation means you can change the internal implementation later (maybe switching from a simple number to a transaction log) without breaking any code that uses the class. Classes become the fundamental building block of **object-oriented programming**, where you model your problem as interacting objects, each managing its own state and responsibilities.
