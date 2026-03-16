---
id: function-notation-review
title: Function Notation Review
domain: mathematics
course: precalculus
prerequisites:
  - id: variable-expressions
    type: hard
builds-toward:
  - domain-and-range
  - function-transformations
tags: [functions, notation, algebra-review]
stage: formal-systems
status: validated
---

# Function Notation Review

## Core Idea
Function notation f(x) provides a compact way to name a rule that assigns each input exactly one output. Understanding notation is essential because every subsequent topic in precalculus and calculus relies on reading, writing, and manipulating expressions like f(x), g(t), or h(x + 2). Mastery here means you can evaluate f(3), interpret f(a + h), and distinguish f(x) from f times x.

## How It's Best Learned
Start by connecting notation to concrete examples: tables, graphs, and verbal descriptions. Practice evaluating functions at numerical inputs first, then at algebraic inputs like f(a + h) - f(a). Emphasize that f(x) is not multiplication.

## Common Misconceptions
- Treating f(x) as f multiplied by x.
- Believing that different letters (f, g, h) must always mean different types of rules.
- Confusing f(x + 2) with f(x) + 2: the first shifts the input, the second shifts the output.

## Questions

```yaml
- question: "If f(x) = 3x - 1, what is f(a + 2)?"
  type: multiple-choice
  options: ["3a - 1 + 2", "3a + 5", "3a + 2 - 1", "3(a + 2)"]
  answer: 1
  explanation: "Substitute (a + 2) for every x: f(a + 2) = 3(a + 2) - 1 = 3a + 6 - 1 = 3a + 5. The entire expression (a + 2) replaces x; you cannot just add 2 to the output."

- question: "f(x + 2) is the same as f(x) + 2 for any function f."
  type: true-false
  answer: false
  explanation: "f(x + 2) changes the INPUT — the 2 is added before the rule is applied. f(x) + 2 changes the OUTPUT — the rule runs first, then 2 is added. For f(x) = x², f(x + 2) = (x+2)² = x² + 4x + 4, while f(x) + 2 = x² + 2. These are different."

- question: "A student writes '2f(x) means the same as f(2x).' Give a counterexample using f(x) = x²."
  type: short-answer
  answer: "At x = 3: 2f(3) = 2(9) = 18, but f(2·3) = f(6) = 36. They are not equal."
  explanation: "2f(x) multiplies the OUTPUT by 2, while f(2x) multiplies the INPUT by 2 before applying the rule. These are different operations and produce different results for any non-linear function."
```

## Explainer

Function notation is a naming convention, not a multiplication. When we write f(x), the letter f names the rule and the x in parentheses is the input. Think of f as a machine: whatever you drop into the parentheses gets processed by the rule. If f(x) = 3x - 1, then f(5) = 14, f(0) = -1, and f(a) = 3a - 1. The letter inside the parentheses is just a placeholder — it says "apply the rule to this."

The most critical skill is evaluating at algebraic inputs. When you compute f(a + h), you substitute the entire expression (a + h) everywhere x appears in the rule. For f(x) = 3x - 1: f(a + h) = 3(a + h) - 1 = 3a + 3h - 1. Many students incorrectly add h only to the output, getting 3a - 1 + h. The key is that input substitution happens inside the machine, before any arithmetic.

The notation f(x + 2) and f(x) + 2 look similar but mean very different things. f(x + 2) shifts the input — you evaluate the rule at a value 2 units to the right of x. f(x) + 2 shifts the output — you run the rule normally and then add 2 to the result. For a squaring function, f(x + 2) = (x + 2)² = x² + 4x + 4, while f(x) + 2 = x² + 2. This distinction becomes central when you study function transformations.

Different function names — f, g, h, or even something like A(t) — are just labels. They do not imply anything different about the shape of the rule. A function can be called anything; what matters is the rule it describes. Scientists often use names like P(t) for population at time t or C(n) for cost of n items, because descriptive letters make the context clearer than bare x.

Finally, note that function notation is not defined for "f times x" — f is not a number, it is a name for a process. The expression f(x) has no meaning if you detach f from its definition. This is why reading f(3) as "f of 3" rather than "f times 3" matters: the former triggers the correct mental image of applying a rule to an input.
