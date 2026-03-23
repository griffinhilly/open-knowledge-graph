---
id: undetermined-coefficients
title: Method of Undetermined Coefficients
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: characteristic-equation-method
  type: hard
builds-toward:
- higher-order-linear-odes
tags:
- particular-solution
- undetermined-coefficients
- non-homogeneous
stage: formal-systems
status: validated
---

# Method of Undetermined Coefficients

## Core Idea
To solve y'' + py' + qy = f(x), find the homogeneous solution y_h, then guess the form of a particular solution y_p based on f(x). For f polynomial, exponential, sine, or cosine, use corresponding y_p forms with unknown coefficients. Substitute into the equation and solve for these coefficients. The general solution is y = y_h + y_p. This method is efficient when applicable.

## Questions

```yaml
- question: "Consider y'' - 4y = e^{2x}. The homogeneous solution is y_h = C₁e^{2x} + C₂e^{-2x}. A student guesses y_p = Ae^{2x} and substitutes into the equation. What will happen?"
  type: multiple-choice
  options:
    - "The substitution will work and give A = 1/4"
    - "The left side will reduce to 0, making it impossible to solve for A"
    - "The substitution gives A = -1/4, which is the correct particular solution"
    - "The method fails entirely because the right side is exponential"
  answer: 1
  explanation: "Since e^{2x} is already a term in y_h (the solution to the homogeneous equation), substituting Ae^{2x} into y'' - 4y gives A(4e^{2x}) - 4(Ae^{2x}) = 0 — the guess annihilates itself and can never equal e^{2x}. This is the resonance case: the standard guess is a solution to the homogeneous equation and always produces zero on the left side. The fix is the modification rule: use y_p = Axe^{2x} instead, which does not duplicate y_h."

- question: "For the equation y'' + y = sin(x), a student correctly identifies that the forcing function is sin(x) and guesses y_p = A sin(x). What is wrong with this guess?"
  type: multiple-choice
  options:
    - "Nothing — A sin(x) is the correct form for this equation"
    - "The guess should be A cos(x) instead, since sin differentiates to cos"
    - "The guess should include both terms: A cos(x) + B sin(x), because differentiating introduces the other trig function"
    - "Sine forcing functions require a polynomial guess, not a trigonometric one"
  answer: 2
  explanation: "Whenever f(x) involves sin or cos, the correct guess always includes BOTH A cos(βx) and B sin(βx), even if only one appears in f(x). This is because differentiating sin introduces cos and vice versa: (A cos + B sin)'' = -A cos - B sin, which after substitution can match sin on the right side by choosing A and B independently. A guess of A sin(x) alone would require the cos term to be zero, but the equation has a cos component in its derivatives that forces a nonzero A cos term. Note also that for this particular equation, sin(x) is in y_h (since the characteristic roots are ±i), so the full guess Ax cos(x) + Bx sin(x) is needed."

- question: "When f(x) in y'' + py' + qy = f(x) is a polynomial of degree n, the correct guess for y_p is a polynomial of degree n with all terms from degree 0 through n included."
  type: true-false
  answer: true
  explanation: "The correct guess for a polynomial forcing function is a full polynomial of the same degree: y_p = Aₙxⁿ + Aₙ₋₁xⁿ⁻¹ + ... + A₁x + A₀. All terms must be included because after substitution, lower-degree terms from y_p'' and y_p' can generate contributions at any degree below n, and the coefficients at each degree must be matched. Truncating the guess (e.g., guessing only Axⁿ) would fail to account for these lower-degree contributions."

- question: "The method of undetermined coefficients can be applied to any continuous function f(x), not just polynomials, exponentials, and sinusoids."
  type: true-false
  answer: false
  explanation: "The method only works for functions whose derivatives eventually cycle back to the same family of functions: polynomials (derivatives are polynomials), exponentials (derivatives are multiples of the same exponential), and sines/cosines (derivatives cycle between them). For functions like f(x) = ln(x), tan(x), or 1/x, differentiation produces new functional forms that cannot be matched by a finite-term guess. For these forcing functions, variation of parameters is needed instead."

- question: "Why does the modification rule (multiplying the initial guess by x) fix the resonance problem in the method of undetermined coefficients?"
  type: short-answer
  answer: "When the initial guess y_p duplicates a term already in y_h, substituting it into the left side of the ODE produces zero (since y_h satisfies the homogeneous equation). Multiplying by x produces a new function — e.g., Axe^{2x} instead of Ae^{2x} — that is no longer in y_h, so it does not annihilate when substituted. Differentiation of xe^{αx} produces xe^{αx} and e^{αx} terms, the latter of which can now match the non-zero right side after collecting coefficients and solving for A."
  explanation: "The resonance situation is structurally identical to the repeated-root case in the homogeneous equation: when a root appears twice, the second solution is x times the first (e.g., xe^{rx} alongside e^{rx}). The modification rule imports this same logic to the particular solution — if the natural frequency of the forcing matches a natural frequency of the system, the response grows linearly in x (or x² for double resonance). This connection between algebraic structure and solution behavior is the deep insight linking the two methods."
```

## Explainer

You've already solved y″ + py′ + qy = 0 using the characteristic equation. The roots r₁, r₂ give the **homogeneous solution** y_h — for real distinct roots, y_h = C₁e^{r₁x} + C₂e^{r₂x}. Now add a forcing function f(x) on the right side. The equation is no longer asking "what decays to zero?" but "what produces exactly f(x) when differentiated and combined?" You need a **particular solution** y_p that satisfies the full equation, then combine: the **general solution** is y = y_h + y_p.

The insight behind undetermined coefficients is that differentiation preserves certain functional forms. Derivatives of polynomials are polynomials; derivatives of e^{αx} are multiples of e^{αx}; derivatives of sin(βx) and cos(βx) cycle back to sines and cosines. So if f(x) is built from these forms, a y_p of the same form has a chance of working. The strategy: **guess the form of y_p, substitute into the ODE, and solve for the unknown coefficients** by matching both sides.

The guessing rules: if f(x) = xⁿ (polynomial of degree n), try y_p = Aₙxⁿ + ··· + A₁x + A₀ (a full polynomial of degree n). If f(x) = e^{αx}, try y_p = Ae^{αx}. If f(x) = sin(βx) or cos(βx), always try y_p = A cos(βx) + B sin(βx) together — even if only sine or cosine appears in f, both terms are needed because differentiating introduces the other. Products combine: f(x) = x²e^{3x} calls for y_p = (Ax² + Bx + C)e^{3x}.

The critical exception is the **modification rule** (also called the resonance case). If your initial guess for y_p would duplicate a term already present in y_h, that guess will produce zero when substituted into the left side of the homogeneous part and can never match f(x). The fix: multiply the guess by x. If the duplication persists, multiply by x². For example, if y_h includes e^{2x} and f(x) = e^{2x}, the usual guess Ae^{2x} fails — use Axe^{2x} instead. This modification is analogous to the repeated-root adjustment in the characteristic equation method, and understanding why it's needed connects the algebra directly to the structure of the solution space.
