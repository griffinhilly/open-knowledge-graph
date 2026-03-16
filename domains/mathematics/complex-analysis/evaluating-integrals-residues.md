---
id: evaluating-integrals-residues
title: Evaluating Real Integrals Using Residues
domain: mathematics
course: complex-analysis
prerequisites:
- id: residue-theorem
  type: hard
tags:
- residue-method
- real-integrals
- applications
stage: advanced
status: draft
---

# Evaluating Real Integrals Using Residues

## Core Idea
Many difficult real integrals (improper integrals, trigonometric integrals) can be evaluated by closing the contour in the complex plane and using the residue theorem. For example, integrals of the form ∫_{-∞}^{∞} dx/(polynomial) are computed by integrating along the real axis and closing via a semicircle in the upper half-plane, picking up residues at poles with positive imaginary part.

## Explainer

The core strategy is an inspired trick: replace a hard real integral with a contour integral in the complex plane that (a) includes the real integral as part of the contour, (b) can be evaluated exactly using the residue theorem, and (c) has other parts of the contour contributing zero. When all three conditions hold, the residue theorem hands you the answer to the original real integral for free.

The **standard semicircular contour** handles improper integrals of the form ∫_{-∞}^{∞} f(x) dx where f(x) = p(x)/q(x) is a rational function with deg(q) ≥ deg(p) + 2 and no real poles. You close the contour by appending a large semicircle C_R of radius R in the upper half-plane. The residue theorem gives ∮ f(z) dz = 2πi · Σ Res(f, zₖ) where the sum is over poles with Im(zₖ) > 0. By the **ML estimate** (or Jordan's lemma for oscillatory integrands), the integral over C_R → 0 as R → ∞. So the original real integral equals 2πi times the sum of residues in the upper half-plane. To compute a residue at a simple pole z₀, use Res(f, z₀) = lim_{z→z₀} (z − z₀)f(z); at a pole of order m, use the derivative formula (1/(m−1)!) · d^{m−1}/dz^{m−1} [(z−z₀)^m f(z)] evaluated at z₀.

For **trigonometric integrals** of the form ∫₀^{2π} R(cos θ, sin θ) dθ, a different substitution works: set z = e^{iθ}, so cos θ = (z + z⁻¹)/2, sin θ = (z − z⁻¹)/(2i), and dθ = dz/(iz). The integral over [0, 2π] becomes a contour integral around the unit circle |z| = 1, and you pick up residues at poles strictly inside the unit disk. The key skill in both cases is identifying which poles fall inside the chosen contour — upper half-plane for the real line, unit disk for trigonometric integrals.

The method has a profound conceptual meaning beyond the calculation: the residue theorem connects the value of a function at isolated singularities to the behavior of its integral around closed paths. It says that the "global" integral around a closed contour depends only on the "local" behavior at poles inside — the rest of the function's structure contributes nothing. This is the machinery that lets complex analysis solve problems that real analysis cannot. As you apply this to increasingly varied integrands, the challenge shifts from knowing the technique to recognizing which contour and which closing argument (ML estimate, Jordan's lemma, indented contours for poles on the real axis) applies to each case.
