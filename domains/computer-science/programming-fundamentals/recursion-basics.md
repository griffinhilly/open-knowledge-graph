---
id: recursion-basics
title: Recursion Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: return-values
  type: hard
- id: variable-scope
  type: hard
- id: while-loops
  type: soft
- id: mathematical-induction
  type: soft
builds-toward:
- algorithm-design-basics
tags:
- recursion
- base case
- call stack
- self-reference
- induction
stage: abstract-reasoning
status: validated
---

# Recursion Basics

## Core Idea
A recursive function is one that calls itself as part of its own definition. Every recursive solution requires a base case (a condition that terminates the recursion) and a recursive case (a call on a smaller or simpler version of the problem). Each function call creates a new stack frame with its own local variables; the call stack grows with each recursive call and shrinks as calls return. Many problems — especially those with naturally recursive structure like trees or mathematical sequences — are elegantly expressed recursively.

## How It's Best Learned
Start with factorial and Fibonacci, tracing the call tree by hand. Then implement recursive sum of a list, string reversal, and binary search. Always identify the base case first before writing the recursive case.

## Common Misconceptions
- Forgetting the base case, causing infinite recursion (stack overflow).
- Not returning the result of the recursive call, so the result is lost.
- Thinking recursion is always more efficient than iteration — it often uses more memory due to stack frames.

## Questions

```yaml
- question: "What happens when a recursive function is called without a valid base case?"
  type: multiple-choice
  options:
    - "The function returns None automatically"
    - "The function runs once and exits"
    - "The call stack grows without bound until the program crashes with a stack overflow"
    - "The compiler detects the infinite loop and refuses to run the code"
  answer: 2
  explanation: "Without a base case, each call to the function spawns another call, which spawns another — the call stack accumulates frames indefinitely. Most environments impose a stack size limit, and when it is exceeded, the program crashes with a stack overflow error (or RecursionError in Python). The function does not self-terminate, and most languages do not statically detect this at compile time."

- question: "A recursive solution to a problem is always faster and uses less memory than an equivalent iterative solution."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Each recursive call creates a new stack frame with its own local variables, consuming memory proportional to the call depth. An iterative loop reuses the same memory. For deep recursions (e.g., large n in factorial), this overhead is substantial. Some algorithms (like tree traversals) are more naturally expressed recursively, but efficiency claims require analysis — recursion is not inherently better."

- question: "Explain what the call stack is doing during a recursive computation, and why each call needs its own stack frame."
  type: short-answer
  answer: "The call stack tracks the state of each active function call. Each recursive call gets its own stack frame containing its local variables and the return address. This is necessary because each call is an independent invocation working on a different subproblem — it must remember its own state while waiting for the deeper call to return."
  explanation: "This is the key to understanding why recursion works at all. When factorial(5) calls factorial(4), the runtime can't forget that factorial(5) is in progress — it needs to multiply the result by 5 when factorial(4) returns. The stack frame preserves this context. Without separate frames, recursive calls would clobber each other's variables. Understanding the stack also explains why forgetting to return the recursive call's result is such a common bug: the result is computed correctly but then discarded."
```

## Explainer

You already know that functions can call other functions — that is how you have been building programs. Recursion takes this one step further: a function can call *itself*. At first this seems paradoxical, but it is one of the most powerful ideas in programming.

The key insight is that many problems have a self-similar structure. The factorial of 5 (written 5!) equals 5 × 4!. And 4! = 4 × 3!. And so on. Once you see this, a recursive definition writes itself: `factorial(n) = n * factorial(n-1)`. But this chain has to stop somewhere — that is the base case. For factorial, `factorial(0) = 1` by definition. Without the base case, the chain never terminates and you get infinite recursion. Writing the base case *first*, before the recursive case, is the discipline that keeps you out of trouble.

When a recursive function runs, the call stack is doing the real work. Each call to `factorial(n)` creates a new stack frame — a small block of memory holding n and the return address. When `factorial(5)` calls `factorial(4)`, the first frame pauses and waits; when `factorial(4)` calls `factorial(3)`, another frame is added. The stack grows to depth n, then unwinds as each call returns its result up to the caller. This is why variable scope matters: each frame has its own copy of `n`, and there is no confusion between them. It is also why deep recursion can be expensive — you are allocating a frame for every level.

A common bug is calling the recursive function but not returning its result: writing `factorial(n-1)` instead of `return factorial(n-1) * n`. The deeper call runs correctly and computes the right answer, but that answer is thrown away because you never returned it. Always check that your recursive case both calls the function *and* uses the return value.

Recursion is not always the right tool. Simple loops — adding up a list, iterating over a string — are almost always clearer and more memory-efficient as iteration. Where recursion shines is on problems with naturally recursive structure: tree traversals, divide-and-conquer algorithms, parsing nested expressions. If you find yourself writing a loop and keeping an explicit stack to track state, that is a signal that recursion might be the cleaner solution. Over time, you will develop judgment about which to reach for.
