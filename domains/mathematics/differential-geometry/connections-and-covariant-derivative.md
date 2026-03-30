---
id: connections-and-covariant-derivative
title: Connections and Covariant Derivative
domain: mathematics
course: differential-geometry
prerequisites:
  - id: vector-fields-differential-geometry
    type: hard
  - id: tangent-vectors-and-tangent-spaces
    type: hard
  - id: riemannian-metrics
    type: soft
  - id: lie-brackets
    type: soft
tags:
  - connection
  - covariant-derivative
  - christoffel-symbols
  - affine-connection
stage: expert
status: validated
---

# Connections and Covariant Derivative

## Core Idea
A connection (or covariant derivative) ∇ provides a way to differentiate vector fields along curves on a manifold — something that requires additional structure beyond the smooth structure because there is no canonical way to compare tangent vectors at different points. The covariant derivative ∇_X Y measures how Y changes as you move along X, and it is determined in coordinates by the Christoffel symbols Γᵏᵢⱼ. Unlike the Lie bracket, the covariant derivative is tensorial in its first argument, making it the right tool for defining parallel transport and curvature.

## Questions

```yaml
- question: "Why can't you simply differentiate a vector field Y in the direction of X using the ordinary directional derivative X(Yⁱ)∂/∂xⁱ?"
  type: multiple-choice
  options:
    - "Because vector fields are not functions and cannot be differentiated"
    - "Because the expression X(Yⁱ)∂/∂xⁱ is not coordinate-independent — it transforms incorrectly under coordinate changes"
    - "Because the directional derivative of a vector field is always zero"
    - "Because X and Y live in different tangent spaces and cannot interact"
  answer: 1
  explanation: "The expression X(Yⁱ)∂/∂xⁱ differentiates the components of Y, but the basis vectors ∂/∂xⁱ also change from point to point. The 'naive' derivative misses the change in the basis vectors, and the result is not a tensor — it does not transform correctly under coordinate changes. A connection adds the correction term Γᵏᵢⱼ Xⁱ Yʲ that accounts for how the basis vectors twist as you move. The full covariant derivative is (∇_X Y)ᵏ = X(Yᵏ) + Γᵏᵢⱼ Xⁱ Yʲ, which transforms as a vector."

- question: "An affine connection ∇ on a manifold is uniquely determined by the Riemannian metric."
  type: true-false
  answer: false
  explanation: "A smooth manifold admits infinitely many connections. What IS unique is the Levi-Civita connection — the one that is both torsion-free (∇_X Y - ∇_Y X = [X,Y]) and metric-compatible (∇g = 0). The Fundamental Theorem of Riemannian Geometry states that given a Riemannian metric, there exists a unique such connection. But other connections exist: connections with torsion appear in Einstein-Cartan theory, and non-metric connections arise in affine differential geometry."

- question: "The Christoffel symbols Γᵏᵢⱼ are the components of a tensor."
  type: true-false
  answer: false
  explanation: "The Christoffel symbols do NOT transform as tensor components. Under a coordinate change x → x', they transform as Γ'ᵏᵢⱼ = (∂x'ᵏ/∂xˡ)(∂xᵐ/∂x'ⁱ)(∂xⁿ/∂x'ʲ)Γˡₘₙ + (∂x'ᵏ/∂xˡ)(∂²xˡ/∂x'ⁱ∂x'ʲ). The second term — involving second derivatives of the coordinate transformation — is the non-tensorial part. It is precisely this non-tensorial term that cancels the non-tensorial part of the naive derivative X(Yⁱ), making the full covariant derivative ∇_X Y a well-defined tensor. The difference of two connections IS a tensor, which is why the space of connections is an affine space."

- question: "A connection ∇ on a manifold must satisfy three algebraic properties. Which property distinguishes it from the Lie bracket?"
  type: short-answer
  answer: "C∞(M)-linearity in the first argument: ∇_{fX} Y = f∇_X Y for any smooth function f. The Lie bracket fails this — [fX, Y] = f[X,Y] - Y(f)X has an extra term. Both operations are ℝ-linear in both arguments and satisfy a Leibniz rule in the second argument (∇_X(fY) = X(f)Y + f∇_X Y). But the C∞(M)-linearity in X makes ∇_X Y depend only on the value of X at a point, not its derivatives — this is tensoriality in the first slot."
  explanation: "This tensoriality means (∇_X Y)_p depends only on X_p (the value of X at p) and on Y along a curve tangent to X at p. The Lie bracket [X,Y]_p depends on the derivatives of both X and Y. This makes the covariant derivative the right tool for defining parallel transport (which should depend on the direction of transport, not on how the direction field extends away from the curve)."
```

## Explainer

On ℝⁿ with standard coordinates, differentiating a vector field Y = Yⁱ eᵢ in the direction X is straightforward: you differentiate the components X(Yⁱ). This works because the standard basis vectors eᵢ are constant — they do not change from point to point. On a curved manifold, the coordinate basis vectors ∂/∂xⁱ vary from chart to chart, and there is no canonical notion of "constant vector field." A **connection** provides the missing ingredient: it specifies how to transport vectors infinitesimally from one tangent space to a nearby one.

A **covariant derivative** (affine connection) is an operation ∇ : 𝔛(M) × 𝔛(M) → 𝔛(M) satisfying: (1) ∇_{fX+gY} Z = f∇_X Z + g∇_Y Z (C∞(M)-linear in the first argument), (2) ∇_X(Y+Z) = ∇_X Y + ∇_X Z (additive in the second argument), and (3) ∇_X(fY) = X(f)Y + f∇_X Y (Leibniz rule in the second argument). In local coordinates, the connection is specified by its **Christoffel symbols** Γᵏᵢⱼ, defined by ∇_{∂/∂xⁱ}(∂/∂xʲ) = Γᵏᵢⱼ ∂/∂xᵏ. The covariant derivative of Y along X is then (∇_X Y)ᵏ = X(Yᵏ) + Γᵏᵢⱼ Xⁱ Yʲ — the first term differentiates components, the second corrects for the changing basis.

The C∞(M)-linearity in the first argument is the crucial property. It means (∇_X Y)_p depends only on the vector X_p ∈ TpM, not on how X extends away from p. This is what makes ∇ tensorial in its first argument — you can evaluate ∇_v Y for a single tangent vector v, which the Lie bracket cannot do. The Leibniz rule in the second argument means ∇_X Y does depend on the behavior of Y along the direction X (it sees the first derivative of Y), making it genuinely differential.

The **torsion** of a connection is T(X,Y) = ∇_X Y - ∇_Y X - [X,Y], measuring the antisymmetric part of ∇ beyond what the Lie bracket accounts for. A torsion-free connection satisfies ∇_X Y - ∇_Y X = [X,Y]. On a Riemannian manifold, the **Levi-Civita connection** is the unique torsion-free, metric-compatible connection. But connections exist independently of any metric — they are a more primitive notion than Riemannian geometry, and they are the natural structure on general vector bundles, principal bundles, and gauge theories in physics.
