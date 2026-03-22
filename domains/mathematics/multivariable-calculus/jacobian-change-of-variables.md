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

## Questions

```yaml
- question: "When evaluating ∬_R f(x,y) dA using the substitution x = g(u,v), y = h(u,v), what correctly replaces the area element dA?"
  type: multiple-choice
  options:
    - "du dv"
    - "J du dv, where J is the signed Jacobian determinant"
    - "|J| du dv, where |J| is the absolute value of the Jacobian determinant"
    - "(1/J) du dv"
  answer: 2
  explanation: "The area element transforms as dA = |J| du dv. The absolute value is required because area elements must be positive regardless of whether the transformation preserves or reverses orientation. Using the signed J (option B) would give a negative result for orientation-reversing transformations. Using 1/J (option D) corresponds to the inverse transformation."

- question: "A student correctly sets up a double integral in polar coordinates but forgets to include the Jacobian factor. Her computed answer will be:"
  type: multiple-choice
  options:
    - "Correct, because the polar transformation has a Jacobian of 1"
    - "Off by a constant factor equal to the area of the integration region"
    - "Wrong because she is effectively computing ∬ f(r,θ) dr dθ instead of ∬ f(r,θ) r dr dθ"
    - "Correct, because the polar transformation is its own inverse and the errors cancel"
  answer: 2
  explanation: "The Jacobian for polar coordinates is r (not 1). Forgetting it means integrating without the r factor — the error is not a constant but varies across the region, since r takes different values at different points. The r factor is not a formula to memorize but the Jacobian of the transformation x = r cosθ, y = r sinθ; this is why it appears and why it cannot simply be dropped."

- question: "The r that appears in the polar area element r dr dθ is exactly the Jacobian determinant of the polar coordinate transformation."
  type: true-false
  answer: true
  explanation: "True. With x = r cosθ, y = r sinθ, the Jacobian matrix is [[cosθ, −r sinθ], [sinθ, r cosθ]], and its determinant is r cos²θ + r sin²θ = r. The r in r dr dθ is not an ad hoc correction — it is the Jacobian. This unifies a formula that might otherwise seem arbitrary with the general theory."

- question: "Any valid substitution x = g(u,v), y = h(u,v) will simplify a double integral, as long as the Jacobian is correctly computed."
  type: true-false
  answer: false
  explanation: "False. A poor substitution can make an integral harder, not easier. The Jacobian correctly accounts for area scaling regardless of the substitution chosen, but if the new region in uv-space is more complicated than R, or if the transformed integrand is messier, the substitution has made the problem worse. The skill is choosing a substitution aligned with the symmetry of the region and integrand — one that turns R into a simpler shape, often a rectangle."

- question: "Explain why the Jacobian determinant appears in the change-of-variables formula for double integrals. What does it measure, and how does this connect to single-variable substitution?"
  type: short-answer
  answer: "In single-variable substitution, the factor |g'(u)| corrects for how much the substitution stretches or compresses the x-axis: a small interval du in u-space corresponds to a length |g'(u)| du in x-space. The Jacobian is the 2D generalization: it measures how much the transformation locally stretches or compresses area. A small rectangle du × dv in uv-space maps to a parallelogram in xy-space with area |J| du dv, so the integral must include |J| to correctly account for that area change."
  explanation: "The geometric interpretation — Jacobian = local area scaling factor — is the key insight. The determinant connection comes from the fact that the columns of the Jacobian matrix are the images of the unit vectors under the linear approximation to the transformation, and the determinant measures the area of the parallelogram they span."
```

## Explainer

Recall the single-variable substitution rule: if x = g(u), then ∫f(x) dx = ∫f(g(u)) |g'(u)| du. The factor g'(u) is the derivative of the substitution — it corrects for the stretching introduced when you change the variable. If g'(u) = 3, a small interval du in u-space corresponds to a length-3 interval dx in x-space, and the integral must be scaled accordingly. The **Jacobian** for a two-variable substitution is the direct 2D generalization of this correction factor.

When you substitute x = g(u,v), y = h(u,v), the transformation maps a region S in uv-space to a region R in xy-space. A small rectangle in uv-space — with sides du and dv — maps to a small parallelogram in xy-space. The **Jacobian determinant** J = ∂(x,y)/∂(u,v) measures the local area scaling: the parallelogram in xy-space has area |J| du dv. This is why ∬_R f(x,y) dA = ∬_S f(g(u,v), h(u,v)) |J| du dv — the |J| factor replaces the lost dA, just as g'(u) replaced dx in one dimension.

The determinant connection comes from your prerequisite on 2×2 determinants. The Jacobian matrix is J = [[∂x/∂u, ∂x/∂v], [∂y/∂u, ∂y/∂v]], whose columns are the partial derivatives of the transformation. The two columns represent the images of the unit vectors in the u and v directions under the linear approximation to the transformation. The determinant of this matrix equals the signed area of the parallelogram spanned by those image vectors — exactly the local area scaling factor you need. Absolute value is used because areas must be positive, regardless of whether the transformation preserves or reverses orientation.

The polar coordinate formula r dr dθ that you already know is a special case. With x = r cosθ, y = r sinθ, the Jacobian matrix is [[cosθ, −r sinθ], [sinθ, r cosθ]], and its determinant is r cos²θ + r sin²θ = r. This unifies a formula you may have memorized (just "add an r for polar") with the general theory — the r factor is exactly the Jacobian. When choosing a substitution, the goal is always to make the new region S in uv-space simpler (often a rectangle) and the new integrand more tractable. A good substitution aligned to the symmetry of the region and integrand can turn an intractable integral into a straightforward one.
