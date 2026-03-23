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
status: validated
---

# Change of Variables and the Jacobian

## Core Idea
To change variables in integrals: ∬_R f(x,y) dx dy = ∬_S f(x(u,v), y(u,v)) |det(J)| du dv, where J is the Jacobian matrix. The determinant's absolute value scales area/volume.

## Questions

```yaml
- question: "A student converts ∬_R f(x,y) dx dy to polar coordinates by substituting x = r cosθ, y = r sinθ and writes ∬_S f(r cosθ, r sinθ) dr dθ. What is wrong with this?"
  type: multiple-choice
  options:
    - "They used the wrong substitution formulas for polar coordinates"
    - "They forgot to include the Jacobian factor r, so the integral doesn't account for how area changes with r"
    - "The limits of integration must be changed before any substitution is valid"
    - "Nothing — substituting coordinates and adjusting limits is all that is required"
  answer: 1
  explanation: "The most common error in change of variables is omitting |det(J)|. For polar coordinates, the Jacobian determinant equals r, which must be included inside the integral. Without it, the integral incorrectly treats all (r, θ) area elements as equal size — but a thin wedge at large r covers much more actual area than the same wedge near the origin. The factor r corrects for this distortion."

- question: "Why can't you factor |det(J)| out of the integral as a constant after performing a change of variables?"
  type: multiple-choice
  options:
    - "The Jacobian is always equal to 1, so there is nothing to factor out"
    - "|det(J)| varies across the domain as a function of the new coordinates, so it must remain inside the integral"
    - "You can only factor it out if the region of integration is a rectangle in the new coordinates"
    - "Factoring the Jacobian out would change the integration variable"
  answer: 1
  explanation: "|det(J)| is the local area magnification factor at each point in the domain, and it generally varies from point to point. For polar coordinates, |det(J)| = r, which changes with r — pulling it outside the integral would treat all r-values as having the same magnification, which is false. Only if the transformation is globally uniform (constant Jacobian) could factoring be valid."

- question: "In single-variable substitution u = g(x), the factor g'(x) plays a different conceptual role than |det(J)| does in multivariable change of variables."
  type: true-false
  answer: false
  explanation: "They play exactly the same role: both are scaling factors that correct for how the substitution stretches or compresses the domain. g'(x) measures how the single-variable substitution locally magnifies the number line; |det(J)| measures how the multivariable transformation locally magnifies area or volume. The Jacobian determinant is precisely the generalization of the derivative to multiple dimensions."

- question: "The extra factor of r that appears in polar coordinate integrals (as in ∬ f(r, θ) r dr dθ) is the absolute value of the Jacobian determinant of the polar coordinate transformation."
  type: true-false
  answer: true
  explanation: "Computing the Jacobian matrix for x = r cosθ, y = r sinθ gives [[cosθ, −r sinθ], [sinθ, r cosθ]], whose determinant is r cos²θ + r sin²θ = r. This is why r appears in every polar integral — it's not a convention or an add-on, it's exactly the Jacobian factor required by the change-of-variables formula."

- question: "Explain in your own words why you must multiply by |det(J)| when changing variables in a multivariable integral — what does this factor represent geometrically?"
  type: short-answer
  answer: "|det(J)| measures how much the coordinate transformation locally magnifies or compresses area at each point. When you substitute new coordinates, small rectangles in the new (u,v)-space correspond to differently-sized regions in the original (x,y)-space. The integral must be corrected by this magnification factor so it accumulates the right amount of area. Integrating without |det(J)| measures the function's values but ignores how much actual area each (u,v) rectangle represents — dimensionally, the answer would be wrong."
  explanation: "The geometric picture is essential: you are remapping a region, and remapping distorts areas. |det(J)| is the ratio of distortion at each point, and it must be incorporated into the integrand to preserve the integral's meaning."
```

## Explainer

When you learned single-variable integration, you used substitution: ∫f(g(x)) g'(x) dx = ∫f(u) du where u = g(x). The term g'(x) is a **scaling factor** — it accounts for how the substitution stretches or compresses the domain. Change of variables in multiple dimensions is the same idea, promoted to n dimensions, where the scaling factor becomes the absolute value of a determinant.

You already know the **Jacobian matrix** J: its (i,j) entry is ∂xᵢ/∂uⱼ, the partial derivative of the i-th original coordinate with respect to the j-th new coordinate. The **determinant of J**, written det(J), measures how much the transformation stretches or compresses area (in 2D) or volume (in 3D). If |det(J)| = 3, a tiny rectangle in (u, v)-space corresponds to a region 3 times as large in (x, y)-space. The integral must be corrected by exactly this factor to remain consistent.

The polar coordinate transformation makes this concrete. Set x = r cos θ, y = r sin θ. The Jacobian matrix is [[cos θ, −r sin θ], [sin θ, r cos θ]], and its determinant is r cos²θ + r sin²θ = r. So the change-of-variables formula gives ∬_R f(x,y) dx dy = ∬_S f(r cos θ, r sin θ) · r dr dθ. The factor of r — often seen but rarely explained in introductory courses — is exactly |det(J)|. It appears because a thin wedge in polar coordinates at large r covers more actual area than the same wedge near the origin.

The key principle: when you change variables, you must always multiply by |det(J)|, never just substitute. Forgetting this factor is the most common error, and it produces integrals that are dimensionally wrong — they measure the function's values without accounting for the distortion the coordinate change introduces. You can think of |det(J)| as the "local area magnification factor" of the transformation. Since this magnification can vary across the domain, it must stay inside the integral as a function of the new coordinates (u, v), not pulled out as a constant.
