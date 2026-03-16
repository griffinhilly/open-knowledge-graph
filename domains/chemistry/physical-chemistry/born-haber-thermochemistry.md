---
id: born-haber-thermochemistry
title: Born-Haber Cycle and Lattice Energy
domain: chemistry
course: physical-chemistry
prerequisites:
- id: hess-law-of-enthalpy
  type: hard
- id: ionic-bonding
  type: hard
builds-toward:
- phase-diagrams-clausius-clapeyron
tags:
- thermochemistry
- born-haber
- lattice-energy
- ionic
stage: advanced
status: draft
---

# Born-Haber Cycle and Lattice Energy

## Core Idea
The Born-Haber cycle is a thermochemical method relating formation enthalpy of an ionic solid to ionization energies, electron affinities, and lattice energy. By decomposing the overall process into individual steps (ionization, dissociation, vaporization, ionic interaction), we can experimentally determine lattice energy—the energy required to completely dissociate one mole of solid ionic compound into gaseous ions. Lattice energy reveals the strength of electrostatic interactions and predicts stability trends.

## How It's Best Learned
Draw complete Born-Haber cycles for common salts (NaCl, CaO, MgF₂) and verify closure using Hess's law. Correlate lattice energies with ionic charges and sizes using Born's equation. Explain why some compounds don't form based on energetics.

## Common Misconceptions
- Lattice energy is the same as formation enthalpy (formation enthalpy includes vaporization and other steps).
- Higher lattice energy always means more stable compound (thermodynamic stability depends on ΔG, not just ΔH).

## Explainer

You already know from Hess's law that the enthalpy change for a reaction is independent of the path — you can break any process into convenient steps, sum their enthalpies, and get the same answer as the direct route. The Born-Haber cycle applies this principle to the formation of ionic solids, and its real power is that it lets you determine **lattice energy** — a quantity that cannot be measured directly but reveals the strength of ionic bonding in a crystal.

Consider forming NaCl from its elements. The overall reaction is Na(s) + ½Cl₂(g) → NaCl(s), and the enthalpy of formation ΔH_f is measurable. The Born-Haber cycle decomposes this into five individual steps: (1) **sublimation** of solid sodium to gaseous atoms, (2) **ionization** of Na(g) to Na⁺(g) by removing an electron, (3) **dissociation** of Cl₂(g) into individual Cl(g) atoms, (4) **electron affinity** — Cl(g) gaining an electron to form Cl⁻(g), and (5) **lattice formation** — the gaseous ions Na⁺ and Cl⁻ coming together to form the crystalline solid. Steps 1–4 all have experimentally known values, and step 5 is the lattice energy you are solving for. Since Hess's law requires all steps to sum to ΔH_f, you simply rearrange: lattice energy = ΔH_f − (sum of steps 1–4).

The lattice energy you extract is almost always a large exothermic value — for NaCl, about −787 kJ/mol. This reflects the enormous electrostatic attraction between densely packed oppositely charged ions. **Coulomb's law** predicts the trends: lattice energy increases with higher ionic charges (MgO >> NaCl because Mg²⁺O²⁻ vs Na⁺Cl⁻) and decreases with larger ionic radii (LiF > LiI because F⁻ is smaller than I⁻, bringing the charges closer). The Born-Landé equation quantifies this, incorporating the Madelung constant that accounts for the geometry of the crystal lattice.

Beyond calculating a single number, the Born-Haber cycle explains why certain compounds exist and others do not. For instance, why doesn't NaCl₂ form? You can construct the hypothetical cycle: the second ionization energy of sodium (removing an electron from a noble gas core) is enormous, and no feasible lattice energy can compensate. The cycle makes this energetic impossibility quantitatively clear. Similarly, comparing CaCl versus CaCl₂ reveals that the much larger lattice energy of the 2+ salt more than compensates for the large second ionization energy of calcium, explaining why CaCl₂ is the stable form. Every time you ask "why does this ionic compound form with these charges and not others?" the Born-Haber cycle provides the thermochemical accounting to answer.
