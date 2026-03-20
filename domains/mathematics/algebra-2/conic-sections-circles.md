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

## Questions

```yaml
- question: "What are the center and radius of the circle (x − 4)² + (y + 3)² = 25?"
  type: multiple-choice
  options:
    - "Center (4, 3), radius 25"
    - "Center (−4, −3), radius 5"
    - "Center (4, −3), radius 5"
    - "Center (4, 3), radius 5"
  answer: 2
  explanation: "The standard form is (x − h)² + (y − k)² = r². Matching: (x − 4)² tells us h = 4. The y-term is (y + 3)² = (y − (−3))², so k = −3. The radius is √25 = 5, not 25. Option D is the most common mistake — reading the y-coordinate as +3 instead of −3 because the equation shows '+3' inside the parentheses. The rule: the center's coordinate is the value you *subtract from* the variable to get the expression inside the parentheses, so (y + 3) = (y − (−3)) means y-coordinate is −3."

- question: "A circle passes through all points exactly 6 units from (−2, 5). Which equation represents this circle?"
  type: multiple-choice
  options:
    - "(x + 2)² + (y − 5)² = 6"
    - "(x − 2)² + (y + 5)² = 36"
    - "(x + 2)² + (y − 5)² = 36"
    - "(x − 2)² + (y + 5)² = 6"
  answer: 2
  explanation: "The center is (−2, 5), giving (x − (−2))² + (y − 5)² = (x + 2)² + (y − 5)². The radius is 6, so the right side is r² = 36, not 6. Option A uses the correct center but forgets to square the radius — the most common arithmetic error. Options B and D have the center signs flipped: center (−2, 5) requires (x + 2)² and (y − 5)², not (x − 2)² and (y + 5)²."

- question: "The equation (x − 3)² + (y + 2)² = 16 represents a circle with center (3, 2) and radius 16."
  type: true-false
  answer: false
  explanation: "Two errors are packed into this statement. First, the center's y-coordinate is −2, not 2: (y + 2)² = (y − (−2))² means k = −2. Second, the radius is √16 = 4, not 16. The right side of the standard form equation is r², so you must take the square root to find r. These are the two most common circle equation errors: misreading the sign of the center and forgetting to take the square root of the right side."

- question: "The standard form of a circle's equation, (x − h)² + (y − k)² = r², is derived directly from the distance formula by squaring both sides of the equation for all points at distance r from center (h, k)."
  type: true-false
  answer: true
  explanation: "The derivation is direct: start with the geometric definition (all points (x, y) at distance r from (h, k)), apply the distance formula (√((x−h)² + (y−k)²) = r), and square both sides to get (x−h)² + (y−k)² = r². This is not a formula to memorize in isolation — it is the algebraic encoding of the geometric definition. Understanding this origin makes sign errors less likely: you know the equation says 'the distance from (x, y) to (h, k) equals r,' which tells you exactly where h and k appear and why the right side is r² not r."

- question: "Explain why the x-coordinate of the center in (x + 5)² + (y − 2)² = 36 is −5, not 5. Use the geometric definition of a circle in your explanation."
  type: short-answer
  answer: "A circle is the set of all points at distance r from the center (h, k). The distance formula gives √((x−h)² + (y−k)²) = r, and squaring both sides gives (x−h)² + (y−k)² = r². The term (x + 5)² must match the form (x − h)², so we rewrite it: (x + 5)² = (x − (−5))², revealing that h = −5. The center's x-coordinate is the value you subtract from x to get the expression — here, you subtract −5, so the center is at x = −5. Reading (x + 5)² as 'center at x = 5' confuses the sign because the standard form subtracts h, so a positive term inside means a negative center coordinate."
  explanation: "This sign confusion is responsible for most errors in circle problems. The key habit is to rewrite the term in standard form before reading the center: always express as (x − h)², never read h directly from the coefficient. If the equation shows (x + 5), rewrite it as (x − (−5)) before identifying h = −5. The same logic applies to y: (y − 2)² directly gives k = 2, while (y + 3)² = (y − (−3))² gives k = −3."
```

## Explainer

A circle is defined geometrically as the set of all points equidistant from a fixed center. Translating that into algebra uses the distance formula you already know: the distance from (x, y) to center (h, k) is sqrt((x − h)² + (y − k)²). Setting this equal to r and squaring both sides gives the **standard form** (x − h)² + (y − k)² = r². This equation is not a formula to memorize in isolation — it is a direct algebraic encoding of the geometric definition.

Reading the equation correctly requires attention to signs. In (x − 3)² + (y + 2)² = 25, the center is (3, −2), not (3, 2). The y-term is (y − (−2))², so the y-coordinate of the center is −2. The radius is sqrt(25) = 5, not 25. These errors are the most common pitfalls, so it helps to always read the equation as "subtract h from x" and "subtract k from y" before identifying the center, then take the square root to find r.

The **general form** x² + y² + Dx + Ey + F = 0 looks nothing like standard form, but your prerequisite skill — completing the square — converts it directly. Group the x-terms and y-terms, complete each square by adding (D/2)² and (E/2)² to both sides, then read off center and radius. For example: x² + y² − 6x + 4y − 3 = 0 → (x² − 6x + 9) + (y² + 4y + 4) = 3 + 9 + 4 → (x − 3)² + (y + 2)² = 16. Center (3, −2), radius 4. Completing the square in both variables simultaneously is the core algebraic technique for this conversion.

As a **conic section**, a circle arises when a plane cuts a cone perpendicular to its axis. It is a special case of an ellipse — one where both axes are equal. This framing sets up the broader family you will study next: ellipses, parabolas, and hyperbolas each arise from tilting the cutting plane at a different angle. The circle is the most symmetric case, which is why it serves as the entry point into conics; its equation is the simplest, and the completing-the-square technique you practice here carries over unchanged to all the others.
