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
status: draft
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
