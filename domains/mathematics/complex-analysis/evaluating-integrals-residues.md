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

## Questions

```yaml
- question: "To evaluate ∫_{-∞}^{∞} dx/(x²+4) using a semicircular contour in the upper half-plane, the integrand f(z) = 1/(z²+4) has poles at z = 2i and z = −2i. Which poles do you include when applying the residue theorem?"
  type: multiple-choice
  options:
    - "Both z = 2i and z = −2i, since both are poles of f(z)"
    - "Only the residue at z = 2i, since it is the only pole with positive imaginary part lying inside the upper half-plane contour"
    - "Only the residue at z = −2i, since it lies on the 'correct' side for the closing semicircle"
    - "Neither pole — the degree condition deg(q) ≥ deg(p) + 2 is not satisfied, so the method fails"
  answer: 1
  explanation: "The residue theorem sums only the residues at poles *inside* the closed contour. The semicircular contour encloses the upper half-plane (Im(z) > 0), so only z = 2i qualifies. The pole at z = −2i is in the lower half-plane, outside the contour, and contributes nothing. Including both residues is the most common error — it produces a wrong answer because the residue theorem specifically counts poles inside the contour, not all poles of the function. Note also that deg(q) = 2 ≥ deg(p) + 2 = 0 + 2 = 2, so the degree condition is satisfied and the method works."

- question: "When closing the contour with a large semicircular arc C_R of radius R in the upper half-plane, why does the integral over C_R tend to zero as R → ∞ for a rational integrand f(z) = p(z)/q(z) with deg(q) ≥ deg(p) + 2?"
  type: multiple-choice
  options:
    - "The semicircle has zero length in the limit, so any bounded integrand contributes nothing"
    - "The residue theorem guarantees that curved contour segments always contribute zero to the integral"
    - "The ML estimate gives |f(z)| ≤ M/R² on C_R while the arc length is πR, bounding the arc integral by πM/R → 0 as R → ∞"
    - "The imaginary parts of the integrand cancel along the semicircle due to the contour's symmetry about the imaginary axis"
  answer: 2
  explanation: "The ML estimate (also called the estimation lemma) bounds a contour integral by the maximum of |f| on the contour times the contour's length: |∫_{C_R} f(z)dz| ≤ M_R · πR. For a rational function with deg(q) ≥ deg(p) + 2, we have |f(z)| = O(1/|z|²), so M_R ≤ K/R² for some constant K, giving the bound K·πR/R² = Kπ/R → 0. Option A is wrong — the arc length πR grows without bound, so zero length is not the reason. Option B is false — curved arcs do not automatically contribute zero. This vanishing is condition (c) that makes the entire method work."

- question: "When evaluating ∫_{-∞}^{∞} p(x)/q(x) dx using the upper half-plane semicircular contour, you should sum the residues at every pole of p(z)/q(z) in the entire complex plane."
  type: true-false
  answer: false
  explanation: "The residue theorem counts only the residues at poles *inside* the closed contour. For the upper half-plane semicircle, this means only poles with strictly positive imaginary part (Im(z) > 0). Poles in the lower half-plane are outside the contour and do not appear in the calculation. Poles on the real axis lie on the contour itself and require special treatment (an indented contour that bypasses them). Summing all poles in the plane is a common error that yields a wrong answer — typically twice the correct answer if the function has symmetric poles above and below the real axis."

- question: "For a trigonometric integral ∫₀^{2π} R(cosθ, sinθ) dθ evaluated via the substitution z = e^{iθ}, you sum the residues at all poles of the resulting function inside the unit circle |z| < 1."
  type: true-false
  answer: true
  explanation: "After substituting z = e^{iθ}, dθ = dz/(iz), cosθ = (z + z⁻¹)/2, sinθ = (z − z⁻¹)/(2i), the integral over [0, 2π] becomes a counterclockwise contour integral around the unit circle |z| = 1. The residue theorem then sums residues at poles strictly inside this contour — i.e., poles with |z| < 1. Poles outside the unit disk (|z| > 1) are outside the contour and don't contribute. This is the exact analogue of the upper half-plane condition: the choice of contour determines which poles count."

- question: "Describe the three conditions that must hold for the standard upper half-plane semicircular contour method to successfully evaluate ∫_{-∞}^{∞} f(x) dx, and explain what goes wrong if each condition fails."
  type: short-answer
  answer: "Condition 1: The contour must include the real integral as a segment. The contour runs along the real axis from −R to R, becoming the desired integral as R → ∞. Failure: if f has poles on the real axis, they lie on the contour itself — the residue theorem requires poles to be strictly inside. The fix is an indented contour that detours around real-axis poles via small semicircles, picking up half-residues.\n\nCondition 2: The closed contour must enclose identifiable poles with computable residues. The residue theorem applies only if f is meromorphic inside the contour with finitely many poles. Failure: infinitely many poles inside (e.g., f(z) = 1/sin(z)) makes the sum unmanageable and the method impractical.\n\nCondition 3: The integral over the large semicircular arc C_R must vanish as R → ∞. For rational f with deg(q) ≥ deg(p) + 2, the ML estimate guarantees this. Failure: if deg(q) = deg(p) + 1, the arc integral may not vanish. Jordan's lemma provides a workaround: for integrands of the form e^{iaz}·g(z) where g(z) → 0 uniformly as |z| → ∞ (a > 0), the arc integral still vanishes — enabling evaluation of Fourier-type integrals that the basic degree condition misses."
  explanation: "Understanding these three conditions is what separates mechanical pattern-matching from genuine command of the technique. When a new integral resists the standard approach, diagnosing which condition fails points directly to the appropriate fix: indented contour for real-axis poles, a different contour geometry for slow decay, or Jordan's lemma for oscillatory integrands."
```

