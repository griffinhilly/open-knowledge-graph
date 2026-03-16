---
id: em-angular-momentum-density
title: Angular Momentum Density in Electromagnetic Fields
domain: physics
course: electrodynamics
prerequisites:
- id: em-field-momentum-density
  type: hard
- id: conservation-of-angular-momentum
  type: soft
tags:
- angular-momentum
- field-momentum
- orbital-angular-momentum
stage: advanced
status: draft
---

# Angular Momentum Density in Electromagnetic Fields

## Core Idea
The angular momentum density l = r × g in electromagnetic fields arises from momentum density. Integrated over all space, this represents the orbital angular momentum of the field, distinct from the spin angular momentum carried by polarization.

## Explainer

You know from your prerequisite on electromagnetic field momentum that the EM field carries linear momentum with density **g** = ε₀(**E** × **B**) = **S**/c², where **S** is the Poynting vector. Angular momentum is built from linear momentum the same way in mechanics: **L** = **r** × **p**. For a continuous field, the **angular momentum density** is **l** = **r** × **g** = ε₀(**r** × (**E** × **B**)). Integrating this density over all space gives the total angular momentum stored in the electromagnetic field.

The existence of field angular momentum leads to a striking consequence: static configurations — an electric charge near a magnetic dipole, for example — can store angular momentum even though nothing is moving. When you disassemble such a configuration (by reducing the magnetic dipole to zero, say), the field angular momentum must go somewhere. As the B field changes, the Faraday-induced E field exerts a torque on the charge, and the charge acquires mechanical angular momentum exactly equal to the angular momentum that was stored in the field. This is angular momentum conservation applied to fields and matter together. The total angular momentum (field + mechanical) is conserved — not field alone, not matter alone.

**Orbital angular momentum** of the field (from **l** = **r** × **g**) must be distinguished from **spin angular momentum**, which is carried by circularly polarized electromagnetic waves. A circularly polarized photon carries spin ±ℏ regardless of its intensity or frequency; this is an intrinsic property of the wave's polarization state. Orbital angular momentum, by contrast, depends on the spatial structure of the beam — a Laguerre-Gaussian laser mode with azimuthal index m carries mℏ orbital angular momentum per photon. Both forms are physically real and separately conserved.

The angular momentum stored in a static field configuration is not just a theoretical curiosity — it has measurable consequences. The **Einstein-de Haas effect** (magnetizing a suspended iron cylinder causes it to rotate) and the **Barnett effect** (rotating a ferromagnet magnetizes it) are direct manifestations of angular momentum exchange between spin degrees of freedom and mechanical rotation, with EM field angular momentum playing the mediating role in the full accounting. Conservation of total angular momentum — mechanical plus field — is the unifying principle across all these phenomena.
