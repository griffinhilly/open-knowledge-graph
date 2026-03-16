---
id: dipole-moment-molecular-polarity
title: Dipole Moment and Molecular Polarity
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-geometry-basics
  type: hard
- id: electronegativity-and-bond-polarity
  type: hard
builds-toward:
- intermolecular-lennard-jones-potential
tags:
- dipole
- polarity
- moment
- molecular
stage: advanced
status: draft
---

# Dipole Moment and Molecular Polarity

## Core Idea
Dipole moment μ measures charge separation in a molecule (μ = q·r) and determines polarity and reactivity. Individual bond dipoles add vectorially; molecular geometry determines whether bond dipoles cancel (nonpolar) or sum (polar). Dipole moments can be calculated from electronegativity differences or measured spectroscopically. Molecular polarity predicts solubility, boiling point, reactivity, and intermolecular interactions.

## Explainer

You already know from electronegativity and bond polarity that when two atoms with different electronegativities share a bond, the electron density shifts toward the more electronegative atom, creating a **bond dipole** — a separation of partial positive (δ+) and partial negative (δ−) charges. The **dipole moment** quantifies this: μ = q × d, where q is the magnitude of the separated charge and d is the distance between the charge centers. The unit is the **debye** (D), where 1 D = 3.336 × 10⁻³⁰ C·m. A larger electronegativity difference or a longer bond gives a larger bond dipole.

The crucial insight is that molecular polarity depends on **geometry**, not just on individual bond dipoles. Each bond dipole is a vector — it has both magnitude and direction — and the **molecular dipole moment** is the vector sum of all bond dipoles. This is why CO₂ is nonpolar despite having two very polar C=O bonds: the molecule is linear, so the two bond dipoles point in exactly opposite directions and cancel to zero. Water, by contrast, has a bent geometry (~104.5°), so its two O–H bond dipoles add constructively to produce a net dipole moment of 1.85 D. The same principle applies to more complex molecules: CCl₄ (tetrahedral, four identical C–Cl dipoles) is nonpolar because the vectors cancel; CHCl₃ is polar because replacing one Cl with H breaks the symmetry.

To predict molecular polarity, start from your knowledge of molecular geometry (VSEPR). Draw the structure, assign bond dipoles based on electronegativity differences, and then add the vectors. Highly symmetric molecules (linear with identical bonds, trigonal planar like BF₃, tetrahedral like CH₄ or CCl₄) will be nonpolar regardless of individual bond polarity. Any asymmetry — different substituents, lone pairs that distort geometry — generally produces a net dipole. Lone pairs contribute their own dipole component pointing away from the nucleus, which is why NF₃ (μ = 0.23 D) has a much smaller dipole than NH₃ (μ = 1.47 D): in NH₃ the lone pair dipole reinforces the N–H bond dipoles, while in NF₃ the lone pair dipole opposes the N–F bond dipoles.

Molecular polarity has far-reaching consequences. Polar molecules experience **dipole-dipole interactions** that raise boiling points relative to nonpolar molecules of similar size. They dissolve preferentially in polar solvents ("like dissolves like"). In spectroscopy, only molecules with a permanent dipole moment absorb in the microwave region (pure rotational spectroscopy), and dipole moment changes during vibration determine infrared absorption intensities. In chemical reactivity, the dipole moment reveals where electron density is concentrated, guiding predictions about nucleophilic and electrophilic sites.
