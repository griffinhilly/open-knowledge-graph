---
id: string-basics
title: String Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
- id: primitive-data-types
  type: hard
builds-toward:
- string-operations
- basic-input-output
tags:
- strings
- text
- characters
- indexing
- immutability
stage: abstract-reasoning
status: validated
---

# String Basics

## Core Idea
A string is a sequence of characters used to represent text. Strings are indexed from zero, so the first character of s is s[0]. In most languages strings are immutable — operations on strings produce new strings rather than modifying the original. String literals are written with quotes; the choice of single vs. double quotes affects how quote characters are included inside the string. Strings support length queries, slicing, and comparison.

## How It's Best Learned
Write programs that index into strings, compute lengths, and extract substrings using slicing. Experiment with trying to assign to a string index and interpret the immutability error.

## Common Misconceptions
- Forgetting that string indexing starts at 0, not 1.
- Trying to modify a character in-place in an immutable string.
- Confusing the string '5' with the integer 5 — they cannot be added arithmetically without conversion.

## Explainer

You already know how to store numbers and booleans in variables. A **string** is how programs store and work with text — anything from a single letter to an entire paragraph. When you write `name = "Alice"`, the variable `name` holds a sequence of five characters. Unlike a number, which is a single indivisible value, a string is structured: it has a first character, a second character, and so on, and you can access each one individually.

**Indexing** is how you reach into a string to get a specific character. The critical convention is that positions start at zero, not one. In the string `"Hello"`, `s[0]` is `"H"`, `s[1]` is `"e"`, and `s[4]` is `"o"`. This zero-based counting is universal across most programming languages and carries over to arrays and lists later. Think of the index as an offset from the beginning: the first character is zero steps from the start, the second is one step, and so on. The **length** of `"Hello"` is 5, but the last valid index is 4 — this off-by-one relationship is a constant source of bugs if you do not internalize it early.

**Immutability** is the property that surprises most beginners. In many languages (Python, Java, JavaScript), strings cannot be changed after creation. If you try `s[0] = "h"` to lowercase the first letter of `"Hello"`, you will get an error. Instead, you create a new string from pieces of the old one: `s = "h" + s[1:]` builds a brand-new string `"hello"` and reassigns the variable. Every string operation — concatenation, slicing, replacing — produces a new string rather than modifying the original. This design choice makes strings safer to pass around in programs because no function can silently alter a string you gave it.

One subtle but important distinction: the string `"5"` and the integer `5` are completely different values. The string is a character — it happens to look like a digit, but the computer treats it as text. You cannot add `"5" + 3` and get `8`; depending on the language you will either get an error or the nonsensical text `"53"`. Moving between string and numeric representations requires explicit type conversion, which bridges the gap between how humans read data (as text) and how programs compute with it (as typed values). Mastering this distinction early prevents an entire category of bugs that plague beginners.
