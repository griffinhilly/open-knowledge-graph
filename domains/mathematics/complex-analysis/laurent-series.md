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

## Explainer

You have worked with power series in the complex plane — series of the form Σ aₙ(z − z₀)^n with non-negative exponents, which converge on a disk centered at z₀. A **Laurent series** extends this idea by allowing negative exponents: Σ_{n=−∞}^{∞} aₙ(z − z₀)^n. This extension is not just notational generosity — it is forced on you by the existence of singularities. If f(z) has a singularity at z₀, it cannot have a Taylor series there, but it may still have a perfectly convergent Laurent expansion on the punctured neighborhood 0 < |z − z₀| < R. The negative-power terms encode exactly how badly f blows up as z → z₀.

The natural domain of a Laurent series is an **annulus** r < |z − z₀| < R, not a disk. The outer radius R is determined by the nearest singularity outside z₀, exactly as for a Taylor series. The inner radius r accounts for the singularity at z₀ itself — the series breaks down at z₀, so we exclude it. A Taylor series is the special case r = 0 and no negative-power terms, where the disk is non-punctured. A concrete example: f(z) = 1/(z(z−1)) around z₀ = 0 has a singularity at z = 0 and at z = 1. The annulus 0 < |z| < 1 avoids both. Expanding 1/(z−1) = −1/(1−z) = −Σz^n for |z| < 1 and dividing by z gives f(z) = −Σz^{n−1} = −z^{−1} − 1 − z − z² − ⋯. The negative-power term is −z^{−1}.

The Laurent series splits into two parts. The **regular part** Σ_{n=0}^{∞} aₙ(z − z₀)^n behaves like a Taylor series; it converges inside the outer circle. The **principal part** Σ_{n=−∞}^{−1} aₙ(z − z₀)^n consists of all the negative-power terms; it captures the singularity's character. The nature of the principal part classifies the singularity: if it has finitely many terms (stopping at (z−z₀)^{−m}), the singularity is a **pole of order m**. If it has infinitely many terms, the singularity is **essential**. If the principal part is empty entirely, there is no singularity — the Laurent series is just a Taylor series.

The coefficient **a₋₁** — the coefficient of (z − z₀)^{−1} — is called the **residue** and occupies a special role. By Cauchy's integral formula, integrating f(z) around a small loop encircling z₀ picks out exactly this coefficient: (1/2πi) ∮ f(z) dz = a₋₁. This is why the residue appears as the output of contour integrals. No other Laurent coefficient contributes to the integral — all the (z − z₀)^n terms with n ≠ −1 integrate to zero around a closed loop. The residue theorem, which you will study next, turns this observation into a powerful computational machine: to evaluate complicated real integrals, encode them as contour integrals in ℂ, locate the singularities inside the contour, read off the residues from the Laurent expansions, and sum them.
