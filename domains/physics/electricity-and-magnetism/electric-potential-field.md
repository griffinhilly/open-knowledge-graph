---
id: electric-potential-field
title: Electric Potential and the Potential-Field Relationship
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law-symmetry
  type: soft
builds-toward:
- equipotential-surfaces
tags:
- potential
- field
- conservative
stage: formal-systems
status: validated
---

# Electric Potential and the Potential-Field Relationship

## Core Idea
Electric potential V(r⃗) is the work per unit charge done by an external agent moving a test charge from infinity to point r⃗. The electric field is the negative gradient of potential: E⃗ = −∇V. Because the electrostatic field is conservative, line integrals are path-independent and equal the potential difference: V_AB = −∫_A^B E⃗·d⃗ℓ.

## Explainer

Think of the electric potential as the elevation map of the electric field landscape. Just as the slope of a hillside tells you how steeply elevation changes with position, the electric field tells you how steeply potential changes with position — and in which direction it decreases fastest. A ball released on a hillside rolls downhill, toward lower elevation; a positive test charge released in an electric field accelerates toward lower potential. The mathematical statement of this is **E⃗ = −∇V**: the field is the negative gradient of the potential. The negative sign captures the downhill-rolling intuition: the field points in the direction of decreasing V, not increasing V.

The definition of **electric potential** V(r⃗) is the work per unit charge required to bring a positive test charge from infinity (where V = 0 by convention) to the point r⃗, moving quasi-statically against the electric force. This makes potential a scalar quantity — a single number at each point in space — which is almost always easier to work with than the vector field E⃗. For a point charge Q, V(r) = kQ/r, decreasing as you move away. To find V for a charge distribution, you sum (or integrate) scalar contributions; to find E⃗ directly, you would sum vector contributions, which is much harder. This is why potential is a practical tool: compute V first, then differentiate to get E⃗.

The reason the integral V_AB = −∫_A^B E⃗·d⃗ℓ does not depend on the path taken is that the electrostatic field is **conservative** — a concept from your work on Gauss's law and vector calculus. A field is conservative when the work done moving along any closed loop is zero, which is equivalent to saying the curl of the field is zero (∇ × E⃗ = 0 for static fields). Path independence is what allows you to define a meaningful scalar "height" (potential) in the first place: if the work were path-dependent, there would be no consistent elevation map to draw. The gradient relationship E⃗ = −∇V is only possible because E⃗ is conservative.

Equipotential surfaces — regions of constant V — are always perpendicular to the field lines. This is a direct consequence of E⃗ = −∇V: gradients are perpendicular to level surfaces. Moving along an equipotential does no work (dV = 0 along the path), while moving across equipotentials (along a field line) does maximum work per unit distance. This geometry is the bridge to the next topic: conductors in equilibrium are equipotential bodies because free charges redistribute until no work is required to move charge within them.

## Questions

```yaml
- question: "If the electric potential is constant throughout a region (V = constant), what is the electric field in that region?"
  type: short-answer
  answer: "E⃗ = 0. Since E⃗ = −∇V and the gradient of a constant is zero, the electric field is zero everywhere in that region."
  explanation: "This is a direct application of E⃗ = −∇V. The field measures how quickly potential changes with position — if potential does not change, there is no field. This is why the interior of a conductor (which is an equipotential) has zero field."

- question: "You move a +2 μC charge from point A to point B, where V_A = 100 V and V_B = 40 V. How much work does the electric field do on the charge?"
  type: short-answer
  answer: "W = q(V_A − V_B) = (2×10⁻⁶ C)(100 − 40 V) = 1.2×10⁻⁴ J = 0.12 mJ. The field does positive work because the positive charge moves from higher to lower potential."
  explanation: "Work done by the electric field equals W = q ΔV = q(V_initial − V_final). This is analogous to gravity doing positive work when an object falls to lower gravitational potential energy. A positive charge moving to lower potential is like a ball rolling downhill — the field accelerates it, so the field does positive work."
```
