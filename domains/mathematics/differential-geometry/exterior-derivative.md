---
id: exterior-derivative
title: Exterior Derivative
domain: mathematics
course: differential-geometry
prerequisites:
  - id: differential-forms-introduction
    type: hard
  - id: partial-derivatives
    type: hard
tags:
  - exterior-derivative
  - differential-forms
  - closed-forms
  - exact-forms
stage: advanced
status: validated
---

# Exterior Derivative

## Core Idea
The exterior derivative d is a linear operator that takes k-forms to (k+1)-forms, generalizing the gradient, curl, and divergence of vector calculus into a single unified operation. It satisfies d² = 0 (applying it twice always gives zero) and the Leibniz rule d(α ∧ β) = dα ∧ β + (-1)^k α ∧ dβ. The condition d² = 0 is the geometric foundation for de Rham cohomology, connecting differential geometry to topology.

## Questions

```yaml
- question: "On ℝ³ with coordinates (x, y, z), the exterior derivative takes: 0-forms (functions) to 1-forms via df = (∂f/∂x)dx + (∂f/∂y)dy + (∂f/∂z)dz. This corresponds to which classical vector calculus operation?"
  type: multiple-choice
  options:
    - "Divergence"
    - "Curl"
    - "Gradient"
    - "Laplacian"
  answer: 2
  explanation: "The exterior derivative of a 0-form (function) on ℝ³ gives a 1-form whose components are the partial derivatives — this is exactly the gradient. Continuing the correspondence: d on 1-forms corresponds to the curl (d of a 1-form gives a 2-form whose components are the curl), and d on 2-forms corresponds to the divergence (d of a 2-form gives a 3-form whose coefficient is the divergence). The identity d² = 0 unifies curl(grad f) = 0 and div(curl F) = 0."

- question: "A differential form ω is called closed if dω = 0, and exact if ω = dα for some form α. Every exact form is closed. Is every closed form exact?"
  type: true-false
  answer: false
  explanation: "Not in general. The famous counterexample is the 1-form ω = (-y dx + x dy)/(x² + y²) on ℝ² \ {0}. It is closed (dω = 0) but not exact — its integral around the unit circle is 2π, which would be zero if ω = df for some function f. The obstruction to closed forms being exact is topological: the de Rham cohomology group Hᵏ(M) = {closed k-forms}/{exact k-forms} measures this failure. On contractible domains, the Poincaré lemma guarantees every closed form is exact."

- question: "Why does d² = 0 hold? What is the essential reason?"
  type: short-answer
  answer: "The identity d² = 0 follows from the equality of mixed partial derivatives (∂²f/∂xⁱ∂xʲ = ∂²f/∂xʲ∂xⁱ) combined with the antisymmetry of the wedge product (dxⁱ ∧ dxʲ = -dxʲ ∧ dxⁱ). When you apply d twice, symmetric second derivatives get wedged with antisymmetric basis forms, and every term cancels with its partner."
  explanation: "In coordinates: d(df) = d(∂f/∂xⁱ dxⁱ) = (∂²f/∂xʲ∂xⁱ) dxʲ ∧ dxⁱ. Since ∂²f/∂xʲ∂xⁱ is symmetric in i,j while dxʲ ∧ dxⁱ is antisymmetric, every pair of terms cancels. This extends to k-forms by the Leibniz rule. The identity d² = 0 is the manifold version of 'curl of gradient is zero' and 'divergence of curl is zero' — both of which are consequences of the same symmetry-antisymmetry cancellation."

- question: "The exterior derivative d is uniquely characterized by four properties: (1) d takes k-forms to (k+1)-forms, (2) on 0-forms, df(X) = X(f), (3) d² = 0, and (4) d(α ∧ β) = dα ∧ β + (-1)^deg(α) α ∧ dβ."
  type: true-false
  answer: true
  explanation: "These four properties (degree-raising, agreement with the differential on functions, nilpotency, and the graded Leibniz rule) uniquely determine d. This is important because it means d is coordinate-independent — any coordinate formula satisfying these axioms must give the same operator. The graded Leibniz rule (the sign (-1)^k accounts for the degree of α) ensures compatibility with the wedge product's antisymmetry."
```

## Explainer

In vector calculus on ℝ³, there are three derivative operations: gradient (scalar → vector), curl (vector → vector), and divergence (vector → scalar). They satisfy two famous identities: curl(grad f) = 0 and div(curl F) = 0. The exterior derivative unifies all three into a single operation d that works in any dimension on any manifold — and the identity d² = 0 captures both classical identities simultaneously.

On an n-manifold with local coordinates, d acts on a k-form ω = ω_{i₁...iₖ} dxⁱ¹ ∧ ... ∧ dxⁱᵏ by the formula dω = (∂ω_{i₁...iₖ}/∂xʲ) dxʲ ∧ dxⁱ¹ ∧ ... ∧ dxⁱᵏ. This is a (k+1)-form. The key properties are: **linearity**, the **graded Leibniz rule** d(α ∧ β) = dα ∧ β + (-1)^{deg α} α ∧ dβ, and **nilpotency** d² = 0. These three properties, together with the requirement that d agrees with the differential on functions, uniquely characterize d — so it is independent of the coordinate system used to compute it.

The identity d² = 0 creates a chain complex: Ω⁰(M) →d Ω¹(M) →d Ω²(M) →d ... →d Ωⁿ(M). Forms in the kernel of d (closed forms, dω = 0) contain those in the image of d (exact forms, ω = dα). The quotient Hᵏ(M) = ker d / im d is the **de Rham cohomology** — a topological invariant that measures the failure of closed forms to be exact. On ℝⁿ, every closed form is exact (the Poincaré lemma). On a torus or a punctured plane, there are closed forms that are not exact, reflecting the nontrivial topology.

The exterior derivative has a beautiful interaction with pullbacks: if F : M → N is a smooth map, then F*(dω) = d(F*ω). This **naturality** means that d commutes with smooth maps between manifolds, making it a truly geometric operation rather than a coordinate artifact. Combined with the Stokes theorem (∫_M dω = ∫_{∂M} ω), the exterior derivative connects local differential information to global integral information — the central theme of differential geometry and topology.
