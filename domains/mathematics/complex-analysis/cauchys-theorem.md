---
id: cauchys-theorem
title: Cauchy's Theorem
domain: mathematics
course: complex-analysis
prerequisites:
- id: contour-integration
  type: hard
- id: greens-theorem
  type: soft
builds-toward:
- cauchys-integral-formula
- fundamental-theorem-algebra-complex
tags:
- cauchys-theorem
- holomorphic
- closed-contours
stage: advanced
status: draft
---

# Cauchy's Theorem

## Core Idea
If f is holomorphic on a simply connected domain D and γ is any closed contour in D, then ∮_γ f(z) dz = 0. This is the cornerstone of complex analysis: it implies line integrals of holomorphic functions are path-independent, and it leads directly to Cauchy's integral formula, Taylor series, and residue methods. The proof uses Green's theorem and the Cauchy-Riemann equations.

## How It's Best Learned
Verify this for f(z) = z² around a circle; integrate directly and use the theorem to check both give zero. Try f(z) = 1/z around a circle centered at the origin; the theorem does NOT apply (f is not holomorphic at 0), and the integral is nonzero.

## Common Misconceptions
Assuming Cauchy's theorem applies to all functions; it requires holomorphicity and a simply connected domain. Forgetting that the domain must be simply connected; on multiply-connected domains with holes, the integral can be nonzero.

## Explainer

**Cauchy's theorem** is the central miracle of complex analysis: if a function is holomorphic (complex-differentiable everywhere) on a simply connected domain, then its integral around any closed loop in that domain is exactly zero. This sounds like a technical statement, but its consequences are profound — it's what makes complex analysis structurally different from real analysis and enables the powerful residue methods used throughout physics and engineering.

To understand why this is surprising, recall your prerequisite: contour integration. A contour integral ∮_γ f(z) dz measures, loosely, the total "circulation" of f around the path γ. For a real function, the value of a line integral generally depends on the path taken. Cauchy's theorem says that for holomorphic functions, path doesn't matter at all — any closed loop integrates to zero. This is the complex analogue of a conservative vector field in multivariable calculus, and the proof makes this connection explicit: via Green's theorem and the **Cauchy-Riemann equations** (which holomorphicity requires), the integrand reduces to a sum of terms that each vanish identically.

The simply connected condition is not a technical footnote — it's load-bearing. A simply connected domain is one with no "holes": any loop can be continuously contracted to a point without leaving the domain. Consider f(z) = 1/z, which is holomorphic everywhere except at z = 0. On the punctured plane ℂ \ {0}, the domain has a hole at the origin. Integrating 1/z around a circle that encloses the origin gives 2πi ≠ 0. The theorem fails because the domain is not simply connected. This is precisely why the theory of residues is interesting: the nonzero contributions from such loops come entirely from the singularities enclosed, making it possible to compute real integrals by tracking complex poles.

Path-independence is the practical payoff for computations. Since ∮_γ f(z) dz = 0 for any closed loop, the integral of a holomorphic function between two points depends only on the endpoints, not the route. You can deform contours at will to avoid obstructions, simplify geometry, or pick a path that's easy to compute — as long as you don't cross a singularity. This deformation principle is the workhorse of all subsequent complex analysis: Cauchy's integral formula, Taylor and Laurent series, and the residue theorem all rely on it.
