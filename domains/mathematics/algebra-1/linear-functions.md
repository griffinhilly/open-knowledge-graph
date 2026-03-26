---
id: linear-functions
title: Linear Functions
domain: mathematics
course: algebra-1
prerequisites:
- id: graphing-linear-equations
  type: hard
- id: slope-intercept-form
  type: hard
builds-toward: []
tags:
- functions
- linear
- domain
- range
- rate-of-change
stage: abstract-reasoning
status: validated
---
# Linear Functions

## Core Idea
A linear function is a function of the form f(x) = mx + b, where every input x produces exactly one output. Viewing y = mx + b through the lens of functions adds structure: the domain is all real numbers (unless context restricts it), the range is all real numbers (for non-zero slope), and the slope m represents a constant rate of change. Function notation like f(3) = 2(3) + 1 = 7 makes input-output relationships explicit and enables composition, evaluation, and comparison of multiple functions. Linear functions model any situation where a quantity changes at a steady rate — distance over time at constant speed, cost per unit, temperature conversion.

## How It's Best Learned
Build on students' existing knowledge of slope-intercept form by rewriting y = mx + b as f(x) = mx + b and practicing function evaluation. Compare two linear functions on the same graph to discuss how domain, range, and rate of change differ. Use real-world contexts where students define the function, state its domain, and interpret f(x) values.

## Common Misconceptions
- Thinking f(x) means "f times x" instead of "the output of function f at input x."
- Believing the domain of a linear function must be restricted to integers or positive numbers, when in pure math it is all real numbers unless otherwise stated.

## Questions

```yaml
- question: "A student writes: 'f(3) = 2x + 1 evaluated at x = 3.' Their answer is f(3) = 7. What is wrong with their reasoning, if anything?"
  type: multiple-choice
  options:
    - "Nothing is wrong — f(3) = 7 is correct"
    - "They used the wrong formula; you must substitute before writing f(3)"
    - "f(3) means f multiplied by 3, so the answer should be 3f, not 7"
    - "The domain of f(x) = 2x + 1 does not include x = 3"
  answer: 0
  explanation: "The reasoning is valid and the answer is correct. f(3) is precisely the question 'what does this function return when the input is 3?' — substituting x = 3 into 2x + 1 gives 7. The common confusion is option C: thinking f(x) means f *times* x. In function notation, f(x) is not multiplication — it means 'the output of function f at input x.' The notation exists specifically to make this input-output relationship explicit."

- question: "A scenario: a phone plan charges $30/month plus $0.10 per text message. Let f(x) = 0.10x + 30, where x is number of texts. A student says 'the domain of this function is all real numbers.' Are they correct?"
  type: multiple-choice
  options:
    - "Yes — as a mathematical function, f(x) = 0.10x + 30 accepts any real number"
    - "No — the domain must be restricted to positive integers since you can't send a negative or fractional text"
    - "No — the domain must be restricted to values that make f(x) positive"
    - "Yes — but only because the slope is positive"
  answer: 1
  explanation: "In this context, the student is wrong. The real-world scenario restricts the domain: x must be a non-negative integer (you can't send −5 texts or 2.7 texts). The *mathematical* function f(x) = 0.10x + 30 has all real numbers as its domain, but context can and does restrict it. This distinction — between the pure mathematical domain and the contextually constrained domain — is a key skill in linear functions. The answer is B: the context forces a restriction to whole numbers ≥ 0."

- question: "For a non-zero linear function f(x) = mx + b, the range is generally a proper subset of the real numbers."
  type: true-false
  answer: false
  explanation: "False. For f(x) = mx + b with m ≠ 0, the range is *all* real numbers. As x takes every real number value, mx + b hits every real number — the output grows without bound as x increases or decreases. The range is only restricted if m = 0 (a horizontal line), in which case the range is the single value {b}, or if the context restricts the domain. The common misconception is thinking range must be limited the way it is for quadratics or other non-linear functions."

- question: "The equation y = 3x + 5 and the equation f(x) = 3x + 5 represent fundamentally the same mathematical object."
  type: true-false
  answer: true
  explanation: "True — they describe the same relationship. Function notation f(x) = 3x + 5 is simply a rewriting of y = 3x + 5 that makes the input-output structure explicit. The variable y is replaced by f(x) to emphasize that 'y is the output of function f when x is the input.' Both have the same slope (3), the same y-intercept (5), and the same graph. The advantage of function notation is practical: f(3) asks a specific question, whereas 'let x = 3 in y = 3x + 5' is more cumbersome and doesn't generalize as cleanly to comparing multiple functions."

- question: "Why does the slope of a linear function represent a 'constant rate of change,' and why does that constancy matter?"
  type: short-answer
  answer: "For every 1-unit increase in input x, the output increases by exactly m — the slope — no matter where on the domain you are. This is what makes the function linear: the rate never accelerates or decelerates. It matters because it allows prediction from any point: if you know the slope and one output, you can compute any other output without needing to re-examine the function."
  explanation: "The constancy distinguishes linear functions from all others. In a quadratic, the rate of change itself changes (it speeds up or slows down). In a linear function, the ratio (change in output)/(change in input) is identical at every point. This means real-world linear models — cost per unit, speed at constant velocity, temperature conversion — allow exact prediction without knowing where you 'started.' The slope is the entire story of how the output responds to the input."
```

## Explainer

You already know how to graph y = mx + b and interpret the slope as rise over run. The shift to **function notation** — writing f(x) = mx + b instead of y = mx + b — is not just cosmetic. It turns the equation into a machine: you feed in any value of x, and the machine returns exactly one output. Writing f(3) = 2(3) + 1 = 7 makes the input-output relationship explicit in a way that "let x = 3" does not. The notation f(3) asks a specific question: "what does this function return when the input is 3?" The answer is a number, 7, not a new equation.

The **domain** of a function is the set of allowable inputs, and the **range** is the set of all possible outputs. For f(x) = mx + b with m ≠ 0, the domain is all real numbers — you can plug in any x you like — and the range is also all real numbers, because as x runs over every value, mx + b hits every value too. This is different from, say, a function defined only on positive integers. Pure mathematics uses all real numbers as the default domain unless a real-world context imposes a restriction. If f(x) = 50x models the distance (in miles) driven in x hours, then the context restricts the domain to x ≥ 0, but the mathematical function itself has no such restriction.

The slope m now carries a precise interpretation: it is the **constant rate of change**. For every 1-unit increase in x, the output increases by exactly m. This constancy is what makes the function linear — the rate never speeds up or slows down. Temperature conversion illustrates this: C = (5/9)(F − 32), which you can write as C(F) = (5/9)F − 160/9. The rate of change is 5/9 degrees Celsius per degree Fahrenheit, everywhere on the domain. Whether you are converting 0°F or 200°F, one additional degree Fahrenheit always adds 5/9 of a degree Celsius.

Function notation also lets you compare multiple functions cleanly. If f(x) = 2x + 1 and g(x) = −x + 7, you can find where they agree by solving f(x) = g(x), which gives 2x + 1 = −x + 7, so x = 2. The intersection point is at x = 2, f(2) = g(2) = 5. This framing — two functions whose output values you are equating — is how linear systems get set up, and it extends to all the non-linear functions you will encounter in later courses. The concept of a function as an input-output rule is the foundation everything else builds on.
