---
id: gaussian-and-mean-curvature
title: The Second Fundamental Form, Gaussian Curvature, and Mean Curvature
domain: mathematics
course: differential-geometry
prerequisites:
  - id: first-fundamental-form
    type: hard
  - id: curvature
    type: hard
  - id: eigenvalues-and-eigenvectors
    type: hard
  - id: hessian-matrix-second-derivative-test
    type: soft
builds-toward:
  - gauss-bonnet-theorem
  - minimal-surfaces
  - sectional-curvature
tags: [differential-geometry, surfaces, second-fundamental-form, shape-operator, gaussian-curvature, mean-curvature, principal-curvatures]
stage: advanced
status: validated
---

# The Second Fundamental Form, Gaussian Curvature, and Mean Curvature

## Core Idea
The second fundamental form measures how a surface bends away from its tangent plane. At each point, the unit normal N changes as you move, and the rate of change defines the shape operator S = -dN, a symmetric linear map on the tangent plane. Its eigenvalues are the principal curvatures k₁ and k₂, the largest and smallest normal curvatures of curves through the point. Their product K = k₁k₂ is the Gaussian curvature and their average H = (k₁ + k₂)/2 is the mean curvature. The sign of K classifies points as elliptic (K > 0), hyperbolic (K < 0) or parabolic (K = 0 with S ≠ 0).

## How It's Best Learned
Start with graphs z = f(x, y) at a point where the tangent plane is horizontal; there the second fundamental form is the Hessian of f, and K is its determinant. Compute k₁, k₂, K and H for a sphere, a cylinder and a saddle and connect each to a picture. Then derive the general formulas in terms of the coefficients of the first and second fundamental forms. Finish by stating Gauss's Theorema Egregium, which says K can be computed from the first fundamental form alone.

## Common Misconceptions
- A cylinder is curved, so its Gaussian curvature is nonzero. (Its principal curvatures are 1/r and 0, so K = 0; a cylinder can be unrolled flat, which is consistent with K being intrinsic.)
- Mean curvature and Gaussian curvature carry the same information. (A plane and a cylinder both have K = 0 but different H; a saddle-shaped minimal surface has H = 0 but K < 0.)
- Gaussian curvature depends on which unit normal is chosen. (Reversing N changes the sign of both principal curvatures, so H changes sign while K = k₁k₂ does not.)

## Questions

```yaml
- question: "What are the Gaussian and mean curvatures of a circular cylinder of radius r (using the inward normal)?"
  type: multiple-choice
  options:
    - "K = 1/r², H = 1/r"
    - "K = 0, H = 1/(2r)"
    - "K = 0, H = 0"
    - "K = 1/r, H = 1/(2r)"
  answer: 1
  explanation: "Around the cylinder the normal curvature is 1/r, and along the rulings it is 0. So k₁ = 1/r and k₂ = 0, giving K = k₁k₂ = 0 and H = (1/r + 0)/2 = 1/(2r)."

- question: "Find the Gaussian curvature of the surface z = x² - y² at the origin."
  type: short-answer
  answer: "K = -4"
  explanation: "At the origin the tangent plane is horizontal, so the second fundamental form is the Hessian of f(x, y) = x² - y², with f_xx = 2, f_yy = -2, f_xy = 0. The principal curvatures are 2 and -2, so K = -4. The negative sign marks a saddle (hyperbolic) point."

- question: "Reversing the choice of unit normal changes the sign of the Gaussian curvature."
  type: true-false
  answer: false
  explanation: "Replacing N by -N negates the shape operator, so both principal curvatures change sign. Their product K = k₁k₂ is unchanged, while the mean curvature H changes sign."

- question: "A sphere of radius R has every normal curvature equal to 1/R (with the inward normal). What are K and H?"
  type: short-answer
  answer: "K = 1/R², H = 1/R"
  explanation: "Every direction is principal with curvature 1/R, so k₁ = k₂ = 1/R. Then K = 1/R² and H = 1/R. Points of a sphere are elliptic, and a sphere has constant positive Gaussian curvature."
```

## Explainer

The first fundamental form describes measurement within a surface. It does not see how the surface sits in space: a plane and a cylinder have the same one. To detect bending, follow the unit normal vector N as you move around the surface.

At a point p, let N be the unit normal. For a tangent vector v, the derivative of N in direction v is again tangent to the surface, since N always has length 1. The map S(v) = -dN(v) is the shape operator. It is a symmetric linear map of the tangent plane to itself, so it has two real eigenvalues k₁ ≥ k₂ with perpendicular eigenvectors. These are the principal curvatures, and their eigenvectors give the principal directions.

There is a concrete reading. Take a unit tangent direction v and slice the surface with the plane containing v and N. The slice is a curve, and its curvature, with a sign that tells which way it bends relative to N, is the normal curvature in direction v. As v rotates, the normal curvature varies between k₂ and k₁.

Two combinations are named. The Gaussian curvature is K = k₁k₂ = det S and the mean curvature is H = (k₁ + k₂)/2 = (trace S)/2. In coordinates, with second fundamental form coefficients L = x_uu · N, M = x_uv · N and N₂ = x_vv · N,

K = (L N₂ - M²)/(EG - F²).

For a graph z = f(x, y) at a point where the tangent plane is horizontal, S is the Hessian of f, and K = f_xx f_yy - f_xy².

Examples show what the numbers mean. A sphere of radius R bends equally in every direction: k₁ = k₂ = 1/R, so K = 1/R². A cylinder of radius r bends around but not along its rulings: k₁ = 1/r, k₂ = 0, so K = 0. The saddle z = x² - y² bends up in one direction and down in the other: at the origin k₁ = 2, k₂ = -2, so K = -4.

The sign of K describes the local shape. When K > 0, the surface lies on one side of its tangent plane near p, like a cap. When K < 0, it crosses the tangent plane, like a saddle. Surfaces with H = 0 everywhere are minimal surfaces, the shapes of soap films spanning a wire.

Gauss's Theorema Egregium states that K depends only on E, F and G and their derivatives. So K is intrinsic, even though it was defined using the normal. The Gauss-Bonnet theorem goes further and relates the total Gaussian curvature of a closed surface to its topology.
