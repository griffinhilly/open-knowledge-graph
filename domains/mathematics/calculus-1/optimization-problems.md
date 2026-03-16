---
id: optimization-problems
title: Optimization Problems
domain: mathematics
course: calculus-1
prerequisites:
- id: first-derivative-test
  type: hard
- id: second-derivative-test
  type: soft
- id: curve-sketching
  type: soft
- id: related-rates
  type: soft
builds-toward:
- work-as-integral
tags:
- derivatives
- applications
- optimization
- word-problems
stage: formal-systems
status: validated
---
# Optimization Problems

## Core Idea
Optimization uses derivatives to find the maximum or minimum value of a quantity subject to constraints. The process involves translating a word problem into a function of one variable (using constraints to eliminate other variables), finding critical points, and verifying that the critical point gives the desired extremum. Applications include maximizing area, minimizing cost, maximizing volume, and optimizing distances.

## How It's Best Learned
Follow a systematic process: draw a diagram, identify variables, write the objective function and constraint, reduce to one variable, differentiate, find critical points, verify with first or second derivative test, check endpoints if on a closed interval. Work many varied problems.

## Common Misconceptions
- Forgetting to check endpoints of the domain (the absolute max/min may occur at an endpoint, not a critical point).
- Setting up the wrong objective function or misusing the constraint.
- Not verifying that a critical point is actually a maximum when a maximum is sought (or a minimum when a minimum is sought).

## Questions

```yaml
- question: "A farmer wants to maximize the area of a rectangular pen using 100 meters of fencing. After differentiating and finding the critical point x = 25, what must you still do before concluding this is the maximum?"
  type: multiple-choice
  options:
    - "Accept x = 25 as the maximum since critical points always give maxima"
    - "Confirm with the second derivative test (or first derivative test) that it is a local max, and compare with endpoint values if the domain is closed"
    - "Check that x = 25 is in the domain, but endpoints never need checking in optimization"
    - "Differentiate the constraint equation instead of the objective function"
  answer: 1
  explanation: "Critical points are candidates for extrema, not guarantees. For a closed domain (e.g., 0 ≤ x ≤ 50 here), you must compare the critical point value with values at both endpoints — the absolute maximum may occur at a boundary. The second derivative test confirms whether the critical point is a local max or min."

- question: "Once you find a critical point of your objective function and the problem asks for a maximum, you can be certain the critical point gives the maximum without further verification."
  type: true-false
  answer: false
  explanation: "Critical points include local maxima, local minima, and saddle points. The problem asking for a maximum does not guarantee the critical point delivers one — you must verify with the first or second derivative test. On a closed domain you also need to compare with endpoint values, since the absolute maximum may occur at the boundary rather than at the critical point."

- question: "Why must you reduce the objective function to one variable before differentiating in an optimization problem?"
  type: short-answer
  answer: "Derivatives only eliminate ambiguity for single-variable functions. The constraint equation relates the variables, so substituting it eliminates all but one, producing a function whose critical points can be found by setting the derivative to zero."
  explanation: "Setting f'(x) = 0 is only meaningful for functions of one variable. When an optimization problem involves two quantities (say area in terms of length and width), the constraint (like a fixed perimeter) provides a relationship between them. Substituting collapses the two-variable relationship into a single-variable function. Without this step you would need multivariable calculus."
```

## Explainer

When you studied derivatives, you learned that f′(x) = 0 at local maxima and minima. Optimization problems are the payoff: they ask you to use this fact to find the largest area, lowest cost, fastest time, or some other quantity in a real situation. The challenge is that real problems don't hand you a ready-made function — you have to build it from a description.

The process is systematic and non-negotiable: (1) draw a diagram and label variables, (2) identify the **objective function** (what you're maximizing or minimizing) and the **constraint** (a restriction relating your variables), (3) use the constraint to eliminate all but one variable, (4) differentiate and find critical points, (5) verify the type of extremum with a derivative test, and (6) check endpoints if the domain is bounded. Steps 3–6 are pure calculus; steps 1–2 are translation from words to algebra, and that's where most effort is required.

Step 3 is where students most often get stuck. Suppose you want to maximize the area A = xy of a rectangle with fixed perimeter 2x + 2y = 100. You have two variables, but the constraint gives you y = 50 − x. Substituting turns A = xy into A(x) = x(50 − x) = 50x − x², a function of one variable. Now A′(x) = 50 − 2x = 0 gives x = 25, and so y = 25 (a square maximizes area for fixed perimeter).

A critical misconception is thinking that finding a critical point means you're done. You still need to verify: is this a maximum or a minimum? A″(25) = −2 < 0 confirms a local maximum by the second derivative test. And if the domain is a closed interval — here 0 ≤ x ≤ 50, since side lengths must be non-negative — you must also compare the critical point value with endpoint values: A(0) = 0, A(25) = 625, A(50) = 0. The maximum is indeed 625 at the critical point, but this comparison is mandatory, not optional.

The variety of optimization problems can feel overwhelming — area, volume, cost, distance — but the structure is always the same. Every problem has one thing to optimize and at least one constraint. Your job is to translate the words into algebra, reduce to one variable, and apply the derivative machinery. Once you see that pattern, the problems become variations on a theme rather than separate puzzles.
