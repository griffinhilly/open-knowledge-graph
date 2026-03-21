---
id: operations-with-complex-numbers
title: Operations with Complex Numbers
domain: mathematics
course: algebra-2
prerequisites:
  - id: complex-numbers-intro
    type: hard
  - id: multiplying-polynomials
    type: hard
builds-toward:
  - solving-quadratic-equations-completing-the-square
  - fundamental-theorem-of-algebra
tags: [complex-numbers, addition, multiplication, conjugates]
stage: abstract-reasoning
status: validated
---

# Operations with Complex Numbers

## Core Idea
Complex numbers support all standard arithmetic. Addition/subtraction: combine real parts and imaginary parts separately. Multiplication: use FOIL and replace i^2 with -1. Division: multiply numerator and denominator by the conjugate of the denominator (a - bi). The conjugate of a + bi is a - bi, and (a + bi)(a - bi) = a^2 + b^2, a real number. The modulus |a + bi| = sqrt(a^2 + b^2) gives the distance from the origin in the complex plane.

## How It's Best Learned
Practice each operation separately, then mix them. For multiplication, emphasize the FOIL-then-simplify process. For division, show that multiplying by the conjugate eliminates i from the denominator. Connect modulus to the distance formula. Give problems that combine multiple operations.

## Common Misconceptions
- Forgetting to replace i^2 with -1 after multiplying.
- Not using the conjugate when dividing (trying to "divide" complex numbers directly).
- Thinking (a + bi)^2 = a^2 + b^2 (it is a^2 + 2abi - b^2).
- Confusing |a + bi| with a + b.

## Questions

```yaml
- question: "What is the result of (2 + 3i)(1 − i)?"
  type: multiple-choice
  options:
    - "5 + i"
    - "2 − 2i"
    - "2 + i"
    - "−1 + 5i"
  answer: 0
  explanation: "Using FOIL: (2 + 3i)(1 − i) = 2 − 2i + 3i − 3i². Replacing i² with −1 gives 2 − 2i + 3i + 3 = 5 + i. Option B is the classic error of leaving i² unreplaced — if a student treats i² as just i, the last term becomes −3i and they get 2 − 2i. The substitution i² = −1 is the single rule that makes complex multiplication work; skipping it produces a result that still contains i², which is not simplified."

- question: "What is (3 + i) ÷ (1 + 2i)?"
  type: multiple-choice
  options:
    - "1 − i"
    - "3 − i"
    - "(1 + 7i)/5"
    - "(5 − 5i)/3"
  answer: 0
  explanation: "Multiply numerator and denominator by the conjugate (1 − 2i): numerator = (3 + i)(1 − 2i) = 3 − 6i + i − 2i² = 3 − 5i + 2 = 5 − 5i; denominator = 1² + 2² = 5. Result: (5 − 5i)/5 = 1 − i. Option C results from multiplying by (1 + 2i)/(1 + 2i) instead of the conjugate — the imaginary terms in the denominator add rather than cancel, so the denominator remains complex."

- question: "The product of any complex number and its conjugate is always a real number."
  type: true-false
  answer: true
  explanation: "(a + bi)(a − bi) = a² − (bi)² = a² − b²i² = a² + b². The imaginary parts cancel exactly because the conjugate has the opposite sign on the imaginary component. This is the difference-of-squares pattern applied to complex numbers, and it is precisely why multiplying by the conjugate is the standard strategy for dividing complex numbers."

- question: "The modulus of 3 + 4i is 7."
  type: true-false
  answer: false
  explanation: "The modulus |a + bi| = √(a² + b²), not a + b. For 3 + 4i: |3 + 4i| = √(9 + 16) = √25 = 5. The common error is adding the real and imaginary parts directly (3 + 4 = 7), but the modulus is the Pythagorean distance from the origin to the point (3, 4) in the complex plane — the two components are legs of a right triangle, and the modulus is the hypotenuse."

- question: "Why does multiplying both the numerator and denominator of a complex fraction by the conjugate of the denominator allow you to simplify the result?"
  type: short-answer
  answer: "Multiplying a complex number by its conjugate eliminates the imaginary part: (a + bi)(a − bi) = a² + b², a real number. Applying this to the denominator converts the divisor from a complex number to a real number, making ordinary division straightforward. Multiplying both numerator and denominator by the same expression preserves the value of the fraction (you are multiplying by 1 in the form conjugate/conjugate), so only the form changes."
  explanation: "The key is the identity (a + bi)(a − bi) = a² + b². Once the denominator is real, you can divide the numerator's real and imaginary parts separately by that real number. This is not a trick but a direct application of the difference-of-squares pattern, which guarantees that the cross terms (involving i) always cancel when you multiply conjugate pairs."
```

## Explainer

Complex arithmetic follows exactly the same rules as polynomial arithmetic over the reals — the only difference is the single reduction rule i² = -1. Once you internalize that, complex arithmetic stops feeling special and starts feeling routine. Think of a + bi as a polynomial in i of degree 1, and every operation you learned for polynomials applies directly, with one extra simplification step at the end.

**Addition** is the simplest operation: add real parts together and imaginary parts together, just as you add like terms in polynomials. (3 + 2i) + (1 - 5i) = 4 - 3i. **Multiplication** is FOIL applied to the two binomials, then one substitution: wherever i² appears, replace it with -1. For example, (2 + 3i)(1 - i) = 2 - 2i + 3i - 3i² = 2 + i - 3(-1) = 5 + i. If you skip the substitution, you'll have a nonsensical i² term remaining — so the substitution is the entire trick, not an optional cleanup.

**Division** is the operation that surprises most students, because you cannot divide complex numbers directly. The strategy is to convert the division into multiplication: multiply numerator and denominator by the **conjugate** of the denominator. The conjugate of (a + bi) is (a - bi), and their product (a + bi)(a - bi) = a² + b² is always a real number — no imaginary part. This is because you're applying the difference of squares pattern: (a + bi)(a - bi) = a² - (bi)² = a² - b²i² = a² + b². So to compute (3 + i)/(1 + 2i): multiply by (1 - 2i)/(1 - 2i) to get (3 + i)(1 - 2i)/((1)² + (2)²) = (3 - 6i + i - 2i²)/5 = (3 - 5i + 2)/5 = (5 - 5i)/5 = 1 - i.

The **modulus** |a + bi| = √(a² + b²) measures the distance from the origin to the point (a, b) in the complex plane. This is just the Pythagorean theorem — the real and imaginary parts are the two legs, and the modulus is the hypotenuse. The modulus has a multiplicative property: |z₁ · z₂| = |z₁| · |z₂|. This geometric view of complex numbers — where moduli multiply under multiplication and distances behave like magnitudes — is the foundation for polar form and for understanding why complex numbers are so powerful in describing rotations and waves.
