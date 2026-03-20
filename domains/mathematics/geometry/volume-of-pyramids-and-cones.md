---
id: volume-of-pyramids-and-cones
title: Volume of Pyramids and Cones
domain: mathematics
course: geometry
prerequisites:
  - id: volume-of-prisms-and-cylinders
    type: hard
  - id: surface-area-of-pyramids-and-cones
    type: soft
builds-toward:
  - volume-of-spheres
tags: [3d-geometry, volume, pyramids, cones, one-third]
stage: abstract-reasoning
status: validated
---

# Volume of Pyramids and Cones

## Core Idea
The volume of a pyramid or cone is V = (1/3) * B * h, where B is the base area and h is the perpendicular height. A pyramid or cone is exactly one-third the volume of a prism or cylinder with the same base and height. This 1/3 factor can be demonstrated by filling experiments and proven rigorously using calculus (Cavalieri's principle with varying cross-sections).

## How It's Best Learned
Demonstrate the 1/3 relationship physically: fill a cone with water and pour it into a cylinder of the same base and height three times to fill it. Apply the formula to regular pyramids and cones. Practice finding height or radius given the volume.

## Common Misconceptions
- Forgetting the 1/3 factor.
- Using slant height instead of vertical height.
- Not computing the base area correctly (e.g., for a triangular pyramid, the base is a triangle, not a rectangle).

## Questions

```yaml
- question: "A cone and a cylinder share the same circular base (radius 3 cm) and the same height (7 cm). What is the volume of the cone?"
  type: multiple-choice
  options:
    - "63π cm³"
    - "21π cm³"
    - "9π cm³"
    - "3π cm³"
  answer: 1
  explanation: "V = (1/3)πr²h = (1/3) × π × 9 × 7 = 21π cm³. Option A (63π) is the cylinder's volume — the most common error is omitting the 1/3 factor. The cone holds exactly one-third as much as the matching cylinder, which can be verified by filling the cone with water and pouring it into the cylinder three times to fill it completely."

- question: "A right square pyramid has a base side of 6 cm and a slant height of 5 cm. What is its volume?"
  type: multiple-choice
  options:
    - "60 cm³"
    - "48 cm³"
    - "72 cm³"
    - "36 cm³"
  answer: 1
  explanation: "The slant height (5 cm) is not the perpendicular height. The distance from the base center to the midpoint of an edge is half the side length = 3 cm. Using the Pythagorean theorem: perpendicular height = √(5² − 3²) = √16 = 4 cm. Volume = (1/3)(6²)(4) = (1/3)(36)(4) = 48 cm³. Option A (60 cm³) is the error from substituting slant height directly: (1/3)(36)(5) = 60."

- question: "A cone and a cylinder with the same base and height have equal volumes."
  type: true-false
  answer: false
  explanation: "The cone's volume is exactly one-third the cylinder's. The cylinder uses V = B × h; the cone uses V = (1/3) × B × h. The 1/3 factor arises because the cone's horizontal cross-sections taper toward the apex, unlike the cylinder's uniform cross-sections. Filling the cone three times fills the matching cylinder exactly."

- question: "The slant height of a right cone is always greater than its perpendicular height."
  type: true-false
  answer: true
  explanation: "The slant height is the hypotenuse of a right triangle whose legs are the perpendicular height and the base radius. Since a hypotenuse is always longer than either leg, the slant height must exceed the perpendicular height. This is why substituting slant height into V = (1/3)Bh always overestimates the volume."

- question: "Explain in your own words why the volume of a cone is one-third the volume of a cylinder with the same base and height, rather than one-half."
  type: short-answer
  answer: "As you move upward through a cone, horizontal cross-sections shrink as the square of the fraction of height remaining — a cross-section at height z has area B × ((h−z)/h)². Integrating these shrinking sections from base to apex gives (1/3)Bh. The 1/3 comes from integrating a squared function, not a linear one, which would give 1/2."
  explanation: "The cross-sections shrink in two dimensions simultaneously (both width and depth taper), so their area shrinks as the square of the linear scale factor. Integrating x² from 0 to 1 gives 1/3, not 1/2. A result of 1/2 would arise only if the cross-sections shrank in one dimension, but area scales as the square of linear dimensions — which is why the factor is precisely 1/3."
```

## Explainer

From your study of prisms and cylinders, you know that their volumes follow the same logic: V = B × h, where B is the base area and h is the perpendicular height. The volume of a prism is just "stack up identical cross-sections from bottom to top." A pyramid and a cone work the same way in spirit — but the cross-sections are not identical. As you move upward in a pyramid, the cross-sections get smaller, tapering toward the apex. This tapering is exactly what introduces the **1/3 factor**: V = (1/3) × B × h.

The physical demonstration is the most convincing way to feel this: a cone and a cylinder with the same base and height, where pouring the cone full of water into the cylinder three times exactly fills it. No calculation needed — the 1/3 is built into the geometry. The rigorous proof uses **Cavalieri's principle**: two solids with the same height have equal volumes if every horizontal cross-section at the same height has the same area. For a pyramid of height h, the cross-section at height z above the base is a scaled-down version of the base with linear scale factor (h-z)/h, so its area is B × ((h-z)/h)². Integrating this from 0 to h gives (1/3)Bh — the calculus confirms what the pouring experiment showed.

Applying the formula requires two steps: identify the base shape and compute its area, then multiply by h and 1/3. For a **square pyramid**, B = s² where s is the side of the square base. For a **cone**, B = πr². For a **triangular pyramid** (tetrahedron), B = (1/2) × base × height of the triangular face. The formula V = (1/3)Bh handles all of these uniformly — the shape of the base goes into B, and the rest is the same.

The most common error is confusing **slant height** (the distance along the face from base edge to apex) with **perpendicular height** (the vertical distance from base to apex, measured straight up through the interior). Slant height is relevant for surface area; perpendicular height is what goes into the volume formula. In a right pyramid or cone, the perpendicular height is the leg of a right triangle whose hypotenuse is the slant height and whose other leg is the distance from the center of the base to the edge. You can always recover the perpendicular height using the Pythagorean theorem if only slant height is given.
