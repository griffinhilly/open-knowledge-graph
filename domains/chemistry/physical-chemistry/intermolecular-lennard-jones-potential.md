---
id: intermolecular-lennard-jones-potential
title: Intermolecular Forces and Lennard-Jones Potential
domain: chemistry
course: physical-chemistry
prerequisites:
- id: dipole-moment-molecular-polarity
  type: soft
- id: intermolecular-forces-overview
  type: hard
builds-toward:
- osmotic-pressure-van-t-hoff
tags:
- intermolecular
- lennard-jones
- van-der-waals
- potential
stage: advanced
status: draft
---

# Intermolecular Forces and Lennard-Jones Potential

## Core Idea
Intermolecular forces arise from electrostatic interactions (ionic, dipole-dipole, hydrogen bonding) and dispersion forces (London forces from induced dipoles). The Lennard-Jones potential V(r) = -A/r⁶ + B/r¹² combines attractive r⁻⁶ dispersion with repulsive r⁻¹² hard-sphere repulsion, describing van der Waals interactions. This simple model explains real gas behavior, phase transitions, and physical properties like boiling points.

## Explainer

From your study of intermolecular forces, you know that molecules attract each other through dipole-dipole interactions, hydrogen bonds, and London dispersion forces, and that these attractions explain why gases condense into liquids. But how do you turn this qualitative picture into something you can calculate with? The **Lennard-Jones potential** is the standard mathematical model that captures the essential physics of how two nonbonded molecules interact as a function of the distance between them.

The potential has two terms that compete. The **attractive term** (−A/r⁶) represents London dispersion forces — the instantaneous dipole-induced dipole interactions that exist between all molecules. The r⁻⁶ dependence comes from quantum mechanical perturbation theory: as two molecules approach, the fluctuating electron cloud of one polarizes the other, creating a correlated attraction that falls off as the sixth power of distance. This is why dispersion forces are short-ranged — double the distance and the attraction drops by a factor of 64.

The **repulsive term** (+B/r¹²) models what happens when molecules get too close: their electron clouds overlap and the Pauli exclusion principle creates a steep repulsive wall. The r⁻¹² form is not derived from first principles — it is a mathematical convenience chosen because r¹² = (r⁶)², which makes computation efficient. The important physical point is that repulsion rises extremely steeply at short range, which is why molecules behave as if they have a definite "size" even though their electron clouds technically extend to infinity.

The Lennard-Jones potential is most commonly written in its parametrized form: V(r) = 4ε[(σ/r)¹² − (σ/r)⁶], where **ε** (epsilon) is the depth of the potential well — the maximum attraction between the two molecules — and **σ** (sigma) is the distance at which the potential crosses zero (the effective molecular diameter). The equilibrium separation, where attraction and repulsion exactly balance, occurs at r = 2^(1/6)·σ ≈ 1.12σ. These two parameters, ε and σ, are specific to each pair of molecule types and can be fitted to experimental data such as second virial coefficients, viscosities, or crystal structures. Despite its simplicity, the Lennard-Jones model successfully predicts real gas deviations from ideal behavior, estimates boiling points and heats of vaporization, and serves as the default pair potential in molecular dynamics simulations of liquids, proteins, and materials.
