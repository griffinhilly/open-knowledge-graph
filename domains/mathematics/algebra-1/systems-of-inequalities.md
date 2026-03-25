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
- id: systems-word-problems
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

## Questions

```yaml
- question: "A student graphs y > x and y < 4 and shades the region where EITHER inequality is satisfied. What error has the student made?"
  type: multiple-choice
  options:
    - "The student used the wrong type of boundary lines (solid instead of dashed)"
    - "The student found the union of the two half-planes instead of their intersection"
    - "The student should not shade at all — the solution is just the two boundary lines"
    - "The student graphed the inequalities in the wrong order"
  answer: 1
  explanation: "The solution to a system of inequalities is the intersection of all half-planes — every point that satisfies ALL constraints simultaneously. Using the union (shading where ANY one inequality holds) is the core conceptual error. A point like (0, 3) satisfies y < 4 but not y > x, so it should not be in the solution. Only points where both shaded regions overlap belong to the feasible region."

- question: "When graphing 2x + y < 5, which boundary line is correct?"
  type: multiple-choice
  options:
    - "A solid line through 2x + y = 5, because the boundary is part of the solution"
    - "A dashed line through 2x + y = 5, because points on the line do NOT satisfy the strict inequality"
    - "A solid line through 2x + y = 5, because all linear boundaries are solid"
    - "A dashed line through x = 5/2, because only x-intercepts matter"
  answer: 1
  explanation: "Strict inequalities (< and >) use dashed boundary lines because points on the boundary line make the expression equal (not strictly less than or greater than), so they are NOT solutions. Non-strict inequalities (≤ and ≥) use solid lines because boundary points do satisfy the inequality. The boundary here is 2x + y = 5, drawn as a dashed line."

- question: "A system of inequalities can have no solution — an empty feasible region — if the constraints are contradictory."
  type: true-false
  answer: true
  explanation: "The feasible region is the intersection of all half-planes. If the constraints conflict — for example, y > 5 and y < 2 simultaneously — no point can satisfy both, and the intersection is empty. This is perfectly valid mathematically. The system has no solution, just as a system of equations can have no solution (parallel lines)."

- question: "The solution to a system of inequalities is the set of all points that satisfy at least one of the inequalities."
  type: true-false
  answer: false
  explanation: "The solution requires satisfying ALL inequalities simultaneously, not just one. A point in the solution must lie in every half-plane at once — it must be in the overlap of all shaded regions. A point that satisfies only some constraints is in the union (not the intersection) of the half-planes and is not a solution to the system."

- question: "Why does the 'corner test' (using a test point like (0,0)) work for identifying the correct half-plane, and when would you NOT use (0,0) as your test point?"
  type: short-answer
  answer: "The test point strategy works because every linear boundary divides the plane into exactly two half-planes: one where the inequality is satisfied, one where it is not. Plugging any single point into the inequality reveals which side is which. You cannot use (0,0) when the boundary line passes through the origin, because then (0,0) is ON the line — not on either side — and will give an ambiguous result (0 = 0 makes the inequality inconclusive). In that case, choose any other point not on the line, like (1, 0) or (0, 1)."
  explanation: "The test point method eliminates the need to memorize direction rules when rearranging inequalities, which often introduces sign errors. Its only limitation is that the test point must not lie on the boundary line itself. When graphing y > x, for instance, the line y = x passes through the origin, so use (1, 0) instead: 0 > 1 is false, confirming (1,0) is in the shaded-wrong half-plane, so shade the other side (above)."
```

## Explainer

You already know how to solve a single inequality like 2x + 3 > 7 and graph it on a number line. When you move to two dimensions, a single linear inequality no longer describes a segment of a line — it describes an entire **half-plane**: every point on one side of a boundary line. The inequality y > x, for instance, is satisfied by every point above the line y = x, an infinite wedge-shaped region stretching upward to the left. Graphing an inequality means (1) drawing the boundary line, (2) deciding if it is solid or dashed, and (3) shading the half-plane that satisfies the inequality.

A system of inequalities stacks multiple constraints on the same plane. Each constraint cuts the plane in half, and the solution to the system is the region that satisfies all constraints simultaneously — the overlap of all the shaded half-planes. Geometrically, you are intersecting regions. This overlap is called the **feasible region**. It may be a bounded polygon, an unbounded wedge, a half-plane, or empty (if the constraints are contradictory). The shape of the feasible region depends on how the boundary lines relate to each other.

The most reliable method for identifying the correct half-plane is the **test point** strategy. After graphing the boundary line, pick any point not on the line — (0, 0) is almost always the easiest choice — and check whether it satisfies the inequality. If it does, shade the side containing (0, 0). If it does not, shade the opposite side. This eliminates the need to remember rules about which way the inequality symbol "points" after rearranging the equation, which is a common source of sign errors.

The connection to your earlier work on systems of equations is revealing. In a system of equations, you seek specific intersection points. In a system of inequalities, you seek an entire region — every point that simultaneously satisfies all constraints. This structure models real-world optimization problems directly: budget limits, time constraints, and production capacities are all inequalities, and the feasible region represents every combination of choices that keeps you within bounds. The corners of the feasible region are especially important — in linear programming, the optimal solution to any objective function always occurs at one of these corner vertices.
