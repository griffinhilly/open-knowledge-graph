---
id: programming-fundamentals-recursion-basics
title: 'Recursion: Fundamentals'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-function-definition
  type: hard
tags:
- recursion
- functions
- self-call
stage: abstract-reasoning
status: draft
---

# Recursion: Fundamentals

## Core Idea
Recursion occurs when a function calls itself. A recursive function must have a base case (where recursion stops) and a recursive case (where it calls itself with simpler input). Recursion naturally expresses self-similar problems.

## Explainer

You already know how to define a function and call it. Recursion adds one surprising twist: a function can call *itself*. This sounds circular — like a dictionary defining a word using that same word — but it works because each self-call operates on a smaller, simpler version of the problem until you hit a case so simple it needs no further calls.

Every recursive function has exactly two parts. The **base case** is the trivial scenario where you can return an answer immediately without calling yourself again. The **recursive case** is where you break the problem into a smaller piece and call yourself on that piece. Take factorial as an example: `factorial(1)` is 1 — that's the base case. `factorial(5)` is `5 * factorial(4)`, which is `5 * 4 * factorial(3)`, and so on, until you reach `factorial(1)` and the chain of calls starts returning answers back up. If you forget the base case, the function calls itself forever until the program crashes — this is the recursive equivalent of an infinite loop.

The key insight is that recursion works on problems with **self-similar structure** — problems where a smaller version of the same problem appears inside the original. A folder contains files and other folders. A sentence can contain clauses that are themselves sentences. A list can be split into a first element and "the rest of the list," where "the rest" is itself a list. Whenever you notice this nesting pattern, recursion is a natural fit. You handle one piece, then trust the recursive call to handle the rest — this "trust the recursion" mindset is the hardest part for beginners, but once it clicks, you'll see recursive structure everywhere.

Not every problem is best solved with recursion. Simple counting or accumulation loops are clearer with `for` or `while`. But for tree-like structures, nested data, and divide-and-conquer algorithms, recursion produces code that mirrors the problem's own structure, making it both elegant and easier to prove correct.
