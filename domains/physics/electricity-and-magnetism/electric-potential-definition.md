---
id: electric-potential-definition
title: Electric Potential and Potential Difference
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law-problem-solving
  type: hard
- id: line-integrals-scalar
  type: hard
builds-toward:
- potential-energy-systems
- equipotential-surfaces
- relationship-e-field-potential
tags:
- potential
- voltage
- scalar
stage: formal-systems
status: draft
---

# Electric Potential and Potential Difference

## Core Idea
Electric potential V at a point is defined as work per unit charge to bring a test charge from infinity: V = U/q. Potential difference ΔV = V_B − V_A is path-independent and related to work done by the field.

## Explainer

From Gauss's law, you know how to find the electric field **E** for symmetric charge distributions. From scalar line integrals, you know how to accumulate a quantity along a path. Electric potential brings these two tools together into something more powerful than working with **E** directly: instead of a vector at every point in space, potential gives you a single **scalar** number at each point, encoding all the same information in a form that is far easier to work with algebraically.

The key definition is V = U/q: the electric potential at a point equals the electric potential energy per unit positive test charge placed there. Equivalently, V(r) = −∫(∞ to r) **E** · d**l**, where you integrate the field along any path from the reference point at infinity to r. The fact that this integral gives the same answer regardless of path taken is not obvious — it follows from the fact that the electric force is **conservative**, a consequence of Coulomb's law having a 1/r² form. You encountered this implicitly when using Gauss's law: the field depends only on radial distance from a point charge, so any tangential displacement does zero work against it.

The practical meaning of potential is this: a positive test charge naturally moves from regions of high potential to low potential, losing potential energy and gaining kinetic energy — exactly like a ball rolling downhill. The "landscape" of potential values in space is a terrain whose hills and valleys tell you which way forces push charges. The potential difference ΔV = V_B − V_A is what matters physically: it is the work per unit charge done by the electric field as a charge moves from A to B. If ΔV is negative (B is at lower potential than A), the field does positive work on a positive charge moving from A to B.

The connection back to **E** is that **E** = −∇V: the electric field points in the direction of steepest decrease in potential, always "downhill" on the potential landscape. **Equipotential surfaces** — surfaces of constant V — are always perpendicular to **E**, because no work is done moving a charge along them. These structures (potential as a scalar landscape, **E** as the gradient pointing downhill) recur throughout electrostatics, capacitance, and eventually quantum mechanics, where the potential energy landscape directly shapes the allowed wavefunctions of bound particles.
