---
id: conservative-fields-potential
title: Conservative Vector Fields and Potential Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: fundamental-theorem-line-integrals
  type: hard
builds-toward:
- curl-and-divergence
tags:
- conservative-fields
- potential-functions
- path-independence
stage: formal-systems
status: validated
---

# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if F = ∇f for some potential function f. Conservative fields have zero curl (∇ × F = 0 for continuous partials) and satisfy the property that ∮_C F · dr = 0 for any closed curve C. Magnetic fields are irrotational models of conservation.

## Questions

```yaml
- question: "A vector field F has zero curl everywhere in the plane except at the origin. Which statement best describes F?"
  type: multiple-choice
  options:
    - "F is conservative everywhere in the plane"
    - "F is conservative on any region that does not contain the origin"
    - "F is conservative on any region that does not encircle the origin"
    - "F cannot be conservative anywhere since its curl is not zero everywhere"
  answer: 2
  explanation: "Zero curl on a simply-connected region is sufficient for F to be conservative there. A region that does not *encircle* the origin is simply connected (no holes). A region that forms an annulus around the origin is not simply connected, and F may fail to be conservative on it even though curl F = 0. Option A is wrong because a circle around the origin gives a nonzero line integral. Option B is subtly wrong: not containing the origin is not the same as not encircling it."

- question: "You compute ∫_C F · dr for a path C from A to B and get 5. A colleague takes a completely different path from A to B and also gets 5. What can you conclude?"
  type: multiple-choice
  options:
    - "Nothing — two paths agreeing once is a coincidence"
    - "F is likely conservative — the integrals would agree for any path from A to B"
    - "F has zero curl at every point"
    - "A potential function exists and f(B) − f(A) = 5"
  answer: 1
  explanation: "Two instances of path-independence are consistent with F being conservative but do not prove it. If F were conservative, *every* path from A to B would give the same value. You cannot conclude D (existence of a potential function) from two data points alone, and you cannot conclude C (zero curl) without either checking curl directly or verifying path-independence holds universally. The data is suggestive, not conclusive."

- question: "For a vector field F with continuous partial derivatives on all of R³, F is conservative if and only if its curl is zero."
  type: true-false
  answer: true
  explanation: "R³ is simply connected — it has no holes or tunnels — so the central equivalence theorem applies in full: zero curl is both necessary and sufficient for F to be conservative. This equivalence breaks down on domains with topological holes (such as R² minus the origin), but on all of R³ the four conditions (F = ∇f, path-independence, zero closed-loop integral, zero curl) are all equivalent."

- question: "A vector field F satisfies curl F = 0 everywhere on R² except at the origin. Then F is conservative."
  type: true-false
  answer: false
  explanation: "Zero curl away from the origin does not guarantee F is conservative on R² minus the origin. The classic counterexample is F = ⟨−y, x⟩/(x² + y²): its curl is zero everywhere except the origin, but ∮_C F · dr = 2π for any circle C enclosing the origin. R² minus the origin is not simply connected — closed curves that encircle the origin cannot be contracted to a point, which is exactly the topological obstruction that allows curl-free fields to fail path-independence."

- question: "Why does the equivalence between 'zero curl' and 'conservative field' require the domain to be simply connected? Give an example illustrating what can go wrong."
  type: short-answer
  answer: "On a domain with holes, there exist closed curves that cannot be shrunk to a point. A field can have zero curl at every point yet still have nonzero circulation around a hole. The classic example: F = ⟨−y, x⟩/(x² + y²) has zero curl on R² \\ {0}, but integrating F around a unit circle centered at the origin gives 2π ≠ 0. Simply-connected domains rule out such topological obstructions by ensuring every closed curve bounds a surface lying entirely in the domain, so Stokes' theorem can equate circulation to the (zero) surface integral of curl F."
  explanation: "Zero curl means the field is locally a gradient (no rotation at any point), but global path-independence also requires that every closed loop can be filled by a surface inside the domain. Holes prevent this for loops that encircle them. Simply connected is the precise topological condition guaranteeing that no such obstructing loops exist."
```

## Explainer

The **Fundamental Theorem for Line Integrals** — your prerequisite — says that if F = ∇f, then ∫_C F · dr = f(B) − f(A), where A and B are the endpoints of C. This is the multivariable analogue of the Fundamental Theorem of Calculus: the line integral depends only on the values of f at the endpoints, not on the path taken. A **conservative vector field** is precisely one for which this path-independence holds. The name "conservative" comes from physics: in a conservative force field, the work done moving a particle depends only on start and end position, so energy is conserved (no energy is gained or lost by taking a roundabout path).

The central equivalence theorem (in a simply-connected domain) is: F is conservative ↔ F = ∇f for some scalar **potential function** f ↔ ∮_C F · dr = 0 for every closed curve C ↔ the curl of F is zero (∇ × F = 0). Each of these four conditions implies all the others. Zero curl is the easiest to check computationally — it only requires partial derivatives. For F = ⟨P, Q, R⟩, the condition is ∂P/∂y = ∂Q/∂x, ∂P/∂z = ∂R/∂x, ∂Q/∂z = ∂R/∂y. In R² this reduces to ∂P/∂y = ∂Q/∂x.

When you have confirmed F is conservative and want to find the potential function f, the method is systematic: since F = ∇f means ∂f/∂x = P, ∂f/∂y = Q, ∂f/∂z = R, integrate the first component with respect to x (introducing a function of y and z as the "constant"), then differentiate with respect to y and match against Q to pin down that function, then differentiate with respect to z to pin down any remaining constant. Each integration step is like running the Fundamental Theorem of Calculus in one variable while treating others as parameters.

The condition that the domain is **simply connected** — containing no "holes" — is crucial. A vector field with zero curl on a domain with holes (like R² minus the origin) may fail to be conservative globally, even though it locally looks like a gradient field. The classic example is F = ⟨−y, x⟩/(x² + y²), which has zero curl away from the origin but whose line integral around a circle enclosing the origin is nonzero. This is why simply-connected domains are required in the equivalence theorem: holes allow closed paths that cannot be contracted to a point, which is exactly the topological obstruction to path-independence.
