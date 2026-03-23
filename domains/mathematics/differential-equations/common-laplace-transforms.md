---
id: common-laplace-transforms
title: Common Laplace Transform Pairs
domain: mathematics
course: differential-equations
prerequisites:
- id: laplace-transform-definition
  type: hard
builds-toward:
- inverse-laplace-transform
tags:
- laplace-transform
- tables
- common-functions
stage: formal-systems
status: validated
---

# Common Laplace Transform Pairs

## Core Idea
Standard Laplace transforms include: L[1] = 1/s, L[t^n] = n!/s^(n+1), L[e^(at)] = 1/(s-a), L[sin(bt)] = b/(s²+b²), L[cos(bt)] = s/(s²+b²). Tables of these pairs are essential references. Combinations via linearity and shifting theorems yield transforms of more complex functions, including step functions, impulses, and piecewise-defined inputs.

## Questions

```yaml
- question: "To find L[e^(3t) sin(2t)], which approach is most efficient?"
  type: multiple-choice
  options:
    - "Compute ∫₀^∞ e^(−st) e^(3t) sin(2t) dt directly from the definition"
    - "Use L[sin(2t)] = 2/(s²+4) and apply the first shifting theorem, replacing s with s−3 to get 2/((s−3)²+4)"
    - "Multiply the separate transforms: L[e^(3t)] · L[sin(2t)] = (1/(s−3)) · (2/(s²+4))"
    - "Apply integration by parts with u = e^(3t) and dv = sin(2t) dt twice"
  answer: 1
  explanation: "The first shifting (s-shift) theorem states L[e^(at)f(t)] = F(s−a). Since L[sin(2t)] = 2/(s²+4), multiplying by e^(3t) simply shifts s to s−3, giving 2/((s−3)²+4) immediately. Option C is a common error: the Laplace transform of a product is NOT the product of transforms (that would be convolution in the time domain). The direct integral (A) works but is inefficient; the shifting theorem exists precisely to avoid repeating that computation."

- question: "Which best explains why the transform pair L[t^n] = n!/s^(n+1) holds?"
  type: multiple-choice
  options:
    - "Because t^n is always non-negative for even n, guaranteeing the integral converges"
    - "It is an empirical result confirmed numerically and must be taken from the table"
    - "Repeated integration by parts reduces the integral — each step pulls down a factor of the current power and gains an extra 1/s — yielding n! in the numerator after n steps"
    - "It follows directly from the s-shift theorem applied to L[1] = 1/s"
  answer: 2
  explanation: "The result is derived by computing ∫₀^∞ t^n e^(−st) dt via integration by parts (or by recognizing it as the gamma function). Each application of integration by parts reduces the power of t by 1 while contributing a factor of 1/s to the denominator. After n steps the integral reduces to ∫₀^∞ e^(−st) dt = 1/s, and the accumulated prefactor is n · (n−1) · ... · 1 = n!. The s-shift theorem shifts s but does not create polynomial factors, so option D is incorrect."

- question: "Because the Laplace transform is linear, L[3cos(2t) − 5sin(t)] can be computed by transforming each term separately and combining the results."
  type: true-false
  answer: true
  explanation: "Linearity states L[af + bg] = aL[f] + bL[g], mirroring the linearity of integration. So L[3cos(2t) − 5sin(t)] = 3·L[cos(2t)] − 5·L[sin(t)] = 3·s/(s²+4) − 5·1/(s²+1). This is one of the two most powerful tools for extending the basic table — linearity plus the shifting theorems handle the vast majority of functions encountered in ODE applications."

- question: "The Laplace transform of a product of two functions equals the product of their individual Laplace transforms: L[f(t)g(t)] = F(s)G(s)."
  type: true-false
  answer: false
  explanation: "This is a very common and consequential error. The Laplace transform does NOT distribute over products: L[f(t)g(t)] ≠ F(s)G(s) in general. The correct relationship for products involves convolution: L[f*g] = F(s)G(s), where (f*g)(t) = ∫₀^t f(τ)g(t−τ) dτ is the convolution of f and g. To handle products like e^(at)sin(bt), use the s-shift theorem — not multiplication of transforms."

- question: "Explain why the first shifting theorem (s-shift) is useful in practice. What does it let you do that you couldn't easily do otherwise?"
  type: short-answer
  answer: "The s-shift theorem states that multiplying a time-domain function f(t) by e^(at) shifts the transform variable: L[e^(at)f(t)] = F(s−a). This means you can immediately write down transforms of exponentially modulated functions — like e^(2t)cos(3t) or e^(−t)t² — by taking the known basic transform and replacing s with s−a, without computing a new integral. It dramatically extends the table with no additional computation."
  explanation: "Without the shifting theorem, every new exponentially modulated function would require computing a fresh integral from the definition. The theorem recognizes a structural pattern — multiplying by e^(at) in time corresponds to a horizontal shift in s-space — and packages that pattern as a reusable rule. Combined with linearity and the basic pairs, it covers the overwhelming majority of functions arising in ODE initial-value problems."
```

