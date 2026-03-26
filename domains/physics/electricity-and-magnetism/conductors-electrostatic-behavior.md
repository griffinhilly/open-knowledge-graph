---
id: conductors-electrostatic-behavior
title: Conductors in Electrostatic Equilibrium
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law-problem-solving
  type: hard
- id: equipotential-surfaces
  type: hard
builds-toward:
- capacitance
- parallel-plate-capacitor-formula
tags:
- conductor
- equilibrium
- charge-distribution
stage: formal-systems
status: validated
---

# Conductors in Electrostatic Equilibrium

## Core Idea
In electrostatic equilibrium, electric field inside a conductor is zero; charges reside on the surface. The entire conductor is an equipotential, and the electric field just outside is perpendicular to the surface with magnitude E = σ/ε₀.

## Explainer

Start with what a conductor actually is: a material containing free electrons that can move in response to any applied electric force. That mobility is the key to everything that follows. Suppose you suddenly place some extra charge inside a conductor. Those charges feel the Coulomb repulsion from each other and experience any existing electric field — so they accelerate. They keep moving until there is no longer any net force on them. That motionless state is **electrostatic equilibrium**, and it requires a very specific condition: the electric field inside the conductor must be exactly zero. If even a tiny field remained, the free charges would still be moving, and we would not be in equilibrium.

You already know from Gauss's law how to deduce where the charges must go. Draw a Gaussian surface just inside the conductor's surface, entirely within the bulk metal. Since E = 0 everywhere on that surface, the flux is zero, which means the enclosed free charge is zero. The only place charge can reside is on the outer surface — there is genuinely no charge in the bulk interior. The **surface charge density σ** distributes itself until the fields it creates exactly cancel any external field inside. On a smooth, isolated sphere, σ is uniform; on a sharp point or edge, σ concentrates and the field just outside becomes very large — the basis of lightning rods.

Because the field inside is zero, moving a test charge anywhere through the bulk costs zero work. That means every two points inside the conductor are at the same potential — the conductor is a single **equipotential**. You can connect this back to equipotential surfaces, your other prerequisite: the conductor's surface itself is an equipotential surface. The field just outside must be perpendicular to that surface, because any tangential component would imply a potential difference along the surface and would drive surface currents — contradicting equilibrium. Using a Gaussian pillbox that straddles the surface (a thin disk with faces parallel to the surface), you can apply Gauss's law to show that the field just outside has magnitude E = σ/ε₀, pointing normally outward from positive charge regions.

These four results — zero interior field, surface-only charge, equipotential bulk, perpendicular exterior field — are not independent facts but a single self-consistent package. Change any one and the others would be violated. They define the electrostatic boundary conditions that govern every capacitor and shielded enclosure you will encounter next.

## Questions

```yaml
- question: "A conducting sphere carries total charge +Q. Where does this charge reside, and why?"
  type: short-answer
  answer: "All charge resides on the outer surface. If any charge were in the interior, a Gaussian surface drawn just inside the conductor would enclose net charge, implying nonzero flux and therefore nonzero interior field — which would contradict equilibrium, since free charges would then continue to move."
  explanation: "The key chain of reasoning is: equilibrium → E_interior = 0 → zero flux through any internal Gaussian surface → zero enclosed charge → charge must be on surface. This argument holds for any shape of conductor, not just spheres."

- question: "The electric field at the surface of a conductor is perpendicular to the surface. What would happen if there were a tangential component?"
  type: short-answer
  answer: "A tangential field would exert a force on surface charges parallel to the surface, causing them to flow along the surface. This current would continue until the tangential component vanished — so a tangential field is impossible in equilibrium."
  explanation: "This is a dynamic stability argument, not just a static rule. The conductor 'enforces' the perpendicularity condition by moving charges whenever it is violated. The steady-state result is that the surface is an equipotential and the external field is purely normal."
```