## Explainer

The core strategy is an inspired trick: replace a hard real integral with a contour integral in the complex plane that (a) includes the real integral as part of the contour, (b) can be evaluated exactly using the residue theorem, and (c) has other parts of the contour contributing zero. When all three conditions hold, the residue theorem hands you the answer to the original real integral for free.

The **standard semicircular contour** handles improper integrals of the form ∫_{-∞}^{∞} f(x) dx where f(x) = p(x)/q(x) is a rational function with deg(q) ≥ deg(p) + 2 and no real poles. You close the contour by appending a large semicircle C_R of radius R in the upper half-plane. The residue theorem gives ∮ f(z) dz = 2πi · Σ Res(f, zₖ) where the sum is over poles with Im(zₖ) > 0. By the **ML estimate** (or Jordan's lemma for oscillatory integrands), the integral over C_R → 0 as R → ∞. So the original real integral equals 2πi times the sum of residues in the upper half-plane. To compute a residue at a simple pole z₀, use Res(f, z₀) = lim_{z→z₀} (z − z₀)f(z); at a pole of order m, use the derivative formula (1/(m−1)!) · d^{m−1}/dz^{m−1} [(z−z₀)^m f(z)] evaluated at z₀.

For **trigonometric integrals** of the form ∫₀^{2π} R(cos θ, sin θ) dθ, a different substitution works: set z = e^{iθ}, so cos θ = (z + z⁻¹)/2, sin θ = (z − z⁻¹)/(2i), and dθ = dz/(iz). The integral over [0, 2π] becomes a contour integral around the unit circle |z| = 1, and you pick up residues at poles strictly inside the unit disk. The key skill in both cases is identifying which poles fall inside the chosen contour — upper half-plane for the real line, unit disk for trigonometric integrals.

The method has a profound conceptual meaning beyond the calculation: the residue theorem connects the value of a function at isolated singularities to the behavior of its integral around closed paths. It says that the "global" integral around a closed contour depends only on the "local" behavior at poles inside — the rest of the function's structure contributes nothing. This is the machinery that lets complex analysis solve problems that real analysis cannot. As you apply this to increasingly varied integrands, the challenge shifts from knowing the technique to recognizing which contour and which closing argument (ML estimate, Jordan's lemma, indented contours for poles on the real axis) applies to each case.
