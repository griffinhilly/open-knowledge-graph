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
stage: advanced
status: draft
---

# Prandtl-Meyer Expansion Function and Expansion Fan Theory

## Core Idea
When supersonic flow expands smoothly through an external corner, Mach number increases across a Prandtl-Meyer expansion fan with isentropic deceleration and entropy constant. The Prandtl-Meyer function ν(M) relates Mach number to expansion angle; tables or functions provide Mach number at any expansion angle. Expansion fans are complementary to shocks and appear in supersonic nozzles, inlets, and high-altitude aerodynamic applications.

## Questions

```yaml
- question: "Supersonic flow at M₁ = 2.0 encounters a 15° convex corner. A student claims the total pressure drops across this expansion, just as it drops across an oblique shock of similar turning angle. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes, because any supersonic flow turning event involves entropy generation regardless of whether it is a shock or fan"
    - "No, the Prandtl-Meyer expansion fan is isentropic; total pressure is preserved and entropy does not increase"
    - "No, but total temperature drops across the expansion fan even though total pressure is preserved"
    - "Yes, because the expansion fan consists of many individual Mach waves, each generating a small entropy increase that accumulates"
  answer: 1
  explanation: "This is the key distinction between shocks and expansion fans. A shock is an irreversible compression — it converts kinetic energy to thermal energy through a discontinuity, increasing entropy and dropping total pressure. A Prandtl-Meyer expansion is a smooth, reversible acceleration through infinitesimal Mach waves; each individual turning is isentropic, and the cumulative process is isentropic. Total pressure, total temperature, and entropy are all conserved across the fan. This is why expansion fan analysis is simpler than shock analysis: isentropic relations apply directly downstream."

- question: "How is the downstream Mach number M₂ found after supersonic flow turns through a convex corner of angle θ?"
  type: multiple-choice
  options:
    - "Apply the normal shock table at M₁ with the given pressure ratio to find the equivalent downstream Mach number"
    - "Apply the Rayleigh flow equations for heat addition equivalent to the turning angle"
    - "Compute ν(M₂) = ν(M₁) + θ using the Prandtl-Meyer function, then invert the function to find M₂"
    - "Use the Bernoulli equation modified for compressible flow with a correction factor for the turning angle"
  answer: 2
  explanation: "The Prandtl-Meyer function ν(M) encodes how much total turning a flow has undergone to accelerate from M = 1 to a given Mach number. Adding the wall turning angle θ directly gives the new function value: ν(M₂) = ν(M₁) + θ. Looking up (or solving for) the Mach number corresponding to ν(M₂) gives M₂. Because the process is isentropic, standard isentropic flow tables then yield all downstream properties (pressure, temperature, density ratios) from M₂ alone — no shock relations or entropy corrections are needed."

- question: "A Prandtl-Meyer expansion fan can only occur when the incoming flow is supersonic (M > 1)."
  type: true-false
  answer: true
  explanation: "Prandtl-Meyer expansion fans require supersonic flow. In subsonic flow, pressure disturbances propagate upstream faster than the flow itself, allowing the flow to 'sense' and smoothly negotiate a corner without forming a fan. In supersonic flow, information cannot travel upstream (beyond the Mach angle); when the flow encounters a convex corner, it adjusts through a fan of Mach waves emanating from the corner tip, each turning and accelerating the flow by an infinitesimal amount. At M < 1, the flow adjusts continuously; the expansion fan is strictly a supersonic phenomenon."

- question: "Both oblique shocks and Prandtl-Meyer expansion fans turn the flow direction and preserve total pressure across the wave system."
  type: true-false
  answer: false
  explanation: "Only Prandtl-Meyer expansion fans preserve total pressure — they are isentropic. Oblique shocks turn the flow (through a compression) and irreversibly increase entropy, which by definition reduces total pressure. The stronger the shock (larger turning angle or higher upstream Mach number), the greater the total pressure loss. This is why nozzle and inlet designers work to avoid shocks: total pressure recovery directly affects thrust efficiency in propulsion applications. Expansion fans are thermodynamically ideal; shocks are not."

- question: "Explain why a Prandtl-Meyer expansion is described as the 'thermodynamic opposite' of a shock, and what physical consequence follows from this for calculating downstream flow properties."
  type: short-answer
  answer: "A shock is an irreversible compression: kinetic energy is converted to heat through a discontinuity, entropy increases, and total pressure drops. A Prandtl-Meyer expansion is a smooth, reversible acceleration through an infinite number of infinitesimal Mach waves — each turning the flow by an infinitesimal angle with zero entropy generation. Total pressure, total temperature, and entropy are all conserved. The consequence is that after an expansion fan, you can apply standard isentropic flow relations with the known total conditions and the calculated downstream Mach number M₂ to find all downstream properties directly, without any separate entropy or pressure-loss calculation."
  explanation: "The isentropic nature of expansion fans is not merely a mathematical convenience — it reflects the physical reality that smooth, gradual acceleration does no irreversible work. This makes expansion fans analytically clean: once you find M₂ from ν(M₂) = ν(M₁) + θ, the problem reduces to a simple isentropic flow table lookup. Shocks require separate shock tables that account for the entropy increase; expansion fans do not."
```

## Explainer

From isentropic flow with area change, you already know that supersonic flow accelerates when a channel diverges — increasing area means increasing Mach number above M = 1. A **Prandtl-Meyer expansion fan** is the two-dimensional analog: when supersonic flow encounters a convex corner (a wall that turns away from the flow), the flow must turn and accelerate through a fan of infinitesimal **Mach waves** radiating from the corner tip. Each Mach wave in the fan turns the flow by an infinitesimal angle and increases the Mach number by an infinitesimal amount. The cumulative effect across the fan can produce dramatic Mach number increases.

The critical distinction from a normal or oblique shock is that this process is **isentropic**. A shock is a compression — it irreversibly increases entropy and drops total pressure. An expansion fan is the thermodynamic opposite: it is a smooth, reversible acceleration. Total pressure, total temperature, and entropy are all preserved across the fan. This makes the Prandtl-Meyer expansion the ideal tool for analyzing the supersonic portions of nozzles and external aerodynamic surfaces where efficiency matters.

The **Prandtl-Meyer function** ν(M) is derived by integrating the relationship between flow turning and Mach number change across each infinitesimal Mach wave in the fan. For a given ratio of specific heats γ, ν(M) is a specific closed-form expression (involving arctangent terms). Its practical value is the simple relationship it provides: if upstream Mach number is M₁ and the wall turns through angle θ, then the downstream Mach number M₂ satisfies ν(M₂) = ν(M₁) + θ. Look up ν(M₁) in tables or compute it, add the turning angle θ (in degrees), and look up the Mach number that corresponds to the result. Since the process is isentropic, standard isentropic flow tables then give you the downstream pressure, temperature, and density ratios from M₂ alone.

Consider a concrete example: supersonic flow at M₁ = 2.0 encounters a 15° convex corner. From tables, ν(2.0) ≈ 26.4°. Adding the 15° turning angle gives ν(M₂) = 41.4°, which from the Prandtl-Meyer table corresponds to M₂ ≈ 2.77. The flow has accelerated substantially, and the downstream pressure has dropped. This calculation is the workhorse for analyzing **supersonic nozzle contours**, **airfoil surface flow**, and the complex wave patterns (alternating shocks and expansion fans) that appear in under- or over-expanded rocket plumes and supersonic jets at off-design conditions.
