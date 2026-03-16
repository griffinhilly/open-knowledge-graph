---
id: strings-as-character-sequences
title: Strings as Character Sequences
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: string-text-representation
  type: hard
builds-toward:
- string-operations
tags:
- strings
- sequences
- characters
stage: abstract-reasoning
status: draft
---

# Strings as Character Sequences

## Core Idea
A string is a sequence of characters. Strings can be indexed like arrays to access individual characters. The length of a string is the number of characters it contains. Strings are immutable in many languages, so operations create new strings.

## How It's Best Learned
Index into strings to get characters. Measure string lengths. Iterate through strings with loops. Attempt to modify strings and observe immutability.

## Common Misconceptions
- Strings are mutable (in most modern languages, strings are immutable; modifications create new strings).
- A string is a character (a string is a sequence; a single character is a separate type).

## Explainer

You already know that text in a program is represented as a string — a value enclosed in quotes. Now it's time to look inside that value and see its structure. A string is not a single indivisible thing; it is a **sequence of characters** laid out in order, much like how an array is a sequence of numbers. The string `"hello"` contains five characters: `'h'`, `'e'`, `'l'`, `'l'`, `'o'`, each sitting at a specific position.

You can access individual characters by their position using **indexing**. In most languages, positions start at 0, so `"hello"[0]` gives `'h'` and `"hello"[4]` gives `'o'`. The **length** of a string is the total number of characters — `"hello"` has length 5, while `""` (the empty string) has length 0. Since strings are sequences, you can iterate through them with loops just as you would iterate through a list: `for char in "hello"` visits each character in order. This connection between strings and sequences means that many techniques you already know from working with collections apply directly to strings.

One crucial property to understand early is **immutability**. In languages like Python and Java, strings cannot be changed after they are created. If you write `s = "hello"` and then want to change the first letter, you cannot do `s[0] = "H"` — that will raise an error. Instead, you create a new string: `s = "H" + s[1:]`. This feels restrictive at first, but immutability prevents a whole class of bugs where one part of a program unexpectedly modifies a string that another part is still using. Operations like concatenation, slicing, and replacing all produce new strings rather than modifying the original.

Understanding strings as character sequences also reveals why certain operations have the costs they do. Checking the length is typically instant because the length is stored alongside the string. But concatenating two strings means creating a brand-new string and copying every character from both originals into it. Building up a long string one character at a time inside a loop can be surprisingly slow for this reason — a pattern you'll learn to optimize as you advance.
