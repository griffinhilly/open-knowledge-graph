---
id: code-comments-and-style
title: Code Comments and Style
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: hello-world-your-first-program
  type: soft
builds-toward:
- function-design-and-contracts
tags:
- documentation
- readability
- best-practices
stage: abstract-reasoning
status: draft
---

# Code Comments and Style

## Core Idea
Comments explain why code exists, not what it does (the code itself shows what). Consistent style—indentation, naming, spacing—makes code readable for yourself later and for others. Good comments and style are markers of professional programming.

## How It's Best Learned
Read others' code and notice which comments help you understand intent; practice re-reading your own code after a week and revising unclear sections.

## Common Misconceptions
That every line needs a comment; actually, clear code with well-named variables needs fewer comments. Comments should explain intent, not restate the code.

## Explainer

Now that you have written your first programs, you have likely noticed that code you wrote last week can look confusing when you return to it. Comments and consistent style are the tools that prevent this — they make code readable not just to the computer, but to the human who will maintain it, which is most often your future self.

A **comment** is text that the language ignores during execution. In Python, anything after a `#` on a line is a comment; in JavaScript and C-family languages, `//` marks a single-line comment and `/* ... */` wraps multi-line comments. The most important rule about comments is that they should explain **why**, not **what**. A comment like `x = x + 1  # increment x` is worse than useless — it restates the obvious and adds visual noise. A comment like `x = x + 1  # compensate for zero-based index when displaying to user` tells the reader something the code alone cannot. Good comments capture intent, document edge cases, warn about non-obvious behavior, and explain *why* a particular approach was chosen over an alternative.

**Style** encompasses everything about how code is formatted: indentation width, where braces go, how variables and functions are named, how blank lines separate logical sections. None of these choices affect what the program does, but they profoundly affect how quickly someone can read and understand it. Most languages have community conventions — Python's PEP 8 recommends 4-space indentation and snake_case for variable names; JavaScript communities often use camelCase and 2-space indentation. The specific convention matters less than **consistency**: mixing tabs and spaces, or alternating between `myVariable` and `my_variable` in the same file, forces the reader to spend mental energy on formatting instead of logic.

A practical guideline is to make your code as self-documenting as possible through clear naming, then add comments only where the code cannot speak for itself. A function named `calculate_shipping_cost` with parameters `weight` and `destination` needs far fewer comments than one named `calc` with parameters `w` and `d`. When you find yourself writing a long comment to explain a complex block, consider whether refactoring the code — extracting a well-named function, renaming a variable, or simplifying the logic — would eliminate the need for the comment entirely. The best code reads like well-structured prose; comments fill in the gaps where the prose alone is insufficient.
