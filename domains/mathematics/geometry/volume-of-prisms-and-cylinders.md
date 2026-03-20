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

## Questions

```yaml
- question: "A rectangular prism and an oblique prism share the same 6 × 4 base and the same perpendicular height of 10 cm, but the oblique prism's sides are slanted. Which has greater volume?"
  type: multiple-choice
  options:
    - "The rectangular prism, because it is upright and its sides are not wasted on slant"
    - "The oblique prism, because its slant height is longer than 10 cm, adding more material"
    - "They have equal volumes, because they have equal cross-sectional areas at every height"
    - "Cannot be determined without knowing the exact slant angle"
  answer: 2
  explanation: "Cavalieri's principle: if two solids have the same height and identical cross-sectional area at every level, they have equal volumes — regardless of how the solid is tilted. Both prisms stack the same 24 cm² base area over the same 10 cm perpendicular height, so both have volume 240 cm³. The slant height is longer, but it only tells you how far the side travels, not how many layers of base area are stacked."

- question: "A student calculates the volume of a cylinder with radius 3 and height 5 as π × 3 × 5 = 15π. What is wrong with this calculation?"
  type: multiple-choice
  options:
    - "The student should have used the diameter (6) instead of the radius"
    - "The student forgot to square the radius — πr²h requires r², not r, so the result has the wrong value and wrong units"
    - "The student should have multiplied by 2π to account for the full circumference"
    - "The formula is correct; the student just needs to add the correct units (cm³)"
  answer: 1
  explanation: "The base of a cylinder is a circle with area πr², not πr. Forgetting to square the radius gives πrh, which has units of length² (not length³) — dimensionally wrong for volume. With r = 3 and h = 5, the correct volume is π(3²)(5) = 45π, not 15π. This is three times larger — a significant error. Always check: volume must have cubic units, confirming you multiplied an area by a length."

- question: "The formula V = Bh works for oblique (tilted) prisms as long as you use the slant height rather than the perpendicular height."
  type: true-false
  answer: false
  explanation: "This is backwards: V = Bh requires the *perpendicular* height — the straight-up distance between the two bases. The slant height is longer and would give an inflated, incorrect volume. Cavalieri's principle explains why: volume is the sum of identical cross-sectional layers stacked vertically; 'height' in V = Bh counts how many vertical layers there are, not how long the slanted side runs."

- question: "A pyramid has the same base and perpendicular height as a prism. The pyramid's volume is less than the prism's volume."
  type: true-false
  answer: true
  explanation: "Yes — a pyramid's volume is exactly (1/3)Bh, compared to Bh for the corresponding prism. They share the same base area and height, but the pyramid tapers to a point, so its cross-sectional area shrinks as you move upward; the prism's cross-section stays constant. This one-third relationship holds for all pyramids relative to their matching prisms (and cones relative to cylinders), which Cavalieri's principle also helps justify."

- question: "Why must you use perpendicular height — not slant height — when calculating the volume of an oblique prism or cylinder?"
  type: short-answer
  answer: "Because V = Bh counts how many layers of base area are stacked to reach the solid's full height. 'Height' means the perpendicular distance between the two bases — how far up the layers are stacked. The slant height measures the distance along the tilted edge, which is longer, but it doesn't change the number of horizontal layers or their size. Using slant height would overcount the layers and give an incorrect (inflated) volume."
  explanation: "Cavalieri's principle formalizes this: volume depends on cross-sectional area at each horizontal level. When a prism is tilted, those cross-sections shift sideways but stay the same size — the tilting doesn't add or remove material. Only the perpendicular height captures the true number of identical layers being stacked."
```

## Explainer

You've already worked with the surfaces of prisms and cylinders — unfolding them into nets and computing total surface area. Volume is a different question: instead of measuring the wrapper around a solid, you're measuring the space inside it.

The core idea is **stacking layers**. Imagine slicing a rectangular prism into thin horizontal sheets, each identical to the base. If the base has area B and you stack layers to a height h, the total volume is B × h. This is not just a formula — it's a physical fact: volume accumulates as area stacked over height. For a rectangular prism with a 4 × 3 base, each layer contributes 12 square units; 5 layers gives 60 cubic units. The unit change from square units to cubic units reflects this: you're multiplying an area (two-dimensional) by a length (one-dimensional) to get a three-dimensional measure.

**Cavalieri's principle** extends this reasoning to oblique (tilted) prisms and cylinders: if two solids have the same height and the same cross-sectional area at every level, they have equal volumes. Imagine a stack of coins standing straight versus leaning sideways — the same number of coins, each the same size, contain the same total metal regardless of how they're tilted. This is why V = Bh works for all prisms and cylinders, not just upright ones, as long as you use the **perpendicular height** rather than the slant length.

For a cylinder, the base is a circle with area πr², giving V = πr²h. A common error is computing πr·h — forgetting to square the radius — which has the wrong units (length²) and is dimensionally incorrect. Notice that volume and surface area formulas look similar but differ in dimensional structure: surface area is measured in units² while volume is in units³. As you move on to pyramids and cones, you'll discover that V = (1/3)Bh — they hold exactly one-third the volume of the corresponding prism or cylinder with the same base and height, a fact that Cavalieri's principle also helps explain.
