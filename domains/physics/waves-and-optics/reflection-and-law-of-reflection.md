---
id: reflection-and-law-of-reflection
title: Reflection and the Law of Reflection
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-and-classification
  type: hard
- id: impedance-matching-and-reflection
  type: soft
- id: reflection-and-refraction-conceptual
  type: soft
- id: reflection-of-light
  type: soft
builds-toward:
- plane-mirrors
- spherical-mirrors
tags:
- reflection
- law-of-reflection
- angle
stage: formal-systems
status: validated
---
# Reflection and the Law of Reflection

## Core Idea
The law of reflection states that the angle of incidence equals the angle of reflection, both measured from the normal to the surface. Reflection occurs when waves encounter a boundary and return into the original medium. The law applies to all wave types reflecting from smooth surfaces.

## Questions

```yaml
- question: "A student measures a light ray hitting a mirror at 60° from the surface and concludes the reflected ray makes 60° with the surface on the other side. What error has the student made?"
  type: multiple-choice
  options:
    - "The reflected ray should be on the same side as the incident ray"
    - "Angles must be measured from the normal (perpendicular to the surface). If the ray is 60° from the surface, it is 30° from the normal — so the reflected ray is 30° from the normal, not 60°"
    - "The law of reflection only applies when angles are measured from the surface, so the student is correct"
    - "The error is that the ray's angle changes upon reflection because the mirror absorbs some energy"
  answer: 1
  explanation: "The law of reflection measures angles from the normal — an imaginary line perpendicular to the surface at the point of contact — not from the surface itself. A ray 60° from the surface is 30° from the normal (since 90° − 60° = 30°). The reflected ray is therefore 30° from the normal, which equals 60° from the surface. In this specific case the numbers agree, but for other angles they won't, and the conceptual error (measuring from the surface) is still wrong in principle and breaks the consistency with Snell's law for refraction."

- question: "Why does a flat mirror produce an image that appears to be located behind the mirror, at the same distance as the object in front?"
  type: multiple-choice
  options:
    - "Mirrors are slightly curved, causing all reflected rays to appear to converge behind the mirror"
    - "Light slows in the glass of the mirror and appears to originate from further away"
    - "Applying θᵢ = θᵣ to every ray from an object point produces diverging reflected rays whose backward extensions all meet at a point symmetrically behind the mirror"
    - "The mirror's silver coating emits light that appears to come from behind the surface"
  answer: 2
  explanation: "This is a direct geometric consequence of the law of reflection applied to all rays. Each ray from an object point hits the mirror at a different angle, reflects at the equal angle, and diverges. Tracing these reflected rays backward (as your eye does when it sees them), they all converge at a single point as far behind the mirror as the object is in front. No special properties of glass or coatings are needed — only the geometry of equal angles."

- question: "The law of reflection (θᵢ = θᵣ) applies specifically to light reflecting from polished surfaces and does not extend to sound, water waves, or other wave types."
  type: true-false
  answer: false
  explanation: "The law of reflection is universal for all wave types reflecting from smooth surfaces. Sound echoing from a flat wall, a water ripple bouncing from a barrier, seismic waves reflecting from geological boundaries — all obey θᵢ = θᵣ. The geometry of wavefront reflection is the same regardless of what is waving. The law derives from the wave nature of the phenomenon, not from properties specific to light."

- question: "Measuring angles from the normal rather than from the surface is an arbitrary convention that could equally well be done the other way."
  type: true-false
  answer: false
  explanation: "The normal provides a stable, orientation-independent reference that simplifies the geometry. When a surface is tilted, angles measured from the surface change with the tilt, producing different numbers for the same physical interaction. The normal always provides a perpendicular baseline that cleanly separates incident and reflected rays. More importantly, the same normal convention is used in Snell's law for refraction — angles of incidence and refraction are both measured from the normal — making all of geometric optics internally consistent. The choice is principled, not arbitrary."

- question: "Explain why concave and convex mirrors focus or diverge light differently from flat mirrors, even though the law of reflection is the same at every point on all three surfaces."
  type: short-answer
  answer: "The law of reflection applies locally: at each point on any mirror, θᵢ = θᵣ measured from the local normal. On a flat mirror, all normals point in the same direction, so all reflected rays remain parallel (or diverge uniformly from a point). On a curved mirror, the normal direction rotates from point to point along the surface. Different rays from the same source hit different parts of the curve at different angles from their respective local normals and are redirected in different directions. For a concave mirror, this geometry causes the reflected rays to converge (focus); for a convex mirror, to diverge further."
  explanation: "The key insight is 'same law, different normals, different outcomes.' The law itself is universal; surface curvature determines how the normals are oriented, which determines the redirection of each ray. Understanding this makes curved mirror optics a direct extension of flat mirror geometry, not a separate phenomenon."
```

## Explainer

From your study of wave properties, you know that waves carry energy through a medium and interact with boundaries. When a wave reaches the interface between two media — light hitting a mirror, sound hitting a wall, a water ripple reaching a barrier — part of the energy bounces back into the original medium. This is **reflection**. The law of reflection describes the exact geometry of that bounce with a single, elegant rule.

The critical convention is that angles are measured from the **normal** — an imaginary line drawn perpendicular to the reflecting surface at the point of contact — not from the surface itself. The **angle of incidence** (θᵢ) is the angle between the incoming ray and the normal; the **angle of reflection** (θᵣ) is the angle between the outgoing ray and the same normal, on the other side. The law states: θᵢ = θᵣ. A ray hitting a flat mirror at 30° from the normal leaves at 30° from the normal, in the same plane as the incoming ray and the normal.

Why measure from the normal rather than the surface? Using the normal provides a stable, universal reference. When a surface is tilted, measuring angles from the surface gives a confusing number that depends on the tilt. The normal always provides a perpendicular baseline that cleanly separates incident and reflected rays. This same convention carries forward to Snell's law for refraction, making the geometry of optics internally consistent across reflection and transmission.

A billiard ball bouncing off a cushion obeys the same rule — angle in equals angle out — because the impulse from the surface acts along the normal. Flat mirrors form images that appear to be behind the mirror at the same distance as the object is in front, a direct consequence of the law applied to every ray from the object: each reflected ray diverges as if it originated from a point symmetrically behind the mirror. The spherical mirrors you'll study next apply this same law at every point on a curved surface — but because the normal direction rotates along the curve, different incident rays meet different normals and are redirected to converge (concave) or diverge (convex), producing the focusing and diverging properties that make curved mirrors useful.
