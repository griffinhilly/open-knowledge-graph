---
id: programming-fundamentals-parameters-arguments
title: Parameters and Arguments
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-function-definition
  type: hard
builds-toward:
- programming-fundamentals-variable-scope
tags:
- functions
- parameters
- arguments
stage: formal-systems
status: draft
---

# Parameters and Arguments

## Core Idea
Parameters are variables declared in a function definition; arguments are values passed when calling the function. Parameters act as local variables that receive argument values, allowing functions to operate on different data.

## Questions

```yaml
- question: "Given the function definition `def multiply(x, y): return x * y`, you call `multiply(3, 7)`. Which statement correctly identifies parameters and arguments?"
  type: multiple-choice
  options:
    - "`3` and `7` are parameters; `x` and `y` are arguments supplied by the definition"
    - "`multiply` is the parameter; `3` and `7` are arguments passed to it"
    - "`x` and `y` are parameters declared in the definition; `3` and `7` are the arguments passed at the call site"
    - "Parameters and arguments are the same thing — both refer to `x`, `y`, `3`, and `7` collectively"
  answer: 2
  explanation: "Parameters (`x` and `y`) are the placeholder variables declared in the function definition — they exist in the function's blueprint but have no value until the function is called. Arguments (`3` and `7`) are the actual values supplied at the call site. When you call `multiply(3, 7)`, Python creates local variables `x = 3` and `y = 7` inside the function. Option D is the most common confusion — treating the terms as synonyms obscures the distinction between a slot and the value that fills it."

- question: "Consider this code: `x = 10 / def double(n): n = n * 2 / result = double(x)`. After the call, what is the value of `x`?"
  type: multiple-choice
  options:
    - "20 — because the function multiplied it by 2"
    - "10 — parameters create local variables inside the function; reassigning `n` inside `double` does not affect the variable `x` in the calling context"
    - "10 — but only because integers are immutable in Python, so this behavior would differ for lists"
    - "It raises a NameError — `x` is not visible inside the function"
  answer: 1
  explanation: "When `double(x)` is called, Python creates a local variable `n` inside the function and sets it to the value of `x` (10). The line `n = n * 2` reassigns the local variable `n` to 20 — it does not touch `x` at all. After the function returns, `n` ceases to exist. `x` remains 10. Option B (mentioning immutability) is partially true for Python but gives the wrong reason conceptually: the key principle is that parameters create isolated local variables, regardless of type."

- question: "In a function call, the first argument is matched to the first parameter, the second argument to the second parameter, and so on — the order of arguments determines which parameter each value fills."
  type: true-false
  answer: true
  explanation: "By default, Python (and most languages) match arguments to parameters positionally — left to right. `def add(a, b): return a - b` called as `add(10, 3)` assigns `a = 10` and `b = 3`, returning 7. If you reversed the arguments: `add(3, 10)`, you get `a = 3`, `b = 10`, returning -7. Order matters unless you use keyword arguments explicitly (e.g., `add(b=3, a=10)`), which override positional matching."

- question: "A parameter and an argument are two different names for the same thing — both refer to the values that a function uses when it runs."
  type: true-false
  answer: false
  explanation: "They are distinct concepts that exist at different moments. A parameter is a placeholder variable declared in the function definition — it exists in the code before any call is made and has no value yet. An argument is a specific value supplied when the function is actually called. The parameter defines the slot; the argument fills it. Conflating the two makes it harder to debug type or count mismatches: an error about 'wrong number of arguments' is about what the caller supplied; an error inside the function about an unexpected value is often about what the parameter received."

- question: "Explain the distinction between a parameter and an argument, and describe why the distinction matters when you are debugging a function that is producing unexpected output."
  type: short-answer
  answer: "A parameter is a variable declared in the function definition that acts as a named slot for incoming data — it has no value until the function is called. An argument is the actual value passed to the function at the call site, which fills that slot. When debugging unexpected output, the distinction matters because it tells you where to look: if the function's logic is correct but results are wrong, the problem may be in the arguments the caller is supplying (wrong values, wrong order, wrong type). If the function is receiving the right arguments but still misbehaving, the problem is in the function body itself. The parameter/argument boundary is the interface between caller and callee — pinpointing which side is broken requires understanding which side you're inspecting."
  explanation: "This is not just vocabulary — it's a debugging strategy. The parameter defines the function's contract (what it promises to accept), and the argument is what the caller actually delivers. When those don't match in type, count, or order, you get errors or unexpected behavior. Tracing a bug by printing what arguments arrive at a parameter is a fundamental technique in every language."
```

## Explainer

When you learned to define functions, you saw that a function packages a reusable block of code behind a name. But a function that always does exactly the same thing with exactly the same data is limited. **Parameters** are what make functions flexible — they are placeholder variables listed in the function's definition that say "I expect to receive some data here." When you actually call the function and supply specific values, those values are called **arguments**. The parameter is the slot; the argument is what fills it.

Consider a function `def greet(name):` that prints a greeting. Here, `name` is a parameter — a variable that doesn't have a value yet. When you call `greet("Alice")`, the string `"Alice"` is the argument. At the moment of the call, Python creates a local variable called `name` inside the function and assigns it the value `"Alice"`. The function body then uses `name` as if it were any other variable. Call `greet("Bob")` next, and `name` becomes `"Bob"` for that execution. Same function, different data, different results — that's the power of parameterization.

Functions can accept multiple parameters, separated by commas: `def add(a, b):` expects two arguments. The order matters — the first argument fills the first parameter, the second fills the second. Some languages also support **keyword arguments**, where you specify which parameter gets which value by name (`add(b=3, a=7)`), and **default values**, where a parameter gets a fallback if no argument is provided (`def greet(name="world")`). These features give you fine-grained control over how data flows into your functions.

The distinction between parameters and arguments may seem like vocabulary trivia, but it matters when debugging. If a function misbehaves, the first question is: "What arguments did it receive?" Parameters define the function's contract — what it expects. Arguments are what the caller actually delivers. When those don't match (wrong number, wrong type, wrong order), you get errors. Understanding this data-passing mechanism is also the foundation for understanding variable scope, which you'll encounter next: parameters create local variables that exist only inside the function call, isolated from the rest of your program.
