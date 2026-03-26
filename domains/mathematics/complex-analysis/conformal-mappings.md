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
status: validated
---

# Conformal Mappings

## Core Idea
A holomorphic function f with f'(z₀) ≠ 0 is conformal (angle-preserving) near z₀: it scales lengths by |f'(z₀)| and rotates by arg(f'(z₀)), preserving angles between curves. Conformal maps are essential in applications: they transform boundary value problems from complicated regions to simple ones (like the unit disk) where solutions are known.

## How It's Best Learned
Visualize f(z) = e^z and see how it maps vertical lines to rays and horizontal lines to circles. Understand why angles are preserved: f'(z) = e^z is nonzero everywhere.

## Common Misconceptions
Thinking all angle-preserving functions are holomorphic; orientation-reversing maps (like conjugation) also preserve angles. Assuming conformal maps are easy to find; finding the right map for a given boundary value problem requires skill and often tables of known maps.

## Questions

```yaml
- question: "The function f(z) = z³ has a critical point at z = 0, where f'(0) = 0. What happens to angles at this point under the map?"
  type: multiple-choice
  options:
    - "Angles are preserved, since z³ is holomorphic everywhere"
    - "Angles are doubled, since z³ is a degree-3 map"
    - "Angles are tripled — multiplied by 3 — because the zero of f' has order 2 (k=2)"
    - "The map is not defined at z = 0 and angles are undefined there"
  answer: 2
  explanation: "At a zero of f' of order k, the map locally behaves like z^{k+1} and multiplies all angles by k+1. For f(z) = z³, we have f'(z) = 3z², which has a zero of order k=2 at z=0. So angles at z=0 are multiplied by k+1 = 3. Being holomorphic everywhere is necessary but not sufficient for conformality — you also need f'(z) ≠ 0. Option A conflates holomorphicity with conformality, a common mistake; the key additional requirement is the nonvanishing derivative."

- question: "Why is Riemann's mapping theorem useful for solving boundary value problems on oddly shaped regions?"
  type: multiple-choice
  options:
    - "It guarantees that any region can be mapped to another region with the same area, making computations equivalent"
    - "It provides an explicit formula for the conformal map, which can be used to compute solutions directly"
    - "It allows you to transform a problem on a complicated region to the unit disk, where solutions are known, and then pull back through the map — because Laplace's equation is preserved under conformal coordinates"
    - "It shows that any harmonic function on a complicated region can be extended to the complex plane"
  answer: 2
  explanation: "The key facts working together are: (1) any simply connected region can be conformally mapped to the unit disk (Riemann's theorem), and (2) Laplace's equation ∇²u = 0 is preserved under conformal coordinate changes. This means a harmonic function on the disk pulls back to a harmonic function on the original region. Since Poisson's formula gives explicit solutions on the disk, you can solve the problem there and transfer the solution back. Riemann's theorem does not provide the explicit map — finding it requires additional work — but its existence guarantees the strategy is always available."

- question: "Laplace's equation is preserved under conformal changes of coordinates, which is what makes conformal maps useful for solving potential problems."
  type: true-false
  answer: true
  explanation: "This is the critical analytical fact underlying all applications of conformal maps to physics and engineering. If u is harmonic (∇²u = 0) in the w-plane, and w = f(z) is conformal, then u ∘ f is harmonic in the z-plane. This means you can transform a boundary value problem for the Laplacian from a complicated domain to a simple one (like the unit disk), solve it there, and pull the solution back. Without this preservation property, conformal maps would be geometrically interesting but analytically useless for differential equations."

- question: "Orientation-reversing maps, like complex conjugation f(z) = z̄, are not angle-preserving and therefore can rarely be conformal."
  type: true-false
  answer: false
  explanation: "Orientation-reversing maps do preserve angles — but they reverse orientation. Complex conjugation maps the angle θ to −θ, so the absolute angle between two curves is preserved even though their signed orientation flips. A conformal map in the strict sense is angle-preserving and orientation-preserving, which is why we require holomorphicity rather than just angle-preservation. But the statement as written — that orientation-reversing maps cannot preserve angles — is false. This is noted in the Common Misconceptions: 'orientation-reversing maps (like conjugation) also preserve angles.'"

- question: "Why is the condition f'(z₀) ≠ 0 essential for conformality, and what goes wrong geometrically when f'(z₀) = 0?"
  type: short-answer
  answer: "A holomorphic function acts near z₀ by multiplying all displacement vectors by f'(z₀). When f'(z₀) ≠ 0, this means every direction is rotated by the same angle arg(f'(z₀)), so the angle between any two tangent vectors is unchanged. When f'(z₀) = 0, the first-order behavior vanishes and the map locally looks like z^{k+1} near the critical point — which multiplies angles by k+1 rather than preserving them. Geometrically, the map 'folds' the plane at that point: distinct directions get mapped to the same direction, angles between curves are distorted."
  explanation: "Intuitively, conformality requires that the linearization of f at z₀ (given by the derivative) be a nonzero complex number — a scaled rotation. Zero derivative means the linearization is the zero map, which collapses all directions. The map then requires looking at higher-order terms, which are no longer pure rotations but power maps that multiply angles. Critical points are geometrically the places where the conformal structure breaks down, and recognizing them is essential when using conformal maps in practice."
```

## Explainer

A **conformal map** is a function that preserves angles. If two curves meet at a point at angle θ, their images under a conformal map also meet at angle θ. The geometric reason follows directly from your knowledge of holomorphic functions: if f is holomorphic at z₀ with f'(z₀) ≠ 0, then near z₀ the function acts by multiplying every displacement by the complex number f'(z₀). Complex multiplication by f'(z₀) = |f'(z₀)|·e^{i·arg(f'(z₀))} scales all lengths by |f'(z₀)| and rotates all directions by arg(f'(z₀)) — the same rotation applied to every direction. Because every tangent vector gets rotated by the same angle, the angle between any two tangent vectors is preserved.

The example that builds the most intuition is f(z) = e^z. Consider two families of lines in the z-plane: vertical lines (Re(z) = a) and horizontal lines (Im(z) = b). Since e^{a+iy} = e^a·e^{iy}, vertical lines (fixed a, varying y) map to circles of radius e^a centered at the origin. Since e^{x+ib} = e^x·e^{ib}, horizontal lines (fixed b, varying x) map to rays from the origin at angle b. Vertical and horizontal lines meet at right angles in the z-plane — and their images (circles and rays) also meet at right angles in the w-plane. The entire Cartesian grid maps to the polar grid, with all 90° intersections preserved.

The power of conformal maps in applications comes from **Riemann's mapping theorem**: any simply connected region (other than all of ℂ) can be conformally mapped to the unit disk. This means that to solve a boundary value problem — say, finding the steady-state temperature distribution or the electrostatic potential in some oddly shaped region — you can instead solve the same problem on the unit disk, where the solution is known (Poisson's formula), and then pull the solution back through the conformal map. The key fact that makes this work: Laplace's equation ∇²u = 0 is preserved under conformal changes of coordinates. Heat sources stay heat sources, insulated boundaries stay insulated.

The condition f'(z₀) ≠ 0 is essential and cannot be dropped. At **critical points** (zeros of f'), the map fails to be conformal: it multiplies angles by an integer factor. Near a zero of f' of order k, the map locally behaves like z^{k+1}, which multiplies all angles by k+1. A right angle becomes a (k+1) × 90° angle. These critical points are the places where the mapping "folds" the plane and where the angle-preserving property breaks down.
