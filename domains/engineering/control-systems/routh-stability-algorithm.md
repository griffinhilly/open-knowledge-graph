---
id: routh-stability-algorithm
title: 'Routh-Hurwitz Stability Test: Algorithm and Application'
domain: engineering
course: control-systems
prerequisites:
- id: transfer-function-derivation-differential-equations
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- routh-hurwitz
- stability-test
- pole-locations
- characteristic-equation
stage: formal-systems
status: draft
---

# Routh-Hurwitz Stability Test: Algorithm and Application

## Core Idea
Routh-Hurwitz test determines stability without computing poles: arrange characteristic polynomial coefficients in a tableau, compute rows using specific rules. Number of sign changes in the first column equals number of poles in right half-plane. Test fails if any element is zero (repeated root on jω-axis); special cases require auxiliary polynomials.

## Explainer

From your transfer function work, you know a system is stable if and only if every pole of its closed-loop transfer function lies in the left half-plane (LHP) of the complex s-plane. The denominator polynomial — the **characteristic equation** — encodes these pole locations. For a first- or second-order system, you can factor it and inspect the roots directly. For higher-order systems, factoring becomes tedious or impossible by hand. The **Routh-Hurwitz test** answers the stability question using only arithmetic on the polynomial coefficients, with no factoring required.

The algorithm builds a **Routh tableau** row by row. Write the characteristic polynomial as aₙsⁿ + aₙ₋₁sⁿ⁻¹ + ⋯ + a₁s + a₀. Place the even-indexed coefficients in row 1 and the odd-indexed coefficients in row 2. Each subsequent row is computed from the two rows above using a determinant formula: each entry is (previous-row-left × two-rows-up-right − previous-row-right × two-rows-up-left) divided by previous-row-left. The tableau narrows by one column per row until you have n+1 rows total, where n is the polynomial degree. The critical information is entirely in the **first column**: count the sign changes among its entries. That count equals exactly the number of RHP poles. Zero sign changes means all poles are in the LHP — the system is stable.

A concrete example grounds the algorithm. For the polynomial s³ + 6s² + 11s + 6 (roots at −1, −2, −3), the tableau's first column contains all positive entries — no sign changes, confirming stability. Perturbing the last coefficient to −6 introduces one RHP root; one sign change appears in the first column. The test is both necessary and sufficient: it cannot give false positives or negatives (in the absence of special cases).

The **special cases** arise regularly in control design and cannot be ignored. If a first-column entry is zero but the row is not entirely zero, a pole lies on the imaginary axis — marginal stability, not Hurwitz stable. The standard workaround replaces the zero with a small positive ε, completes the tableau symbolically, and examines the sign changes as ε → 0⁺. If an **entire row is zero**, the characteristic polynomial has a factor that is itself a polynomial in s² — meaning poles come in symmetric pairs (e.g., ±jω pairs or ±σ pairs symmetric about the origin). In this case, form the **auxiliary polynomial** from the row just above the zero row, differentiate it with respect to s, use the derivative's coefficients to replace the zero row, and continue. The auxiliary polynomial's roots are the marginal poles whose location you need. This all-zero-row case appears naturally when asking "at what gain K does the closed-loop system become marginally stable?" — a standard root locus question that the Routh criterion answers algebraically without plotting.
