---
id: conservative-fields
title: Conservative Vector Fields and Potential Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: line-integrals-vector-fields
  type: hard
- id: gradient-vector
  type: hard
- id: partial-derivatives
  type: hard
- id: directional-derivatives
  type: soft
builds-toward:
- fundamental-theorem-line-integrals
- greens-theorem
- stokes-theorem
tags:
- conservative
- potential-function
- path-independence
- exact-differential
stage: formal-systems
status: validated
---
# Conservative Vector Fields and Potential Functions

## Core Idea
A vector field F is conservative if ∫_C F · dr is independent of the path from start to end — it depends only on the endpoints. F is conservative if and only if F = ∇f for some scalar potential function f. For F = ⟨P, Q⟩ in a simply connected domain, the test for conservativeness is ∂P/∂y = ∂Q/∂x (the mixed partial equality condition). A conservative field does zero net work around any closed loop: ∮_C F · dr = 0.

## How It's Best Learned
The equivalences — path independence, zero circulation on closed loops, existence of a potential function, and the curl test — should all be presented together. Visualize: a conservative field is like a gravitational field where the work against gravity equals the change in potential energy regardless of the route taken. Finding the potential function requires integrating and comparing partial derivatives.

## Common Misconceptions
- ∂P/∂y = ∂Q/∂x is necessary but only sufficient when the domain is simply connected (no holes). On domains with holes, this test can fail to detect non-conservative fields.
- A conservative field has zero curl everywhere; the converse is true only on simply connected domains.
- The potential function f is determined only up to a constant: if F = ∇f, then F = ∇(f + C) for any constant C.

## Questions

```yaml
- question: "A vector field F = ⟨P, Q⟩ is defined on ℝ² minus the origin. A student checks that ∂P/∂y = ∂Q/∂x everywhere on the domain and concludes that F must be conservative. Is this reasoning valid?"
  type: multiple-choice
  options:
    - "Yes — the mixed partial test is both necessary and sufficient for conservativeness"
    - "No — the domain has a hole; the mixed partial test is necessary but not sufficient on non-simply-connected domains"
    - "No — the mixed partial test only works in three dimensions, not two"
    - "Yes — as long as F is smooth, equal mixed partials guarantee path independence on any domain"
  answer: 1
  explanation: "The mixed partial test (∂P/∂y = ∂Q/∂x) is sufficient only on simply connected domains — regions with no holes where every closed loop can be shrunk to a point. ℝ² minus the origin has a hole. On such domains, a field can satisfy the mixed partial condition everywhere yet still fail to be conservative, because a loop encircling the hole cannot be contracted. The classic example is F = ⟨−y/(x²+y²), x/(x²+y²)⟩, which passes the mixed partial test but gives ∮ F · dr = 2π around the origin."

- question: "You have confirmed that F is conservative with potential function f. You want to compute the work done by F along a curve from A = (1, 0) to B = (3, 4). Which statement is correct?"
  type: multiple-choice
  options:
    - "You must parameterize the specific curve and evaluate ∫ F · dr directly"
    - "The work equals f(B) − f(A), regardless of which path connects A to B"
    - "The work is zero, because conservative fields do no work on any path"
    - "You need to choose the shortest path to minimize the work integral"
  answer: 1
  explanation: "Path independence is the defining property of a conservative field: the work integral ∫_C F · dr depends only on the endpoints, not the path. With a potential function f in hand, the Fundamental Theorem for Line Integrals gives the work as f(B) − f(A) — no parameterization needed. Option C confuses 'conservative' with 'zero work'; a conservative field does zero work on closed loops, not on all paths. Option A describes the brute-force approach that works for any field but misses the elegance of the conservative case."

- question: "If F = ∇f is a conservative vector field, then ∮_C F · dr = 0 for every closed curve C in the domain."
  type: true-false
  answer: true
  explanation: "This is one of the four equivalent characterizations of a conservative field. Since going around a closed loop returns to the starting point, and the work equals f(end) − f(start), we get f(A) − f(A) = 0 for any closed curve. This is why conservative fields are physically associated with energy conservation — lifting a mass and returning it to the same height costs zero net work against gravity, which is a conservative field."

- question: "A conservative vector field has a unique potential function f — there is exactly one f such that F = ∇f."
  type: true-false
  answer: false
  explanation: "The potential function is determined only up to an additive constant. If F = ∇f, then F = ∇(f + C) for any constant C, since ∇C = 0. This means there is an infinite family of valid potential functions differing by constants. To specify a unique potential, you must impose a normalization condition — for example, requiring f = 0 at a reference point. This is directly analogous to indefinite integration, where ∫f dx + C acknowledges the same ambiguity."

- question: "Explain why the mixed partial test (∂P/∂y = ∂Q/∂x) can fail to identify a non-conservative field, and what condition on the domain ensures the test is sufficient."
  type: short-answer
  answer: "The test can fail on domains with holes — regions that are not simply connected. On such domains, a field can satisfy ∂P/∂y = ∂Q/∂x everywhere yet still have a non-zero loop integral around a hole, because the hole prevents certain loops from being contracted to a point. The condition that makes the test sufficient is simple connectedness: every closed loop in the domain can be continuously shrunk to a point. On simply connected domains (like all of ℝ² or a convex region), equal mixed partials guarantee a potential function exists and the field is conservative."
  explanation: "The deeper reason is Stokes' theorem: on a simply connected domain, a field with zero curl (∂P/∂y = ∂Q/∂x) integrates to zero around every loop because every loop bounds a region over which the curl integrates. When the domain has a hole, some loops don't bound any region in the domain — the integral around them is not constrained to zero by the curl condition alone."
```

