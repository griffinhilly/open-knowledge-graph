---
id: electric-field-from-distributions
title: Electric Field from Charge Distributions
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: coulomb-force-superposition
  type: hard
- id: triple-integrals
  type: soft
builds-toward:
- gauss-law-symmetry
tags:
- field
- distributions
- integration
stage: formal-systems
status: validated
---

# Electric Field from Charge Distributions

## Core Idea
For extended charge distributions with linear, surface, or volume charge densities (λ, σ, ρ), the electric field is found by integrating Coulomb contributions: E⃗(r⃗) = (1/4πε₀) ∫ (ρ(r⃗′)/|r⃗−r⃗′|²) r̂ dV′. Symmetric configurations (spheres, cylinders, planes) yield closed-form results or simplify via Gauss's law.

## Questions

```yaml
- question: "When computing the electric field from an infinite line of charge using direct integration, why do the components of dE parallel to the line cancel out?"
  type: multiple-choice
  options:
    - "Because the line has zero net charge along its length"
    - "Because symmetry ensures that for every source element contributing a parallel component in one direction, there is an equal element contributing an equal and opposite parallel component"
    - "Because parallel components of the electric field always cancel in any continuous distribution"
    - "Because Coulomb's law only applies to the radial component"
  answer: 1
  explanation: "For an infinite line, consider any element at position +z along the line. There is a symmetric element at −z contributing a parallel field component in the opposite direction. These cancel exactly by symmetry. Only the radial components (pointing away from the line) add constructively, because all radial contributions point in the same direction. This symmetry argument is why only the perpendicular component survives and the integral reduces to a simpler one-dimensional computation."

- question: "The charge density of a sphere is doubled uniformly throughout its volume. What happens to the electric field at a point outside the sphere?"
  type: multiple-choice
  options:
    - "It remains the same, because the sphere's geometry hasn't changed"
    - "It doubles, because the field is linear in the charge density by superposition"
    - "It quadruples, because the field depends on charge squared"
    - "It decreases by half, because more charge creates more cancellation"
  answer: 1
  explanation: "The electric field from a charge distribution is computed by integrating Coulomb contributions: E ∝ ∫ ρ dV / r². Since ρ appears linearly in the integrand (not squared), doubling ρ everywhere doubles each infinitesimal contribution, and therefore doubles the total field by the linearity of integration (superposition). The field does not depend on charge squared."

- question: "To find the net electric field from a charge distribution, you can integrate the scalar magnitudes |dE| of each infinitesimal contribution and sum them directly."
  type: true-false
  answer: false
  explanation: "The electric field is a vector quantity — each infinitesimal element dq contributes a field dE⃗ with both a magnitude and a direction. Both change as you move from one source element to another. You must integrate vector components separately (e.g., dEₓ and dEᵧ), which allows cancellation between components pointing in opposite directions. Integrating only magnitudes ignores this cancellation and gives a larger (incorrect) result — for example, it would predict a nonzero field at the center of a symmetric distribution, where the true field is zero."

- question: "For a uniformly charged infinite plane, the electric field at any point not on the plane points perpendicular to the plane."
  type: true-false
  answer: true
  explanation: "By symmetry, any component of the field parallel to the plane must cancel. For every source element contributing a rightward parallel component, there is a symmetric element contributing an equal leftward component. Only the perpendicular (normal) components add constructively. The result is E = σ/(2ε₀) pointing away from the plane on both sides, with no parallel component anywhere. This same symmetry argument justifies why Gauss's law with a pillbox surface gives the field for a planar distribution."

- question: "Explain why the vector nature of the electric field makes integrating over charge distributions more challenging than integrating a scalar quantity like electric potential."
  type: short-answer
  answer: "For scalar quantities (like potential V), you integrate a single number — each source element contributes a positive scalar dV = kλ dℓ/r, and you add them all up. For the vector field, each element contributes a direction as well as a magnitude, and both the magnitude (through 1/r²) and the direction (through r̂) change as you move along the distribution. You must decompose dE⃗ into components (x, y, z or radial, parallel) and integrate each separately. Components in opposite directions cancel — which is actually helpful for symmetric cases, but requires careful bookkeeping in general. An integration that would be one line for potential may require three separate integrals for the field."
  explanation: "The added complexity is not just algebraic — it reflects physics. Cancellation of field components due to symmetry is physically meaningful (the forces in opposing directions balance), and tracking that cancellation requires the full vector treatment."
```

## Explainer

You already know from Coulomb's law that the field from a single point charge falls off as 1/r² in a radial direction. You also know the superposition principle: fields from multiple charges add as vectors. This topic is simply the logical extension of superposition to infinitely many infinitesimal charges spread across a line, surface, or volume. Instead of summing discrete contributions, you integrate continuous ones.

The central idea is to replace the discrete sum ΣkqᵢR̂ᵢ/rᵢ² with an integral. If charge is spread along a line with **linear charge density** λ (charge per unit length), each infinitesimal element dℓ carries charge dq = λ dℓ and contributes a field dE = (1/4πε₀)(λ dℓ/r²)r̂. You integrate this over the whole line. Similarly, **surface charge density** σ gives dq = σ dA, and **volume charge density** ρ gives dq = ρ dV. The vector nature of the integral is what makes the calculation challenging: both the magnitude 1/r² and the direction r̂ change with each source element's position, so you must often work in components.

The most important skill is recognizing when symmetry makes the integral tractable or unnecessary. For an infinite line of charge, all field components parallel to the line cancel by symmetry — only the radial component survives, and the integral reduces to a simple one-dimensional computation. For an infinite plane of surface charge, only the normal component survives. These symmetric cases are worth memorizing as building blocks: infinite line gives E = λ/(2πε₀r), infinite plane gives E = σ/(2ε₀). When you later encounter Gauss's law, you will see that these same results emerge more elegantly from symmetry arguments alone — but the direct integration here builds the intuition for *why* symmetry matters.

For less symmetric distributions, the integration becomes a genuine triple integral over volume. Your prerequisite knowledge of triple integrals applies directly: you choose a coordinate system suited to the geometry (spherical for spheres, cylindrical for cylinders), express r and r̂ in those coordinates, and carry out the integral component by component. The result is always a vector field — every point in space gets assigned a direction and magnitude telling you the force per unit charge that a test charge would feel there.
