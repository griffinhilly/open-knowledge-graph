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
- id: force-on-current-carrying-conductor
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

## Questions

```yaml
- question: "A current element Idℓ points directly toward the field point (the angle between dℓ and r̂ is zero). What is its contribution to the magnetic field at that point?"
  type: multiple-choice
  options:
    - "Maximum contribution — the element is aligned with the displacement vector"
    - "Zero — the cross product dℓ × r̂ vanishes when they are parallel"
    - "μ₀I/(4πr²) — the standard Biot-Savart magnitude without angular dependence"
    - "It contributes only a radial component, not a tangential one"
  answer: 1
  explanation: "The Biot-Savart law has the cross product dℓ × r̂, whose magnitude is |dℓ||r̂|sin θ. When dℓ and r̂ are parallel (θ = 0), sin θ = 0 and the contribution is zero. This is the opposite of the intuitive 'line-of-sight' expectation from Coulomb's law. Only current elements oriented at an angle to the displacement vector contribute to B. Elements pointing directly at you generate no field at your location."

- question: "Why is the Biot-Savart integral especially simple to evaluate for a circular current loop at its own center?"
  type: multiple-choice
  options:
    - "Because the 1/r² factor cancels with the circumference, leaving a constant integrand"
    - "Because every element dℓ is perpendicular to r̂ (sin θ = 1) and all elements contribute in the same direction"
    - "Because the current loops cancel, leaving only the net axial component"
    - "Because the field at the center is zero by symmetry"
  answer: 1
  explanation: "At the center of a circular loop, the displacement vector r̂ from any element to the center always points radially inward — perpendicular to the tangential current element dℓ. This means sin θ = 1 for every element, so the cross product has its maximum magnitude everywhere. Furthermore, by symmetry, every element's dB contribution points in the same axial direction. The integral reduces to just integrating dℓ around the circumference (giving 2πR), yielding B = μ₀I/(2R). The perpendicularity is what makes the simplification possible."

- question: "The magnetic field produced by a long straight current-carrying wire points radially outward from the wire, like the electric field from a line charge."
  type: true-false
  answer: false
  explanation: "This is a fundamental distinction between magnetism and electrostatics. The electric field from a line charge points radially outward (away from the wire) because Coulomb's law has no directional preference beyond the radial. The Biot-Savart law, however, involves a cross product: the magnetic field from a straight wire circles around the wire in closed loops (azimuthal direction), not radially outward. The right-hand rule gives the direction: curl your right-hand fingers in the direction B circles when your thumb points in the current direction."

- question: "A current element at angle θ = 90° to the displacement vector r̂ produces the maximum possible magnetic field contribution at the field point."
  type: true-false
  answer: true
  explanation: "The Biot-Savart magnitude is dB = (μ₀/4π)(I dℓ sin θ)/r². The sin θ factor is maximized when θ = 90°, meaning the current element is perpendicular to the line connecting it to the field point. This is exactly the geometry of the circular loop at its center (every element is tangential, displacement is radial — always perpendicular), which is why that geometry gives such a clean integral."

- question: "Explain why the Biot-Savart law requires a cross product while Coulomb's law only needs a scalar multiplication by r̂."
  type: short-answer
  answer: "Coulomb's law describes a radially symmetric source: a point charge pushes or pulls directly along the line connecting it to the field point. The field direction is always r̂. Magnetic fields, by contrast, are generated by moving charges (current), and the field direction depends on both the current direction and the displacement — it is perpendicular to both simultaneously. The cross product dℓ × r̂ is precisely the operation that produces a vector perpendicular to two given vectors, encoding this geometry automatically. The sin θ factor that results means elements pointing toward you contribute nothing, while transverse elements contribute most."
  explanation: "This contrast reveals a deep asymmetry between electric and magnetic fields. Electric fields can be described by a scalar potential; magnetic fields require a vector potential. The cross product in Biot-Savart is not a mathematical convenience — it reflects the physical fact that magnetic forces act perpendicular to the velocity of the source charge, an entirely different geometry than the radial Coulomb force."
```

## Explainer

The Biot-Savart law is to magnetism what Coulomb's law is to electrostatics: it tells you the magnetic field produced by a source, built up element by element. The key conceptual move is the same one you used in integration — divide the source into infinitesimal pieces, find the contribution from each piece, and sum. Here the "source" is a steady current, and each piece is an infinitesimal current element Id**l**: a short length of wire d**l** carrying current I. Each element contributes a tiny field dB, and the total field is the integral of all contributions.

What makes Biot-Savart geometrically richer than Coulomb's law is the **cross product** d**l** × r̂. In Coulomb's law, the field from a point charge points radially outward — symmetric in all directions. In Biot-Savart, the field from a current element circles around the wire: it is perpendicular both to the current direction and to the line from the element to the field point. Your prerequisite knowledge of the cross product is essential here — the cross product automatically gives you this perpendicular direction and has magnitude sin θ, so current elements pointing directly toward your field point (θ = 0) contribute nothing. Only elements oriented at an angle to the displacement vector contribute to the field.

The long straight wire result B = μ₀I/(2πr) is the archetype you should derive once and internalize. The strategy: set up coordinates with the wire along the z-axis, write d**l** = dz ẑ, express r̂ as a function of z and the perpendicular distance r, evaluate the cross product, and integrate from −∞ to +∞. The integral is a standard form. The result says the field circles around the wire at a distance that falls off as 1/r — faster than the 1/r² of Coulomb's law because the field from distant elements cancels transversely. **Symmetry** is what makes this tractable: you can argue the field must be azimuthal and depend only on distance, then choose a field point and integrate.

For the circular loop at its center, the geometry is simpler because every element d**l** on the loop is perpendicular to r̂ (which points from the element to the center), so sin θ = 1 for every element. The field from every element points in the same direction (along the axis), and the integral reduces to just integrating d**l** around the circumference 2πR. This gives B = μ₀I/(2R). When the geometry lacks this perfect alignment, off-axis fields require more work — but the principle is always the same: identify d**l**, write r̂, take the cross product, integrate.
