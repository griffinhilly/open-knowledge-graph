---
id: conservative-vector-fields
title: Conservative Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: conservative-fields
  type: hard
- id: fundamental-theorem-line-integrals
  type: hard
builds-toward:
- greens-theorem
- curl-divergence
tags:
- conservative
- potential
stage: formal-systems
status: validated
---

# Conservative Vector Fields

## Core Idea
A vector field F is conservative if F = ∇f for some potential f. Line integrals are path-independent: ∫_C F · dr = f(endpoint) - f(startpoint). In 2D, F = (P, Q) is conservative iff P_y = Q_x.

## Questions

```yaml
- question: "A conservative vector field F has potential function f, with f(A) = 3 and f(B) = 11. A particle travels from A to B along path C₁ (a straight line) and from A to B along path C₂ (a long curved detour). What is the work done along each path?"
  type: multiple-choice
  options:
    - "Work along C₁ equals 8; work along C₂ is larger because the particle travels a greater distance"
    - "Both equal 8, since the line integral of a conservative field depends only on the endpoints, not the path"
    - "The work depends on the particle's speed along each path, not just the endpoints"
    - "Work along C₂ equals 0 because the particle loops before reaching B"
  answer: 1
  explanation: "The Fundamental Theorem of Line Integrals states that ∫_C F·dr = f(endpoint) − f(startpoint) for any conservative field. Both paths share the same endpoints A and B, so both give f(B) − f(A) = 11 − 3 = 8. The path is completely irrelevant — its length, shape, and direction do not affect the integral. This path-independence is the defining property of conservative fields and is exactly why gravity does the same work lifting a book regardless of the route taken."

- question: "A student verifies that ∂P/∂y = ∂Q/∂x everywhere for a field F = ⟨P, Q⟩ defined on the punctured plane ℝ² \\ {(0,0)}. What can she conclude?"
  type: multiple-choice
  options:
    - "F is conservative — the cross-partial condition is both necessary and sufficient for conservativity"
    - "F is conservative on any path that avoids the origin, since the condition holds wherever F is defined"
    - "F might not be conservative — the cross-partial condition is sufficient only on simply connected domains, and removing the origin creates a topological hole that can prevent this"
    - "F is definitely not conservative, because fields with singularities are never conservative"
  answer: 2
  explanation: "The cross-partial condition (∂P/∂y = ∂Q/∂x) is necessary for conservativity and is sufficient on simply connected domains — domains with no holes. The punctured plane is not simply connected: the missing origin is a hole. The classic counterexample is F = ⟨−y, x⟩/(x²+y²), which satisfies the cross-partial condition everywhere it is defined yet has a nonzero line integral around any closed curve enclosing the origin. The hole allows a 'winding number' obstruction that makes the field non-conservative despite passing the cross-partial test."

- question: "For any conservative vector field F, the line integral ∮_C F·dr around any closed curve C equals zero."
  type: true-false
  answer: true
  explanation: "If F = ∇f, then ∮_C F·dr = f(endpoint) − f(startpoint) by the Fundamental Theorem of Line Integrals. For a closed curve, the endpoint is the same as the starting point, so the integral equals f(p) − f(p) = 0. This zero-integral property for closed curves is equivalent to path independence and is often used as the definition of a conservative field. It generalizes the observation that gravity does zero net work over any closed path."

- question: "If ∂P/∂y = ∂Q/∂x at most point in a vector field's domain, then the field is very likely to be conservative, regardless of the shape of the domain."
  type: true-false
  answer: false
  explanation: "The cross-partial condition is sufficient for conservativity only on simply connected domains. On domains with holes — like the punctured plane — the condition can hold everywhere yet the field can still be non-conservative. The field F = ⟨−y, x⟩/(x²+y²) is the standard counterexample: its cross-partials are equal on the punctured plane, but its integral around a unit circle centered at the origin equals 2π, not 0. The topological structure of the domain matters as much as the algebraic condition."

- question: "Explain in your own words why the existence of a potential function f makes line integrals path-independent. What does the Fundamental Theorem of Line Integrals say, and how is it analogous to the single-variable Fundamental Theorem of Calculus?"
  type: short-answer
  answer: "If F = ∇f, then moving through F is like moving through a landscape where f measures elevation. The work done equals the change in elevation — f(endpoint) − f(startpoint) — regardless of the route, because all paths between the same two heights change elevation by the same amount. The Fundamental Theorem of Line Integrals formalizes this: ∫_C F·dr = f(B) − f(A). The analogy to single-variable calculus is exact: ∫_a^b f'(x) dx = f(b) − f(a) because f' is the 'gradient' in 1D, and integration telescopes to endpoint evaluations. In both cases, the antiderivative (or potential function) absorbs all information about the interior of the path."
  explanation: "The key insight is that a potential function reduces a path integral — which naively depends on every point along the route — to two evaluations of a scalar function at the endpoints. This is computationally powerful: instead of parametrizing a complicated curve and computing a vector line integral, you simply find f and evaluate it at start and end. The method works only when F is conservative (F = ∇f), which is why identifying conservative fields is the first step in any line integral problem."
```

## Explainer

Think about lifting a book: whether you carry it straight up, take the scenic route around the room, or move it in a spiral, the work done against gravity is the same — it depends only on the height change. Gravity is **conservative** in exactly this sense: the work integral depends only on the starting and ending points, not the path taken. A conservative vector field is one that behaves like gravity — any line integral through it depends only on where you start and end.

The mathematical structure behind this is a **potential function** f — a scalar function whose gradient equals the field: F = ∇f. Think of f as a landscape: its gradient at every point is the steepness and direction of uphill. The field F tells you how the landscape slopes; moving through F is like moving through that terrain. The Fundamental Theorem of Line Integrals makes this precise: ∫_C F · dr = f(endpoint) − f(startpoint). The integral telescopes to two evaluations of f, making the path irrelevant. This is the exact multivariable analogue of the single-variable Fundamental Theorem, where ∫_a^b f'(x) dx = f(b) − f(a).

Testing conservativity without finding f uses the **curl criterion**. In 2D, write F = ⟨P, Q⟩. If F = ∇f, then P = ∂f/∂x and Q = ∂f/∂y. Differentiating: ∂P/∂y = ∂²f/∂y∂x and ∂Q/∂x = ∂²f/∂x∂y. By the equality of mixed partial derivatives, these must match: ∂P/∂y = ∂Q/∂x. This is the **cross-partial condition**. On a simply connected region (no holes), it is also sufficient — if the cross-partials match, the field is conservative. The condition fails for fields like F = ⟨−y, x⟩/(x² + y²) on the punctured plane, where the domain has a hole that creates topological obstruction.

Recovering f from a conservative field is systematic. Integrate P with respect to x to get f = ∫P dx + g(y), where g(y) is an unknown function of y alone. Then differentiate this expression with respect to y, set equal to Q, and solve for g'(y). The cross-partial condition guarantees this system is consistent. Conservative fields arise throughout physics (gravitational and electric fields are both conservative), and identifying them is valuable precisely because the Fundamental Theorem eliminates the need to parametrize and compute the integral — you just evaluate the potential function at two points.
