---
id: stress-concentration-and-singularities
title: Stress Concentration and Stress Singularities
domain: engineering
course: materials-science
prerequisites:
- id: stress-strain-behavior
  type: hard
- id: elastic-constants-and-elasticity
  type: soft
builds-toward:
- stress-intensity-factor-and-fracture
- fatigue-crack-initiation
tags:
- stress-concentration
- singularity
- geometric-effects
- notch-strength
stage: formal-systems
status: draft
---

# Stress Concentration and Stress Singularities

## Core Idea
Geometric discontinuities—notches, holes, corners, cracks—create local stress concentrations that exceed the nominal applied stress by a concentration factor Kt. Stress singularities at sharp crack tips describe the inverse-square-root stress field characteristic of linear elastic fracture mechanics. Stress concentration governs crack initiation and is critical for fatigue and fracture prediction.

## Explainer

You already know from stress-strain behavior that a uniformly loaded bar under tension develops a uniform stress σ = F/A everywhere in its cross-section, far from the ends and any features. But real components are never perfectly uniform: they have holes for fasteners, fillets at section changes, keyways, threads, and surface scratches. Near any geometric discontinuity, the stress field is no longer uniform — it is locally amplified, sometimes dramatically, because the load-carrying "flow" of stress must crowd around the obstacle.

The **stress concentration factor** Kt = σ_max/σ_nom is the ratio of peak local stress to the nominal stress calculated from basic mechanics (load divided by net area). For a circular hole in a wide plate under far-field tension, Kt = 3 — the stress at the edge of the hole is exactly three times the applied far-field stress, regardless of the hole's size. This result from elasticity theory has a striking implication: a 1 mm hole and a 100 mm hole in a large plate have the same Kt. What matters is the shape of the feature, not its absolute size. Kt depends on geometry ratios: shallow, wide notches have lower Kt than sharp, deep ones; gradual fillets have lower Kt than abrupt right-angle corners. These relationships are tabulated in stress concentration handbooks (Peterson's), and selecting geometries with low Kt is a primary tool in fatigue-resistant design.

For a **crack** — an idealized notch with zero tip radius — Kt would formally be infinite. Elasticity theory predicts that the stress near a crack tip diverges as σ ∝ K/√r, where r is the distance from the crack tip and K is the **stress intensity factor**. This inverse-square-root **singularity** is universal for all cracks in linear elastic materials; the geometry, crack length, and loading magnitude enter only through K. The stress intensity factor is the central quantity in linear elastic fracture mechanics (LEFM): if K exceeds the material's fracture toughness K_Ic (a material property), the crack propagates catastrophically. This connects stress concentration to your future study of fracture toughness and crack growth.

The engineering significance is profound: fatigue failures — components that crack and fail at stresses far below the yield strength after many repeated load cycles — almost always initiate at stress concentrations. The mechanism is that the locally amplified stress exceeds the fatigue limit even when the nominal stress does not. Classic failure sites are bolt holes, keyways, thread roots, weld toes, and surface corrosion pits. The **fatigue stress concentration factor** Kf is typically slightly lower than Kt because small plastically deformed volumes at stress concentrations blunt the theoretical elastic peak; their ratio Kf/Kt defines **notch sensitivity**. Designing for fatigue resistance means eliminating sharp transitions (large fillet radii), controlling surface finish (avoiding machining marks), and sometimes introducing beneficial compressive residual stresses through shot peening or surface rolling — all engineering responses to the amplifying power of geometric stress concentration.
