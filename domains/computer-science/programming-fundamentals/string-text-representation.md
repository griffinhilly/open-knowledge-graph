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

## Explainer

From your work with memory and data storage, you know that computers store everything as binary numbers. **Strings** are how programming languages represent text on top of that binary foundation. A string is a sequence of **characters** — letters, digits, punctuation, spaces — stored consecutively in memory. When you write `"hello"` in code, the language creates a string object containing five characters, each mapped to a numeric code (such as ASCII or Unicode) that the computer stores internally. The quotation marks tell the language "treat this as text, not as a variable name or a number."

The most fundamental string operations build directly on the idea of sequences. **Indexing** lets you access a single character by its position: `"hello"[0]` gives `'h'` (most languages start counting at zero). **Length** tells you how many characters the string contains. **Concatenation** joins two strings end-to-end: `"hello" + " world"` produces `"hello world"`. These three operations — access an element, measure the sequence, combine sequences — recur throughout programming whenever you work with ordered collections of data.

A critical property of strings in most languages is **immutability**: once a string is created, its contents cannot be changed in place. If you want to "modify" a string — say, replace a letter or convert to uppercase — the language creates an entirely new string with the changes applied. The original remains untouched. This might seem wasteful, but immutability prevents a whole class of bugs where one part of your program accidentally alters text that another part depends on. When you concatenate strings repeatedly in a loop, each concatenation creates a new string object, which is why languages offer more efficient alternatives (like string builders) for heavy text assembly.

Understanding that strings are not numbers — even when they look like numbers — prevents a common class of errors. The string `"42"` and the integer `42` are fundamentally different values stored in different ways. Adding the integer 1 to the integer 42 gives 43, but adding the string "1" to the string "42" might give "142" (concatenation) or cause an error, depending on the language. Moving between strings and numbers requires explicit **type conversion**, which you will explore as you progress to string operations and input/output.
