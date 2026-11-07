---
id: bernoulli-differential-equations
title: Bernoulli Equations and Substitution Methods
domain: mathematics
course: differential-equations
prerequisites:
  - id: integrating-factor-method
    type: hard
  - id: separable-differential-equations
    type: soft
builds-toward: []
tags: [differential-equations, first-order, nonlinear, substitution, bernoulli-equation]
stage: formal-systems
status: validated
---

# Bernoulli Equations and Substitution Methods

## Core Idea
A Bernoulli equation has the form y' + P(x)y = Q(x)yⁿ, where n is a real number other than 0 or 1. It is nonlinear, but the substitution v = y^(1-n) turns it into the linear equation v' + (1 - n)P(x)v = (1 - n)Q(x), which an integrating factor solves. The broader lesson is that a well-chosen change of variable can turn an equation you cannot solve into one you can. The logistic equation is a familiar Bernoulli equation with n = 2.

## How It's Best Learned
Derive the substitution once in general so students see why the exponent 1 - n is the right choice, then practice the steps on equations with n = 2, n = 3 and n = 1/2. Always check the final answer by substituting it back into the original equation. Point out the solution y = 0, which is easy to lose when dividing by yⁿ.

## Common Misconceptions
- Bernoulli equations must be solved by separation of variables. (Most are not separable; the substitution v = y^(1-n) makes them linear instead.)
- The substitution is v = yⁿ. (The correct substitution is v = y^(1-n), which makes the y^(1-n) term and the derivative term match.)
- Dividing by yⁿ loses nothing. (For n > 0, the constant solution y = 0 can be lost and must be checked separately.)
- The method works for n = 0 or n = 1. (Those cases are already linear and need no substitution; the formula v = y^(1-n) is useless when n = 1.)

## Questions

```yaml
- question: "Which substitution turns y' + 2y = xy³ into a linear equation?"
  type: multiple-choice
  options: ["v = y³", "v = y⁻²", "v = y²", "v = ln y"]
  answer: 1
  explanation: "Here n = 3, so v = y^(1-n) = y⁻². Then v' = -2y⁻³y', and dividing the equation by y³ gives y⁻³y' + 2y⁻² = x, which becomes -v'/2 + 2v = x, a linear equation in v."

- question: "Solve y' + y = y²."
  type: short-answer
  answer: "y = 1/(1 + Ceˣ), together with the solution y = 0."
  explanation: "With n = 2, set v = y⁻¹, so v' = -y⁻²y'. Dividing by y² gives y⁻²y' + y⁻¹ = 1, which becomes -v' + v = 1, or v' - v = -1. Its solution is v = 1 + Ceˣ, so y = 1/(1 + Ceˣ). Dividing by y² excluded y = 0, which also satisfies the equation."

- question: "Every Bernoulli equation with n ≠ 0, 1 is a linear differential equation in y."
  type: true-false
  answer: false
  explanation: "The term Q(x)yⁿ makes the equation nonlinear in y whenever n is not 0 or 1. The equation becomes linear only in the new variable v = y^(1-n)."

- question: "The logistic equation P' = rP(1 - P/K) can be written P' - rP = -(r/K)P². What is n, and what substitution linearizes it?"
  type: multiple-choice
  options:
    - "n = 1, v = P"
    - "n = 2, v = P⁻¹"
    - "n = 2, v = P²"
    - "n = -1, v = P²"
  answer: 1
  explanation: "The right side is a multiple of P², so n = 2 and the substitution is v = P^(1-2) = 1/P. The resulting linear equation is v' + rv = r/K, whose solution leads to the familiar S-shaped logistic curve."
```

## Explainer

You can solve first-order linear equations y' + P(x)y = Q(x) with an integrating factor. Many models are slightly nonlinear, though, and one family is close enough to linear that a substitution rescues it. A Bernoulli equation, named for Jacob Bernoulli, has the form

y' + P(x)y = Q(x)yⁿ, with n ≠ 0, 1.

When n = 0 or n = 1 the equation is linear. Otherwise the yⁿ term makes it nonlinear.

The idea is to divide by yⁿ and look for a new variable. Dividing gives

y⁻ⁿy' + P(x)y^(1-n) = Q(x).

Now set v = y^(1-n). By the chain rule, v' = (1 - n)y⁻ⁿy', so y⁻ⁿy' = v'/(1 - n). Substituting,

v'/(1 - n) + P(x)v = Q(x), or v' + (1 - n)P(x)v = (1 - n)Q(x).

This equation is linear in v. Solve it with an integrating factor, then recover y from y = v^(1/(1-n)). The exponent 1 - n is chosen exactly so that the derivative term and the P(x) term involve the same new variable.

Example: y' + y = y². Here n = 2, so v = y⁻¹. Dividing by y² gives y⁻²y' + y⁻¹ = 1. Since v' = -y⁻²y', this becomes -v' + v = 1, or v' - v = -1. The integrating factor is e⁻ˣ, and the solution is v = 1 + Ceˣ. Therefore y = 1/(1 + Ceˣ). Check by substitution: the derivative is y' = -Ceˣ/(1 + Ceˣ)², and y' + y simplifies to 1/(1 + Ceˣ)², which is y².

When we divided by y², we assumed y ≠ 0. The constant function y = 0 also solves y' + y = y², and it does not come from the formula for any value of C. For n > 0, always check y = 0 separately.

The logistic population model P' = rP(1 - P/K) is a Bernoulli equation with n = 2. The substitution v = 1/P turns it into the linear equation v' + rv = r/K, which gives a second route to the logistic solution besides separation of variables.

Bernoulli equations are one example of a general strategy. Homogeneous equations y' = F(y/x) yield to the substitution v = y/x, and equations y' = G(ax + by) yield to v = ax + by. In each case, the right substitution turns an unfamiliar equation into a known type.
