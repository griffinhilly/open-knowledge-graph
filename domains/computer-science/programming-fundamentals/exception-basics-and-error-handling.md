---
id: exception-basics-and-error-handling
title: Exception Basics and Error Handling
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: program-structure-and-flow
  type: hard
tags:
- errors
- exceptions
- handling
stage: abstract-reasoning
status: draft
---

# Exception Basics and Error Handling

## Core Idea
Exceptions represent errors or exceptional conditions that disrupt normal execution. Try-catch blocks allow handling exceptions gracefully. Throwing an exception signals an error; catching it prevents the program from crashing and enables recovery.

## How It's Best Learned
Write code that throws exceptions (e.g., divide by zero). Use try-catch to handle exceptions and continue execution.

## Common Misconceptions
- All errors are exceptions (syntax errors and logic errors are different from runtime exceptions).
- Exceptions should be caught and ignored (exceptions should be handled meaningfully; ignoring them hides problems).

## Explainer

In normal program flow, statements execute one after another in a predictable sequence — the control flow you've already learned. But what happens when something goes wrong at runtime? A user enters "hello" where a number was expected. A file you're trying to read doesn't exist. You divide by zero. These are not bugs in your logic — they're unexpected conditions that your program needs to handle gracefully. **Exceptions** are the mechanism most languages provide for dealing with these situations without scattering error-checking code throughout your program.

The core structure is the **try-catch block** (called `try-except` in Python). You wrap the risky code in a `try` block, and if an exception occurs during execution, control immediately jumps to the matching `catch` (or `except`) block. The code in the `catch` block is your **exception handler** — it decides what to do about the problem. For example, if you're reading user input and converting it to a number, you'd wrap the conversion in a `try` block and handle the `ValueError` in the `except` block by printing an error message and asking again. Without exception handling, that same error would crash the program with a traceback.

When an exception is **thrown** (or **raised** in Python), the runtime searches for a handler by unwinding the **call stack** — it checks the current function for a matching `catch` block, then the function that called it, then the function that called that one, and so on. If no handler is found anywhere in the chain, the program terminates with an error message. This unwinding behavior means you don't need to handle exceptions at the exact point where they occur — you can let them propagate upward to a place where you have enough context to respond meaningfully. A low-level file-reading function might throw an IOException, but the high-level function that called it might be the right place to decide whether to retry, use a default, or alert the user.

A crucial principle is to handle exceptions **specifically and meaningfully**. Catching every possible exception with a bare `catch` or `except` block and ignoring it is one of the worst habits in programming — it silences errors, making bugs invisible and debugging nearly impossible. Instead, catch the specific exception types you know how to handle, and let unexpected ones propagate so they surface as visible errors. Many languages also provide a **finally** block that runs whether or not an exception occurred, which is the right place for cleanup code like closing files or releasing resources. The pattern of try-catch-finally gives you precise control over both the happy path and the error path of your program.
