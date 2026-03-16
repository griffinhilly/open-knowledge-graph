---
id: equipartition-theorem
title: The Equipartition Theorem
domain: physics
course: thermodynamics
prerequisites:
- id: rms-speed-and-kinetic-energy
  type: hard
builds-toward:
- heat-capacity-of-gases
- adiabatic-processes
tags:
- equipartition
- degrees-of-freedom
- internal-energy
- heat-capacity
stage: formal-systems
status: validated
---

# The Equipartition Theorem

## Core Idea
The equipartition theorem states that each quadratic degree of freedom (each independent way a molecule can store energy) contributes (1/2)kT to the average energy per molecule. Monatomic gases have 3 translational degrees, so U = (3/2)NkT. Diatomic molecules add 2 rotational degrees at room temperature (U = (5/2)NkT) and 2 vibrational degrees at high temperatures. This explains why different gases have different heat capacities and why heat capacity can change with temperature.

## How It's Best Learned
Physically interpret each degree of freedom: three independent directions of translation, two rotation axes for a dumbbell-shaped diatomic molecule. Predict Cv for monatomic, diatomic, and triatomic gases and compare to experimental values.

## Common Misconceptions
- Vibrational modes are not always active — at room temperature, quantum effects 'freeze out' vibrational degrees in diatomic gases; classical equipartition overestimates Cv in that regime.
- The theorem is statistical and holds only on average over many molecules.

## Explainer

From your study of the kinetic theory of gases — specifically rms speed and kinetic energy — you know that the average translational kinetic energy of a molecule in thermal equilibrium is (3/2)kT. This result came from computing ⟨½mv²⟩ = ½m⟨v_x² + v_y² + v_z²⟩ and using the Maxwell-Boltzmann distribution. The equipartition theorem generalizes this: the factor of (3/2) comes from having three independent translational directions, and each one contributes exactly (1/2)kT. The theorem says this is not a coincidence — it is a universal rule that applies to any quadratic term in the energy, regardless of whether it is kinetic or potential.

The precise statement is: for any degree of freedom that appears **quadratically** in the total energy — of the form ½ax² for any constant a and generalized coordinate x — the thermal average of that term is exactly (1/2)kT, independent of a. "Quadratic" is the key word. A spring has potential energy ½kx² and kinetic energy ½mv²: both are quadratic, so each contributes (1/2)kT to the average energy. A vibrational mode thus contributes (1/2)kT from kinetic energy plus (1/2)kT from potential energy = kT total, compared to (1/2)kT per direction of pure translation. This is why heat capacities differ so dramatically by molecular type.

Applying the theorem: a **monatomic** gas molecule (e.g., argon) has only three translational degrees of freedom, so its internal energy per molecule is U = 3 × (½kT) = (3/2)kT, and its molar heat capacity at constant volume is C_v = (3/2)R. A **diatomic** molecule (e.g., N₂) at room temperature adds two rotational degrees (rotation about the two axes perpendicular to the bond axis — rotation about the bond axis has negligible moment of inertia and does not contribute), giving U = (5/2)kT and C_v = (5/2)R. At high temperatures, the two vibrational modes (one kinetic, one potential) activate, pushing C_v toward (7/2)R. These predictions match experiment beautifully in the appropriate temperature ranges.

The important caveat is **quantum freezing**. The equipartition theorem is a classical result. Quantum mechanics imposes discrete energy levels on each mode, with level spacing ΔE = ħω for vibrations and ΔE ∝ ħ²/I for rotations. If the thermal energy kT is much smaller than ΔE, the mode cannot absorb thermal energy in the small increments that equipartition assumes — it stays in its ground state and contributes essentially zero to the heat capacity. This is why vibrational modes in H₂ are frozen out at room temperature (their ħω is large), while rotational modes in N₂ are not (their ħ²/I is much smaller). The failure of classical equipartition at low temperatures was one of the early clues that classical mechanics was incomplete, and its resolution by quantum statistics was a triumph of early quantum theory.
