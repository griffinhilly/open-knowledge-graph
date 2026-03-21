---
id: point-slope-form
title: Point-Slope Form
domain: mathematics
course: algebra-1
prerequisites:
  - id: slope-concept
    type: hard
  - id: slope-intercept-form
    type: soft
builds-toward:
  - writing-linear-equations
  - parallel-and-perpendicular-slopes
tags: [point-slope, linear-equations, slope, writing-equations]
stage: abstract-reasoning
status: validated
---

# Point-Slope Form

## Core Idea
Point-slope form is y − y₁ = m(x − x₁), where m is the slope and (x₁, y₁) is any known point on the line. This form is most useful when you know the slope and a point (or two points, from which you compute the slope). It comes directly from the slope definition: m = (y − y₁)/(x − x₁), rearranged. Point-slope form is often the fastest way to write a linear equation, and it converts easily to slope-intercept form by distributing and solving for y. It also appears in calculus as the basis for linear approximation.

## How It's Best Learned
Derive it from the slope formula so students see it is not an arbitrary form but a rearrangement. Practice writing equations given a slope and a point, then given two points (find slope first, then use either point). Convert to slope-intercept form and verify both forms produce the same graph. Emphasize that either point can serve as (x₁, y₁) — the result is the same line.

## Common Misconceptions
- Getting the signs wrong: writing y − 3 = m(x − (−2)) as y − 3 = m(x − 2) instead of y − 3 = m(x + 2).
- Thinking you must always use the "first" point listed — either point works.
- Not converting to slope-intercept form when asked (stopping at point-slope form).

## Questions

```yaml
- question: "A line passes through the point (−3, 4) with slope 2. Which equation correctly represents this line in point-slope form?"
  type: multiple-choice
  options:
    - "y − 4 = 2(x − 3)"
    - "y − 4 = 2(x + 3)"
    - "y + 4 = 2(x + 3)"
    - "y − 4 = 2x − 3"
  answer: 1
  explanation: "The form is y − y₁ = m(x − x₁). With y₁ = 4, m = 2, and x₁ = −3, substituting literally gives y − 4 = 2(x − (−3)), which simplifies to y − 4 = 2(x + 3). Option A makes the classic sign error: it writes x − 3 instead of x + 3, dropping the double negative. The formula demands 'x minus x₁' — subtracting a negative x₁ produces addition."

- question: "A line has slope 3 and passes through the point (2, 7). After converting to slope-intercept form, what is the y-intercept?"
  type: multiple-choice
  options:
    - "1"
    - "13"
    - "−1"
    - "7"
  answer: 0
  explanation: "Starting from point-slope form: y − 7 = 3(x − 2). Distribute: y − 7 = 3x − 6. Add 7: y = 3x + 1. The y-intercept is 1. Option D (7) is a common error — students forget to distribute the slope and incorrectly treat the y₁ value as the y-intercept. Option B (13) comes from treating the point as (−2, 7) and adding rather than subtracting."

- question: "When writing a line's equation in point-slope form using two given points, it doesn't matter which point you use as (x₁, y₁) — both produce the same line."
  type: true-false
  answer: true
  explanation: "Both points lie on the same line, so plugging either one into y − y₁ = m(x − x₁) produces a different-looking equation that describes the same geometric object. Distributing and simplifying both equations to slope-intercept form yields identical results. Students sometimes believe they must use the 'first' point listed, but the choice is free."

- question: "The equation y − 3 = 4(x + 2) means the line passes through the point (2, 3)."
  type: true-false
  answer: false
  explanation: "The form is y − y₁ = m(x − x₁), so x₁ is the value being subtracted from x. Since the equation shows (x + 2), that equals (x − (−2)), meaning x₁ = −2, not 2. The line passes through (−2, 3). This is the sign trap: when the x-coordinate is negative, subtracting it produces addition, which students misread as a positive coordinate."

- question: "Where does point-slope form come from, and what two pieces of information do you need to write a linear equation using it?"
  type: short-answer
  answer: "Point-slope form comes directly from the slope definition: m = (y − y₁)/(x − x₁). Multiplying both sides by (x − x₁) gives y − y₁ = m(x − x₁). You need the slope m and any one specific point (x₁, y₁) on the line. If two points are given instead, compute the slope first, then use either point."
  explanation: "Recognizing point-slope form as a rearrangement of the slope definition — not an arbitrary formula — makes it easier to reconstruct and apply correctly. It also reveals why the signs matter: each variable in the formula is subtracted from its corresponding point coordinate, which is why negative coordinates produce addition in the equation."
```

## Explainer

You already know that **slope** measures the steepness of a line — the ratio of vertical change to horizontal change, rise over run. Point-slope form isn't a new idea layered on top of that; it's just the slope definition written in a slightly rearranged way. Starting from slope = (y − y₁)/(x − x₁), multiply both sides by (x − x₁) and you get **y − y₁ = m(x − x₁)**. That's the whole derivation. The form is worth naming because it's often the fastest route from information to equation.

The key insight is what information the form demands. To write an equation for a line, you need two pieces of data: the slope and one specific location. Point-slope form accepts exactly that. If you're given slope m = 3 and the point (2, 5), write immediately: y − 5 = 3(x − 2). No intermediate steps required. If you're given two points instead, compute the slope first (m = (y₂ − y₁)/(x₂ − x₁)), then use either point in the form — you'll get the same line either way.

Watch the signs carefully. The form is y − y₁, so if your point has a negative coordinate, subtraction of a negative becomes addition. For the point (−3, 4) with slope 2: y − 4 = 2(x − (−3)), which simplifies to y − 4 = 2(x + 3). A common error is to write x − 3 here, dropping the double negative. Reading the formula literally — "y minus y₁" and "x minus x₁" — and substituting the actual values of y₁ and x₁ prevents this mistake.

To convert to slope-intercept form, simply distribute m and solve for y. From y − 4 = 2(x + 3): distribute to get y − 4 = 2x + 6, then add 4 to both sides: y = 2x + 10. You'll also encounter point-slope form again in calculus, where the tangent line to a curve at a point (a, f(a)) has slope f′(a). The tangent line equation is y − f(a) = f′(a)(x − a) — exactly point-slope form, making this the algebraic template for local linear approximation.
