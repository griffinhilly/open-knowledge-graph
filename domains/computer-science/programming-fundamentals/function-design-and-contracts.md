---
id: function-design-and-contracts
title: Function Design and Contracts
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: functions-decomposing-problems
  type: hard
- id: return-values
  type: hard
builds-toward:
- recursion-basics
- testing-and-validation-basics
tags:
- functions
- design
- contracts
stage: formal-systems
status: validated
---
# Function Design and Contracts

## Core Idea
A function contract specifies what the function promises: input types and meanings, output type and meaning, preconditions (what must be true before calling), postconditions (what's true after). A well-documented contract makes functions easier to use and test.

## How It's Best Learned
Document existing functions with contracts; test functions at boundary conditions specified in the contract; deliberately violate contracts to see failures.

## Common Misconceptions
That contracts are optional documentation; that a function should work with any input (preconditions define valid inputs); that contracts are too formal for simple code (they scale from simple to complex).

## Questions

```yaml
- question: "A function calculate_average(numbers) divides the sum by the length of the list. A colleague calls it with an empty list, causing a division-by-zero crash. Whose responsibility is this failure under a contract-based design approach?"
  type: multiple-choice
  options:
    - "The function's — it should handle any input it might receive, including empty lists, to be robust"
    - "The caller's — the precondition 'list must contain at least one element' was violated"
    - "Both equally — the function should have defensive code and the caller should have checked"
    - "Neither — this is a language runtime bug, not a design problem"
  answer: 1
  explanation: "Under contract-based design, preconditions define the caller's obligations. If the precondition states 'the list must contain at least one element' and the caller passes an empty list, the caller has violated the contract — the function is not at fault for misbehaving. This framing resolves the ambiguity: instead of writing defensive code that handles every conceivable bad input, the function clearly defines its boundary. Option A reflects the common misconception that 'robust' means 'handles any input' — but robustness means reliably fulfilling the postcondition when preconditions are met, not accepting undefined inputs."

- question: "A developer finds that her function is hard to write a contract for — the postconditions have many special cases and the preconditions are tangled and interconnected. What does this signal?"
  type: multiple-choice
  options:
    - "The function needs more thorough documentation to cover all the edge cases in the contract"
    - "The function handles a genuinely complex problem and a complicated contract is expected"
    - "The function is doing too much and should be decomposed into smaller functions, each with a clean contract"
    - "The contract concept does not scale well to complex functions and should be abandoned here"
  answer: 2
  explanation: "A tangled contract is a design smell. If you can't state what a function does clearly — if the preconditions are complex and the postconditions have many exceptions — that is evidence the function has too many responsibilities. The solution is decomposition: break it into smaller functions each with a clean, simple contract. A function with a clear contract is easy to understand in isolation, easy to test, and easy to compose. Difficulty stating the contract is not a documentation problem; it's a design signal."

- question: "A well-designed function should be able to handle any input it receives, even invalid ones, by returning a sensible default or raising a graceful error."
  type: true-false
  answer: false
  explanation: "This describes defensive programming taken too far. Contract-based design defines a function's preconditions — the inputs for which the function guarantees correct behavior. When a caller violates a precondition, the function's behavior is undefined; it is the caller's fault, not the function's. Writing code to handle every conceivable bad input obscures the contract, makes functions harder to understand and test, and distributes error-handling logic unpredictably. The right approach is to define valid inputs clearly (preconditions) and let callers be responsible for meeting them."

- question: "Writing a function's contract before implementing it — specifying preconditions and postconditions first — helps clarify what the function should do and guides how to test it systematically."
  type: true-false
  answer: true
  explanation: "Specifying the contract before implementation is a form of design-by-specification. Once you know what must be true before calling (preconditions) and what the function guarantees after returning (postconditions), you have a complete specification that drives both implementation and testing. Tests naturally target: does the function satisfy its postconditions when preconditions are met? Does it correctly reject or signal an error when preconditions are violated? Boundary values become obvious from the precondition statements. The contract is not documentation added after the fact — it is the specification the implementation should satisfy."

- question: "How does thinking in terms of preconditions and postconditions change the approach to testing a function, compared to testing without a formal contract?"
  type: short-answer
  answer: "With a contract, testing becomes systematic rather than ad hoc. Preconditions define the valid input space, so you test: (1) postconditions are satisfied throughout the valid range, especially at boundary values, and (2) the function correctly rejects or signals an error when preconditions are violated. Without a contract, testers must guess which inputs matter and which behaviors are expected. With a contract, the test cases are derived directly from the specification: if the precondition says 'list must have at least one element,' you test with exactly one element (boundary), with a typical list, and with an empty list (violation)."
  explanation: "This reveals why contracts are not bureaucratic overhead but a practical tool. They make the testing target explicit — you're no longer testing 'does the function do something reasonable?' but 'does the function satisfy its stated postconditions when called within its stated preconditions?' This precision makes tests more reliable and easier to write, and makes it immediately clear when a test failure is due to a precondition violation versus a postcondition failure."
```

## Explainer

You already know how to decompose a problem into functions and how to return values from them. But consider this: you write a function `calculate_average(numbers)` that divides the sum by the length of the list. A colleague calls it with an empty list. The program crashes with a division-by-zero error. Whose fault is it — yours for not handling empty lists, or your colleague's for passing one? Without a clear agreement, this question has no answer. A **function contract** is that agreement, made explicit.

A contract has two sides. **Preconditions** state what must be true *before* the function is called — the caller's obligations. For `calculate_average`, a precondition might be "the list must contain at least one number." **Postconditions** state what the function guarantees *after* it returns — the function's obligations. Here, the postcondition might be "returns a float equal to the arithmetic mean of all elements in the list." If the caller violates a precondition (passing an empty list), the function is not at fault for misbehaving. If the caller meets all preconditions, the function *must* deliver on its postconditions.

This framing transforms how you think about error handling and testing. Instead of writing defensive code that tries to handle every conceivable bad input, you define the boundary clearly: "I handle *this*; you are responsible for *that*." Testing becomes systematic — you write tests that exercise the postconditions when preconditions are met, and you write tests that verify the function rejects or signals an error when preconditions are violated. Boundary values are especially important: if the precondition says "list must have at least one element," test with exactly one element (the boundary) and with an empty list (the violation).

Well-designed contracts also guide **function decomposition**. If you find it hard to state a function's contract concisely — if the preconditions are tangled or the postconditions have many special cases — that is a signal the function is doing too much. Break it into smaller functions, each with a clean, simple contract. A function with a clear contract is a function that is easy to understand in isolation, easy to test, and easy to compose with other functions. The contract is not bureaucratic overhead — it is the specification that makes reliable software possible.
