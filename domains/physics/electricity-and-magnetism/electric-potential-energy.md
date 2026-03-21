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

## Questions

```yaml
- question: "Two protons are initially held 0.5 nm apart and then released from rest. As they move apart, what happens to the total mechanical energy of the system?"
  type: multiple-choice
  options:
    - "Total mechanical energy is conserved; potential energy decreases as kinetic energy increases"
    - "Total mechanical energy increases because the electric field does positive work on the protons"
    - "Total mechanical energy decreases because the protons shed their potential energy"
    - "Kinetic energy increases and so does potential energy, so total energy increases"
  answer: 0
  explanation: "The electric force is conservative, so total mechanical energy (KE + PE) is conserved. Initially, both protons are at rest (KE = 0) with positive potential energy U = kq²/r > 0. As they repel and fly apart, r increases, U decreases, and by conservation of energy the decrease in U equals the increase in KE. Total KE + U remains constant. The work done by the electric force equals −ΔU = ΔKE — it converts PE to KE, but conserves the total."

- question: "An electron and a proton are separated by distance r. Their electric potential energy U = −ke²/r is negative. The most physically meaningful interpretation is:"
  type: multiple-choice
  options:
    - "Energy must be added to the system to separate them to infinity — the configuration is bound"
    - "The system has 'anti-energy' that can be used to do work on other objects"
    - "The electron has negative energy and the proton has positive energy; they sum to zero"
    - "There was an error; potential energy cannot be negative"
  answer: 0
  explanation: "Negative potential energy means the current configuration has less energy than the reference state (U = 0 at infinite separation). To move from negative U to U = 0, energy must be added — the pair is bound. This parallels gravitational potential energy for two masses: U_grav = −Gm₁m₂/r is also negative, and we are gravitationally bound to Earth in the same sense. Negative U does not mean 'negative energy' belonging to individual particles — it belongs to the configuration."

- question: "The electric potential energy of two charges is a property of each individual charge, not of the pair."
  type: true-false
  answer: false
  explanation: "Electric potential energy belongs to the system — the pair of charges — not to either charge individually. It represents the work done to assemble the configuration against the interaction force. If you bring charge q₁ from infinity in isolation, no work is needed (no field to work against). Only when you bring q₂ into the field of q₁ does work appear, stored in the configuration as a whole. The formula U = kq₁q₂/r depends on both charges and their separation, not on one alone."

- question: "If a positive charge is released near a fixed positive charge, it will move from a region of high electric potential energy to a region of lower electric potential energy, and the electric force does positive work on it."
  type: true-false
  answer: true
  explanation: "The relationship is W_electric = −ΔU. If U decreases (ΔU < 0), then W_electric = −ΔU > 0: the force does positive work. For two like charges, U = kq₁q₂/r > 0 and decreases as r increases. The electric force points outward (repulsion), in the same direction as the displacement — so positive work is done, decreasing PE and increasing KE. This mirrors a ball rolling downhill: the force acts in the direction of motion, converting PE to KE."

- question: "Explain why electric potential energy is a property of a system of charges rather than of an individual charge. Use the concept of work done in assembling the system."
  type: short-answer
  answer: "Potential energy represents stored work — specifically, the work done against the interaction force to assemble the configuration from a reference state (charges infinitely far apart). Bringing a single charge from infinity requires no work because no force acts on it in isolation. Work only appears when a second charge is brought into the field of the first — that work is stored in the spatial relationship between the pair. U = kq₁q₂/r depends on both charges and their separation, confirming it is a shared property of the system, not of either charge alone."
  explanation: "A single isolated charge has no electric potential energy — there is nothing to interact with. The moment a second charge is introduced, the configuration has potential energy. For three charges, U = U₁₂ + U₁₃ + U₂₃, where each term belongs to one pair. The total equals the work to assemble all three charges from infinity: bring q₁ (free), bring q₂ into q₁'s field (work = U₁₂), bring q₃ into the fields of both (work = U₁₃ + U₂₃). The energy resides in the configuration, not in any individual charge."
```

## Explainer

You already know gravitational potential energy: U_grav = mgh near Earth's surface, and more generally U_grav = −Gm₁m₂/r for two masses. Electric potential energy has an identical mathematical structure. For two point charges q₁ and q₂ separated by distance r, the electric potential energy is U = kq₁q₂/r — the same 1/r dependence, with mass replaced by charge and G replaced by k. This is not a coincidence: both the gravitational and electric forces are conservative, inverse-square forces. The mathematical framework carries over directly.

The critical conceptual point is that potential energy belongs to the **pair of charges**, not to either charge individually. When you push two positive charges together, you do work against the repulsive force, and that work is stored in the configuration — in the field between them. If you release them, the electric force does the work back, converting that stored energy into kinetic energy. The formula U = kq₁q₂/r encodes the sign automatically: two like charges have positive U (you had to invest energy to bring them together), and two opposite charges have negative U (they naturally attract, and you would need to invest energy to separate them to infinity).

The reference point convention — setting U = 0 at r → ∞ — means every finite separation has a potential energy measured relative to "infinitely apart." This is the same convention used in planetary mechanics. Work-energy accounting follows the conservative force rule you know: the work done *by* the electric force equals −ΔU. If a positive charge moves from a region of high potential energy to low potential energy, the electric force does positive work, and the charge gains kinetic energy equal to the energy it loses. An external agent pushing the charge the other way must do positive work equal to +ΔU.

For systems of **three or more charges**, the total potential energy is the sum over all unique pairs: U_total = U₁₂ + U₁₃ + U₂₃. Each pair contributes independently. The factor of ½ in the general formula U = ½Σᵢ qᵢVᵢ (where Vᵢ is the potential at charge i due to all other charges) avoids counting each pair twice — an algebraic identity that becomes important when charges are continuous distributions. The physical interpretation remains the same: U_total is the energy stored in the assembly, and it equals the work an external agent must do to assemble the configuration, bringing each charge in from infinity one by one.

