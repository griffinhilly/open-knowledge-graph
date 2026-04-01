---
id: gravitational-energy-pseudo-tensors
title: Gravitational Energy and Pseudo-Tensors
domain: physics
course: general-relativity
prerequisites:
- id: einstein-field-equations
  type: hard
- id: stress-energy-tensor
  type: hard
- id: noethers-theorem-fields
  type: soft
tags:
- gravitational-energy
- pseudo-tensor
- landau-lifshitz
- bondi-mass
- quasi-local-energy
stage: expert
status: validated
---

# Gravitational Energy and Pseudo-Tensors

## Core Idea
Defining gravitational energy in general relativity is fundamentally problematic because the equivalence principle allows gravity to be locally eliminated — there is no local, covariant expression for gravitational energy density. Pseudo-tensors (such as the Einstein, Landau-Lifshitz, and Moller prescriptions) provide coordinate-dependent expressions for gravitational energy-momentum that, combined with the matter stress-energy tensor, yield a conserved total energy-momentum: ∂_μ(√(-g)(T^μν + t^μν_LL)) = 0 (ordinary, not covariant, divergence). These are not tensors — they transform inhomogeneously and can be made to vanish at any point by choice of coordinates. Meaningful definitions of gravitational energy exist only in special circumstances: total (ADM) mass for asymptotically flat spacetimes, Bondi mass at null infinity (accounting for energy radiated as gravitational waves), and quasi-local energy constructions for bounded regions. The non-localizability of gravitational energy is one of the deepest conceptual features of GR.

## Questions

```yaml
- question: "Why can't gravitational energy be described by a true tensor in general relativity?"
  type: multiple-choice
  options:
    - "Because the Einstein field equations are nonlinear"
    - "Because the equivalence principle allows gravity to be locally eliminated — a freely falling observer sees no gravitational field, hence no gravitational energy, at any single point"
    - "Because gravitational energy is always exactly zero"
    - "Because tensors can only describe electromagnetic energy, not gravitational energy"
  answer: 1
  explanation: "A tensor that is nonzero in one coordinate system is nonzero in all coordinate systems. But the equivalence principle says that at any point, coordinates can be chosen (freely falling frame) in which the gravitational field — and hence any candidate for gravitational energy density — vanishes. A quantity that can be made to vanish by coordinate choice at any point cannot be a tensor (unless it is identically zero everywhere, which it clearly isn't globally). This is why pseudo-tensors, which are coordinate-dependent, are the best one can do locally."

- question: "The Landau-Lifshitz pseudo-tensor gives different values for the gravitational energy at a point depending on the coordinate system used. This means gravitational energy in GR is physically meaningless."
  type: true-false
  answer: false
  explanation: "While the local density of gravitational energy is indeed coordinate-dependent and physically ambiguous, the total gravitational energy integrated over appropriate regions is well-defined and physically meaningful in certain contexts. The ADM mass (total energy of an asymptotically flat spacetime) is coordinate-independent and conserved. The Bondi mass measures total energy at null infinity, accounting for energy carried away by gravitational radiation. These global and quasi-local quantities have clear physical interpretations — it is only the local density that is ill-defined."

- question: "Explain the distinction between ADM mass and Bondi mass, and what physical process accounts for their difference."
  type: short-answer
  answer: "The ADM mass M_ADM is the total energy of an asymptotically flat spacetime measured at spatial infinity — it includes all forms of energy (matter, radiation, gravitational binding). The Bondi mass M_Bondi is measured at future null infinity (J⁺) and equals the ADM mass minus the total energy radiated away as gravitational waves up to that retarded time. As a binary system inspirals and emits gravitational waves, M_Bondi decreases while M_ADM remains constant (energy is conserved, just redistributed between the source and the radiation). The Bondi mass loss formula dM_Bondi/du ≤ 0 (u is retarded time) proves that gravitational waves carry positive energy."
  explanation: "The Bondi mass loss formula was historically important because it settled the debate about whether gravitational waves are physically real and carry energy. The positivity of the energy flux (Bondi, van der Burg, Metzner, 1962; Sachs, 1962) established that gravitational radiation is a genuine physical phenomenon, not a coordinate artifact."

- question: "In what sense is the non-localizability of gravitational energy consistent with the conservation law ∇^μ T_μν = 0 for matter?"
  type: short-answer
  answer: "∇^μ T_μν = 0 is a local conservation law for matter energy-momentum only. In flat spacetime, this integrates to global conservation of total matter energy. In curved spacetime, the covariant divergence cannot be integrated to give global conservation because there is no way to compare vectors at different points. Energy can transfer between matter and the gravitational field: for example, a ball falling in a gravitational field gains kinetic energy (matter T_μν) at the expense of gravitational potential energy. The pseudo-tensor formalism captures this by writing ∂_μ((-g)(T^μν + t^μν)) = 0, where the ordinary (not covariant) divergence does integrate to global conservation — but only at the cost of using the coordinate-dependent pseudo-tensor t^μν for gravitational energy."
  explanation: "This framework is self-consistent: matter energy-momentum is locally conserved (covariant divergence), and total energy-momentum (matter + gravity) is globally conserved in an appropriate sense (ordinary divergence with pseudo-tensor). The price of global conservation is loss of coordinate-independence for the gravitational contribution."
```

