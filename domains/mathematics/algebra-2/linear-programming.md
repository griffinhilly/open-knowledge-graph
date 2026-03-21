---
id: linear-programming
title: Linear Programming
domain: mathematics
course: algebra-2
prerequisites:
- id: systems-of-inequalities
  type: soft
builds-toward: []
tags:
- optimization
- linear-programming
- constraints
- feasible-region
- objective-function
stage: formal-systems
status: validated
---
# Linear Programming

## Core Idea
Linear programming is a method for finding the maximum or minimum value of a linear objective function (such as profit = 3x + 5y) subject to a set of linear inequality constraints. The constraints define a feasible region — a polygon on the coordinate plane. The Corner Point Theorem guarantees that the optimal value occurs at one of the vertices of this feasible region, so the solution method is: graph the constraints, identify the vertices, evaluate the objective function at each vertex, and select the best one. Linear programming is widely used in business, logistics, manufacturing, and resource allocation.

## How It's Best Learned
Work through a complete example from start to finish: define variables, write constraints as inequalities, graph the feasible region, find corner points, and evaluate the objective function. Use a context students can relate to (maximizing profit from selling two products with limited resources). Emphasize why the Corner Point Theorem works by tracing the objective function's value across the region.

## Common Misconceptions
- Testing random points inside the feasible region instead of evaluating only the corner points.
- Forgetting implicit constraints like x >= 0 and y >= 0, which restrict the feasible region to the first quadrant.

## Questions

```yaml
- question: "A feasible region has corner points at (0, 4), (3, 2), and (6, 0). The objective function is P = 3x + 5y. A student argues that the optimal mix must be somewhere in the middle — not at an extreme corner — and evaluates P at the interior point (3, 2) only, concluding P = 19 is the maximum. What is the actual maximum value of P?"
  type: multiple-choice
  options:
    - "20 — at corner point (0, 4)"
    - "19 — the student's answer was correct"
    - "18 — at corner point (6, 0)"
    - "A higher value exists in the interior of the feasible region"
  answer: 0
  explanation: "P(0,4) = 0 + 20 = 20, P(3,2) = 9 + 10 = 19, P(6,0) = 18 + 0 = 18. The maximum is 20 at (0, 4). The Corner Point Theorem guarantees the optimum occurs at a vertex — never in the interior — because the objective function's level curves are straight lines that slide across the region until they exit at a corner. A point in the interior can always be improved by moving toward a boundary or corner."

- question: "Which action correctly applies the Corner Point Theorem when solving a linear programming problem?"
  type: multiple-choice
  options:
    - "Evaluate the objective function at many points inside the feasible region and find the largest"
    - "Evaluate the objective function at each vertex of the feasible region and compare"
    - "Find where the objective function equals zero and check nearby vertices"
    - "Evaluate the objective function along each boundary edge and average the results"
  answer: 1
  explanation: "The Corner Point Theorem states that the maximum (or minimum) of a linear objective function over a closed polygonal feasible region always occurs at one of the vertices. The correct procedure is: (1) find all corner points by solving pairs of intersecting boundary lines, (2) evaluate the objective at each, (3) pick the best. Sampling interior points or averaging edges is both inefficient and unreliable."

- question: "If a linear programming problem has a bounded feasible region, the Corner Point Theorem guarantees that the optimal value of the objective function occurs at one of the vertices."
  type: true-false
  answer: true
  explanation: "True. A bounded feasible region is a closed polygon. Because the objective function is linear, its level curves are parallel lines. As you translate these lines in the direction of improving the objective, the last point of the feasible region touched before the line exits is always a corner vertex. This is why the theorem holds — and it only requires the region to be closed and the objective to be linear."

- question: "A point in the interior of the feasible region can sometimes achieve a higher objective value than all corner points if the objective function has a steep slope."
  type: true-false
  answer: false
  explanation: "False. No interior point can beat every corner point for a linear objective. The Corner Point Theorem is unconditional for bounded feasible regions — it applies regardless of the slope or direction of the objective function. Interior points lie on level curves strictly between two boundary values; moving toward the boundary always keeps the option to improve. If the objective function is parallel to a boundary edge, the entire edge is optimal, but each endpoint of that edge is still a corner."

- question: "A student solves a linear programming problem by graphing the constraints, shading the feasible region, and then picking the point that 'looks like the best balance' near the middle of the region. Explain why this approach is structurally unreliable, and describe the correct procedure."
  type: short-answer
  answer: "The approach fails because the optimal value of a linear objective never lies in the interior of the feasible region — it always occurs at a corner vertex. 'Looking balanced' has nothing to do with maximizing a linear function. The correct procedure is: (1) graph all constraints to find the feasible region, (2) identify all corner points by solving the systems of equations formed at each intersection of boundary lines, (3) evaluate the objective function at every corner point, and (4) select the corner with the best value. This is the Corner Point Theorem and it is guaranteed by the geometry of linear functions over polygons."
  explanation: "The misconception stems from confusing optimization with 'balance.' A linear objective function values one unit of x and one unit of y at fixed rates regardless of where in the region you are. Moving toward a corner that weights the more valuable variable more heavily always improves the objective. Only when the objective is parallel to a boundary edge does an entire edge (including two corners) tie for optimal."
```

## Explainer

From your work with systems of inequalities, you know how to graph the region satisfying multiple linear constraints simultaneously — each inequality cuts away part of the plane, and the overlapping region that satisfies all constraints is the **feasible region**. Linear programming adds one more ingredient: a goal. Among all the points in that region, which one makes some quantity (profit, cost, time) as large or as small as possible?

Set up the problem with two decision variables. Say a bakery can make x loaves of bread and y cakes, each requiring different amounts of time and ingredients. The constraints become inequalities: maybe 2x + 3y ≤ 12 (hours of oven time), x + y ≤ 5 (pounds of flour), plus x ≥ 0 and y ≥ 0 (you can't make negative quantities). These four inequalities together carve out a polygon — the feasible region. Every point inside or on this polygon represents a production plan the bakery could actually execute.

The **objective function** is what you're optimizing: profit P = 4x + 6y (dollars per item, say). Think of the level curves of P: for each fixed profit value k, the equation 4x + 6y = k is a straight line. As k increases, this line shifts parallel to itself across the plane. You want to push it as far as possible in the direction of increasing k while still touching the feasible region. The last point of the feasible region the sliding line touches before leaving it entirely is the optimum — and because the feasible region is a polygon, that point is always a **corner vertex**. This is the **Corner Point Theorem**: the optimum of a linear objective over a closed polygonal feasible region always occurs at a vertex (or along an entire edge if the objective is parallel to a boundary, in which case any point on that edge works).

The solution procedure: (1) define your variables, (2) write constraints as inequalities (don't forget x ≥ 0, y ≥ 0), (3) graph the feasible region, (4) find all corner points by solving the intersecting boundary lines, (5) evaluate the objective at each corner, (6) pick the best. The only subtlety is finding the corner points precisely — read them from the graph if the intersections fall at integer coordinates, or solve the corresponding systems of equations. Linear programming underlies real-world optimization in logistics, scheduling, and economics; this two-variable version builds the geometric intuition that scales to problems with hundreds of variables.
