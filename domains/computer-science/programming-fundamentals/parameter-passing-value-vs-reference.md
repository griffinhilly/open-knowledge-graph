---
id: parameter-passing-value-vs-reference
title: 'Parameter Passing: Value vs. Reference'
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: function-parameters-passing-data
  type: hard
- id: scope-shadowing-and-lifetime
  type: soft
builds-toward:
- function-design-and-contracts
tags:
- functions
- parameters
- memory
stage: abstract-reasoning
status: draft
---

# Parameter Passing: Value vs. Reference

## Core Idea
Pass-by-value creates a copy; changes inside the function don't affect the original. Pass-by-reference passes the actual variable; changes are visible outside. Some languages default to one, others allow choosing (ref, &). Understanding which applies prevents bugs.

## How It's Best Learned
Modify parameters inside functions and check if the original changed; test with different types (primitives vs objects); use language-specific tools to track memory.

## Common Misconceptions
That all languages use the same passing strategy (they don't); that pass-by-reference is always better (pass-by-value is safer); that objects and primitives follow the same rules (often they don't).
