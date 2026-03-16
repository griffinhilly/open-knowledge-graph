---
id: volume-of-prisms-and-cylinders
title: Volume of Prisms and Cylinders
domain: mathematics
course: geometry
prerequisites:
  - id: surface-area-of-prisms
    type: soft
  - id: surface-area-of-cylinders
    type: soft
builds-toward:
  - volume-of-pyramids-and-cones
  - volume-of-spheres
tags: [3d-geometry, volume, prisms, cylinders]
stage: abstract-reasoning
status: validated
---

# Volume of Prisms and Cylinders

## Core Idea
The volume of a prism or cylinder is V = B * h, where B is the area of the base and h is the perpendicular height. This follows from Cavalieri's principle: solids with equal cross-sectional areas at every height have equal volumes. For a rectangular prism, V = lwh. For a cylinder, V = pi*r^2*h. Volume measures the space enclosed by a three-dimensional figure.

## How It's Best Learned
Start with unit cubes to build intuition for volume as "layers of area." Show that stacking identical cross-sections produces the volume formula. Practice with various base shapes. Introduce Cavalieri's principle as the underlying justification. Give problems requiring unit conversions.

## Common Misconceptions
- Confusing volume and surface area formulas.
- Using the slant height instead of the perpendicular height for oblique prisms.
- Forgetting to square the radius in pi*r^2*h (computing pi*r*h instead).

## Explainer

You've already worked with the surfaces of prisms and cylinders — unfolding them into nets and computing total surface area. Volume is a different question: instead of measuring the wrapper around a solid, you're measuring the space inside it.

The core idea is **stacking layers**. Imagine slicing a rectangular prism into thin horizontal sheets, each identical to the base. If the base has area B and you stack layers to a height h, the total volume is B × h. This is not just a formula — it's a physical fact: volume accumulates as area stacked over height. For a rectangular prism with a 4 × 3 base, each layer contributes 12 square units; 5 layers gives 60 cubic units. The unit change from square units to cubic units reflects this: you're multiplying an area (two-dimensional) by a length (one-dimensional) to get a three-dimensional measure.

**Cavalieri's principle** extends this reasoning to oblique (tilted) prisms and cylinders: if two solids have the same height and the same cross-sectional area at every level, they have equal volumes. Imagine a stack of coins standing straight versus leaning sideways — the same number of coins, each the same size, contain the same total metal regardless of how they're tilted. This is why V = Bh works for all prisms and cylinders, not just upright ones, as long as you use the **perpendicular height** rather than the slant length.

For a cylinder, the base is a circle with area πr², giving V = πr²h. A common error is computing πr·h — forgetting to square the radius — which has the wrong units (length²) and is dimensionally incorrect. Notice that volume and surface area formulas look similar but differ in dimensional structure: surface area is measured in units² while volume is in units³. As you move on to pyramids and cones, you'll discover that V = (1/3)Bh — they hold exactly one-third the volume of the corresponding prism or cylinder with the same base and height, a fact that Cavalieri's principle also helps explain.
