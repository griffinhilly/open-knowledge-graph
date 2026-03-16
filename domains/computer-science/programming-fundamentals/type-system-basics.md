---
id: type-system-basics
title: Type Systems and Type Safety
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: integer-and-floating-point-types
  type: hard
- id: boolean-type-and-truth-values
  type: hard
- id: string-text-representation
  type: hard
builds-toward:
- type-conversion-casting
tags:
- types
- type-safety
- systems
stage: abstract-reasoning
status: draft
---

# Type Systems and Type Safety

## Core Idea
A type system defines what operations are valid on different data types. Type checking (compile-time or runtime) prevents invalid operations like adding a string and an integer, catching errors early and ensuring program correctness.

## How It's Best Learned
Try invalid operations (e.g., string + number) and observe type errors. Explore type checking in your language.

## Common Misconceptions
- Type safety is only about compile-time errors (runtime type checking also provides safety).
- All languages have static type checking (some use dynamic typing).

## Explainer

You have already worked with integers, floats, booleans, and strings as separate kinds of data. A **type system** is the set of rules a programming language uses to keep track of which kind of data each value is and what operations make sense for it. Adding two integers makes sense. Adding two strings (concatenation) makes sense. But adding an integer to a string — what would that even mean? Should `"hello" + 5` produce `"hello5"`, or `"hello"` shifted by 5, or an error? Different languages answer differently, and the type system is what enforces whatever answer the language designers chose.

**Type checking** is the mechanism that enforces these rules, and it comes in two major flavors. In **statically typed** languages like Java, C, or TypeScript, types are checked before the program runs — at compile time. If you try to assign a string to a variable declared as an integer, the compiler refuses to build your program. You catch the mistake before anyone runs the code. In **dynamically typed** languages like Python or JavaScript, types are checked while the program is running — at runtime. The code will start executing, and only when it reaches the problematic operation does it throw a type error. Neither approach is inherently better: static typing catches errors earlier but requires more upfront annotation, while dynamic typing offers more flexibility but defers errors to runtime.

The practical benefit of understanding type systems is **predictability**. When you know that a variable holds an integer, you know you can do arithmetic with it. When you know a function returns a boolean, you know you can use it in an `if` condition. **Type safety** is the guarantee that a program will not perform an operation on a value of the wrong type. A type-safe program will never, say, try to divide a string by a number — either the compiler prevents it or the runtime raises an error. As you move toward type conversion and casting, you will learn how to deliberately cross type boundaries when you need to, but the type system ensures you always do so explicitly rather than accidentally.
