---
id: string-text-representation
title: Strings and Text Representation
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: memory-and-data-storage
  type: hard
builds-toward:
- string-operations
- basic-input-output
tags:
- types
- strings
- text
stage: abstract-reasoning
status: draft
---

# Strings and Text Representation

## Core Idea
Strings represent sequences of characters and are a fundamental data type for handling text. Strings are immutable in many languages and support operations like concatenation, indexing, and length measurement.

## How It's Best Learned
Create strings, index into them, concatenate them, and measure their length. Print strings to see text output.

## Common Misconceptions
- Strings are mutable (in most languages they are immutable; modifications create new strings).
- A string 'hello' and a number 123 can be directly compared or added without conversion.

## Questions

```yaml
- question: "In Python, a programmer writes: name = 'Alice' followed by name[0] = 'B', intending to change the first character. What happens?"
  type: multiple-choice
  options:
    - "The string becomes 'Blice' — the character is changed in place"
    - "A new string 'Blice' is silently created and name is updated"
    - "An error occurs because strings are immutable and cannot be modified by index assignment"
    - "Nothing changes — the assignment is ignored"
  answer: 2
  explanation: "Strings are immutable in Python. You cannot change a character in place using index assignment — Python raises a TypeError. This is a direct consequence of immutability: once a string object is created, its contents are fixed. To create a modified version, you must build a new string (e.g., 'B' + name[1:]). Immutability prevents one part of a program from accidentally altering a string that other parts rely on."

- question: "What is the result of evaluating '3' + '4' in Python?"
  type: multiple-choice
  options:
    - "7 — Python adds the numeric values"
    - "7.0 — Python converts both to floats before adding"
    - "'34' — Python concatenates the two strings"
    - "An error — you cannot use + with strings"
  answer: 2
  explanation: "'3' and '4' are strings, not integers. The + operator on strings performs concatenation, joining them end-to-end: '34'. This is fundamentally different from integer addition (3 + 4 = 7). The string '3' stores the text character '3'; the integer 3 stores the numeric value three. They are different types with different behaviors. To get numeric addition, you must first convert: int('3') + int('4') = 7."

- question: "When you call a method like .upper() on a string in Python, the original string variable is modified in place to contain the uppercase version."
  type: true-false
  answer: false
  explanation: "Strings are immutable — no method modifies the original string. Calling 'hello'.upper() returns a new string 'HELLO'; the original 'hello' is unchanged. To use the result, you must assign it: name = name.upper(). Forgetting this is a common source of bugs where a programmer calls a string method expecting modification but then wonders why the variable hasn't changed."

- question: "The string '99' and the integer 99 are different values that cannot be directly added together in most programming languages without type conversion."
  type: true-false
  answer: true
  explanation: "Even though '99' looks like a number, it is stored as a sequence of two text characters ('9' and '9'), not as the numeric value ninety-nine. Adding the integer 1 to the integer 99 gives 100. But adding the integer 1 to the string '99' will either raise a TypeError or produce unexpected results depending on the language. Explicit type conversion — int('99') or str(99) — is required to move between the two representations."

- question: "Why does string immutability prevent a class of bugs, even though it may seem less convenient than mutable strings?"
  type: short-answer
  answer: "Immutability means that once a string is created, no code can change its contents. If strings were mutable, multiple variables could reference the same string object, and a change made through one variable would silently affect all other references to that object. Immutability guarantees that a string value stays constant wherever it is used, eliminating a whole class of 'action at a distance' bugs where one part of the program unexpectedly alters data another part depends on."
  explanation: "This is the core design rationale for immutability. The trade-off is efficiency: repeated concatenation creates many short-lived string objects. Languages address this with dedicated tools (StringBuilder in Java, join() in Python) for cases where heavy text assembly is needed. But the safety guarantees of immutability outweigh the inconvenience for most use cases."
```

## Explainer

From your work with memory and data storage, you know that computers store everything as binary numbers. **Strings** are how programming languages represent text on top of that binary foundation. A string is a sequence of **characters** — letters, digits, punctuation, spaces — stored consecutively in memory. When you write `"hello"` in code, the language creates a string object containing five characters, each mapped to a numeric code (such as ASCII or Unicode) that the computer stores internally. The quotation marks tell the language "treat this as text, not as a variable name or a number."

The most fundamental string operations build directly on the idea of sequences. **Indexing** lets you access a single character by its position: `"hello"[0]` gives `'h'` (most languages start counting at zero). **Length** tells you how many characters the string contains. **Concatenation** joins two strings end-to-end: `"hello" + " world"` produces `"hello world"`. These three operations — access an element, measure the sequence, combine sequences — recur throughout programming whenever you work with ordered collections of data.

A critical property of strings in most languages is **immutability**: once a string is created, its contents cannot be changed in place. If you want to "modify" a string — say, replace a letter or convert to uppercase — the language creates an entirely new string with the changes applied. The original remains untouched. This might seem wasteful, but immutability prevents a whole class of bugs where one part of your program accidentally alters text that another part depends on. When you concatenate strings repeatedly in a loop, each concatenation creates a new string object, which is why languages offer more efficient alternatives (like string builders) for heavy text assembly.

Understanding that strings are not numbers — even when they look like numbers — prevents a common class of errors. The string `"42"` and the integer `42` are fundamentally different values stored in different ways. Adding the integer 1 to the integer 42 gives 43, but adding the string "1" to the string "42" might give "142" (concatenation) or cause an error, depending on the language. Moving between strings and numbers requires explicit **type conversion**, which you will explore as you progress to string operations and input/output.
