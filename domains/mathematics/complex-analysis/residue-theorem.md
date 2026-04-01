---
id: residue-theorem
title: The Residue Theorem
domain: mathematics
course: complex-analysis
prerequisites:
- id: residues-definition-computation
  type: hard
- id: contour-integration
  type: soft
builds-toward:
- evaluating-integrals-residues
- argument-principle
tags:
- residue-theorem
- contour-integrals
- applications
stage: advanced
status: validated
---

# The Residue Theorem

## Core Idea
If f is holomorphic inside and on a closed contour γ except for finitely many isolated singularities z₁, ..., zₙ inside γ, then ∮_γ f(z) dz = 2πi Σ Res(f, zₖ). This theorem reduces a contour integral to a sum of residues, making it a powerful tool for evaluating real integrals and summing series.

## How It's Best Learned
Apply this to compute ∮_γ dz/(z²+1) around a circle of radius 2. Identify the poles, compute their residues, and verify the result matches a direct contour integral.

## Common Misconceptions
Forgetting the factor 2πi; it comes from the integral formula for a simple pole. Assuming the theorem works for multiply-connected domains without accounting for all enclosed singularities.

## Questions

```yaml
- question: "A function f(z) has isolated singularities at z = 0, z = 1+i, and z = 3. You integrate f around the circle |z−1| = 1.5. How many singularities contribute to the contour integral?"
  type: multiple-choice
  options:
    - "All 3 — the residue theorem sums over all singularities of f, regardless of position"
    - "2 — both z=0 (distance 1 from center) and z=1+i (distance 1 from center) lie inside the contour"
    - "1 — only z=1+i lies inside since it is closest to the center"
    - "0 — none of the singularities lie exactly at the center z=1"
  answer: 1
  explanation: "The residue theorem sums only over singularities enclosed by the contour. |0−1|=1 < 1.5, so z=0 is inside. |1+i−1|=|i|=1 < 1.5, so z=1+i is inside. |3−1|=2 > 1.5, so z=3 is outside. Option 0 is the classic error: position relative to the contour, not mere existence, determines which singularities contribute."

- question: "A student correctly computes Res(f, 1) + Res(f, −2) for a function with poles at z=1 and z=−2, both enclosed by the contour γ. The student announces this sum as the value of ∮_γ f(z) dz. What is missing?"
  type: multiple-choice
  options:
    - "The student must multiply the sum by 2πi to get the correct integral value"
    - "Nothing is missing — the sum of residues equals the contour integral"
    - "The student must divide by 2πi because the residues already include that factor"
    - "The student must subtract the contribution from the contour itself"
  answer: 0
  explanation: "The residue theorem states ∮_γ f(z) dz = 2πi × Σ Res(f, zₖ). The factor 2πi arises from the fundamental integral ∮ dz/(z−z₀) = 2πi and cannot be omitted. Forgetting this factor is the single most common computational error when applying the theorem. The sum of residues alone is not the integral."

- question: "A function that is holomorphic everywhere inside and on a closed contour (no singularities enclosed) must have a contour integral equal to zero."
  type: true-false
  answer: true
  explanation: "This is Cauchy's theorem, the foundation from which the Residue Theorem generalizes. If f is holomorphic (analytic) everywhere inside and on γ, there are no singularities to contribute residues, and the sum Σ Res = 0, giving ∮_γ f dz = 2πi · 0 = 0. The Residue Theorem extends this: isolated singularities are the sole sources of nonzero contour integrals."

- question: "The Residue Theorem applies primarily to functions with simple poles; it cannot be used for functions with poles of order 2 or higher."
  type: true-false
  answer: false
  explanation: "The Residue Theorem applies to any isolated singularity, including poles of any order and essential singularities. The residue is defined as the coefficient a₋₁ of the 1/(z−z₀) term in the Laurent series, regardless of pole order. For a pole of order m at z₀, the residue is computed via lim_{z→z₀} (1/(m−1)!) d^{m-1}/dz^{m-1} [(z−z₀)^m f(z)]. The theorem remains ∮_γ f dz = 2πi Σ Res(f, zₖ) in all cases."

- question: "Why does the factor 2πi appear in the residue theorem? Where does it come from?"
  type: short-answer
  answer: "It comes from the most fundamental contour integral in complex analysis: ∮_{|z−z₀|=r} 1/(z−z₀) dz = 2πi. Parametrizing with z = z₀ + re^{iθ} gives dz = ire^{iθ}dθ, and the integrand becomes (ire^{iθ})/(re^{iθ}) = i. Integrating i from 0 to 2π yields 2πi. Every pole's contribution to a contour integral ultimately reduces to a scalar multiple of this kernel integral, which is why 2πi appears universally — it is the winding number of the contour around the singularity multiplied by 2πi."
  explanation: "The 2πi factor is not an artifact of notation — it encodes the topology of the contour. The winding number of a positively oriented simple closed curve around an interior point is exactly 1, contributing one factor of 2πi. If the contour wound around a point twice, you would get 4πi. This topological interpretation is what makes the theorem so powerful: the integral depends only on which singularities are enclosed and how many times the contour winds around them."
```

