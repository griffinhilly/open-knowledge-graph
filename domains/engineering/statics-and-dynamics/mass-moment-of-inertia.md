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
status: draft
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

## Explainer

You already know the **area moment of inertia** I = ∫r² dA from statics — it measures how a cross-section's area is distributed around an axis and governs beam bending stiffness. The **mass moment of inertia** follows exactly the same mathematical logic, but replaces area elements dA with mass elements dm: I = ∫r² dm. The conceptual role also parallels: just as area moment resists bending, mass moment resists angular acceleration. In the rotational analog of Newton's second law, ΣM = Iα, the mass moment of inertia I plays precisely the role that mass m plays in ΣF = ma.

The definition I = ∫r² dm reveals why geometry matters so much: mass far from the axis contributes quadratically, not linearly. A hollow cylinder and a solid cylinder of equal mass and outer radius have very different moments of inertia — the hollow cylinder has more because its mass is concentrated at large r. For a solid disk of mass m and radius R, I_G = mR²/2; for a thin rod rotating about its end, I = mL²/3. These formulas are derived by setting up the integral over appropriate geometry. For engineering purposes, memorizing the centroidal values for standard shapes is far more practical than re-deriving them.

The **parallel-axis theorem** I = I_G + md² is the key tool for composite bodies. It says: if you know I_G (the moment about the centroidal axis), you can find I about any parallel axis simply by adding md², where d is the distance between the axes. The theorem only works in one direction — FROM the centroid TO a parallel axis. To go the other way (you know I about some non-centroidal axis and want I_G), you subtract md². Composite bodies like a flywheel with bolted-on masses are handled by computing I for each component about its own centroid, transferring to the system's rotation axis using the parallel-axis theorem, and summing.

The distinction from area moment of inertia deserves emphasis. Area moment (units: m⁴) depends only on shape and determines stress distribution in beams. Mass moment (units: kg·m²) depends on both shape and mass distribution and determines rotational dynamics. A steel I-beam and an aluminum I-beam of identical geometry have the same area moment of inertia but very different mass moments. Keeping these quantities separate in your thinking prevents the most common error in dynamics: plugging an area moment value into a torque-acceleration equation.
