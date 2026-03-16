---
id: limits-continuity-complex-functions
title: Limits and Continuity of Complex Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: convergence-complex-sequences
  type: hard
- id: complex-functions-mappings
  type: hard
builds-toward:
- complex-differentiability
- holomorphic-functions
tags:
- limits
- continuity
- topology
stage: advanced
status: draft
---

# Limits and Continuity of Complex Functions

## Core Idea
A function f has limit L at z₀ if lim(z→z₀) f(z) = L means for every ε > 0 there exists δ > 0 such that |z - z₀| < δ implies |f(z) - L| < ε. A function is continuous at z₀ if lim(z→z₀) f(z) = f(z₀). Continuity is equivalent to each real part u and imaginary part v being continuous as functions from ℝ² to ℝ.

## Explainer

You already know how complex sequences converge: a sequence {zₙ} converges to L if |zₙ - L| → 0, meaning the distance in the complex plane shrinks to zero. You also know that a complex function f(z) maps points in the complex plane to other points in the complex plane, and you can write f(z) = u(x,y) + iv(x,y) where z = x + iy. Limits and continuity of complex functions combine both of these ideas using the same ε-δ framework from real analysis — but the geometry is fundamentally two-dimensional, which changes what "approaching z₀" means.

In real analysis, x can approach x₀ from only two directions: the left or the right. For a limit to exist, both one-sided limits must agree. In the complex plane, z can approach z₀ from **infinitely many directions** — along any ray, spiral, or curve leading to z₀. The definition |z - z₀| < δ means "within a disk of radius δ centered at z₀," so the limit condition must hold no matter which path z takes through that disk. This makes complex limits stricter than real limits: a function with different values along different approach paths has no limit at that point.

A powerful consequence is the **component criterion**: f(z) = u(x,y) + iv(x,y) has limit L = a + ib at z₀ = x₀ + iy₀ if and only if u(x,y) → a and v(x,y) → b as (x,y) → (x₀,y₀) in ℝ². This reduces a complex limit to two real multivariable limits. Similarly, f is continuous at z₀ if and only if u and v are both continuous as real functions at (x₀,y₀). Continuity of the component functions is both necessary and sufficient — there is no extra "complex" condition beyond this pair of real conditions.

The stricter path-independence requirement becomes essential in the next step of complex analysis: complex differentiability. A real function can have a derivative even if it approaches from only two directions; a complex function must behave consistently along every possible path to z₀ before it can be differentiated. This extra constraint turns out to force remarkably strong structure — functions that are differentiable in the complex sense (holomorphic functions) are infinitely differentiable and equal their Taylor series everywhere they are defined. The strictness you see here in limits and continuity is the first sign that complex analysis will be far more rigid and powerful than real analysis.
