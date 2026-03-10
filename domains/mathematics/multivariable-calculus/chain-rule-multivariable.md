---
id: chain-rule-multivariable
title: The Multivariable Chain Rule
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: chain-rule
  type: hard
- id: tangent-planes
  type: soft
builds-toward:
- implicit-differentiation
- gradient-vector
tags:
- chain-rule
- composite-functions
- tree-diagram
- total-derivative
stage: formal-systems
status: draft
---

# The Multivariable Chain Rule

## Core Idea
If z = f(x, y) and both x and y depend on a parameter t, then dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). More generally, if z depends on x and y, and each depends on s and t, then ∂z/∂s = (∂z/∂x)(∂x/∂s) + (∂z/∂y)(∂y/∂s). The key rule is: the derivative of a composite function sums contributions from every path from the output to the input variable in the dependency diagram. Tree diagrams make the structure of these sums transparent.

## How It's Best Learned
Teach tree diagrams explicitly. Draw a tree from z to its intermediate variables (x, y) and then to the final parameters (t or s, t). Each path from root to leaf contributes one product of partials. Verify with a concrete example where f can be substituted directly, so students can check their chain rule answer against direct computation.

## Common Misconceptions
- Using dz/dx instead of ∂z/∂x when z also depends on y is incorrect; ordinary derivative notation implies only one independent variable.
- When x and y both depend on the same variable t, BOTH contributions must be added — students sometimes include only one.
- The multivariable chain rule reduces to the single-variable chain rule when the intermediate variables are each functions of a single parameter.
