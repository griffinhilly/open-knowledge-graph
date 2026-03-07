---
id: limits-intuitive-introduction
title: Limits - Intuitive Introduction
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
  - id: rational-functions-asymptotes-review
    type: soft
builds-toward:
  - limit-definition-intuitive
  - limit-laws
tags: [limits, introduction, calculus-preview]
stage: formal-systems
status: draft
---

# Limits - Intuitive Introduction

## Core Idea
A limit describes what value a function approaches as the input approaches some target, even if the function is not defined there. For example, (x^2 - 1)/(x - 1) is undefined at x = 1, but as x gets close to 1, the function approaches 2. This concept is the bridge between precalculus and calculus, enabling the precise definition of derivatives and integrals.

## How It's Best Learned
Start with numerical examples: build tables of function values approaching the target from both sides. Then use graphs to visualize. Emphasize that the limit is about approaching behavior, not the function's actual value at the point. Introduce the notation lim as x approaches a of f(x) = L.

## Common Misconceptions
- Believing the limit must equal f(a): the function's value at a (if it exists) may differ from the limit.
- Thinking you can always find a limit by plugging in: limits handle exactly the cases where plugging in fails.
- Confusing "approaches" with "reaches": a limit describes a trend, not necessarily an achieved value.
