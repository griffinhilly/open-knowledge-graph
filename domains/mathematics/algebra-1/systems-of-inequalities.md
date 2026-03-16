---
id: systems-of-inequalities
title: Systems of Inequalities
domain: mathematics
course: algebra-1
prerequisites:
- id: solving-inequalities
  type: hard
- id: compound-inequalities
  type: soft
- id: systems-graphing
  type: soft
builds-toward:
- linear-programming
tags:
- inequalities
- systems
- graphing
- feasible-region
stage: abstract-reasoning
status: validated
---
# Systems of Inequalities

## Core Idea
A system of inequalities consists of two or more inequalities graphed on the same coordinate plane. Each inequality defines a half-plane (the region on one side of a boundary line), and the solution to the system is the intersection of all half-planes — called the feasible region. For example, the system y > x and y < 4 describes the region above the line y = x and below the line y = 4. Boundary lines may be solid (for <= or >=) or dashed (for < or >). Systems of inequalities model real-world constraints: budget limits, minimum requirements, capacity restrictions.

## How It's Best Learned
Start by graphing single linear inequalities and shading the correct half-plane. Then overlay two inequalities and identify where the shading overlaps. Use test points to verify which region satisfies all inequalities simultaneously. Real-world problems (e.g., "you can spend at most $50 on tickets and must buy at least 3") make the feasible region meaningful.

## Common Misconceptions
- Shading the wrong side of a boundary line because of confusion about the direction of the inequality after rearranging.
- Using a solid line for strict inequalities (< or >) instead of a dashed line.

## Explainer

You already know how to solve a single inequality like 2x + 3 > 7 and graph it on a number line. When you move to two dimensions, a single linear inequality no longer describes a segment of a line — it describes an entire **half-plane**: every point on one side of a boundary line. The inequality y > x, for instance, is satisfied by every point above the line y = x, an infinite wedge-shaped region stretching upward to the left. Graphing an inequality means (1) drawing the boundary line, (2) deciding if it is solid or dashed, and (3) shading the half-plane that satisfies the inequality.

A system of inequalities stacks multiple constraints on the same plane. Each constraint cuts the plane in half, and the solution to the system is the region that satisfies all constraints simultaneously — the overlap of all the shaded half-planes. Geometrically, you are intersecting regions. This overlap is called the **feasible region**. It may be a bounded polygon, an unbounded wedge, a half-plane, or empty (if the constraints are contradictory). The shape of the feasible region depends on how the boundary lines relate to each other.

The most reliable method for identifying the correct half-plane is the **test point** strategy. After graphing the boundary line, pick any point not on the line — (0, 0) is almost always the easiest choice — and check whether it satisfies the inequality. If it does, shade the side containing (0, 0). If it does not, shade the opposite side. This eliminates the need to remember rules about which way the inequality symbol "points" after rearranging the equation, which is a common source of sign errors.

The connection to your earlier work on systems of equations is revealing. In a system of equations, you seek specific intersection points. In a system of inequalities, you seek an entire region — every point that simultaneously satisfies all constraints. This structure models real-world optimization problems directly: budget limits, time constraints, and production capacities are all inequalities, and the feasible region represents every combination of choices that keeps you within bounds. The corners of the feasible region are especially important — in linear programming, the optimal solution to any objective function always occurs at one of these corner vertices.
