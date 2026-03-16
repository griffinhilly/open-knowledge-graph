---
id: curvilinear-motion-components
title: 'Curvilinear Motion: Tangential and Normal Components'
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: kinematics-particles-curvilinear
  type: hard
builds-toward:
- relative-motion-reference-frames
- rigid-body-plane-motion-analysis
tags:
- curvilinear
- tangential
- normal
- components
stage: formal-systems
status: draft
---

# Curvilinear Motion: Tangential and Normal Components

## Core Idea
For curved motion, acceleration is decomposed into tangential (along the path) and normal (perpendicular to path, toward center) components: a_t = dv/dt and a_n = v²/ρ, where ρ is the radius of curvature. This decomposition is particularly useful for circular and path-dependent motion where the direction of velocity changes.

## Explainer

From your study of curvilinear kinematics, you know that velocity is always directed along the tangent to the path, and that acceleration is the rate of change of the velocity *vector* — not just its magnitude. This is the key: even at constant speed around a curve, the velocity vector is continuously rotating, and a rotating vector has a nonzero rate of change. That rate of change is acceleration, and it points inward, toward the center of curvature. Decomposing acceleration into two perpendicular components — one along the path, one toward the center — makes this geometry explicit and tractable.

The **tangential component** a_t = dv/dt captures the rate at which *speed* changes. If you press the gas pedal on a curved road, you feel pushed back in your seat — that sensation is tangential acceleration. If you're coasting at steady speed, a_t = 0, even though you're accelerating overall because the curve keeps turning your velocity vector. The tangential direction is simply the unit tangent **e_t** to the path at the particle's current position.

The **normal component** a_n = v²/ρ captures the rate at which the *direction* of velocity changes. Here ρ is the **radius of curvature** — the radius of the instantaneous circle that best fits the path at that point. A tighter curve (smaller ρ) or a higher speed both increase a_n. The normal direction **e_n** always points toward the center of curvature. This is why you feel pressed outward on a sharp turn at high speed: the car is being pulled inward by a_n, and by Newton's third law you feel the reaction force pushing you outward.

The power of this decomposition comes when applying Newton's second law: ΣF_t = m·a_t governs how the particle speeds up or slows down along the path, while ΣF_n = m·v²/ρ governs the centripetal force needed to maintain the curved trajectory. For circular motion with constant radius, ρ = R is constant everywhere, which simplifies the analysis greatly. For general curved paths — rollercoaster loops, orbital mechanics, vehicle dynamics — computing ρ at each point lets you separate the "how fast am I going?" question from the "how sharp is the turn?" question, solving each independently before combining them.

