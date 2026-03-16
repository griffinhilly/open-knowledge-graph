---
id: error-handling-exceptions
title: Error Handling and Exceptions
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-defining-calling
  type: hard
- id: return-values
  type: soft
- id: debugging-basics
  type: soft
- id: type-conversion
  type: soft
builds-toward:
- file-io-basics
tags:
- exceptions
- try
- except
- raise
- error handling
- robustness
stage: abstract-reasoning
status: validated
---
# Error Handling and Exceptions

## Core Idea
Exceptions are events that disrupt normal program flow when an error occurs at runtime. A try-except block (or try-catch in some languages) catches exceptions and handles them gracefully instead of crashing the program. The raise statement signals that an error condition has occurred. Different exception types (ValueError, TypeError, FileNotFoundError, etc.) represent different error categories, allowing targeted handling. Good exception handling makes programs robust against bad input and unexpected conditions.

## How It's Best Learned
Wrap risky operations (type conversion, file access, division) in try-except blocks. Write functions that raise custom exceptions with informative messages. Practice catching specific exception types rather than bare except clauses.

## Common Misconceptions
- Using a bare except: that silently catches all exceptions, including program bugs.
- Catching exceptions that should propagate (e.g., KeyboardInterrupt).
- Confusing error handling (try-except) with error prevention (input validation before the risky operation).

## Explainer

You know how to define and call functions, and you have encountered situations where things go wrong at runtime — a user types "abc" when your program expects a number, or a file you try to open does not exist. Without error handling, these situations crash your program with a traceback. **Exceptions** are Python's mechanism for dealing with runtime errors gracefully, allowing your program to detect the problem, respond to it, and continue running.

The core construct is the **try-except block**. You place the risky code inside the `try` clause and specify what to do if it fails in the `except` clause. For example: `try: age = int(input("Age: "))` followed by `except ValueError: print("Please enter a number")`. If `int()` fails because the input is not a valid integer, Python raises a `ValueError` exception. Instead of crashing, execution jumps to the except block, which handles the error. If no exception occurs, the except block is skipped entirely. This is fundamentally different from checking conditions beforehand (like `if input.isdigit()`) — exceptions handle errors that are difficult or impossible to predict in advance, such as network timeouts or corrupted files.

Different error conditions produce different **exception types**, and you should catch them specifically. `ValueError` means a function received an argument of the right type but inappropriate value. `TypeError` means the types do not match. `FileNotFoundError` means the file path does not exist. `ZeroDivisionError` means you divided by zero. Catching specific types lets you respond appropriately to each: you might re-prompt the user for a ValueError but log an error and exit for a FileNotFoundError. A bare `except:` with no type catches *everything*, including `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, which makes your program difficult to stop and hides genuine bugs. Always name the exception type you expect.

Python also provides `else` and `finally` clauses for try blocks. The `else` block runs only if no exception occurred — it is the right place for code that should execute only on success. The `finally` block runs *no matter what*, whether an exception occurred or not, making it ideal for cleanup operations like closing files or releasing resources. You can also **raise** exceptions yourself with the `raise` statement: `raise ValueError("Age must be positive")` signals to the calling code that something went wrong. This is how you build functions that communicate errors upward through the call stack. The caller can then decide whether to handle the exception or let it propagate further. Well-designed error handling gives your program a clear separation between the normal path (try and else) and the error-recovery path (except and finally), making both easier to reason about.
