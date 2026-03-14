---
id: fixed-point-number-representation
title: Fixed-Point Number Representation
domain: computer-science
course: computer-architecture
prerequisites:
- id: binary-number-system
  type: hard
- id: binary-arithmetic
  type: soft
builds-toward:
- floating-point-representation
- arithmetic-logic-units-design
tags:
- representation
- numbers
- fixed-point
stage: formal-systems
status: draft
---

# Fixed-Point Number Representation

## Core Idea
Fixed-point representation stores numbers with a fixed number of digits before and after the decimal point, encoded as integers scaled by a power of 2. This approach trades range for precision and is simpler to implement in hardware than floating-point arithmetic.

## How It's Best Learned
Start with decimal fixed-point (e.g., 2 digits after decimal), convert to binary, then implement basic arithmetic operations.

## Common Misconceptions
Fixed-point precision is uniform across all values, unlike floating-point. The decimal point location is implicit, not stored.
