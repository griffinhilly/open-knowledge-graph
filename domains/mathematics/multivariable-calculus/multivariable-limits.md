---
id: multivariable-limits
title: Limits and Continuity in Multiple Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: functions-of-several-variables
  type: hard
- id: limit-laws
  type: hard
- id: continuity-definition
  type: hard
builds-toward:
- partial-derivatives
tags:
- limits
- continuity
- multivariable
- epsilon-delta
stage: formal-systems
status: validated
---

# Limits and Continuity in Multiple Variables

## Core Idea
The limit lim_{(x,y)→(a,b)} f(x, y) = L means f(x, y) approaches L as (x, y) approaches (a, b) along every possible path. This is fundamentally harder than single-variable limits: one-variable limits require checking only two directions (left and right), but in ℝ² there are infinitely many paths of approach. A function is continuous at (a, b) if the limit equals f(a, b). Showing a limit does not exist is typically done by finding two paths that give different limiting values.

## How It's Best Learned
Emphasize the path-dependence issue with a concrete example, such as f(x,y) = xy/(x²+y²) near the origin. Show that different approach paths (y=0, y=x, y=x²) give different limits. Then show how the squeeze theorem can establish that a limit does exist. The contrast between existence proofs and non-existence proofs builds the key skill.

## Common Misconceptions
- It is NOT sufficient to check finitely many paths to prove a limit exists; existence proofs require general arguments (squeeze theorem, delta-epsilon).
- Showing the limit along y=mx is 0 for all slopes m does not prove the limit is 0 — it might still fail along y=x².
- A function can be discontinuous at a point even if it is defined there.

## Questions

```yaml
- question: "You check that lim_{(x,y)→(0,0)} f(x,y) = 0 along every straight-line path y = mx. What can you conclude?"
  type: multiple-choice
  options:
    - "The limit is 0 — checking all linear paths is sufficient to prove a multivariable limit"
    - "Nothing definitive about the limit — you still need to check curved paths or use a general argument"
    - "The limit does not exist — you must also check the path x = 0 separately"
    - "The function is continuous at (0,0) — straight-line limits matching implies continuity"
  answer: 1
  explanation: "This is the central trap in multivariable limits. Verifying the limit along all lines y = mx (including the special cases x = 0 and y = 0) is NOT sufficient to prove the limit exists. A classic counterexample is f(x,y) = x²y/(x⁴+y²): the limit along every line y = mx is 0, but along y = x², f(x,x²) = x²·x²/(x⁴+x⁴) = 1/2. So the limit is 0 on all lines but 1/2 on a parabola — the limit does not exist. Only a general argument (squeeze theorem or epsilon-delta) can prove existence."

- question: "For f(x,y) = xy/(x²+y²), you evaluate the limit along y=0 (getting 0) and along y=x (getting 1/2). What is the correct conclusion?"
  type: multiple-choice
  options:
    - "The limit is 1/4, the average of the two path limits"
    - "The limit does not exist, because two paths give different values"
    - "More paths must be checked before concluding anything"
    - "The limit is 0 because most paths give 0"
  answer: 1
  explanation: "If two different paths of approach to a point give different limiting values, the limit does not exist — period. The limit requires every path to give the same value L. Finding even one pair of paths with different limits is a complete proof of non-existence. No averaging, no majority vote — the two-path test is definitive for showing non-existence. This is the go-to strategy: find a path giving one value, find another giving a different value, done."

- question: "To prove that a multivariable limit exists and equals L, it is sufficient to verify that f(x,y) → L along most straight line through (a,b)."
  type: true-false
  answer: false
  explanation: "Straight-line paths are only a small subset of the infinitely many paths approaching (a,b). As the counterexample f(x,y) = x²y/(x⁴+y²) shows, a function can equal 0 on every line through the origin yet equal 1/2 along the parabola y=x². Existence requires the function to converge to L along every path simultaneously — curves, spirals, and all. Only general arguments like the squeeze theorem or epsilon-delta proofs can establish this."

- question: "Finding two paths of approach to a point that give different limit values is sufficient to prove the limit does not exist."
  type: true-false
  answer: true
  explanation: "By definition, a limit exists only if the function approaches the same value along every path. If even one pair of paths gives different values, the function is approaching different numbers depending on direction — so a single limiting value cannot exist. The two-path test is a complete proof of non-existence, not just evidence. It is the most practical non-existence strategy because it only requires computing two specific limits."

- question: "Why can't you prove a multivariable limit exists by checking finitely many paths, even if you check infinitely many straight lines?"
  type: short-answer
  answer: "A limit at (a,b) requires convergence to the same value along every possible path — including curves like y=x², y=x³, spirals, and paths that approach (a,b) in any manner. Straight lines form only a one-parameter family; there are infinitely many curved paths not covered by them. A function can be engineered to equal 0 on all lines yet equal 1/2 on a specific parabola. Proving existence requires a general bound on |f(x,y) - L| that holds simultaneously for all approach directions, typically achieved with the squeeze theorem or an epsilon-delta argument using r = √(x²+y²)."
  explanation: "The intuition from single-variable calculus — where left and right limits suffice — breaks down in higher dimensions because the 'directions' are no longer just two. The space of paths to a point in ℝ² is genuinely infinite-dimensional, and any finite or parametric family of special paths leaves infinitely many others unchecked."
```

## Explainer

In single-variable calculus, you defined lim_{x→a} f(x) = L by demanding that f(x) get arbitrarily close to L as x approaches a. The catch was simple: x can only approach a from the left or the right, so checking two directions was enough to confirm or refute a limit. In two variables, a point (a, b) in the plane is surrounded by infinitely many paths of approach — straight lines at every angle, parabolas, spirals, and more. A **multivariable limit** requires the function to converge to the same value L along every single one of these paths simultaneously.

This path-dependence is what makes multivariable limits genuinely harder. Consider f(x, y) = xy/(x² + y²) near the origin. Along the x-axis (y = 0), f = 0 for all x ≠ 0, so the limit from this path is 0. Along y = x, f = x²/(2x²) = 1/2 for all x ≠ 0, so the limit from this path is 1/2. Two paths give two different values, so the limit does not exist. This two-path test is the go-to strategy for showing a limit **fails to exist**: find two paths to (a, b) along which the function values approach different numbers.

But the two-path test cannot prove a limit exists. Even if the limit is 0 along every line y = mx through the origin, it might still fail along y = x². The path y = x² through the origin gives f(x, x²) = x · x²/(x² + x⁴) = x³/(x²(1 + x²)) = x/(1 + x²) → 0, so that path also gives 0 for this example — but this illustrates the need for caution, not a shortcut. To prove a limit exists, you need a genuine argument, typically the **squeeze theorem**: bound |f(x, y) − L| between 0 and a function of r = √(x² + y²) that goes to 0, exploiting the fact that any approach to (a, b) drives r → 0.

**Continuity** at (a, b) means the limit exists, equals f(a, b), and f is defined there — all three conditions simultaneously. For most elementary formulas (polynomials, rational functions away from their zeros, compositions of continuous functions), continuity holds everywhere the function is defined. The important exception is piecewise-defined functions, especially those with a special value assigned at a single point like the origin, where you must check whether the limit of the formula matches the assigned value. These continuity checks become essential prerequisites for partial derivatives, since differentiability requires the function to be well-behaved near a point in all directions.
