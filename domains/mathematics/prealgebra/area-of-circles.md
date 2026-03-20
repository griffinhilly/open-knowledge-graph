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

## Questions

```yaml
- question: "Circle A has a radius of 3 cm. Circle B has a radius of 6 cm. How many times larger is Circle B's area than Circle A's?"
  type: multiple-choice
  options:
    - "2 times larger — the radius doubled, so the area doubles"
    - "3 times larger — corresponding to the ratio of their radii"
    - "4 times larger — area scales with the square of the radius"
    - "6 times larger — because pi multiplies the squared difference"
  answer: 2
  explanation: "Area scales with the square of the radius: A = πr². Circle A has area π(3²) = 9π. Circle B has area π(6²) = 36π. The ratio is 36π ÷ 9π = 4. When the radius doubles, area quadruples — not doubles. This is because area is two-dimensional: it grows in both directions simultaneously. The tempting wrong answer (2 times) treats area as if it scales linearly with radius, like circumference does. The r² in the formula is the key: doubling r multiplies area by 2² = 4."

- question: "A circle has a diameter of 10 cm. Which calculation correctly finds its area?"
  type: multiple-choice
  options:
    - "π × 10² = 100π cm² — applying the formula directly to the given measurement"
    - "π × 5² = 25π cm² — dividing the diameter by 2 to get the radius first"
    - "2π × 10 = 20π cm² — using the circumference formula"
    - "π × (10/2) = 5π cm² — dividing diameter by 2 but not squaring"
  answer: 1
  explanation: "The formula A = πr² requires the radius, not the diameter. A diameter of 10 cm means the radius is 5 cm (half the diameter). The correct area is π × 5² = 25π ≈ 78.5 cm². Using the diameter directly — π × 10² = 100π — gives an answer exactly four times too large. This is the most common computational error with circle area: failing to halve the diameter before squaring. Always ask 'Is this the radius or the diameter?' before substituting into the formula."

- question: "Doubling the radius of a circle doubles its area."
  type: true-false
  answer: false
  explanation: "Doubling the radius quadruples the area. If the original radius is r, the original area is πr². If the radius doubles to 2r, the new area is π(2r)² = π × 4r² = 4πr² — exactly four times the original. Circumference scales linearly (C = 2πr), so doubling the radius does double the circumference. Confusing the two formulas leads to the intuition that area also doubles, but the r² in the area formula means area grows much faster than radius."

- question: "The formula A = πr² can be derived by rearranging a circle's wedge-shaped slices into an approximate rectangle with height r and base πr."
  type: true-false
  answer: true
  explanation: "This is the standard geometric motivation for the formula. Slice a circle into many thin wedges (like a pizza), then alternate them pointing up and down. As the wedges become infinitely thin, the resulting shape becomes a rectangle: its height equals the radius r (the length of each wedge), and its base equals half the circumference = πr (half the perimeter wraps along the top, half along the bottom). Area of rectangle = r × πr = πr². This derivation shows where the formula comes from rather than treating it as an arbitrary rule."

- question: "Why does doubling a circle's radius quadruple its area rather than double it?"
  type: short-answer
  answer: "Because area is two-dimensional and the formula A = πr² squares the radius. When the radius doubles, the squared term grows by a factor of 2² = 4. The circle grows in both length and width simultaneously when the radius increases, so area grows as the product of two doublings."
  explanation: "This contrasts with circumference (C = 2πr), which scales linearly — double the radius, double the circumference. Area's quadratic dependence on radius appears throughout science and engineering: a pipe twice as wide carries four times the flow, a photograph blown up to twice the linear size needs four times the ink. Recognizing that area and length scale differently is one of the most important and frequently applied geometric insights."
```

## Explainer

You already know that the circumference of a circle is C = 2πr — the total distance around the edge. Area asks a different question: how much flat space does the circle cover? To see where A = πr² comes from, imagine slicing a circle like a pizza into many thin wedges. Now fan those wedges out and lay them alternately pointing up and down, fitting them together like teeth on two combs. The resulting shape is nearly a rectangle. As you cut into thinner and thinner slices, the bumpy top and bottom edges become smoother, and the shape approaches a true rectangle. The height of that rectangle is the radius r, and the length is half the circumference — πr. Area of the rectangle = height × length = r × πr = πr². That is where the formula comes from.

Notice what the formula tells you about **scaling**. Circumference scales with r (double the radius, double the circumference), but area scales with r² (double the radius, quadruple the area). If one circle has radius 3 cm and another has radius 6 cm, the bigger one is not twice as large in area — it is four times as large. This is because area is two-dimensional: it grows in both length and width when the radius increases. This square relationship appears constantly in science and engineering — why a pipe twice as wide can carry four times the flow, why a photograph blown up to twice the size needs four times the ink.

The most common error is using the diameter instead of the radius. If you are given a diameter of 10, your radius is 5, and A = π(5²) = 25π ≈ 78.5 square units. Using the diameter directly would give π(10²) = 100π — exactly four times too large. Before substituting into A = πr², always ask: "Is this number the radius or the diameter?" If it is the diameter, divide by 2 first. A helpful memory trick: the radius goes to the center, and the formula uses the radius because we defined the circle by how far we reach out from the center.

You can also work backward: given the area, find the radius. If A = 50π, then πr² = 50π, so r² = 50, and r = √50 ≈ 7.07. This uses your knowledge of exponents and square roots from earlier topics. The two-way fluency — plugging in to find area, and unpacking area to find radius — prepares you for surface area and volume work ahead, where circular cross-sections appear inside cylinders, cones, and spheres.
