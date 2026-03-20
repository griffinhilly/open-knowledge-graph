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

## Questions

```yaml
- question: "A Python program uses a bare `except: pass` to wrap its main processing function. It works fine in testing. In production, users report they cannot stop the program with Ctrl+C. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The `pass` statement should be replaced with a `return` statement to allow clean exits"
    - "A bare `except:` catches all exceptions including `KeyboardInterrupt`, silently swallowing the signal that would otherwise stop the program"
    - "The `try` block needs to be wrapped in a `while` loop to handle repeated exceptions in production"
    - "The function raises too many different exception types for a single handler to manage"
  answer: 1
  explanation: "A bare `except:` catches everything — including `KeyboardInterrupt` (Ctrl+C) and `SystemExit`. Combined with `pass`, it silently discards the signal, making the program impossible to stop normally. This is the canonical reason to always name specific exception types. Catch only what you expect and can meaningfully handle; let everything else propagate."

- question: "A function opens a network connection, performs an operation that might fail, and must close the connection whether the operation succeeds or fails. Which structure handles this correctly?"
  type: multiple-choice
  options:
    - "Put the close call inside both the try and except blocks separately"
    - "Use a `finally` block, which runs regardless of whether an exception was raised"
    - "Use an `else` block, which runs only if no exception occurred"
    - "Wrap the entire function in an outer try-except and close the connection in the outer handler"
  answer: 1
  explanation: "`finally` is designed precisely for cleanup that must always execute — closing files, releasing connections, freeing resources. The `else` block runs only on success, so it won't close if an exception is raised. Duplicating the close call in try and except is error-prone and hard to maintain. `finally` provides a single, guaranteed execution point regardless of the code path."

- question: "Catching a specific exception type (e.g., `except ValueError`) is better practice than using a bare `except:` clause."
  type: true-false
  answer: true
  explanation: "Specific exception handling allows you to respond appropriately to expected errors while letting unexpected ones (and system signals like KeyboardInterrupt) propagate normally. A bare `except:` catches everything, including bugs you haven't anticipated — hiding errors that should be visible and making programs impossible to stop or debug. Always name the exception you expect."

- question: "Using try-except blocks is the best way to prevent invalid user input from reaching your program, replacing the need for upfront input validation."
  type: true-false
  answer: false
  explanation: "This confuses error handling with error prevention. Input validation (checking format, range, or type before processing) prevents known invalid inputs from reaching risky operations — it's cleaner and more explicit. Error handling with try-except is appropriate for failures you can't reliably predict in advance: network timeouts, corrupted files, race conditions. Good programs use both strategies at different points."

- question: "What is the difference between error prevention and error handling, and when is each approach appropriate?"
  type: short-answer
  answer: "Error prevention uses upfront validation to check inputs before a risky operation — e.g., checking that a string is numeric before converting it. Error handling uses try-except to respond to runtime failures. Prevention is best when you can reliably detect problems in advance. Handling is appropriate for situations that are hard to predict: network failures, missing files, unexpected data formats. Good programs use both."
  explanation: "The distinction matters because overusing try-except for things that should be validated upfront produces code that's harder to read and debug. If you can say 'if input is valid, proceed; otherwise, prompt again,' that's cleaner than catching a ValueError after the fact. Save exception handling for genuinely unpredictable failures — the cases where you can't know in advance whether the operation will succeed."
```

## Explainer

You know how to define and call functions, and you have encountered situations where things go wrong at runtime — a user types "abc" when your program expects a number, or a file you try to open does not exist. Without error handling, these situations crash your program with a traceback. **Exceptions** are Python's mechanism for dealing with runtime errors gracefully, allowing your program to detect the problem, respond to it, and continue running.

The core construct is the **try-except block**. You place the risky code inside the `try` clause and specify what to do if it fails in the `except` clause. For example: `try: age = int(input("Age: "))` followed by `except ValueError: print("Please enter a number")`. If `int()` fails because the input is not a valid integer, Python raises a `ValueError` exception. Instead of crashing, execution jumps to the except block, which handles the error. If no exception occurs, the except block is skipped entirely. This is fundamentally different from checking conditions beforehand (like `if input.isdigit()`) — exceptions handle errors that are difficult or impossible to predict in advance, such as network timeouts or corrupted files.

Different error conditions produce different **exception types**, and you should catch them specifically. `ValueError` means a function received an argument of the right type but inappropriate value. `TypeError` means the types do not match. `FileNotFoundError` means the file path does not exist. `ZeroDivisionError` means you divided by zero. Catching specific types lets you respond appropriately to each: you might re-prompt the user for a ValueError but log an error and exit for a FileNotFoundError. A bare `except:` with no type catches *everything*, including `KeyboardInterrupt` (Ctrl+C) and `SystemExit`, which makes your program difficult to stop and hides genuine bugs. Always name the exception type you expect.

Python also provides `else` and `finally` clauses for try blocks. The `else` block runs only if no exception occurred — it is the right place for code that should execute only on success. The `finally` block runs *no matter what*, whether an exception occurred or not, making it ideal for cleanup operations like closing files or releasing resources. You can also **raise** exceptions yourself with the `raise` statement: `raise ValueError("Age must be positive")` signals to the calling code that something went wrong. This is how you build functions that communicate errors upward through the call stack. The caller can then decide whether to handle the exception or let it propagate further. Well-designed error handling gives your program a clear separation between the normal path (try and else) and the error-recovery path (except and finally), making both easier to reason about.
