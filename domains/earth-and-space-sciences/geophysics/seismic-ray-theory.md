---
id: seismic-ray-theory
title: Seismic Ray Theory and Ray Tracing
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: elastic-wave-propagation-in-solids
  type: hard
- id: seismic-body-waves-p-and-s
  type: hard
- id: differential-equations-intro
  type: soft
- id: wave-equation-one-dimensional
  type: soft
- id: geometric-optics-ray-approximation
  type: hard
- id: wave-motion-definition
  type: hard
- id: wave-properties-intro
  type: hard
- id: snells-law
  type: hard
builds-toward:
- seismic-refraction-surveys
- seismic-tomography-velocity-imaging
tags:
- seismic
- ray
- theory
- propagation
stage: advanced
status: validated
---

# Seismic Ray Theory and Ray Tracing

## Core Idea
Ray theory describes wave propagation as rays traveling along paths determined by Snell's law and the velocity structure. Ray parameters (p-values) remain constant along rays, enabling inversion of travel times to velocity models.

## Questions

```yaml
- question: "In Earth's mantle, seismic velocity generally increases with depth. Consider two seismic rays launched from the same earthquake: one at a steep downward angle and one at a shallow angle nearly horizontal. Which ray penetrates deeper before turning back toward the surface?"
  type: multiple-choice
  options:
    - "The shallow-angle ray, because it is nearly parallel to the velocity gradient and travels farther before refracting upward"
    - "The steep-angle ray, because it has a smaller ray parameter and penetrates to greater depth before turning"
    - "Both rays turn at the same depth because the turning depth depends only on the velocity structure, not the launch angle"
    - "The shallow-angle ray turns immediately near the surface because low-angle rays cannot refract into high-velocity material"
  answer: 1
  explanation: "The ray parameter p = sin(θ)/v is conserved along the ray path. A steeper ray (larger θ from horizontal at launch) has a smaller p value. The turning point occurs where the ray becomes horizontal (θ = 90°), meaning sin(θ)/v = 1/v_turn = p. A smaller p corresponds to a larger v_turn — a deeper layer with higher velocity — so steep rays (small p) turn deeper. Shallow-angle rays (large p) hit the turning condition at shallower, lower-velocity depths. This is the inverse of intuition: it's the steep ray, not the shallow one, that penetrates deeper."

- question: "A seismologist observes a gap in a travel-time curve — a range of epicentral distances where no direct seismic arrivals are recorded. What does this shadow zone most likely indicate about Earth's interior?"
  type: multiple-choice
  options:
    - "The earthquake was too small to generate seismic waves detectable at those distances"
    - "A low-velocity zone at depth deflects rays away from those distances, leaving a gap in direct-wave coverage"
    - "Seismic attenuation absorbs all energy before the waves can travel that far through the mantle"
    - "The seismometers at those distances were not operating when the earthquake occurred"
  answer: 1
  explanation: "A low-velocity zone (LVZ) bends rays toward steeper angles (they speed up entering the LVZ, which by Snell's law bends them away from horizontal). This refracts direct rays into a narrower distance range, leaving a gap — a shadow zone — at intermediate distances. The classic example is Earth's outer core: P-wave velocity drops sharply at the core-mantle boundary, creating a P-wave shadow zone between ~105° and ~140°. Similarly, the asthenosphere LVZ creates subtle effects in teleseismic travel times. Shadow zones are diagnostic of velocity decreases with depth."

- question: "The ray parameter p = sin(θ)/v is conserved along a seismic ray path, which causes rays to curve continuously as they travel through rock where velocity changes smoothly with depth."
  type: true-false
  answer: true
  explanation: "Conservation of the ray parameter is the seismic analog of Snell's law generalized to continuously varying media. At every point along the ray, sin(θ)/v must equal the same constant p. As v increases with depth, sin(θ) must increase to maintain p constant — meaning θ increases toward 90° (horizontal). This progressive bending continues until the ray reaches its turning point, then reverses on the way back up. The result is curved ray paths through Earth rather than straight lines, which is why seismic rays from shallow earthquakes follow arcs through the interior."

- question: "Seismic rays travel in straight lines through Earth's interior and only change direction abruptly when they encounter sharp velocity discontinuities like the Moho or core-mantle boundary."
  type: true-false
  answer: false
  explanation: "Rays curve continuously wherever velocity changes smoothly with depth — which describes most of Earth's mantle. Sharp discontinuities produce abrupt direction changes (refraction and reflection following Snell's law), but gradual velocity gradients cause continuous bending. In reality, most seismic rays follow smooth curves that arc through the mantle, turning at depth before returning to the surface. Assuming straight-line propagation would yield completely wrong travel times and epicenter locations."

- question: "How does the shape of the travel-time curve — arrival time plotted against epicentral distance — encode information about Earth's velocity structure, and how can it be inverted to recover velocity as a function of depth?"
  type: short-answer
  answer: "The travel-time curve's slope at any distance gives the ray parameter p = dt/dΔ of the ray arriving at that distance. Since each ray samples a specific depth range determined by its turning point, the curve encodes which velocities are encountered at which depths. A gradual smooth curve indicates velocity increasing steadily with depth. A discontinuity in the curve indicates a sharp velocity jump (like the Moho). A triplication (multiple arrivals at the same distance) indicates a rapid velocity increase. The Herglotz-Wiechert formula inverts the p(Δ) function directly into a v(z) profile. Modern tomography extends this by fitting travel times from many earthquakes and stations to build 3D velocity models."
  explanation: "The inverse problem — recovering Earth structure from surface observations — is the core of seismic tomography. The travel-time curve is the bridge between observable quantities (arrival times) and the target (velocity structure). Every shape feature of the curve has a physical interpretation in terms of what the interior is doing to the rays."
```

