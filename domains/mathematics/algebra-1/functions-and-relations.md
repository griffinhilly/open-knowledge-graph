---
id: functions-and-relations
title: Relations and Functions
domain: mathematics
course: algebra-1
prerequisites:
  - id: function-tables
    type: hard
  - id: coordinate-plane-all-four-quadrants
    type: hard
builds-toward:
  - linear-functions
  - function-notation-review
  - domain-and-range
tags: [functions, relations, vertical-line-test, mapping, graphs]
stage: abstract-reasoning
status: validated
---

# Relations and Functions

## Core Idea
A relation is any set of input-output pairs. A function is a relation in which every input is paired with exactly one output. The same output may appear for several inputs, but one input may never lead to two different outputs. On a graph, a relation is a function exactly when no vertical line crosses the graph more than once. This definition underlies every function studied in algebra and calculus.

## How It's Best Learned
Show the same relation four ways: as a list of ordered pairs, a table, a mapping diagram with arrows, and a graph. Have students test each one by asking whether any input has two arrows leaving it. Use everyday examples (each student has one birthday, but a birthday can belong to many students) before abstract ones, and include non-examples such as the circle x² + y² = 25.

## Common Misconceptions
- A function cannot repeat an output. (Repeated outputs are allowed; f(x) = x² gives 4 for both x = 2 and x = -2 and is still a function.)
- Every equation in x and y describes y as a function of x. (The equation x = y² pairs x = 4 with both y = 2 and y = -2, so y is not a function of x.)
- The vertical line test works by checking horizontal lines. (Horizontal lines test whether outputs repeat, which is a different question; only vertical lines check for one input with two outputs.)
- A function must be given by a formula. (A table, a list of pairs or a graph can define a function as long as each input has one output.)

## Questions

```yaml
- question: "Which relation is a function?"
  type: multiple-choice
  options:
    - "{(1, 2), (1, 3), (2, 4)}"
    - "{(1, 5), (2, 5), (3, 5)}"
    - "{(0, 0), (4, 2), (4, -2)}"
    - "{(3, 1), (3, 1), (3, 2)}"
  answer: 1
  explanation: "In {(1, 5), (2, 5), (3, 5)} each input 1, 2, 3 has exactly one output. All outputs being 5 is allowed. The other options each pair one input with two different outputs: 1 with 2 and 3, 4 with 2 and -2, and 3 with 1 and 2."

- question: "A relation in which two different inputs have the same output cannot be a function."
  type: true-false
  answer: false
  explanation: "The definition restricts inputs, not outputs. Each input must have exactly one output, but different inputs may share an output. For example, every input of f(x) = 7 has output 7."

- question: "Does the graph of the circle x² + y² = 25 represent y as a function of x? Explain using the vertical line test."
  type: short-answer
  answer: "No. The vertical line x = 3 meets the circle at (3, 4) and (3, -4), so the input 3 has two outputs."
  explanation: "A vertical line that crosses a graph twice shows one x-value paired with two y-values. Most vertical lines through the interior of this circle cross it twice, so the circle fails the test."

- question: "A table lists inputs 1, 2, 3, 2 with outputs 4, 6, 8, 6. Is this a function?"
  type: multiple-choice
  options:
    - "No, because the input 2 appears twice"
    - "Yes, because the input 2 is paired with the same output both times"
    - "No, because the output 6 appears twice"
    - "Yes, because there are four inputs and four outputs"
  answer: 1
  explanation: "A repeated row such as (2, 6) listed twice is the same pair, so 2 still has only one output. The relation would fail only if 2 were paired with two different outputs."
```

## Explainer

In earlier work you built tables from rules like "multiply by 3 and add 1." Each input produced one output. That property has a name, and it is the central idea of algebra from here on.

Start with the broader idea of a relation, which is simply a collection of input-output pairs. The pairs might come from a rule, a table, a graph or real life. The set {(1, 3), (2, 5), (2, 7)} is a relation. So is the pairing of each person in a room with the people they have met.

A function is a relation with one restriction: each input is paired with exactly one output. The relation above fails, because the input 2 goes to both 5 and 7. The relation {(1, 3), (2, 5), (4, 5)} passes. The output 5 appears twice, but that is fine, since the rule concerns inputs only. A helpful picture is a vending machine: pressing one button should always give the same snack, but two different buttons may give the same snack.

A mapping diagram makes the test visual. List inputs in one oval and outputs in another, and draw an arrow from each input to its output. The relation is a function if no input has more than one arrow leaving it.

Graphs give a quick test as well. Each point on a graph is an (x, y) pair with x as the input. If some vertical line crosses the graph twice, then one x-value has two y-values, and the graph is not a function. This is the vertical line test. Every non-vertical line passes it, and so does the parabola y = x². A circle such as x² + y² = 25 fails, since the line x = 3 hits both (3, 4) and (3, -4).

Why care? When a relation is a function, you can name it, such as f, and write f(x) for the single output that x produces. Without the one-output rule, f(2) would be ambiguous. The set of allowed inputs is called the domain and the set of outputs produced is called the range. Linear, quadratic and exponential functions are all special cases of this one definition.
