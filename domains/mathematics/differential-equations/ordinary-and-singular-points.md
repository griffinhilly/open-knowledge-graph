---
id: ordinary-and-singular-points
title: Ordinary and Singular Points of ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series-solutions
  type: hard
builds-toward:
- frobenius-method
tags:
- series
- classification
- analytic
stage: advanced
status: validated
---

# Ordinary and Singular Points of ODEs

## Core Idea
For y'' + p(x)y' + q(x)y = 0, a point x₀ is ordinary if p and q are analytic at x₀ (power series solutions exist), and singular if either is not. Regular singular points admit Frobenius series solutions; irregular singular points do not.

## Questions

```yaml
- question: "A student encounters y'' + (1/x)y' + (1/x²)y = 0 and begins computing a standard power series solution y = Σaₙxⁿ centered at x₀ = 0. After extensive algebra, the method fails. Based on classifying x₀ = 0, what went wrong?"
  type: multiple-choice
  options:
    - "x = 0 is an ordinary point, so the standard series should converge — the student made an algebraic error."
    - "x = 0 is a regular singular point, so the standard power series method doesn't apply there; the Frobenius method should be used instead."
    - "x = 0 is an irregular singular point, so no series solution exists near the origin."
    - "Power series must be centered at x = 1 to avoid the singularity at the origin."
  answer: 1
  explanation: "For this equation, p(x) = 1/x and q(x) = 1/x². Check: (x − 0)·p(x) = x·(1/x) = 1 (analytic at 0); (x − 0)²·q(x) = x²·(1/x²) = 1 (analytic at 0). Both multiplied forms are analytic, so x = 0 is a regular singular point — not an ordinary point. The standard power series assumes analyticity of p and q at x₀, which fails here. The Frobenius method (assuming y = x^r·Σaₙxⁿ) is the right tool for regular singular points. Option 2 is wrong because the singularity is not irregular; option 3 misunderstands that shifting the center doesn't resolve a singularity."

- question: "For the ODE y'' + (3/x)y' + (1/x²)y = 0, classify x₀ = 0."
  type: multiple-choice
  options:
    - "Ordinary point — both p(x) and q(x) are defined for all x ≠ 0."
    - "Regular singular point — (x − 0)p(x) = 3 and (x − 0)²q(x) = 1 are both analytic at x = 0."
    - "Irregular singular point — both p(x) and q(x) blow up at x = 0, making it worse than a regular singularity."
    - "Cannot be classified without knowing boundary or initial conditions."
  answer: 1
  explanation: "The test for a regular singular point: compute (x − x₀)p(x) and (x − x₀)²q(x) and check analyticity at x₀. Here, x·(3/x) = 3 (a constant, definitely analytic) and x²·(1/x²) = 1 (also analytic). So x = 0 is a regular singular point. Option 2 is the common error: seeing that p and q blow up at x = 0 and concluding the singularity is 'irregular.' The key is not whether p and q blow up but whether the blow-up is mild enough for the multiplied forms to remain analytic. p(x) has at most a simple pole and q(x) has at most a double pole — exactly the regular singular threshold."

- question: "Near an ordinary point x₀, a power series solution y = Σaₙ(x − x₀)ⁿ is guaranteed to converge in a neighborhood that extends at least as far as the nearest singular point."
  type: true-false
  answer: true
  explanation: "This is the existence theorem for power series solutions near ordinary points. The radius of convergence of the solution series is at least as large as the distance from x₀ to the nearest singular point in the complex plane. This gives a concrete, computable lower bound for how far the series solution is valid. Knowing where the singular points are therefore tells you, in advance, the minimum radius of convergence of any power series solution centered at an ordinary point — before you compute a single coefficient."

- question: "Any point where p(x) or q(x) becomes unbounded in y'' + p(x)y' + q(x)y = 0 is an irregular singular point, requiring methods beyond Frobenius."
  type: true-false
  answer: false
  explanation: "This conflates 'singular point' with 'irregular singular point.' A point where p(x) or q(x) is not analytic is a singular point, but it may be regular or irregular. The distinction is the rate of blow-up: if p(x) has at most a simple pole and q(x) has at most a double pole at x₀ — equivalently, if (x − x₀)p(x) and (x − x₀)²q(x) are both analytic at x₀ — then the singularity is regular, and the Frobenius method applies. Only when (x − x₀)p(x) or (x − x₀)²q(x) still fails to be analytic do we have an irregular singular point where Frobenius also fails."

- question: "Why is it important to classify a point as ordinary, regular singular, or irregular singular before attempting to find a series solution? What happens if you skip this step?"
  type: short-answer
  answer: "The classification determines which solution method applies. Near an ordinary point, a standard power series y = Σaₙ(x − x₀)ⁿ works and two independent solutions are guaranteed. Near a regular singular point, you need the Frobenius method: y = (x − x₀)^r·Σaₙ(x − x₀)ⁿ, where the exponent r is determined by the indicial equation. Near an irregular singular point, neither method works, and more advanced techniques are needed. If you skip classification and attempt a standard power series at a singular point, the recurrence relation for the coefficients will typically fail — infinite or undefined coefficients, or a recursion that collapses to zero solutions. You end up with a lot of algebra and no valid solution, with no clear diagnostic for why."
  explanation: "This is the practical payoff of the classification: it is a decision tree that saves wasted effort. The exam skill is not just knowing the definitions but applying the test (compute (x−x₀)p and (x−x₀)²q, check analyticity) before choosing a solution strategy. Identifying the point type before computing is as important as the computation itself."
```

