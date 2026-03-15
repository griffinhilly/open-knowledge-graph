---
id: variation-of-parameters
title: Variation of Parameters Method
domain: mathematics
course: differential-equations
prerequisites:
- id: wronskian-linear-independence
  type: hard
- id: integration-by-parts
  type: hard
builds-toward:
- higher-order-linear-odes
tags:
- particular-solution
- variation-of-parameters
- general-method
stage: formal-systems
status: draft
---

# Variation of Parameters Method

## Core Idea
Variation of parameters is a universal method for finding a particular solution to y'' + p(x)y' + q(x)y = f(x). Assume y_p = u₁(x)y₁ + u₂(x)y₂ where y₁, y₂ solve the homogeneous equation, and solve for u₁, u₂ using the Wronskian. Though more computational than undetermined coefficients, this method works for any continuous f(x), making it the universal tool when other methods fail.
