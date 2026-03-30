---
id: minimal-surfaces
title: Minimal Surfaces
domain: mathematics
course: differential-geometry
prerequisites:
  - id: riemannian-metrics
    type: hard
  - id: connections-and-covariant-derivative
    type: hard
  - id: submanifolds
    type: hard
  - id: curvature-tensor
    type: soft
tags:
  - minimal-surfaces
  - mean-curvature
  - second-fundamental-form
  - variational-problems
stage: expert
status: validated
---

# Minimal Surfaces

## Core Idea
A minimal surface is a surface whose mean curvature vanishes everywhere — it is a critical point of the area functional. Equivalently, every point has a neighborhood that minimizes area among surfaces with the same boundary. Soap films spanning wire frames are physical realizations of minimal surfaces. The study of minimal surfaces sits at the intersection of differential geometry, partial differential equations, and the calculus of variations, and has produced some of the deepest results in geometric analysis.

## Questions

```yaml
- question: "A minimal surface has zero mean curvature H = 0. This means the surface is a critical point of the area functional. Does this mean minimal surfaces have the least area among all surfaces with the same boundary?"
  type: multiple-choice
  options:
    - "Yes — zero mean curvature implies global area minimization"
    - "Not necessarily — they are critical points (like saddle points can be critical points of a function), so they locally minimize area but may not globally minimize"
    - "No — minimal surfaces always maximize area"
    - "Only for compact surfaces without boundary"
  answer: 1
  explanation: "Minimal surfaces are critical points of the area functional, meaning the first variation of area vanishes. Like saddle points of functions, they need not be global (or even local) minima. The catenoid, for instance, is minimal but can be deformed to a surface with less area (a pair of disks). Area-minimizing surfaces are always minimal (H = 0), but the converse is false. The terminology 'minimal' is historical and somewhat misleading."

- question: "The second fundamental form of a surface S ⊂ ℝ³ measures how S curves within the ambient space. The mean curvature H is the trace of the second fundamental form. If the principal curvatures at a point are κ₁ and κ₂, then H = (κ₁ + κ₂)/2 = 0 on a minimal surface. What does this imply about the principal curvatures?"
  type: short-answer
  answer: "At every point of a minimal surface, κ₁ = -κ₂. The surface curves equally in opposite directions — it is saddle-shaped at every point (except where both curvatures are zero, which is an umbilic flat point). The Gaussian curvature K = κ₁κ₂ = -κ₁² ≤ 0 at every point. Minimal surfaces therefore have non-positive Gaussian curvature everywhere."
  explanation: "The saddle shape is visible in examples: the catenoid, helicoid, and Enneper's surface all have saddle-shaped geometry at every point. The condition κ₁ = -κ₂ means the surface looks like a saddle in every direction — if it curves up in one principal direction, it curves down equally in the perpendicular direction."

- question: "The Plateau problem asks: given a closed curve Γ in ℝ³, does there exist a minimal surface (area-minimizing surface) with boundary Γ?"
  type: true-false
  answer: true
  explanation: "The Plateau problem was solved by Jesse Douglas and Tibor Radó in 1930 (Douglas received a Fields Medal for this). For any rectifiable Jordan curve Γ in ℝ³, there exists a disk-type surface of least area spanning Γ. The solution may not be unique, smooth, or embedded — regularity and uniqueness require additional conditions on Γ. The Plateau problem is the founding problem of the calculus of variations in geometry and has been generalized in many directions (higher dimensions, different boundary conditions, singular surfaces)."

- question: "The only complete minimal surfaces in ℝ³ that are also planes are... planes. More precisely, a complete minimal surface in ℝ³ with finite total curvature ∫|K|dA < ∞ is conformally equivalent to a compact Riemann surface with finitely many punctures."
  type: true-false
  answer: true
  explanation: "This is a deep theorem combining minimal surface theory with complex analysis. The Weierstrass representation expresses minimal surfaces in ℝ³ using holomorphic data (a meromorphic function and a holomorphic 1-form on a Riemann surface). Finite total curvature forces the Riemann surface to have finite topology — it is a compact surface with punctures (the 'ends' of the minimal surface). Classical examples: the plane (genus 0, no punctures), the catenoid (genus 0, two punctures), the Costa surface (genus 1, three punctures)."
```

## Explainer

When a surface S sits inside ℝ³ (or more generally, inside a Riemannian manifold), it inherits an intrinsic geometry from the ambient metric, and it also has **extrinsic** geometric properties — how it bends within the ambient space. The **second fundamental form** II(X, Y) = -g(∇_X N, Y) measures this extrinsic bending, where N is the unit normal. The **principal curvatures** κ₁, κ₂ are the eigenvalues of the shape operator (the second fundamental form viewed as an endomorphism of the tangent space), and the **mean curvature** H = (κ₁ + κ₂)/2 is their average.

A surface is **minimal** if H = 0 everywhere. The name comes from the first variation of area: a surface has H = 0 if and only if the first variation of area vanishes for every compactly supported normal variation. This is the Euler-Lagrange equation for the area functional — minimal surfaces are the "geodesics" of the area problem. Physically, a soap film spanning a wire frame minimizes surface tension (proportional to area) and has H = 0 (unless there is a pressure difference across the film, which gives H = const ≠ 0 — a constant mean curvature surface).

The classical minimal surfaces in ℝ³ are: the **plane** (the trivial example), the **catenoid** (the surface of revolution of a catenary, the only minimal surface of revolution), and the **helicoid** (the only ruled minimal surface). These were known in the 18th century. Modern examples include the **Costa surface** (1984, the first complete embedded minimal surface of finite topology beyond the plane and catenoid) and the **gyroid** (a triply periodic minimal surface appearing in materials science). The **Weierstrass representation** provides a parametric construction of all minimal surfaces using complex analysis: a minimal surface in ℝ³ is determined by a holomorphic function and a meromorphic function on a Riemann surface.

Minimal surfaces in Riemannian manifolds (beyond ℝ³) are a central topic in geometric analysis. The existence of minimal surfaces (Plateau's problem) has been generalized to arbitrary Riemannian manifolds using geometric measure theory. The regularity theory (when are minimal surfaces smooth?) involves deep PDE techniques. The topology of minimal surfaces constrains and is constrained by the ambient geometry — for instance, Schoen-Yau used minimal surface techniques to prove the positive mass theorem in general relativity, and Colding-Minicozzi used minimal surface theory to study the Ricci flow. Minimal surfaces remain one of the most active areas of research in differential geometry.