## Explainer

From your work with power series solutions, you know that you can assume y = ∑ aₙ(x − x₀)ⁿ, substitute into a differential equation, and solve for the coefficients by matching powers of (x − x₀). This method works beautifully when the equation behaves well near x₀. But not all equations behave well everywhere: some have coefficients that blow up at certain points, and near those points the standard power series method breaks down. The classification into ordinary and singular points is exactly the question of where the method works versus where it needs modification.

Write the equation in **standard form**: y'' + p(x)y' + q(x)y = 0. A point x₀ is called an **ordinary point** if both p(x) and q(x) are analytic at x₀ — meaning each can be represented by a convergent power series in a neighborhood of x₀. Near an ordinary point, the existence theorem guarantees two linearly independent power series solutions, and the radius of convergence extends at least as far as the nearest singular point. The familiar examples (like Hermite's equation or simple harmonic oscillator) have no singular points or have them far from the origin, which is why power series solutions in those cases are straightforward.

A **singular point** is any x₀ where p(x) or q(x) fails to be analytic. Not all singular points are equally bad. A point x₀ is a **regular singular point** if (x − x₀)p(x) and (x − x₀)²q(x) are both analytic at x₀ — that is, p(x) has at most a simple pole and q(x) has at most a double pole at x₀. The multiplication by (x − x₀) and (x − x₀)² "removes" the bad behavior just enough. The Euler equation x²y'' + αxy' + βy = 0 is the prototype: at x₀ = 0, p(x) = α/x (simple pole) and q(x) = β/x² (double pole), so x · p(x) = α and x² · q(x) = β are both constant — definitely analytic. Euler equations are exactly the regular singular case in its purest form.

An **irregular singular point** is one where the singularity is worse: (x − x₀)p(x) or (x − x₀)²q(x) is still singular. Near irregular singular points, power series and Frobenius series both fail, and solutions typically involve essential singularities, exponential factors, or formal divergent series. The theory is much harder and outside most first courses.

The classification matters because it tells you which tool to reach for. Near an ordinary point, use standard power series. Near a regular singular point, use the **Frobenius method** (which you'll study next): assume y = (x − x₀)^r ∑ aₙ(x − x₀)ⁿ, where the exponent r is determined by the **indicial equation** formed from the coefficients of p and q. The indicial equation typically gives two roots r₁, r₂, and depending on whether r₁ − r₂ is a non-integer, zero, or a positive integer, you get two independent Frobenius series, one series and one series times ln(x − x₀), or other special forms. Identifying the type of point before computing is not a formality — it determines whether you proceed with a standard series, a Frobenius series, or need more advanced methods entirely.
