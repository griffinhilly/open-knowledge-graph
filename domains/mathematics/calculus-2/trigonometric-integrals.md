---
id: trigonometric-integrals
title: Trigonometric Integrals
domain: mathematics
course: calculus-2
prerequisites:
- id: trigonometric-identities-pythagorean
  type: hard
- id: double-angle-identities
  type: hard
- id: u-substitution
  type: hard
- id: integration-by-parts
  type: soft
- id: amplitude-period-phase-shift
  type: soft
- id: half-angle-identities
  type: soft
builds-toward:
- trigonometric-substitution
tags:
- integration
- techniques
- trigonometric
stage: formal-systems
status: validated
---
# Trigonometric Integrals

## Core Idea
Trigonometric integrals involve products and powers of trig functions: sin^m(x) cos^n(x), tan^m(x) sec^n(x), etc. The strategy depends on the exponents: if one exponent is odd, save one factor for du and convert the rest using Pythagorean identities. If both are even, use half-angle (power-reduction) identities. For tangent-secant integrals, similar strategies apply with tan^2 = sec^2 - 1.

## How It's Best Learned
Organize by case: sin^m cos^n with one odd exponent, both even, and the analogous tan-sec cases. Master each case's strategy, then practice mixed problems where you identify the case first. Connect to the identities from precalculus.

## Common Misconceptions
- Applying the wrong strategy (e.g., using power-reduction when an odd exponent allows a simpler substitution).
- Making errors in the Pythagorean identity substitution (sin^2 = 1 - cos^2 vs. cos^2 = 1 - sin^2).
- Forgetting the reduction formulas for higher powers of secant.

## Explainer

Trigonometric integrals aren't a new class of techniques — they're a coordinated application of tools you already have: **u-substitution**, **Pythagorean identities**, and **power-reduction (half-angle) identities**. The challenge is recognizing which combination applies. The strategy is determined almost entirely by whether the exponents are odd or even.

For integrals of the form ∫ sinᵐ(x) cosⁿ(x) dx, the decision tree is: **If either m or n is odd**, save one factor of that function to form du, and convert the remaining even power using the Pythagorean identity sin²(x) + cos²(x) = 1. For example, ∫ sin³(x) cos²(x) dx: m = 3 is odd, so write sin³(x) = sin²(x) · sin(x) = (1 − cos²(x)) · sin(x). Now let u = cos(x), du = −sin(x) dx. The integral becomes −∫ (1 − u²) u² du = −∫ (u² − u⁴) du, which is a polynomial in u — easy to integrate. The odd exponent provides the "extra" factor for du and makes the whole thing algebraic.

**If both m and n are even**, the odd-exponent trick doesn't work — you can't save a factor for du. Instead, use the **power-reduction identities**: sin²(x) = (1 − cos(2x))/2 and cos²(x) = (1 + cos(2x))/2. These halve the power while introducing a double-angle. For ∫ sin²(x) cos²(x) dx: write it as ∫ [(1 − cos(2x))/2][(1 + cos(2x))/2] dx = (1/4) ∫ (1 − cos²(2x)) dx, then apply power-reduction again to cos²(2x). The process telescopes down to integrable terms, though it takes more steps.

The **tangent-secant family** ∫ tanᵐ(x) secⁿ(x) dx follows analogous logic, anchored by the identity tan²(x) = sec²(x) − 1. If n (the secant exponent) is even, save sec²(x) as the du factor (since d/dx[tan x] = sec²x) and convert remaining secants. If m (the tangent exponent) is odd, save sec(x)tan(x) as the du factor (since d/dx[sec x] = sec x tan x) and convert remaining tangents using tan²(x) = sec²(x) − 1. Cases where m is even and n is odd are harder and may require reduction formulas or integration by parts.

The meta-skill here is **case recognition before computation**. Identify the family (sin-cos vs. tan-sec), check parity of exponents, select the strategy, and execute. Errors almost always come from picking the wrong case or making a sign error in the identity substitution. Keeping a reference card of the four main cases — (odd m), (odd n), (both even) for sin-cos; and the tan-sec analogs — turns trigonometric integrals from a confusing zoo into a decision flowchart.
