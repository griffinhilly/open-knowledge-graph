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

## Questions

```yaml
- question: "MgO has a lattice energy of approximately −3791 kJ/mol, much larger than NaCl's −787 kJ/mol. What is the primary reason for this difference?"
  type: multiple-choice
  options:
    - "MgO has a higher molar mass, so more energy is released when the crystal forms"
    - "MgO adopts a different crystal structure that packs ions more efficiently"
    - "Mg²⁺ and O²⁻ carry higher charges and have smaller ionic radii than Na⁺ and Cl⁻, producing much stronger electrostatic attraction"
    - "The enthalpy of formation of MgO is larger, so its lattice energy must be larger too"
  answer: 2
  explanation: "Lattice energy is fundamentally an electrostatic phenomenon governed by Coulomb's law: it increases with higher ionic charges and decreases with larger ionic radii. MgO has doubly charged ions (2+/2−) while NaCl has singly charged ions (1+/1−). The charge factor alone increases lattice energy by roughly a factor of four (2×2 vs 1×1). Additionally, Mg²⁺ and O²⁻ are smaller than Na⁺ and Cl⁻, bringing charges closer together. The combination of higher charge and smaller size explains the nearly five-fold difference in lattice energy. Note that option D confuses cause and effect: lattice energy is a component of the formation enthalpy calculation, not derived from it."

- question: "Why can lattice energy not be measured directly by calorimetry, unlike most other enthalpies in the Born-Haber cycle?"
  type: multiple-choice
  options:
    - "Lattice energies are too small to detect with standard calorimetric equipment"
    - "There is no practical way to combine a mole of gaseous cations with a mole of gaseous anions under controlled conditions to directly measure the heat released"
    - "Calorimetry only measures bond energies in molecular compounds, not ionic solids"
    - "The lattice energy and enthalpy of formation are the same quantity, so measuring one measures the other"
  answer: 1
  explanation: "Lattice energy is defined as the energy change when gaseous ions condense into a crystal: Na⁺(g) + Cl⁻(g) → NaCl(s). Performing this reaction in a calorimeter would require starting with isolated gaseous ions — an experimentally impractical starting state. You cannot easily generate and bottle a mole of gaseous Na⁺ and Cl⁻ ions. This is why the Born-Haber cycle is necessary: it provides an indirect route using measurable quantities (ionization energy, electron affinity, sublimation enthalpy, dissociation enthalpy, and formation enthalpy) to calculate lattice energy as the unknown term via Hess's law."

- question: "The lattice energy of an ionic compound equals its standard enthalpy of formation."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions about the Born-Haber cycle. Lattice energy is only one step in the formation process. The standard enthalpy of formation (e.g., Na(s) + ½Cl₂(g) → NaCl(s)) also includes sublimation of the metal, dissociation of the halogen molecule, ionization of the metal, and electron affinity of the nonmetal. The lattice energy is the last step: gaseous ions → solid crystal. It is typically the largest single term, but it is not equal to ΔH_f. The Born-Haber cycle's entire purpose is to relate these distinct quantities through Hess's law."

- question: "The Born-Haber cycle is an application of Hess's law: because enthalpy is a state function, the sum of all steps in the cycle must equal the directly measurable enthalpy of formation."
  type: true-false
  answer: true
  explanation: "This is the core principle. Hess's law states that the total enthalpy change is path-independent — only the initial and final states matter. The Born-Haber cycle constructs a multi-step path (sublimation + ionization + dissociation + electron affinity + lattice formation) from the same reactants to the same product as the direct formation reaction. All steps must sum to ΔH_f. Because every step except lattice energy is independently measurable, lattice energy can be solved as the one unknown term."

- question: "Using the Born-Haber framework, explain why the hypothetical compound NaCl₂ does not form as a stable ionic solid."
  type: short-answer
  answer: "Forming NaCl₂ would require removing two electrons from sodium — the first ionization energy (removing the outer 3s electron, ~496 kJ/mol) plus the enormous second ionization energy (removing an electron from sodium's stable neon-like core, ~4562 kJ/mol). The total ionization cost for Na²⁺ is roughly 5058 kJ/mol. No feasible lattice energy for a Na²⁺/Cl⁻ compound (only singly charged Cl⁻ ions) could compensate for this enormous energetic input. The Born-Haber cycle makes this explicit: summing all steps for the hypothetical NaCl₂ gives a strongly positive ΔH_f, meaning the compound is thermodynamically unstable relative to the elements."
  explanation: "This question requires using the Born-Haber logic as an explanatory tool, not just a calculation procedure. The key insight is that lattice energy scales with charge, but going from NaCl to NaCl₂ only doubles the charge on the cation while the second ionization energy increases by roughly an order of magnitude. The energetic accounting shows why real ionic compounds form with the specific charges they do — not because of convention, but because of thermodynamic necessity."
```

## Explainer

You already know from Hess's law that the enthalpy change for a reaction is independent of the path — you can break any process into convenient steps, sum their enthalpies, and get the same answer as the direct route. The Born-Haber cycle applies this principle to the formation of ionic solids, and its real power is that it lets you determine **lattice energy** — a quantity that cannot be measured directly but reveals the strength of ionic bonding in a crystal.

Consider forming NaCl from its elements. The overall reaction is Na(s) + ½Cl₂(g) → NaCl(s), and the enthalpy of formation ΔH_f is measurable. The Born-Haber cycle decomposes this into five individual steps: (1) **sublimation** of solid sodium to gaseous atoms, (2) **ionization** of Na(g) to Na⁺(g) by removing an electron, (3) **dissociation** of Cl₂(g) into individual Cl(g) atoms, (4) **electron affinity** — Cl(g) gaining an electron to form Cl⁻(g), and (5) **lattice formation** — the gaseous ions Na⁺ and Cl⁻ coming together to form the crystalline solid. Steps 1–4 all have experimentally known values, and step 5 is the lattice energy you are solving for. Since Hess's law requires all steps to sum to ΔH_f, you simply rearrange: lattice energy = ΔH_f − (sum of steps 1–4).

The lattice energy you extract is almost always a large exothermic value — for NaCl, about −787 kJ/mol. This reflects the enormous electrostatic attraction between densely packed oppositely charged ions. **Coulomb's law** predicts the trends: lattice energy increases with higher ionic charges (MgO >> NaCl because Mg²⁺O²⁻ vs Na⁺Cl⁻) and decreases with larger ionic radii (LiF > LiI because F⁻ is smaller than I⁻, bringing the charges closer). The Born-Landé equation quantifies this, incorporating the Madelung constant that accounts for the geometry of the crystal lattice.

Beyond calculating a single number, the Born-Haber cycle explains why certain compounds exist and others do not. For instance, why doesn't NaCl₂ form? You can construct the hypothetical cycle: the second ionization energy of sodium (removing an electron from a noble gas core) is enormous, and no feasible lattice energy can compensate. The cycle makes this energetic impossibility quantitatively clear. Similarly, comparing CaCl versus CaCl₂ reveals that the much larger lattice energy of the 2+ salt more than compensates for the large second ionization energy of calcium, explaining why CaCl₂ is the stable form. Every time you ask "why does this ionic compound form with these charges and not others?" the Born-Haber cycle provides the thermochemical accounting to answer.
