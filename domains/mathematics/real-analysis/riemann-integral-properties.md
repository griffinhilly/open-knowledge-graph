---
id: riemann-integral-properties
title: Properties of the Riemann Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: riemann-integrability-criteria
  type: hard
builds-toward:
- fundamental-theorem-calculus-rigorous
- improper-integrals-rigorous
tags:
- integral-properties
- linearity
- monotonicity
stage: advanced
status: validated
---

# Properties of the Riemann Integral

## Core Idea
The Riemann integral satisfies linearity (∫(af + bg) = a∫f + b∫g), monotonicity (f ≤ g ⟹ ∫f ≤ ∫g), and additivity over intervals. These properties follow from the definition and form the computational toolkit of integration. They extend to the Lebesgue integral.

## Questions

```yaml
- question: "You need to show that |∫₀¹ sin(x²)/√(x+1) dx| ≤ 1 without computing the integral explicitly. Which property of the Riemann integral is most directly applicable?"
  type: multiple-choice
  options:
    - "Linearity — split the integrand into sin(x²) and 1/√(x+1) and integrate each separately"
    - "Monotonicity — because |sin(x²)/√(x+1)| ≤ 1 on [0,1], and ∫₀¹ 1 dx = 1"
    - "Additivity — split the interval at x = 0.5 and bound each half separately"
    - "None of these — the bound requires computing the integral explicitly"
  answer: 1
  explanation: "Monotonicity (with the triangle inequality |∫f| ≤ ∫|f|) is the right tool. On [0,1], |sin(x²)| ≤ 1 and √(x+1) ≥ 1, so |sin(x²)/√(x+1)| ≤ 1 everywhere. Monotonicity then gives |∫f| ≤ ∫|f| ≤ ∫₀¹ 1 dx = 1. No explicit computation needed. Linearity handles sums and scalar multiples of integrable functions, not bounding absolute values this way. Additivity helps decompose domains but doesn't directly yield this bound. Option D reflects the misconception that bounding an integral always requires evaluating it explicitly."

- question: "A function f equals 1 on [0, 0.5) and 3 on [0.5, 1]. Which property most directly enables computation of ∫₀¹ f dx?"
  type: multiple-choice
  options:
    - "Linearity — write f = 1 + 2·1_{[0.5,1]} and integrate each term"
    - "Additivity over intervals — ∫₀¹ f = ∫₀^{0.5} f + ∫_{0.5}¹ f, and each piece is constant on its subinterval"
    - "Monotonicity — since 1 ≤ f(x) ≤ 3, the integral lies between 1 and 3"
    - "The integral cannot be computed because f is discontinuous at x = 0.5"
  answer: 1
  explanation: "Additivity over intervals allows splitting the integration domain at x = 0.5 where f changes formula. On [0, 0.5], f = 1, giving integral 0.5; on [0.5, 1], f = 3, giving integral 1.5; total is 2. Linearity (option A) also works but requires rewriting f first, making additivity the more direct approach for piecewise functions. Option C gives only bounds, not the value. Option D is false — a single-point discontinuity does not prevent Riemann integrability; bounded functions with finitely many discontinuities are integrable."

- question: "If f(x) ≤ g(x) for all x in [a, b], then ∫ₐᵇ f < ∫ₐᵇ g (strict inequality)."
  type: true-false
  answer: false
  explanation: "Monotonicity guarantees only weak inequality: ∫f ≤ ∫g. Strict inequality requires f(x) < g(x) on a set of positive measure, not merely at isolated points. For example, if f and g agree everywhere except at finitely many points, then ∫f = ∫g even though f ≤ g pointwise. The Riemann integral is insensitive to the function's behavior on sets of measure zero — individual points or finite collections of points contribute nothing to the integral. This is one place where the Lebesgue theory makes the statement more precise."

- question: "Linearity of the Riemann integral — ∫(αf + βg) = α∫f + β∫g — allows any integrable function to be integrated by breaking it into simpler parts, provided each part is individually integrable on the same interval."
  type: true-false
  answer: true
  explanation: "This is the operational significance of linearity. Any integrable function that can be decomposed as a sum of simpler functions (polynomials, trigonometric terms, rational functions after partial fractions) can be integrated piece by piece. Every standard integration technique — partial fractions, breaking a sum into terms, scaling by constants — ultimately relies on linearity. The condition 'provided each part is integrable' is important: linearity requires both summands to be integrable; you cannot split into parts that are individually non-integrable and apply the rule."

- question: "Explain why the three core properties of the Riemann integral — linearity, monotonicity, and additivity — are described as a computational toolkit rather than just theoretical results."
  type: short-answer
  answer: "The Darboux construction answers 'does the integral exist?' — but it is unwieldy as a computational tool. The three properties answer 'how do we work with it?' Linearity allows decomposition: a complicated integrand is split into simpler parts, each integrated separately — this underlies partial fractions, integration by parts, and every technique that recombines simpler integrals. Additivity handles piecewise-defined functions and allows breaking the domain at problematic points. Monotonicity provides estimation: when exact computation is hard, bounding the integrand between simpler functions immediately bounds the integral. Together, they translate the abstract definition into actionable computation without returning to Darboux sums each time."
  explanation: "The distinction between existence and computation is central to real analysis. Darboux sums prove existence but are not what you use in practice. The properties are the bridge from the abstract construction to the computational techniques of calculus. Understanding why they hold — they are proved from the Darboux definition — gives you both confidence in their application and the ability to reason correctly about edge cases where familiar intuitions fail."
```

## Explainer

You built the Riemann integral from Darboux sums: the lower sum L(f, P) and upper sum U(f, P) sandwich the integral from below and above, and f is integrable when the infimum of upper sums equals the supremum of lower sums. That construction answers "does the integral exist?" — but it is not something you want to use directly for every computation. The properties of the Riemann integral are the tools that let you work efficiently without returning to Darboux sums from scratch each time.

**Linearity** is the most-used property: ∫ₐᵇ (αf + βg) = α ∫ₐᵇ f + β ∫ₐᵇ g. This holds whenever f and g are both integrable on [a, b]. The proof is not deep — Darboux sums are already linear in the function, so the inequality squeezeback argument transfers directly — but the payoff is enormous. It means integration distributes over sums and scales with constants, which underlies every technique for computing integrals of complicated expressions by breaking them into simpler parts. Without linearity, you could not use substitution and partial fractions to split a rational function and integrate each piece.

**Monotonicity** says that if f(x) ≤ g(x) for all x in [a, b], then ∫ₐᵇ f ≤ ∫ₐᵇ g. Geometrically this is obvious: if one function lies below another everywhere, it sweeps out less area. The proof uses the fact that lower and upper Darboux sums respect pointwise inequality of functions. Monotonicity is the gateway to estimation: if you can bound a complicated integrand between two simpler ones, you immediately bound the integral. A direct consequence is the **integral mean value inequality**: if m ≤ f(x) ≤ M on [a, b], then m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a). This is the weakest possible estimate (using only global bounds), but it suffices for convergence proofs and error estimates.

**Additivity over intervals** states that ∫ₐᶜ f = ∫ₐᵇ f + ∫ᵦᶜ f for any b between a and c (and by convention, extending to any b when ∫ₐᵇ f is defined with reversed orientation as −∫ᵦᵃ f). This allows you to handle functions defined piecewise, to break integrals at discontinuities or change-of-formula points, and to integrate over unions of intervals. Together, linearity, monotonicity, and additivity form a package that extends cleanly to the Lebesgue integral — and the fact that these properties are shared explains why many analytic arguments work identically in both theories, with the Lebesgue theory adding the power to handle larger classes of functions.
