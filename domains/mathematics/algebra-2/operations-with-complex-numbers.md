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

## Explainer

Complex arithmetic follows exactly the same rules as polynomial arithmetic over the reals — the only difference is the single reduction rule i² = -1. Once you internalize that, complex arithmetic stops feeling special and starts feeling routine. Think of a + bi as a polynomial in i of degree 1, and every operation you learned for polynomials applies directly, with one extra simplification step at the end.

**Addition** is the simplest operation: add real parts together and imaginary parts together, just as you add like terms in polynomials. (3 + 2i) + (1 - 5i) = 4 - 3i. **Multiplication** is FOIL applied to the two binomials, then one substitution: wherever i² appears, replace it with -1. For example, (2 + 3i)(1 - i) = 2 - 2i + 3i - 3i² = 2 + i - 3(-1) = 5 + i. If you skip the substitution, you'll have a nonsensical i² term remaining — so the substitution is the entire trick, not an optional cleanup.

**Division** is the operation that surprises most students, because you cannot divide complex numbers directly. The strategy is to convert the division into multiplication: multiply numerator and denominator by the **conjugate** of the denominator. The conjugate of (a + bi) is (a - bi), and their product (a + bi)(a - bi) = a² + b² is always a real number — no imaginary part. This is because you're applying the difference of squares pattern: (a + bi)(a - bi) = a² - (bi)² = a² - b²i² = a² + b². So to compute (3 + i)/(1 + 2i): multiply by (1 - 2i)/(1 - 2i) to get (3 + i)(1 - 2i)/((1)² + (2)²) = (3 - 6i + i - 2i²)/5 = (3 - 5i + 2)/5 = (5 - 5i)/5 = 1 - i.

The **modulus** |a + bi| = √(a² + b²) measures the distance from the origin to the point (a, b) in the complex plane. This is just the Pythagorean theorem — the real and imaginary parts are the two legs, and the modulus is the hypotenuse. The modulus has a multiplicative property: |z₁ · z₂| = |z₁| · |z₂|. This geometric view of complex numbers — where moduli multiply under multiplication and distances behave like magnitudes — is the foundation for polar form and for understanding why complex numbers are so powerful in describing rotations and waves.
