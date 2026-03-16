---
id: area-of-circles
title: Area of Circles
domain: mathematics
course: prealgebra
prerequisites:
- id: circumference
  type: hard
- id: exponents-intro
  type: soft
builds-toward:
- surface-area-intro
- volume-of-prisms-and-cylinders
tags:
- area
- circles
- pi
- geometry
stage: abstract-reasoning
status: validated
---
# Area of Circles

## Core Idea
The area of a circle is A = pi * r², where r is the radius. This formula can be motivated by cutting a circle into many thin wedges and rearranging them into an approximate parallelogram with height r and base pi * r, giving area pi * r². The squaring of the radius means that doubling the radius quadruples the area — a key insight about how area scales differently from length. Circle area is used in calculating the cross-sections of cylinders, the area of sectors, and countless applications in science and engineering.

## How It's Best Learned
Show the wedge-rearrangement demonstration (physically or with animation). Emphasize that you must use the radius, not the diameter, in the formula. If given the diameter, first divide by 2. Practice computing areas for given radii, and also working backward — given the area, find the radius. Compare with circumference to help students distinguish the two formulas.

## Common Misconceptions
- Using the diameter instead of the radius in the formula (computing pi * d² instead of pi * r²).
- Forgetting to square the radius (computing pi * r instead of pi * r²).
- Mixing up area and circumference formulas.

## Explainer

You already know that the circumference of a circle is C = 2πr — the total distance around the edge. Area asks a different question: how much flat space does the circle cover? To see where A = πr² comes from, imagine slicing a circle like a pizza into many thin wedges. Now fan those wedges out and lay them alternately pointing up and down, fitting them together like teeth on two combs. The resulting shape is nearly a rectangle. As you cut into thinner and thinner slices, the bumpy top and bottom edges become smoother, and the shape approaches a true rectangle. The height of that rectangle is the radius r, and the length is half the circumference — πr. Area of the rectangle = height × length = r × πr = πr². That is where the formula comes from.

Notice what the formula tells you about **scaling**. Circumference scales with r (double the radius, double the circumference), but area scales with r² (double the radius, quadruple the area). If one circle has radius 3 cm and another has radius 6 cm, the bigger one is not twice as large in area — it is four times as large. This is because area is two-dimensional: it grows in both length and width when the radius increases. This square relationship appears constantly in science and engineering — why a pipe twice as wide can carry four times the flow, why a photograph blown up to twice the size needs four times the ink.

The most common error is using the diameter instead of the radius. If you are given a diameter of 10, your radius is 5, and A = π(5²) = 25π ≈ 78.5 square units. Using the diameter directly would give π(10²) = 100π — exactly four times too large. Before substituting into A = πr², always ask: "Is this number the radius or the diameter?" If it is the diameter, divide by 2 first. A helpful memory trick: the radius goes to the center, and the formula uses the radius because we defined the circle by how far we reach out from the center.

You can also work backward: given the area, find the radius. If A = 50π, then πr² = 50π, so r² = 50, and r = √50 ≈ 7.07. This uses your knowledge of exponents and square roots from earlier topics. The two-way fluency — plugging in to find area, and unpacking area to find radius — prepares you for surface area and volume work ahead, where circular cross-sections appear inside cylinders, cones, and spheres.
