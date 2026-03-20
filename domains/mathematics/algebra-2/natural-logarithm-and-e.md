---
id: natural-logarithm-and-e
title: Natural Logarithm and e
domain: mathematics
course: algebra-2
prerequisites:
- id: logarithms-intro
  type: hard
- id: exponential-growth-and-decay
  type: hard
- id: solving-exponential-equations
  type: soft
- id: solving-logarithmic-equations
  type: soft
builds-toward:
- limit-definition-intuitive
- derivative-as-slope-of-tangent
tags:
- natural-logarithm
- e
- euler
- continuous-compounding
stage: formal-systems
status: validated
---
# Natural Logarithm and e

## Core Idea
The number e (approximately 2.71828) is the base of the natural exponential function and natural logarithm. It arises naturally from continuous compounding: as n approaches infinity, (1 + 1/n)^n approaches e. The natural logarithm ln(x) = log_e(x) is the inverse of e^x. The pair (e^x, ln(x)) is fundamental in calculus because the derivative of e^x is e^x itself. Continuous growth/decay is modeled by A = A_0 * e^(kt).

## How It's Best Learned
Motivate e through compound interest: show that compounding more frequently approaches a limit. Define e as that limit. Practice converting between e^x = y and ln(y) = x. Solve equations involving e^x and ln(x). Compare natural log with common log. Emphasize that e is just a number (albeit irrational and transcendental), not a variable.

## Common Misconceptions
- Thinking e is a variable rather than a specific constant.
- Confusing ln(x) with log(x) (ln uses base e, log typically uses base 10).
- Thinking ln(e) = e (ln(e) = 1, because e^1 = e).
- Not recognizing that ln(1) = 0 and ln(e^x) = x.

## Questions

```yaml
- question: "What is the value of ln(e²)?"
  type: multiple-choice
  options: ["e", "2e", "2", "1/2"]
  answer: 2
  explanation: "ln and e^x are inverse functions, so ln(e^x) = x for any x. Therefore ln(e²) = 2. A common error is thinking the answer involves e itself, confusing the base with the exponent the logarithm returns."

- question: "The expression ln(e) equals e, since the natural log and e are closely related."
  type: true-false
  answer: false
  explanation: "ln(e) = 1, not e. The logarithm asks: 'e to what power gives me this input?' Since e¹ = e, the answer is 1. A logarithm always returns an exponent — a number, never the base itself."

- question: "A savings account compounds interest continuously at 5% per year. Write the formula for the balance A after t years if the initial principal is A₀."
  type: short-answer
  answer: "A = A₀ · e^(0.05t)"
  explanation: "Continuous compounding uses A = A₀ · e^(kt), where k is the annual rate as a decimal. Here k = 0.05. This formula arises because e is defined as the limit of (1 + 1/n)^n as n → ∞, capturing what happens when compounding becomes infinitely frequent."
```

## Explainer

You have already worked with exponential functions like 2^x and 10^x. The number e (approximately 2.71828) looks like an odd choice for a base, but it emerges from a concrete question: what happens if you compound interest not monthly, not daily, but continuously — every instant? Start with $1 at 100% annual interest. Compounded n times per year, the balance after one year is (1 + 1/n)^n. As n grows toward infinity, this expression does not blow up — it converges to a specific constant: e. That is where e comes from, and why it appears throughout every model of continuous growth or decay.

The natural logarithm, written ln(x), is simply the logarithm with base e. Just as log₁₀(1000) = 3 because 10³ = 1000, ln(e³) = 3 because e³ is indeed e³. Because ln and e^x are inverse functions, they undo each other: e^(ln x) = x and ln(e^x) = x. This inverse relationship is the key to solving equations — apply one function to both sides to cancel the other.

Three values are worth internalizing: ln(1) = 0 (because e⁰ = 1), ln(e) = 1 (because e¹ = e), and ln(e^k) = k for any k. A frequent misconception is that ln(e) = e — but the logarithm asks for an exponent, not the base. The answer is always a plain number. Here it is 1.

Continuous growth and decay are modeled by A = A₀ · e^(kt). If k > 0 the quantity grows; if k < 0 it decays. To solve for time or rate, take ln of both sides: if A/A₀ = e^(kt), then ln(A/A₀) = kt. This is the same algebraic move you practiced with other exponential equations, just using ln in place of log.

The deeper reason e is indispensable — one you will explore in calculus — is that the derivative of e^x is e^x itself. It is the only function that is its own rate of change. This makes e the natural base for any process where the rate of change is proportional to the current value: population growth, radioactive decay, Newton's law of cooling, and more.
