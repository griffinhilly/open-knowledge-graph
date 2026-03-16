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

## Explainer

From your work with functions and variable scope, you know how to organize code into reusable blocks and how variables live within defined boundaries. Classes take this organization one level higher by **bundling related data and the functions that operate on that data into a single unit**. Imagine you're writing a program to manage bank accounts. Without classes, you'd have separate variables (`account_balance`, `account_owner`, `account_number`) and separate functions (`deposit()`, `withdraw()`, `get_balance()`), all floating independently. With a class, these belong together as a coherent whole.

A **class** is a blueprint or template — it describes what data an object will hold (its **attributes**) and what it can do (its **methods**). Think of a cookie cutter: the cutter itself is the class, and each cookie you stamp out is an **instance** (an object). Defining `class BankAccount:` creates the template. Calling `my_account = BankAccount()` creates an actual object from that template — this is called **instantiation**. Each instance has its own independent copy of the attributes. If you create two BankAccount objects, depositing into one doesn't affect the other, just as two cookies cut from the same cutter are separate physical objects.

Methods are functions that live inside a class and operate on a specific instance's data. In Python, every method takes `self` as its first parameter, which refers to the particular object the method was called on. When you write `my_account.deposit(50)`, Python automatically passes `my_account` as `self`, so the method knows *which* account to update. This is what connects the function to the data — `self.balance += amount` modifies this particular account's balance, not some global variable. The `__init__` method (the constructor) runs automatically when you create a new instance, setting up the object's initial state.

The deeper principle at work is **encapsulation**: grouping data with the operations that make sense for that data, and presenting a clean interface to the rest of the program. Other code doesn't need to know *how* the BankAccount tracks its balance internally — it just calls `deposit()` and `withdraw()`. This separation means you can change the internal implementation later (maybe switching from a simple number to a transaction log) without breaking any code that uses the class. Classes become the fundamental building block of **object-oriented programming**, where you model your problem as interacting objects, each managing its own state and responsibilities.
