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

## Questions

```yaml
- question: "A solid steel ball and a large steel cargo ship have the same total mass. The ball sinks; the ship floats. What is the correct explanation?"
  type: multiple-choice
  options:
    - "The ship is made of a different, lower-density alloy than the solid ball"
    - "The ship's large surface area increases drag, slowing its descent and keeping it afloat"
    - "The ship is hollow — the average density of the hull, enclosed air, and cargo together is less than water, so the ship displaces its weight in water before sinking"
    - "The buoyant force on the ship is greater because its bottom surface area is larger, amplifying the upward pressure"
  answer: 2
  explanation: "Buoyancy depends on the weight of fluid displaced, not on the object's material density in isolation. A solid steel ball has an average density (~7800 kg/m³) far above water, so it sinks before displacing its own weight. A steel ship is hollow: the enclosed volume of air brings the average density of the entire system (hull + air + cargo) below ~1000 kg/m³. As the ship settles, it displaces water until the displaced water's weight equals the ship's total weight — and it floats. Option D is wrong because buoyancy depends on displaced *volume*, not surface area in contact with fluid."

- question: "A submarine is fully submerged at 50 m depth in seawater (treated as incompressible). It descends to 200 m without changing its volume. How does the buoyant force change?"
  type: multiple-choice
  options:
    - "It increases significantly — hydrostatic pressure is much higher at 200 m, increasing the upward force"
    - "It remains the same — for an incompressible fluid, buoyant force equals ρ_fluid × g × V_displaced and is independent of depth"
    - "It decreases — the greater water pressure at depth compresses the submarine slightly, reducing displaced volume"
    - "It increases because the water is slightly denser at depth, increasing the weight of the displaced fluid"
  answer: 1
  explanation: "Archimedes' principle: F_b = ρ_fluid × g × V_displaced. For an incompressible fluid, ρ_fluid and g are constant, and V_displaced is fixed (submarine volume unchanged). The buoyant force is therefore constant regardless of depth. While pressure increases with depth, the key insight is that pressure increases equally on all faces — the net upward force (bottom pressure minus top pressure) depends only on the depth *difference* across the object (equal to its height), not on the absolute depth. For an incompressible fluid this depth difference and ρ_fluid are constant. (Option D is technically true at very large depths, but negligible for this context.)"

- question: "An iceberg floats with approximately 89% of its volume submerged because the ratio V_submerged/V_total equals ρ_ice/ρ_seawater ≈ 917/1025."
  type: true-false
  answer: true
  explanation: "For a floating object, weight equals buoyant force: ρ_obj × V_obj × g = ρ_fluid × V_submerged × g. Rearranging: V_submerged/V_obj = ρ_obj/ρ_fluid = 917/1025 ≈ 0.894, confirming that ~89% is submerged and ~11% is above water. This is a direct consequence of Archimedes' principle applied to partial submersion. The iceberg keeps sinking until the weight of displaced seawater exactly equals the weight of the entire iceberg."

- question: "The buoyant force on a submerged object increases as the object sinks deeper, because the hydrostatic pressure surrounding the object increases with depth."
  type: true-false
  answer: false
  explanation: "For an incompressible fluid, the buoyant force is F_b = ρ_fluid × g × V_displaced — it depends only on the displaced volume, not on depth. As an object descends, pressure increases on all surfaces, but the pressure on the bottom face increases by exactly the same amount as the pressure on the top face, so the net upward force (their difference integrated over the surfaces) remains constant. This is derivable from the pressure-depth relationship: the net upward force equals ρ_f × g × H × A = ρ_f × g × V, where H is the object's height — independent of the absolute depth to the top or bottom."

- question: "Using the concept of displaced fluid weight, explain why a large steel cargo ship floats even though solid steel is about 8 times denser than water."
  type: short-answer
  answer: "The buoyant force equals the weight of fluid displaced — not the weight of the ship's steel, and not any property of the steel's density alone. A cargo ship is hollow: its hull encloses a large volume of air and cargo space. The *average* density of the entire system (steel hull + air + any cargo) can be less than the density of water. As the ship is lowered into water, it displaces an increasing volume of water. It stops sinking (reaches equilibrium) when the weight of displaced water equals the ship's total weight. For a steel ship, this happens before the deck goes underwater because the enclosed air volume is large enough that the average density of the ship falls below water density. The ship's maximum load capacity is determined by how deep it can settle before flooding — at maximum draft, buoyancy force still equals total weight."
  explanation: "The key insight is that Archimedes' principle applies to the displaced volume — the volume swept out by the submerged portion of the hull — not to the volume of steel material. A hollow object displaces far more water than a solid object of the same mass and material, which is why the shape matters: a steel sphere sinks, but the same steel formed into a bowl shape floats."
```

## Explainer

From your study of fluid statics, you know that pressure in a fluid increases linearly with depth: p = p_0 + ρ_f g h. This single fact is all you need to derive Archimedes' principle from scratch. Imagine a rectangular block submerged with its top face at depth h_1 and bottom face at depth h_2 = h_1 + H. The downward pressure on the top face is ρ_f g h_1 per unit area; the upward pressure on the bottom face is ρ_f g h_2 per unit area. Multiplying by the face area A, the net upward force is ρ_f g (h_2 − h_1) A = ρ_f g H A = ρ_f g V — exactly the weight of fluid that would occupy the displaced volume V. The derivation works for any shape because the pressure field doesn't know what object is there; it only responds to depth.

The **buoyant force** F_b = ρ_f g V_displaced acts upward through the **center of buoyancy**, which is the centroid of the displaced fluid volume. Compare this to the object's weight, which acts downward through its center of mass. For a uniform object of density ρ_obj, equilibrium requires F_b = W, giving ρ_f g V_displaced = ρ_obj g V_obj. For a fully submerged object, V_displaced = V_obj, so the condition for floating is simply ρ_obj < ρ_f. If ρ_obj = ρ_f, the object achieves **neutral buoyancy** — it neither sinks nor rises — the principle behind submarines adjusting ballast.

For a partially submerged object (a floating boat, an iceberg), only the fraction below the waterline displaces fluid. Setting weight equal to buoyant force: ρ_obj V_obj g = ρ_f V_submerged g, so V_submerged / V_obj = ρ_obj / ρ_f. An iceberg, with ρ_ice ≈ 917 kg/m³ in seawater with ρ_f ≈ 1025 kg/m³, floats with about 89% of its volume submerged — which is where "tip of the iceberg" comes from. A steel ship seems paradoxical until you account for the enclosed air: the average density of the hull, machinery, cargo, and trapped air together is less than water, so the ship displaces its weight before sinking.

One subtlety worth holding onto: the buoyant force depends on the volume of fluid displaced, not on the object's volume alone. A hollow sphere partially filled with water displaces a volume equal to the outer dimensions of the submerged portion, not the volume of material. This is why a ship's load capacity is determined by how deeply it can sink before the deck goes under — more cargo means more displacement until the buoyant force still equals total weight at the maximum allowable draft.
