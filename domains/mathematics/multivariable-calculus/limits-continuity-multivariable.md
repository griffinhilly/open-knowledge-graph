---
id: limits-continuity-multivariable
title: Limits and Continuity in Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: functions-of-several-variables
  type: hard
- id: limit-definition-intuitive
  type: hard
builds-toward:
- partial-derivatives
- differentiability-multivariate
tags:
- limits
- continuity
- epsilon-delta
stage: formal-systems
status: validated
---

# Limits and Continuity in Multivariable Functions

## Core Idea
For a multivariable function, lim_(x,y)→(a,b) f(x,y) = L if for every ε > 0 there exists δ > 0 such that |f(x,y) − L| < ε whenever 0 < √[(x−a)² + (y−b)²] < δ. Continuity requires the limit to exist and equal f(a, b). Multiple paths to a point complicate convergence analysis.

## Questions

```yaml
- question: "A student checks the limit of f(x,y) as (x,y)→(0,0) along five different paths and finds the value L = 0 in every case. Can they conclude the limit equals 0?"
  type: multiple-choice
  options:
    - "Yes — checking five paths with consistent results is sufficient to establish the limit"
    - "No — infinitely many paths remain unchecked; only the epsilon-delta definition or a bounding argument can prove the limit exists"
    - "Yes — if the limit is the same along straight lines at all angles, it is the same along all paths"
    - "Yes, provided the paths include both straight lines and at least one curved path"
  answer: 1
  explanation: "The path test can only disprove a limit. Two paths giving different values proves no limit exists, but checking finitely many consistent paths can never prove the limit exists, because infinitely many paths remain unchecked. A function can give 0 along every straight line through the origin and still fail to have a limit (e.g., returning a different value along y = x²). Proof of existence requires the epsilon-delta framework or a bounding argument that covers all paths at once."

- question: "For f(x,y) = xy/(x² + y²), a student evaluates the limit at the origin along y = 0 and gets 0, then along y = x and gets 1/2. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "The limit is somewhere between 0 and 1/2; more paths are needed to pinpoint it"
    - "The limit does not exist at the origin, because two paths give different limiting values"
    - "The limit is 0, since y = 0 is the simpler and more natural path"
    - "The limit is 1/2, since the path y = x is more general than y = 0"
  answer: 1
  explanation: "If two paths to the same point give different limiting values, the limit does not exist — full stop. A limit requires the function to approach the same value L no matter how you approach the point. Different results along y = 0 and y = x prove that no single value L satisfies the definition for all paths. There is no 'most correct' path among conflicting ones."

- question: "In multivariable calculus, if two different paths to a point (a, b) yield different limiting values for f(x, y), then the limit of f at (a, b) does not exist."
  type: true-false
  answer: true
  explanation: "The limit lim_{(x,y)→(a,b)} f(x,y) = L must hold for every possible path of approach simultaneously. If even one path gives a different value, the limit does not exist. This is the path test: a sufficient condition for non-existence. It cannot prove existence, because you cannot check all paths by testing finitely many."

- question: "Showing that lim_{(x,y)→(0,0)} f(x,y) = 0 along nearly every straight line through the origin is sufficient to prove the limit equals 0."
  type: true-false
  answer: false
  explanation: "Straight lines form only a subset of the infinitely many paths to the origin. A function can give the limit 0 along every line y = mx yet approach a different value along a curved path such as y = x². The limit exists only if the function approaches the same value along every conceivable path — including parabolas, spirals, oscillating curves, and others."

- question: "Explain why the path test in multivariable limits can disprove the existence of a limit but cannot prove that a limit exists."
  type: short-answer
  answer: "The path test checks finitely many paths, but infinitely many paths approach any point. Disproving existence requires only one counterexample — a single path giving a different value. Proving existence requires showing the function approaches L along every path, which cannot be completed by checking examples. Proof requires the epsilon-delta definition or a bounding argument (such as polar coordinates) that covers all paths simultaneously."
  explanation: "This asymmetry is fundamental: existence claims require universal quantification (for all paths), so a proof must handle all cases at once. Non-existence claims require only one counterexample. The polar coordinate approach — setting x = r cosθ, y = r sinθ and showing the expression approaches L as r → 0 independently of θ — is the standard tool for proving existence, because r → 0 captures all paths simultaneously."
```

## Explainer

From single-variable limits, you know that lim_{x→a} f(x) = L means f(x) can be made arbitrarily close to L by taking x close enough to a — from either side. In one dimension, "from either side" covers all possible directions of approach. In two dimensions, the situation is fundamentally harder: there are infinitely many paths through (a, b) — lines at every angle, parabolas, spirals, spirals that spiral inward — and the limit lim_{(x,y)→(a,b)} f(x,y) = L must hold along every single one of them simultaneously.

This is the key new difficulty. If even one path to (a, b) gives a different limiting value, or no limit at all, then the two-variable limit does not exist. The **path test** exploits this: substitute y = mx (approach along straight lines of varying slope m) or y = x² (approach along a parabola) and check whether the result depends on the choice. For f(x,y) = xy/(x² + y²), the limit along y = 0 gives 0, but along y = x gives x²/(2x²) = 1/2. Because two paths give different values, no limit exists at the origin. The path test can efficiently disprove a limit's existence, but it can never prove existence — checking finitely many paths leaves infinitely many unchecked.

To prove a limit exists, you need the full epsilon-delta definition with the Euclidean distance r = √[(x−a)² + (y−b)²] replacing |x−a|. The strategy is to bound |f(x,y) − L| in terms of r and show the bound goes to zero. **Polar coordinates** (x = a + r cos θ, y = b + r sin θ) are often the cleanest tool near the origin: r → 0 corresponds to approaching along any path whatsoever, and if the expression in polar form tends to L independently of θ, the limit is established for all paths at once. The **squeeze theorem** applies in exactly the same way as in one dimension.

**Continuity** at (a, b) means three things hold simultaneously: f is defined there, the limit exists, and the limit equals f(a, b). Polynomials, exponentials, and trigonometric functions are continuous everywhere they are defined — for these, limit evaluation is just substitution. The interesting cases are rational functions where the denominator vanishes, and piecewise-defined functions where you must check whether the pieces agree at the boundary. Continuity is the foundational hypothesis for everything that follows: partial derivatives assume it, the chain rule requires it, and differentiability (which is stronger than continuity) implies it. Getting comfortable with the multi-path nature of limits is the essential step before any further calculus in higher dimensions.
