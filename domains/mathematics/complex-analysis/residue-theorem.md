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
status: draft
---

# The Residue Theorem

## Core Idea
If f is holomorphic inside and on a closed contour γ except for finitely many isolated singularities z₁, ..., zₙ inside γ, then ∮_γ f(z) dz = 2πi Σ Res(f, zₖ). This theorem reduces a contour integral to a sum of residues, making it a powerful tool for evaluating real integrals and summing series.

## How It's Best Learned
Apply this to compute ∮_γ dz/(z²+1) around a circle of radius 2. Identify the poles, compute their residues, and verify the result matches a direct contour integral.

## Common Misconceptions
Forgetting the factor 2πi; it comes from the integral formula for a simple pole. Assuming the theorem works for multiply-connected domains without accounting for all enclosed singularities.

## Explainer

You know from contour integration that for a holomorphic function on a simply connected domain, every closed contour integral is zero — that is Cauchy's theorem. Isolated singularities break this: they are the sole sources of nonzero contour integrals. The **Residue Theorem** makes this precise: ∮_γ f(z) dz = 2πi Σ Res(f, zₖ), where the sum runs over all isolated singularities zₖ enclosed by γ. The theorem reduces a potentially difficult integral to the algebraic task of computing residues.

The factor 2πi comes from the most fundamental contour integral in the subject. For f(z) = 1/(z − z₀), integrate around a small circle centered at z₀: parametrize as z = z₀ + re^{iθ}, so dz = ire^{iθ} dθ, and the integral becomes ∫₀^{2π} ire^{iθ}/(re^{iθ}) dθ = ∫₀^{2π} i dθ = 2πi. For any holomorphic function h(z), the integral of h(z)/(z − z₀) around z₀ yields 2πi · h(z₀) by Cauchy's integral formula — and that value h(z₀) is exactly the residue Res(h/(z − z₀), z₀). Higher-order poles contribute through higher Laurent coefficients, but the factor 2πi appears universally.

To apply the theorem, work through the steps on a concrete example. Let f(z) = e^z/z and integrate around |z| = 2. The only singularity inside is a simple pole at z = 0. To find Res(f, 0), write the Laurent expansion: since e^z = 1 + z + z²/2! + ···, we get e^z/z = 1/z + 1 + z/2! + ···, so the coefficient of 1/z is 1. The theorem gives ∮_{|z|=2} e^z/z dz = 2πi · 1 = 2πi. For a function with multiple poles — say f(z) = 1/((z − 1)(z + 2)) integrated around |z| = 3 — both poles lie inside the contour; compute each residue separately and sum before multiplying by 2πi.

The theorem's greatest power is in evaluating real integrals that resist elementary methods. To compute ∫_{−∞}^{∞} dx/(1 + x²), extend to a contour in the complex plane: integrate along the real axis from −R to R, then close with a large semicircle in the upper half-plane. As R → ∞, the semicircle's contribution vanishes (by the ML inequality). The enclosed singularity is the pole of 1/(1 + z²) = 1/((z − i)(z + i)) at z = i, with residue lim_{z→i} (z − i)/(z² + 1) = 1/(2i). The theorem gives total contour integral = 2πi · (1/(2i)) = π. So ∫_{−∞}^{∞} dx/(1 + x²) = π — a result verifiable by arctangent, but the method extends to integrals no elementary technique can handle, making the Residue Theorem one of the most applied results in all of analysis.
