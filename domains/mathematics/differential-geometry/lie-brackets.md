---
id: lie-brackets
title: Lie Brackets
domain: mathematics
course: differential-geometry
prerequisites:
  - id: vector-fields-differential-geometry
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
tags:
  - lie-bracket
  - commutator
  - vector-fields-differential-geometry
  - lie-algebra
stage: advanced
status: validated
---

# Lie Brackets

## Core Idea
The Lie bracket [X, Y] of two vector fields measures their failure to commute — both as derivations (XY - YX applied to functions) and as flows (the infinitesimal obstruction to their flows commuting). It produces a new vector field that is bilinear, antisymmetric, and satisfies the Jacobi identity. The Lie bracket turns the space of vector fields into an infinite-dimensional Lie algebra and is the foundational algebraic operation in differential geometry.

## Questions

```yaml
- question: "Given vector fields X = ∂/∂x and Y = x∂/∂y on ℝ², what is [X, Y]?"
  type: multiple-choice
  options:
    - "0 (the zero vector field)"
    - "∂/∂y"
    - "x∂/∂x"
    - "-∂/∂y"
  answer: 1
  explanation: "Computing directly: [X,Y](f) = X(Y(f)) - Y(X(f)). We have Y(f) = x·∂f/∂y, so X(Y(f)) = ∂/∂x(x·∂f/∂y) = ∂f/∂y + x·∂²f/∂x∂y. Also X(f) = ∂f/∂x, so Y(X(f)) = x·∂²f/∂x∂y (since ∂/∂y of ∂f/∂x = ∂²f/∂y∂x). The difference is ∂f/∂y. Therefore [X,Y] = ∂/∂y. The bracket is nonzero because the coefficient of Y depends on x, which X differentiates."

- question: "The Lie bracket is C∞(M)-linear in both arguments: [fX, Y] = f[X, Y] for any smooth function f."
  type: true-false
  answer: false
  explanation: "The Lie bracket is NOT C∞(M)-linear — it satisfies [fX, Y] = f[X, Y] - Y(f)·X instead. The extra term Y(f)·X arises because Y differentiates the function f. This is why the Lie bracket is not a tensor: tensorial operations are by definition C∞(M)-multilinear. The Lie bracket's failure of C∞(M)-linearity means it cannot be computed pointwise from the values of X and Y — it depends on their derivatives. This distinguishes it from operations like the metric pairing g(X,Y) which is tensorial."

- question: "The Jacobi identity states [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0. What role does this identity play in the structure of vector fields?"
  type: short-answer
  answer: "The Jacobi identity ensures that the Lie bracket makes the space of vector fields into a Lie algebra — a vector space with a bilinear, antisymmetric bracket satisfying this three-term relation. The Jacobi identity is the Lie algebra analogue of associativity for groups. It guarantees that the adjoint representation (ad_X(Y) = [X,Y]) is itself a Lie algebra homomorphism, which is essential for the theory of Lie groups and their actions on manifolds."
  explanation: "Without the Jacobi identity, the bracket would be an arbitrary antisymmetric bilinear operation, and much of the theory of Lie algebras, Lie groups, and symmetry in differential geometry would collapse. The identity can be verified by direct computation using the definition [X,Y] = XY - YX and the associativity of composition of derivations."

- question: "If the flows of two vector fields X and Y commute (φs ∘ ψt = ψt ∘ φs for all s, t), then [X, Y] = 0."
  type: true-false
  answer: true
  explanation: "This is correct, and the converse also holds: [X, Y] = 0 if and only if the flows commute. The Lie bracket [X, Y]_p can be computed as the limit lim_{t→0} (1/t²)(ψ_{-t} ∘ φ_{-t} ∘ ψ_t ∘ φ_t(p) - p), measuring the gap when you flow along X, then Y, then back along X, then back along Y. If the flows commute, this loop closes exactly and the bracket vanishes. Coordinate vector fields ∂/∂xⁱ always have vanishing brackets because the coordinate flows (translations along coordinate axes) commute."
```

## Explainer

When you compose two derivations X and Y acting on smooth functions, the result XY (meaning X applied after Y) is not itself a derivation — it involves second derivatives and fails the Leibniz rule. But the **commutator** [X, Y] = XY - YX is a derivation: the second-derivative terms cancel, leaving a first-order operator. In local coordinates where X = Xⁱ∂/∂xⁱ and Y = Yʲ∂/∂xʲ, the bracket has components [X,Y]ᵏ = Xⁱ(∂Yᵏ/∂xⁱ) - Yⁱ(∂Xᵏ/∂xⁱ). This is the **Lie bracket** of X and Y — a new vector field that captures how X and Y interact.

The geometric meaning of the Lie bracket is the failure of flows to commute. Start at a point p, flow along X for time ε, then along Y for time ε, then back along X for time ε, then back along Y for time ε. If you return exactly to p, the flows commute and [X, Y] = 0. If not, the gap is approximately ε²[X, Y]_p. The bracket measures the infinitesimal "twist" that prevents the two flows from forming a coordinate grid. This is why coordinate vector fields ∂/∂xⁱ always have vanishing brackets — their flows are precisely the coordinate translations that do form a grid.

The Lie bracket satisfies three algebraic properties: **bilinearity** ([aX + bY, Z] = a[X,Z] + b[Y,Z]), **antisymmetry** ([X,Y] = -[Y,X]), and the **Jacobi identity** ([X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0). These make the space of vector fields 𝔛(M) into a **Lie algebra** — the same algebraic structure that appears in Lie group theory, quantum mechanics, and representation theory. The Jacobi identity is not obvious from the definition but follows from direct computation using the associativity of function composition.

A critical subtlety: the Lie bracket is ℝ-bilinear but not C∞(M)-bilinear. The formula [fX, Y] = f[X,Y] - Y(f)X shows that multiplying a vector field by a function before bracketing produces an extra term. This means the Lie bracket is not a tensor — you cannot compute [X,Y]_p knowing only X_p and Y_p; you need the derivatives of the coefficient functions. This is the first instance of a pattern that recurs throughout differential geometry: the most natural operations on vector fields are often not tensorial, and identifying which operations are tensorial (and therefore define geometric objects independent of coordinates) is a central concern.
