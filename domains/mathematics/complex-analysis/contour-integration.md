---
id: contour-integration
title: Contour Integration
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-line-integrals
  type: hard
builds-toward:
- cauchys-theorem
- residue-theorem
tags:
- contour-integrals
- closed-paths
- circulation
stage: advanced
status: draft
---

# Contour Integration

## Core Idea
A contour integral is the integral of f(z) around a closed path γ, written ∮_γ f(z) dz. For holomorphic f on a simply connected domain, any closed contour integral is zero — a consequence of Cauchy's theorem. For f with isolated singularities, the contour integral picks up 2πi times the sum of residues inside, the foundation of the residue theorem.

## Questions

```yaml
- question: "Let f(z) = 1/(z − 2). You integrate f counterclockwise around a circle of radius 3 centered at the origin. What is the value of ∮ f(z) dz?"
  type: multiple-choice
  options:
    - "0 — f has a singularity, so Cauchy's theorem does not apply and the integral cannot be computed"
    - "2πi — the pole at z = 2 lies inside the contour, contributing 2πi times the residue, which equals 1"
    - "6πi — the residue is multiplied by the radius of the contour"
    - "πi — because the pole is not at the center of the contour, only half the residue contributes"
  answer: 1
  explanation: "The residue theorem: ∮ f(z) dz = 2πi × Σ(residues inside γ). The only singularity of f(z) = 1/(z−2) is at z = 2, which lies inside the circle of radius 3 centered at the origin. The residue of 1/(z−2) at z = 2 is lim(z→2)(z−2) · 1/(z−2) = 1. So the integral equals 2πi × 1 = 2πi. The radius of the contour is irrelevant — what matters is only which singularities are inside the contour and their residues. This is the power of the residue theorem: the value is determined entirely by what's inside."

- question: "Let f(z) = 1/(z² + 1) = 1/((z − i)(z + i)). Evaluated counterclockwise around a circle of radius 2 centered at the origin, ∮ f(z) dz equals:"
  type: multiple-choice
  options:
    - "0 — f is holomorphic everywhere on and inside the circle since it has no singularities there"
    - "2πi — only the pole at z = i lies inside the contour"
    - "0 — both poles z = i and z = −i lie inside the contour, but their residues are equal and opposite, summing to zero"
    - "4πi — both poles lie inside the contour and each contributes 2πi"
  answer: 2
  explanation: "Both poles z = i and z = −i lie inside the circle of radius 2. Res(f, i) = lim(z→i)(z−i) · 1/((z−i)(z+i)) = 1/(2i). Res(f, −i) = lim(z→−i)(z+i) · 1/((z−i)(z+i)) = 1/(−2i) = −1/(2i). Sum of residues = 1/(2i) − 1/(2i) = 0. So ∮ f(z) dz = 2πi × 0 = 0. The integral is zero even though f has singularities inside the contour — because the residues cancel. This shows that zero contour integral does NOT necessarily mean f is holomorphic inside; the residues may simply cancel."

- question: "For a holomorphic function f on a simply connected domain, the value of ∮_γ f(z) dz depends on the shape and size of the closed contour γ."
  type: true-false
  answer: false
  explanation: "By Cauchy's theorem, if f is holomorphic throughout the region bounded by γ (and on γ itself), then ∮_γ f(z) dz = 0, regardless of the shape, size, or placement of γ. A large square, a tiny circle, a wiggly path — any closed contour in a region where f has no singularities gives the same answer: zero. The shape of the contour matters only in that it determines *which singularities lie inside* — and hence which residues contribute. For a holomorphic function, there are no singularities, so the answer is always zero."

- question: "A singularity of f(z) located strictly inside a closed contour γ can affect the value of ∮_γ f(z) dz, even though γ never passes through the singularity."
  type: true-false
  answer: true
  explanation: "This is the topological heart of contour integration. The path γ goes around the singularity, never touching it, yet the value of the integral reflects the singularity's residue. The singularity contributes 2πi × Res(f, z₀) to the integral, detectable by any closed path that winds around it once counterclockwise. This is a fundamentally non-local property with no analogue in real single-variable calculus, where the integral between two points depends only on the path, not on what lies in nearby regions."

- question: "Explain in your own words why ∮_γ (1/z) dz = 2πi around the unit circle, even though the unit circle never passes through the singularity at z = 0."
  type: short-answer
  answer: "The function 1/z has a simple pole at z = 0 with residue 1. As the unit circle winds once counterclockwise around the origin, it 'sees' the singularity topologically — the path encloses z = 0. The residue theorem tells us the integral equals 2πi times the residue, so 2πi × 1 = 2πi. This can be verified directly: parameterize as z = e^(iθ), dz = ie^(iθ) dθ, and ∮ (1/z) dz = ∫₀^(2π) e^(−iθ) · ie^(iθ) dθ = ∫₀^(2π) i dθ = 2πi. The path doesn't touch z = 0, but by going around it, the integral accumulates a contribution from the singularity's local behavior — specifically, the 1/z term that doesn't cancel when integrated over a full loop."
  explanation: "Contrast with f(z) = z: ∮ z dz = 0 around any closed path, because z is holomorphic everywhere. The 2πi answer for 1/z is a signature of the singularity at the origin. The residue theorem systematizes this: any meromorphic function can be decomposed into a holomorphic part (contributing 0 to any closed integral) and polar parts near each singularity (contributing 2πi × residue for each enclosed singularity)."
```

## Explainer

Complex line integrals, which you just studied, allow you to integrate f(z) along any path in the complex plane connecting two endpoints. A **contour integral** is a special case: the path is **closed**, meaning it starts and ends at the same point. The notation ∮_γ f(z) dz emphasizes this closure. What makes the closed-path case special is that the topology of what lies *inside* the path determines the value of the integral — something with no direct analogue in single-variable real calculus.

The foundational fact is that if f is **holomorphic** (complex-differentiable) everywhere inside and on the closed curve γ, then ∮_γ f(z) dz = 0. This is Cauchy's theorem, which you will prove next. Holomorphic functions have no "sources" or "circulation" — if the function is smooth throughout the enclosed region, the integral detects nothing. But the moment f has an isolated **singularity** (a point where it is undefined or not differentiable) inside the contour, the integral need not vanish. The contour path never passes through the singularity, yet the integral "feels" it through the surrounding behavior of f.

The mechanism is the **residue**: a number associated with each isolated singularity that captures the leading singular behavior of f near that point. For a simple pole at z = z₀ (a singularity where f(z) ≈ c/(z − z₀) near z₀), the residue is lim(z→z₀) (z − z₀)f(z). To see this concretely: consider f(z) = 1/z and a unit circle γ centered at the origin. Parameterize as z = e^(iθ), dz = ie^(iθ) dθ, and compute ∮ (1/z) dz = ∫₀^(2π) (e^(−iθ)) · ie^(iθ) dθ = ∫₀^(2π) i dθ = 2πi. This equals 2πi times the residue of 1/z at z = 0, which is 1. The closed path has gone around the singularity once and picked up its full contribution.

The **residue theorem** generalizes this: ∮_γ f(z) dz = 2πi · Σ(residues of f at singularities inside γ), where each residue is weighted by the number of times γ winds around that singularity. This turns contour integration into a largely algebraic problem — locate the singularities inside the contour, compute each residue, sum them, multiply by 2πi. The theorem's real power emerges when you use cleverly chosen contours to evaluate definite real integrals like ∫₋∞^∞ 1/(1+x²) dx that are difficult or impossible to compute by elementary antiderivatives.
