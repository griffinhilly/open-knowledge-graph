---
id: undetermined-coefficients
title: Method of Undetermined Coefficients
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: characteristic-equation-method
  type: hard
builds-toward:
- higher-order-linear-odes
tags:
- particular-solution
- undetermined-coefficients
- non-homogeneous
stage: formal-systems
status: draft
---

# Method of Undetermined Coefficients

## Core Idea
To solve y'' + py' + qy = f(x), find the homogeneous solution y_h, then guess the form of a particular solution y_p based on f(x). For f polynomial, exponential, sine, or cosine, use corresponding y_p forms with unknown coefficients. Substitute into the equation and solve for these coefficients. The general solution is y = y_h + y_p. This method is efficient when applicable.
