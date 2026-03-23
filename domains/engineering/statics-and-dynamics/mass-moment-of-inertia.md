---
id: mass-moment-of-inertia
title: Mass Moment of Inertia
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: area-moment-of-inertia-engineering
  type: hard
- id: parallel-axis-theorem-statics
  type: soft
builds-toward:
- rigid-body-kinetics-force-acceleration
- rigid-body-work-energy
- angular-impulse-momentum
tags:
- dynamics
- moment of inertia
- rotational inertia
- composite bodies
- parallel-axis theorem
stage: formal-systems
status: validated
---

# Mass Moment of Inertia

## Core Idea
The mass moment of inertia I quantifies a body's resistance to angular acceleration about a given axis, playing the same role in rotational dynamics that mass plays in translational dynamics (analogously, ΣM = I*alpha parallels ΣF = ma). It is defined as I = integral of r^2 dm, where r is the perpendicular distance from each mass element to the rotation axis. For common shapes (cylinders, spheres, rods, disks), standard formulas exist for I about the centroidal axis. The parallel-axis theorem for mass, I = I_G + md^2, transfers the moment of inertia from the centroidal axis to any parallel axis at distance d. Composite bodies are handled by summing the transferred moments of inertia of each constituent part.

## How It's Best Learned
Memorize the centroidal mass moments of inertia for standard shapes (slender rod: mL^2/12, solid cylinder: mR^2/2, solid sphere: 2mR^2/5, thin disk: mR^2/2). For composite bodies, apply the parallel-axis theorem to each component and sum. Always verify units (kg*m^2 in SI). Compare mass moment of inertia (units: mass * length^2) to area moment of inertia (units: length^4) to avoid confusing the two.

## Common Misconceptions
- Confusing mass moment of inertia (used in dynamics, units kg*m^2) with area moment of inertia (used in beam bending, units m^4) — they are different physical quantities despite sharing the name.
- Applying the parallel-axis theorem in reverse (subtracting md^2) without verifying that the starting axis passes through the centroid — the theorem only transfers FROM the centroid.
- Forgetting that hollow or composite bodies require careful accounting of subtracted volumes with their own parallel-axis transfers.

## Questions

