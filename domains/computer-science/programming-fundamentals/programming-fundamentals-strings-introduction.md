---
id: programming-fundamentals-strings-introduction
title: 'Strings: Introduction and Representation'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-primitive-types
  type: hard
builds-toward:
- programming-fundamentals-string-operations
tags:
- strings
- text
- characters
stage: formal-systems
status: draft
---

# Strings: Introduction and Representation

## Core Idea
Strings are sequences of characters representing text. In most languages, strings are immutable (cannot be changed after creation). Strings are indexed like arrays, where each character has a position.

## Questions

```yaml
- question: "Given `word = \"Python\"`, what does `word[0]` evaluate to?"
  type: multiple-choice
  options:
    - "\"P\" — the first character, at index 0"
    - "\"y\" — the second character, since index 0 is a placeholder"
    - "\"n\" — the last character"
    - "An error — strings cannot be accessed by index"
  answer: 0
  explanation: "Strings use zero-based indexing, consistent with arrays in most languages. Index 0 refers to the first character. So `word[0]` is `\"P\"`, `word[1]` is `\"y\"`, and `word[5]` is `\"n\"`. Zero-based indexing applies uniformly to all sequences and will carry through all future work with lists, arrays, and strings."

- question: "A student writes `name = \"Alice\"` and then tries `name[0] = \"B\"` to change it to \"Blice\". What happens in most languages?"
  type: multiple-choice
  options:
    - "The string is modified in place to become \"Blice\""
    - "An error occurs because strings are immutable and individual characters cannot be changed"
    - "A new string \"Blice\" is automatically created and `name` now refers to it"
    - "Nothing happens — the assignment to an index is silently ignored"
  answer: 1
  explanation: "Strings are immutable in most languages: once created, their contents cannot be changed in place. Attempting to assign to an index (`name[0] = \"B\"`) raises an error. To achieve the desired result, you must create a new string: `name = \"B\" + name[1:]`. Immutability is a deliberate design choice that simplifies memory management and prevents bugs from shared references unexpectedly modifying each other."

- question: "A string is fundamentally different from an array — strings cannot be indexed or have their length measured the way arrays can."
  type: true-false
  answer: false
  explanation: "Strings behave exactly like ordered sequences and support the same indexing notation as arrays. `\"Hello\"[0]` gives `\"H\"`, `\"Hello\"[4]` gives `\"o\"`, and `len(\"Hello\")` returns 5. Strings are not a mysterious special type — they are sequences of characters, and all sequence-based reasoning (indexing, length, position) applies directly. This mental model is essential for the string operations covered in the next topic."

- question: "Because strings are immutable, any operation that appears to modify a string actually creates a new string in memory."
  type: true-false
  answer: true
  explanation: "Immutability means the original string object cannot be changed. When you write `greeting = greeting + \"!\"`, Python does not alter the existing string `\"Hello\"` — it creates a new string `\"Hello!\"` and rebinds the variable to point to it. The old string remains unchanged and will be garbage-collected if nothing else references it. This has performance implications for building strings in a loop, which is why languages provide more efficient alternatives like `join()`."

- question: "Why are strings immutable in most programming languages, and what practical consequence does immutability have for modifying text in a program?"
  type: short-answer
  answer: "Immutability simplifies memory management and prevents bugs caused by shared references: if two variables point to the same string, neither can accidentally modify the other's data. The practical consequence is that you cannot change a string in place — to modify text, you must create a new string with the desired content using concatenation or slicing, then rebind the variable to the new string."
  explanation: "Immutability trades flexibility for safety and predictability. Mutable strings would allow bugs where modifying a string through one variable unexpectedly changes another variable pointing to the same object. The cost is that building strings incrementally requires creating many intermediate objects, which is why languages provide efficient alternatives. Understanding this tradeoff prepares you for the broader distinction between mutable and immutable types throughout programming."
```

## Explainer

You have already worked with primitive types like integers, floats, and booleans — values that represent single numbers or true/false conditions. **Strings** are the data type for text. A string is a sequence of characters enclosed in quotes: `"Hello, world!"` or `'Python'`. Each character in the string — letters, digits, spaces, punctuation — occupies a position, making a string behave much like an ordered collection.

Because strings are sequences, you can access individual characters using the same indexing notation you would use with arrays. In `greeting = "Hello"`, the expression `greeting[0]` returns `"H"`, `greeting[1]` returns `"e"`, and so on. The length of a string — retrieved with `len(greeting)` in Python or `.length` in other languages — tells you how many characters it contains. This means the same zero-based indexing logic applies: the last character is at index `length - 1`.

A key property of strings in most languages is **immutability**: once a string is created, its contents cannot be changed in place. You cannot write `greeting[0] = "J"` to turn `"Hello"` into `"Jello"`. Instead, you create a new string with the desired content — for example, `greeting = "J" + greeting[1:]`. This may seem restrictive at first, but immutability simplifies how the language manages memory and prevents a whole category of bugs where shared references to the same string accidentally modify each other.

Strings bridge the gap between human-readable text and machine-processable data. User input from the keyboard arrives as a string. File contents are read as strings. Web pages are transmitted as strings. Nearly every program you write will create, inspect, or transform strings in some way. Understanding that a string is fundamentally a sequence of characters — with a defined length, indexable positions, and (usually) immutable contents — gives you the mental model you need for the string operations you will learn next.
