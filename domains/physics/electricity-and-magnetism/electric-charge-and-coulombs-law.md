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
- id: electric-charge-conceptual
  type: hard
- id: static-electricity-intro
  type: soft
builds-toward:
- electric-field
- electric-potential-energy
tags:
- charge
- coulombs-law
- electrostatics
- force
stage: formal-systems
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

## Questions

```yaml
- question: "A proton (charge +e) and an electron (charge −e) are separated by distance r. The electron exerts a force F on the proton, directed toward the electron. What force does the proton exert on the electron?"
  type: multiple-choice
  options:
    - "A force greater than F, because the proton is more massive"
    - "A force equal to F directed toward the proton — equal in magnitude but opposite in direction"
    - "No force, because the electron is negatively charged and cannot exert force on positive charge"
    - "A force F/2, because the force is shared equally between the two charges"
  answer: 1
  explanation: "Coulomb's law obeys Newton's third law: the force the proton exerts on the electron is equal in magnitude and opposite in direction to the force the electron exerts on the proton. The mass difference is irrelevant — Newton's third law applies regardless of how different the two objects are. Both particles experience the same force magnitude F; they simply accelerate differently due to their mass difference (a = F/m)."

- question: "Three positive charges are placed at the corners of a triangle. How would you correctly find the total electrostatic force on one of the charges?"
  type: multiple-choice
  options:
    - "Apply Coulomb's law only to the nearest charge, since distant charges have negligible effect"
    - "Add the magnitudes of the forces from each of the other two charges"
    - "Calculate the Coulomb force from each other charge separately, then add those forces as vectors"
    - "Use an average distance to compute a single combined force from the other two charges"
  answer: 2
  explanation: "The principle of superposition states that the total electrostatic force on a charge is the vector sum of the individual Coulomb forces from every other charge. You must compute each pairwise force as a vector (with both magnitude and direction), then add the vectors. Simply adding magnitudes ignores direction and produces the wrong answer whenever forces are not collinear. Superposition is the key tool that makes multi-charge problems tractable."

- question: "Electric charge is a type of force — it is what causes the electrostatic force between objects."
  type: true-false
  answer: false
  explanation: "Charge is a property of matter, not a force. Confusing charge with force conflates the cause with the effect. Charge is an intrinsic attribute (like mass) that objects possess; the electrostatic force is what arises between two charged objects because of their charges. An object can have charge without experiencing any force (if no other charges are nearby). The distinction matters: charge is a scalar property measured in coulombs; force is a vector interaction measured in newtons."

- question: "If the distance between two point charges is halved, the electrostatic force between them increases to four times its original value."
  type: true-false
  answer: true
  explanation: "True. Coulomb's law states F = kq₁q₂/r². If r is halved (r → r/2), then r² → r²/4, making F → 4kq₁q₂/r² = 4F. This inverse-square relationship is the same mathematical structure as Newton's law of gravitation. Halving the distance quadruples the force; doubling the distance reduces it to one-quarter. This rapid scaling with distance is why electrostatic forces are strong at atomic scales but negligible at large distances for neutral bulk matter."

- question: "How is Coulomb's law analogous to Newton's law of gravitation, and what is the key difference that makes electrostatics more complex?"
  type: short-answer
  answer: "Both laws have the same mathematical form — a force proportional to the product of two source quantities (charges or masses) and inversely proportional to the square of the separation distance: F = kq₁q₂/r² versus F = Gm₁m₂/r². The key difference is that electric charge comes in two signs (positive and negative), while mass has only one sign. This means the electrostatic force can either attract (unlike charges) or repel (like charges), whereas gravity always attracts. The signed nature of q₁q₂ determines the direction of the force, adding complexity absent in gravitation."
  explanation: "The analogy is deep — both are inverse-square laws with superposition — but the signed nature of charge fundamentally changes the physics. It enables shielding, bound atomic states, and the near-neutrality of bulk matter. It also means the net force on a charge in a complex charge distribution requires careful vector addition, since forces from opposite-sign charges point in opposite directions."
```

## Explainer

**Electric charge** is a fundamental intrinsic property of matter, like mass — you cannot explain it in terms of anything more basic, only describe what it does. It comes in two varieties we call positive and negative, and crucially, it is **quantized**: every observed charge is an integer multiple of the elementary charge e ≈ 1.6 × 10⁻¹⁹ C. A proton carries +e, an electron carries −e, and a neutral object has equal amounts of both. When you rub a glass rod with silk, you're not creating charge — you're transferring electrons from one object to the other, leaving one with a deficit (positive) and the other with a surplus (negative).

**Coulomb's law** describes the force between two point charges: F = kq₁q₂/r². This has exactly the same mathematical structure as Newton's law of gravitation (F = Gm₁m₂/r²) that you already know — an inverse-square law proportional to the product of the two sources. The key difference is that charge can be positive or negative, so the force can attract or repel, while gravity only attracts. Like charges (same sign, so q₁q₂ > 0) give a positive force magnitude in the repulsive direction; unlike charges (opposite sign) attract. The constant k ≈ 9 × 10⁹ N·m²/C² is often written as 1/(4πε₀), where **ε₀** is the **permittivity of free space** — a constant that will recur throughout electromagnetism.

Coulomb's law is a vector law, and this is where your vector prerequisite earns its keep. The force on charge 1 due to charge 2 points along the line connecting them (radially outward for repulsion, inward for attraction). When multiple charges are present, you apply the **principle of superposition**: the total force on any one charge is the vector sum of the individual Coulomb forces from each other charge. This superposition principle is not obvious — it is an empirical fact that electric forces add linearly — and it is what makes electrostatics computationally tractable.

The mutual nature of the force is a direct consequence of Newton's third law. Charge A pulls on charge B with some force F; charge B pulls on charge A with an equal and opposite force −F. This symmetry holds regardless of how different the charges are in magnitude — a proton and an electron exert equal forces on each other. Finally, remember the scope of the law: it is exact for **point charges** (or equivalently, for spherically symmetric charge distributions viewed from outside). For extended charge distributions, you must sum (integrate) Coulomb contributions over every infinitesimal piece of charge — that more general treatment is what the electric field and Gauss's law are built to handle.
