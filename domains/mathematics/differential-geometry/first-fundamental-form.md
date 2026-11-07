---
id: first-fundamental-form
title: The First Fundamental Form of a Surface
domain: mathematics
course: differential-geometry
prerequisites:
  - id: parametric-surfaces
    type: hard
  - id: surface-area-integrals
    type: hard
  - id: dot-product
    type: soft
builds-toward:
  - gaussian-and-mean-curvature
  - riemannian-metrics
  - gauss-bonnet-theorem
tags: [differential-geometry, surfaces, first-fundamental-form, metric, arc-length, intrinsic-geometry]
stage: advanced
status: validated
---

# The First Fundamental Form of a Surface

## Core Idea
For a surface given by a parametrization x(u, v), the first fundamental form records how to measure lengths on the surface using the parameters. Its coefficients are E = x_u · x_u, F = x_u · x_v and G = x_v · x_v, and the squared length of a small step (du, dv) is E du² + 2F du dv + G dv². From E, F and G alone one can compute lengths of curves, angles between curves and areas of regions on the surface. Properties determined by the first fundamental form are called intrinsic: they can be measured by someone living on the surface, without reference to the surrounding space.

## How It's Best Learned
Compute E, F and G for a plane in polar coordinates, a cylinder, a sphere and a surface of revolution, and use them to find arc lengths and areas that can be checked against known answers. Notice that a cylinder and a plane have the same coefficients in suitable coordinates, and connect this to rolling a sheet of paper into a tube without stretching. Keep the dot-product definitions in view so the formulas stay grounded.

## Common Misconceptions
- E, F and G depend only on the surface. (They depend on the parametrization; the same sphere has different coefficients in different coordinates, while lengths and areas computed from them agree.)
- Two surfaces with the same first fundamental form must have the same shape in space. (A plane and a cylinder have the same coefficients in suitable coordinates, yet one is flat and the other is curved in space.)
- The area element is E·G du dv. (It is √(EG - F²) du dv, which equals |x_u × x_v| du dv; the F term matters when coordinate curves are not perpendicular.)

## Questions

```yaml
- question: "For the sphere x(φ, θ) = (R sin φ cos θ, R sin φ sin θ, R cos φ), what are E, F and G?"
  type: multiple-choice
  options:
    - "E = R², F = 0, G = R² sin²φ"
    - "E = R² sin²φ, F = 0, G = R²"
    - "E = R, F = R, G = R sin φ"
    - "E = 1, F = 0, G = 1"
  answer: 0
  explanation: "x_φ = (R cos φ cos θ, R cos φ sin θ, -R sin φ) has squared length R², x_θ = (-R sin φ sin θ, R sin φ cos θ, 0) has squared length R² sin²φ, and their dot product is 0. So the meridians and parallels are perpendicular and E = R², F = 0, G = R² sin²φ."

- question: "Using the sphere's coefficients E = R², F = 0, G = R² sin²φ, compute the total surface area of the sphere."
  type: short-answer
  answer: "4πR²"
  explanation: "The area element is √(EG - F²) dφ dθ = R² sin φ dφ dθ. Integrating over 0 ≤ φ ≤ π and 0 ≤ θ ≤ 2π gives R² · 2 · 2π = 4πR²."

- question: "The cylinder x(θ, z) = (cos θ, sin θ, z) and the plane x(u, v) = (u, v, 0) have the same first fundamental form in these coordinates."
  type: true-false
  answer: true
  explanation: "For the cylinder, x_θ = (-sin θ, cos θ, 0) and x_z = (0, 0, 1), so E = 1, F = 0, G = 1, exactly as for the plane. This is why a flat sheet can be rolled into a cylinder without stretching: small regions of the two surfaces are isometric."

- question: "Write the formula for the length of a curve t ↦ x(u(t), v(t)) on a surface, for a ≤ t ≤ b, in terms of E, F and G."
  type: short-answer
  answer: "Length = ∫ from a to b of √(E u'(t)² + 2F u'(t) v'(t) + G v'(t)²) dt"
  explanation: "The velocity is x_u u' + x_v v' by the chain rule. Its squared length is (x_u · x_u)u'² + 2(x_u · x_v)u'v' + (x_v · x_v)v'², which is the first fundamental form evaluated on (u', v')."
```

## Explainer

Suppose a surface S in space is described by a parametrization x(u, v), so that each pair of parameters gives a point. A curve on the surface can be described by functions u(t) and v(t). To find its length, we need its speed. By the chain rule its velocity is x_u u' + x_v v', where x_u and x_v are the partial derivative vectors. The squared speed is

|x_u u' + x_v v'|² = E u'² + 2F u'v' + G v'²,

with E = x_u · x_u, F = x_u · x_v and G = x_v · x_v. The quadratic expression I = E du² + 2F du dv + G dv² is the first fundamental form. It is the dot product of space, restricted to tangent vectors of the surface and written in the surface's own coordinates.

Everything metric about the surface comes from these three functions. Arc length is the integral of √(E u'² + 2F u'v' + G v'²). The angle θ between the coordinate curves satisfies cos θ = F/√(EG), so F = 0 means the coordinate grid is orthogonal. Area comes from |x_u × x_v|, and the identity |a × b|² = |a|²|b|² - (a · b)² gives the area element √(EG - F²) du dv.

Take the sphere of radius R with x(φ, θ) = (R sin φ cos θ, R sin φ sin θ, R cos φ). A short computation gives E = R², F = 0 and G = R² sin²φ. The area element is R² sin φ dφ dθ, and integrating over the sphere gives 4πR². Near the poles, where sin φ is small, a step in θ covers little distance.

Now compare a plane and a cylinder. The plane x(u, v) = (u, v, 0) has E = 1, F = 0, G = 1. The cylinder x(θ, z) = (cos θ, sin θ, z) also has E = 1, F = 0, G = 1. To an observer confined to either surface, measuring with a tape that bends with the surface, small regions look exactly alike. A sheet of paper rolls into a cylinder without stretching for this reason. Such a correspondence that preserves the first fundamental form is called a local isometry.

Properties that depend only on E, F and G are intrinsic. Gauss proved that the Gaussian curvature, which seems to depend on how the surface bends in space, is intrinsic too. So a sphere has no local isometry to the plane, and every flat map of the Earth distorts something. A metric written in local coordinates is also the starting idea of Riemannian geometry.
