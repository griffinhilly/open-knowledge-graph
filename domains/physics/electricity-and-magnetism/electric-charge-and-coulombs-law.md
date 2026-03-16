---
id: electric-charge-and-coulombs-law
title: Electric Charge and Coulomb's Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: newtons-second-law
  type: hard
- id: vectors-in-two-dimensions
  type: hard
builds-toward:
- electric-field
- electric-potential-energy
tags:
- charge
- coulombs-law
- electrostatics
- force
stage: concrete-operations
status: validated
---

# Electric Charge and Coulomb's Law

## Core Idea
Electric charge is a fundamental property of matter that comes in two types — positive and negative — and is quantized in units of the elementary charge e ≈ 1.6 × 10⁻¹⁹ C. Coulomb's law states that the electrostatic force between two point charges is proportional to the product of their charges and inversely proportional to the square of the distance between them: F = kq₁q₂/r². Like charges repel and unlike charges attract. The constant k ≈ 9 × 10⁹ N·m²/C² is related to the permittivity of free space by k = 1/(4πε₀).

## How It's Best Learned
Start with qualitative experiments (rubbing rods, observing attraction/repulsion) before working quantitative problems. Practice vector addition of forces from multiple charges to build intuition before tackling continuous charge distributions.

## Common Misconceptions
- Charge is not a force; it is a property that produces force.
- Coulomb's law applies strictly to point charges; extended objects require integration.
- The force is mutual — both charges experience equal and opposite forces (Newton's third law applies).

## Explainer

**Electric charge** is a fundamental intrinsic property of matter, like mass — you cannot explain it in terms of anything more basic, only describe what it does. It comes in two varieties we call positive and negative, and crucially, it is **quantized**: every observed charge is an integer multiple of the elementary charge e ≈ 1.6 × 10⁻¹⁹ C. A proton carries +e, an electron carries −e, and a neutral object has equal amounts of both. When you rub a glass rod with silk, you're not creating charge — you're transferring electrons from one object to the other, leaving one with a deficit (positive) and the other with a surplus (negative).

**Coulomb's law** describes the force between two point charges: F = kq₁q₂/r². This has exactly the same mathematical structure as Newton's law of gravitation (F = Gm₁m₂/r²) that you already know — an inverse-square law proportional to the product of the two sources. The key difference is that charge can be positive or negative, so the force can attract or repel, while gravity only attracts. Like charges (same sign, so q₁q₂ > 0) give a positive force magnitude in the repulsive direction; unlike charges (opposite sign) attract. The constant k ≈ 9 × 10⁹ N·m²/C² is often written as 1/(4πε₀), where **ε₀** is the **permittivity of free space** — a constant that will recur throughout electromagnetism.

Coulomb's law is a vector law, and this is where your vector prerequisite earns its keep. The force on charge 1 due to charge 2 points along the line connecting them (radially outward for repulsion, inward for attraction). When multiple charges are present, you apply the **principle of superposition**: the total force on any one charge is the vector sum of the individual Coulomb forces from each other charge. This superposition principle is not obvious — it is an empirical fact that electric forces add linearly — and it is what makes electrostatics computationally tractable.

The mutual nature of the force is a direct consequence of Newton's third law. Charge A pulls on charge B with some force F; charge B pulls on charge A with an equal and opposite force −F. This symmetry holds regardless of how different the charges are in magnitude — a proton and an electron exert equal forces on each other. Finally, remember the scope of the law: it is exact for **point charges** (or equivalently, for spherically symmetric charge distributions viewed from outside). For extended charge distributions, you must sum (integrate) Coulomb contributions over every infinitesimal piece of charge — that more general treatment is what the electric field and Gauss's law are built to handle.
