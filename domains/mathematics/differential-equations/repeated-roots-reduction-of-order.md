---
id: repeated-roots-reduction-of-order
title: Repeated Roots and Reduction of Order
domain: mathematics
course: differential-equations
prerequisites:
- id: characteristic-equation-method
  type: hard
- id: product-rule
  type: hard
builds-toward:
- wronskian-linear-independence
tags:
- repeated-roots
- reduction-of-order
- second-solution
stage: advanced
status: draft
---

# Repeated Roots and Reduction of Order

## Core Idea
When the characteristic equation has a repeated root r, one solution is e^(rx), but we need a second linearly independent solution. The reduction-of-order method yields y₂ = x·e^(rx). The general solution is y = (c₁ + c₂x)e^(rx). For higher multiplicities, additional solutions involve higher powers of x. This technique extends beyond repeated roots to finding second solutions from any known solution.
