---
id: electromagnetic-angular-momentum-radiation
title: Electromagnetic Angular Momentum
domain: physics
course: electrodynamics
prerequisites:
- id: poynting-vector-energy-flow
  type: hard
- id: angular-momentum
  type: hard
tags:
- angular-momentum
- orbital-angular-momentum
- spin-angular-momentum
stage: advanced
status: draft
---

# Electromagnetic Angular Momentum

## Core Idea
Electromagnetic fields carry angular momentum given by L = ε₀∫(r × (E × B))d³r, with density l = ε₀(E × B)/c². This reveals that light carries intrinsic angular momentum, leading to observable effects like radiation pressure torque and optical manipulation of particles. Orbital angular momentum (from helical phase structure) and spin angular momentum (from circular polarization) contribute independently, with important applications in optical tweezers and quantum information.

## Explainer

From your study of the Poynting vector and from classical mechanics, you know two things: electromagnetic fields carry energy with flux S = (E × B)/μ₀, and angular momentum is defined as L = r × p for particles. These two ideas merge in electromagnetic angular momentum — the field itself stores angular momentum, not just energy and linear momentum.

The linear momentum density of the electromagnetic field is g = ε₀(E × B) = S/c². This is already a non-obvious result: fields exert radiation pressure and carry momentum even in empty space. Angular momentum density follows naturally by taking the cross product of position with momentum density: l = r × g = ε₀(r × (E × B))/c². Integrating over all space gives the total **electromagnetic angular momentum** L = ε₀∫(r × (E × B))d³r. Crucially, this is a property of the field configuration, not of any individual particle — it exists wherever there are crossed E and B fields.

A striking example: a charged sphere (electric field radially outward) sitting inside a solenoid (uniform B field along the axis) carries electromagnetic angular momentum even though nothing is moving. When the solenoid is switched off, the changing B field induces an electric field (by Faraday's law) that exerts a tangential force on the charged sphere, causing it to rotate. Total angular momentum is conserved — the angular momentum stored in the fields is transferred to mechanical angular momentum of the sphere. This is the **Feynman disk paradox**, and it is one of the most counterintuitive demonstrations that fields are physically real carriers of mechanical quantities.

For radiation, two distinct types of angular momentum arise. **Spin angular momentum** is associated with circular or elliptical polarization — circularly polarized light carries ±ℏ per photon (quantum mechanically). **Orbital angular momentum** (OAM) arises from helical phase structure in the wavefront: a beam whose phase winds by 2πℓ around the beam axis carries Lℓ per photon, where ℓ is an integer. These two contributions add independently and can be manipulated separately using optical elements. OAM beams have revolutionized optical tweezers (rotating trapped particles), spatial-mode multiplexing in optical fiber communications, and protocols in quantum information where each OAM value labels an independent channel — a direct technological application of field angular momentum.
