---
id: hydrostatic-pressure-distribution
title: Hydrostatic Pressure Distribution
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pressure-and-forces-in-fluids
  type: hard
- id: fluid-properties-and-continuum
  type: soft
builds-toward:
- forces-on-submerged-surfaces
- floating-body-stability-equilibrium
tags:
- statics
- pressure
- hydrostatics
stage: formal-systems
status: validated
---

# Hydrostatic Pressure Distribution

## Core Idea
In a static fluid, pressure varies linearly with depth: P = P₀ + ρgh, where ρ is fluid density, g is gravitational acceleration, and h is depth. This hydrostatic pressure distribution results from the weight of fluid above and acts perpendicular to any surface. The distribution is independent of the shape of the container and depends only on the fluid density and vertical height difference.

## How It's Best Learned
Measure water pressure at different depths in a column using pressure gauges or manometers. Observe that pressure increase per unit depth is the same regardless of container shape, demonstrating the principle that pressure depends only on vertical height.

## Common Misconceptions
- Pressure at a depth depends on the shape or total volume of the container (pressure depends only on depth, not on container shape).
- Pressure in a fluid only acts downward (pressure acts in all directions equally).
- Different fluids at the same depth have the same pressure (pressure depends on fluid density; heavier fluids have higher pressure at the same depth).

## Questions

```yaml
- question: "Container A is a narrow cylinder with diameter 2 cm filled with water to a depth of 3 m. Container B is a swimming pool 25 m wide filled with water to the same 3 m depth. What is the pressure at the bottom of each container?"
  type: multiple-choice
  options:
    - "Container B has much higher pressure because it contains far more water pushing down"
    - "Container A has higher pressure because the narrow column concentrates the weight"
    - "Both containers have the same pressure at the bottom, because pressure depends only on depth and fluid density"
    - "The pressures are equal only if the containers are at the same atmospheric pressure"
  answer: 2
  explanation: "This is the hydrostatic paradox: P = P₀ + ρgh depends only on fluid density ρ, gravitational acceleration g, and vertical depth h — not on the container's volume, cross-sectional area, or shape. Both containers have the same ρ (water), the same g, and the same h (3 m). The additional weight of water in the pool is supported by the pool's sloped or flat sidewalls, not transmitted to the bottom. This result surprises most students but follows directly from the force balance that derives the hydrostatic equation."

- question: "A vertical dam wall holds back water to a depth of 20 m. At what depth below the water surface is the hydrostatic pressure on the dam wall greatest, and why?"
  type: multiple-choice
  options:
    - "At the top of the dam (0 m depth), where the water exerts the most direct force"
    - "At mid-depth (10 m), where the pressure is averaged over the wall"
    - "At the base (20 m depth), because pressure increases linearly with depth and is maximum there"
    - "Pressure is uniform across the dam face because the water is static"
  answer: 2
  explanation: "From P = P₀ + ρgh, pressure increases linearly with depth h. At 20 m depth, the gauge pressure is ρgh = 1000 × 9.81 × 20 ≈ 196 kPa, which is approximately twice the pressure at 10 m. Pressure is maximum at the base, not uniform. This is why dam walls are typically thicker at the base — the structure must resist a greater hydrostatic force there. Computing the net force on the dam requires integrating the linearly varying pressure over the entire submerged face."

- question: "A U-tube manometer measures the pressure difference between two points using only the height difference of the fluid columns in the two arms, regardless of the tube's diameter."
  type: true-false
  answer: true
  explanation: "The hydrostatic equation P = P₀ + ρgh shows that pressure in a static fluid column depends only on the vertical height of fluid above it, not on the tube's cross-sectional area or diameter. A thin U-tube and a wide U-tube filled with the same fluid to the same height have the same pressure at every depth. This is precisely what makes manometers practical: you need only measure the fluid height difference, not the tube geometry, to determine a pressure difference."

- question: "Hydrostatic pressure acts primarily downward on surfaces below the fluid, since it is caused by the weight of fluid pressing down."
  type: true-false
  answer: false
  explanation: "Pressure in a static fluid is isotropic — it acts equally in all directions at any given point. This follows from Pascal's principle: if pressure were not equal in all directions, a fluid element would experience a net force and accelerate, violating the assumption of static equilibrium. A horizontal floor at depth h experiences pressure P₀ + ρgh pushing upward; a vertical wall at the same depth experiences the same pressure pushing horizontally; a ceiling would experience it pushing downward. The direction of the pressure force on a surface is always perpendicular to (normal to) that surface, regardless of the surface's orientation."

- question: "Explain why the hydrostatic pressure at a given depth does not depend on the total volume or shape of the fluid container, even though containers with more fluid have more total weight pressing down."
  type: short-answer
  answer: "The hydrostatic equation P = P₀ + ρgh is derived from a force balance on a thin horizontal slab of fluid: the pressure difference between the top and bottom of the slab must exactly support the slab's weight. This local force balance depends only on the fluid density and the height of the slab, not on what's happening elsewhere in the container. When the container is wider, the sidewalls — whether sloped, curved, or vertical — bear the additional weight of extra fluid through normal forces; this weight is not transmitted to the bottom. The result is that only the vertical column of fluid directly above any point determines the pressure at that point."
  explanation: "The key is that the hydrostatic derivation is local — it applies to a differential element of fluid and integrates upward, accumulating the weight of each successive layer. Container geometry affects where walls can support weight but not the vertical pressure gradient dP/dh = ρg. This locality is also why different fluids stacked in layers can be analyzed independently, and why density (not total mass) is the relevant fluid property."
```

## Explainer

You already know that pressure is force per unit area, and that in a static fluid, pressure at a point is isotropic — it acts equally in all directions. This follows from Pascal's principle: if it didn't, a tiny fluid element would accelerate in the direction of the pressure imbalance, and the fluid wouldn't be static. The question then is: how does pressure change from point to point in a motionless fluid? The answer follows from a simple force balance on a column of fluid.

Imagine isolating a thin horizontal slab of fluid at depth h below the surface. The fluid above it exerts a downward pressure, and the fluid below exerts an upward pressure. For the slab to remain stationary, the pressure difference between top and bottom must exactly support the weight of the slab. Working this out gives dP/dh = ρg — pressure increases linearly with depth in an incompressible fluid of uniform density. Integrating from the surface gives **P = P₀ + ρgh**, where P₀ is the pressure at the free surface (usually atmospheric), ρ is the fluid density, g is gravitational acceleration, and h is the vertical depth below the surface. Three numbers — density, gravity, and depth — determine everything.

The most surprising implication is the **hydrostatic paradox**: pressure at a given depth is completely independent of the container's shape or total volume of fluid above. A 1-centimeter-diameter pipe filled with water to 10 meters produces the same pressure at the bottom as an Olympic swimming pool of the same depth. This seems counterintuitive — the swimming pool has vastly more water pressing down — but the sidewalls of the wider container support the excess weight. Pressure depends only on the vertical height of fluid, not on how much total fluid is present. This is why manometers can measure pressure using only a small U-shaped tube: the height difference in the fluid column directly encodes the pressure difference.

The omnidirectional nature of pressure means it acts perpendicular to any surface it contacts, regardless of that surface's orientation. A horizontal floor at depth h experiences pressure P₀ + ρgh pushing upward; a vertical wall at that same depth experiences the same pressure pushing horizontally. This matters enormously for engineering design: the net hydrostatic force on a dam wall, for example, must be computed by integrating the linearly varying pressure distribution over the entire submerged face — a calculation that builds directly on the linear P(h) relationship established here.