## Explainer

You know from contour integration that for a holomorphic function on a simply connected domain, every closed contour integral is zero — that is Cauchy's theorem. Isolated singularities break this: they are the sole sources of nonzero contour integrals. The **Residue Theorem** makes this precise: ∮_γ f(z) dz = 2πi Σ Res(f, zₖ), where the sum runs over all isolated singularities zₖ enclosed by γ. The theorem reduces a potentially difficult integral to the algebraic task of computing residues.

The factor 2πi comes from the most fundamental contour integral in the subject. For f(z) = 1/(z − z₀), integrate around a small circle centered at z₀: parametrize as z = z₀ + re^{iθ}, so dz = ire^{iθ} dθ, and the integral becomes ∫₀^{2π} ire^{iθ}/(re^{iθ}) dθ = ∫₀^{2π} i dθ = 2πi. For any holomorphic function h(z), the integral of h(z)/(z − z₀) around z₀ yields 2πi · h(z₀) by Cauchy's integral formula — and that value h(z₀) is exactly the residue Res(h/(z − z₀), z₀). Higher-order poles contribute through higher Laurent coefficients, but the factor 2πi appears universally.

To apply the theorem, work through the steps on a concrete example. Let f(z) = e^z/z and integrate around |z| = 2. The only singularity inside is a simple pole at z = 0. To find Res(f, 0), write the Laurent expansion: since e^z = 1 + z + z²/2! + ···, we get e^z/z = 1/z + 1 + z/2! + ···, so the coefficient of 1/z is 1. The theorem gives ∮_{|z|=2} e^z/z dz = 2πi · 1 = 2πi. For a function with multiple poles — say f(z) = 1/((z − 1)(z + 2)) integrated around |z| = 3 — both poles lie inside the contour; compute each residue separately and sum before multiplying by 2πi.

The theorem's greatest power is in evaluating real integrals that resist elementary methods. To compute ∫_{−∞}^{∞} dx/(1 + x²), extend to a contour in the complex plane: integrate along the real axis from −R to R, then close with a large semicircle in the upper half-plane. As R → ∞, the semicircle's contribution vanishes (by the ML inequality). The enclosed singularity is the pole of 1/(1 + z²) = 1/((z − i)(z + i)) at z = i, with residue lim_{z→i} (z − i)/(z² + 1) = 1/(2i). The theorem gives total contour integral = 2πi · (1/(2i)) = π. So ∫_{−∞}^{∞} dx/(1 + x²) = π — a result verifiable by arctangent, but the method extends to integrals no elementary technique can handle, making the Residue Theorem one of the most applied results in all of analysis.
