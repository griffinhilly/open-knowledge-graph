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

## Questions

```yaml
- question: "A structural engineer is designing a reinforced concrete beam with heavy steel bars concentrated near the bottom. For calculating the neutral axis location used in bending stress analysis, which reference point should she use?"
  type: multiple-choice
  options:
    - "The center of mass of the cross-section, because bending involves forces on the material"
    - "The geometric centroid of the cross-section, because bending stress calculations depend on section geometry, not material distribution"
    - "The midpoint between the centroid and the center of mass as a practical approximation"
    - "The center of mass, because steel is much stiffer and heavier than concrete"
  answer: 1
  explanation: "Bending stress and neutral axis location are geometric calculations based on area moment of inertia — they use the centroid of the cross-sectional area. The fact that the steel bars make the center of mass different from the centroid is relevant for dynamics (F = ma applied to the beam as a moving body), not for static bending stress calculations. This is the central practical distinction: centroid for geometric/section properties, center of mass for Newton's laws applied to the moving body."

- question: "A hollow steel sphere and a solid foam sphere have the same outer radius but very different density distributions. Where is the center of mass of the hollow steel sphere relative to its centroid?"
  type: multiple-choice
  options:
    - "The center of mass is shifted toward the bottom because the steel shell is heavier there"
    - "They coincide — both are at the geometric center, because the hollow sphere has uniform shell thickness and thus uniform mass distribution around the center"
    - "The center of mass is above the centroid because the foam interior pulls it up"
    - "The centroid is undefined for hollow objects"
  answer: 1
  explanation: "A hollow sphere with uniform wall thickness has its mass distributed symmetrically about the geometric center — so the center of mass equals the centroid (at the center). The centroid of the outer sphere shape is also at the center. Both coincide, for the same reason they coincide for a uniform solid sphere: the mass distribution is symmetric about the center. Centroid and center of mass differ only when density varies non-uniformly, breaking the symmetry."

- question: "For any object with uniform density, the centroid and center of mass are always the same point."
  type: true-false
  answer: true
  explanation: "When density ρ is constant, it cancels from the center of mass formula: x̄_cm = ∫x ρ dV / ∫ρ dV = ρ∫x dV / ρ∫dV = ∫x dV / V — which is exactly the centroid formula. Uniform density is the one condition under which the purely geometric centroid and the mass-weighted center of mass coincide. This is why introductory statics problems rarely distinguish them: most introductory problems assume uniform material."

- question: "When applying Newton's second law (ΣF = ma) to a rigid body in motion, the acceleration a refers to the acceleration of the body's geometric centroid."
  type: true-false
  answer: false
  explanation: "This is the critical error the distinction is designed to prevent. Newton's second law for a rigid body states that ΣF = m·a_cm, where a_cm is the acceleration of the center of mass — not the centroid. For a non-uniform body (like a steel-reinforced beam or a car engine with heavy components on one side), the centroid and center of mass are different points with different accelerations. Using the centroid acceleration in Newton's law gives wrong answers. The centroid is for geometry; the center of mass is for dynamics."

- question: "Explain when an engineer should use the centroid versus the center of mass, and give one concrete example of each."
  type: short-answer
  answer: "Use the centroid for geometric questions about a shape, independent of the material's density distribution: calculating area moments of inertia, finding where a distributed load resultant acts, or determining the neutral axis for bending. The centroid is a property of the geometry alone. Use the center of mass when applying Newton's laws to the body as a dynamic system: F = ma for translational motion, angular momentum about a moving reference point, or kinetic energy of a rigid body in motion. Example of centroid use: a distributed snow load on a beam is replaced by a resultant force acting through the centroid of the load diagram — this is purely geometric. Example of center of mass use: analyzing the trajectory of a thrown wrench, where the center of mass follows a parabola while the wrench rotates around it."
  explanation: "The rule of thumb: centroid for 'where does the geometry put things?' questions (section properties, load resultants), center of mass for 'how does this object move?' questions (Newton's second law, kinetic energy). For uniform-density objects they are the same point, which is why the distinction rarely matters in introductory courses."
```

## Explainer

The **centroid** is a purely geometric property — it is the average position of all points in a shape, treating every infinitesimal element equally. When you computed centroids using composite areas and integration, the formula was x̄ = ∫x dA / A: position weighted by area, nothing more. The shape's material doesn't appear anywhere in the calculation. A hollow steel ring and a solid foam disk of identical outer dimensions have exactly the same centroid.

The **center of mass** adds one ingredient: density. The formula becomes x̄_cm = ∫x ρ dV / ∫ρ dV — position weighted by mass, not area. For a uniform object, density ρ is constant and cancels from numerator and denominator, so center of mass equals centroid. The two concepts are identical for homogeneous objects, which is why the distinction rarely surfaces in introductory statics problems.

The distinction becomes critical the moment density varies through the object. Consider a reinforced concrete beam: the geometric centroid sits at mid-height, but the heavy steel reinforcing bars at the bottom pull the center of mass downward. For structural calculations (neutral axis location, area moment of inertia for bending), you use the geometric centroid of the cross section. For dynamics, when you write F = ma for the beam as a rigid body, the acceleration a refers to the acceleration of the center of mass — the steel-weighted location, not the geometric mid-height.

The practical rule: use the centroid for geometric questions (distributed load resultants, area moment of inertia, section properties) and use the center of mass for dynamic equations (Newton's second law, kinetic energy of a rigid body, angular momentum about a moving point). For the distributed loads on beams you studied earlier, the resultant acts through the centroid of the load diagram — that is a geometric calculation, independent of the beam's material. But once the beam starts moving, F = ma ties directly to the center of mass.

For the upcoming topics on moment of inertia and rigid-body work-energy, this distinction will reappear constantly. The parallel-axis theorem shifts a moment of inertia from an axis through the centroid to a parallel axis through another point — but when the body is in motion, the natural reference is the center of mass. Keeping these two points clearly distinguished, and knowing which one is relevant in each context, is the central skill this topic develops.
