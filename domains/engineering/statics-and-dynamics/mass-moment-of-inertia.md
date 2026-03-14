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
