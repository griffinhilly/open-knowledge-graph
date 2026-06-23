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
- id: connected-simply-connected-plane
  type: hard
builds-toward:
- cauchys-integral-formula
- fundamental-theorem-algebra-complex
tags:
- cauchys-theorem
- holomorphic
- closed-contours
stage: advanced
status: validated
---

# Cauchy's Theorem

## Core Idea
If f is holomorphic on a simply connected domain D and γ is any closed contour in D, then ∮_γ f(z) dz = 0. This is the cornerstone of complex analysis: it implies line integrals of holomorphic functions are path-independent, and it leads directly to Cauchy's integral formula, Taylor series, and residue methods. The proof uses Green's theorem and the Cauchy-Riemann equations.

## How It's Best Learned
Verify this for f(z) = z² around a circle; integrate directly and use the theorem to check both give zero. Try f(z) = 1/z around a circle centered at the origin; the theorem does NOT apply (f is not holomorphic at 0), and the integral is nonzero.

## Common Misconceptions
Assuming Cauchy's theorem applies to all functions; it requires holomorphicity and a simply connected domain. Forgetting that the domain must be simply connected; on multiply-connected domains with holes, the integral can be nonzero.

## Questions

```yaml
- question: "You integrate f(z) = 1/z along a circular contour centered at the origin. Cauchy's theorem says the integral must be zero — true or false?"
  type: multiple-choice
  options:
    - "True — 1/z is a complex function, and Cauchy's theorem applies to all complex functions on closed contours"
    - "False — the theorem requires holomorphicity, and 1/z has a singularity at z = 0 inside the contour"
    - "True — the contour is closed, which is the only condition the theorem requires"
    - "False — but only because the contour must be a straight line, not a circle"
  answer: 1
  explanation: "Cauchy's theorem requires f to be holomorphic on a simply connected domain containing the contour. Since 1/z has a singularity at z = 0, it is not holomorphic on any domain that includes the origin. Integrating 1/z around a circle enclosing the origin gives 2πi ≠ 0 — a foundational counterexample. Options A and C represent the common misconception that the theorem applies to all complex functions."

- question: "A function f is holomorphic everywhere except at two points inside a domain. You integrate f around a closed contour that encircles both singularities. Why does Cauchy's theorem fail?"
  type: multiple-choice
  options:
    - "The contour must be a circle for the theorem to apply"
    - "The domain is not simply connected — the singularities act as holes through which the contour cannot be contracted to a point"
    - "Cauchy's theorem only applies when the contour encloses no singularities and the function is holomorphic outside"
    - "The theorem still applies; the integral will be zero because f is holomorphic on the contour itself"
  answer: 1
  explanation: "Simple connectivity is the key geometric requirement: any loop in the domain must be contractible to a point without leaving the domain. Singularities inside the domain create 'holes' that prevent this contraction. The contour shape (circle, square, etc.) is irrelevant — only topology matters. Option D is wrong because holomorphicity *on* the contour is insufficient; f must be holomorphic *throughout* the interior."

- question: "The function f(z) = z² is holomorphic on the entire complex plane (it is entire). Therefore ∮_γ z² dz = 0 for any closed contour γ in ℂ."
  type: true-false
  answer: true
  explanation: "Because z² is entire (holomorphic everywhere with no singularities), the complex plane is a simply connected domain and Cauchy's theorem applies. The integral around any closed contour is exactly zero. This is in sharp contrast to 1/z, which has a singularity at the origin and gives a nonzero integral around contours enclosing that singularity."

- question: "Cauchy's theorem states that the integral of any complex function around any closed contour equals zero."
  type: true-false
  answer: false
  explanation: "This overstates the theorem. Two conditions are required: the function must be *holomorphic* (complex-differentiable throughout the relevant region) and the domain must be *simply connected* (no holes). The classic counterexample is ∮ (1/z) dz around a circle enclosing the origin, which equals 2πi, not zero — because 1/z is not holomorphic at z = 0."

- question: "Explain why the simply connected condition in Cauchy's theorem is not merely a technical formality. Use the example of f(z) = 1/z to illustrate what goes wrong when it fails."
  type: short-answer
  answer: "Simple connectivity guarantees that any closed loop can be continuously shrunk to a point without leaving the domain — meaning there are no 'holes.' For 1/z on the punctured plane ℂ \\ {0}, the origin is a singularity that creates a hole: a loop enclosing the origin cannot be contracted past it. The proof of Cauchy's theorem uses Green's theorem and the Cauchy-Riemann equations, which require the integrand to be well-defined and holomorphic everywhere inside the contour. When a singularity is enclosed, those conditions fail at the singularity, and the integral picks up a nonzero contribution — exactly 2πi per enclosed pole of 1/z. This failure is precisely what makes residue theory possible: nonzero contour integrals encode information about the singularities enclosed."
  explanation: "Simple connectivity is the topological condition that makes the proof go through. Without it, the homotopy argument breaks down: you cannot deform the contour to a point without crossing the singularity. The fact that ∮ (1/z) dz = 2πi is not an exception to be dismissed — it is the gateway to the entire residue theorem and complex integration methods used across physics and engineering."
```

## Explainer

**Cauchy's theorem** is the central miracle of complex analysis: if a function is holomorphic (complex-differentiable everywhere) on a simply connected domain, then its integral around any closed loop in that domain is exactly zero. This sounds like a technical statement, but its consequences are profound — it's what makes complex analysis structurally different from real analysis and enables the powerful residue methods used throughout physics and engineering.

To understand why this is surprising, recall your prerequisite: contour integration. A contour integral ∮_γ f(z) dz measures, loosely, the total "circulation" of f around the path γ. For a real function, the value of a line integral generally depends on the path taken. Cauchy's theorem says that for holomorphic functions, path doesn't matter at all — any closed loop integrates to zero. This is the complex analogue of a conservative vector field in multivariable calculus, and the proof makes this connection explicit: via Green's theorem and the **Cauchy-Riemann equations** (which holomorphicity requires), the integrand reduces to a sum of terms that each vanish identically.

The simply connected condition is not a technical footnote — it's load-bearing. A simply connected domain is one with no "holes": any loop can be continuously contracted to a point without leaving the domain. Consider f(z) = 1/z, which is holomorphic everywhere except at z = 0. On the punctured plane ℂ \ {0}, the domain has a hole at the origin. Integrating 1/z around a circle that encloses the origin gives 2πi ≠ 0. The theorem fails because the domain is not simply connected. This is precisely why the theory of residues is interesting: the nonzero contributions from such loops come entirely from the singularities enclosed, making it possible to compute real integrals by tracking complex poles.

Path-independence is the practical payoff for computations. Since ∮_γ f(z) dz = 0 for any closed loop, the integral of a holomorphic function between two points depends only on the endpoints, not the route. You can deform contours at will to avoid obstructions, simplify geometry, or pick a path that's easy to compute — as long as you don't cross a singularity. This deformation principle is the workhorse of all subsequent complex analysis: Cauchy's integral formula, Taylor and Laurent series, and the residue theorem all rely on it.
