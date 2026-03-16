---
id: routh-hurwitz-criterion
title: Routh-Hurwitz Stability Criterion
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: characteristic-polynomial
  type: hard
- id: polynomial-functions-degree-and-leading-coefficient
  type: soft
- id: time-domain-response-second-order
  type: soft
builds-toward:
- root-locus-method
- gain-and-phase-margins
tags:
- stability
- routh-array
- characteristic-equation
- sign-changes
- hurwitz
stage: advanced
status: validated
---
# Routh-Hurwitz Stability Criterion

## Core Idea
The Routh-Hurwitz criterion determines whether all roots (poles) of a polynomial lie in the left half of the complex s-plane — a necessary and sufficient condition for stability — without explicitly computing the roots. The Routh array is constructed from the characteristic polynomial's coefficients, and the number of sign changes in the first column equals the number of right-half-plane poles. Special cases arise when a zero appears in the first column (use ε substitution) or an entire row is zero (use the auxiliary polynomial method). The criterion also determines the range of a gain parameter K that keeps a closed-loop system stable.

## How It's Best Learned
Build Routh arrays by hand for polynomials of degree 2 through 5, deliberately generating both special cases (zero in first column, zero row) to practice those procedures. Find stability gain ranges by treating K symbolically and applying sign-change conditions.

## Common Misconceptions
- All positive coefficients is necessary but not sufficient for stability in polynomials of degree 3 and higher — the Routh array must still be checked.
- A row of all zeros indicates roots on the imaginary axis (or origin), not necessarily instability — the auxiliary polynomial reveals the actual root locations.
- The criterion tests the characteristic polynomial of the closed-loop system, not the open-loop denominator alone.

## Explainer

You know from the characteristic equation that closed-loop stability requires all roots of the characteristic polynomial to lie in the left half of the s-plane. For a first-order polynomial s + a, stability just means a > 0. For a second-order polynomial s² + bs + c, it means b > 0 and c > 0. But for higher-order polynomials, "all coefficients positive" is necessary but not sufficient — a fifth-degree polynomial can have all positive coefficients and still have right-half-plane roots. The **Routh-Hurwitz criterion** provides a complete, systematic answer for any degree polynomial without factoring.

The algorithm starts from the characteristic polynomial a_n s^n + a_{n-1} s^{n-1} + ... + a_1 s + a_0. The **Routh array** is a triangular table built from these coefficients. The first two rows are filled directly from alternating coefficients: row 1 gets a_n, a_{n-2}, a_{n-4}, ...; row 2 gets a_{n-1}, a_{n-3}, a_{n-5}, .... Each subsequent row is computed from the two rows above it using a 2×2 determinant divided by the leading element of the previous row. Specifically, for rows with elements [p, q, r, ...] and [u, v, w, ...], the next row starts with (pu − qv_correction)... — the standard formula you compute mechanically. The table terminates after n+1 rows, each with one fewer nonzero element.

The stability verdict comes from counting **sign changes in the first column** of the completed array. The number of sign changes equals the number of roots with positive real part (right-half-plane roots). For stability, you need zero sign changes — every entry in the first column must be positive (or all negative, by convention). This is the payoff: you never compute a single root, yet you know exactly how many are unstable. For a design problem with a free gain parameter K, the characteristic polynomial has K as a symbol in some entries. Setting the conditions "all first-column entries > 0" gives you a system of inequalities that defines the stability range for K — a closed-form answer without numerical root-finding.

The two **special cases** arise frequently. If a zero appears in the first column (but the row is not all zeros), the standard fix is to substitute a small positive number ε, complete the array symbolically, and take the limit as ε → 0. If a complete row of zeros appears, it means the characteristic polynomial has a symmetric factor — roots that are symmetric about the origin (real roots of equal magnitude opposite sign, or complex conjugate pairs on the imaginary axis). You recover the missing row by differentiating the **auxiliary polynomial** formed from the row immediately above the zero row, then inserting that derivative's coefficients and continuing. The auxiliary polynomial's roots (which you can factor out and find exactly) reveal whether there are imaginary-axis roots (marginally stable) or canceling pairs of left/right half-plane roots. In practice, an all-zero row during a gain-sweep problem often means you've hit the exact gain value at which the closed-loop poles touch the imaginary axis — the **stability margin**.