```yaml
- question: "An engineer calculates the area moment of inertia I_A of a steel beam's cross-section for a bending stress analysis. A colleague then uses the same numerical value to compute angular acceleration via ΣM = Iα. What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — both analyses use the same geometric property of the beam"
    - "Area moment of inertia (units: m⁴, governs bending stiffness) and mass moment of inertia (units: kg·m², governs rotational dynamics) are different physical quantities; plugging one into the other's formula gives incorrect results"
    - "The parallel-axis theorem must be applied to convert the area moment to a mass moment before use"
    - "ΣM = Iα only applies to circular rotating bodies, not to beams"
  answer: 1
  explanation: "This is the most dangerous confusion in dynamics, explicitly identified as the primary misconception for this topic. Area moment of inertia (second moment of area) has units of m⁴ and appears in beam bending formulas (σ = Mc/I, δ = FL³/3EI). Mass moment of inertia has units of kg·m² and appears in rotational dynamics (ΣM = Iα). Despite sharing a name and similar definitions (both involve r² integrated over something), they are fundamentally different quantities. The numerical values are not interchangeable even if an engineer wanted to apply them."

- question: "A hollow cylinder and a solid cylinder have identical total mass and identical outer radius. Which has a larger mass moment of inertia about its central axis?"
  type: multiple-choice
  options:
    - "The solid cylinder — it has more material everywhere, including at large radii"
    - "The hollow cylinder — its mass is concentrated at a larger average radius, and the r² weighting means farther mass contributes much more"
    - "They are equal — same mass and same outer radius means the same I"
    - "The solid cylinder — removing material from the center (to make it hollow) reduces resistance to rotation"
  answer: 1
  explanation: "The definition I = ∫r² dm weights mass by the square of its distance from the axis. A solid cylinder has mass near the center (small r, small contribution) and at the edges. A hollow cylinder concentrates all its mass at large r, where the r² multiplier is greatest. For a solid disk, I = mR²/2; for a thin hollow cylinder (all mass at radius R), I = mR². Same mass, same outer radius, but I differs by a factor of 2. This quadratic weighting is why hollow shafts and spoked wheels can achieve high rotational inertia with less material."

- question: "The parallel-axis theorem I = I_G + md² allows you to transfer a moment of inertia from a centroidal axis to any parallel axis at distance d, but you must start with the centroidal value — the theorem only works in this direction."
  type: true-false
  answer: true
  explanation: "The parallel-axis theorem adds md² to shift away from the centroid. To find I_G from a known I at some other axis, you reverse it: I_G = I − md². But this reversal requires that you know I at a non-centroidal axis. The misconception is applying the theorem without verifying the starting axis passes through the centroid — if you mistakenly add md² to a non-centroidal I, you get a value that corresponds to no physically meaningful axis."

- question: "A steel I-beam and an aluminum I-beam with identical cross-sectional geometry have the same mass moment of inertia because their shapes are identical."
  type: true-false
  answer: false
  explanation: "Mass moment of inertia (I = ∫r² dm) depends on both geometry and mass distribution. Two beams with identical geometry but different materials have different densities, so their mass elements dm differ at every point. Steel is approximately 2.9 times denser than aluminum, so the steel beam has a much larger mass moment of inertia for the same shape. Area moment of inertia (∫r² dA) would be identical for both beams with the same geometry — it depends only on shape, not material."

- question: "Why does the location of mass relative to the rotation axis matter quadratically — not linearly — in determining mass moment of inertia?"
  type: short-answer
  answer: "The definition I = ∫r² dm weights each mass element by the square of its distance r from the axis. This quadratic dependence comes from the physics of rotation: the kinetic energy of a rotating body is (1/2)Iω², and each mass element contributes (1/2)(dm)v² = (1/2)(dm)(rω)² = (1/2)r²(dm)ω². The r² factor appears because velocity in circular motion is v = rω — farther mass moves faster for the same angular velocity. Doubling the radius of a mass element quadruples its kinetic energy contribution and therefore quadruples its contribution to I. This is why geometry dominates: redistributing mass farther from the axis dramatically increases I even without changing total mass."
  explanation: "The practical consequence is enormous in engineering design. A flywheel stores rotational kinetic energy proportional to I — concentrating mass at the rim (large r) maximizes energy storage per unit mass. Conversely, reducing r² contributions by moving mass toward the axis reduces I and makes a body easier to accelerate rotationally. This principle governs design of everything from figure skater spin poses to automotive crankshafts."
```

## Explainer

You already know the **area moment of inertia** I = ∫r² dA from statics — it measures how a cross-section's area is distributed around an axis and governs beam bending stiffness. The **mass moment of inertia** follows exactly the same mathematical logic, but replaces area elements dA with mass elements dm: I = ∫r² dm. The conceptual role also parallels: just as area moment resists bending, mass moment resists angular acceleration. In the rotational analog of Newton's second law, ΣM = Iα, the mass moment of inertia I plays precisely the role that mass m plays in ΣF = ma.

The definition I = ∫r² dm reveals why geometry matters so much: mass far from the axis contributes quadratically, not linearly. A hollow cylinder and a solid cylinder of equal mass and outer radius have very different moments of inertia — the hollow cylinder has more because its mass is concentrated at large r. For a solid disk of mass m and radius R, I_G = mR²/2; for a thin rod rotating about its end, I = mL²/3. These formulas are derived by setting up the integral over appropriate geometry. For engineering purposes, memorizing the centroidal values for standard shapes is far more practical than re-deriving them.

The **parallel-axis theorem** I = I_G + md² is the key tool for composite bodies. It says: if you know I_G (the moment about the centroidal axis), you can find I about any parallel axis simply by adding md², where d is the distance between the axes. The theorem only works in one direction — FROM the centroid TO a parallel axis. To go the other way (you know I about some non-centroidal axis and want I_G), you subtract md². Composite bodies like a flywheel with bolted-on masses are handled by computing I for each component about its own centroid, transferring to the system's rotation axis using the parallel-axis theorem, and summing.

The distinction from area moment of inertia deserves emphasis. Area moment (units: m⁴) depends only on shape and determines stress distribution in beams. Mass moment (units: kg·m²) depends on both shape and mass distribution and determines rotational dynamics. A steel I-beam and an aluminum I-beam of identical geometry have the same area moment of inertia but very different mass moments. Keeping these quantities separate in your thinking prevents the most common error in dynamics: plugging an area moment value into a torque-acceleration equation.
