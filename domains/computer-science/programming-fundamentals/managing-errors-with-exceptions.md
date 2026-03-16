---
id: managing-errors-with-exceptions
title: Managing Errors with Exceptions
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: error-handling-exceptions
  type: hard
builds-toward:
- testing-and-validation-basics
tags:
- errors
- exceptions
- handling
stage: abstract-reasoning
status: draft
---

# Managing Errors with Exceptions

## Core Idea
Exceptions signal errors during execution. Try-catch blocks catch exceptions and execute recovery code. Finally blocks execute regardless of success. Proper exception handling prevents crashes and enables graceful degradation.

## How It's Best Learned
Write code that throws exceptions; catch different exception types; test recovery code; use finally to clean up resources.

## Common Misconceptions
That exceptions are for errors only (they signal abnormal conditions, not all are errors); that catching an exception means the program continues normally (the exception still occurred); that every exception should be caught (some should propagate up the call stack).

## Explainer

From your study of error handling and exceptions, you know that exceptions are a mechanism for signaling that something has gone wrong during execution — a file that does not exist, a network connection that drops, a division by zero. **Managing** exceptions is about deciding *where* and *how* to respond to these signals so that your program degrades gracefully instead of crashing. The core construct is the **try-catch block** (called `try-except` in Python): you wrap risky code in `try`, and if an exception occurs, execution jumps to the matching `catch`/`except` block where you handle the problem.

The most important principle is **specificity**: catch the narrowest exception type that makes sense. Writing `except Exception:` catches everything, including bugs you want to know about — a typo that causes a `NameError`, for example, would be silently swallowed. Instead, catch `FileNotFoundError` when opening a file, `ValueError` when parsing user input, or `ConnectionError` when making network requests. Each handler should do something meaningful: display an error message, use a default value, retry the operation, or log the failure. A catch block that simply passes or prints "something went wrong" defeats the purpose — it hides the problem without solving it.

The **finally** block runs regardless of whether an exception occurred or not. This is essential for **cleanup** — closing files, releasing network connections, or freeing resources that must be released no matter what. Without `finally`, a function that opens a file and then crashes mid-processing would leave the file handle dangling. The pattern `try: work with resource / except: handle error / finally: close resource` ensures cleanup happens on both the success and failure paths. In Python, the `with` statement automates this pattern for common resources, but understanding `finally` is important for cases where `with` is not available.

Not every exception should be caught. A function deep in your call stack may not have enough context to handle an error — only the calling code knows whether a missing file is fatal or just means "use the default." In these cases, the right approach is to **let the exception propagate** up the call stack until it reaches code that knows how to respond. Think of exception propagation as a question being passed upward: "I cannot find this file — what should I do?" Each level of the call stack either answers that question (by catching it) or passes it further up. If no one catches it, the program terminates with a stack trace — which is often the correct behavior for genuinely unexpected errors, because it tells you exactly what went wrong and where.
