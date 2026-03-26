---
id: tangent-planes-surfaces
title: Tangent Planes to Surfaces
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: tangent-planes-linear-approximation
  type: hard
builds-toward:
- surface-parametrization
tags:
- tangent-planes
- surfaces
- normal-vector
stage: formal-systems
status: validated
---

# Tangent Planes to Surfaces

## Core Idea
For a surface z = f(x, y), the tangent plane at (x₀, y₀, z₀) has equation z − z₀ = f_x(x₀, y₀)(x − x₀) + f_y(x₀, y₀)(y − y₀). The normal vector is n = ⟨f_x, f_y, −1⟩, and ∇f lies in the plane.

## Questions

```yaml
- question: "For the surface z = f(x,y), which vector is normal to the tangent plane at the point (x₀, y₀, z₀)?"
  type: multiple-choice
  options:
    - "⟨f_x, f_y⟩ — the 2D gradient vector evaluated at (x₀, y₀)"
    - "⟨f_x, f_y, −1⟩ — the gradient components plus −1 as the z-component"
    - "⟨f_x, f_y, 1⟩ — the gradient components plus +1 as the z-component"
    - "⟨−f_x, −f_y, 0⟩ — the negative gradient in the xy-plane"
  answer: 1
  explanation: "The tangent plane equation f_x(x−x₀) + f_y(y−y₀) − (z−z₀) = 0 is in the form n·⟨x−x₀, y−y₀, z−z₀⟩ = 0, so the normal vector is the coefficient vector n = ⟨f_x, f_y, −1⟩. The −1 appears because z enters with a coefficient of −1 when the equation is rearranged. Option A is the most tempting wrong answer: the 2D gradient ∇f = ⟨f_x, f_y⟩ lives in the xy-plane and lies IN the tangent plane (it is not the normal to it). Confusing the 2D gradient with the 3D normal is the central misconception of this topic."

- question: "For an implicitly defined surface F(x, y, z) = c, which vector is normal to the surface at a point?"
  type: multiple-choice
  options:
    - "The 2D gradient ⟨F_x, F_y⟩ evaluated on the surface"
    - "The 3D gradient ∇F = ⟨F_x, F_y, F_z⟩"
    - "The unit tangent vector to any curve lying on the surface"
    - "The Hessian matrix of F at the point"
  answer: 1
  explanation: "Because F is constant (= c) along the surface, any tangent direction v to the surface satisfies ∇F · v = 0. This means ∇F is perpendicular to every tangent vector, making it the normal. This unifies the explicit and implicit cases: for z = f(x,y), define F = f(x,y)−z, so ∇F = ⟨f_x, f_y, −1⟩ — recovering the explicit formula. The Hessian is a matrix of second derivatives and does not in general point normal to the surface."

- question: "The 2D gradient vector ∇f = ⟨f_x, f_y⟩ is the normal vector to the tangent plane of the surface z = f(x,y)."
  type: true-false
  answer: false
  explanation: "The 2D gradient lives in the xy-plane and actually lies IN the tangent plane (projected down). The normal to the tangent plane in 3D is ⟨f_x, f_y, −1⟩ — which includes the −1 z-component arising from the z term in the plane equation. Confusing the 2D gradient with the 3D normal is the most common error in this topic. The gradient ∇f encodes the slope in each horizontal direction; the normal must also account for the z-direction."

- question: "The tangent plane to z = f(x,y) at a point (x₀, y₀, z₀) contains the tangent line to the cross-sectional curve obtained by fixing y = y₀."
  type: true-false
  answer: true
  explanation: "Setting y = y₀ in the tangent plane equation z − z₀ = f_x(x−x₀) + f_y(y−y₀) gives z − z₀ = f_x(x−x₀), which is exactly the tangent line in the xz-plane at y = y₀. Similarly, fixing x = x₀ gives the tangent line in the yz-plane. The tangent plane is precisely the unique plane that contains both of these tangent lines simultaneously — it is the natural 3D generalization of the 1D tangent line."

- question: "Explain why the normal vector to the tangent plane of z = f(x,y) has −1 as its z-component, rather than +1 or some other value."
  type: short-answer
  answer: "Rearranging the tangent plane equation: f_x(x−x₀) + f_y(y−y₀) − (z−z₀) = 0. Written as a dot product n·⟨x−x₀, y−y₀, z−z₀⟩ = 0, the normal vector is the coefficient vector n = ⟨f_x, f_y, −1⟩. The −1 appears because z appears on the right side of z − z₀ = f_x(x−x₀) + f_y(y−y₀), so when moved to the left it becomes −(z−z₀), giving a coefficient of −1 for z."
  explanation: "This can also be understood from the implicit formulation: define F(x,y,z) = f(x,y) − z. Then the surface z = f(x,y) is the level set F = 0, and ∇F = ⟨f_x, f_y, −1⟩. The −1 comes from ∂F/∂z = −1. The sign matters: it points 'upward' out of the surface in the sense that increasing z means increasing z−f(x,y), so the outward normal has a negative z-component when the surface is a graph over the xy-plane."
```

## Explainer

In single-variable calculus, the tangent line at a point (x₀, y₀) on the curve y = f(x) has equation y − y₀ = f'(x₀)(x − x₀). It is the best linear approximation to f near x₀. The **tangent plane** for a surface z = f(x, y) is the direct 3D extension: a flat plane that best approximates the surface near the point (x₀, y₀, z₀). Instead of one derivative, there are two — f_x and f_y, the partial derivatives you know from the gradient — and the plane accounts for the slope in each independent direction.

The tangent plane equation z − z₀ = f_x(x₀, y₀)(x − x₀) + f_y(x₀, y₀)(y − y₀) can be read as: "the change in z is approximately the x-slope times the change in x, plus the y-slope times the change in y." Hold y fixed (set y = y₀) and the equation becomes z − z₀ = f_x(x − x₀), which is exactly the tangent line in the xz-plane. Hold x fixed and you recover the tangent line in the yz-plane. The tangent plane combines both tangent lines simultaneously — it is the unique plane containing both.

The **gradient** ∇f = ⟨f_x, f_y⟩ encodes both partial derivatives but lives in the xy-plane, not in 3D. The **normal vector** to the tangent plane is n = ⟨f_x, f_y, −1⟩. To see why: rewrite the tangent plane as f_x(x − x₀) + f_y(y − y₀) − (z − z₀) = 0, which is the equation n · ⟨x − x₀, y − y₀, z − z₀⟩ = 0 — the standard form of a plane with normal n. The third component is −1 because z appears with coefficient −1 when you move it to the left side. This is why the statement "∇f lies in the plane" is true: the 2D gradient vector is not the 3D normal; the normal has an additional z-component.

For a surface given **implicitly** as F(x, y, z) = c (rather than explicitly as z = f(x,y)), the 3D gradient ∇F = ⟨F_x, F_y, F_z⟩ is the normal vector to the surface. This is the more general form: since F is constant on the surface, any tangent direction v must satisfy ∇F · v = 0, making ∇F normal to every tangent direction. The explicit case z = f(x,y) is a special case: define F(x,y,z) = f(x,y) − z, so ∇F = ⟨f_x, f_y, −1⟩, recovering the normal vector from the Core Idea. This unification — the gradient of an implicit equation is always the normal to the corresponding surface — is one of the most reusable ideas in multivariable calculus.
