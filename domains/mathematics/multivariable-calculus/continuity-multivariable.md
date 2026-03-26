---
id: continuity-multivariable
title: Continuity in Multiple Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-limits
  type: hard
- id: epsilon-delta-continuity
  type: soft
builds-toward:
- partial-derivatives
- differentiability-multivariable
tags:
- continuity
- limits
stage: formal-systems
status: validated
---

# Continuity in Multiple Variables

## Core Idea
Function f(x, y) is continuous at (a, b) if lim_{(x,y)→(a,b)} f(x, y) = f(a, b). In multiple variables, the limit must be the same approaching from all directions, making the concept richer than in one dimension.

## Questions

```yaml
- question: "For f(x, y) = xy/(x² + y²) with f(0, 0) = 0: both iterated limits — first fixing x = 0 then taking y → 0, and vice versa — equal 0. Does this prove f is continuous at the origin?"
  type: multiple-choice
  options:
    - "Yes — if both iterated limits equal the function value, the function is continuous at that point."
    - "No — continuity requires the joint limit lim_{(x,y)→(0,0)} to exist and equal f(0,0), and iterated limits don't guarantee the joint limit exists."
    - "Yes — checking along the coordinate axes gives sufficient coverage of all directions approaching the origin."
    - "No — continuity in multiple variables requires checking infinitely many paths, which is impossible to verify in practice."
  answer: 1
  explanation: "This is the classic counterexample. Along any line y = mx, the limit is m/(1 + m²), which depends on m — so different lines give different limits and the joint limit does not exist. f is therefore not continuous at the origin, despite both iterated limits equaling 0. Option A is the central misconception: passing both axis-direction limits is necessary but not sufficient. Option D is also wrong — finding a single path that gives a different value is sufficient to disprove the limit's existence."

- question: "A student wants to prove that f(x, y) = sin(x² + y²)/(x² + y²), defined as 1 at (0, 0), is continuous at the origin. Which approach is valid?"
  type: multiple-choice
  options:
    - "Show that the limit as x → 0 (holding y = 0) equals 1, and the limit as y → 0 (holding x = 0) equals 1."
    - "Substitute x = r cos θ, y = r sin θ so x² + y² = r², then show the limit as r → 0 equals 1 regardless of θ."
    - "Argue by symmetry: the function depends only on x² + y², so all directions are equivalent, meaning one direction suffices."
    - "Graph the function near the origin and observe no visible discontinuity."
  answer: 1
  explanation: "Converting to polar coordinates is the standard strategy for this class of problem. Since x² + y² = r², the function becomes sin(r²)/r² → 1 as r → 0, and this limit is independent of θ. Checking all directions simultaneously is what polar coordinates achieve. Option A only checks two specific paths (the axes), which is insufficient — a different path might give a different limit. Option C sounds similar to option B but is informal and would not constitute a proof."

- question: "If both partial derivatives ∂f/∂x and ∂f/∂y exist at a point (a, b), the function f should be continuous there."
  type: true-false
  answer: false
  explanation: "This is one of the most surprising results in multivariable calculus. Partial derivatives measure behavior only along the coordinate axes — they say nothing about approaching along other directions. A function can have both partial derivatives at a point while being discontinuous there. For example, f(x, y) = xy/(x² + y²) has both partial derivatives equal to 0 at the origin, yet is discontinuous there. Continuity (and later, full differentiability) requires control over all paths, not just the axial ones."

- question: "Checking that lim_{(x,y)→(a,b)} f(x, y) equals f(a, b) along most straight line through (a, b) is sufficient to prove continuity at that point."
  type: true-false
  answer: false
  explanation: "Straight lines through a point don't cover all possible approach paths — curved paths like parabolas y = cx² are not captured. The classic counterexample is f(x, y) = x²y/(x⁴ + y²): along every line y = mx through the origin, the limit is 0, but along the parabola y = x², the limit is 1/2. So the joint limit does not exist and f is discontinuous at the origin, despite passing every straight-line test. Disproving continuity requires only one bad path; proving it requires the ε-δ definition or a technique (like polar coordinates) that controls all paths simultaneously."

- question: "Why does the concept of continuity become richer — and harder to verify — in multiple variables compared to single-variable calculus, and what is the consequence for how we must test it?"
  type: short-answer
  answer: "In single-variable calculus, a point has only two approach directions (left and right), so checking both suffices. In multiple variables, a point can be approached along infinitely many paths — every line, parabola, spiral, etc. — and the limit must be the same along all of them. This means checking any finite set of paths (such as the coordinate axes) can never prove continuity; it can only disprove it by exhibiting a path that gives a different value. Proving continuity usually requires the ε-δ definition or a substitution (like polar coordinates) that controls all directions simultaneously."
  explanation: "The core insight is that 'infinitely many paths' requires fundamentally different proof strategies. The existence of partial derivatives — which only tests the coordinate axes — is particularly insufficient. This gap between partial derivative existence and continuity motivates the stronger concept of differentiability, which requires a linear approximation to hold in all directions."
```

## Explainer

In single-variable calculus, continuity at a point means the limit equals the function value — and a limit in ℝ can only be approached from two directions (left and right). In multiple variables, a point like (a, b) in ℝ² can be approached along infinitely many paths: along the x-axis, along the y-axis, along any line y = mx, along parabolas y = cx², along spirals. From your study of multivariable limits, you know that the limit lim_{(x,y)→(a,b)} f(x,y) exists only if *all* these paths give the same value. **Continuity** builds directly on this: f is continuous at (a, b) if the limit exists, equals f(a, b), and f(a, b) is defined.

The richer path structure creates failure modes that don't exist in one dimension. The classic example is f(x, y) = xy/(x² + y²) at the origin (with f(0,0) = 0). Along any line y = mx, the limit as (x, y) → (0, 0) is mx²/(x²(1 + m²)) = m/(1 + m²) — which depends on m. Different lines give different limits, so the limit doesn't exist and f is not continuous at the origin. Yet both iterated limits lim_{x→0} lim_{y→0} f and lim_{y→0} lim_{x→0} f equal 0. This shows that checking continuity by fixing one variable at a time is insufficient — the joint limit is the true test.

Geometrically, continuity of f(x, y) means the surface z = f(x, y) has no holes or jumps — it is a connected surface without tears. The ε-δ definition transfers from single-variable calculus: for every ε > 0 there exists δ > 0 such that whenever ||(x, y) − (a, b)|| < δ, we have |f(x, y) − f(a, b)| < ε. Here the distance is the Euclidean distance in ℝ², capturing all directions simultaneously.

Continuity in multiple variables has the same stability properties you learned in one dimension: sums, products, and compositions of continuous functions are continuous, and quotients are continuous where the denominator is nonzero. Polynomials in x and y are continuous everywhere; rational functions are continuous on their domain. Continuity is the prerequisite for differentiability: just as in one variable, a function must be continuous at a point to be differentiable there. The converse fails sharply — partial derivatives can exist at a point even if the function is discontinuous there — which is why the stronger condition of **differentiability** will require more than just the existence of partial derivatives.
