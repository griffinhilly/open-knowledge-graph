---
id: integration-by-parts
title: Integration by Parts
domain: mathematics
course: calculus-2
prerequisites:
  - id: product-rule
    type: hard
  - id: u-substitution
    type: hard
builds-toward:
  - trigonometric-integrals
tags: [integration, techniques, by-parts]
stage: formal-systems
status: validated
---

# Integration by Parts

## Core Idea
Integration by parts reverses the product rule: the integral of u dv = uv - the integral of v du. It converts one integral into another, hopefully simpler one. The LIATE rule (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential) helps choose u. Common applications include integrals involving ln(x), x*e^x, x*sin(x), and arctan(x). Sometimes multiple applications or a cyclical trick are needed.

## How It's Best Learned
Derive from the product rule. Practice choosing u and dv using LIATE. Work through standard types: polynomial times exponential, polynomial times trig, logarithms. Show the tabular method for repeated integration by parts. Practice the cyclical case (e.g., integral of e^x sin(x) dx).

## Common Misconceptions
- Choosing u and dv poorly, making the integral harder instead of easier.
- Forgetting the minus sign in uv - integral of v du.
- Not recognizing when integration by parts needs to be applied multiple times or when a cyclical equation arises.
