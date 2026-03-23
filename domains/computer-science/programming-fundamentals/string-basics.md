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
stage: formal-systems
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

## Questions

```yaml
- question: "In Python, a student runs: s = 'Hello'; s[0] = 'h'. What happens?"
  type: multiple-choice
  options:
    - "s becomes 'hello' — the first character is lowercased in place"
    - "s becomes 'hHello' — the character is inserted at position 0"
    - "A TypeError or similar error is raised — strings are immutable"
    - "Nothing happens — the assignment is silently ignored"
  answer: 2
  explanation: "Strings are immutable in Python, meaning you cannot change individual characters after the string is created. Attempting s[0] = 'h' raises a TypeError: 'str' object does not support item assignment. To achieve the effect, you must create a new string: s = 'h' + s[1:]. This immutability is a deliberate design choice — it makes strings safe to pass around since no function can silently alter a string you hand it."

- question: "The string s = 'Python' has length 6. What is the value of s[5]?"
  type: multiple-choice
  options:
    - "'o' — the fifth letter of Python"
    - "An IndexError — index 5 is out of range for a 6-character string"
    - "'n' — the last character, at index 5"
    - "'P' — index 5 counts 5 characters from the end"
  answer: 2
  explanation: "String indexing starts at 0, so a string of length 6 has valid indices 0 through 5. s[0]='P', s[1]='y', s[2]='t', s[3]='h', s[4]='o', s[5]='n'. The last valid index is always length minus 1. The off-by-one relationship between length (6) and last index (5) is a consistent source of bugs — if you try s[6], you get an IndexError. Think of the index as an offset from the start: the first character is 0 steps in, the last is 5 steps in."

- question: "In Python, every string operation that appears to modify a string actually creates a new string; the original string object is unchanged."
  type: true-false
  answer: true
  explanation: "String immutability means operations like concatenation, slicing, and case conversion always produce new string objects. If you write s = s.upper(), the variable s is reassigned to point to a new uppercase string — the original string object still exists unchanged in memory (until garbage collected). This matters when you pass strings to functions: a function cannot alter the original string, only return a new one. Immutability makes strings reliable across multiple references to the same object."

- question: "In Python, the string '42' and the integer 42 can be used interchangeably in arithmetic expressions."
  type: true-false
  answer: false
  explanation: "The string '42' and the integer 42 are completely different types. Attempting '42' + 3 raises a TypeError in Python because you cannot add a string and an integer directly. In some languages (like JavaScript), this produces '423' through implicit type coercion — a different problem entirely. Explicit conversion is always required: int('42') converts the string to 42, or str(42) converts the integer to '42'. This distinction is critical whenever reading numeric data from files, user input, or APIs, which always arrive as strings."

- question: "Explain why string immutability is a useful design choice, not just a limitation. What problems would arise if strings could be modified in place?"
  type: short-answer
  answer: "Immutability makes strings safe to share across multiple parts of a program. If strings were mutable, passing a string to a function would risk that function silently altering it — a hard-to-debug side effect. With immutability, you can safely pass a string anywhere knowing it cannot be changed. Immutability also enables optimizations like string interning (sharing a single copy of equal strings) and makes strings usable as dictionary keys (which require objects that don't change)."
  explanation: "Languages with mutable strings (like C's character arrays) require defensive copying whenever a string is passed to untrusted code. Python's immutability eliminates this class of bug entirely: every operation produces a new string, so the original is always intact. The cost is that building strings in a loop through concatenation is inefficient (each + creates a new object), which is why Python provides ''.join() for that pattern. Understanding immutability also prepares you for the same concept appearing in other data types, like tuples versus lists."
```

## Explainer

You already know how to store numbers and booleans in variables. A **string** is how programs store and work with text — anything from a single letter to an entire paragraph. When you write `name = "Alice"`, the variable `name` holds a sequence of five characters. Unlike a number, which is a single indivisible value, a string is structured: it has a first character, a second character, and so on, and you can access each one individually.

**Indexing** is how you reach into a string to get a specific character. The critical convention is that positions start at zero, not one. In the string `"Hello"`, `s[0]` is `"H"`, `s[1]` is `"e"`, and `s[4]` is `"o"`. This zero-based counting is universal across most programming languages and carries over to arrays and lists later. Think of the index as an offset from the beginning: the first character is zero steps from the start, the second is one step, and so on. The **length** of `"Hello"` is 5, but the last valid index is 4 — this off-by-one relationship is a constant source of bugs if you do not internalize it early.

**Immutability** is the property that surprises most beginners. In many languages (Python, Java, JavaScript), strings cannot be changed after creation. If you try `s[0] = "h"` to lowercase the first letter of `"Hello"`, you will get an error. Instead, you create a new string from pieces of the old one: `s = "h" + s[1:]` builds a brand-new string `"hello"` and reassigns the variable. Every string operation — concatenation, slicing, replacing — produces a new string rather than modifying the original. This design choice makes strings safer to pass around in programs because no function can silently alter a string you gave it.

One subtle but important distinction: the string `"5"` and the integer `5` are completely different values. The string is a character — it happens to look like a digit, but the computer treats it as text. You cannot add `"5" + 3` and get `8`; depending on the language you will either get an error or the nonsensical text `"53"`. Moving between string and numeric representations requires explicit type conversion, which bridges the gap between how humans read data (as text) and how programs compute with it (as typed values). Mastering this distinction early prevents an entire category of bugs that plague beginners.
