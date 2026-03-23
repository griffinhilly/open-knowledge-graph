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

## Questions

```yaml
- question: "An engineer is choosing between a 5 mm diameter hole and a 25 mm diameter hole in a large steel plate under uniform tension. Which statement best describes how the stress concentration factor Kt compares between the two holes?"
  type: multiple-choice
  options:
    - "The 25 mm hole has a higher Kt because it interrupts more of the cross-section"
    - "The 5 mm hole has a higher Kt because stress crowds more tightly around a smaller feature"
    - "Both holes have the same Kt = 3, because Kt depends on shape, not absolute size"
    - "The 25 mm hole has a lower Kt because it creates a more gradual stress gradient"
  answer: 2
  explanation: "For a circular hole in a wide plate, Kt = 3 regardless of hole diameter — this is one of the most important results in stress concentration theory. What matters is the geometric shape (circle), not the absolute size. The misconception in options A and B is confusing net area reduction (a different effect on nominal stress) with the stress concentration factor itself, which is purely a function of geometry ratios."

- question: "A rotating shaft component fails by fatigue cracking at a fillet, despite the nominal applied stress being well below the material's fatigue limit. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Fatigue failure requires the nominal stress to exceed yield, so this must be a manufacturing defect"
    - "The locally amplified stress at the geometric discontinuity exceeds the fatigue limit even though the nominal stress does not"
    - "Fatigue is controlled by average cross-sectional stress, so stress concentration is irrelevant to initiation"
    - "The fillet reduces cross-sectional area, lowering nominal stress and accelerating fatigue"
  answer: 1
  explanation: "Stress concentration is precisely why fatigue failures occur at stresses far below the nominal fatigue limit. The fillet creates a local stress amplification Kt times the nominal stress; even when the nominal stress is safe, the locally amplified stress at the fillet root may exceed the fatigue limit, initiating microcracks. This is why fatigue failures almost always begin at geometric features — holes, keyways, thread roots, surface scratches — rather than in smooth, uniform regions."

- question: "Doubling the diameter of a circular hole in a large plate under uniform tension does not change the stress concentration factor Kt at the hole edge."
  type: true-false
  answer: true
  explanation: "Kt for a circular hole in a wide plate equals 3 regardless of hole size, as long as the hole is small relative to the plate width. Kt depends on geometric shape and ratios, not absolute dimensions. This is a striking and often counterintuitive result: a 1 mm hole and a 100 mm hole in an otherwise identical plate have exactly the same peak-stress amplification factor."

- question: "A sharp crack in an elastic material has an extremely high but finite stress concentration factor Kt, because the tip radius approaches — but never quite reaches — zero."
  type: true-false
  answer: false
  explanation: "For a crack with zero tip radius, Kt is formally infinite — this is a stress singularity, not merely a very high Kt. The elastic stress field diverges as σ ∝ K/√r as the distance r from the crack tip approaches zero. The concept of Kt no longer applies; instead, linear elastic fracture mechanics (LEFM) uses the stress intensity factor K to characterize the crack tip field. The transition from Kt (for notches with finite radius) to K (for cracks) marks the boundary between stress concentration and fracture mechanics."

- question: "Why do fatigue failures almost always initiate at geometric features like holes, fillets, or surface scratches, even when the nominal applied stress is well below the material's fatigue limit?"
  type: short-answer
  answer: "Geometric discontinuities amplify local stress by a factor Kt above the nominal stress. Even if the nominal stress is below the fatigue limit, the locally amplified stress at the feature can exceed the fatigue limit, initiating microcracks that grow with each load cycle until sudden fracture occurs."
  explanation: "This is the central engineering significance of stress concentration: the fatigue limit is a material property measured on smooth specimens with uniform stress, but real components always have notches, holes, and surface irregularities. The local stress at these features equals Kt × σ_nominal, and for a fillet with Kt = 2.5 and a nominal stress of 60% of the fatigue limit, the local stress would be 150% of the fatigue limit — a guaranteed fatigue failure site. Designing for fatigue resistance means minimizing Kt through generous fillet radii, smooth surface finishes, and avoiding abrupt geometry changes."
```

## Explainer

You already know from stress-strain behavior that a uniformly loaded bar under tension develops a uniform stress σ = F/A everywhere in its cross-section, far from the ends and any features. But real components are never perfectly uniform: they have holes for fasteners, fillets at section changes, keyways, threads, and surface scratches. Near any geometric discontinuity, the stress field is no longer uniform — it is locally amplified, sometimes dramatically, because the load-carrying "flow" of stress must crowd around the obstacle.

The **stress concentration factor** Kt = σ_max/σ_nom is the ratio of peak local stress to the nominal stress calculated from basic mechanics (load divided by net area). For a circular hole in a wide plate under far-field tension, Kt = 3 — the stress at the edge of the hole is exactly three times the applied far-field stress, regardless of the hole's size. This result from elasticity theory has a striking implication: a 1 mm hole and a 100 mm hole in a large plate have the same Kt. What matters is the shape of the feature, not its absolute size. Kt depends on geometry ratios: shallow, wide notches have lower Kt than sharp, deep ones; gradual fillets have lower Kt than abrupt right-angle corners. These relationships are tabulated in stress concentration handbooks (Peterson's), and selecting geometries with low Kt is a primary tool in fatigue-resistant design.

For a **crack** — an idealized notch with zero tip radius — Kt would formally be infinite. Elasticity theory predicts that the stress near a crack tip diverges as σ ∝ K/√r, where r is the distance from the crack tip and K is the **stress intensity factor**. This inverse-square-root **singularity** is universal for all cracks in linear elastic materials; the geometry, crack length, and loading magnitude enter only through K. The stress intensity factor is the central quantity in linear elastic fracture mechanics (LEFM): if K exceeds the material's fracture toughness K_Ic (a material property), the crack propagates catastrophically. This connects stress concentration to your future study of fracture toughness and crack growth.

The engineering significance is profound: fatigue failures — components that crack and fail at stresses far below the yield strength after many repeated load cycles — almost always initiate at stress concentrations. The mechanism is that the locally amplified stress exceeds the fatigue limit even when the nominal stress does not. Classic failure sites are bolt holes, keyways, thread roots, weld toes, and surface corrosion pits. The **fatigue stress concentration factor** Kf is typically slightly lower than Kt because small plastically deformed volumes at stress concentrations blunt the theoretical elastic peak; their ratio Kf/Kt defines **notch sensitivity**. Designing for fatigue resistance means eliminating sharp transitions (large fillet radii), controlling surface finish (avoiding machining marks), and sometimes introducing beneficial compressive residual stresses through shot peening or surface rolling — all engineering responses to the amplifying power of geometric stress concentration.
