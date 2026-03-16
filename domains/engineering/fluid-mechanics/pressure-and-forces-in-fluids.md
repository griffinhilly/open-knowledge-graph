---
id: pressure-and-forces-in-fluids
title: Pressure and Forces in Fluids
domain: engineering
course: fluid-mechanics
prerequisites:
- id: introduction-to-fluid-mechanics
  type: soft
builds-toward:
- static-and-dynamic-pressure
- hydrostatic-pressure-distribution
tags:
- fundamentals
- statics
- pressure
stage: formal-systems
status: draft
---

# Pressure and Forces in Fluids

## Core Idea
Pressure is the normal force per unit area exerted by a fluid on a surface. In fluids at rest, pressure acts equally in all directions and is a scalar quantity. Pressure differences create forces on submerged surfaces and are the basis for many engineering applications including hydraulic systems and pressure vessels.

## Explainer

The defining feature of pressure in a fluid — and what distinguishes it from forces in solid mechanics — is its **isotropy**: in a fluid at rest, pressure at any point acts equally in all directions. Push on a solid block and the force has a direction. Apply pressure to a fluid and it transmits to every surrounding surface regardless of orientation. This is Pascal's principle, and it underlies the entire field of hydraulics: a pressure applied at one piston in a connected fluid system is felt equally at every other piston, regardless of path or orientation. A small piston with a large pressure can generate a large force on a big piston — the basis for hydraulic jacks, brakes, and presses.

The relationship between pressure and depth in a static fluid follows directly from force balance. Consider a thin horizontal slice of fluid at depth h: it must support the weight of all fluid above it. The weight per unit area of that fluid column is ρgh (density × gravitational acceleration × height), so pressure increases with depth as P = P₀ + ρgh, where P₀ is the surface pressure. This **hydrostatic pressure distribution** is linear in depth for a fluid of uniform density. It explains why a dam must be thicker at the base than the top, why deep-sea vehicles require pressure-resistant hulls, and why mercury manometers measure pressure differences as height differences.

To find the **force on a submerged surface**, integrate the pressure over the surface area. For a flat horizontal surface at uniform depth, F = P × A. For an angled or vertical surface, the pressure varies across the surface (deeper parts experience higher pressure), so both the magnitude and line of action of the resultant force must be calculated by integration. The resultant force does not act at the centroid of the area — it acts at the **center of pressure**, which lies below the centroid because the deeper, higher-pressure portion of the surface contributes more force.

Engineering practice distinguishes **gauge pressure** from **absolute pressure**. Absolute pressure is measured from perfect vacuum; gauge pressure subtracts atmospheric pressure (approximately 101.3 kPa at sea level). Pressure gauges measure gauge pressure by default because they sense the difference between the fluid pressure and the surrounding atmosphere. A tire "inflated to 32 psi" has 32 psi gauge, or about 46.7 psi absolute. When calculating pressure differences that drive fluid motion or forces on surfaces exposed to atmosphere on one side, gauge pressures cancel the atmospheric contribution automatically — which is why gauge pressure is the standard working unit in most fluid engineering calculations.
