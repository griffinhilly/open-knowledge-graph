---
id: wronskian-linear-independence
title: Wronskian and Linear Independence
domain: mathematics
course: differential-equations
prerequisites:
- id: repeated-roots-reduction-of-order
  type: hard
- id: determinants-2x2-3x3
  type: hard
builds-toward:
- undetermined-coefficients
- variation-of-parameters
tags:
- wronskian
- linear-independence
- theoretical
stage: formal-systems
status: draft
---

# Wronskian and Linear Independence

## Core Idea
The Wronskian W[y₁, y₂] = y₁y₂' - y₂y₁' is a determinant measuring linear independence of two solutions. If W ≠ 0 at any point, the solutions are linearly independent and form a fundamental set generating all solutions. For linear ODEs, the Wronskian is either always zero or never zero, making it a definitive test for independence.
