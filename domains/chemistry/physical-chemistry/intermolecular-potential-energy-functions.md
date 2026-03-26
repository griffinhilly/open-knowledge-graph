---
id: intermolecular-potential-energy-functions
title: Intermolecular Potential Energy Surfaces
domain: chemistry
course: physical-chemistry
prerequisites:
- id: intermolecular-forces
  type: hard
- id: molecular-polarity
  type: hard
- id: intermolecular-lennard-jones-potential
  type: soft
builds-toward:
- van-der-waals-equation-of-state-advanced
- hydrogen-bonding-energetics
tags:
- intermolecular-forces
- potential
- interactions
- van-der-waals
stage: formal-systems
status: validated
---
# Intermolecular Potential Energy Surfaces

## Core Idea
Intermolecular interactions are quantified by pair potential functions U(r), which combine attractive terms (London dispersion, dipole-dipole, hydrogen bonding) and repulsive core interactions. The Lennard-Jones potential U(r) = 4ε[(σ/r)¹² − (σ/r)⁶] exemplifies this competition; the balance determines equilibrium intermolecular distance and intermolecular binding energy. These potentials are inputs to molecular dynamics simulations and solution models.

## Questions

```yaml
- question: "Two noble gases, A and B, have the same LJ σ parameter but gas A has a well depth ε twice as large as gas B. What physical property difference does this predict?"
  type: multiple-choice
  options:
    - "Gas A has a larger molecular radius, causing it to pack more densely in the liquid phase"
    - "Gas A has a higher boiling point, because deeper intermolecular attraction requires more thermal energy to overcome"
    - "Gas A and B have the same boiling point since σ — not ε — determines phase behavior"
    - "Gas A has a smaller equilibrium distance because the deeper well pulls molecules closer together"
  answer: 1
  explanation: "The well depth ε is the depth of the energy minimum — it directly measures the strength of intermolecular attraction. A deeper well means more energy is required to pull molecules apart, so more thermal energy (higher temperature) is needed to vaporize the liquid — hence a higher boiling point. Option D is tempting but wrong: the equilibrium distance r_min = 2^(1/6)σ depends only on σ, not on ε. Changing ε deepens the well without shifting its position. The boiling points of noble gases (He < Ne < Ar < Kr < Xe) correlate directly with increasing ε driven by larger, more polarizable electron clouds."

- question: "In the Lennard-Jones potential U(r) = 4ε[(σ/r)¹² − (σ/r)⁶], what physical phenomenon does the (σ/r)⁶ attractive term represent?"
  type: multiple-choice
  options:
    - "Covalent bond formation at close intermolecular range"
    - "Permanent dipole-dipole interactions between polar molecules"
    - "London dispersion forces from instantaneous dipole-induced dipole interactions"
    - "Hydrogen bonding between electronegative atoms and hydrogen"
  answer: 2
  explanation: "The r⁻⁶ dependence is well-grounded in quantum mechanical perturbation theory: London dispersion forces (instantaneous dipole-induced dipole) fall off exactly as 1/r⁶. This makes the attractive term the most physically justified part of the LJ potential. The repulsive term (r⁻¹²) is chosen for computational convenience, not from first principles. Options A, B, and D describe real intermolecular forces, but none of them produce a 1/r⁶ distance dependence; the LJ potential is specifically designed for nonpolar systems where dispersion is the dominant attractive interaction."

- question: "In the Lennard-Jones potential, the repulsive exponent 12 was derived from quantum mechanical calculations of Pauli repulsion between overlapping electron clouds."
  type: true-false
  answer: false
  explanation: "The exponent 12 was chosen for computational convenience — it is exactly the square of 6, meaning the repulsive term is simply the square of the attractive term and requires no additional computation. The physically accurate description of Pauli repulsion involves an exponential function (e^{−αr}), as used in the Buckingham potential. The LJ r⁻¹² form overestimates repulsion at short range and underestimates it at very short range compared to ab initio calculations. Its practical advantage is speed in molecular dynamics simulations, not physical accuracy."

- question: "As temperature increases, molecules in a Lennard-Jones liquid move further apart on average, even though the equilibrium distance is at the potential energy minimum, because the LJ well is asymmetric — steeper on the repulsive side than the attractive side."
  type: true-false
  answer: true
  explanation: "This is the molecular explanation of thermal expansion. At absolute zero, molecules would sit at r_min. As temperature increases, they vibrate with greater amplitude across the well. Because the repulsive wall is very steep (r⁻¹²) while the attractive tail is gentle (r⁻⁶), molecules sample further out on the attractive side during vibration than they penetrate on the repulsive side. The average position therefore shifts outward, increasing the average intermolecular distance — macroscopically observed as thermal expansion. A symmetric well would give no thermal expansion regardless of vibration amplitude."

- question: "Explain how the shape of the Lennard-Jones potential accounts for two seemingly contradictory properties of liquids: near-incompressibility under compression, and volume expansion upon heating."
  type: short-answer
  answer: "Near-incompressibility follows from the steep repulsive wall (r⁻¹² term): trying to push molecules closer together than r_min meets a rapidly increasing energy cost, requiring very large pressures to achieve small compressions. Thermal expansion follows from the asymmetry of the well: the steep repulsive side and gentle attractive side mean thermal vibrations cause molecules to spend more time on the attractive side, shifting the average separation outward as temperature increases."
  explanation: "These properties arise from different features of the same potential curve. The incompressibility is about the behavior at r < r_min (steep repulsive wall), while thermal expansion is about the asymmetric shape of the entire well. A perfectly symmetric well (like a harmonic oscillator) would give no thermal expansion — molecules would vibrate symmetrically around the minimum. The anharmonicity of the LJ well is what produces both effects, and this is why simple harmonic models of molecular vibration fail to predict thermal expansion while the LJ potential succeeds."
```

