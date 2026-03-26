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
stage: expert
status: validated
---

# Angular Momentum Density in Electromagnetic Fields

## Core Idea
The angular momentum density l = r × g in electromagnetic fields arises from momentum density. Integrated over all space, this represents the orbital angular momentum of the field, distinct from the spin angular momentum carried by polarization.

## Questions

```yaml
- question: "A stationary electric charge is placed near a magnetic dipole, and the system sits undisturbed. The magnetic dipole is then slowly reduced to zero. What happens to the electric charge, and why?"
  type: multiple-choice
  options:
    - "Nothing — the charge is stationary and feels no force since the fields are static"
    - "The charge accelerates: as B decreases, Faraday induction creates an E field that exerts a torque, converting stored field angular momentum into mechanical angular momentum"
    - "The charge is repelled radially by the collapsing B field, gaining linear momentum"
    - "The charge gains angular momentum spontaneously, violating conservation laws"
  answer: 1
  explanation: "The static charge-near-dipole configuration stores angular momentum in the electromagnetic field even though nothing is moving. When the magnetic dipole is reduced to zero, the changing B field induces an E field (Faraday's law), which exerts a torque on the charge. The charge acquires mechanical angular momentum precisely equal to the angular momentum that was stored in the field. This is conservation of total angular momentum — field plus mechanical. Nothing is violated; the field angular momentum is converted to mechanical angular momentum, not created from nothing."

- question: "What distinguishes the orbital angular momentum of an electromagnetic field from its spin angular momentum?"
  type: multiple-choice
  options:
    - "Orbital comes from polarization state; spin comes from spatial beam structure"
    - "Orbital depends on spatial structure of the beam (e.g., Laguerre-Gaussian modes); spin is intrinsic to polarization state (±ℏ per photon for circular polarization)"
    - "Spin angular momentum is classical; orbital angular momentum is quantum mechanical"
    - "They are the same thing — 'orbital' and 'spin' are synonyms for EM field angular momentum"
  answer: 1
  explanation: "These are physically distinct forms of field angular momentum. Spin angular momentum is an intrinsic property of polarization: a circularly polarized photon carries ±ℏ spin angular momentum regardless of the spatial profile of the beam. Orbital angular momentum (OAM) depends on the spatial wavefront structure — a Laguerre-Gaussian beam with azimuthal index m carries mℏ OAM per photon. They can both be present simultaneously, they are separately conserved, and they couple differently to matter. Conflating them is a common error."

- question: "A static configuration of an electric charge and a magnetic dipole stores no angular momentum because hardly anything in the system is rotating."
  type: true-false
  answer: false
  explanation: "This is the key conceptual surprise of electromagnetic field angular momentum. The fields of the two sources (E from the charge, B from the dipole) cross in space, and the Poynting vector S = E × B/μ₀ is nonzero in the region around them — even though nothing is moving. The angular momentum density l = r × g = r × (ε₀ E × B) is nonzero and integrates to a real, finite total angular momentum stored in the field. Angular momentum in classical physics is not exclusively a property of moving matter; fields carry it too."

- question: "Conservation of angular momentum in electrodynamics requires that primarily the mechanical angular momentum of charged particles is conserved."
  type: true-false
  answer: false
  explanation: "Mechanical angular momentum alone is not conserved in electrodynamics — only the *total* angular momentum (mechanical + field) is. This is analogous to linear momentum: the electromagnetic field carries momentum density g = ε₀(E × B), and similarly carries angular momentum density l = r × g. When fields and charged matter interact, angular momentum can transfer between the field and mechanical degrees of freedom. Tracking only mechanical angular momentum will appear to show violations of conservation; accounting for field angular momentum restores it."

- question: "How does the existence of electromagnetic field angular momentum require us to modify the classical statement of conservation of angular momentum?"
  type: short-answer
  answer: "The conservation law must be extended to include the angular momentum carried by the electromagnetic field, not just mechanical angular momentum. The total conserved quantity is L_total = L_mechanical + L_field, where L_field = ∫ (r × g) dV = ε₀ ∫ (r × (E × B)) dV. When charged matter and fields interact, angular momentum can flow between them, so neither is separately conserved — only the sum is."
  explanation: "This is a direct parallel to linear momentum: EM fields carry momentum density g = S/c², and angular momentum density l = r × g. Conservation of angular momentum applies to the total system, field included. The Einstein-de Haas and Barnett effects are macroscopic demonstrations: magnetizing an iron bar causes it to rotate (spin angular momentum transfers to mechanical rotation), with the EM field serving as the intermediary. The correct statement is that the universe conserves total angular momentum — mechanical plus electromagnetic field contributions."
```

## Explainer

You know from your prerequisite on electromagnetic field momentum that the EM field carries linear momentum with density **g** = ε₀(**E** × **B**) = **S**/c², where **S** is the Poynting vector. Angular momentum is built from linear momentum the same way in mechanics: **L** = **r** × **p**. For a continuous field, the **angular momentum density** is **l** = **r** × **g** = ε₀(**r** × (**E** × **B**)). Integrating this density over all space gives the total angular momentum stored in the electromagnetic field.

The existence of field angular momentum leads to a striking consequence: static configurations — an electric charge near a magnetic dipole, for example — can store angular momentum even though nothing is moving. When you disassemble such a configuration (by reducing the magnetic dipole to zero, say), the field angular momentum must go somewhere. As the B field changes, the Faraday-induced E field exerts a torque on the charge, and the charge acquires mechanical angular momentum exactly equal to the angular momentum that was stored in the field. This is angular momentum conservation applied to fields and matter together. The total angular momentum (field + mechanical) is conserved — not field alone, not matter alone.

**Orbital angular momentum** of the field (from **l** = **r** × **g**) must be distinguished from **spin angular momentum**, which is carried by circularly polarized electromagnetic waves. A circularly polarized photon carries spin ±ℏ regardless of its intensity or frequency; this is an intrinsic property of the wave's polarization state. Orbital angular momentum, by contrast, depends on the spatial structure of the beam — a Laguerre-Gaussian laser mode with azimuthal index m carries mℏ orbital angular momentum per photon. Both forms are physically real and separately conserved.

The angular momentum stored in a static field configuration is not just a theoretical curiosity — it has measurable consequences. The **Einstein-de Haas effect** (magnetizing a suspended iron cylinder causes it to rotate) and the **Barnett effect** (rotating a ferromagnet magnetizes it) are direct manifestations of angular momentum exchange between spin degrees of freedom and mechanical rotation, with EM field angular momentum playing the mediating role in the full accounting. Conservation of total angular momentum — mechanical plus field — is the unifying principle across all these phenomena.
