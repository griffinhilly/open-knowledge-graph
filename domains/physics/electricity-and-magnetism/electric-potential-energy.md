---
id: electric-potential-energy
title: Electric Potential Energy
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-charge-and-coulombs-law
  type: hard
- id: work-and-energy
  type: hard
- id: potential-energy
  type: hard
builds-toward:
- electric-potential
tags:
- potential-energy
- work
- electrostatics
- conservative-force
stage: formal-systems
status: validated
---

# Electric Potential Energy

## Core Idea
The electric force is conservative, meaning the work it does on a charge moving between two points is path-independent and equals the negative change in electric potential energy: W = −ΔU. For two point charges separated by distance r, the electric potential energy is U = kq₁q₂/r. The reference point is typically U = 0 at r → ∞. For systems of multiple charges, total potential energy is the sum over all unique pairs.

## How It's Best Learned
Connect to gravitational potential energy — both are conservative forces with 1/r² dependence (gravitation analogous to Coulomb). Practice computing U for 2-charge, then 3-charge systems. Use energy conservation to find speeds of released charges.

## Common Misconceptions
- Potential energy belongs to the system of charges, not to a single charge.
- Negative potential energy means the configuration is bound — energy must be added to separate the charges.
- The work done by an external agent equals +ΔU, while the work done by the electric force equals −ΔU.

## Explainer

You already know gravitational potential energy: U_grav = mgh near Earth's surface, and more generally U_grav = −Gm₁m₂/r for two masses. Electric potential energy has an identical mathematical structure. For two point charges q₁ and q₂ separated by distance r, the electric potential energy is U = kq₁q₂/r — the same 1/r dependence, with mass replaced by charge and G replaced by k. This is not a coincidence: both the gravitational and electric forces are conservative, inverse-square forces. The mathematical framework carries over directly.

The critical conceptual point is that potential energy belongs to the **pair of charges**, not to either charge individually. When you push two positive charges together, you do work against the repulsive force, and that work is stored in the configuration — in the field between them. If you release them, the electric force does the work back, converting that stored energy into kinetic energy. The formula U = kq₁q₂/r encodes the sign automatically: two like charges have positive U (you had to invest energy to bring them together), and two opposite charges have negative U (they naturally attract, and you would need to invest energy to separate them to infinity).

The reference point convention — setting U = 0 at r → ∞ — means every finite separation has a potential energy measured relative to "infinitely apart." This is the same convention used in planetary mechanics. Work-energy accounting follows the conservative force rule you know: the work done *by* the electric force equals −ΔU. If a positive charge moves from a region of high potential energy to low potential energy, the electric force does positive work, and the charge gains kinetic energy equal to the energy it loses. An external agent pushing the charge the other way must do positive work equal to +ΔU.

For systems of **three or more charges**, the total potential energy is the sum over all unique pairs: U_total = U₁₂ + U₁₃ + U₂₃. Each pair contributes independently. The factor of ½ in the general formula U = ½Σᵢ qᵢVᵢ (where Vᵢ is the potential at charge i due to all other charges) avoids counting each pair twice — an algebraic identity that becomes important when charges are continuous distributions. The physical interpretation remains the same: U_total is the energy stored in the assembly, and it equals the work an external agent must do to assemble the configuration, bringing each charge in from infinity one by one.

