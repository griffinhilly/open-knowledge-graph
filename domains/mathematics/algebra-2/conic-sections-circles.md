---
id: conic-sections-circles
title: 'Conic Sections: Circles'
domain: mathematics
course: algebra-2
prerequisites:
- id: circle-basics
  type: hard
- id: solving-quadratic-equations-completing-the-square
  type: hard
- id: coordinate-geometry-proofs
  type: soft
builds-toward:
- conic-sections-ellipses
- conic-sections-overview
tags:
- conics
- circles
- center
- radius
- standard-form
stage: abstract-reasoning
status: validated
---
# Conic Sections: Circles

## Core Idea
A circle is the set of all points at a fixed distance (radius r) from a center point (h, k). The standard form equation is (x-h)^2 + (y-k)^2 = r^2. The general form x^2 + y^2 + Dx + Ey + F = 0 can be converted to standard form by completing the square in both x and y. A circle is a special conic section (a degenerate ellipse where both axes are equal). Two circles can intersect in 0, 1, or 2 points.

## How It's Best Learned
Start from the distance formula definition: sqrt((x-h)^2 + (y-k)^2) = r, then square both sides. Practice writing equations given center and radius, and identifying center and radius from equations. Convert from general form to standard form by completing the square. Graph circles and find intersection points with lines.

## Common Misconceptions
- Forgetting to square the radius on the right side (writing r instead of r^2).
- Not completing the square correctly when converting from general form.
- Thinking (x-3)^2 + (y+2)^2 = 16 has center (3, 2) instead of (3, -2).
- Confusing the equation of a circle with that of an ellipse.

## Explainer

A circle is defined geometrically as the set of all points equidistant from a fixed center. Translating that into algebra uses the distance formula you already know: the distance from (x, y) to center (h, k) is sqrt((x − h)² + (y − k)²). Setting this equal to r and squaring both sides gives the **standard form** (x − h)² + (y − k)² = r². This equation is not a formula to memorize in isolation — it is a direct algebraic encoding of the geometric definition.

Reading the equation correctly requires attention to signs. In (x − 3)² + (y + 2)² = 25, the center is (3, −2), not (3, 2). The y-term is (y − (−2))², so the y-coordinate of the center is −2. The radius is sqrt(25) = 5, not 25. These errors are the most common pitfalls, so it helps to always read the equation as "subtract h from x" and "subtract k from y" before identifying the center, then take the square root to find r.

The **general form** x² + y² + Dx + Ey + F = 0 looks nothing like standard form, but your prerequisite skill — completing the square — converts it directly. Group the x-terms and y-terms, complete each square by adding (D/2)² and (E/2)² to both sides, then read off center and radius. For example: x² + y² − 6x + 4y − 3 = 0 → (x² − 6x + 9) + (y² + 4y + 4) = 3 + 9 + 4 → (x − 3)² + (y + 2)² = 16. Center (3, −2), radius 4. Completing the square in both variables simultaneously is the core algebraic technique for this conversion.

As a **conic section**, a circle arises when a plane cuts a cone perpendicular to its axis. It is a special case of an ellipse — one where both axes are equal. This framing sets up the broader family you will study next: ellipses, parabolas, and hyperbolas each arise from tilting the cutting plane at a different angle. The circle is the most symmetric case, which is why it serves as the entry point into conics; its equation is the simplest, and the completing-the-square technique you practice here carries over unchanged to all the others.
