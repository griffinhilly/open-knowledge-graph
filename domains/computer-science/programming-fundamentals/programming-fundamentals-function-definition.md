---
id: programming-fundamentals-function-definition
title: Function Definition and Calling
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-variables-assignment
  type: hard
builds-toward:
- programming-fundamentals-parameters-arguments
- programming-fundamentals-return-values
tags:
- functions
- definition
- calling
stage: abstract-reasoning
status: draft
---

# Function Definition and Calling

## Core Idea
A function is a reusable block of code that performs a specific task. Defining a function specifies its name and body; calling it executes that code. Functions reduce duplication and organize code logically.

## Explainer

You already know that programs execute statements in sequence and that variables store values for later use. Functions build on both ideas: they let you bundle a sequence of statements together, give that bundle a name, and run it whenever you want. If variables are like labeled boxes that hold data, functions are like labeled recipes that hold instructions.

**Defining** a function means writing its code — giving it a name and a body of statements. In Python, `def greet(): print("Hello!")` creates a function called `greet`. But here is the critical distinction: defining a function does not run it. The code inside sits dormant until you **call** the function by writing its name followed by parentheses: `greet()`. Think of it like saving a contact in your phone versus actually calling them. The definition is the save; the call is the dial. You can call the same function as many times as you want, and it will execute its body each time.

Why bother? Imagine you need to print a formatted greeting in five different places in your program. Without functions, you would copy and paste the same three lines five times. If you later need to change the greeting, you would have to find and fix all five copies — and you will inevitably miss one. With a function, you write the code once, call it five times, and change it in one place. This principle is sometimes called **DRY** — Don't Repeat Yourself. Functions are the primary tool for achieving it.

Functions also make programs easier to read and reason about. When you see `calculate_tax(price)` in the middle of a program, you immediately understand the intent without reading the implementation. Each function becomes a building block with a clear name and a clear job. As your programs grow, you will compose larger behaviors out of smaller functions, each one a manageable, testable unit. This decomposition — breaking a big problem into named, reusable pieces — is the foundation of all software design.
