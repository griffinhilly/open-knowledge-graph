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

## Questions

```yaml
- question: "In Python, a student writes s = 'hello' and then tries s[0] = 'H' expecting to change the first letter. What happens?"
  type: multiple-choice
  options:
    - "The string becomes 'Hello' because indexing supports both reading and writing characters"
    - "A TypeError is raised — strings are immutable and cannot be modified in place via index assignment"
    - "The operation silently fails and s remains 'hello' with no error"
    - "It works because Python strings behave like lists for single-character assignments"
  answer: 1
  explanation: "String immutability means you can read characters by index but cannot write to them. s[0] = 'H' raises TypeError: 'str' object does not support item assignment. To produce 'Hello', you must create a new string: s = 'H' + s[1:]. This immutability is a deliberate design choice — it prevents one part of a program from unexpectedly modifying a string that another part is still using."

- question: "What is the correct index to access the last character of the string 'python' (which has 6 characters)?"
  type: multiple-choice
  options:
    - "6 — because there are 6 characters in the string"
    - "5 — because indexing starts at 0, so a 6-character string uses positions 0 through 5"
    - "7 — because you need to go one beyond the length to reach the end"
    - "-1 — this is the only valid way to access the last character"
  answer: 1
  explanation: "Zero-based indexing means the first character is at index 0 and the last character is at index length - 1. For 'python' (length 6), the last character 'n' is at index 5. Index 6 would be out of bounds and raise an IndexError. (Note: -1 also works in Python as a convenient shorthand for the last character, but index 5 is the fundamental answer based on understanding how zero-based indexing works.)"

- question: "In Python, the expression 'hello' + ' world' creates a brand-new string rather than modifying either of the original strings."
  type: true-false
  answer: true
  explanation: "String concatenation in Python (and most languages with immutable strings) creates a new string object containing all the characters of both originals. Neither 'hello' nor ' world' is changed — a third string 'hello world' is created. This is a direct consequence of immutability: since strings cannot be modified, the only way to combine them is to create something new. Building a long string by concatenating inside a loop is slow precisely because each step allocates a new string and copies all previous characters."

- question: "Because strings can be indexed like arrays to read individual characters, you can also assign to string indexes (e.g., s[0] = 'H') to change individual characters, just as you would with a list."
  type: true-false
  answer: false
  explanation: "Strings support index access for reading but not for writing. s[0] returns the first character, but s[0] = 'H' raises a TypeError. This is the immutability principle: once created, a string's characters cannot be changed in place. Lists are mutable and do support index assignment. The behavioral difference between strings and lists on this operation is one of the first and most important distinctions in Python programming."

- question: "Why are strings immutable in languages like Python and Java, and what is the practical consequence when you want to 'modify' a string?"
  type: short-answer
  answer: "Strings are immutable to prevent bugs where one part of a program unexpectedly changes a string that another part is still using — a class of aliasing bugs that mutability makes easy to introduce. The practical consequence is that every operation that appears to 'modify' a string actually creates a new string: concatenation, slicing, replacing, converting case. The original is untouched. This means building up a long string character-by-character in a loop is inefficient — each step copies all prior characters — so languages provide more efficient alternatives like join() or StringBuilder."
  explanation: "Immutability is a trade-off: it adds safety and makes strings usable as dictionary keys (since their hash can't change), at the cost of making modification patterns slightly more verbose and making naive repeated concatenation expensive."
```

## Explainer

You already know that text in a program is represented as a string — a value enclosed in quotes. Now it's time to look inside that value and see its structure. A string is not a single indivisible thing; it is a **sequence of characters** laid out in order, much like how an array is a sequence of numbers. The string `"hello"` contains five characters: `'h'`, `'e'`, `'l'`, `'l'`, `'o'`, each sitting at a specific position.

You can access individual characters by their position using **indexing**. In most languages, positions start at 0, so `"hello"[0]` gives `'h'` and `"hello"[4]` gives `'o'`. The **length** of a string is the total number of characters — `"hello"` has length 5, while `""` (the empty string) has length 0. Since strings are sequences, you can iterate through them with loops just as you would iterate through a list: `for char in "hello"` visits each character in order. This connection between strings and sequences means that many techniques you already know from working with collections apply directly to strings.

One crucial property to understand early is **immutability**. In languages like Python and Java, strings cannot be changed after they are created. If you write `s = "hello"` and then want to change the first letter, you cannot do `s[0] = "H"` — that will raise an error. Instead, you create a new string: `s = "H" + s[1:]`. This feels restrictive at first, but immutability prevents a whole class of bugs where one part of a program unexpectedly modifies a string that another part is still using. Operations like concatenation, slicing, and replacing all produce new strings rather than modifying the original.

Understanding strings as character sequences also reveals why certain operations have the costs they do. Checking the length is typically instant because the length is stored alongside the string. But concatenating two strings means creating a brand-new string and copying every character from both originals into it. Building up a long string one character at a time inside a loop can be surprisingly slow for this reason — a pattern you'll learn to optimize as you advance.
