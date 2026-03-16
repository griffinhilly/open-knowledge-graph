---
id: center-of-mass-vs-centroid
title: Center of Mass versus Centroid
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: centroid-areas-composite
  type: hard
- id: distributed-loads-beams
  type: soft
- id: applications-integrals-area-mass
  type: hard
builds-toward:
- moment-of-inertia-about-centroid
- rigid-body-work-energy
tags:
- center-of-mass
- centroid
- density
- gravity
stage: formal-systems
status: draft
---

# Center of Mass versus Centroid

## Core Idea
The centroid is the geometric center of a shape (area or volume) assuming uniform density. The center of mass accounts for actual density distribution; they coincide only for uniform density objects. In statics, the centroid is used for geometric properties and distributed load resultants. In dynamics, the center of mass is essential for applying Newton's laws to rigid bodies.

## Explainer

The **centroid** is a purely geometric property — it is the average position of all points in a shape, treating every infinitesimal element equally. When you computed centroids using composite areas and integration, the formula was x̄ = ∫x dA / A: position weighted by area, nothing more. The shape's material doesn't appear anywhere in the calculation. A hollow steel ring and a solid foam disk of identical outer dimensions have exactly the same centroid.

The **center of mass** adds one ingredient: density. The formula becomes x̄_cm = ∫x ρ dV / ∫ρ dV — position weighted by mass, not area. For a uniform object, density ρ is constant and cancels from numerator and denominator, so center of mass equals centroid. The two concepts are identical for homogeneous objects, which is why the distinction rarely surfaces in introductory statics problems.

The distinction becomes critical the moment density varies through the object. Consider a reinforced concrete beam: the geometric centroid sits at mid-height, but the heavy steel reinforcing bars at the bottom pull the center of mass downward. For structural calculations (neutral axis location, area moment of inertia for bending), you use the geometric centroid of the cross section. For dynamics, when you write F = ma for the beam as a rigid body, the acceleration a refers to the acceleration of the center of mass — the steel-weighted location, not the geometric mid-height.

The practical rule: use the centroid for geometric questions (distributed load resultants, area moment of inertia, section properties) and use the center of mass for dynamic equations (Newton's second law, kinetic energy of a rigid body, angular momentum about a moving point). For the distributed loads on beams you studied earlier, the resultant acts through the centroid of the load diagram — that is a geometric calculation, independent of the beam's material. But once the beam starts moving, F = ma ties directly to the center of mass.

For the upcoming topics on moment of inertia and rigid-body work-energy, this distinction will reappear constantly. The parallel-axis theorem shifts a moment of inertia from an axis through the centroid to a parallel axis through another point — but when the body is in motion, the natural reference is the center of mass. Keeping these two points clearly distinguished, and knowing which one is relevant in each context, is the central skill this topic develops.
