---
id: buoyancy-and-archimedes
title: Buoyancy and Archimedes' Principle
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-statics-pressure
  type: hard
builds-toward:
- hydrostatic-forces-on-surfaces
tags:
- buoyancy
- Archimedes
- flotation
- submerged bodies
stage: advanced
status: validated
---

# Buoyancy and Archimedes' Principle

## Core Idea
Archimedes' principle states that a body submerged or floating in a fluid experiences an upward buoyant force equal to the weight of fluid displaced. The buoyant force acts through the center of buoyancy, which is the centroid of the displaced fluid volume. For flotation, the weight of the object equals the weight of fluid displaced, setting the draft depth.

## How It's Best Learned
Derive the buoyant force by integrating hydrostatic pressure over the submerged surface, then verify it equals ρ_fluid × g × V_displaced. Apply to objects of varying density to predict sinking, floating, or neutral buoyancy before checking with physical experiments.

## Common Misconceptions
- Buoyancy depends on the displaced fluid volume, not the object's volume if only partially submerged.
- A denser object can float if shaped to displace enough fluid (e.g., a steel ship).
- The buoyant force is unchanged whether the object is at different depths, as long as it remains fully submerged in an incompressible fluid.

## Explainer

From your study of fluid statics, you know that pressure in a fluid increases linearly with depth: p = p_0 + ρ_f g h. This single fact is all you need to derive Archimedes' principle from scratch. Imagine a rectangular block submerged with its top face at depth h_1 and bottom face at depth h_2 = h_1 + H. The downward pressure on the top face is ρ_f g h_1 per unit area; the upward pressure on the bottom face is ρ_f g h_2 per unit area. Multiplying by the face area A, the net upward force is ρ_f g (h_2 − h_1) A = ρ_f g H A = ρ_f g V — exactly the weight of fluid that would occupy the displaced volume V. The derivation works for any shape because the pressure field doesn't know what object is there; it only responds to depth.

The **buoyant force** F_b = ρ_f g V_displaced acts upward through the **center of buoyancy**, which is the centroid of the displaced fluid volume. Compare this to the object's weight, which acts downward through its center of mass. For a uniform object of density ρ_obj, equilibrium requires F_b = W, giving ρ_f g V_displaced = ρ_obj g V_obj. For a fully submerged object, V_displaced = V_obj, so the condition for floating is simply ρ_obj < ρ_f. If ρ_obj = ρ_f, the object achieves **neutral buoyancy** — it neither sinks nor rises — the principle behind submarines adjusting ballast.

For a partially submerged object (a floating boat, an iceberg), only the fraction below the waterline displaces fluid. Setting weight equal to buoyant force: ρ_obj V_obj g = ρ_f V_submerged g, so V_submerged / V_obj = ρ_obj / ρ_f. An iceberg, with ρ_ice ≈ 917 kg/m³ in seawater with ρ_f ≈ 1025 kg/m³, floats with about 89% of its volume submerged — which is where "tip of the iceberg" comes from. A steel ship seems paradoxical until you account for the enclosed air: the average density of the hull, machinery, cargo, and trapped air together is less than water, so the ship displaces its weight before sinking.

One subtlety worth holding onto: the buoyant force depends on the volume of fluid displaced, not on the object's volume alone. A hollow sphere partially filled with water displaces a volume equal to the outer dimensions of the submerged portion, not the volume of material. This is why a ship's load capacity is determined by how deeply it can sink before the deck goes under — more cargo means more displacement until the buoyant force still equals total weight at the maximum allowable draft.
