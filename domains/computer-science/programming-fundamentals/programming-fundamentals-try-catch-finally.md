---
id: programming-fundamentals-try-catch-finally
title: Try-Catch-Finally Blocks
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-exceptions-intro
  type: hard
tags:
- errors
- exceptions
- try
- catch
stage: abstract-reasoning
status: draft
---

# Try-Catch-Finally Blocks

## Core Idea
Try-catch blocks allow graceful error handling. Code in the try block runs normally; if an exception occurs, the catch block handles it. Finally blocks run regardless of success or error, useful for cleanup. Multiple catch blocks handle different exception types.

## Explainer

From your introduction to exceptions, you know that runtime errors — dividing by zero, accessing a missing file, or receiving unexpected input — can crash a program if left unhandled. The **try-catch-finally** construct gives you a structured way to anticipate these errors, respond to them, and ensure critical cleanup always happens. Think of it as a safety net: you attempt something that might fail, and instead of crashing, your program gracefully recovers.

The **try block** wraps the code that might throw an exception. Execution proceeds normally line by line until either the block completes successfully or an exception is thrown. If no exception occurs, the catch block is skipped entirely. If an exception does occur, execution immediately jumps to the **catch block** — no further lines in the try block run. The catch block receives the exception object, which typically contains a message and a type describing what went wrong. You can use this information to log the error, display a user-friendly message, retry the operation, or take alternative action. Many languages support **multiple catch blocks** ordered from most specific to most general, so you can handle a `FileNotFoundException` differently from a generic `IOException`.

The **finally block** runs no matter what — whether the try block succeeded, whether an exception was caught, or even if you return from inside the try or catch. This makes it the right place for **cleanup code**: closing files, releasing database connections, or freeing resources that must not leak. Without finally, you would need to duplicate cleanup code in both the normal path and every error path, which is fragile and error-prone. A common real-world pattern is opening a file in try, processing it, catching any I/O errors, and closing the file in finally.

A key design principle is to keep try blocks focused. Wrapping too much code in a single try block makes it hard to know which operation caused the exception and leads to catch blocks that handle errors they were not designed for. A good rule of thumb: wrap only the specific operations that can fail, handle only the exceptions you can meaningfully respond to, and let unexpected exceptions propagate upward to a higher-level handler. This keeps your error handling precise and your program's behavior predictable.
