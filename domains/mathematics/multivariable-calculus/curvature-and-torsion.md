---
id: curvature-and-torsion
title: Curvature and Torsion of Space Curves
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: arc-length-curves-3d
  type: hard
builds-toward:
- surface-parametrization
tags:
- curvature
- torsion
- geometry
stage: formal-systems
status: validated
---

# Curvature and Torsion of Space Curves

## Core Idea
Curvature κ = |dT/ds| measures how sharply a curve bends; torsion τ measures how much it twists out of its oscillating plane. For a curve r(t), κ = |r'(t) × r''(t)| / |r'(t)|³. Torsion reveals how much the curve deviates from being planar.

## Questions

```yaml
- question: "A space curve r(t) has torsion τ = 0 at every point. What does this tell you about the curve?"
  type: multiple-choice
  options:
    - "The curve is a straight line — zero torsion implies zero curvature as well"
    - "The curve lies entirely within a fixed plane"
    - "The curve has constant speed in its parameterization"
    - "The curvature κ must be constant but not necessarily zero"
  answer: 1
  explanation: "Torsion measures how much the curve twists out of its osculating plane. When τ = 0 everywhere, the binormal vector B is constant (dB/ds = −τN = 0), so the curve never rotates out of a fixed plane — it is a planar curve. This does not force κ = 0; a circle has τ = 0 and nonzero curvature. A zero-torsion curve bends freely within one plane but does not spiral."

- question: "You take a helix r(t) and reparameterize it to travel along the curve twice as fast. What changes?"
  type: multiple-choice
  options:
    - "The curvature κ increases because the velocity vector is larger"
    - "The torsion τ changes sign because the direction of traversal affects twisting"
    - "The speed |r'(t)| increases, but κ and τ are unchanged"
    - "Both κ and τ double since all rates of change scale with speed"
  answer: 2
  explanation: "Curvature and torsion are intrinsic geometric properties of how the curve sits in space — they are independent of how fast you traverse it. The formula κ = |r' × r''| / |r'|³ divides out the speed dependence: if you double speed, both the numerator and denominator scale appropriately, leaving κ unchanged. Speed is a property of the parameterization, not the curve."

- question: "A circle of radius R has curvature 1/R, so a tighter circle (smaller R) has greater curvature than a wider circle."
  type: true-false
  answer: true
  explanation: "κ = 1/R captures the intuition that bending is more extreme on tighter circles. A circle of radius 0.1 has curvature 10; one of radius 10 has curvature 0.1. A straight line (infinite radius) has curvature 0. The formula measures the rate at which the unit tangent vector T rotates per unit arc length — which is faster on tighter circles."

- question: "A curve can have zero curvature everywhere but nonzero torsion at some points."
  type: true-false
  answer: false
  explanation: "If κ = 0 everywhere, the curve is a straight line — the unit tangent T never changes direction, so the principal normal N is undefined, and the Frenet-Serret frame degenerates. Torsion requires a well-defined binormal B = T × N, which does not exist when the curve fails to bend. A straight line has no twisting behavior to measure."

- question: "Why does the curvature formula κ = |r'(t) × r''(t)| / |r'(t)|³ divide by the cube of speed rather than speed itself?"
  type: short-answer
  answer: "The cross product |r' × r''| captures the bending signal but also scales with the square of speed (both r' and r'' grow when you traverse the curve faster). Dividing by |r'|² would cancel that speed scaling. But there is an additional factor of |r'| in the denominator because arc length parameterization requires one further normalization — essentially, κ is defined as the rate of change of T per unit arc length, and converting from time parameter to arc length introduces the extra |r'| in the denominator, giving the cube total."
  explanation: "The key insight is that κ must be intrinsic — a geometric property of the curve's shape, not of how fast you draw it. The cube in the denominator is exactly the correction factor that removes all parameterization dependence, leaving only the geometry."
```

## Explainer

From your work with arc length, you know how to measure how far you've traveled along a curve in 3D space, parameterizing by arc length s to get a "unit-speed" description. Curvature and torsion take this idea further: they measure *how* the curve turns and twists as you travel along it. Together they completely characterize the shape of a space curve up to rigid motion — knowing κ(s) and τ(s) at every point tells you the curve's full geometry.

**Curvature** κ captures bending. The unit tangent vector **T**(s) = r'(s) always points in the direction of travel and has length 1. As you move along the curve, **T** rotates. The rate of this rotation — |d**T**/ds| — is the curvature. A straight line has κ = 0: **T** never changes direction. A circle of radius R has constant curvature κ = 1/R: tighter circles bend more sharply. The vector d**T**/ds, when nonzero, points toward the center of curvature, and normalizing it gives the **principal normal vector** **N**. Geometrically, **T** and **N** span the **osculating plane** — the plane that best fits the curve at that point, like a tangent plane but for a curve.

**Torsion** τ measures how much the curve twists *out of* its osculating plane. If τ = 0 everywhere, the curve lies entirely in a fixed plane — it's a planar curve. Positive torsion means the curve spirals in one direction; negative torsion reverses the spiral. The **binormal vector** **B** = **T** × **N** is perpendicular to the osculating plane, and torsion is defined by −d**B**/ds = τ**N**. The three vectors {**T**, **N**, **B**} form the **Frenet-Serret frame**, a moving coordinate system that travels with the curve and rotates according to the equations dT/ds = κN, dN/ds = −κT + τB, dB/ds = −τN. These are the Frenet-Serret formulas.

In practice, you rarely have arc-length parameterization explicitly, so you use the formula κ = |r'(t) × r''(t)| / |r'(t)|³ for an arbitrary parameter t. The cross product captures the area of the parallelogram spanned by velocity and acceleration — which is large when the curve bends sharply relative to its speed. The cube of speed in the denominator corrects for the fact that faster traversal inflates the numerator without changing the geometry. For torsion, the scalar triple product formula τ = (r' × r'') · r''' / |r' × r''|² captures the out-of-plane component of the third derivative. The most important intuition: curvature and torsion are *intrinsic* properties of how the curve sits in space, independent of how fast you parameterize it.
