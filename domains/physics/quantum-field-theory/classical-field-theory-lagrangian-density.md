---
id: classical-field-theory-lagrangian-density
title: Classical Field Theory and Lagrangian Density
domain: physics
course: quantum-field-theory
prerequisites:
- id: lagrangian-mechanics-intro
  type: hard
- id: maxwell-equations-differential-form
  type: hard
tags:
- lagrangian-density
- classical-fields
- euler-lagrange
stage: expert
status: validated
---

# Classical Field Theory and Lagrangian Density

## Core Idea
Classical field theory replaces discrete particle coordinates with continuous fields phi(x,t) as dynamical variables. The Lagrangian becomes a Lagrangian density L integrated over space, and the Euler-Lagrange equations generalize to field equations governing how fields evolve in spacetime.

## Questions

```yaml
- question: "In particle mechanics, the Lagrangian depends on generalized coordinates q_i(t) and their time derivatives. When transitioning to field theory, a student writes L = L(phi, dphi/dt). What critical modification is missing?"
  type: multiple-choice
  options:
    - "The Lagrangian must also depend on the spatial derivatives of the field, because a field's dynamics depend on its spatial variation"
    - "The Lagrangian must be replaced by a Hamiltonian for fields"
    - "The field phi must be complex-valued for the formalism to work"
    - "The Lagrangian must include an explicit dependence on spacetime coordinates x and t"
  answer: 0
  explanation: "A field phi(x,t) varies in both time and space, so its dynamics depend on spatial gradients as well as time derivatives. The Lagrangian density L(phi, partial_mu phi) depends on the field and all its spacetime partial derivatives. In particle mechanics, only time derivatives appear because the generalized coordinates are functions of time alone. The spatial derivative dependence is what makes field equations partial differential equations rather than ordinary differential equations."

- question: "The Euler-Lagrange equation for a field, partial_mu (partial L / partial (partial_mu phi)) - partial L / partial phi = 0, reduces to the Klein-Gordon equation when L = (1/2)(partial_mu phi)(partial^mu phi) - (1/2)m^2 phi^2."
  type: true-false
  answer: true
  explanation: "Applying the Euler-Lagrange equation to this Lagrangian density: partial L / partial phi = -m^2 phi, and partial L / partial (partial_mu phi) = partial^mu phi. Taking partial_mu of the latter gives the d'Alembertian of phi. The resulting equation is (partial_mu partial^mu + m^2)phi = 0, which is exactly the Klein-Gordon equation for a free scalar field of mass m. This demonstrates how the Lagrangian density encodes the field equation."

- question: "A Lagrangian density that depends explicitly on the spacetime coordinates (not just through the fields) still yields valid Euler-Lagrange equations, but it breaks Poincare invariance."
  type: true-false
  answer: true
  explanation: "The Euler-Lagrange derivation works for any L, regardless of explicit coordinate dependence. However, explicit dependence on spacetime coordinates means the physics is different at different points in spacetime, which violates translational invariance (a component of Poincare invariance). Fundamental Lagrangian densities in particle physics do not have such explicit dependence, which is precisely what guarantees conservation of energy-momentum via Noether's theorem."

- question: "Explain why the action S = integral L d^4x must be a Lorentz scalar, and what this requirement imposes on the Lagrangian density L."
  type: short-answer
  answer: "The action must be Lorentz-invariant because the equations of motion derived from it (via the principle of least action) must be the same in all inertial frames. Since d^4x transforms as a Lorentz scalar (the Jacobian of a Lorentz transformation is 1), L itself must also be a Lorentz scalar. This means L must be built from Lorentz-invariant combinations of the fields and their derivatives: scalar products of four-vectors, traces of tensor products, and contractions with the metric tensor. This constraint dramatically restricts the allowed terms in L."
  explanation: "This is why Lorentz invariance is such a powerful organizing principle. Rather than guessing field equations directly, you construct the most general Lorentz-scalar L from your fields and their derivatives (subject to additional constraints like gauge invariance and renormalizability), and the field equations follow automatically. The physical content is encoded in the symmetry requirements on L."
```

## Explainer

In classical particle mechanics, you specify a system by its Lagrangian L(q, dq/dt) and derive the equations of motion from the Euler-Lagrange equations. The transition to **field theory** replaces the discrete coordinates q_i(t) with a continuous field phi(x, t) -- or in relativistic notation, phi(x^mu). The field assigns a number (or a set of numbers, for vector or spinor fields) to every point in spacetime. Instead of a finite number of degrees of freedom, you now have infinitely many: one for each spatial point.

The Lagrangian of particle mechanics becomes a **Lagrangian density** L(phi, partial_mu phi), and the total Lagrangian is L = integral L d^3x. The action is S = integral L d^4x = integral L d^3x dt, integrated over all of spacetime. The field-theoretic Euler-Lagrange equation follows from demanding that the action is stationary under variations of phi: partial_mu (partial L / partial (partial_mu phi)) - partial L / partial phi = 0. This single equation, together with a choice of L, generates all the classical field equations you already know. Maxwell's equations, the Klein-Gordon equation, and the Dirac equation all arise from specific choices of Lagrangian density.

The power of this formulation is that **symmetries of the Lagrangian density directly constrain the physics**. A Lagrangian density that is a Lorentz scalar automatically produces Lorentz-covariant field equations. Internal symmetries (like phase rotations of a complex field) lead to conserved currents. The requirement that L contain no explicit spacetime dependence guarantees energy-momentum conservation. Rather than postulating field equations and then checking their properties, you build L from symmetry principles and derive everything else. This is the starting point for quantization: once you have the classical Lagrangian density, you can quantize the field using canonical or path-integral methods.

The simplest example is the free real scalar field, with L = (1/2)(partial_mu phi)(partial^mu phi) - (1/2)m^2 phi^2. The first term is the kinetic energy density (the relativistic generalization of (1/2)(dphi/dt)^2, including spatial gradient terms), and the second is a mass term. The Euler-Lagrange equation gives the Klein-Gordon equation. More complex Lagrangians include interaction terms (like lambda phi^4 / 4! for self-interacting scalars), coupling to other fields, and gauge field terms. The entire Standard Model of particle physics is specified by a single Lagrangian density, and every prediction of the theory follows from it.
