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
- id: triple-integrals-cylindrical-spherical
  type: soft
- id: triple-integrals
  type: soft
tags:
- Jacobian
- change-of-variables
- substitution
- determinant
- transformation
stage: formal-systems
status: validated
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

## Explainer

Recall the single-variable substitution rule: if x = g(u), then ∫f(x) dx = ∫f(g(u)) |g'(u)| du. The factor g'(u) is the derivative of the substitution — it corrects for the stretching introduced when you change the variable. If g'(u) = 3, a small interval du in u-space corresponds to a length-3 interval dx in x-space, and the integral must be scaled accordingly. The **Jacobian** for a two-variable substitution is the direct 2D generalization of this correction factor.

When you substitute x = g(u,v), y = h(u,v), the transformation maps a region S in uv-space to a region R in xy-space. A small rectangle in uv-space — with sides du and dv — maps to a small parallelogram in xy-space. The **Jacobian determinant** J = ∂(x,y)/∂(u,v) measures the local area scaling: the parallelogram in xy-space has area |J| du dv. This is why ∬_R f(x,y) dA = ∬_S f(g(u,v), h(u,v)) |J| du dv — the |J| factor replaces the lost dA, just as g'(u) replaced dx in one dimension.

The determinant connection comes from your prerequisite on 2×2 determinants. The Jacobian matrix is J = [[∂x/∂u, ∂x/∂v], [∂y/∂u, ∂y/∂v]], whose columns are the partial derivatives of the transformation. The two columns represent the images of the unit vectors in the u and v directions under the linear approximation to the transformation. The determinant of this matrix equals the signed area of the parallelogram spanned by those image vectors — exactly the local area scaling factor you need. Absolute value is used because areas must be positive, regardless of whether the transformation preserves or reverses orientation.

The polar coordinate formula r dr dθ that you already know is a special case. With x = r cosθ, y = r sinθ, the Jacobian matrix is [[cosθ, −r sinθ], [sinθ, r cosθ]], and its determinant is r cos²θ + r sin²θ = r. This unifies a formula you may have memorized (just "add an r for polar") with the general theory — the r factor is exactly the Jacobian. When choosing a substitution, the goal is always to make the new region S in uv-space simpler (often a rectangle) and the new integrand more tractable. A good substitution aligned to the symmetry of the region and integrand can turn an intractable integral into a straightforward one.
