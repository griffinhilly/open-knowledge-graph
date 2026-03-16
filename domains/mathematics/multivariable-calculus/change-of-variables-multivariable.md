---
id: change-of-variables-multivariable
title: Change of Variables and the Jacobian
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: jacobian-change-of-variables
  type: hard
- id: determinant-computation
  type: hard
builds-toward:
- surface-integrals
tags:
- jacobian
- determinant
stage: formal-systems
status: draft
---

# Change of Variables and the Jacobian

## Core Idea
To change variables in integrals: ∬_R f(x,y) dx dy = ∬_S f(x(u,v), y(u,v)) |det(J)| du dv, where J is the Jacobian matrix. The determinant's absolute value scales area/volume.

## Explainer

When you learned single-variable integration, you used substitution: ∫f(g(x)) g'(x) dx = ∫f(u) du where u = g(x). The term g'(x) is a **scaling factor** — it accounts for how the substitution stretches or compresses the domain. Change of variables in multiple dimensions is the same idea, promoted to n dimensions, where the scaling factor becomes the absolute value of a determinant.

You already know the **Jacobian matrix** J: its (i,j) entry is ∂xᵢ/∂uⱼ, the partial derivative of the i-th original coordinate with respect to the j-th new coordinate. The **determinant of J**, written det(J), measures how much the transformation stretches or compresses area (in 2D) or volume (in 3D). If |det(J)| = 3, a tiny rectangle in (u, v)-space corresponds to a region 3 times as large in (x, y)-space. The integral must be corrected by exactly this factor to remain consistent.

The polar coordinate transformation makes this concrete. Set x = r cos θ, y = r sin θ. The Jacobian matrix is [[cos θ, −r sin θ], [sin θ, r cos θ]], and its determinant is r cos²θ + r sin²θ = r. So the change-of-variables formula gives ∬_R f(x,y) dx dy = ∬_S f(r cos θ, r sin θ) · r dr dθ. The factor of r — often seen but rarely explained in introductory courses — is exactly |det(J)|. It appears because a thin wedge in polar coordinates at large r covers more actual area than the same wedge near the origin.

The key principle: when you change variables, you must always multiply by |det(J)|, never just substitute. Forgetting this factor is the most common error, and it produces integrals that are dimensionally wrong — they measure the function's values without accounting for the distortion the coordinate change introduces. You can think of |det(J)| as the "local area magnification factor" of the transformation. Since this magnification can vary across the domain, it must stay inside the integral as a function of the new coordinates (u, v), not pulled out as a constant.