## Explainer

From the Laplace transform definition, you know that L[f(t)] = ∫₀^∞ e^(−st) f(t) dt converts a function of t into a function of s. Each entry in the transform table comes from computing this integral once, carefully, and then recording the result so you never have to do it again. Understanding a handful of derivations — rather than memorizing all entries blindly — is enough to reconstruct the table and extend it when you encounter unfamiliar functions.

The simplest entry is L[1] = 1/s. Compute: ∫₀^∞ e^(−st) · 1 dt = [−(1/s)e^(−st)]₀^∞ = 0 − (−1/s) = 1/s, valid for s > 0. The next step up is L[t^n] = n!/s^(n+1), derived by repeated integration by parts (or by recognizing the gamma function integral). For n = 1: ∫₀^∞ t e^(−st) dt = 1/s². For general n, each integration by parts pulls down a factor of n and increases the power of s in the denominator, yielding n! in the numerator. The exponential L[e^(at)] = 1/(s−a) follows from the same first integral with s replaced by s−a, valid for s > a. Trig transforms follow from Euler's formula: e^(ibt) = cos(bt) + i sin(bt), so L[e^(ibt)] = 1/(s − ib); separating real and imaginary parts gives L[cos(bt)] = s/(s² + b²) and L[sin(bt)] = b/(s² + b²).

Once you have the basic pairs, two theorems extend them enormously. **Linearity** means L[af + bg] = aL[f] + bL[g]: you can transform linear combinations term by term, just like differentiation and integration. **The first shifting theorem** (s-shift) says L[e^(at)f(t)] = F(s−a) where F = L[f]: multiplying by an exponential in t shifts the transform variable s. So L[e^(2t)sin(3t)] = 3/((s−2)² + 9) simply by replacing s with s−2 in L[sin(3t)] = 3/(s² + 9). The **second shifting theorem** (t-shift) handles step functions: L[u_c(t) f(t−c)] = e^(−cs) F(s), where u_c is the Heaviside step function turning on at t = c. This lets you transform piecewise-defined functions that switch behavior at specific times — exactly what arises in engineering problems with switching inputs.

The real value of these tables emerges when solving ODEs. After transforming an initial-value problem, you obtain an algebraic expression in s for Y(s) = L[y(t)]. To recover y(t), you decompose Y(s) into a sum of recognizable table entries — often using partial fractions — and read off the inverse transform from the table. The transforms of derivatives (L[y'] = sY − y(0), L[y''] = s²Y − sy(0) − y'(0)) are how initial conditions enter. Knowing the common transform pairs fluently means you can match the pieces of a partial fraction decomposition to table entries immediately, turning the inverse transform step from a bottleneck into a mechanical lookup.
