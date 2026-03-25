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
- id: routh-stability-algorithm
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
stage: expert
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

## Questions

```yaml
- question: "A control system has the characteristic polynomial s³ + 6s² + 11s + 6. All coefficients are positive. A student concludes the system must be stable. Is the student correct, and why or why not?"
  type: multiple-choice
  options:
    - "Yes — positive coefficients guarantee all roots are in the left half-plane for any degree polynomial"
    - "No — positive coefficients are necessary but not sufficient for degree ≥ 3; the Routh array must be constructed to confirm stability"
    - "No — a third-order system with all positive coefficients always has at least one right-half-plane root"
    - "Yes for this specific polynomial, but not in general — degree-3 systems are a special exception where positive coefficients are sufficient"
  answer: 1
  explanation: "All positive coefficients is a necessary condition for stability (any negative or zero coefficient immediately implies an unstable root), but it is not sufficient for polynomials of degree 3 or higher. A degree-4 polynomial like s⁴ + s³ + 2s² + s + 1 has all positive coefficients yet is unstable. The Routh array must be completed and the first column checked for sign changes. For this specific polynomial (s³ + 6s² + 11s + 6 = (s+1)(s+2)(s+3)), it happens to be stable, but the student cannot know that from coefficients alone without building the array."

- question: "While constructing a Routh array, you find that the first-column entry in row 3 is zero, but the row contains other nonzero entries. What is the correct next step?"
  type: multiple-choice
  options:
    - "Declare the system unstable immediately — any zero in the first column means there is a right-half-plane pole"
    - "Substitute a small positive number ε for the zero, complete the array symbolically, and count sign changes as ε → 0⁺"
    - "Replace the zero row with the derivative of the auxiliary polynomial formed from the row above"
    - "Declare the system marginally stable — a zero in the first column (with remaining nonzero entries) always corresponds to a purely imaginary root"
  answer: 1
  explanation: "A zero in the first column (with other nonzero entries in the same row) requires the ε substitution. You cannot directly divide by zero in the next row calculation, so replace the first-column zero with ε > 0, complete the array, then examine the sign of the resulting expressions as ε → 0⁺. If sign changes occur in the limit, there are right-half-plane roots. The auxiliary polynomial method (option C) is used when an ENTIRE row is zero, which indicates a different special case — symmetric root distribution. Options A and D are wrong: a first-column zero is ambiguous without completing the array."

- question: "A polynomial with all positive coefficients is guaranteed to be a stable characteristic polynomial — meaning all its roots have negative real parts."
  type: true-false
  answer: false
  explanation: "This is the most common misconception when first learning Routh-Hurwitz. Positive coefficients are necessary for stability (a negative or missing coefficient immediately implies instability) but are not sufficient for degree 3 or higher. The classic counterexample is s⁴ + s³ + 2s² + s + 1, which has all positive coefficients but contains right-half-plane roots (verifiable by the Routh array). The Routh-Hurwitz criterion exists precisely because the coefficient sign test is insufficient — you need the full array to determine whether the more subtle stability conditions are satisfied."

- question: "An all-zero row appearing in the Routh array during a gain-sweep problem typically means the system has become marginally stable at that gain value — meaning the closed-loop poles are on the imaginary axis."
  type: true-false
  answer: true
  explanation: "An all-zero row means the characteristic polynomial has a symmetric factor — roots that are symmetric about the origin. During a gain sweep, this most commonly means the roots that started in the left half-plane have migrated to the imaginary axis at the critical gain value. The auxiliary polynomial (formed from the row above the zero row) can be solved to find the exact imaginary-axis root locations and the corresponding critical gain. This is, in fact, a useful feature: the all-zero row condition gives you the stability boundary directly, telling you the exact gain at which the system transitions from stable to unstable."

- question: "What is the Routh-Hurwitz criterion actually counting, and why is this especially useful when designing systems with a free gain parameter K?"
  type: short-answer
  answer: "The number of sign changes in the first column of the completed Routh array equals the number of closed-loop poles in the right half of the s-plane (unstable poles). For stability, you need zero sign changes — all first-column entries must share the same sign. When the characteristic polynomial contains a symbolic gain K, the first-column entries become algebraic expressions in K. Setting the condition 'all entries positive' yields a system of inequalities whose solution is the stability range for K — a closed-form answer. This avoids numerically solving for poles at every candidate K value."
  explanation: "This is the practical payoff that makes Routh-Hurwitz a design tool, not just an analysis tool. A designer asked 'for what values of K is this closed-loop system stable?' can write the characteristic polynomial with K symbolic, build the Routh array, express the first-column entries as functions of K, and solve the resulting inequalities. The answer is exact and algebraic. Root locus gives similar information graphically, but Routh-Hurwitz gives it analytically — particularly useful for verifying stability bounds when the polynomial degree is high or when exact pole locations are not needed."
```

## Explainer

You know from the characteristic equation that closed-loop stability requires all roots of the characteristic polynomial to lie in the left half of the s-plane. For a first-order polynomial s + a, stability just means a > 0. For a second-order polynomial s² + bs + c, it means b > 0 and c > 0. But for higher-order polynomials, "all coefficients positive" is necessary but not sufficient — a fifth-degree polynomial can have all positive coefficients and still have right-half-plane roots. The **Routh-Hurwitz criterion** provides a complete, systematic answer for any degree polynomial without factoring.

The algorithm starts from the characteristic polynomial a_n s^n + a_{n-1} s^{n-1} + ... + a_1 s + a_0. The **Routh array** is a triangular table built from these coefficients. The first two rows are filled directly from alternating coefficients: row 1 gets a_n, a_{n-2}, a_{n-4}, ...; row 2 gets a_{n-1}, a_{n-3}, a_{n-5}, .... Each subsequent row is computed from the two rows above it using a 2×2 determinant divided by the leading element of the previous row. Specifically, for rows with elements [p, q, r, ...] and [u, v, w, ...], the next row starts with (pu − qv_correction)... — the standard formula you compute mechanically. The table terminates after n+1 rows, each with one fewer nonzero element.

The stability verdict comes from counting **sign changes in the first column** of the completed array. The number of sign changes equals the number of roots with positive real part (right-half-plane roots). For stability, you need zero sign changes — every entry in the first column must be positive (or all negative, by convention). This is the payoff: you never compute a single root, yet you know exactly how many are unstable. For a design problem with a free gain parameter K, the characteristic polynomial has K as a symbol in some entries. Setting the conditions "all first-column entries > 0" gives you a system of inequalities that defines the stability range for K — a closed-form answer without numerical root-finding.

The two **special cases** arise frequently. If a zero appears in the first column (but the row is not all zeros), the standard fix is to substitute a small positive number ε, complete the array symbolically, and take the limit as ε → 0. If a complete row of zeros appears, it means the characteristic polynomial has a symmetric factor — roots that are symmetric about the origin (real roots of equal magnitude opposite sign, or complex conjugate pairs on the imaginary axis). You recover the missing row by differentiating the **auxiliary polynomial** formed from the row immediately above the zero row, then inserting that derivative's coefficients and continuing. The auxiliary polynomial's roots (which you can factor out and find exactly) reveal whether there are imaginary-axis roots (marginally stable) or canceling pairs of left/right half-plane roots. In practice, an all-zero row during a gain-sweep problem often means you've hit the exact gain value at which the closed-loop poles touch the imaginary axis — the **stability margin**.
