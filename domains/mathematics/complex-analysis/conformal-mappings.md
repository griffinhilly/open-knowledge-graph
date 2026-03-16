---
id: conformal-mappings
title: Conformal Mappings
domain: mathematics
course: complex-analysis
prerequisites:
- id: holomorphic-functions
  type: hard
- id: complex-differentiability
  type: soft
builds-toward:
- mobius-transformations
tags:
- conformal-mappings
- angle-preserving
- geometry
stage: advanced
status: draft
---

# Conformal Mappings

## Core Idea
A holomorphic function f with f'(z₀) ≠ 0 is conformal (angle-preserving) near z₀: it scales lengths by |f'(z₀)| and rotates by arg(f'(z₀)), preserving angles between curves. Conformal maps are essential in applications: they transform boundary value problems from complicated regions to simple ones (like the unit disk) where solutions are known.

## How It's Best Learned
Visualize f(z) = e^z and see how it maps vertical lines to rays and horizontal lines to circles. Understand why angles are preserved: f'(z) = e^z is nonzero everywhere.

## Common Misconceptions
Thinking all angle-preserving functions are holomorphic; orientation-reversing maps (like conjugation) also preserve angles. Assuming conformal maps are easy to find; finding the right map for a given boundary value problem requires skill and often tables of known maps.

## Explainer

A **conformal map** is a function that preserves angles. If two curves meet at a point at angle θ, their images under a conformal map also meet at angle θ. The geometric reason follows directly from your knowledge of holomorphic functions: if f is holomorphic at z₀ with f'(z₀) ≠ 0, then near z₀ the function acts by multiplying every displacement by the complex number f'(z₀). Complex multiplication by f'(z₀) = |f'(z₀)|·e^{i·arg(f'(z₀))} scales all lengths by |f'(z₀)| and rotates all directions by arg(f'(z₀)) — the same rotation applied to every direction. Because every tangent vector gets rotated by the same angle, the angle between any two tangent vectors is preserved.

The example that builds the most intuition is f(z) = e^z. Consider two families of lines in the z-plane: vertical lines (Re(z) = a) and horizontal lines (Im(z) = b). Since e^{a+iy} = e^a·e^{iy}, vertical lines (fixed a, varying y) map to circles of radius e^a centered at the origin. Since e^{x+ib} = e^x·e^{ib}, horizontal lines (fixed b, varying x) map to rays from the origin at angle b. Vertical and horizontal lines meet at right angles in the z-plane — and their images (circles and rays) also meet at right angles in the w-plane. The entire Cartesian grid maps to the polar grid, with all 90° intersections preserved.

The power of conformal maps in applications comes from **Riemann's mapping theorem**: any simply connected region (other than all of ℂ) can be conformally mapped to the unit disk. This means that to solve a boundary value problem — say, finding the steady-state temperature distribution or the electrostatic potential in some oddly shaped region — you can instead solve the same problem on the unit disk, where the solution is known (Poisson's formula), and then pull the solution back through the conformal map. The key fact that makes this work: Laplace's equation ∇²u = 0 is preserved under conformal changes of coordinates. Heat sources stay heat sources, insulated boundaries stay insulated.

The condition f'(z₀) ≠ 0 is essential and cannot be dropped. At **critical points** (zeros of f'), the map fails to be conformal: it multiplies angles by an integer factor. Near a zero of f' of order k, the map locally behaves like z^{k+1}, which multiplies all angles by k+1. A right angle becomes a (k+1) × 90° angle. These critical points are the places where the mapping "folds" the plane and where the angle-preserving property breaks down.
