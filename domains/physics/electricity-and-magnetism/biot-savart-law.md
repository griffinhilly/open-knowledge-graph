---
id: biot-savart-law
title: Biot-Savart Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-field-intro
  type: hard
- id: electric-current-and-resistance
  type: hard
- id: cross-product
  type: hard
- id: line-integrals-vector-fields
  type: soft
- id: magnetic-force-on-current-carrying-conductors
  type: soft
builds-toward:
- amperes-law
- magnetic-flux-and-induction
tags:
- Biot-Savart
- magnetic-field-calculation
- current
- integration
stage: formal-systems
status: validated
---
# Biot-Savart Law

## Core Idea
The Biot-Savart law gives the magnetic field contribution dB from an infinitesimal current element Id l: dB = (μ₀/4π) (Id l × r̂)/r². The total field is obtained by integrating over the entire current distribution. For a long straight wire at distance r, the result is B = μ₀I/(2πr). For a circular current loop of radius R at its center, B = μ₀I/(2R). The permeability of free space μ₀ = 4π × 10⁻⁷ T·m/A.

## How It's Best Learned
First verify the formula for a long straight wire by integrating the Biot-Savart law, then use the result without re-deriving it for composite geometries. Always identify the symmetry and dominant field direction before computing the integral.

## Common Misconceptions
- Biot-Savart applies to steady currents; it cannot be directly applied to accelerating charges.
- The cross product d l × r̂ determines the direction of dB — do not just look at the magnitude.
- Unlike Coulomb's law, the Biot-Savart integrand is not radially symmetric.

## Explainer

The Biot-Savart law is to magnetism what Coulomb's law is to electrostatics: it tells you the magnetic field produced by a source, built up element by element. The key conceptual move is the same one you used in integration — divide the source into infinitesimal pieces, find the contribution from each piece, and sum. Here the "source" is a steady current, and each piece is an infinitesimal current element Id**l**: a short length of wire d**l** carrying current I. Each element contributes a tiny field dB, and the total field is the integral of all contributions.

What makes Biot-Savart geometrically richer than Coulomb's law is the **cross product** d**l** × r̂. In Coulomb's law, the field from a point charge points radially outward — symmetric in all directions. In Biot-Savart, the field from a current element circles around the wire: it is perpendicular both to the current direction and to the line from the element to the field point. Your prerequisite knowledge of the cross product is essential here — the cross product automatically gives you this perpendicular direction and has magnitude sin θ, so current elements pointing directly toward your field point (θ = 0) contribute nothing. Only elements oriented at an angle to the displacement vector contribute to the field.

The long straight wire result B = μ₀I/(2πr) is the archetype you should derive once and internalize. The strategy: set up coordinates with the wire along the z-axis, write d**l** = dz ẑ, express r̂ as a function of z and the perpendicular distance r, evaluate the cross product, and integrate from −∞ to +∞. The integral is a standard form. The result says the field circles around the wire at a distance that falls off as 1/r — faster than the 1/r² of Coulomb's law because the field from distant elements cancels transversely. **Symmetry** is what makes this tractable: you can argue the field must be azimuthal and depend only on distance, then choose a field point and integrate.

For the circular loop at its center, the geometry is simpler because every element d**l** on the loop is perpendicular to r̂ (which points from the element to the center), so sin θ = 1 for every element. The field from every element points in the same direction (along the axis), and the integral reduces to just integrating d**l** around the circumference 2πR. This gives B = μ₀I/(2R). When the geometry lacks this perfect alignment, off-axis fields require more work — but the principle is always the same: identify d**l**, write r̂, take the cross product, integrate.
