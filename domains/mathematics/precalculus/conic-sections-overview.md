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

## Explainer

You've studied function transformations and domain-and-range, so you know how shifting and stretching change the graph of an equation. Conic sections extend this toolkit to a wider family of curves — ones that include ovals, U-shapes, and X-shapes — all arising from a single geometric idea: slicing a double cone with a plane. The angle and position of the cut determines which conic you get: a circle, ellipse, parabola, or hyperbola.

Each conic has a **standard form** equation that reveals its structure. The **circle** with center (h, k) and radius r: (x−h)² + (y−k)² = r². The **ellipse**: (x−h)²/a² + (y−k)²/b² = 1 — the denominators differ, stretching one axis more than the other to produce an oval. The **parabola** y = a(x−h)² + k is familiar from quadratic functions, but conics also include horizontal parabolas x = a(y−k)² + h, which open left or right and are not functions. The **hyperbola** (x−h)²/a² − (y−k)²/b² = 1 has a subtraction instead of addition, producing two separate branches with **asymptotes** y = ±(b/a)(x−h). Notice the key distinction: ellipses use addition of two squared terms; hyperbolas use subtraction.

The **focus** is a special interior point (or pair of points) that appears in the geometric definition of each conic. Every point on an ellipse has the same sum of distances to the two foci — this property explains why planets travel in ellipses with the sun at one focus (Kepler's first law). Every point on a parabola is equidistant from the focus and a line called the **directrix** — satellite dishes and headlights are paraboloids because parallel signals all reflect through the focus. Hyperbolas appear in GPS systems where a receiver's position lies on a hyperbola defined by the time difference between two signals. Recognizing which conic you have from a general second-degree equation Ax² + Bxy + Cy² + Dx + Ey + F = 0 requires completing the square — a technique from your algebra background applied now to two variables at once.

A key concept to carry forward: conics illustrate that not every curve in the plane is a function. A full ellipse or hyperbola fails the vertical line test — one x value corresponds to two y values. This broadens your mental model of "curve" beyond "function graph." When you reach polar coordinates and parametric equations, conics become even easier to describe, and their unifying focus-directrix geometry connects them all under one elegant formula using **eccentricity** e: a circle has e = 0, an ellipse has 0 < e < 1, a parabola has e = 1, and a hyperbola has e > 1.
