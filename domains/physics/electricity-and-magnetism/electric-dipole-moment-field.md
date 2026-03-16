---
id: electric-dipole-moment-field
title: Electric Dipole Moment and Dipole Field
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: relationship-e-field-potential
  type: hard
- id: taylor-polynomials
  type: soft
builds-toward:
- dielectric-materials-polarization
tags:
- dipole
- moment
- far-field
stage: formal-systems
status: draft
---

# Electric Dipole Moment and Dipole Field

## Core Idea
An electric dipole (two opposite charges ±q separated by d) has dipole moment p = qd. Far from the dipole, the potential varies as V ∝ p⋅r̂/r², and the field dominates multipole expansions of many charge distributions.

## Explainer

When two equal and opposite charges +q and −q are placed close together, the system is electrically neutral overall — but not everywhere. Up close the full complexity of both charges matters, but from far away the charges nearly cancel and the field simplifies dramatically. The surviving leading-order effect is characterized by a single vector called the **electric dipole moment**: p⃗ = qd⃗, where d⃗ points from the negative to the positive charge and the magnitude qd measures both the strength of the charges and their separation.

The dipole potential falls off as V ∝ p⋅r̂/r², compared to the 1/r monopole potential of a single charge. This 1/r² decay arises from the near-cancellation: the +q is slightly closer than the −q, so their potentials don't quite cancel. The leftover piece is the dipole term — the first correction in a systematic expansion. If you know Taylor polynomials, you can see this explicitly by expanding 1/|r − d/2| for small d: the 1/r terms cancel between the two charges, and the next term gives the 1/r² potential. Successive corrections (quadrupole, octupole, ...) fall off as 1/r³, 1/r⁴, and the dipole dominates at large distances for any neutral charge distribution.

The dipole electric field has a characteristic angular pattern. Along the **dipole axis** (the line joining the charges), the field points in the same direction as p⃗ with magnitude 2p/(4πε₀r³). In the **equatorial plane** (perpendicular to p⃗, through the midpoint), the field points antiparallel to p⃗ with magnitude p/(4πε₀r³). The angular factors cosθ and sinθ in the field components give the dipole pattern its distinctive lobed shape — two lobes along the axis and a weaker fringe in the equatorial plane.

Why does this matter beyond a simple two-charge toy problem? Because the **multipole expansion** is universal: any charge distribution — a polar molecule, an antenna, an atomic nucleus — can be decomposed into monopole + dipole + quadrupole + ... contributions. For a neutral, asymmetric molecule like water, the monopole term vanishes and the dipole term dominates at large distances. This is why dipole moments control intermolecular forces, dielectric behavior, and the absorption of microwave radiation. The abstract concept of p⃗ = qd⃗ you learn here recurs throughout electromagnetism, quantum mechanics, and molecular physics as the central quantity describing how charge distributions interact with external fields.
