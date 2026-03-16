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

## Explainer

From your work with systems of inequalities, you know how to graph the region satisfying multiple linear constraints simultaneously — each inequality cuts away part of the plane, and the overlapping region that satisfies all constraints is the **feasible region**. Linear programming adds one more ingredient: a goal. Among all the points in that region, which one makes some quantity (profit, cost, time) as large or as small as possible?

Set up the problem with two decision variables. Say a bakery can make x loaves of bread and y cakes, each requiring different amounts of time and ingredients. The constraints become inequalities: maybe 2x + 3y ≤ 12 (hours of oven time), x + y ≤ 5 (pounds of flour), plus x ≥ 0 and y ≥ 0 (you can't make negative quantities). These four inequalities together carve out a polygon — the feasible region. Every point inside or on this polygon represents a production plan the bakery could actually execute.

The **objective function** is what you're optimizing: profit P = 4x + 6y (dollars per item, say). Think of the level curves of P: for each fixed profit value k, the equation 4x + 6y = k is a straight line. As k increases, this line shifts parallel to itself across the plane. You want to push it as far as possible in the direction of increasing k while still touching the feasible region. The last point of the feasible region the sliding line touches before leaving it entirely is the optimum — and because the feasible region is a polygon, that point is always a **corner vertex**. This is the **Corner Point Theorem**: the optimum of a linear objective over a closed polygonal feasible region always occurs at a vertex (or along an entire edge if the objective is parallel to a boundary, in which case any point on that edge works).

The solution procedure: (1) define your variables, (2) write constraints as inequalities (don't forget x ≥ 0, y ≥ 0), (3) graph the feasible region, (4) find all corner points by solving the intersecting boundary lines, (5) evaluate the objective at each corner, (6) pick the best. The only subtlety is finding the corner points precisely — read them from the graph if the intersections fall at integer coordinates, or solve the corresponding systems of equations. Linear programming underlies real-world optimization in logistics, scheduling, and economics; this two-variable version builds the geometric intuition that scales to problems with hundreds of variables.
