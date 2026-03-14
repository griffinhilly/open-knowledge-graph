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
