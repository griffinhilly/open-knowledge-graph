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

## Questions

```yaml
- question: "You are testing whether lim_{(x,y)→(0,0)} f(x,y) exists. Approaching along y=0 gives a limiting value of 0; approaching along y=x gives a limiting value of 1/2. What can you conclude?"
  type: multiple-choice
  options:
    - "The limit is 0, since the simpler path (y=0) takes priority"
    - "The limit does not exist, because two paths give different values"
    - "You need to check more paths before drawing any conclusion"
    - "The limit is somewhere between 0 and 1/2, since both paths are valid"
  answer: 1
  explanation: "The defining property of a multivariable limit is that it must be the same along every path approaching the point. Finding even two paths that give different values is sufficient to prove the limit does not exist — no further checking is needed. This is the key asymmetry: disproving existence requires only two paths; proving existence requires an ε-δ argument valid for all paths simultaneously."

- question: "To rigorously prove that lim_{(x,y)→(a,b)} f(x,y) = L, which approach is sufficient?"
  type: multiple-choice
  options:
    - "Show that the limit equals L along all lines y = m(x−a) through (a,b)"
    - "Show the limit equals L along all lines through (a,b) and also along the parabolic path y = (x−a)²"
    - "Provide an ε-δ argument showing |f(x,y)−L| < ε for all (x,y) within distance δ of (a,b)"
    - "Show the iterated limits lim_{x→a} lim_{y→b} f and lim_{y→b} lim_{x→a} f are both equal to L"
  answer: 2
  explanation: "Only the ε-δ argument suffices because it must cover all paths simultaneously, including infinitely many curved paths not captured by linear or parabolic tests. Showing agreement along a finite collection of paths — no matter how many — never rules out a curved path that disagrees. The ε-δ formulation (every point in a punctured disk of radius δ maps within ε of L) is the only way to make 'all paths' mathematically precise."

- question: "In ℝ², there are infinitely many distinct paths along which (x,y) can approach a point (a,b)."
  type: true-false
  answer: true
  explanation: "Unlike the single-variable case, where only two directions exist (left and right), in ℝ² a point can be approached from any direction and along any continuous curve passing through it — including straight lines at every angle, parabolas, spirals, and so on. This infinite variety of approach paths is precisely what makes multivariable limits harder than single-variable limits, and why checking finitely many paths can never prove a limit exists."

- question: "If lim_{(x,y)→(0,0)} f(x,y) gives the same value L along every straight line through the origin, then the limit equals L."
  type: true-false
  answer: false
  explanation: "This is a classic trap. Agreement along all straight lines is necessary but not sufficient. Curved paths (e.g., y = x²) may still give a different value. A standard counterexample is f(x,y) = xy²/(x²+y⁴): along every line y=mx it approaches 0, but along the parabola x=y² it approaches 1/2. A complete proof requires either an ε-δ argument or confirming agreement along curved paths as well — and ultimately only ε-δ is conclusive."

- question: "Why is the 'all paths must agree' requirement the central difficulty of multivariable limits, and how does it differ fundamentally from the single-variable case?"
  type: short-answer
  answer: "In one dimension, a point a can only be approached from the left or right — there are just two directions. The single-variable limit exists when these two one-sided limits agree. In two (or more) dimensions, a point (a,b) can be approached along any continuous curve, of which there are uncountably many. The limit must equal L along every one of these paths simultaneously. This cannot be verified path by path; instead, an ε-δ argument must show that the entire punctured disk (all points within distance δ of (a,b), regardless of direction) maps within ε of L."
  explanation: "The geometric intuition is this: in 1D, 'approaching a' is like walking toward a door with only two walls — left and right. In 2D, 'approaching (a,b)' means coming from any point of the compass plus every curved trajectory. The ε-δ condition captures this by quantifying over an entire disk rather than just an interval."
```

## Explainer

You already know the ε-δ definition of a single-variable limit: lim_{x→a} f(x) = L means that as x gets arbitrarily close to a (within δ), f(x) gets arbitrarily close to L (within ε). In one dimension, "close to a" means within an interval (a − δ, a + δ), and there are only two directions to approach from: left and right. The multivariable definition keeps the ε-δ structure but radically expands what "close to (a, b)" means.

In ℝ², "within distance δ of the point (a, b)" is a **disk** of radius δ centered at (a, b) — all points (x, y) satisfying √((x−a)² + (y−b)²) < δ. Notice the distance formula uses the vector norm you have already studied. The limit lim_{(x,y)→(a,b)} f(x,y) = L holds if and only if, for every ε > 0, there is a δ > 0 such that every point in this punctured disk maps to within ε of L. The word "every" is load-bearing: there are infinitely many directions from which (x, y) can approach (a, b), and the limit must equal L along all of them simultaneously.

This "all paths" requirement is both the central difficulty and the key tool. To **prove** a limit exists, you must show the ε-δ condition holds for all approach paths — typically by bounding |f(x,y) − L| using algebraic estimates and the distance to (a, b). To **disprove** a limit exists (or prove a limit does not exist), you only need to find **two paths** that give different limiting values. For example, if approaching along y = 0 gives lim = 0 but approaching along y = x gives lim = 1/2, the limit does not exist at the origin — regardless of what happens along any other path.

A standard technique: approach along y = mx (lines through the origin) or along y = x² (parabolas) to test for path-dependence. If the limit along y = mx depends on the slope m, the overall limit fails to exist. If all lines give the same value L, the limit *might* equal L — but you must still check curved paths before concluding. The only route to a complete proof of existence is an ε-δ argument, usually by factoring |f(x,y) − L| and bounding it by a constant times the distance to (a, b), which can then be made small by choosing δ small.
