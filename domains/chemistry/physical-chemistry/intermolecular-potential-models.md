---
id: intermolecular-potential-models
title: Intermolecular Potential Energy Models
domain: chemistry
course: physical-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: statistical-mechanics-foundations
  type: soft
- id: molecular-polarity
  type: soft
builds-toward:
- transport-phenomena-gases
tags:
- Lennard-Jones
- van-der-Waals
- dispersion
- pair-potential
- virial-equation
- second-virial-coefficient
stage: advanced
status: validated
---

# Intermolecular Potential Energy Models

## Core Idea
Intermolecular potential models quantify the energy of interaction between molecules as a function of separation distance r. The Lennard-Jones 12-6 potential u(r) = 4ε[(σ/r)¹² − (σ/r)⁶] captures short-range repulsion (Pauli exclusion, r⁻¹²) and long-range London dispersion attraction (r⁻⁶) with two parameters: well depth ε and collision diameter σ. Electrostatic contributions (dipole-dipole, dipole-induced-dipole) add orientation-dependent terms. The second virial coefficient B(T) = −2πN_A∫[exp(−u(r)/kT)−1]r²dr connects the pair potential to deviations from ideal gas behavior, providing a direct experimental route to determining ε and σ from equation-of-state measurements.

## How It's Best Learned
Plot the LJ potential and identify the equilibrium separation (r_min = 2^(1/6)σ), well depth ε, and where the potential crosses zero (r = σ). Calculate B(T) numerically for argon and compare to experimental data across a range of temperatures.

## Common Misconceptions
- Thinking the r⁻¹² repulsion term has a physical origin; it is chosen for computational convenience, not because repulsion follows a 12th-power law (e.g., exponential functions are more accurate).
- Confusing ε (well depth, positive) with the total interaction energy (which is negative at the minimum of the potential).

## Questions

```yaml
- question: "A molecule pair has an LJ potential with σ = 3.4 Å. At what separation distance does the potential energy reach its minimum (equilibrium) value?"
  type: multiple-choice
  options:
    - "r = σ = 3.4 Å, because σ is defined as the equilibrium separation"
    - "r = 2^(1/6) × σ ≈ 3.82 Å, just beyond the zero-crossing"
    - "r = 2σ = 6.8 Å, where the long-range attraction is strongest"
    - "r = σ/2 = 1.7 Å, inside the repulsive core"
  answer: 1
  explanation: "σ is the collision diameter — the distance at which the LJ potential crosses zero (repulsion and attraction exactly balance). The actual minimum occurs slightly farther out, at r_min = 2^(1/6)σ ≈ 1.12σ. This is a common confusion: σ is a zero-crossing, not an equilibrium. The well depth ε (positive) is the magnitude of the potential at r_min, and the potential energy there is −ε."

- question: "Why is the r⁻¹² repulsion term used in the Lennard-Jones potential rather than an exponential function, even though the exponential is physically more accurate?"
  type: multiple-choice
  options:
    - "Quantum mechanics rigorously derives a 12th-power repulsion from Pauli exclusion between electron clouds"
    - "Experimental data for noble gases precisely fit a 12th-power law at short range"
    - "The exponent 12 is the square of 6, making the repulsion term the square of the attractive term and drastically simplifying computation"
    - "An exponential function cannot produce the steep repulsive wall observed in molecular collisions"
  answer: 2
  explanation: "The r⁻¹² choice is computational convenience, not physical rigor. Because (σ/r)¹² = [(σ/r)⁶]², the repulsive term can be computed by squaring an already-computed quantity — halving the number of expensive power operations in molecular simulation. Exponential repulsion (the Buckingham potential) is physically more accurate but harder to compute. The key insight is that the r⁻¹² exponent has no deep theoretical justification; it was chosen to make the math tractable."

- question: "The second virial coefficient B(T) is negative at low temperatures for gases modeled by the Lennard-Jones potential."
  type: true-false
  answer: true
  explanation: "At low temperatures, kT is small relative to the well depth ε, so thermal energy cannot overcome the attractive part of the potential. Molecules spend more time near each other than a purely repulsive gas would, making the gas more compressible than ideal. This corresponds to negative B(T). At high temperatures, kT >> ε, the attraction becomes negligible, and the hard repulsive core dominates — B(T) becomes positive. This temperature dependence is what makes B(T) measurements across a range of T so useful for simultaneously fitting both ε and σ."

- question: "The parameter ε in the Lennard-Jones potential represents the total potential energy of two molecules at their equilibrium separation."
  type: true-false
  answer: false
  explanation: "ε (positive) is the depth of the energy well — the magnitude of the minimum potential energy. The actual potential energy at the minimum is −ε (negative, since it represents attraction). The sign matters: the well depth ε tells you how strongly the molecules attract each other, but the potential energy there is −ε. Confusing ε with the total energy leads to sign errors when calculating thermodynamic quantities from the pair potential."

- question: "Why does the second virial coefficient B(T) provide an experimental route to determining the Lennard-Jones parameters ε and σ? What is the physical logic connecting a macroscopic PVT measurement to a microscopic pair potential?"
  type: short-answer
  answer: "B(T) = −2πN_A∫[exp(−u(r)/kT)−1]r²dr. This integral directly encodes how much two molecules deviate from independent (ideal) behavior due to their pairwise interaction. At each temperature, B(T) is a single number derived from PVT data. Because the LJ potential has two parameters (ε, σ) and B(T) depends on temperature, measuring B across a range of temperatures gives a curve whose shape and magnitude can only be matched by specific values of ε and σ. The bridge is statistical mechanics: the Mayer f-function exp(−u/kT)−1 weights the interaction energy by Boltzmann factors, connecting the microscopic energy landscape to the macroscopic equation of state."
  explanation: "The key insight is that PVT deviations from ideality encode pair interaction information. Ideal gas molecules don't interact; real gas deviations are caused by interactions. B(T) captures the pairwise contribution. Because the LJ potential changes shape with ε and σ, different parameter choices produce differently shaped B(T) curves. Fitting experimental B(T) data constrains both parameters simultaneously — turning PVT measurements taken with a pressure gauge into knowledge about molecular interaction strength and size."
```

