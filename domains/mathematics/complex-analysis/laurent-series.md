---
id: laurent-series
title: Laurent Series
domain: mathematics
course: complex-analysis
prerequisites:
- id: power-series-complex-plane
  type: hard
builds-toward:
- singularities-classification
- residues-definition-computation
tags:
- laurent-series
- principal-part
- singularities
stage: advanced
status: draft
---

# Laurent Series

## Core Idea
A Laurent series is Σ_(n=-∞)^∞ aₙ(z - z₀)^n. It converges on an annulus r < |z - z₀| < R. Any holomorphic function on an annulus has a unique Laurent expansion. The coefficient a₋₁ (the residue) plays a special role. The principal part Σ_(n=-∞)^(-1) aₙ(z - z₀)^n captures the behavior near the singularity at z₀.

## How It's Best Learned
Expand f(z) = 1/(z(z-1)) as a Laurent series around z = 0 in the annulus 0 < |z| < 1. Notice the negative powers appear and identify the residue (a₋₁).

## Common Misconceptions
Thinking Laurent series are like Taylor series but with negative powers; they describe behavior near singularities. Confusing the principal part with the regular part; they represent different aspects of the singularity.

## Questions

```yaml
- question: "A function has a Laurent expansion around z₀ where the principal part contains exactly three terms (down to (z − z₀)^{−3}). What type of singularity does z₀ represent?"
  type: multiple-choice
  options:
    - "An essential singularity, because negative powers are present"
    - "A removable singularity, because the series converges near z₀"
    - "A pole of order 3, because the principal part terminates at (z − z₀)^{−3}"
    - "A branch point, because the index goes negative"
  answer: 2
  explanation: "A singularity is a pole of order m when the principal part has finitely many terms, terminating at (z − z₀)^{−m}. Three terms ending at the −3 power means a pole of order 3. An essential singularity requires infinitely many terms in the principal part. Option A is the classic misconception — the mere presence of negative powers does not imply an essential singularity; it only does when those terms continue without end."

- question: "Why is the coefficient a₋₁ in a Laurent series singled out as 'the residue'?"
  type: multiple-choice
  options:
    - "It is always the largest coefficient and dominates near the singularity"
    - "It is the only Laurent coefficient that survives integration around a closed loop encircling z₀"
    - "It equals the limit of f(z) as z → z₀, giving the singularity's strength"
    - "It determines whether the singularity is removable or not"
  answer: 1
  explanation: "Integrating (z − z₀)^n around a small loop gives zero for every integer n except n = −1, where it gives 2πi. Therefore (1/2πi)∮f(z)dz = a₋₁ — only the (z − z₀)^{−1} term contributes. All other terms integrate to zero around a closed path. This is why the residue is the key number for computing contour integrals, not because it is necessarily the largest or limit-related coefficient."

- question: "The principal part of a Laurent series converges on the same disk-shaped region as the regular (non-negative power) part."
  type: true-false
  answer: false
  explanation: "The two parts converge on different regions. The regular part Σ_{n≥0} aₙ(z−z₀)^n converges inside a disk |z − z₀| < R. The principal part Σ_{n<0} aₙ(z−z₀)^n is a power series in 1/(z−z₀) that converges outside a circle |z − z₀| > r. The Laurent series as a whole converges on the annulus r < |z − z₀| < R where both parts converge simultaneously — not on a disk."

- question: "Every singularity of a complex function can be classified by examining how many terms appear in the principal part of its Laurent series."
  type: true-false
  answer: true
  explanation: "The classification is complete and based solely on the principal part: zero terms (principal part is empty) means a removable singularity; finitely many terms ending at (z−z₀)^{−m} means a pole of order m; infinitely many terms means an essential singularity. The regular part plays no role in the classification — only the negative-power terms matter."

- question: "Explain why a₋₁ — the residue — has special significance for contour integration, while no other Laurent coefficient does."
  type: short-answer
  answer: "When you integrate (z − z₀)^n around a closed loop encircling z₀, the result is 2πi if n = −1 and zero for all other integers n. So integrating term-by-term through the Laurent series, only the (z − z₀)^{−1} term survives. All other terms contribute nothing. The residue a₋₁ is therefore the sole Laurent coefficient that encodes what a contour integral 'sees' at a singularity, which is why residues are the central tool for evaluating complex integrals."
  explanation: "This is a consequence of the antiderivative: (z − z₀)^n for n ≠ −1 has an antiderivative (z − z₀)^{n+1}/(n+1) that returns to its starting value after a full loop, giving zero net integral. The n = −1 case is the exception because log(z − z₀) is multivalued — it does not return to its original value after encircling z₀, picking up the factor 2πi instead."
```

## Explainer

You have worked with power series in the complex plane — series of the form Σ aₙ(z − z₀)^n with non-negative exponents, which converge on a disk centered at z₀. A **Laurent series** extends this idea by allowing negative exponents: Σ_{n=−∞}^{∞} aₙ(z − z₀)^n. This extension is not just notational generosity — it is forced on you by the existence of singularities. If f(z) has a singularity at z₀, it cannot have a Taylor series there, but it may still have a perfectly convergent Laurent expansion on the punctured neighborhood 0 < |z − z₀| < R. The negative-power terms encode exactly how badly f blows up as z → z₀.

The natural domain of a Laurent series is an **annulus** r < |z − z₀| < R, not a disk. The outer radius R is determined by the nearest singularity outside z₀, exactly as for a Taylor series. The inner radius r accounts for the singularity at z₀ itself — the series breaks down at z₀, so we exclude it. A Taylor series is the special case r = 0 and no negative-power terms, where the disk is non-punctured. A concrete example: f(z) = 1/(z(z−1)) around z₀ = 0 has a singularity at z = 0 and at z = 1. The annulus 0 < |z| < 1 avoids both. Expanding 1/(z−1) = −1/(1−z) = −Σz^n for |z| < 1 and dividing by z gives f(z) = −Σz^{n−1} = −z^{−1} − 1 − z − z² − ⋯. The negative-power term is −z^{−1}.

The Laurent series splits into two parts. The **regular part** Σ_{n=0}^{∞} aₙ(z − z₀)^n behaves like a Taylor series; it converges inside the outer circle. The **principal part** Σ_{n=−∞}^{−1} aₙ(z − z₀)^n consists of all the negative-power terms; it captures the singularity's character. The nature of the principal part classifies the singularity: if it has finitely many terms (stopping at (z−z₀)^{−m}), the singularity is a **pole of order m**. If it has infinitely many terms, the singularity is **essential**. If the principal part is empty entirely, there is no singularity — the Laurent series is just a Taylor series.

The coefficient **a₋₁** — the coefficient of (z − z₀)^{−1} — is called the **residue** and occupies a special role. By Cauchy's integral formula, integrating f(z) around a small loop encircling z₀ picks out exactly this coefficient: (1/2πi) ∮ f(z) dz = a₋₁. This is why the residue appears as the output of contour integrals. No other Laurent coefficient contributes to the integral — all the (z − z₀)^n terms with n ≠ −1 integrate to zero around a closed loop. The residue theorem, which you will study next, turns this observation into a powerful computational machine: to evaluate complicated real integrals, encode them as contour integrals in ℂ, locate the singularities inside the contour, read off the residues from the Laurent expansions, and sum them.
