---
id: conformal-mapping-electrostatics
title: Conformal Mapping Method
domain: physics
course: electrodynamics
prerequisites:
- id: complex-plane
  type: hard
- id: complex-functions-mappings
  type: hard
- id: laplace-poisson-equations-electrostatics
  type: hard
tags:
- complex-analysis
- analytic-functions
- 2d-electrostatics
stage: expert
status: validated
---

# Conformal Mapping Method

## Core Idea
In 2D, the Laplace equation is satisfied by the real and imaginary parts of any analytic function. Conformal mappings between domains transform solutions systematically, allowing solution of complex geometries by mapping to simple ones.

## Explainer

From your study of the Laplace and Poisson equations in electrostatics, you know that finding the potential in a region means solving ∇²V = 0 subject to boundary conditions. For symmetric geometries — spheres, cylinders, infinite planes — this is tractable by direct methods. But for complicated boundaries (a conducting wedge, a pair of cylinders, a gap between conducting plates at an angle), direct methods fail. Conformal mapping is the elegant escape route: instead of solving on the hard geometry, you transform the geometry into a simple one, solve there, and transform the solution back.

The bridge is **complex analysis**. An **analytic function** f(z) = u(x,y) + iv(x,y) (where z = x + iy) satisfies the Cauchy-Riemann equations, and from those equations it follows that both the real part u and the imaginary part v satisfy the Laplace equation: ∇²u = 0 and ∇²v = 0. So every analytic function automatically gives you two **harmonic functions** — two valid electrostatic potentials — for free. Furthermore, the level curves of u and v are always perpendicular to each other, so one naturally plays the role of equipotentials and the other plays the role of field lines.

A **conformal mapping** is a complex function w = f(z) that maps one region of the complex plane to another while preserving angles locally. Because the Laplace equation is invariant under conformal transformations, if Φ(w) satisfies Laplace's equation in the w-plane, then Φ(f(z)) satisfies it in the z-plane. The strategy is: (1) identify the boundary conditions in the hard geometry (z-plane), (2) find an analytic function that maps that geometry to a simple one (w-plane), (3) solve Laplace's equation in the simple geometry, and (4) transform back. For example, the mapping w = z² transforms a wedge of half-angle π/4 into a half-plane; the mapping w = ln(z) transforms a pair of concentric cylinders into a rectangular strip where the solution is a simple linear function.

The method is limited to two spatial dimensions, which is why it appears in 2D electrostatics problems (long conductors, cross-sections of cables) rather than fully 3D problems. Within that limitation it is extraordinarily powerful: geometries that would require numerical computation can often be solved in closed form. The key skill is building a catalog of useful mappings — the Joukowski transform, the Schwarz-Christoffel mapping for polygonal boundaries, logarithmic and power-function maps — and recognizing which geometry calls for which. Each mapping is not just a trick but a structural fact about how the Laplace equation behaves under coordinate changes, which connects directly to the broader theory of harmonic functions in complex analysis.

## Questions

```yaml
- question: "Why do the real and imaginary parts of an analytic function both satisfy the Laplace equation?"
  type: short-answer
  answer: "An analytic function satisfies the Cauchy-Riemann equations: ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. Differentiating the first equation with respect to x and the second with respect to y and adding gives ∂²u/∂x² + ∂²u/∂y² = 0, i.e., ∇²u = 0. Similarly for v."
  explanation: "This connection is fundamental: complex differentiability imposes the Cauchy-Riemann constraints, and those constraints are precisely the Laplace equation. It explains why complex analysis is so natural for 2D potential theory — the two fields are the same mathematical structure."

- question: "A conducting wedge has opening angle α. You want to find the potential inside using conformal mapping. What type of mapping would you look for, and why?"
  type: short-answer
  answer: "Look for a power-law mapping w = z^(π/α), which maps the wedge sector into a half-plane. The boundary conditions (V = 0 on both sides of the wedge) map to V = 0 on the entire real axis in the w-plane, where the solution is a simple half-plane problem with known form."
  explanation: "Power maps z^n scale angles by n, so choosing n = π/α straightens the wedge into a 180° flat boundary (half-plane). In the half-plane, the solution is V ∝ Im(w) = Im(z^(π/α)), which can be written explicitly in polar coordinates as V ∝ r^(π/α) sin(πθ/α). Near the wedge tip (r → 0), this determines how field strength diverges."
```