## Explainer

From intermolecular forces, you know qualitatively that molecules attract at long range (London dispersion, dipole-dipole) and repel at short range (electron cloud overlap). **Intermolecular potential models** translate these qualitative ideas into mathematical functions that predict the exact energy of interaction at any separation distance r. Having an equation instead of a hand-waving description is what makes it possible to calculate real physical properties — gas viscosities, boiling points, crystal structures — from molecular parameters.

The workhorse model is the **Lennard-Jones (LJ) 12-6 potential**: u(r) = 4ε[(σ/r)¹² − (σ/r)⁶]. The (σ/r)⁶ term captures the attractive London dispersion interaction, which has a solid theoretical basis in quantum mechanics (induced-dipole/induced-dipole interactions fall off as r⁻⁶). The (σ/r)¹² repulsive term models the sharp increase in energy when electron clouds overlap, though the exponent 12 is chosen for mathematical convenience (it is simply the square of 6, making computation efficient) rather than physical rigor. The two parameters have intuitive meanings: **ε** is the depth of the energy well — how strongly the molecules attract at their optimal separation — and **σ** is the collision diameter — the distance at which the potential crosses zero, meaning repulsion and attraction exactly balance. The minimum energy occurs at r_min = 2^(1/6)σ ≈ 1.12σ, just slightly beyond the collision diameter.

For molecules with permanent dipoles, the LJ potential alone is insufficient. You must add **electrostatic terms** that depend on molecular orientation: the dipole-dipole interaction (∝ r⁻³), the dipole-induced dipole interaction (∝ r⁻⁶), and for ions, Coulombic terms (∝ r⁻¹). These orientation-dependent contributions explain why polar molecules like water have much stronger intermolecular interactions than nonpolar molecules of similar size. More sophisticated models like the Stockmayer potential combine the LJ function with a point dipole, while modern force fields used in molecular simulations assign partial charges to individual atoms and sum pairwise Coulombic and LJ interactions across all atom pairs.

The bridge between these microscopic pair potentials and macroscopic behavior runs through the **second virial coefficient** B(T), which describes the first correction to ideal gas behavior in the equation PV = nRT(1 + B/V + ...). The integral B(T) = −2πN_A∫₀^∞[exp(−u(r)/kT) − 1]r²dr connects the pair potential directly to measurable PV data. At low temperatures, attractions dominate and B is negative (gas is more compressible than ideal); at high temperatures, repulsions dominate and B is positive. Fitting experimental B(T) data across a range of temperatures determines ε and σ for a given molecule, turning the abstract potential into a calibrated, predictive tool.
