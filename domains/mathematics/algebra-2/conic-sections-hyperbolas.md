---
id: conic-sections-hyperbolas
title: 'Conic Sections: Hyperbolas'
domain: mathematics
course: algebra-2
prerequisites:
- id: conic-sections-ellipses
  type: hard
- id: rational-functions-and-asymptotes
  type: soft
builds-toward:
- conic-sections-overview
tags:
- conics
- hyperbolas
- foci
- asymptotes
- transverse-axis
stage: abstract-reasoning
status: validated
---
# Conic Sections: Hyperbolas

## Core Idea
A hyperbola is the set of all points where the absolute difference of distances to two foci is constant. Standard forms: (x-h)^2/a^2 - (y-k)^2/b^2 = 1 (horizontal transverse axis) or (y-k)^2/a^2 - (x-h)^2/b^2 = 1 (vertical transverse axis). Unlike ellipses, c^2 = a^2 + b^2. The hyperbola has two branches and two asymptotes that guide the shape: y - k = +/-(b/a)(x - h) for horizontal, y - k = +/-(a/b)(x - h) for vertical.

## How It's Best Learned
Contrast with ellipses: sum of distances (ellipse) vs. difference of distances (hyperbola). Identify center, vertices (a units from center on the transverse axis), and foci (c units from center). Draw the "box" formed by a and b to find asymptotes. Graph by sketching asymptotes first, then drawing the two branches approaching them. Practice converting from general form.

## Common Misconceptions
- Confusing the c relationship: ellipses use c^2 = a^2 - b^2, hyperbolas use c^2 = a^2 + b^2.
- Getting asymptote slopes wrong (b/a for horizontal, a/b for vertical).
- Thinking a must always be greater than b (for hyperbolas, a is simply the denominator under the positive term).
- Drawing the branches crossing the asymptotes (they approach but never cross).

## Questions

```yaml
- question: "For the hyperbola x²/16 − y²/9 = 1, what is the distance from the center to each focus?"
  type: multiple-choice
  options:
    - "c = √(16 − 9) = √7 ≈ 2.65"
    - "c = √(16 + 9) = 5"
    - "c = √16 = 4"
    - "c = √9 = 3"
  answer: 1
  explanation: "For a hyperbola, c² = a² + b², so c = √(16 + 9) = √25 = 5. The most tempting wrong answer is √7, using the ellipse formula c² = a² − b². The distinction matters: for an ellipse, foci are inside the curve (c < a), so subtracting b² shrinks c; for a hyperbola, foci are outside the curve (c > a), so adding b² enlarges c. If you get c < a for a hyperbola, you have used the wrong formula."

- question: "Consider the hyperbola (y − 3)²/4 − (x + 1)²/25 = 1. A student claims a = 5 because 'a is always the larger denominator.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — a is always the larger denominator in all conic sections"
    - "For hyperbolas, a is the denominator under the positive term; here a² = 4 so a = 2, regardless of which is larger"
    - "The formula only applies to hyperbolas centered at the origin; this one is shifted"
    - "a and b switch definitions when the transverse axis is vertical"
  answer: 1
  explanation: "For hyperbolas, 'a' is defined as the denominator under the *positive* term and corresponds to the semi-transverse axis. In this equation the positive term is (y−3)²/4, so a² = 4 and a = 2. The value b² = 25 is larger, but that does not make b into a. This contrasts with ellipses, where a conventionally denotes the larger semi-axis. For hyperbolas, there is no requirement that a > b."

- question: "For any hyperbola, the foci are located farther from the center than the vertices."
  type: true-false
  answer: true
  explanation: "Vertices are a units from center; foci are c units from center. Since c² = a² + b² and b² > 0, we have c² > a², so c > a. The foci always lie beyond the vertices along the transverse axis. This is the opposite of ellipses, where c < a and foci lie between the center and the vertices — a useful contrast to remember."

- question: "The asymptotes of a hyperbola pass through the vertices of the curve."
  type: true-false
  answer: false
  explanation: "Asymptotes pass through the *center* of the hyperbola, not the vertices. The branches curve away from the vertices and approach the asymptotes only as they extend toward infinity — they never touch or cross the asymptotes at any point. At the vertices (the closest points on the branches to the center), the branches are actually farthest from the asymptotes. The 'box method' makes this clear: asymptotes are diagonals through the box's corners at (±a, ±b), while vertices sit on the sides of the box at (±a, 0) or (0, ±a)."

- question: "Why does a hyperbola produce two separate branches while an ellipse is a single closed curve? Connect the defining distance condition to the geometric difference."
  type: short-answer
  answer: "An ellipse is defined by a constant *sum* of distances: d₁ + d₂ = 2a. Since both distances are positive, any satisfying point lies in a bounded region pulling toward the oval between the foci. A hyperbola uses a constant *absolute difference*: |d₁ − d₂| = 2a. This condition can be satisfied in two distinct ways — d₁ − d₂ = 2a (points substantially closer to one focus, forming one branch) and d₂ − d₁ = 2a (points substantially closer to the other focus, forming the second branch). The absolute difference allows solutions on both sides of the two foci, producing two open outward-facing branches rather than one closed curve."
  explanation: "The algebraic switch from sum to absolute difference is the single change that produces the dramatic visual difference. The sum condition bounds points to a closed oval; the difference condition permits points anywhere that maintain the correct distance differential, which happens on two separate sides of the focal pair."
```

## Explainer

You learned that an **ellipse** is defined by a constant sum of distances to two foci: for any point on the ellipse, d₁ + d₂ = 2a. A **hyperbola** swaps sum for difference: |d₁ − d₂| = 2a, where a is the semi-transverse axis length. This single change — from sum to absolute difference — produces a dramatically different shape. Where an ellipse is a closed oval, a hyperbola splits into two separate **branches** opening away from each other. The two foci are now outside the curve rather than inside it, and the curve stretches outward toward infinity rather than closing back on itself.

The standard form (x−h)²/a² − (y−k)²/b² = 1 describes a hyperbola centered at (h, k) with a **horizontal transverse axis** — the two vertices are a units left and right of center, and the branches open left and right. Flip the subtraction to (y−k)²/a² − (x−h)²/b² = 1 and the transverse axis is vertical, with branches opening up and down. In either case, a is always the denominator under the **positive** term, regardless of whether a > b or not. The foci lie c units from center along the transverse axis, where c² = a² + b². Compare this to the ellipse formula c² = a² − b²: for ellipses the foci are inside (c < a), so subtracting b² shrinks c; for hyperbolas the foci are outside (c > a), so adding b² enlarges c.

The most distinctive feature of a hyperbola is its pair of **asymptotes** — lines the branches approach but never touch. The trick to finding them is to draw a rectangle: go a units from center along the transverse axis and b units perpendicular to it, forming a box. The asymptotes are the diagonals of that box, passing through the center. For a horizontal hyperbola, those slopes are ±b/a; for a vertical one, ±a/b. This "box method" also gives you a reliable graphing strategy: draw the box, draw the asymptotes through its corners, then sketch two branches curving away from center and hugging the asymptotes as they extend outward.

Your background in rational functions and asymptotes from the prerequisite makes the asymptotic behavior intuitive. As x gets very large in (x²/a²) − (y²/b²) = 1, solving for y gives y ≈ ±(b/a)x — the curve looks more and more like its asymptote lines at large distances. Near the vertices the branches curve away sharply; far from the center they appear almost straight. This interplay between the local behavior (curved branches near vertices) and global behavior (approaching straight lines at infinity) is exactly the pattern you studied in rational functions, now appearing geometrically as a conic section.
