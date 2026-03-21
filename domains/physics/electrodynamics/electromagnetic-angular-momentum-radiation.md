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

## Questions

```yaml
- question: "A charged sphere sits stationary inside a solenoid carrying a steady current. Before the solenoid is switched off, what is the angular momentum of the system?"
  type: multiple-choice
  options:
    - "Zero — nothing is moving, so no angular momentum is present"
    - "Nonzero — angular momentum is stored in the electromagnetic field configuration, even with static fields and no motion"
    - "Nonzero — the charged sphere is slowly precessing due to the static magnetic field"
    - "Undefined — angular momentum requires a well-defined rotation axis, and this system is symmetric"
  answer: 1
  explanation: "This is the core lesson of electromagnetic angular momentum: the fields themselves carry angular momentum via l = ε₀(r × (E × B)). The electric field (from the charge) and magnetic field (from the solenoid) together store angular momentum throughout the overlapping field region, even though neither object is moving. When the solenoid is switched off, the disappearing B field induces an E field (Faraday's law) that exerts a tangential force on the charged sphere, setting it rotating — field angular momentum converts to mechanical angular momentum. This is the Feynman disk paradox."

- question: "Orbital angular momentum (OAM) and spin angular momentum (SAM) of a light beam differ in which of the following ways?"
  type: multiple-choice
  options:
    - "OAM arises from circular polarization; SAM arises from helical phase structure in the wavefront"
    - "OAM arises from helical phase structure in the wavefront; SAM arises from circular or elliptical polarization"
    - "OAM and SAM are two names for the same physical quantity — the total angular momentum of the beam"
    - "OAM is purely quantum mechanical, while SAM is a classical wave property"
  answer: 1
  explanation: "The two types are physically distinct and arise from different aspects of the field. Spin angular momentum (SAM) is tied to polarization state: circularly polarized light carries ±ℏ per photon. Orbital angular momentum (OAM) arises from helical phase structure — the phase winds by 2πℓ around the beam axis, carrying ℓℏ per photon. They can be manipulated independently using optical elements (waveplates change SAM; spiral phase plates change OAM), which has enabled independent control in optical tweezer and communications applications."

- question: "When the current in a solenoid enclosing a stationary charged sphere is switched off, the sphere begins to rotate — and this rotation is explained by conservation of angular momentum."
  type: true-false
  answer: true
  explanation: "This is exactly the Feynman disk paradox. The changing B field induces a tangential E field (Faraday's law) that exerts a torque on the charged sphere. The sphere acquires mechanical angular momentum precisely equal to the angular momentum that was stored in the crossed E and B fields. Total angular momentum is conserved: field angular momentum converts to mechanical angular momentum. Nothing was 'spinning' before, yet the system had nonzero angular momentum stored in the fields."

- question: "The electromagnetic angular momentum density at a point requires a moving charge at that point — it cannot be nonzero in the empty space between a static charge distribution and a static magnetic field."
  type: true-false
  answer: false
  explanation: "The angular momentum density l = ε₀(r × (E × B)) depends only on the values of E and B at each point — not on the presence of charges there. Wherever both an electric field and a magnetic field are present with appropriate spatial geometry, angular momentum is stored in the fields even in vacuum. The charged sphere + solenoid example is precisely a static configuration with angular momentum distributed throughout the space where both E and B overlap. Fields carry energy, momentum, and angular momentum as properties of space, not just of charges."

- question: "The Feynman disk paradox involves a stationary charged ring and a solenoid with no moving parts. How does this demonstrate that angular momentum can be stored in electromagnetic fields, and what happens when the solenoid is switched off?"
  type: short-answer
  answer: "The charged ring produces a radial electric field E; the solenoid produces an axial magnetic field B. The angular momentum density l = ε₀(r × (E × B)) is nonzero throughout the space where both fields overlap, even though nothing is moving. Initial mechanical angular momentum is zero, but total angular momentum (field + mechanical) is nonzero. When the solenoid is switched off, the disappearing B field induces an azimuthal E field by Faraday's law, which exerts a tangential force on the charged ring, causing it to rotate. The mechanical angular momentum gained by the ring equals the field angular momentum that was initially stored — angular momentum is conserved, converted from field form to mechanical form."
  explanation: "The paradox resolves only if you accept that fields are real physical entities carrying conserved quantities, not just calculational conveniences. The pre-switch state has zero mechanical angular momentum but nonzero total angular momentum; the post-switch state has that angular momentum carried mechanically. This makes field angular momentum physically real in the strongest sense: it participates in conservation laws."
```

## Explainer

From your study of the Poynting vector and from classical mechanics, you know two things: electromagnetic fields carry energy with flux S = (E × B)/μ₀, and angular momentum is defined as L = r × p for particles. These two ideas merge in electromagnetic angular momentum — the field itself stores angular momentum, not just energy and linear momentum.

The linear momentum density of the electromagnetic field is g = ε₀(E × B) = S/c². This is already a non-obvious result: fields exert radiation pressure and carry momentum even in empty space. Angular momentum density follows naturally by taking the cross product of position with momentum density: l = r × g = ε₀(r × (E × B))/c². Integrating over all space gives the total **electromagnetic angular momentum** L = ε₀∫(r × (E × B))d³r. Crucially, this is a property of the field configuration, not of any individual particle — it exists wherever there are crossed E and B fields.

A striking example: a charged sphere (electric field radially outward) sitting inside a solenoid (uniform B field along the axis) carries electromagnetic angular momentum even though nothing is moving. When the solenoid is switched off, the changing B field induces an electric field (by Faraday's law) that exerts a tangential force on the charged sphere, causing it to rotate. Total angular momentum is conserved — the angular momentum stored in the fields is transferred to mechanical angular momentum of the sphere. This is the **Feynman disk paradox**, and it is one of the most counterintuitive demonstrations that fields are physically real carriers of mechanical quantities.

For radiation, two distinct types of angular momentum arise. **Spin angular momentum** is associated with circular or elliptical polarization — circularly polarized light carries ±ℏ per photon (quantum mechanically). **Orbital angular momentum** (OAM) arises from helical phase structure in the wavefront: a beam whose phase winds by 2πℓ around the beam axis carries Lℓ per photon, where ℓ is an integer. These two contributions add independently and can be manipulated separately using optical elements. OAM beams have revolutionized optical tweezers (rotating trapped particles), spatial-mode multiplexing in optical fiber communications, and protocols in quantum information where each OAM value labels an independent channel — a direct technological application of field angular momentum.