## Explainer

From your study of intermolecular forces, you know the qualitative picture: molecules attract each other through London dispersion, dipole-dipole, and hydrogen bonding interactions, but repel when they get too close and their electron clouds overlap. **Intermolecular potential energy functions** make this picture quantitative by expressing the interaction energy U as a mathematical function of the distance r between two molecules (or atoms). The shape of U(r) — a curve that plunges to a minimum and then rises steeply — encodes everything about how two molecules interact.

The most widely used model is the **Lennard-Jones (LJ) potential**: U(r) = 4ε[(σ/r)¹² − (σ/r)⁶]. This deceptively simple equation has two terms and two parameters. The attractive term (σ/r)⁶ captures **London dispersion forces**, which arise from instantaneous dipole-induced dipole interactions and fall off as 1/r⁶ — this is well-grounded in quantum mechanical perturbation theory. The repulsive term (σ/r)¹² models the steep wall of **Pauli repulsion** when electron clouds overlap. The exponent 12 is chosen for computational convenience (it is the square of 6) rather than from first principles, but it reproduces the essential physics: a hard, short-range repulsion. The parameter **ε** (epsilon) is the depth of the energy well — the strength of the attraction at the optimal distance. The parameter **σ** (sigma) is the distance at which U = 0, roughly the "size" of the molecule. The equilibrium distance (the minimum of U) occurs at r = 2^(1/6)σ ≈ 1.12σ.

The shape of the LJ curve explains many bulk properties. The well depth ε determines boiling points — deeper wells mean stronger attractions and higher boiling points. The equilibrium distance sets molecular packing in liquids and solids. The steepness of the repulsive wall explains why liquids are nearly incompressible. The asymmetry of the curve (steep repulsion, gentle attraction) explains thermal expansion: as temperature increases, molecules vibrate more broadly across the asymmetric well, and the average distance shifts outward.

Beyond the LJ potential, more sophisticated functions exist for specific interactions. The **Morse potential** adds an exponential form that better captures bond-like interactions. **Electrostatic terms** (Coulomb's law) are added for charged or polar species. **Buckingham potentials** use an exponential repulsion instead of r⁻¹². In molecular dynamics simulations, these functions are evaluated billions of times to compute forces between every pair of molecules, propagating their trajectories through time. The accuracy of any simulation — whether predicting protein folding, liquid viscosity, or gas solubility — ultimately depends on how well these potential functions represent the true intermolecular interactions.
