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
stage: abstract-reasoning
status: draft
---

# Strings: Introduction and Representation

## Core Idea
Strings are sequences of characters representing text. In most languages, strings are immutable (cannot be changed after creation). Strings are indexed like arrays, where each character has a position.

## Explainer

You have already worked with primitive types like integers, floats, and booleans — values that represent single numbers or true/false conditions. **Strings** are the data type for text. A string is a sequence of characters enclosed in quotes: `"Hello, world!"` or `'Python'`. Each character in the string — letters, digits, spaces, punctuation — occupies a position, making a string behave much like an ordered collection.

Because strings are sequences, you can access individual characters using the same indexing notation you would use with arrays. In `greeting = "Hello"`, the expression `greeting[0]` returns `"H"`, `greeting[1]` returns `"e"`, and so on. The length of a string — retrieved with `len(greeting)` in Python or `.length` in other languages — tells you how many characters it contains. This means the same zero-based indexing logic applies: the last character is at index `length - 1`.

A key property of strings in most languages is **immutability**: once a string is created, its contents cannot be changed in place. You cannot write `greeting[0] = "J"` to turn `"Hello"` into `"Jello"`. Instead, you create a new string with the desired content — for example, `greeting = "J" + greeting[1:]`. This may seem restrictive at first, but immutability simplifies how the language manages memory and prevents a whole category of bugs where shared references to the same string accidentally modify each other.

Strings bridge the gap between human-readable text and machine-processable data. User input from the keyboard arrives as a string. File contents are read as strings. Web pages are transmitted as strings. Nearly every program you write will create, inspect, or transform strings in some way. Understanding that a string is fundamentally a sequence of characters — with a defined length, indexable positions, and (usually) immutable contents — gives you the mental model you need for the string operations you will learn next.
