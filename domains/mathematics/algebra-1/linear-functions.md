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

## Explainer

You already know how to graph y = mx + b and interpret the slope as rise over run. The shift to **function notation** — writing f(x) = mx + b instead of y = mx + b — is not just cosmetic. It turns the equation into a machine: you feed in any value of x, and the machine returns exactly one output. Writing f(3) = 2(3) + 1 = 7 makes the input-output relationship explicit in a way that "let x = 3" does not. The notation f(3) asks a specific question: "what does this function return when the input is 3?" The answer is a number, 7, not a new equation.

The **domain** of a function is the set of allowable inputs, and the **range** is the set of all possible outputs. For f(x) = mx + b with m ≠ 0, the domain is all real numbers — you can plug in any x you like — and the range is also all real numbers, because as x runs over every value, mx + b hits every value too. This is different from, say, a function defined only on positive integers. Pure mathematics uses all real numbers as the default domain unless a real-world context imposes a restriction. If f(x) = 50x models the distance (in miles) driven in x hours, then the context restricts the domain to x ≥ 0, but the mathematical function itself has no such restriction.

The slope m now carries a precise interpretation: it is the **constant rate of change**. For every 1-unit increase in x, the output increases by exactly m. This constancy is what makes the function linear — the rate never speeds up or slows down. Temperature conversion illustrates this: C = (5/9)(F − 32), which you can write as C(F) = (5/9)F − 160/9. The rate of change is 5/9 degrees Celsius per degree Fahrenheit, everywhere on the domain. Whether you are converting 0°F or 200°F, one additional degree Fahrenheit always adds 5/9 of a degree Celsius.

Function notation also lets you compare multiple functions cleanly. If f(x) = 2x + 1 and g(x) = −x + 7, you can find where they agree by solving f(x) = g(x), which gives 2x + 1 = −x + 7, so x = 2. The intersection point is at x = 2, f(2) = g(2) = 5. This framing — two functions whose output values you are equating — is how linear systems get set up, and it extends to all the non-linear functions you will encounter in later courses. The concept of a function as an input-output rule is the foundation everything else builds on.
