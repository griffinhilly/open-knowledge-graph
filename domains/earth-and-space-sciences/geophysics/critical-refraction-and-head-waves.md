---
id: critical-refraction-and-head-waves
title: Critical Angle Refraction and Head Waves
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: seismic-ray-tracing-methods
  type: hard
- id: seismic-refraction-surveys
  type: soft
builds-toward:
- reflection-seismic-survey-design
tags:
- seismic
- refraction
- head-waves
- critical-angle
stage: expert
status: validated
---
# Critical Angle Refraction and Head Waves

## Core Idea
When a seismic ray encounters a velocity increase at a boundary, it reaches a critical angle of incidence beyond which total internal reflection occurs. At the critical angle, refracted waves travel horizontally along the interface and generate head waves that arrive at large distances before direct rays. Head waves provide important constraints on velocity structure and are widely used in refraction seismic surveys.

## Questions

```yaml
- question: "On a seismic time-distance (t-x) plot, the head wave arrival forms a line with slope 1/V₂. What does this slope tell you?"
  type: multiple-choice
  options:
    - "The velocity of the upper (slower) layer, since the head wave travels upward through it"
    - "The average velocity of both layers combined"
    - "The velocity of the deeper (faster) layer, which the head wave travels along"
    - "The vertical velocity gradient through the entire crust"
  answer: 2
  explanation: "The head wave travels horizontally along the interface at the velocity of the deeper layer, V₂. Its apparent velocity on the surface (the inverse of the slope of the t-x line) is V₂ because the horizontal segment dominates the travel time at large offsets. The direct wave line has slope 1/V₁ (the upper layer velocity). This is what makes refraction seismology so powerful: the slope directly reveals V₂ without needing to drill to that depth. The intercept of the head wave line encodes the layer depth, while the slope gives the velocity."

- question: "A seismic survey records both direct waves and head waves. At what distances does the head wave arrive first?"
  type: multiple-choice
  options:
    - "At all distances, since the head wave travels in the faster layer"
    - "Only at short distances, close to the source, where the path is nearly horizontal"
    - "Beyond the crossover distance, where the speed advantage of V₂ outweighs the longer path length"
    - "Head waves never arrive before direct waves — they are always secondary arrivals"
  answer: 2
  explanation: "The head wave travels a longer total path (down at the critical angle, along the interface, back up at the critical angle) but the horizontal segment moves at the faster velocity V₂. At short distances, the direct wave's shorter path wins. Beyond the crossover distance, the head wave's speed advantage compounds enough to overcome the path length penalty. On a t-x plot, the crossover is the point where the two lines intersect — beyond it, the head wave line (shallower slope, 1/V₂) is below the direct wave line (steeper slope, 1/V₁), meaning earlier arrival."

- question: "Head waves can form at a boundary between any two layers, regardless of which layer has higher seismic velocity."
  type: true-false
  answer: false
  explanation: "Head waves require that the lower layer have a higher velocity (V₂ > V₁). Snell's law determines that a ray bends away from the normal when entering a faster medium. The critical angle (arcsin(V₁/V₂)) only exists when V₂ > V₁ — if V₂ ≤ V₁, there is no angle at which the refracted ray reaches 90° and travels horizontally. Head waves are a phenomenon of velocity increase with depth. If the deeper layer is slower, the refracted ray bends toward the normal and no critical refraction occurs."

- question: "At short source-receiver distances in a refraction survey, head waves arrive before the direct P-wave because they travel partly through the faster lower layer."
  type: true-false
  answer: false
  explanation: "At short distances, the direct wave arrives first — it travels a shorter total path through the upper layer, and the head wave's speed advantage has not had enough horizontal distance to overcome its longer path. Only beyond the crossover distance does the head wave overtake the direct wave. This is why refraction surveys must use sufficiently long receiver spreads: if all receivers are too close to the source, the head wave arrives second and may be obscured. Designing receiver geometry to capture head wave first arrivals is a practical consideration in seismic refraction surveys."

- question: "Why do head waves arrive before direct waves at large source-receiver distances, even though the head wave travels a longer total path?"
  type: short-answer
  answer: "The head wave travels part of its path at V₂, the faster lower-layer velocity, while the direct wave travels entirely at V₁, the slower upper-layer velocity. Although the head wave path is geometrically longer (down at the critical angle, horizontally along the interface, back up), the horizontal segment can be very long and moves at V₂ > V₁. At large enough distances, the time saved by traveling fast horizontally exceeds the time penalty from the angled down-and-up segments, so the head wave arrives first."
  explanation: "This is analogous to driving a longer highway route instead of city streets: the extra distance is compensated by the higher speed. The crossover distance is where the two travel times are equal — for a simple two-layer case, it equals 2h·√((V₂+V₁)/(V₂-V₁)) where h is the layer depth. Beyond this distance, the faster horizontal propagation dominates, and the head wave becomes the first arrival. This crossover distance also encodes information about layer depth, making the geometry doubly useful in seismic interpretation."
```

## Explainer

From seismic ray tracing, you know that a seismic wave crossing a boundary between two layers bends according to Snell's law: sin(θ₁)/V₁ = sin(θ₂)/V₂, where θ is the angle of incidence or refraction and V is the wave velocity in each layer. When V₂ > V₁ — the deeper layer is faster — the refracted ray bends away from the normal. As the incidence angle increases, the refracted angle grows faster. At one specific angle, called the **critical angle** (θ_c = arcsin(V₁/V₂)), the refracted ray bends to exactly 90° and travels horizontally along the interface between the two layers.

This horizontally traveling wave is the key to the whole phenomenon. As it races along the top of the faster layer at velocity V₂, it continuously radiates energy back upward into the slower layer at the critical angle — like a boat creating a wake. These upward-radiating waves are called **head waves** (sometimes called refraction arrivals or conical waves). They propagate back to the surface where geophones can record them. The geometry is distinctive: the ray goes down at the critical angle, runs along the interface, and comes back up at the critical angle, forming a characteristic "V" path with a horizontal segment.

The practical importance of head waves becomes clear when you consider travel times. The direct wave travels straight from source to receiver through the slower upper layer at velocity V₁. The head wave takes a longer path — down, along, and back up — but the horizontal segment travels at the faster velocity V₂. At short source-receiver distances, the direct wave arrives first because its path is shorter. But beyond a certain distance called the **crossover distance**, the head wave overtakes the direct wave because its speed advantage along the interface more than compensates for the extra path length. On a time-distance plot, the direct arrival forms a line with slope 1/V₁, while the head wave arrival forms a line with slope 1/V₂ (shallower, since V₂ > V₁). The intercept time of the head-wave line encodes the depth to the interface.

This is why head waves are so valuable in exploration and crustal geophysics: the slope of the refraction arrival directly gives the velocity of the deeper layer, and the intercept time gives the layer depth. For a simple two-layer case, the math is straightforward. For multiple layers, each velocity boundary produces its own head wave, and the travel-time curve becomes a series of line segments with progressively shallower slopes — each segment revealing the velocity of a deeper layer. The entire framework of seismic refraction surveying is built on detecting and interpreting these arrivals.
