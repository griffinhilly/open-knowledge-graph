---
id: triple-integrals
title: Triple Integrals in Cartesian Coordinates
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals-cartesian
  type: hard
- id: area-volume-integrals
  type: soft
- id: applications-double-integrals
  type: soft
builds-toward:
- triple-integrals-cylindrical
- triple-integrals-spherical
tags:
- triple-integral
- volume
stage: formal-systems
status: validated
---
# Triple Integrals in Cartesian Coordinates

## Core Idea
The triple integral ∭_W f(x,y,z) dV gives signed volume or accumulates density. In Cartesian coordinates, dV = dx dy dz, and the integral becomes an iterated integral with three steps.

## Questions

```yaml
- question: "The region W is defined by 0 ≤ x ≤ 1, 0 ≤ y ≤ 1, and 0 ≤ z ≤ 4 − x² − y². A student evaluates the innermost integral ∫₀^(4−x²−y²) dz. What does the result of this step represent?"
  type: multiple-choice
  options:
    - "The total volume of W, computed in a single step"
    - "The value 4 − x² − y², a function of x and y that represents the height of the solid at each point (x,y), still to be integrated over the base region"
    - "A constant equal to the average height of the solid"
    - "Zero, because integrating 1 over a symmetric region cancels out"
  answer: 1
  explanation: "When you evaluate the innermost integral ∫₀^(4−x²−y²) 1 dz with x and y held fixed, you get 4 − x² − y² — a function that depends on x and y. This represents the height of the solid at that particular horizontal position. You have not yet computed the full volume; you have computed a height function that still needs to be integrated over the base region (0 ≤ x ≤ 1, 0 ≤ y ≤ 1) to sum up all those heights. The triple integral is completed by the two remaining integrations over y and x."

- question: "A solid W is described as: 'at each height z from 0 to 2, the cross-section is the disk x² + y² ≤ z².' What is the most natural order of integration for computing ∭_W f dV?"
  type: multiple-choice
  options:
    - "Integrate z first (innermost), then x, then y — because z determines the boundary"
    - "Integrate x first, then y, then z — alphabetical order is always simplest"
    - "Integrate x and y first (inner and middle), then z last (outer) — because the solid is naturally described as cross-sections at each z"
    - "All six orderings are equally simple for this region — choice is arbitrary"
  answer: 2
  explanation: "When a solid is described via cross-sections at each z — 'at height z, the cross-section is ...' — the natural structure calls for integrating over x and y first (for each fixed z) and then integrating over z last. For each fixed z, the cross-section x² + y² ≤ z² is a disk of radius z, which is easily described in polar coordinates. If you tried to integrate z first, you would need to invert the region description — finding for each (x,y) the range of z — which is algebraically more complicated. Choosing the order that matches the natural description of the solid is the core skill in setting up triple integrals."

- question: "If f(x,y,z) = 1 everywhere in the region W, then ∭_W dV computes the surface area of W."
  type: true-false
  answer: false
  explanation: "When f = 1, the triple integral ∭_W 1 dV computes the volume of W, not the surface area. Each infinitesimal piece dV = dx dy dz contributes its volume to the sum, and integrating over the entire region W totals all these pieces into the full three-dimensional volume. Surface area requires a different kind of integral — a surface integral that accounts for the shape and orientation of the boundary, not an integration over the interior."

- question: "All six orderings of a triple integral (dx dy dz, dx dz dy, dy dx dz, etc.) give the same numerical answer when computed correctly, even though the limits of integration look different for each ordering."
  type: true-false
  answer: true
  explanation: "This is Fubini's theorem applied to triple integrals: as long as f is continuous (or integrable) over W, the value of ∭_W f dV is independent of the order of integration. What changes between orderings is the description of the limits — some orderings produce simple constant limits, others produce complicated functions. The skill in choosing an order is not about getting a different answer but about finding the algebraically cleanest path to the same answer. A solid that is easy to describe as 'upper surface minus lower surface over a base region' naturally suggests integrating z first."

- question: "Why is choosing the order of integration a skill in setting up triple integrals, rather than an arbitrary convention? What factors determine which ordering is most practical?"
  type: short-answer
  answer: "The six orderings all give the same value, but they require different limit expressions. The order that matches the natural geometric description of the solid produces the simplest limits. If the solid is described as 'lying between two surfaces for (x,y) in a base region,' integrating the bounded variable (z) first produces simple function-valued limits for z and constant limits for x and y. If instead you integrate in the wrong order, the limits of the inner integral may be impossible to express simply, or the resulting integrals may be much harder to evaluate analytically."
  explanation: "In practice, the first question to ask is: how is the boundary of W described most naturally? If it is 'above the plane z=0 and below the paraboloid z = 4−x²−y²,' then z is the natural innermost variable. If it is 'inside the cylinder x²+y² ≤ 1 from z=0 to z=3,' then x and y are the natural inner variables with z outer. Drawing the solid and identifying which variable's bounds depend on the others directs the order choice. Some regions require switching to cylindrical or spherical coordinates to become tractable, which is the motivation for those coordinate systems."
```

## Explainer

You have already computed double integrals by slicing a two-dimensional region into strips and integrating layer by layer. A **triple integral** extends this process one dimension further: you slice a three-dimensional solid W into thin slabs, then into columns, then into small box-shaped pieces of volume dV = dx dy dz. The triple iterated integral ∫∫∫ f(x,y,z) dx dy dz integrates out one variable at a time, treating all other variables as constants during each step. The three integrations correspond to three nested loops: innermost first, outermost last.

The geometric meaning depends on f. When f(x,y,z) = 1, the triple integral ∭_W 1 dV equals the **volume** of W — every tiny box contributes its volume 1 · dx dy dz, and summing over W gives the total. When f represents mass density (mass per unit volume), ∭_W f dV equals total mass. When f represents charge density, the integral gives total charge. Triple integrals are the natural tool whenever a quantity is distributed continuously through a three-dimensional region and you want the total.

Setting up the limits requires describing the region W precisely. For a rectangular box a ≤ x ≤ b, c ≤ y ≤ d, e ≤ z ≤ g, all six limits are constants and the integral is straightforward. For a non-rectangular solid — say the region above the xy-plane, below z = 4 - x² - y², for x and y inside the unit square — the limits interact: z runs from 0 to 4 - x² - y², while x and y have constant limits. The inner integral (in z) is computed first with x and y fixed, producing a function of x and y; then the double integral over x and y finishes the calculation.

Choosing the order of integration is where the real skill lies. The same solid W can be described with any of six orderings (dx dy dz, dx dz dy, dy dx dz, and so on), and the correct limits differ for each. A solid described naturally as "for each (x, y) in region D, z runs from the lower surface to the upper surface" calls for integrating z first (inner), then (x, y) over D. If the solid is instead described by cross-sections perpendicular to the z-axis — "at height z, the cross-section is region D(z)" — then integrate over x and y first (inner and middle), z last (outer). Drawing the solid and identifying its natural description is always the first step before writing any integral limits.
