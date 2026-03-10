---
id: jacobian-change-of-variables
title: Jacobians and Change of Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian
  type: hard
- id: determinants-2x2-3x3
  type: hard
- id: partial-derivatives
  type: hard
- id: double-integrals-polar
  type: soft
tags:
- Jacobian
- change-of-variables
- substitution
- determinant
- transformation
stage: formal-systems
status: draft
---

# Jacobians and Change of Variables

## Core Idea
When changing variables in a double integral using the substitution x = g(u, v), y = h(u, v), the area element transforms as dA = |J| du dv, where J is the Jacobian determinant J = ∂(x,y)/∂(u,v) = det([[∂x/∂u, ∂x/∂v], [∂y/∂u, ∂y/∂v]]). The Jacobian measures how the transformation stretches or compresses areas locally. Polar, cylindrical, and spherical coordinate changes are all special cases: the polar Jacobian is r, the cylindrical Jacobian is r, and the spherical Jacobian is ρ² sinφ.

## How It's Best Learned
Show that the polar change of variables (x = r cosθ, y = r sinθ) gives Jacobian r, unifying the earlier polar integral formula with the general theory. The geometric interpretation — Jacobian = local area scaling factor — is the key idea. Practice with transformations that simplify a difficult region into a rectangle.

## Common Misconceptions
- The absolute value |J| is used in integrals (areas must be positive), not J itself.
- The Jacobian for the inverse transformation is J^{−1}; the two Jacobians are reciprocals of each other.
- Change of variables simplifies integrals only if the new region in uv-coordinates is simpler than the original — choosing a poor substitution can make things worse.
