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
status: draft
---

# Common Laplace Transform Pairs

## Core Idea
Standard Laplace transforms include: L[1] = 1/s, L[t^n] = n!/s^(n+1), L[e^(at)] = 1/(s-a), L[sin(bt)] = b/(s²+b²), L[cos(bt)] = s/(s²+b²). Tables of these pairs are essential references. Combinations via linearity and shifting theorems yield transforms of more complex functions, including step functions, impulses, and piecewise-defined inputs.

## Explainer

From the Laplace transform definition, you know that L[f(t)] = ∫₀^∞ e^(−st) f(t) dt converts a function of t into a function of s. Each entry in the transform table comes from computing this integral once, carefully, and then recording the result so you never have to do it again. Understanding a handful of derivations — rather than memorizing all entries blindly — is enough to reconstruct the table and extend it when you encounter unfamiliar functions.

The simplest entry is L[1] = 1/s. Compute: ∫₀^∞ e^(−st) · 1 dt = [−(1/s)e^(−st)]₀^∞ = 0 − (−1/s) = 1/s, valid for s > 0. The next step up is L[t^n] = n!/s^(n+1), derived by repeated integration by parts (or by recognizing the gamma function integral). For n = 1: ∫₀^∞ t e^(−st) dt = 1/s². For general n, each integration by parts pulls down a factor of n and increases the power of s in the denominator, yielding n! in the numerator. The exponential L[e^(at)] = 1/(s−a) follows from the same first integral with s replaced by s−a, valid for s > a. Trig transforms follow from Euler's formula: e^(ibt) = cos(bt) + i sin(bt), so L[e^(ibt)] = 1/(s − ib); separating real and imaginary parts gives L[cos(bt)] = s/(s² + b²) and L[sin(bt)] = b/(s² + b²).

Once you have the basic pairs, two theorems extend them enormously. **Linearity** means L[af + bg] = aL[f] + bL[g]: you can transform linear combinations term by term, just like differentiation and integration. **The first shifting theorem** (s-shift) says L[e^(at)f(t)] = F(s−a) where F = L[f]: multiplying by an exponential in t shifts the transform variable s. So L[e^(2t)sin(3t)] = 3/((s−2)² + 9) simply by replacing s with s−2 in L[sin(3t)] = 3/(s² + 9). The **second shifting theorem** (t-shift) handles step functions: L[u_c(t) f(t−c)] = e^(−cs) F(s), where u_c is the Heaviside step function turning on at t = c. This lets you transform piecewise-defined functions that switch behavior at specific times — exactly what arises in engineering problems with switching inputs.

The real value of these tables emerges when solving ODEs. After transforming an initial-value problem, you obtain an algebraic expression in s for Y(s) = L[y(t)]. To recover y(t), you decompose Y(s) into a sum of recognizable table entries — often using partial fractions — and read off the inverse transform from the table. The transforms of derivatives (L[y'] = sY − y(0), L[y''] = s²Y − sy(0) − y'(0)) are how initial conditions enter. Knowing the common transform pairs fluently means you can match the pieces of a partial fraction decomposition to table entries immediately, turning the inverse transform step from a bottleneck into a mechanical lookup.
