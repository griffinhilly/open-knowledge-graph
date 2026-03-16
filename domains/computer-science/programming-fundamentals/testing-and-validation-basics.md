---
id: testing-and-validation-basics
title: Testing and Validation Basics
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: function-design-and-contracts
  type: hard
tags:
- testing
- validation
- correctness
stage: abstract-reasoning
status: draft
---

# Testing and Validation Basics

## Core Idea
Testing verifies that code works correctly. Unit tests check individual functions; integration tests check interactions. Test cases should cover normal cases, edge cases, and error cases. Testing is faster and cheaper than debugging production code.

## How It's Best Learned
Write test cases for functions before implementation (test-driven development); test edge cases (empty input, boundary values); run tests after each change.

## Common Misconceptions
That testing is the QA department's job (developers test too); that passing tests guarantees correctness (tests only verify what they test); that comprehensive testing is slow (it saves time by catching bugs early).

## Explainer

From function design and contracts, you understand that a well-designed function has a clear specification: given certain inputs, it should produce certain outputs and maintain certain guarantees. Testing is the practice of systematically verifying that your code actually meets those specifications. Instead of running your program and eyeballing the output, you write code that checks the output automatically.

The simplest form of a test is an **assertion** — a statement that a given condition must be true. If you have a function `def add(a, b): return a + b`, a test might say `assert add(2, 3) == 5`. If the assertion holds, the test passes silently. If it fails, you get an immediate, specific error telling you exactly what went wrong. A **unit test** is a collection of such assertions targeting a single function or small piece of logic. The name comes from the idea that you're testing the smallest "unit" of code in isolation, apart from the rest of the system.

Good tests require thinking about more than just the happy path. For any function, you should consider three categories of test cases. **Normal cases** verify typical inputs: `add(2, 3)` should return `5`. **Edge cases** probe boundaries and special values: `add(0, 0)`, `add(-1, 1)`, `add(999999, 1)`. These are where bugs hide most often, because developers tend to think about typical inputs when writing code but forget the extremes. **Error cases** verify that the function handles invalid input gracefully: what happens if you pass a string to `add`? Should it raise an error? Return a default? The function's contract (its preconditions and postconditions) tells you what the correct behavior should be.

The deeper insight is that testing changes how you write code, not just how you verify it. When you know you need to test a function, you naturally write it to be more testable — cleaner inputs and outputs, fewer side effects, smaller scope. **Test-driven development** (TDD) takes this to its logical conclusion: write the tests first, watch them fail, then write the code that makes them pass. Even if you don't follow strict TDD, the discipline of writing tests alongside your code catches bugs when they're cheapest to fix — at the moment of creation, not weeks later in production. A function with good tests becomes a reliable building block that you can refactor, extend, or reuse with confidence, because the tests will immediately tell you if you've broken something.
