---
id: type-conversion
title: Type Conversion and Casting
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: primitive-data-types
  type: hard
- id: operators-and-expressions
  type: hard
builds-toward:
- string-operations
- basic-input-output
- error-handling-exceptions
tags:
- casting
- type conversion
- int
- float
- str
- coercion
stage: abstract-reasoning
status: validated
---

# Type Conversion and Casting

## Core Idea
Type conversion (casting) transforms a value from one data type to another. Explicit conversion uses functions like int(), float(), and str() to request a specific type. Implicit conversion (coercion) happens automatically when a language combines compatible types (e.g., adding an int to a float). Not all conversions are valid — converting 'hello' to int raises an error. Understanding when and how to convert types is essential for processing user input and mixing numeric types correctly.

## How It's Best Learned
Write a calculator that reads string input, converts to numbers, computes, and formats the result as a string. Deliberately trigger conversion errors and read the error messages carefully.

## Common Misconceptions
- Assuming int('3.14') succeeds — it does not in most languages; float('3.14') must come first.
- Thinking int(3.9) rounds to 4 — it truncates to 3.
- Not realizing that all console input arrives as a string and must be explicitly converted.
