---
id: static-and-dynamic-pressure
title: Static and Dynamic Pressure
domain: engineering
course: fluid-mechanics
prerequisites:
- id: pressure-and-forces-in-fluids
  type: hard
- id: bernoullis-equation
  type: soft
builds-toward:
- pitot-tube-velocity-measurement
- absolute-gauge-atmospheric-pressure
tags:
- pressure
- flow
- measurement
stage: formal-systems
status: validated
---

# Static and Dynamic Pressure

## Core Idea
Static pressure is the pressure of a fluid at rest or the component of pressure independent of motion, while dynamic pressure represents the kinetic energy per unit volume of moving fluid. The sum of static and dynamic pressure (plus elevation effects) is constant along a streamline for incompressible inviscid flow, forming the basis of Bernoulli's equation.

## How It's Best Learned
Compare a manometer reading taken when a Pitot tube faces the flow (stagnation pressure) versus when a static pressure tap is used perpendicular to flow. The difference directly demonstrates dynamic pressure and Bernoulli's principle in action.

## Common Misconceptions
- Dynamic pressure is a different type of pressure added to static pressure (it is actually the kinetic energy density per unit volume, derived from Bernoulli's energy balance).
- Static pressure is zero in a moving fluid (static pressure is always present; it is measured by pressure taps perpendicular to flow).

## Questions

```yaml
- question: "Air (density 1.2 kg/m³) flows through a duct at 50 m/s. A static pressure tap perpendicular to the flow reads 100,000 Pa. A Pitot tube facing into the flow is installed at the same location. What pressure does the Pitot tube read?"
  type: multiple-choice
  options:
    - "100,000 Pa — the Pitot tube measures static pressure, same as the wall tap"
    - "101,500 Pa — stagnation pressure equals static pressure plus dynamic pressure (½ρV² = ½ × 1.2 × 2500 = 1,500 Pa)"
    - "97,000 Pa — the Pitot tube measures dynamic pressure only, which is less than static pressure"
    - "50,000 Pa — dynamic pressure is half the static pressure at this flow speed"
  answer: 1
  explanation: "Stagnation pressure = static pressure + dynamic pressure = P_static + ½ρV² = 100,000 + ½(1.2)(50²) = 100,000 + 1,500 = 101,500 Pa. The Pitot tube brings the flow to rest at its tip, converting all kinetic energy to pressure. The static tap measures pressure without decelerating the flow. The difference (1,500 Pa) is the dynamic pressure. This is exactly how airspeed is measured: V = √(2(P_stag − P_static)/ρ). Option A is the key misconception to avoid — Pitot tubes and static taps measure fundamentally different quantities."

- question: "A student argues: 'In very fast-moving air, all the pressure has been converted to kinetic energy, so the static pressure must be nearly zero.' What is the fundamental error in this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — at very high velocities, static pressure approaches zero as kinetic energy dominates"
    - "The error is that static pressure is always present in a moving fluid; dynamic pressure represents additional kinetic energy that becomes pressure only when the flow decelerates to rest — the two coexist at all nonzero velocities"
    - "The error is that kinetic energy and pressure are measured in different units and cannot be compared directly"
    - "The student is almost correct, but static pressure approaches zero only at supersonic speeds, not subsonic speeds"
  answer: 1
  explanation: "Static pressure is an inherent property of the fluid related to molecular motion — it is always present whether the fluid moves or not. Dynamic pressure ½ρV² is the kinetic energy per unit volume of the bulk flow, and it represents additional pressure that appears *only when the flow is brought to rest* (at a stagnation point). In a moving fluid, both exist simultaneously: the static pressure acts on surfaces parallel to the flow, and the stagnation pressure (static + dynamic) acts on surfaces facing the flow. Bernoulli's equation says their sum is conserved along a streamline — not that one replaces the other."

- question: "Dynamic pressure is a type of pressure that moving fluids exert in the direction perpendicular to the flow, in addition to the static pressure they exert on most surfaces."
  type: true-false
  answer: false
  explanation: "Dynamic pressure ½ρV² is not a separate force on surfaces perpendicular to flow — it is the kinetic energy per unit volume of the bulk motion. It only manifests as an actual pressure increase on surfaces that bring the flow to rest (stagnation surfaces, like the tip of a Pitot tube or the leading edge of an airfoil). On surfaces parallel to the flow (static pressure taps), only static pressure acts. Calling dynamic pressure a 'type of pressure on perpendicular surfaces' confuses the energy quantity with the stagnation effect."

- question: "In ideal (inviscid, incompressible) flow along a streamline, a region where the fluid moves faster has lower static pressure than a region where it moves slower."
  type: true-false
  answer: true
  explanation: "This is a direct statement of Bernoulli's equation: P + ½ρV² = constant along a streamline. If velocity increases (½ρV² increases), static pressure P must decrease to keep the sum constant. This principle explains lift on airfoils (faster flow over the curved top surface lowers pressure above the wing), flow through constrictions (higher velocity in a narrowed pipe means lower static pressure — the Venturi effect), and many other phenomena. The key qualifier is 'along a streamline' for inviscid, incompressible, steady flow."

- question: "Why does a Pitot tube measure stagnation pressure rather than static pressure, and how is fluid velocity derived from these two measurements?"
  type: short-answer
  answer: "A Pitot tube faces directly into the oncoming flow. The fluid approaching the tube's opening is decelerated to zero velocity at the tip — a stagnation point. At a stagnation point, all kinetic energy converts to pressure, so the pressure rises from static pressure to stagnation pressure (P_stag = P_static + ½ρV²). A separate static port (a tap perpendicular to the flow, where fluid is not decelerated) measures static pressure alone. The velocity is then derived from the difference: V = √(2(P_stag − P_static)/ρ). The two measurements together isolate the dynamic pressure ½ρV², from which velocity follows."
  explanation: "This measurement strategy directly embodies the distinction between static and dynamic pressure. The Pitot-static system — combining a forward-facing stagnation tube with a static port — is the standard airspeed measurement device in aviation. The same principle operates in industrial flow meters (Pitot probes in ducts) and in research (hot-wire anemometry aside, Pitot tubes remain a standard for velocity measurement). The key insight is that you need both measurements to isolate V; neither alone is sufficient."
```

## Explainer

From your study of pressure in fluids, you know that a fluid exerts force on any surface it contacts, and that pressure is that force per unit area. In a stationary fluid, pressure is the same in all directions at a given depth — it's isotropic. When the fluid moves, this clean picture breaks down in one important way: the pressure you measure depends on whether your measurement surface faces the flow or is aligned with it. That distinction is the heart of this topic.

**Static pressure** is the pressure the fluid exerts on a surface that moves with the fluid — or equivalently, on a surface oriented parallel to the flow direction. It represents the thermal and intermolecular activity of the fluid molecules, independent of their bulk motion. You measure static pressure with a tap drilled perpendicular to the pipe wall, so the flowing fluid slides past it without being slowed down. In the absence of any flow, static pressure is the only pressure; it matches the ambient or gauge pressure you already understand.

**Dynamic pressure** is the additional pressure that arises from bringing a moving fluid to rest. When flow is decelerated to zero velocity — for example, at the front face of a blunt object or inside a forward-facing tube — kinetic energy converts to pressure energy. The amount of pressure gained equals ½ρV², where ρ is the fluid density and V is the flow speed. This quantity has units of pressure (Pa) but physically represents the kinetic energy per unit volume of the moving fluid. It is not "added" to the static pressure in the sense of an extra force; rather, Bernoulli's equation tells us that when velocity decreases, pressure increases by exactly this amount.

The sum of static pressure and dynamic pressure is **stagnation pressure** (also called total pressure): P_stag = P_static + ½ρV². Bernoulli's equation is simply a statement that stagnation pressure is conserved along a streamline in ideal flow. A Pitot tube measures stagnation pressure at its tip (flow comes to rest there) while a separate static port measures static pressure; the velocity follows from V = √(2(P_stag − P_static)/ρ). This is the operational definition that makes the distinction between static and dynamic pressure practically useful — every velocity measurement in a flowing fluid exploits this exact relationship.
