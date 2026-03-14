---
id: linear-recurrence-solutions
title: Solving Linear Recurrence Relations via Characteristic Equations
domain: mathematics
course: discrete-math
prerequisites:
- id: recurrence-relations-definition
  type: hard
builds-toward:
- nonhomogeneous-recurrence-solutions
tags:
- recurrence-relations
- characteristic-equations
stage: formal-systems
status: draft
---

# Solving Linear Recurrence Relations via Characteristic Equations

## Core Idea
For homogeneous linear recurrences a(n) = c₁a(n-1) + ⋯ + cₖa(n-k), the characteristic equation is xᵏ - c₁xᵏ⁻¹ - ⋯ - cₖ = 0. The general solution is a linear combination of terms r^n where r are roots of the characteristic equation. Repeated roots yield polynomial factors in the solution.
