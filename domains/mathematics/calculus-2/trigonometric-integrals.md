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

## Questions

```yaml
- question: "You need to evaluate ∫ sin²(x) cos³(x) dx. Which strategy is correct?"
  type: multiple-choice
  options:
    - "Apply power-reduction to both factors since sin has an even exponent"
    - "Save cos(x) as the du factor, convert cos²(x) = 1 − sin²(x), then let u = sin(x)"
    - "Integrate by parts with u = sin²(x) and dv = cos³(x) dx"
    - "Apply the double-angle identity sin(2x) = 2 sin(x) cos(x) to the entire product"
  answer: 1
  explanation: "The exponent of cos is 3 (odd), so the odd-power strategy applies regardless of the sin exponent. Save one cos(x) for du, rewrite cos²(x) = 1 − sin²(x), and substitute u = sin(x). Option A is the classic misconception — students fixate on sin being even, but it is cos's odd exponent that determines the strategy. Power-reduction is only needed when both exponents are even."

- question: "You encounter ∫ sin⁴(x) cos²(x) dx. Both exponents are even. The correct approach is:"
  type: multiple-choice
  options:
    - "Let u = cos(x) and save sin(x) for du — the odd-exponent trick works on either factor"
    - "Apply power-reduction: sin²(x) = (1 − cos 2x)/2 and cos²(x) = (1 + cos 2x)/2, then expand"
    - "Use integration by parts repeatedly, since no substitution applies when both exponents are even"
    - "The integral cannot be evaluated in closed form"
  answer: 1
  explanation: "When both exponents are even, no single factor can be 'saved' for a substitution du because saving one would still leave an odd power of the other. Power-reduction (half-angle) identities are the correct tool: they lower the powers while introducing double-angle terms that are eventually integrable. Integration by parts (option C) is a last resort here and far less efficient."

- question: "In ∫ sinᵐ(x) cosⁿ(x) dx with m odd, the correct procedure saves one sin(x) factor as du and uses sin²(x) = 1 − cos²(x) to convert the remaining sin factors, then substitutes u = cos(x)."
  type: true-false
  answer: true
  explanation: "Exactly right. With m odd, write sinᵐ(x) = sinᵐ⁻¹(x) · sin(x). The sinᵐ⁻¹(x) piece has even exponent m−1, so it can be converted to a polynomial in cos²(x) using sin²(x) = 1 − cos²(x). The leftover sin(x) pairs with dx to form du = −sin(x) dx (with u = cos(x)), turning the integral into a polynomial in u — straightforward to integrate."

- question: "If both exponents in ∫ sinᵐ(x) cosⁿ(x) dx are even, u-substitution with u = cos(x) can still reduce the integral to a manageable form."
  type: true-false
  answer: false
  explanation: "U-substitution with u = cos(x) requires a sin(x) factor for du. With both exponents even, saving one sin(x) leaves sinᵐ⁻¹(x) — an odd power — which cannot be converted to a polynomial in cos²(x) using sin²(x) = 1 − cos²(x) without leaving a remaining sin(x). The correct tool for the both-even case is the power-reduction (half-angle) identities, which lower the powers algebraically without needing a du factor."

- question: "Why does the odd-exponent strategy work for ∫ sinᵐ(x) cosⁿ(x) dx when one exponent is odd, but not when both are even?"
  type: short-answer
  answer: "When one exponent is odd, you can split off one factor (e.g., sin(x)) to serve as du in a substitution. The remaining even-power factor converts cleanly to a polynomial in the other function via the Pythagorean identity. When both exponents are even, any attempt to save a factor leaves an odd power that can't be converted without creating another leftover factor — the substitution chain never terminates. Power-reduction identities bypass this by algebraically lowering powers without needing a du factor."
  explanation: "The substitution strategy works precisely because an odd exponent provides the 'extra' factor needed for du. Even exponents don't provide this, so the algebraic approach (power-reduction) becomes necessary. Recognizing which case applies — and why — is the central skill of trigonometric integration."
```

## Explainer

Trigonometric integrals aren't a new class of techniques — they're a coordinated application of tools you already have: **u-substitution**, **Pythagorean identities**, and **power-reduction (half-angle) identities**. The challenge is recognizing which combination applies. The strategy is determined almost entirely by whether the exponents are odd or even.

For integrals of the form ∫ sinᵐ(x) cosⁿ(x) dx, the decision tree is: **If either m or n is odd**, save one factor of that function to form du, and convert the remaining even power using the Pythagorean identity sin²(x) + cos²(x) = 1. For example, ∫ sin³(x) cos²(x) dx: m = 3 is odd, so write sin³(x) = sin²(x) · sin(x) = (1 − cos²(x)) · sin(x). Now let u = cos(x), du = −sin(x) dx. The integral becomes −∫ (1 − u²) u² du = −∫ (u² − u⁴) du, which is a polynomial in u — easy to integrate. The odd exponent provides the "extra" factor for du and makes the whole thing algebraic.

**If both m and n are even**, the odd-exponent trick doesn't work — you can't save a factor for du. Instead, use the **power-reduction identities**: sin²(x) = (1 − cos(2x))/2 and cos²(x) = (1 + cos(2x))/2. These halve the power while introducing a double-angle. For ∫ sin²(x) cos²(x) dx: write it as ∫ [(1 − cos(2x))/2][(1 + cos(2x))/2] dx = (1/4) ∫ (1 − cos²(2x)) dx, then apply power-reduction again to cos²(2x). The process telescopes down to integrable terms, though it takes more steps.

The **tangent-secant family** ∫ tanᵐ(x) secⁿ(x) dx follows analogous logic, anchored by the identity tan²(x) = sec²(x) − 1. If n (the secant exponent) is even, save sec²(x) as the du factor (since d/dx[tan x] = sec²x) and convert remaining secants. If m (the tangent exponent) is odd, save sec(x)tan(x) as the du factor (since d/dx[sec x] = sec x tan x) and convert remaining tangents using tan²(x) = sec²(x) − 1. Cases where m is even and n is odd are harder and may require reduction formulas or integration by parts.

The meta-skill here is **case recognition before computation**. Identify the family (sin-cos vs. tan-sec), check parity of exponents, select the strategy, and execute. Errors almost always come from picking the wrong case or making a sign error in the identity substitution. Keeping a reference card of the four main cases — (odd m), (odd n), (both even) for sin-cos; and the tan-sec analogs — turns trigonometric integrals from a confusing zoo into a decision flowchart.
