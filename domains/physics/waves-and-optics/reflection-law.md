---
id: reflection-law
title: The Law of Reflection
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-properties-intro
  type: soft
- id: angle-basics-and-classification
  type: hard
builds-toward:
- plane-mirrors
- spherical-mirrors
- refraction-intro
tags:
- reflection
- angle of incidence
- angle of reflection
- normal
- specular
stage: formal-systems
status: validated
---

# The Law of Reflection

## Core Idea
When a wave strikes a surface, the angle of reflection equals the angle of incidence, both measured from the normal (the line perpendicular to the surface at the point of contact). This law holds for all wave types — water waves, sound, and light. Specular reflection (smooth surface) produces clear images; diffuse reflection (rough surface) scatters light in many directions, making objects visible but not mirror-like.

## How It's Best Learned
Shine a laser at a mirror and measure incident and reflected angles with a protractor. Then compare reflection from a mirror vs. from matte paper to distinguish specular and diffuse reflection.

## Common Misconceptions
- Angles are always measured from the normal, not from the surface itself; students frequently measure from the surface and get the complementary angle.
- Diffuse reflection follows the law at each microscopic surface point — the scatter comes from variations in surface orientation, not violation of the law.

## Questions

```yaml
- question: "A light ray strikes a flat mirror at an angle of 25° measured from the mirror surface. What is the angle of reflection, measured from the normal?"
  type: multiple-choice
  options:
    - "25°, because the angle of reflection equals the angle of incidence and that angle is 25°"
    - "65°, because the angle of incidence from the normal is 90° − 25° = 65°"
    - "50°, because the reflection doubles the surface angle"
    - "90°, because light always reflects perpendicular to the surface"
  answer: 1
  explanation: "The law of reflection requires both angles to be measured from the **normal**, not from the surface. A ray arriving at 25° from the surface is arriving at 90° − 25° = 65° from the normal. It therefore reflects at 65° from the normal. The most common error is using the surface angle (25°) as the angle of incidence — option A is exactly this mistake. Always draw the normal first and measure from it."

- question: "A sheet of white paper reflects light diffusely — you can see it from any direction, but you don't see your reflection in it. What explains this diffuse scattering?"
  type: multiple-choice
  options:
    - "Paper violates the law of reflection, scattering light randomly at each surface point"
    - "Paper absorbs most of the light and re-emits it in all directions"
    - "The law of reflection holds at each microscopic surface point, but the surface normals point in many different directions, so reflected rays scatter outward"
    - "Paper is transparent enough that light passes through and scatters inside the material"
  answer: 2
  explanation: "The law of reflection is not violated by diffuse surfaces — it holds perfectly at every microscopic facet. The scatter comes from the surface geometry: a rough surface has countless tiny facets each facing a slightly different direction. Parallel incoming rays obey the law at each facet, but because neighboring facets face different directions, the reflected rays spread in all directions. This is why you can see paper from any angle (scattered light reaches your eye) but it doesn't form an image (the reflected rays are not parallel)."

- question: "The law of reflection applies mainly to light waves, not to sound or water waves."
  type: true-false
  answer: false
  explanation: "The law of reflection follows from the general physics of wave behavior at boundaries — not from anything special about light. Water waves bounce off the edge of a tank, sound echoes off walls, and radar pulses reflect off aircraft — all obeying the same rule: angle of incidence equals angle of reflection, measured from the normal. This universality is one reason the law is considered fundamental."

- question: "A ray hitting a mirror at 40° from the normal reflects at 40° from the normal, on the opposite side of the normal."
  type: true-false
  answer: true
  explanation: "This is the law of reflection stated correctly: both angles — incidence and reflection — are measured from the normal, and they are equal. The reflected ray lies on the opposite side of the normal from the incident ray, in the same plane. Note that 40° from the normal corresponds to 50° from the mirror surface; if the question had said '40° from the surface,' the angles of incidence and reflection would each be 50° from the normal."

- question: "Why is the normal — rather than the surface itself — used as the reference line for measuring angles in the law of reflection?"
  type: short-answer
  answer: "The normal is perpendicular to the surface at the point of contact and provides a symmetric reference: the incident and reflected rays make equal angles on either side of it. Using the surface as reference gives the complementary angle and is inconsistent across different surface orientations. The normal also generalizes naturally to curved surfaces, where the tangent plane and its perpendicular normal can be defined at each point — making it the only reference that works universally."
  explanation: "In practice, using the surface instead of the normal gives the complementary angle. A ray hitting at 30° from the surface has an angle of incidence of 60° from the normal — and reflects at 60°, not 30°. The normal-based convention is both mathematically consistent and physically meaningful: it correctly describes wave behavior at curved surfaces, where the local normal varies from point to point."
```

## Explainer

You've already worked with angles — measuring them, classifying them as acute, right, and obtuse. The law of reflection applies this geometric machinery to a specific physical situation: what happens when a wave hits a surface. The rule is simple: **the angle of incidence equals the angle of reflection**, with both angles measured from the **normal** — the imaginary line perpendicular to the surface at the point of contact.

The normal is the essential reference line, and it is where most errors happen. A ray arriving at 30° from the surface has an angle of incidence of 60° (measured from the normal, not the surface — these are complementary). It reflects at 60° on the other side of the normal, leaving at 30° from the surface. Students who measure from the surface get the complement, and their calculations fall apart. The correct habit is always: draw the normal first, then measure from it.

**Specular reflection** occurs from smooth, mirror-like surfaces. When a surface is smooth at the scale of the wave's wavelength, all the surface normals point in the same direction. Parallel incoming rays reflect as parallel outgoing rays — you get a clear, geometrically precise image. **Diffuse reflection** occurs from rough surfaces like paper, walls, or skin. Microscopically, the surface normals point in countless different directions. At each tiny point, the law of reflection holds perfectly — the angle of incidence equals the angle of reflection at that microscopic facet. But because neighboring facets face different directions, parallel incoming rays scatter outward in all directions. This is why matte objects are visible from any angle (they scatter light toward your eye from many directions) but don't form images.

The law holds for all wave types — water waves, sound, and light — because it follows from the general physics of wave reflection at boundaries, not from anything special about light. If you've ever heard your voice echo off a wall or seen ripples bounce off the edge of a tub, you've observed the same law at work. The universality is part of what makes this such a fundamental result.
