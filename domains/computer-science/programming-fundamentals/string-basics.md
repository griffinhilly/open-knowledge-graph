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
status: draft
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
