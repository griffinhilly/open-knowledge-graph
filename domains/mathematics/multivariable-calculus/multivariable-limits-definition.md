---
id: multivariable-limits-definition
title: Limits of Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-functions-intro-domain
  type: hard
- id: epsilon-delta-continuity
  type: soft
builds-toward:
- continuity-multivariable
- partial-derivatives
tags:
- limits
- multivariable
- epsilon-delta
stage: advanced
status: draft
---

# Limits of Multivariable Functions

## Core Idea
We say lim_{(x,y)→(a,b)} f(x, y) = L if for every ε > 0 there exists δ > 0 such that |f(x, y) − L| < ε whenever 0 < √((x−a)² + (y−b)²) < δ. The limit must be the same along all paths approaching (a, b).

## Explainer

You already know the ε-δ definition of a single-variable limit: lim_{x→a} f(x) = L means that as x gets arbitrarily close to a (within δ), f(x) gets arbitrarily close to L (within ε). In one dimension, "close to a" means within an interval (a − δ, a + δ), and there are only two directions to approach from: left and right. The multivariable definition keeps the ε-δ structure but radically expands what "close to (a, b)" means.

In ℝ², "within distance δ of the point (a, b)" is a **disk** of radius δ centered at (a, b) — all points (x, y) satisfying √((x−a)² + (y−b)²) < δ. Notice the distance formula uses the vector norm you have already studied. The limit lim_{(x,y)→(a,b)} f(x,y) = L holds if and only if, for every ε > 0, there is a δ > 0 such that every point in this punctured disk maps to within ε of L. The word "every" is load-bearing: there are infinitely many directions from which (x, y) can approach (a, b), and the limit must equal L along all of them simultaneously.

This "all paths" requirement is both the central difficulty and the key tool. To **prove** a limit exists, you must show the ε-δ condition holds for all approach paths — typically by bounding |f(x,y) − L| using algebraic estimates and the distance to (a, b). To **disprove** a limit exists (or prove a limit does not exist), you only need to find **two paths** that give different limiting values. For example, if approaching along y = 0 gives lim = 0 but approaching along y = x gives lim = 1/2, the limit does not exist at the origin — regardless of what happens along any other path.

A standard technique: approach along y = mx (lines through the origin) or along y = x² (parabolas) to test for path-dependence. If the limit along y = mx depends on the slope m, the overall limit fails to exist. If all lines give the same value L, the limit *might* equal L — but you must still check curved paths before concluding. The only route to a complete proof of existence is an ε-δ argument, usually by factoring |f(x,y) − L| and bounding it by a constant times the distance to (a, b), which can then be made small by choosing δ small.
