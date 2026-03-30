---
id: noethers-theorem-fields
title: Noether's Theorem for Fields
domain: physics
course: quantum-field-theory
prerequisites:
- id: classical-field-theory-lagrangian-density
  type: hard
- id: lagrangian-mechanics-intro
  type: hard
tags:
- noether
- conserved-currents
- symmetry
stage: expert
status: validated
---

# Noether's Theorem for Fields

## Core Idea
Noether's theorem for fields states that every continuous symmetry of the Lagrangian density yields a conserved current j^mu with partial_mu j^mu = 0. Spacetime translations give energy-momentum conservation; internal symmetries give conserved charges like electric charge.

## Questions

```yaml
- question: "In particle mechanics, Noether's theorem associates symmetries with conserved quantities (scalars). In field theory, the analogous object is a conserved current j^mu rather than a conserved scalar. Why does the upgrade from scalar to four-vector occur?"
  type: multiple-choice
  options:
    - "Because fields exist throughout space, conservation must hold locally at each point — requiring a current density and a continuity equation, not just a global constant"
    - "Because Lorentz invariance demands that all physical quantities be four-vectors"
    - "Because quantum effects require the conserved quantity to transform as a four-vector"
    - "Because fields have spin, which introduces additional vector degrees of freedom"
  answer: 0
  explanation: "In particle mechanics, there is one degree of freedom q(t) and conservation means dQ/dt = 0 for some scalar Q. In field theory, the conserved quantity (charge, energy, momentum) is distributed throughout space. Local conservation means the density can change at a point only if there is a flux through its boundary — this is the continuity equation partial_mu j^mu = 0. The conserved charge Q = integral j^0 d^3x is still a scalar, but the local statement of conservation requires a current four-vector."

- question: "The energy-momentum tensor T^{mu nu} arises from Noether's theorem applied to spacetime translations. What symmetry gives rise to the conserved angular momentum tensor?"
  type: multiple-choice
  options:
    - "Time-reversal symmetry"
    - "Lorentz transformations (boosts and rotations)"
    - "Scale transformations (dilatations)"
    - "Gauge transformations"
  answer: 1
  explanation: "Lorentz invariance of the Lagrangian (invariance under boosts and rotations) gives rise to a conserved rank-3 tensor M^{mu nu rho} whose spatial components encode angular momentum. The six independent components of the antisymmetric Lorentz transformation parameters correspond to three rotations (giving angular momentum conservation) and three boosts (giving center-of-energy conservation). Scale transformations, if present, give the dilatation current, which is a separate conserved quantity related to conformal symmetry."

- question: "For a complex scalar field with Lagrangian L = (partial_mu phi*)(partial^mu phi) - m^2 phi* phi, the U(1) symmetry phi -> e^{i alpha} phi yields a conserved current proportional to i(phi* partial_mu phi - phi partial_mu phi*). This current is identically zero for a real scalar field."
  type: true-false
  answer: true
  explanation: "If phi is real, then phi* = phi and the expression i(phi partial_mu phi - phi partial_mu phi) = 0 identically. This is physically correct: the U(1) symmetry phi -> e^{i alpha} phi does not exist for a real field (it would change the field). Real scalar fields have no conserved charge analogous to electric charge, which is why the particles they describe are electrically neutral and are their own antiparticles."

- question: "Noether's theorem guarantees conservation only at the classical level. In quantum field theory, symmetries of the classical Lagrangian can fail to be symmetries of the quantum theory."
  type: true-false
  answer: true
  explanation: "This is the phenomenon of quantum anomalies. The path integral measure or the regularization procedure can break a classical symmetry, leading to non-conservation of the corresponding current at the quantum level. The most famous example is the chiral anomaly, where the classically conserved axial current acquires a divergence proportional to F_mu_nu F-tilde^{mu nu}. Anomalies have profound physical consequences, including the explanation of neutral pion decay."

- question: "Derive the conserved current associated with the global U(1) symmetry of a complex scalar field, and explain why the conserved charge can be interpreted as particle number minus antiparticle number."
  type: short-answer
  answer: "Under phi -> e^{i alpha} phi, the infinitesimal variation is delta phi = i alpha phi. Applying Noether's formula j^mu = (partial L / partial (partial_mu phi)) delta phi + (partial L / partial (partial_mu phi*)) delta phi*, one obtains j^mu = i(phi* partial^mu phi - phi partial^mu phi*) (up to a conventional factor). The conserved charge Q = integral j^0 d^3x. After quantization, phi creates antiparticles and destroys particles, while phi-dagger creates particles and destroys antiparticles. The charge operator Q counts the number of particles minus the number of antiparticles, which is why it is conserved: pair creation produces one particle and one antiparticle, leaving Q unchanged."
  explanation: "This identification of the Noether charge with particle-minus-antiparticle number is one of the key bridges between classical field symmetry and quantum particle physics. It explains why electric charge is conserved in every process: charge conservation is the quantum manifestation of the U(1) symmetry of the Lagrangian."
```

## Explainer

You already know Noether's theorem from classical mechanics: if the Lagrangian is invariant under time translations, energy is conserved; under spatial translations, momentum is conserved; under rotations, angular momentum is conserved. The field-theory version promotes these conserved quantities from global scalars to **conserved currents**. A conserved current j^mu satisfies the continuity equation partial_mu j^mu = 0, which says that the charge density j^0 can only change at a point if there is a flux of current through its boundary. The total charge Q = integral j^0 d^3x is constant in time, provided the current vanishes at spatial infinity.

For spacetime translations, Noether's theorem produces the **energy-momentum tensor** T^{mu nu}. The component T^{00} is the energy density, T^{0i} is the momentum density, and the conservation law partial_mu T^{mu nu} = 0 encodes conservation of both energy and momentum. For internal symmetries -- transformations that act on the field values rather than on spacetime coordinates -- the theorem gives conserved currents associated with the symmetry group. The most important example is the global U(1) symmetry phi -> e^{i alpha} phi of a complex field, which yields a conserved current whose charge is electric charge (or more generally, particle number minus antiparticle number).

The derivation follows the same logic as in particle mechanics but with the field-theoretic Euler-Lagrange equation. If a continuous transformation phi -> phi + epsilon delta phi leaves the Lagrangian density invariant (or changes it by a total divergence), then the current j^mu = (partial L / partial (partial_mu phi)) delta phi is conserved on-shell (when the equations of motion are satisfied). The energy-momentum tensor arises from the special case where the transformation is a spacetime translation: delta phi = partial_nu phi, and the resulting T^{mu nu} is a rank-2 tensor rather than a four-vector.

What makes Noether's theorem indispensable in quantum field theory is that it links the symmetries you impose on the Lagrangian to the conservation laws that constrain scattering processes. Every Feynman diagram must conserve all Noether charges at every vertex. Furthermore, the theorem survives quantization in most cases, but with a crucial caveat: some classical symmetries are **anomalous**, meaning they are broken by quantum effects. The study of anomalies -- which classical symmetries survive quantization and which do not -- is one of the most important topics in modern quantum field theory.
