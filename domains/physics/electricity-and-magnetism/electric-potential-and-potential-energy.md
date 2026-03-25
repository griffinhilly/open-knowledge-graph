---
id: electric-potential-and-potential-energy
title: Electric Potential and Potential Energy
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-field-and-coulombs-law
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- scalar-and-vector-potentials
- boundary-value-problems-em
tags:
- electrostatics
- potential-theory
- energy
stage: expert
status: validated
---

# Electric Potential and Potential Energy

## Core Idea
Electric potential V is the work per unit charge to bring a test charge from infinity to a point. Potential relates to electric field by E = -∇V. The scalar potential often simplifies calculations compared to working directly with fields.

## Questions

```yaml
- question: "A positive test charge is placed between two parallel plates: the left plate is at +200V and the right plate is at 0V. In which direction does the electric force on the charge point?"
  type: multiple-choice
  options:
    - "Toward the left plate (toward higher potential), because positive charges are attracted to positive regions"
    - "Toward the right plate (toward lower potential), because E = −∇V means the field points from high to low potential"
    - "The charge feels no net force, because it is midway between the plates"
    - "Perpendicular to both plates, along the equipotential surfaces"
  answer: 1
  explanation: "The relation E = −∇V means the electric field points in the direction of steepest *decrease* in potential — like water flowing downhill. With the left plate at +200V and the right at 0V, potential decreases from left to right, so E points rightward. The force on a positive test charge is F = qE, so it is pushed toward the right (lower potential) plate. The common misconception is that positive charges are attracted to regions of higher (positive) potential, but it is the gradient of V — the rate of change — that determines force direction, and the force is in the direction of decreasing V."

- question: "A positive charge q is moved from point A (V = 50 V) to point B (V = 20 V). What happens to its electric potential energy?"
  type: multiple-choice
  options:
    - "It increases, because the charge moved to a region of lower potential"
    - "It decreases, because ΔU = q(V_B − V_A) = q(20 − 50) < 0 for positive q"
    - "It stays the same, because the electric force is conservative"
    - "It changes by 30 J regardless of the value of q"
  answer: 1
  explanation: "Potential energy is U = qV, so the change is ΔU = q(V_B − V_A) = q(20 − 50) = −30q. For a positive charge, this is a decrease in potential energy. The work done by the electric field equals −ΔU, so the field does positive work on the charge as it moves from high to low potential — analogous to gravity doing positive work as a mass falls from high to low altitude. Option C confuses conservation of total energy with constancy of potential energy; option D ignores that ΔU depends on both the potential difference and the charge."

- question: "Electric potential V and electric potential energy U are different quantities — V is a property of the point in space, while U depends on both the potential at that point and the charge placed there."
  type: true-false
  answer: true
  explanation: "This distinction is essential. V = W/q is a property of the location — it describes the energy landscape per unit charge, independent of any charge placed there. U = qV depends on both the potential and the specific charge q. A proton and an electron at the same location have potential energies of opposite sign (same V, but opposite q). The field, equipotential surfaces, and all geometric properties belong to V; U only appears when you introduce a specific charge."

- question: "The electric field always points from regions of low potential to regions of high potential, since positive charges are attracted toward higher potentials."
  type: true-false
  answer: false
  explanation: "The relationship is E = −∇V, where the minus sign is critical. The field points in the direction of *decreasing* potential — from high to low V. Think of V as altitude: the electric field is like the gravitational field, which points downhill (toward decreasing altitude), not uphill. A positive charge released in an electric field accelerates toward lower potential (losing potential energy, gaining kinetic energy) — the field points in that same direction of lower potential."

- question: "Why is working with electric potential V often simpler than working directly with the electric field E when solving problems involving multiple point charges?"
  type: short-answer
  answer: "Electric potential V is a scalar — it has magnitude but no direction. To find the total potential at a point due to multiple charges, you add the scalar contributions: V_total = kQ₁/r₁ + kQ₂/r₂ + ... Each term is a number, and numbers add simply. The electric field E is a vector — each charge's contribution has both magnitude and direction, requiring separate x, y, and z components that must be combined geometrically. Once V is found by scalar addition, the field can be recovered by differentiation (E = −∇V), which is often less work than direct vector addition throughout."
  explanation: "The practical power of the potential formalism is computational: scalar addition is far simpler than vector addition. Students who understand this recognize why physicists reach for potentials first in electrostatics problems. It is not that potential is more fundamental than the field — it is that calculating one scalar function and then differentiating it once is usually easier than tracking three field components at every point."
```

## Explainer

From Coulomb's law and the electric field concept, you know that a charge Q creates an electric field E = kQ/r² pointing radially outward. Moving a test charge q through this field requires work, and that work depends only on the start and end points — not on the path taken — because the electric force is **conservative**. This path-independence is the key that lets us define a scalar quantity, the **electric potential** V, that fully encodes the energy landscape without keeping track of directions.

The potential V at a point is defined as the work done per unit positive test charge to bring it from a reference point (conventionally infinity, where V = 0) to that point: V = W/q. For a single point charge Q at the origin, V = kQ/r — a simple scalar that falls off as 1/r, in contrast to the electric field which falls off as 1/r² and must be tracked as a vector. The **electric potential energy** of a charge q placed at a location where the potential is V is then U = qV, analogous to gravitational potential energy mgh. Moving the charge from point A to point B changes its potential energy by ΔU = q(V_B − V_A) = −W_by_field, the work done by the field is the negative of the change in potential energy, just as in mechanics.

The connection between potential and field is the gradient relation **E = −∇V**. You learned the gradient from multivariable calculus: ∇V is the vector of partial derivatives (∂V/∂x, ∂V/∂y, ∂V/∂z), pointing in the direction of steepest increase of V. The minus sign means the electric field points in the direction of steepest *decrease* of potential — like water flowing downhill from high to low potential. This is conceptually powerful: if you can find V (a scalar, requiring one calculation instead of three), you can recover E (a vector) by differentiation. For many geometries — especially those with symmetry — finding V by summing kQ/r contributions is far easier than summing vectorial E contributions, and then differentiating gives E.

Surfaces where V = constant are called **equipotential surfaces**, and they are always perpendicular to the electric field lines (since E = −∇V means E is perpendicular to surfaces of constant V). No work is done moving a charge along an equipotential surface. This geometric picture unifies static and dynamic problems: the motion of a charged particle in an electric field is formally identical to the motion of a mass in a gravitational field, with V playing the role of gravitational altitude and qV playing the role of potential energy mgh. This analogy carries forward into boundary value problems, Poisson's equation ∇²V = −ρ/ε₀, and ultimately the four-potential formalism of relativistic electrodynamics.
