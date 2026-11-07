---
id: hyperbolic-functions
title: Hyperbolic Functions
domain: mathematics
course: calculus-1
prerequisites:
  - id: derivatives-of-exponential-functions
    type: hard
  - id: trigonometric-identities-pythagorean
    type: soft
builds-toward:
  - complex-trigonometric-functions
  - trigonometric-substitution
tags: [calculus, hyperbolic-functions, sinh, cosh, exponential-functions, derivatives]
stage: formal-systems
status: validated
---

# Hyperbolic Functions

## Core Idea
The hyperbolic sine and cosine are combinations of exponentials: sinh x = (eˣ - e⁻ˣ)/2 and cosh x = (eˣ + e⁻ˣ)/2. They satisfy cosh²x - sinh²x = 1, so the point (cosh t, sinh t) lies on the hyperbola x² - y² = 1, just as (cos t, sin t) lies on the circle x² + y² = 1. Their derivatives are simple: (sinh x)' = cosh x and (cosh x)' = sinh x. They appear in the shape of a hanging cable, in some integrals, and in solutions of differential equations.

## How It's Best Learned
Derive each identity and derivative directly from the exponential definitions, so nothing has to be memorized blind. Graph eˣ/2 and e⁻ˣ/2 and build cosh and sinh from them by adding and subtracting. Compare each hyperbolic identity with its trigonometric counterpart and note where the signs differ.

## Common Misconceptions
- The derivative of cosh x is -sinh x, as with cosine. (It is +sinh x, since the derivative of (eˣ + e⁻ˣ)/2 is (eˣ - e⁻ˣ)/2.)
- Hyperbolic functions are periodic like trigonometric functions. (For real x, sinh and cosh are not periodic; cosh x grows without bound in both directions.)
- The identity cosh²x + sinh²x = 1 holds. (The correct identity is cosh²x - sinh²x = 1.)
- cosh x can take any real value. (cosh x ≥ 1 for every real x, with equality only at x = 0.)

## Questions

```yaml
- question: "What is the derivative of cosh x?"
  type: multiple-choice
  options: ["-sinh x", "sinh x", "cosh x", "-cosh x"]
  answer: 1
  explanation: "cosh x = (eˣ + e⁻ˣ)/2, so its derivative is (eˣ - e⁻ˣ)/2 = sinh x. Unlike cosine, there is no minus sign, because the derivative of e⁻ˣ is -e⁻ˣ."

- question: "For every real number x, cosh²x - sinh²x = 1."
  type: true-false
  answer: true
  explanation: "cosh²x = (e²ˣ + 2 + e⁻²ˣ)/4 and sinh²x = (e²ˣ - 2 + e⁻²ˣ)/4. Subtracting gives 4/4 = 1."

- question: "Evaluate cosh 0 and sinh 0, and explain why cosh x ≥ 1 for all real x."
  type: short-answer
  answer: "cosh 0 = 1 and sinh 0 = 0. Since cosh²x = 1 + sinh²x ≥ 1 and cosh x is positive, cosh x ≥ 1."
  explanation: "At x = 0, e⁰ = 1, so cosh 0 = (1 + 1)/2 = 1 and sinh 0 = (1 - 1)/2 = 0. The identity forces cosh²x ≥ 1, and cosh x is a sum of positive terms divided by 2, so cosh x ≥ 1."

- question: "Which curve describes the shape of a flexible cable hanging under its own weight between two supports?"
  type: multiple-choice
  options: ["A parabola y = ax²", "A catenary y = a cosh(x/a)", "A sine curve y = a sin(x)", "A circle"]
  answer: 1
  explanation: "A uniform hanging cable forms a catenary, which is a scaled hyperbolic cosine. It resembles a parabola near its lowest point but is a different curve."
```

## Explainer

Some combinations of eˣ and e⁻ˣ come up so often that they have their own names. Define

sinh x = (eˣ - e⁻ˣ)/2 and cosh x = (eˣ + e⁻ˣ)/2,

read "hyperbolic sine" and "hyperbolic cosine." The other four hyperbolic functions are built from these the same way the trigonometric ones are: tanh x = sinh x / cosh x, and sech, csch and coth are the reciprocals of cosh, sinh and tanh.

Their graphs come from the exponentials. The function cosh x is the average of eˣ and e⁻ˣ. It is even, has its minimum value 1 at x = 0, and rises in both directions, so its graph looks like a U. The function sinh x is odd, passes through the origin, and increases everywhere. The function tanh x increases from -1 to 1 and has horizontal asymptotes at y = ±1.

The name comes from a key identity. Square the definitions: cosh²x = (e²ˣ + 2 + e⁻²ˣ)/4 and sinh²x = (e²ˣ - 2 + e⁻²ˣ)/4. Subtracting gives cosh²x - sinh²x = 1. So the point (cosh t, sinh t) always lies on the right branch of the hyperbola x² - y² = 1. Compare cos²t + sin²t = 1 for the unit circle. Many hyperbolic identities look like trigonometric ones with some signs changed, for example sinh(2x) = 2 sinh x cosh x and cosh(2x) = cosh²x + sinh²x.

Derivatives follow from the rule (eˣ)' = eˣ and (e⁻ˣ)' = -e⁻ˣ:

(sinh x)' = (eˣ + e⁻ˣ)/2 = cosh x, and (cosh x)' = (eˣ - e⁻ˣ)/2 = sinh x.

Notice that both signs are positive, unlike (cos x)' = -sin x. The quotient rule then gives (tanh x)' = sech²x. Each derivative formula gives an integral formula too, such as ∫ cosh x dx = sinh x + C.

The inverse functions can be written with logarithms. Solving y = sinh x for x gives sinh⁻¹ y = ln(y + √(y² + 1)). This explains why integrals such as ∫ dx/√(x² + 1) produce either an inverse hyperbolic sine or the equivalent logarithm.

Hyperbolic functions also model physical shapes. A uniform cable hanging between two poles takes the shape of a catenary, y = a cosh(x/a). The differential equation y'' = y has the general solution y = A cosh x + B sinh x, which parallels y'' = -y and its solution y = A cos x + B sin x.
