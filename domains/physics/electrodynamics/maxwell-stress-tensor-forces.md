---
id: maxwell-stress-tensor-forces
title: Maxwell Stress Tensor and Field Forces
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-stress-tensor
  type: hard
- id: em-field-momentum-density
  type: hard
tags:
- stress-tensor
- field-forces
- radiation-pressure
stage: expert
status: draft
---

# Maxwell Stress Tensor and Field Forces

## Core Idea
The Maxwell stress tensor T_ij represents the flow of electromagnetic momentum. Its divergence gives the force density on matter, enabling calculation of electromagnetic pressure, tension, and forces between current-carrying conductors without explicit use of Lorentz force.

## Questions

```yaml
- question: "An engineer wants to find the net electromagnetic force on a charged capacitor. Instead of integrating the Lorentz force density ρE over the volume of the charges, she draws a spherical surface around the capacitor and integrates T·dA. Why can she choose any closed surface enclosing the capacitor, not just the one geometrically closest to it?"
  type: multiple-choice
  options:
    - "The stress tensor is constant in free space, so the surface shape does not matter"
    - "By the divergence theorem, the surface integral of the stress tensor over any closed surface gives the same total force as long as the same sources are enclosed — just as Gauss's law gives the same flux for any surface enclosing the same charge"
    - "The electric and magnetic fields cancel outside the capacitor, so the integrand is zero away from the surface"
    - "The stress tensor is only defined at the surface of the object, so any enclosing surface maps to the same values"
  answer: 1
  explanation: "This is the key advantage of the stress-tensor method. In static fields, ∇·T̄ = f (force density), so the total force on enclosed sources equals ∮ T̄·dA for any closed surface by the divergence theorem — analogous to how ∮ E·dA = Q_enc/ε₀ for any Gaussian surface. This freedom to choose a convenient surface (where the fields may be simpler or more symmetric) is exactly what makes the method powerful in practice. The Lorentz force method requires integrating over all the sources; the stress tensor method only requires integrating over the field at an arbitrary enclosing surface."

- question: "A plane electromagnetic wave with intensity I strikes a surface. If the surface is perfectly absorbing, the radiation pressure is I/c. What is the radiation pressure if the surface is perfectly reflecting?"
  type: multiple-choice
  options:
    - "Still I/c — the total energy deposited per unit time is the same regardless of reflection"
    - "2I/c — perfect reflection reverses the wave's momentum, so the impulse delivered to the surface is twice as large"
    - "I/(2c) — only half the wave's momentum is available for transfer to a reflecting surface"
    - "0 — a perfectly reflecting surface returns all the wave's energy, so it exerts no net force"
  answer: 1
  explanation: "Momentum transfer to the surface equals the change in the wave's momentum. An absorbed wave delivers momentum flux I/c (its full forward momentum is lost). A perfectly reflected wave reverses direction: its momentum changes by 2 × (I/c), so the force per unit area is 2I/c. This factor-of-two difference is directly computable from the Maxwell stress tensor: the stress on an absorbing surface includes only the incoming wave's momentum flux, while the stress on a reflecting surface includes both the incoming and outgoing wave contributions. This doubling is why reflective solar sails are more efficient than absorbing ones."

- question: "In the Maxwell stress tensor, the diagonal components (T_xx, T_yy, T_zz) represent electromagnetic shear stresses, while the off-diagonal components represent electromagnetic pressure."
  type: true-false
  answer: false
  explanation: "This is reversed. The diagonal components represent electromagnetic *pressure* — force per unit area perpendicular to a surface — while the off-diagonal components represent *shear stress* — force per unit area parallel to a surface. The physical intuition is that T_ij is the flux of the i-th component of momentum in the j-th direction; when i = j (diagonal), the momentum flux is perpendicular to the surface (pressure); when i ≠ j (off-diagonal), the momentum flux is parallel to the surface (shear)."

- question: "To use the Maxwell stress tensor to calculate the force on a physical object, you must integrate over a surface that lies exactly on the object's boundary — you cannot use a more distant enclosing surface."
  type: true-false
  answer: false
  explanation: "The freedom to choose any convenient closed surface enclosing the object is one of the method's main practical advantages. In static cases, ∮ T̄·dA is the same for every closed surface enclosing the same sources, by the divergence theorem. You might choose a distant spherical surface where the fields have simpler form (e.g., pure radiation fields), a surface where boundary conditions are known analytically, or a surface aligned with coordinate symmetries. Choosing the boundary surface as the object's own surface can sometimes be the hardest choice because the fields may be complex there."

- question: "How is using the Maxwell stress tensor to calculate force on an object analogous to using a Gaussian surface in electrostatics? What does this analogy reveal about the physical meaning of the stress tensor?"
  type: short-answer
  answer: "In electrostatics, Gauss's law says ∮ E·dA = Q_enc/ε₀: the total electric flux through any closed surface equals the total enclosed charge. You can compute the charge enclosed without knowing the detailed charge distribution — just the field at the surface. The Maxwell stress tensor works the same way for force: ∮ T̄·dA = F_enc (in static fields), so the total electromagnetic force on everything inside the surface equals the stress-tensor flux through the surface. You can compute the force without knowing the detailed current/charge distribution inside — just the field at the surface. This reveals that T_ij is a *momentum flux tensor*: it tells you how fast electromagnetic momentum is flowing through unit area in a given direction. Force is the rate of momentum transfer, so integrating T over a surface gives the total rate at which the field delivers momentum to enclosed sources."
  explanation: "The analogy is deep: both Gauss's law and the stress-tensor method convert a volume integral (over sources) into a surface integral (over fields). Both exploit the divergence theorem. Both let you choose the most convenient surface rather than integrating over the actual source distribution. The stress tensor is essentially a '3×3 Gauss's law' for electromagnetic momentum rather than charge."
```

