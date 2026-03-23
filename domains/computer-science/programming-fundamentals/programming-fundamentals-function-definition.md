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
stage: formal-systems
status: draft
---

# Function Definition and Calling

## Core Idea
A function is a reusable block of code that performs a specific task. Defining a function specifies its name and body; calling it executes that code. Functions reduce duplication and organize code logically.

## Questions

```yaml
- question: "A student writes the following Python program and runs it: `def welcome(): print('Hello!')`. Nothing prints. Why?"
  type: multiple-choice
  options:
    - "Python functions require a return statement to produce any output"
    - "The function was defined but never called — the body only runs when the function is invoked with welcome()"
    - "print() cannot be used inside a function definition"
    - "The function name must match the filename for it to execute"
  answer: 1
  explanation: "Defining a function with `def` stores the code for later use — it does not execute it. The body runs only when the function is called by writing `welcome()`. This is the single most important distinction in this topic: the definition is a saved recipe; the call is when you actually cook. Forgetting to call a defined function is one of the most common beginner mistakes."

- question: "A programmer needs to display a formatted receipt in five different places in her program. She copies and pastes the same four lines five times. What principle does this violate, and what is the correct solution?"
  type: multiple-choice
  options:
    - "It violates object-oriented design; she should use a class instead"
    - "It violates the DRY principle (Don't Repeat Yourself); she should define the receipt logic as a function and call it in each place"
    - "It violates type safety; repeated code causes type errors at runtime"
    - "Nothing — repeating code is acceptable and sometimes preferred for clarity"
  answer: 1
  explanation: "The DRY principle states that logic should exist in one place. Duplicating four lines five times means any change requires finding and fixing all five copies — one will inevitably be missed. A function encapsulates the logic once; calling it five times means a single edit propagates everywhere. This is the primary practical motivation for using functions."

- question: "When Python executes a `def` statement, it immediately runs all the code inside the function body."
  type: true-false
  answer: false
  explanation: "A `def` statement creates (defines) the function and associates its body with the given name — it does not execute the body. The body executes only when the function is called with its name followed by parentheses. This is analogous to saving a contact in your phone: saving does not call them."

- question: "The same function can be called multiple times within a single program, and it will execute its entire body each time it is called."
  type: true-false
  answer: true
  explanation: "This is the key benefit of functions: write once, execute many times. Each call is independent — the function runs its full body from top to bottom each time it is invoked. This eliminates the need to copy-paste code and ensures consistent behavior across all uses."

- question: "What is the difference between defining a function and calling a function? Why does this distinction matter?"
  type: short-answer
  answer: "Defining a function (using `def`) creates the function and stores its instructions — it does not execute them. Calling a function (writing its name with parentheses) triggers execution of the body. The distinction matters because you can define a function once and call it many times, and nothing happens until a call is made."
  explanation: "Confusing definition with execution leads to bugs where students write a function but wonder why nothing happens. Understanding that `def` is a storage operation, not an execution operation, is foundational to all subsequent function concepts — parameters, return values, scope, and recursion all build on this distinction."
```

## Explainer

You already know that programs execute statements in sequence and that variables store values for later use. Functions build on both ideas: they let you bundle a sequence of statements together, give that bundle a name, and run it whenever you want. If variables are like labeled boxes that hold data, functions are like labeled recipes that hold instructions.

**Defining** a function means writing its code — giving it a name and a body of statements. In Python, `def greet(): print("Hello!")` creates a function called `greet`. But here is the critical distinction: defining a function does not run it. The code inside sits dormant until you **call** the function by writing its name followed by parentheses: `greet()`. Think of it like saving a contact in your phone versus actually calling them. The definition is the save; the call is the dial. You can call the same function as many times as you want, and it will execute its body each time.

Why bother? Imagine you need to print a formatted greeting in five different places in your program. Without functions, you would copy and paste the same three lines five times. If you later need to change the greeting, you would have to find and fix all five copies — and you will inevitably miss one. With a function, you write the code once, call it five times, and change it in one place. This principle is sometimes called **DRY** — Don't Repeat Yourself. Functions are the primary tool for achieving it.

Functions also make programs easier to read and reason about. When you see `calculate_tax(price)` in the middle of a program, you immediately understand the intent without reading the implementation. Each function becomes a building block with a clear name and a clear job. As your programs grow, you will compose larger behaviors out of smaller functions, each one a manageable, testable unit. This decomposition — breaking a big problem into named, reusable pieces — is the foundation of all software design.