## Explainer

In Newtonian gravity and in electromagnetism, energy density is a well-defined local quantity: you can point to a region of space and unambiguously say how much energy is stored in the gravitational or electromagnetic field there. In general relativity, this is impossible for gravitational energy. The obstacle is the equivalence principle: at any single point, you can choose coordinates (a local freely falling frame) in which the gravitational field and all its associated effects vanish. If gravitational energy were described by a tensor, it would have to be nonzero in every coordinate system if nonzero in any — but the equivalence principle requires it to vanish in the freely falling frame. This contradiction means no covariant, local expression for gravitational energy density exists.

Pseudo-tensors circumvent this by abandoning covariance. The Landau-Lifshitz pseudo-tensor t^μν_LL, for example, is defined so that ∂_μ((-g)(T^μν + t^μν_LL)) = 0 — an ordinary (partial) divergence, not a covariant one. This is a genuine conservation law that can be integrated over a spatial volume using Gauss's theorem to give a conserved total energy. However, t^μν_LL depends on the coordinate system: in one set of coordinates, the gravitational energy density might be large and positive at a point; in another, it could be zero or negative. Different pseudo-tensor prescriptions (Einstein, Moller, Weinberg, Bergmann-Thomson) give different local distributions but agree on total energy when integrated over all space for asymptotically flat spacetimes.

Meaningful, coordinate-independent gravitational energy is defined only in special geometric situations. For asymptotically flat spacetimes (isolated systems in otherwise empty space), the ADM mass provides the total energy measured at spatial infinity. It equals the sum of all matter energy plus gravitational binding energy and is conserved in time. At future null infinity, the Bondi mass provides the total energy remaining after accounting for energy radiated as gravitational waves. The difference M_ADM - M_Bondi is the total energy carried away by gravitational radiation, and the Bondi mass is monotonically non-increasing — gravitational waves carry positive energy. The positive energy theorem (Schoen-Yau, 1979; Witten, 1981) proves that the ADM mass is non-negative for physically reasonable matter, a deep result that confirms the stability of Minkowski spacetime.

For finite regions (not extending to infinity), quasi-local energy constructions (Brown-York, Wang-Yau, Hawking) attempt to define the gravitational energy within a bounded 2-surface. These are gauge-independent but depend on the choice of reference (what you compare the geometry against) and have various technical subtleties. The lack of a universal, local, covariant definition of gravitational energy is not a deficiency of the theory but a reflection of a deep physical truth: gravity is geometry, and "gravitational energy" is inseparable from the structure of spacetime itself. This non-localizability has profound implications for quantum gravity, where the standard techniques for quantizing field energies (which assume a well-defined local energy density) must be fundamentally reconsidered.
