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

## Questions

```yaml
- question: "A hydraulic jack has a small piston of area 10 cm² and a large piston of area 1,000 cm². A force of 50 N is applied to the small piston. What force does the large piston exert?"
  type: multiple-choice
  options:
    - "50 N — force is conserved in a closed hydraulic system"
    - "0.5 N — the pressure is distributed over a larger area, reducing force"
    - "5,000 N — pressure is transmitted equally throughout the fluid (Pascal's principle)"
    - "5,000 N only if both pistons are at the same height"
  answer: 2
  explanation: "Pascal's principle: pressure applied at one point in a static connected fluid is transmitted equally to all other points. Pressure at small piston = 50 N / 0.001 m² = 50,000 Pa. The large piston (0.1 m²) experiences the same pressure: F = 50,000 × 0.1 = 5,000 N. This 100× mechanical advantage is how hydraulic jacks, brakes, and presses work. Option A confuses force with pressure; pressure (not force) is what transmits equally."

- question: "A flat rectangular gate is mounted vertically in a dam, with its top edge at the water surface. Where does the resultant hydrostatic force on the gate act?"
  type: multiple-choice
  options:
    - "At the geometric centroid of the gate — the midpoint of the vertical dimension"
    - "Above the centroid — water pressure is highest at the surface where most water contacts the gate"
    - "Below the centroid — deeper portions experience higher pressure and contribute more force"
    - "Uniformly across the gate — pressure is isotropic so no single point of application exists"
  answer: 2
  explanation: "Hydrostatic pressure increases linearly with depth (P = P₀ + ρgh), so the bottom of a vertical gate is under higher pressure than the top. The resultant force is the integral of pressure over area, weighted toward the deeper, higher-pressure portions. This shifts the center of pressure below the geometric centroid. Designing gates and dam faces requires finding this center of pressure — not the centroid — to correctly place structural supports."

- question: "In a fluid at rest, pressure acts more strongly in the downward (vertical) direction than horizontally, because gravity is what creates the pressure."
  type: true-false
  answer: false
  explanation: "Pressure in a static fluid is isotropic — at any given point and depth, it acts equally in all directions. Gravity causes pressure to increase with depth, but at a specific depth the pressure magnitude is the same whether you measure it acting upward, downward, or sideways. This isotropy is what allows pressure to transmit through a fluid in all directions, which is the basis for Pascal's principle and hydraulic machines. It distinguishes pressure in fluids from directed forces in solids."

- question: "Gauge pressure equals absolute pressure minus atmospheric pressure."
  type: true-false
  answer: true
  explanation: "Absolute pressure is measured from perfect vacuum. Gauge pressure subtracts atmospheric pressure (the reference the gauge experiences on its exterior), so gauge = absolute − atmospheric. A tire at '32 psi gauge' has absolute pressure of roughly 32 + 14.7 ≈ 46.7 psi. In engineering calculations involving forces on surfaces exposed to atmosphere on one side, gauge pressures automatically cancel the atmospheric contribution, simplifying the math — which is why gauge pressure is the working standard."

- question: "Why must a dam be structurally stronger (thicker or more reinforced) at its base than at its top, even though the dam surface area is the same at all depths?"
  type: short-answer
  answer: "Because hydrostatic pressure increases linearly with depth: P = P₀ + ρgh. The water at the base of the dam exerts far greater pressure per unit area than water near the surface. Since force equals pressure times area, and the area is the same at every depth, the force on base sections is proportionally larger. The base must resist this greater force, requiring greater structural strength than the top."
  explanation: "This is a direct application of the hydrostatic pressure distribution. At the water surface h = 0, so pressure equals atmospheric. At depth h, pressure has increased by ρgh — for a 30m dam with water (ρ = 1000 kg/m³), that's an additional ~294,000 Pa at the base. The force on a 1 m² section at the base is roughly 294 kN more than at the surface. Ignoring this gradient would lead to catastrophic structural failure at the base, as famously illustrated in historical dam failures."
```

## Explainer

The defining feature of pressure in a fluid — and what distinguishes it from forces in solid mechanics — is its **isotropy**: in a fluid at rest, pressure at any point acts equally in all directions. Push on a solid block and the force has a direction. Apply pressure to a fluid and it transmits to every surrounding surface regardless of orientation. This is Pascal's principle, and it underlies the entire field of hydraulics: a pressure applied at one piston in a connected fluid system is felt equally at every other piston, regardless of path or orientation. A small piston with a large pressure can generate a large force on a big piston — the basis for hydraulic jacks, brakes, and presses.

The relationship between pressure and depth in a static fluid follows directly from force balance. Consider a thin horizontal slice of fluid at depth h: it must support the weight of all fluid above it. The weight per unit area of that fluid column is ρgh (density × gravitational acceleration × height), so pressure increases with depth as P = P₀ + ρgh, where P₀ is the surface pressure. This **hydrostatic pressure distribution** is linear in depth for a fluid of uniform density. It explains why a dam must be thicker at the base than the top, why deep-sea vehicles require pressure-resistant hulls, and why mercury manometers measure pressure differences as height differences.

To find the **force on a submerged surface**, integrate the pressure over the surface area. For a flat horizontal surface at uniform depth, F = P × A. For an angled or vertical surface, the pressure varies across the surface (deeper parts experience higher pressure), so both the magnitude and line of action of the resultant force must be calculated by integration. The resultant force does not act at the centroid of the area — it acts at the **center of pressure**, which lies below the centroid because the deeper, higher-pressure portion of the surface contributes more force.

Engineering practice distinguishes **gauge pressure** from **absolute pressure**. Absolute pressure is measured from perfect vacuum; gauge pressure subtracts atmospheric pressure (approximately 101.3 kPa at sea level). Pressure gauges measure gauge pressure by default because they sense the difference between the fluid pressure and the surrounding atmosphere. A tire "inflated to 32 psi" has 32 psi gauge, or about 46.7 psi absolute. When calculating pressure differences that drive fluid motion or forces on surfaces exposed to atmosphere on one side, gauge pressures cancel the atmospheric contribution automatically — which is why gauge pressure is the standard working unit in most fluid engineering calculations.