## Explainer

The Lorentz force law **f** = ρ**E** + **J** × **B** gives the force density on charges and currents directly. But integrating this over complex geometries is often difficult, especially when the charge/current distribution is itself a response to the field. The **Maxwell stress tensor** provides an equivalent but often more powerful method: instead of integrating over the sources, you integrate over a surface enclosing them. The force on everything inside the surface equals the flux of EM momentum through the surface — an approach analogous to using a Gaussian surface for flux instead of integrating over all charges.

The stress tensor T_ij has a concrete physical meaning: it is the flux of the i-th component of momentum in the j-th direction. The diagonal components represent **pressure** (force per unit area perpendicular to a surface), while the off-diagonal components represent **shear stress** (force per unit area parallel to a surface). Electric fields push along field lines (tension) and push outward perpendicular to them (pressure); magnetic fields similarly create tension along field lines and pressure perpendicular to them. The familiar result that field lines "want to be as short as possible" (tension) and "want to spread out sideways" (pressure) comes directly from the stress tensor's sign structure.

To find the force on an object, choose any closed surface S enclosing the object and evaluate **F** = ∮ T̄ · d**A** − ε₀μ₀ d/dt ∫**S** dV, where **S** = **E** × **H** is the Poynting vector. For static fields the time derivative vanishes and the force is purely the surface integral of the stress tensor. You can choose the surface however you like — close to the object's surface, or far away where the fields are simpler. This freedom to choose the Gaussian-like surface is what makes the method powerful.

**Radiation pressure** is a vivid application. A plane electromagnetic wave exerts pressure P = I/c on a perfectly absorbing surface (I = intensity). This follows directly from the Maxwell stress tensor: the wave carries momentum density **g** = **S**/c², and when absorbed the momentum is transferred to the surface. For a perfectly reflecting surface the pressure doubles to 2I/c because momentum reverses direction. This is not just a theoretical result — radiation pressure drives comet tails away from the sun, enables laser tweezers to trap cells, and is being exploited in proposed solar sail spacecraft. The Maxwell stress tensor is the machinery that makes these force calculations systematic.
