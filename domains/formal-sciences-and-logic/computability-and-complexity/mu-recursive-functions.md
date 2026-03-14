---
id: mu-recursive-functions
title: Mu-Recursive Functions
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: primitive-recursive-functions
  type: hard
- id: general-recursive-functions
  type: hard
builds-toward:
- church-turing-thesis-formal
tags:
- computability
- recursive-functions
- models-of-computation
stage: formal-systems
status: draft
---

# Mu-Recursive Functions

## Core Idea
The mu-recursive (partial recursive) functions extend the primitive recursive functions by adding the unbounded minimization (mu) operator, which searches for the smallest input satisfying a condition. This single addition is enough to capture all Turing-computable functions, but at the cost of totality — mu-recursive functions may be partial, undefined on some inputs when the search never terminates. The equivalence between mu-recursive functions and Turing machines is one of the key pillars supporting the Church-Turing thesis.

## How It's Best Learned
Start with familiar primitive recursive functions (addition, multiplication), then define a function that requires unbounded search — such as finding the smallest divisor of a number greater than 1. Formalize this using the mu operator, then construct a mu-recursive function that is genuinely partial (undefined on some inputs) to see why totality is lost.

## Common Misconceptions
- The mu operator does not simply add loops — it specifically searches for the least natural number satisfying a predicate, and if no such number exists, the function is undefined (not zero or error).
- Mu-recursive functions are not a strict superset of primitive recursive functions in terms of definedness — every primitive recursive function is total, but many mu-recursive functions are partial.
