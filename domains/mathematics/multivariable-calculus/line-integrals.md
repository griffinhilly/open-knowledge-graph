---
id: line-integrals
title: Line Integrals of Scalar and Vector Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-fields
  type: hard
- id: arc-length-parametric
  type: hard
- id: work-circulation
  type: soft
builds-toward:
- fundamental-theorem-line-integrals
- conservative-fields-potential
tags:
- line-integrals
- work
- circulation
stage: formal-systems
status: validated
---
# Line Integrals of Scalar and Vector Functions

## Core Idea
Line integrals ∫_C f ds (scalar) or ∫_C F · dr (vector) integrate along curves. The scalar version sums f weighted by arc length; the vector version computes work done by F along a path C. Both depend on the parametrization's orientation.

## Questions

```yaml
- question: "A wire lies along a curve C and has a variable linear density ρ(x,y) at each point. Which integral gives the total mass of the wire?"
  type: multiple-choice
  options:
    - "∫_C ρ · dr (the vector line integral of ρ along C)"
    - "∫_C ρ ds (the scalar line integral of ρ with respect to arc length)"
    - "∫_C F · dr where F is a force field equal to ρ"
    - "The ordinary integral ∫_a^b ρ(t) dt over the parameter interval"
  answer: 1
  explanation: "The scalar line integral ∫_C ρ ds is exactly the right tool: it multiplies the density at each point by the arc-length element ds, accumulating the total mass. Option A is a vector integral that computes work (requires a dot product), which doesn't apply to a scalar density. Option D omits the |r′(t)| factor that converts the parameter increment to arc length — without it, you're not measuring along the actual curve."

- question: "You traverse curve C from point A to point B and compute both ∫_C f ds and ∫_C F · dr. You then reverse direction and traverse C from B to A. What happens to each integral?"
  type: multiple-choice
  options:
    - "Both integrals are negated"
    - "Both integrals remain unchanged"
    - "The scalar integral is negated; the vector integral is unchanged"
    - "The vector integral is negated; the scalar integral is unchanged"
  answer: 3
  explanation: "Reversing orientation reverses the direction vector r′(t), which negates the dot product F · r′(t), so ∫_C F · dr changes sign. But the scalar integral uses |r′(t)| (the speed, always positive), so reversing orientation doesn't change ds — the scalar integral is unchanged. This asymmetry reflects the physics: a force that aids motion one way opposes it the other way, but a physical property like mass is the same regardless of which direction you measure the wire."

- question: "The vector line integral ∫_C F · dr measures the component of F perpendicular to the path, integrated over arc length."
  type: true-false
  answer: false
  explanation: "This is backwards. The dot product F · dr = F · r′(t) dt extracts the component of F *parallel* to (along) the direction of motion. A force perpendicular to the path does zero work — precisely because F · r′ = 0 when they are orthogonal. The scalar line integral ∫_C f ds integrates a quantity weighted by arc length, but that's a different operation entirely from projecting onto the perpendicular."

- question: "Reversing the orientation of a curve C negates both the scalar and vector line integrals over C."
  type: true-false
  answer: false
  explanation: "Only the vector line integral changes sign under orientation reversal. The scalar integral ∫_C f ds uses ds = |r′(t)| dt, which is always non-negative (it measures arc length), so reversing direction doesn't affect it. The vector integral ∫_C F · dr uses dr = r′(t) dt, which flips sign when the direction of traversal is reversed, so the integral negates."

- question: "When computing a vector line integral ∫_C F · dr via parametrization r(t), why does the factor r′(t) appear in the integrand rather than |r′(t)|?"
  type: short-answer
  answer: "The factor r′(t) dt = dr is the infinitesimal displacement vector along the curve, which encodes both the length of the tiny piece and its direction. The dot product F · r′(t) extracts how much F aligns with the direction of motion — this is work (force times displacement in the direction of motion). For the scalar integral, we only care about arc length (how long the piece is), so we use the speed |r′(t)|, which discards direction. Using r′(t) instead of |r′(t)| in the vector integral is what makes orientation matter: when you reverse the path, r′ flips sign, so the dot product changes sign."
  explanation: "The distinction between r′(t) and |r′(t)| encodes the entire difference between the two types of line integrals. Scalar integrals accumulate quantities along a curve without caring about direction; vector integrals measure directional alignment between a field and a path, which is inherently orientation-dependent."
```

## Explainer

Ordinary integrals accumulate a quantity along a straight line segment (the x-axis). Line integrals do the same thing along an arbitrary curve in space. The curve is the domain of integration, and you need a way to measure "how much" of that curve passes through each point. That is the role of **arc length** from your prerequisites: the scalar ds is an infinitesimal piece of arc length, telling you how long a tiny piece of the curve is.

The **scalar line integral** ∫_C f ds answers: if f(x,y,z) is a density or weight at each point, what is the total accumulated quantity along the curve? Imagine a wire whose linear density (mass per unit length) varies from point to point. The total mass is ∫_C ρ ds — sum up density times length element at each point along the wire. To compute this, you parametrize the curve: let r(t) for t ∈ [a,b] trace out C, then ds = |r′(t)| dt, and the integral becomes ∫_a^b f(r(t)) |r′(t)| dt — a standard single-variable integral. The factor |r′(t)| is the speed of the parametrization, which converts the parameter increment dt into actual arc length.

The **vector line integral** ∫_C F · dr asks a different question: how much does the vector field F push the path forward? The integrand F · dr picks up the component of F in the direction of motion along C. This is the **work** done by a force field F on a particle traveling along C. Using the parametrization, dr = r′(t) dt, so the integral becomes ∫_a^b F(r(t)) · r′(t) dt. The dot product F · r′(t) extracts how much F aligns with the direction of travel at each moment; integrating it gives cumulative work. When F is perpendicular to the path everywhere, this integral is zero — a force perpendicular to motion does no work.

**Orientation matters** for vector line integrals but not for scalar ones. Reversing the direction of traversal negates the vector line integral (since r′(t) reverses), but leaves the scalar integral unchanged (since |r′(t)| is always positive). This asymmetry reflects the underlying physics: a force field that aids your journey one way opposes it the other way. For conservative vector fields — those with a potential function — the vector line integral depends only on the endpoints, not the path taken. That is the content of the Fundamental Theorem for Line Integrals, which you will explore next.
