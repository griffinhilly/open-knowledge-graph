---
id: conductors-in-electrostatics
title: Conductors in Electrostatic Equilibrium
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law
  type: hard
- id: electric-field
  type: hard
- id: electric-potential
  type: soft
builds-toward:
- capacitance
tags:
- conductors
- electrostatics
- shielding
- induced-charge
stage: formal-systems
status: validated
---
# Conductors in Electrostatic Equilibrium

## Core Idea
In a conductor at electrostatic equilibrium, the electric field inside the bulk material is exactly zero; any excess charge resides entirely on the surface. Consequently, the interior is an equipotential region, and the field just outside the surface is perpendicular to it with magnitude σ/ε₀, where σ is the local surface charge density. These properties follow directly from Gauss's law applied to a Gaussian surface just inside the conductor surface.

## How It's Best Learned
Apply Gauss's law with a pillbox Gaussian surface at the conductor surface to derive the boundary condition E = σ/ε₀. Then analyze scenarios like a conductor with a cavity, a grounded conductor, and induced charges.

## Common Misconceptions
- Charge does not distribute uniformly on an irregular conductor; it concentrates at sharp points.
- A hollow conductor shields its interior from external fields — Faraday cage effect.
- Equilibrium is reached on timescales of ~10⁻¹⁹ s for metals, essentially instantaneous.

## Questions

```yaml
- question: "A conducting sphere carries a net positive charge. Where does this charge reside when the conductor is in electrostatic equilibrium?"
  type: multiple-choice
  options:
    - "Uniformly distributed throughout the interior of the sphere"
    - "Concentrated at the geometric center of the sphere"
    - "Entirely on the outer surface of the sphere"
    - "Half in the interior and half on the surface"
  answer: 2
  explanation: "In electrostatic equilibrium, E = 0 everywhere inside the conductor. By Gauss's law, if E = 0 on every closed surface drawn inside the conductor, the total enclosed charge must be zero. This means no charge can reside in the interior — all excess charge migrates to and stays on the outer surface. This is true regardless of the conductor's shape or the amount of charge."

- question: "A hollow conducting shell has a point charge +q placed inside its cavity. What is the electric field inside the bulk conducting material of the shell (not inside the cavity)?"
  type: multiple-choice
  options:
    - "Non-zero, pointing away from the central charge"
    - "Zero — in electrostatic equilibrium, E = 0 inside any conductor's bulk material"
    - "Equal to kq/r² at every point within the conducting material"
    - "Non-zero near the inner surface, zero near the outer surface"
  answer: 1
  explanation: "The electric field inside the bulk conducting material is always exactly zero in electrostatic equilibrium, regardless of what charges are present in the cavity or outside. Free charges in the conductor redistribute in response to the interior charge: −q is induced on the inner surface and +q appears on the outer surface. Within the bulk material itself, these rearrangements ensure E = 0. This is the Faraday cage effect."

- question: "The electric field at the surface of a conductor in electrostatic equilibrium is always perpendicular to the surface."
  type: true-false
  answer: true
  explanation: "If the field had a component tangential to the surface, that component would exert a force on free surface charges and drive a current along the surface — contradicting electrostatic equilibrium. At equilibrium, no currents flow, which requires the tangential component to be zero. Therefore, the field is purely perpendicular (normal) to the conductor's surface, with magnitude σ/ε₀."

- question: "Charge distributes uniformly over the surface of any conductor in electrostatic equilibrium."
  type: true-false
  answer: false
  explanation: "Uniform surface charge density occurs only for a perfectly spherical conductor. For an irregular conductor, charge concentrates where surface curvature is greatest — especially at sharp points or edges. The external electric field is therefore strongest near tips (σ is highest there). This is why lightning rods use sharp points: intense local fields ionize air, allowing charge to bleed off safely rather than accumulating for a destructive discharge."

- question: "Explain, using free charges and Gauss's law, why the electric field inside a conductor must be zero in electrostatic equilibrium."
  type: short-answer
  answer: "A conductor contains free electrons that respond to any electric field. If any net field existed inside, it would exert a force on electrons, causing them to accelerate — which is a current, contradicting 'electrostatic' equilibrium. At equilibrium, all motion has ceased, so the net force on every electron is zero, meaning E = 0 everywhere inside. Applying Gauss's law to any closed surface drawn within the conductor: since E = 0, the flux is zero, so the enclosed charge is zero. Since this holds for any interior surface, no charge can reside in the interior — all excess charge must live on the outer surface."
  explanation: "The argument is self-consistent: free charges rearrange until E = 0, and then Gauss's law confirms that their redistribution to the surface is the only arrangement consistent with E = 0 inside."
```

## Explainer

You already know from Gauss's law that the flux through any closed surface equals the enclosed charge divided by ε₀. Now consider a Gaussian surface drawn just inside the bulk of a conductor — infinitesimally inside the surface. In static equilibrium, there is no current flowing, so free electrons have already repositioned themselves until there is no net force on them. If any internal electric field existed, it would push electrons, contradicting equilibrium. Therefore, **E = 0 everywhere inside a conductor in electrostatic equilibrium**. By Gauss's law, zero field through every interior Gaussian surface means zero net enclosed charge — any excess charge must therefore reside entirely on the surface.

Because E = 0 throughout the interior, the work done moving a charge between any two interior points is zero. That means all interior points are at the same potential — the conductor's interior (and surface) is an **equipotential region**. This is why conductors are used as shielding: any potential difference established outside produces no field inside, regardless of the conductor's shape or the complexity of the external configuration.

At the conductor surface itself, the field is not zero — it must support the surface charge density. Using a flat pillbox Gaussian surface that straddles the surface (part inside, part outside), Gauss's law gives E = σ/ε₀ directed perpendicular to the surface, where σ is the local surface charge density. The field is always perpendicular because a tangential component would drive currents along the surface, again contradicting equilibrium.

The distribution of charge on an irregular conductor is not uniform — it concentrates where the surface curves most sharply. At a pointed tip, the surface charge density and the external field are much stronger than at a flat region. This explains lightning rods: a sharp point creates a strong local field that ionizes air and allows charge to bleed off safely. Finally, a hollow conductor provides a **Faraday cage**: external electric fields induce surface charges on the outer surface that precisely cancel the external field inside the cavity. Any object placed inside the cavity is completely shielded from external electrostatic disturbances.
