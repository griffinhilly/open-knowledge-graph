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
status: draft
---

# Conservative Vector Fields

## Core Idea
A vector field F is conservative if F = ∇f for some potential f. Line integrals are path-independent: ∫_C F · dr = f(endpoint) - f(startpoint). In 2D, F = (P, Q) is conservative iff P_y = Q_x.

## Explainer

Think about lifting a book: whether you carry it straight up, take the scenic route around the room, or move it in a spiral, the work done against gravity is the same — it depends only on the height change. Gravity is **conservative** in exactly this sense: the work integral depends only on the starting and ending points, not the path taken. A conservative vector field is one that behaves like gravity — any line integral through it depends only on where you start and end.

The mathematical structure behind this is a **potential function** f — a scalar function whose gradient equals the field: F = ∇f. Think of f as a landscape: its gradient at every point is the steepness and direction of uphill. The field F tells you how the landscape slopes; moving through F is like moving through that terrain. The Fundamental Theorem of Line Integrals makes this precise: ∫_C F · dr = f(endpoint) − f(startpoint). The integral telescopes to two evaluations of f, making the path irrelevant. This is the exact multivariable analogue of the single-variable Fundamental Theorem, where ∫_a^b f'(x) dx = f(b) − f(a).

Testing conservativity without finding f uses the **curl criterion**. In 2D, write F = ⟨P, Q⟩. If F = ∇f, then P = ∂f/∂x and Q = ∂f/∂y. Differentiating: ∂P/∂y = ∂²f/∂y∂x and ∂Q/∂x = ∂²f/∂x∂y. By the equality of mixed partial derivatives, these must match: ∂P/∂y = ∂Q/∂x. This is the **cross-partial condition**. On a simply connected region (no holes), it is also sufficient — if the cross-partials match, the field is conservative. The condition fails for fields like F = ⟨−y, x⟩/(x² + y²) on the punctured plane, where the domain has a hole that creates topological obstruction.

Recovering f from a conservative field is systematic. Integrate P with respect to x to get f = ∫P dx + g(y), where g(y) is an unknown function of y alone. Then differentiate this expression with respect to y, set equal to Q, and solve for g'(y). The cross-partial condition guarantees this system is consistent. Conservative fields arise throughout physics (gravitational and electric fields are both conservative), and identifying them is valuable precisely because the Fundamental Theorem eliminates the need to parametrize and compute the integral — you just evaluate the potential function at two points.
