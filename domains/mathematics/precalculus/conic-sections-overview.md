---
id: conic-sections-overview
title: Conic Sections Overview
domain: mathematics
course: precalculus
prerequisites:
  - id: function-transformations
    type: soft
  - id: domain-and-range
    type: soft
builds-toward:
  - polar-graphs
  - parametric-equations-intro
tags: [conics, parabola, ellipse, hyperbola, circle]
stage: formal-systems
status: validated
---

# Conic Sections Overview

## Core Idea
Conic sections (circles, ellipses, parabolas, hyperbolas) are curves formed by intersecting a plane with a cone. Each has a standard equation form that reveals its key features: center, vertices, foci, axes, and asymptotes (for hyperbolas). Conics appear in planetary orbits, satellite dishes, bridges, and optics. They provide important examples of curves that are not functions (failing the vertical line test).

## How It's Best Learned
Study each conic type individually: standard form, key features, graphing procedure. Then compare and contrast. Practice completing the square to convert general second-degree equations to standard form. Connect to the focus-directrix definition that unifies all conics.

## Common Misconceptions
- Confusing ellipses and hyperbolas based on equation form (sum of squares vs. difference of squares).
- Forgetting to complete the square before identifying the conic.
- Assuming all conics are functions.

## Questions

```yaml
- question: "A student sees these two equations: (x−2)²/9 + (y+1)²/4 = 1 and (x−2)²/9 − (y+1)²/4 = 1. Which correctly identifies each conic?"
  type: multiple-choice
  options:
    - "Both are ellipses — both have the standard (x−h)²/a² form"
    - "The first is an ellipse; the second is a hyperbola — addition of squares gives an ellipse, subtraction gives a hyperbola"
    - "The first is a hyperbola; the second is an ellipse — the minus sign in the second means it opens outward"
    - "Both are hyperbolas — any equation with two squared terms separated by a constant is a hyperbola"
  answer: 1
  explanation: "The sign between the two squared terms is the definitive test. Addition of two positive squared terms equals a positive constant → ellipse (or circle if denominators are equal). Subtraction → hyperbola. Option C reverses this. Options A and D reflect the common confusion of ignoring the sign between terms."

- question: "A comet travels a path around the sun with eccentricity e = 1. What is the shape of its orbit?"
  type: multiple-choice
  options:
    - "Ellipse — all bound orbits are ellipses"
    - "Circle — e = 1 represents a perfect circle"
    - "Parabola — e = 1 is the boundary between bound and unbound orbits"
    - "Hyperbola — e > 0 means the orbit opens outward"
  answer: 2
  explanation: "Eccentricity unifies all conics: circle (e = 0), ellipse (0 < e < 1), parabola (e = 1), hyperbola (e > 1). A parabola is the knife-edge case between a closed orbit (ellipse) and an escape trajectory (hyperbola). The Sun sits at the focus of the parabola. Options A and B are wrong — circles require e = 0 and bound orbits require e < 1."

- question: "Most conic section can be expressed as a function of x — that is, it passes the vertical line test."
  type: true-false
  answer: false
  explanation: "A full ellipse or hyperbola fails the vertical line test: at any x value between the vertices, a vertical line intersects the curve at two points (one on the top half, one on the bottom). They are relations, not functions. Only a parabola opening left or right also fails as a function — and horizontal parabolas are conic sections too. Circles similarly fail. This is a key reason conics matter: they extend our study of curves beyond function graphs."

- question: "The asymptotes of a hyperbola (x−h)²/a² − (y−k)²/b² = 1 pass through the center (h, k) of the hyperbola."
  type: true-false
  answer: true
  explanation: "The asymptotes of this hyperbola are the lines y − k = ±(b/a)(x − h), which both pass through (h, k). They act as 'guides' that the branches of the hyperbola approach but never reach as x → ±∞. This is why the center is important even though no point of the hyperbola actually sits there — it's the intersection point of the asymptotes."

- question: "What is the geometric unifying principle behind all four conic sections, and how does the concept of eccentricity capture it?"
  type: short-answer
  answer: "All conics can be defined via a focus and directrix: a conic is the locus of points where the ratio of distance to focus to distance to directrix equals a constant e (the eccentricity). When e = 0, the curve closes into a circle; for 0 < e < 1, an ellipse; e = 1, a parabola; e > 1, a hyperbola. Alternatively, all four shapes arise from slicing a double cone at different angles — changing the tilt of the cutting plane transitions you between conics."
  explanation: "The focus-directrix definition reveals that circles, ellipses, parabolas, and hyperbolas are not four separate formulas but one geometric idea parameterized by eccentricity. This unification is essential for polar form of conics, which describes all four with a single compact equation r = ed/(1 − e cos θ). Understanding the underlying geometry is what allows you to recognize conics in physical applications — satellite dishes (paraboloids), planetary orbits (ellipses), and GPS signal geometry (hyperbolas)."
```

## Explainer

You've studied function transformations and domain-and-range, so you know how shifting and stretching change the graph of an equation. Conic sections extend this toolkit to a wider family of curves — ones that include ovals, U-shapes, and X-shapes — all arising from a single geometric idea: slicing a double cone with a plane. The angle and position of the cut determines which conic you get: a circle, ellipse, parabola, or hyperbola.

Each conic has a **standard form** equation that reveals its structure. The **circle** with center (h, k) and radius r: (x−h)² + (y−k)² = r². The **ellipse**: (x−h)²/a² + (y−k)²/b² = 1 — the denominators differ, stretching one axis more than the other to produce an oval. The **parabola** y = a(x−h)² + k is familiar from quadratic functions, but conics also include horizontal parabolas x = a(y−k)² + h, which open left or right and are not functions. The **hyperbola** (x−h)²/a² − (y−k)²/b² = 1 has a subtraction instead of addition, producing two separate branches with **asymptotes** y = ±(b/a)(x−h). Notice the key distinction: ellipses use addition of two squared terms; hyperbolas use subtraction.

The **focus** is a special interior point (or pair of points) that appears in the geometric definition of each conic. Every point on an ellipse has the same sum of distances to the two foci — this property explains why planets travel in ellipses with the sun at one focus (Kepler's first law). Every point on a parabola is equidistant from the focus and a line called the **directrix** — satellite dishes and headlights are paraboloids because parallel signals all reflect through the focus. Hyperbolas appear in GPS systems where a receiver's position lies on a hyperbola defined by the time difference between two signals. Recognizing which conic you have from a general second-degree equation Ax² + Bxy + Cy² + Dx + Ey + F = 0 requires completing the square — a technique from your algebra background applied now to two variables at once.

A key concept to carry forward: conics illustrate that not every curve in the plane is a function. A full ellipse or hyperbola fails the vertical line test — one x value corresponds to two y values. This broadens your mental model of "curve" beyond "function graph." When you reach polar coordinates and parametric equations, conics become even easier to describe, and their unifying focus-directrix geometry connects them all under one elegant formula using **eccentricity** e: a circle has e = 0, an ellipse has 0 < e < 1, a parabola has e = 1, and a hyperbola has e > 1.
