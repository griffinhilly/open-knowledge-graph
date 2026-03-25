---
id: graphing-linear-equations
title: Graphing Linear Equations
domain: mathematics
course: algebra-1
prerequisites:
- id: slope-intercept-form
  type: hard
- id: standard-form-linear-equations
  type: soft
- id: coordinate-plane-intro
  type: hard
- id: coordinate-plane-all-four-quadrants
  type: soft
- id: function-tables
  type: soft
- id: proportional-relationships
  type: soft
- id: parallel-and-perpendicular-slopes
  type: soft
builds-toward:
- systems-graphing
- graphing-quadratics
tags:
- graphing
- linear-equations
- coordinate-plane
- slope
stage: abstract-reasoning
status: validated
---
# Graphing Linear Equations

## Core Idea
Graphing a linear equation means plotting its line on the coordinate plane. There are three main methods: (1) from slope-intercept form (y = mx + b), plot the y-intercept and use the slope; (2) from standard form (Ax + By = C), find the x- and y-intercepts and connect them; (3) make a table of values and plot points. Every linear equation in two variables produces a straight line, and every straight line corresponds to a linear equation. Graphing makes abstract equations visual and is the basis for understanding systems of equations and linear models.

## How It's Best Learned
Practice all three methods and discuss when each is most efficient. Emphasize that two points determine a line, but three points provide a check. Include horizontal lines (y = k) and vertical lines (x = k) as special cases. Use graphing to verify algebraic work and to estimate solutions to equations.

## Common Misconceptions
- Plotting the slope as a single point instead of as a rise/run movement.
- Graphing y = 3 as a vertical line (it is horizontal) or x = 3 as horizontal (it is vertical).
- Only plotting two points from a table without checking alignment with a third point.

## Questions

```yaml
- question: "What is the y-intercept of the line y = 3x − 4?"
  type: multiple-choice
  options: ["3", "−4", "4", "−3"]
  answer: 1
  explanation: "In slope-intercept form y = mx + b, the y-intercept is b — the constant term. Here b = −4, so the line crosses the y-axis at (0, −4). The value 3 is the slope, not the intercept. A common error is reading the coefficient of x as the intercept or dropping the negative sign."

- question: "The graph of the equation y = 5 is a vertical line."
  type: true-false
  answer: false
  explanation: "y = 5 means 'y is always 5, no matter what x is.' Every point on this line has y-coordinate 5, so the line runs horizontally across the plane. Vertical lines are described by x = constant (e.g., x = 5). Confusing horizontal and vertical is one of the most common graphing errors."

- question: "You are graphing y = (3/4)x + 2 using the slope-intercept method. After plotting the y-intercept, describe exactly how you would use the slope to find the next point."
  type: short-answer
  answer: "Plot the y-intercept at (0, 2). Then move right 4 units (run) and up 3 units (rise) to land on the next point at (4, 5)."
  explanation: "Slope = rise/run = 3/4. Starting at the y-intercept (0, 2), move in the direction that rise/run describes: 3 up and 4 to the right. This gives (0+4, 2+3) = (4, 5). Many students try to plot slope as a single coordinate rather than as a directed movement."
```

## Explainer

Graphing a linear equation translates an algebraic rule into a picture. Every linear equation in x and y produces a straight line, and every straight line on a coordinate plane corresponds to a linear equation. The graph and the equation carry the same information — just in different forms.

The most efficient method for most equations is **slope-intercept form**: y = mx + b. You already know that b is the y-intercept (where the line crosses the y-axis) and m is the slope (rise over run). The graphing procedure follows directly: plot (0, b) as your starting point, then use the slope to step to a second point. If m = 2/3, move right 3 and up 2. Connect the two points and extend in both directions. Two points determine a line — but always plot a third as a check.

Some equations arrive in **standard form** (Ax + By = C). The cleanest approach here is to find the two intercepts. Set x = 0 to find the y-intercept; set y = 0 to find the x-intercept. Plot both points and connect them. This avoids rearranging the equation, though you should recognize both forms.

Two special cases trip up many students. The equation y = 5 has no x term, which means x can be anything while y is always 5 — a **horizontal** line at height 5. The equation x = 3 constrains only x, making y free — a **vertical** line at x = 3. The rule is: "y = constant → horizontal; x = constant → vertical."

Finally, a **table of values** works for any equation and is a good fallback. Pick three or four x-values, compute the corresponding y-values, and plot the points. If they fall on a straight line you have it right; if not, one of your calculations has an error. Graphing is also a great way to check algebraic solutions — if you think the answer to a system of equations is (2, 1), plot both lines and verify they actually cross at that point.
