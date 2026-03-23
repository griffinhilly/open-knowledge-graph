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
stage: expert
status: validated
---

# Routh-Hurwitz Stability Test: Algorithm and Application

## Core Idea
Routh-Hurwitz test determines stability without computing poles: arrange characteristic polynomial coefficients in a tableau, compute rows using specific rules. Number of sign changes in the first column equals number of poles in right half-plane. Test fails if any element is zero (repeated root on jω-axis); special cases require auxiliary polynomials.

## Questions

```yaml
- question: "After constructing the Routh tableau for a 5th-order system, the first column reads: 2, 3, −1, 4, 1. How many poles does the system have in the right half-plane?"
  type: multiple-choice
  options:
    - "Zero — the first column contains no zeros"
    - "One — there is one negative entry in the first column"
    - "Two — there are two sign changes in the first column (2→3→−1 and −1→4)"
    - "Three — there are three positive entries and two sign-change boundaries"
  answer: 2
  explanation: "The Routh-Hurwitz rule counts sign changes in the first column, not negative entries. The sequence 2, 3, −1, 4, 1 has two sign changes: 3→−1 (positive to negative) and −1→4 (negative to positive). Each sign change corresponds to exactly one root in the right half-plane. So the system has two RHP poles and is unstable. A common mistake is counting the single negative entry (option B) — but the theorem is about transitions, not counts of negative values."

- question: "While constructing the Routh tableau for a closed-loop system with variable gain K, you find that an entire row becomes identically zero for K = 5. What does this indicate, and how do you proceed?"
  type: multiple-choice
  options:
    - "The system is stable at K = 5; an all-zero row means no remaining poles need to be checked"
    - "The characteristic polynomial has roots on the imaginary axis at K = 5 — marginal stability; form the auxiliary polynomial from the row above, differentiate it, substitute its coefficients for the zero row, and continue"
    - "The tableau calculation is incorrect; no valid characteristic polynomial produces an all-zero row"
    - "The gain K = 5 stabilizes the system completely and the all-zero row confirms all remaining poles are in the left half-plane"
  answer: 1
  explanation: "An all-zero row means the characteristic polynomial has a symmetric factor — poles that come in pairs symmetric about the origin, such as ±jω pairs on the imaginary axis. This is marginal stability (poles on the stability boundary), not stability. The procedure is to form the auxiliary polynomial from the row just above the all-zero row, differentiate it with respect to s, use the derivative's coefficients to replace the zero row, and complete the tableau. The marginal gain K = 5 is exactly the answer to 'at what gain does the system first become marginally stable?' — a standard root-locus design question."

- question: "A system is stable if and only if all entries in the first column of its Routh tableau are positive."
  type: true-false
  answer: true
  explanation: "This is a restatement of the Routh-Hurwitz stability criterion for real-coefficient polynomials. Zero sign changes in the first column means all poles are in the left half-plane, which is exactly the stability condition for a continuous-time system. The test is both necessary and sufficient (absent the special zero-row cases, which indicate marginal stability rather than strict stability). All positive first-column entries implies no RHP poles."

- question: "The Routh-Hurwitz test determines stability by finding the roots of the characteristic polynomial and checking whether they lie in the left half-plane."
  type: true-false
  answer: false
  explanation: "This is precisely what the Routh-Hurwitz test avoids. Its main practical value is that it determines stability — specifically, the number of right-half-plane poles — using only arithmetic operations on the polynomial coefficients, without computing any roots at all. Finding roots of high-degree polynomials by hand is tedious and error-prone; the Routh tableau reduces the problem to a structured table calculation. The number of sign changes in the first column gives the number of RHP roots directly. Root-finding and Routh analysis answer the same question by completely different means."

- question: "What does a sign change in the first column of the Routh tableau represent, and why does counting sign changes give the exact number of right-half-plane poles?"
  type: short-answer
  answer: "Each sign change in the first column corresponds to exactly one root crossing from the left half-plane to the right half-plane in the complex s-plane. The Routh-Hurwitz criterion is derived from Cauchy's argument principle and Sturm sequences: the number of times the first column changes sign equals the number of roots of the characteristic polynomial with positive real part. This is a theorem, not a heuristic — the test is both necessary and sufficient, so zero sign changes guarantees all poles are in the LHP (stable) and n sign changes means exactly n unstable poles."
  explanation: "The deep reason is algebraic: the Routh algorithm constructs a Sturm sequence for the characteristic polynomial, and the sign changes in the leading coefficients of a Sturm sequence count real roots in an interval — here adapted to count complex roots with positive real part. The engineering payoff is enormous: stability analysis of an arbitrary-order system reduces to filling in a table by hand. No eigenvalue solver, no factoring, no numerical root-finding — just arithmetic and sign inspection."
```

## Explainer

From your transfer function work, you know a system is stable if and only if every pole of its closed-loop transfer function lies in the left half-plane (LHP) of the complex s-plane. The denominator polynomial — the **characteristic equation** — encodes these pole locations. For a first- or second-order system, you can factor it and inspect the roots directly. For higher-order systems, factoring becomes tedious or impossible by hand. The **Routh-Hurwitz test** answers the stability question using only arithmetic on the polynomial coefficients, with no factoring required.

The algorithm builds a **Routh tableau** row by row. Write the characteristic polynomial as aₙsⁿ + aₙ₋₁sⁿ⁻¹ + ⋯ + a₁s + a₀. Place the even-indexed coefficients in row 1 and the odd-indexed coefficients in row 2. Each subsequent row is computed from the two rows above using a determinant formula: each entry is (previous-row-left × two-rows-up-right − previous-row-right × two-rows-up-left) divided by previous-row-left. The tableau narrows by one column per row until you have n+1 rows total, where n is the polynomial degree. The critical information is entirely in the **first column**: count the sign changes among its entries. That count equals exactly the number of RHP poles. Zero sign changes means all poles are in the LHP — the system is stable.

A concrete example grounds the algorithm. For the polynomial s³ + 6s² + 11s + 6 (roots at −1, −2, −3), the tableau's first column contains all positive entries — no sign changes, confirming stability. Perturbing the last coefficient to −6 introduces one RHP root; one sign change appears in the first column. The test is both necessary and sufficient: it cannot give false positives or negatives (in the absence of special cases).

The **special cases** arise regularly in control design and cannot be ignored. If a first-column entry is zero but the row is not entirely zero, a pole lies on the imaginary axis — marginal stability, not Hurwitz stable. The standard workaround replaces the zero with a small positive ε, completes the tableau symbolically, and examines the sign changes as ε → 0⁺. If an **entire row is zero**, the characteristic polynomial has a factor that is itself a polynomial in s² — meaning poles come in symmetric pairs (e.g., ±jω pairs or ±σ pairs symmetric about the origin). In this case, form the **auxiliary polynomial** from the row just above the zero row, differentiate it with respect to s, use the derivative's coefficients to replace the zero row, and continue. The auxiliary polynomial's roots are the marginal poles whose location you need. This all-zero-row case appears naturally when asking "at what gain K does the closed-loop system become marginally stable?" — a standard root locus question that the Routh criterion answers algebraically without plotting.
