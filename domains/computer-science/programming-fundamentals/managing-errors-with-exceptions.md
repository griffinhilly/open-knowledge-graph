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
stage: formal-systems
status: draft
---

# Managing Errors with Exceptions

## Core Idea
Exceptions signal errors during execution. Try-catch blocks catch exceptions and execute recovery code. Finally blocks execute regardless of success. Proper exception handling prevents crashes and enables graceful degradation.

## How It's Best Learned
Write code that throws exceptions; catch different exception types; test recovery code; use finally to clean up resources.

## Common Misconceptions
That exceptions are for errors only (they signal abnormal conditions, not all are errors); that catching an exception means the program continues normally (the exception still occurred); that every exception should be caught (some should propagate up the call stack).

## Questions

```yaml
- question: "A function opens a configuration file at startup. The file doesn't exist. Which approach best handles this?"
  type: multiple-choice
  options:
    - "Use a bare `except:` block, print 'error occurred', and continue with empty settings"
    - "Catch `FileNotFoundError` specifically, log the error, and fall back to default settings"
    - "Let the exception propagate so the program terminates with a stack trace"
    - "Catch `FileNotFoundError` and silently pass, continuing with an uninitialized config"
  answer: 1
  explanation: "Catching `FileNotFoundError` specifically (option B) is correct: it handles the exact error expected at this boundary, logs it for debugging, and recovers with a sensible default. Option A catches too broadly — a bare `except:` would swallow bugs like NameError that indicate coding mistakes. Option C (propagate) is sometimes correct but wrong here if a default config is available. Option D silently ignores the error, hiding the problem without solving it."

- question: "You are writing a function deep in a call stack that parses user-provided JSON. The JSON is malformed. What is usually the right approach?"
  type: multiple-choice
  options:
    - "Catch the error, print 'invalid input', and return None to let the program continue"
    - "Catch the error and retry parsing with the same input automatically"
    - "Let the exception propagate — the calling code has the context to decide whether this is fatal"
    - "Use a finally block to guarantee the program does not terminate"
  answer: 2
  explanation: "A function deep in the stack often lacks the context to make the right recovery decision. The calling code might want to prompt the user to re-enter data, use a cached value, or terminate entirely — all valid responses depending on the application. Letting the exception propagate passes the decision upward to where context exists. Option A (return None) swaps an exception for a silent bad value that may cause harder-to-diagnose errors later."

- question: "Using a bare `except Exception:` clause is safer than catching specific exception types because it guarantees no exception will crash the program."
  type: true-false
  answer: false
  explanation: "Catching everything silently swallows bugs that should be fixed. A NameError from a typo, an AttributeError from a logic mistake, or an ImportError from a missing module would all be caught and hidden, turning coding errors into mysterious silent failures. The goal of exception handling is not to prevent crashes at all costs — it is to recover from expected failure conditions while letting unexpected ones surface so they can be fixed."

- question: "The `finally` block in a try-except-finally structure runs regardless of whether an exception was raised or not."
  type: true-false
  answer: true
  explanation: "This is the essential property that makes `finally` useful for cleanup. Whether the `try` block succeeds, raises an exception that is caught, or raises one that is not caught, the `finally` block always executes. This guarantees that resources like file handles, database connections, and network sockets are released even when something goes wrong — preventing resource leaks on both success and failure paths."

- question: "Explain why catching every exception at every level of your program is not good error handling, even though it prevents crashes."
  type: short-answer
  answer: "Catching every exception hides bugs that should be fixed and removes the information (stack traces) needed to diagnose them. It also prevents exceptions from reaching the level of the call stack that has enough context to handle them correctly. Good error handling is specific: catch the narrowest exception type expected at each boundary, do something meaningful in response, and let unexpected exceptions propagate so they surface as visible failures."
  explanation: "The key insight is that crashes are not the enemy — silent, incorrect behavior is worse than a visible crash with a useful stack trace. Exception handling should communicate errors meaningfully, not suppress them. A program that silently swallows all exceptions and continues in a broken state is harder to debug and less trustworthy than one that terminates loudly at the point of failure."
```

## Explainer

From your study of error handling and exceptions, you know that exceptions are a mechanism for signaling that something has gone wrong during execution — a file that does not exist, a network connection that drops, a division by zero. **Managing** exceptions is about deciding *where* and *how* to respond to these signals so that your program degrades gracefully instead of crashing. The core construct is the **try-catch block** (called `try-except` in Python): you wrap risky code in `try`, and if an exception occurs, execution jumps to the matching `catch`/`except` block where you handle the problem.

The most important principle is **specificity**: catch the narrowest exception type that makes sense. Writing `except Exception:` catches everything, including bugs you want to know about — a typo that causes a `NameError`, for example, would be silently swallowed. Instead, catch `FileNotFoundError` when opening a file, `ValueError` when parsing user input, or `ConnectionError` when making network requests. Each handler should do something meaningful: display an error message, use a default value, retry the operation, or log the failure. A catch block that simply passes or prints "something went wrong" defeats the purpose — it hides the problem without solving it.

The **finally** block runs regardless of whether an exception occurred or not. This is essential for **cleanup** — closing files, releasing network connections, or freeing resources that must be released no matter what. Without `finally`, a function that opens a file and then crashes mid-processing would leave the file handle dangling. The pattern `try: work with resource / except: handle error / finally: close resource` ensures cleanup happens on both the success and failure paths. In Python, the `with` statement automates this pattern for common resources, but understanding `finally` is important for cases where `with` is not available.

Not every exception should be caught. A function deep in your call stack may not have enough context to handle an error — only the calling code knows whether a missing file is fatal or just means "use the default." In these cases, the right approach is to **let the exception propagate** up the call stack until it reaches code that knows how to respond. Think of exception propagation as a question being passed upward: "I cannot find this file — what should I do?" Each level of the call stack either answers that question (by catching it) or passes it further up. If no one catches it, the program terminates with a stack trace — which is often the correct behavior for genuinely unexpected errors, because it tells you exactly what went wrong and where.
