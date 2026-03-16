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
status: draft
---

# Curvature and Torsion of Space Curves

## Core Idea
Curvature κ = |dT/ds| measures how sharply a curve bends; torsion τ measures how much it twists out of its oscillating plane. For a curve r(t), κ = |r'(t) × r''(t)| / |r'(t)|³. Torsion reveals how much the curve deviates from being planar.

## Explainer

From your work with arc length, you know how to measure how far you've traveled along a curve in 3D space, parameterizing by arc length s to get a "unit-speed" description. Curvature and torsion take this idea further: they measure *how* the curve turns and twists as you travel along it. Together they completely characterize the shape of a space curve up to rigid motion — knowing κ(s) and τ(s) at every point tells you the curve's full geometry.

**Curvature** κ captures bending. The unit tangent vector **T**(s) = r'(s) always points in the direction of travel and has length 1. As you move along the curve, **T** rotates. The rate of this rotation — |d**T**/ds| — is the curvature. A straight line has κ = 0: **T** never changes direction. A circle of radius R has constant curvature κ = 1/R: tighter circles bend more sharply. The vector d**T**/ds, when nonzero, points toward the center of curvature, and normalizing it gives the **principal normal vector** **N**. Geometrically, **T** and **N** span the **osculating plane** — the plane that best fits the curve at that point, like a tangent plane but for a curve.

**Torsion** τ measures how much the curve twists *out of* its osculating plane. If τ = 0 everywhere, the curve lies entirely in a fixed plane — it's a planar curve. Positive torsion means the curve spirals in one direction; negative torsion reverses the spiral. The **binormal vector** **B** = **T** × **N** is perpendicular to the osculating plane, and torsion is defined by −d**B**/ds = τ**N**. The three vectors {**T**, **N**, **B**} form the **Frenet-Serret frame**, a moving coordinate system that travels with the curve and rotates according to the equations dT/ds = κN, dN/ds = −κT + τB, dB/ds = −τN. These are the Frenet-Serret formulas.

In practice, you rarely have arc-length parameterization explicitly, so you use the formula κ = |r'(t) × r''(t)| / |r'(t)|³ for an arbitrary parameter t. The cross product captures the area of the parallelogram spanned by velocity and acceleration — which is large when the curve bends sharply relative to its speed. The cube of speed in the denominator corrects for the fact that faster traversal inflates the numerator without changing the geometry. For torsion, the scalar triple product formula τ = (r' × r'') · r''' / |r' × r''|² captures the out-of-plane component of the third derivative. The most important intuition: curvature and torsion are *intrinsic* properties of how the curve sits in space, independent of how fast you parameterize it.