## Explainer

From your study of line integrals, you know that ∫_C F · dr computes the work done by a vector field F along a curve C, and this integral generally depends on the path taken. A **conservative vector field** is the special case where path does not matter: for any two curves connecting the same endpoints, the work integral is identical. Equivalently, any closed-loop integral ∮_C F · dr = 0 — going around a loop and returning to start nets zero work. The physical analogy is gravity or electrostatics: the work to lift a mass from ground level to height h is mgh regardless of which zigzag path you take. Path-independence is what distinguishes these "well-behaved" fields from general ones.

You also know the gradient vector ∇f from your partial derivatives work. A vector field F is conservative if and only if it equals the gradient of some scalar **potential function** f: F = ∇f = ⟨∂f/∂x, ∂f/∂y⟩. When a potential function exists, path-independence is immediate: by the chain rule, the work from point A to point B equals f(B) − f(A), just like the single-variable Fundamental Theorem of Calculus. The potential is determined only up to a constant — ∇(f + C) = ∇f for any constant C — so there is a whole family of valid potentials, and you should always specify the constant (often by setting f = 0 at a reference point) when a unique answer is needed.

To test whether F = ⟨P, Q⟩ is conservative without finding f explicitly, use the **mixed partial test**: if F = ∇f, then P = ∂f/∂x and Q = ∂f/∂y. Clairaut's theorem guarantees ∂P/∂y = ∂²f/∂y∂x = ∂²f/∂x∂y = ∂Q/∂x. So ∂P/∂y = ∂Q/∂x is necessary. It is also sufficient on **simply connected domains** — regions with no holes, where every closed loop can be continuously shrunk to a point. On domains with holes (such as ℝ² minus the origin), a field can satisfy the mixed partial test everywhere yet still fail to be conservative, because a loop encircling the hole cannot be contracted.

To find the potential function when F is confirmed conservative, integrate P with respect to x (treating y as a constant): f(x, y) = ∫P dx + g(y). Then differentiate the result with respect to y and set it equal to Q to determine g(y). This pins down any y-dependent terms that were invisible in the x-integration. The four characterizations — F = ∇f, path-independence, zero circulation on closed loops, and equal mixed partials — are all equivalent on simply connected domains. Each framing is most useful for different problems, and recognizing them as the same property is the key insight that makes conservative fields the clean foundation for Green's theorem and Stokes' theorem.