## Explainer

You already understand that seismic waves travel through the Earth as P-waves and S-waves, and from your study of wave properties and geometric optics, you know that waves change direction when they encounter changes in the medium they travel through. **Seismic ray theory** applies the same high-frequency approximation used in optics — treating wave propagation as the tracing of rays along paths — to the problem of seismic waves traveling through Earth's interior. Just as a light ray bends when it passes from air into glass, a seismic ray bends when it crosses a boundary between rocks with different seismic velocities.

The foundation of ray theory is **Snell's law**, which you have already encountered: sin(θ)/v = constant along a ray path, where θ is the angle between the ray and the vertical, and v is the local seismic velocity. This constant is called the **ray parameter** (p), and its conservation is the single most important principle in seismic ray tracing. In a medium where velocity increases smoothly with depth — as it generally does in Earth's interior — Snell's law requires rays to curve continuously, bending away from the vertical as they descend into faster material and then curving back toward the surface. The result is that seismic rays follow curved paths that arc through the interior, diving to a maximum depth (the **turning point**, where the ray becomes horizontal) before rising back to the surface. The turning depth depends on the ray parameter: rays with smaller p values (launched more steeply) penetrate deeper, while rays with larger p values (launched at shallow angles) turn at shallower depths.

This geometry means that a seismometer at a given distance from an earthquake receives energy that has sampled a specific depth range of the Earth's interior. By recording the **travel time** — the time elapsed between the earthquake and the arrival of the seismic wave — at many stations at different distances, seismologists build a **travel-time curve**: a plot of arrival time versus angular distance. The shape of this curve encodes the velocity structure of the interior. Where velocity increases gradually, the travel-time curve is smooth and concave downward. A sharp velocity increase (like the Moho at the base of the crust) produces a discontinuity in the curve, and a **low-velocity zone** causes a shadow zone where no direct rays arrive at certain distances — exactly analogous to how a lens can create regions of focused and defocused light.

The practical power of ray theory lies in the **inverse problem**: given observed travel times, reconstruct the velocity model. The Herglotz-Wiechert inversion formula provides an exact solution for a spherically symmetric Earth, converting the observed p(Δ) function (ray parameter as a function of distance) into a velocity-depth profile v(z). Modern seismology extends this approach with numerical ray tracing through three-dimensional velocity models, iteratively adjusting the model until computed travel times match observations. This is the foundation of **seismic tomography**, which images velocity variations throughout Earth's mantle and core — but that extension builds directly on the ray-theoretical framework of Snell's law, ray parameters, and the relationship between travel times and velocity structure.
