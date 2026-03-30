---
id: intermolecular-lennard-jones-potential
title: Intermolecular Forces and Lennard-Jones Potential
domain: chemistry
course: physical-chemistry
prerequisites:
- id: dipole-moment-molecular-polarity
  type: soft
- id: intermolecular-forces
  type: hard
builds-toward:
- osmotic-pressure-van-t-hoff
tags:
- intermolecular
- lennard-jones
- van-der-waals
- potential
stage: advanced
status: validated
---

# Intermolecular Forces and Lennard-Jones Potential

## Core Idea
Intermolecular forces arise from electrostatic interactions (ionic, dipole-dipole, hydrogen bonding) and dispersion forces (London forces from induced dipoles). The Lennard-Jones potential V(r) = -A/r⁶ + B/r¹² combines attractive r⁻⁶ dispersion with repulsive r⁻¹² hard-sphere repulsion, describing van der Waals interactions. This simple model explains real gas behavior, phase transitions, and physical properties like boiling points.

## Questions

```yaml
- question: "In the Lennard-Jones potential V(r) = 4ε[(σ/r)¹² − (σ/r)⁶], what does σ represent?"
  type: multiple-choice
  options:
    - "The equilibrium separation between two molecules — where the potential energy is at its minimum"
    - "The depth of the potential well, measuring the maximum attraction between two molecules"
    - "The distance at which the potential energy equals zero — interpreted as the effective molecular diameter"
    - "The distance at which the repulsive term first exceeds the attractive term"
  answer: 2
  explanation: "σ is the distance at which the potential crosses zero on the way from positive (repulsive) to negative (attractive) values. It represents the effective 'size' of a molecule — the hard-sphere diameter below which overlap becomes extremely costly. The equilibrium separation (minimum energy) is at r = 2^(1/6)·σ ≈ 1.12σ, which is slightly larger than σ. ε (epsilon) is the depth of the potential well, measuring the binding energy at equilibrium. These two parameters fully characterize a Lennard-Jones interaction and are fitted to experimental data."

- question: "Why is the repulsive term in the Lennard-Jones potential written as r⁻¹² rather than a form derived from quantum mechanics?"
  type: multiple-choice
  options:
    - "Because the r⁻¹² form is derived rigorously from the Pauli exclusion principle and matches experimental repulsion exactly"
    - "Because r⁻¹² produces a repulsive wall steep enough to mimic hard-sphere behavior, and r¹² = (r⁶)² is computationally convenient — requiring no extra power calculation"
    - "Because r⁻¹² ensures the potential minimum occurs exactly at r = σ"
    - "Because the repulsive exponent must always be twice the attractive exponent for mathematical consistency"
  answer: 1
  explanation: "The r⁻¹² exponent is not derived from first principles — it is a pragmatic choice. The true quantum mechanical repulsion (from Pauli exclusion and electron-electron overlap) does not have a simple power-law form. The r⁻¹² term was chosen because: (1) it rises steeply enough at short range to mimic hard-sphere repulsion, and (2) since the attractive term goes as r⁻⁶, computing r⁻¹² simply means squaring the already-computed r⁻⁶ term — a significant computational saving in molecular dynamics simulations. The convenience is computational, not physical."

- question: "The equilibrium separation between two Lennard-Jones molecules (where the potential energy is minimum) occurs at the distance σ."
  type: true-false
  answer: false
  explanation: "σ is where the potential energy equals zero, not where it is minimum. The minimum occurs at r = 2^(1/6)·σ ≈ 1.12σ — slightly larger than σ. At r = σ, the repulsive and attractive terms are equal in magnitude, so the net potential is zero, but the curve is still descending toward the minimum. This distinction matters: at σ, molecules would still attract each other and move closer; only at 2^(1/6)σ are they in equilibrium."

- question: "Doubling the intermolecular separation reduces the London dispersion attraction by a factor of 64."
  type: true-false
  answer: true
  explanation: "The attractive term in the Lennard-Jones potential scales as r⁻⁶. Doubling r means the attraction scales as (2r)⁻⁶ = r⁻⁶/64 — a reduction by a factor of 64. This steep distance dependence is why London dispersion forces are short-range and why closely packed molecules in a liquid experience far stronger cohesion than the same molecules in a gas. It also explains why large polarizable molecules (with stronger dispersion) have much higher boiling points than small ones."

- question: "What are the physical origins of the two terms in the Lennard-Jones potential, and why is the repulsive term written as r⁻¹² rather than a physically derived form?"
  type: short-answer
  answer: "The attractive r⁻⁶ term models London dispersion forces — quantum mechanical correlated fluctuations in electron density that create instantaneous dipole-induced dipole attractions. Its r⁻⁶ dependence comes from perturbation theory. The repulsive r⁻¹² term models Pauli exclusion repulsion when electron clouds overlap, but it is not derived from quantum mechanics — it was chosen because r¹² = (r⁶)² is computationally efficient and produces a sufficiently steep repulsive wall."
  explanation: "Understanding why r⁻¹² is a convenience rather than a derived result matters for knowing the model's limitations. Real repulsion falls off somewhat differently, and the LJ potential is known to be imperfect at very short and very long ranges. More accurate models exist, but LJ remains the workhorse of molecular simulation because its two-parameter simplicity (ε, σ) captures the essential physics at a low computational cost."
```

## Explainer

From your study of intermolecular forces, you know that molecules attract each other through dipole-dipole interactions, hydrogen bonds, and London dispersion forces, and that these attractions explain why gases condense into liquids. But how do you turn this qualitative picture into something you can calculate with? The **Lennard-Jones potential** is the standard mathematical model that captures the essential physics of how two nonbonded molecules interact as a function of the distance between them.

The potential has two terms that compete. The **attractive term** (−A/r⁶) represents London dispersion forces — the instantaneous dipole-induced dipole interactions that exist between all molecules. The r⁻⁶ dependence comes from quantum mechanical perturbation theory: as two molecules approach, the fluctuating electron cloud of one polarizes the other, creating a correlated attraction that falls off as the sixth power of distance. This is why dispersion forces are short-ranged — double the distance and the attraction drops by a factor of 64.

The **repulsive term** (+B/r¹²) models what happens when molecules get too close: their electron clouds overlap and the Pauli exclusion principle creates a steep repulsive wall. The r⁻¹² form is not derived from first principles — it is a mathematical convenience chosen because r¹² = (r⁶)², which makes computation efficient. The important physical point is that repulsion rises extremely steeply at short range, which is why molecules behave as if they have a definite "size" even though their electron clouds technically extend to infinity.

The Lennard-Jones potential is most commonly written in its parametrized form: V(r) = 4ε[(σ/r)¹² − (σ/r)⁶], where **ε** (epsilon) is the depth of the potential well — the maximum attraction between the two molecules — and **σ** (sigma) is the distance at which the potential crosses zero (the effective molecular diameter). The equilibrium separation, where attraction and repulsion exactly balance, occurs at r = 2^(1/6)·σ ≈ 1.12σ. These two parameters, ε and σ, are specific to each pair of molecule types and can be fitted to experimental data such as second virial coefficients, viscosities, or crystal structures. Despite its simplicity, the Lennard-Jones model successfully predicts real gas deviations from ideal behavior, estimates boiling points and heats of vaporization, and serves as the default pair potential in molecular dynamics simulations of liquids, proteins, and materials.
