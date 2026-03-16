---
id: prandtl-meyer-expansion-function-tables
title: Prandtl-Meyer Expansion Function and Expansion Fan Theory
domain: engineering
course: fluid-mechanics
prerequisites:
- id: isentropic-flow-with-area-change
  type: hard
- id: mach-number-compressibility-effects
  type: hard
tags:
- expansion
- isentropic
- mach-number
stage: formal-systems
status: draft
---

# Prandtl-Meyer Expansion Function and Expansion Fan Theory

## Core Idea
When supersonic flow expands smoothly through an external corner, Mach number increases across a Prandtl-Meyer expansion fan with isentropic deceleration and entropy constant. The Prandtl-Meyer function ν(M) relates Mach number to expansion angle; tables or functions provide Mach number at any expansion angle. Expansion fans are complementary to shocks and appear in supersonic nozzles, inlets, and high-altitude aerodynamic applications.

## Explainer

From isentropic flow with area change, you already know that supersonic flow accelerates when a channel diverges — increasing area means increasing Mach number above M = 1. A **Prandtl-Meyer expansion fan** is the two-dimensional analog: when supersonic flow encounters a convex corner (a wall that turns away from the flow), the flow must turn and accelerate through a fan of infinitesimal **Mach waves** radiating from the corner tip. Each Mach wave in the fan turns the flow by an infinitesimal angle and increases the Mach number by an infinitesimal amount. The cumulative effect across the fan can produce dramatic Mach number increases.

The critical distinction from a normal or oblique shock is that this process is **isentropic**. A shock is a compression — it irreversibly increases entropy and drops total pressure. An expansion fan is the thermodynamic opposite: it is a smooth, reversible acceleration. Total pressure, total temperature, and entropy are all preserved across the fan. This makes the Prandtl-Meyer expansion the ideal tool for analyzing the supersonic portions of nozzles and external aerodynamic surfaces where efficiency matters.

The **Prandtl-Meyer function** ν(M) is derived by integrating the relationship between flow turning and Mach number change across each infinitesimal Mach wave in the fan. For a given ratio of specific heats γ, ν(M) is a specific closed-form expression (involving arctangent terms). Its practical value is the simple relationship it provides: if upstream Mach number is M₁ and the wall turns through angle θ, then the downstream Mach number M₂ satisfies ν(M₂) = ν(M₁) + θ. Look up ν(M₁) in tables or compute it, add the turning angle θ (in degrees), and look up the Mach number that corresponds to the result. Since the process is isentropic, standard isentropic flow tables then give you the downstream pressure, temperature, and density ratios from M₂ alone.

Consider a concrete example: supersonic flow at M₁ = 2.0 encounters a 15° convex corner. From tables, ν(2.0) ≈ 26.4°. Adding the 15° turning angle gives ν(M₂) = 41.4°, which from the Prandtl-Meyer table corresponds to M₂ ≈ 2.77. The flow has accelerated substantially, and the downstream pressure has dropped. This calculation is the workhorse for analyzing **supersonic nozzle contours**, **airfoil surface flow**, and the complex wave patterns (alternating shocks and expansion fans) that appear in under- or over-expanded rocket plumes and supersonic jets at off-design conditions.
