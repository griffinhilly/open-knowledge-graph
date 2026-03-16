---
id: dielectric-materials-polarization
title: Dielectric Materials and Polarization
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-dipole-moment-field
  type: hard
- id: capacitor-circuits-series-parallel
  type: soft
builds-toward:
- dielectric-susceptibility-constant
- energy-density-electric-field
tags:
- dielectric
- polarization
- material
stage: formal-systems
status: draft
---

# Dielectric Materials and Polarization

## Core Idea
Dielectrics are insulators; applied fields polarize atoms/molecules, creating induced dipoles aligned with the field. Polarization creates an induced electric field that opposes the external field, reducing the total field inside the material.

## Explainer

From your study of electric dipole moments, you know that a pair of equal and opposite charges separated by a small distance constitutes a dipole, characterized by a dipole moment **p** = qd pointing from negative to positive charge. In a vacuum, individual atoms and molecules are electrically neutral and symmetric. But when you apply an external electric field, that field pushes positive charges slightly in one direction and negative charges in the other, stretching the electron cloud away from the nucleus. The result is an **induced dipole**: each atom acquires a tiny dipole moment aligned with the applied field. This is **electric polarization**.

**Polarization P** is the dipole moment per unit volume — the macroscopic average of all those microscopic induced dipoles. In a uniformly polarized material, the interior dipoles cancel each other (the positive end of one dipole is adjacent to the negative end of the next), but at the surfaces, charges are left uncompensated. These **bound surface charges** (σ_b = P · n̂) create their own electric field, directed *opposite* to the external field inside the material. The material pushes back.

This is why dielectrics reduce the electric field inside them. The total field inside is E = E₀ − E_induced, where E₀ is the applied field and E_induced arises from the bound charges. The ratio E₀/E defines the **dielectric constant** κ (or relative permittivity ε_r), which is always ≥ 1. For a capacitor filled with dielectric, the same surface charge on the plates now produces a weaker field inside, so the capacitor can store *more* charge at the same voltage. Capacitance increases by exactly the factor κ: C = κC₀. This is the practical payoff — dielectrics let you pack more energy into a given capacitor.

The degree of polarization depends on the material. In **linear dielectrics**, P is proportional to the applied field: P = ε₀χ_e E, where χ_e is the **electric susceptibility**. Highly polarizable materials (large χ_e) respond strongly, greatly reducing the internal field. Water (κ ≈ 80) is strongly polarizable because its permanent molecular dipoles align with the field in addition to being induced. Non-polar materials like polyethylene (κ ≈ 2.3) rely only on induced dipoles and respond weakly. In all cases, the effect of the dielectric is to partially screen the applied field, a phenomenon that underlies the operation of capacitors, insulators, and the optical properties of transparent materials.
