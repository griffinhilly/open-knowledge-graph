---
id: character-and-string-basics
title: Character and String Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: primitive-types-integers-floats-strings
  type: hard
builds-toward:
- string-basics
- string-operations
tags:
- strings
- text
- characters
stage: abstract-reasoning
status: draft
---

# Character and String Basics

## Core Idea
Strings are sequences of characters. Characters are represented as numbers (ASCII, Unicode) under the hood. Strings are immutable in many languages—operations on strings create new strings rather than modifying existing ones.

## How It's Best Learned
Print individual characters from a string by index; practice concatenation and simple string methods; look up ASCII values to understand the character-number relationship.

## Common Misconceptions
That strings can be modified in-place; that character codes are universal (they're standardized as ASCII/Unicode but implementations vary); that empty string '' is the same as whitespace ' '.

## Explainer

You already know from working with primitive types that strings are one of the basic data types alongside integers and floats. But strings are different in an important way: while an integer is a single value, a **string is a sequence of characters** — an ordered collection of individual letters, digits, symbols, or spaces. The string `"Hello"` is not one indivisible thing; it is five characters: `'H'`, `'e'`, `'l'`, `'l'`, `'o'`, each stored at a specific position (index) starting from 0.

Under the hood, every character is represented as a number. The **ASCII** standard assigns numbers 0–127 to common characters: `'A'` is 65, `'a'` is 97, `'0'` (the digit) is 48, and a space is 32. This is why you can compare characters — when your code checks if `'a' < 'b'`, it is really comparing 97 < 98. **Unicode** extends this to over 100,000 characters covering every writing system, emoji, and symbol. You do not need to memorize codes, but understanding that characters are numbers explains behaviors that otherwise seem magical, like why sorting strings puts uppercase before lowercase (uppercase letters have lower ASCII values).

Most languages let you access individual characters by index — `"Hello"[0]` gives `'H'`, `"Hello"[4]` gives `'o'`. You can loop through a string character by character, check its length, and combine strings using **concatenation** (the `+` operator in many languages: `"Hello" + " " + "World"` produces `"Hello World"`). These operations feel natural, but there is a critical subtlety: in many languages including Python and Java, strings are **immutable**. When you "change" a string, you are actually creating an entirely new string. The expression `greeting = "Hello"` followed by `greeting = greeting + "!"` does not modify the original `"Hello"` — it creates a new string `"Hello!"` and points the variable at it. The old string still exists in memory until it is garbage collected.

Why does immutability matter? Because it means string operations that seem cheap can be expensive. Concatenating one character at a time inside a loop creates a new string object on every iteration. For building strings incrementally, languages provide mutable alternatives like `StringBuilder` in Java or joining a list in Python. Understanding the character-as-number foundation and the immutability constraint gives you the mental model to use strings effectively rather than fighting against how they actually work.
