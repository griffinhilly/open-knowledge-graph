---
id: ionic-bonding
title: Ionic Bonding
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-trends
  type: hard
- id: ionization-energy-and-electron-removal
  type: soft
builds-toward:
- lewis-structures
- electrochemistry-basics
- metallic-bonding
tags:
- ions
- lattice-energy
- ionic-compounds
- cation
- anion
- crystal-lattice
stage: abstract-reasoning
status: validated
---

# Ionic Bonding

## Core Idea
Ionic bonds form when a metal atom transfers one or more electrons to a nonmetal atom, creating oppositely charged ions that attract each other electrostatically. The resulting ionic compound forms a three-dimensional crystal lattice — not discrete molecules — and the lattice energy (energy released when gaseous ions assemble into the lattice) determines stability and physical properties like melting point. Ionic compounds are generally hard, brittle, high-melting, and conduct electricity when dissolved in water or melted.

## How It's Best Learned
Practice writing formulas for ionic compounds by balancing charges, and connect lattice energy magnitudes to observable properties like hardness and melting point. Use periodic trends to predict which element pairs are likely to form ionic compounds (large electronegativity difference).

## Common Misconceptions
- Ionic compounds do not contain discrete molecules — the formula unit (e.g., NaCl) represents only the simplest ratio of ions in the lattice.
- Not all metal-nonmetal combinations form purely ionic bonds; some combinations have significant covalent character due to polarization effects.

## Questions

```yaml
- question: "Magnesium oxide (MgO) has a melting point of ~2852°C while sodium chloride (NaCl) melts at only 801°C. Which factor best explains this difference?"
  type: multiple-choice
  options:
    - "Mg is more electronegative than Na, making MgO bonds more polar"
    - "MgO has a different crystal structure that is inherently more stable"
    - "The lattice energy of MgO is much greater because Mg²⁺ and O²⁻ carry higher charges than Na⁺ and Cl⁻"
    - "Oxygen forms stronger covalent bonds than chlorine"
  answer: 2
  explanation: "Lattice energy is proportional to the product of ionic charges (Coulomb's law). MgO has 2+ and 2- charges vs NaCl's 1+ and 1-, so the electrostatic attraction is roughly four times stronger, yielding much higher lattice energy and therefore a much higher melting point. Electronegativity predicts whether bonding is ionic but does not determine lattice energy magnitude."

- question: "The formula NaCl represents a discrete molecule containing exactly one sodium atom covalently bonded to one chlorine atom."
  type: true-false
  answer: false
  explanation: "NaCl is not a molecule. Ionic compounds form extended three-dimensional crystal lattices in which each Na⁺ is surrounded by 6 Cl⁻ neighbors and each Cl⁻ is surrounded by 6 Na⁺ neighbors. The formula unit NaCl represents only the simplest whole-number ratio of ions in the lattice. There are no discrete NaCl pairs, and properties like molecular weight and boiling point do not apply in the same way they do for molecular compounds."

- question: "What is lattice energy, and what does a high lattice energy indicate about an ionic compound's physical properties?"
  type: short-answer
  answer: "Lattice energy is the energy released when gaseous ions assemble into a crystal lattice. A high lattice energy indicates strong electrostatic attraction between ions, which results in high hardness, high melting point, and generally lower solubility."
  explanation: "Lattice energy reflects the total electrostatic stabilization of the crystal. It increases with higher ionic charges and smaller ionic radii (ions closer together, stronger attraction by Coulomb's law). Breaking the lattice requires overcoming this energy, so high-lattice-energy compounds require more thermal energy to melt and are mechanically harder."
```

## Explainer

You know from periodic trends that metals have low ionization energies — they release electrons relatively easily — and that nonmetals have high electron affinities — they strongly attract electrons. Ionic bonding is what happens when these tendencies meet directly: a metal atom transfers one or more electrons to a nonmetal atom, converting both into charged ions. The metal becomes a cation (positive) and the nonmetal becomes an anion (negative), and opposite charges attract via Coulomb's law.

But what forms is not a single bonded pair of ions. Each cation attracts multiple anions in all directions, and each anion attracts multiple cations, building up a three-dimensional crystal lattice. In sodium chloride, every Na⁺ is surrounded by 6 Cl⁻ neighbors, and every Cl⁻ by 6 Na⁺ — a repeating cubic arrangement that extends for billions of ion pairs. The formula unit NaCl expresses only the simplest ratio of ions (1:1), not the existence of discrete NaCl molecules. This is a fundamental distinction from molecular compounds: there are no individual NaCl units you could isolate.

The energy holding this lattice together is the lattice energy — the energy released when gaseous ions come together to form the solid. Lattice energy is governed by Coulomb's law: it increases when ions carry higher charges and when ions are smaller (bringing opposite charges closer together). This is why MgO (Mg²⁺ and O²⁻, both small ions with charge ±2) melts at nearly 2852°C while NaCl (Na⁺ and Cl⁻, with charge ±1) melts at only 801°C — the MgO lattice energy is roughly four times larger. Whenever you need to predict relative melting points, hardness, or stability of ionic compounds, lattice energy is your primary tool.

The brittle behavior of ionic crystals also follows from the lattice structure. When a crystal is struck, a layer of ions shifts relative to the layer beneath it. If the shift brings like-charged ions into alignment across the plane, the resulting repulsion tears the crystal apart rather than allowing it to bend. This is structurally unlike metals, where delocalized electrons let layers slide past each other — that is why metals are malleable and ionic crystals are not.

Conductivity follows the same logic. In a solid ionic crystal, every ion is locked into a fixed lattice position and cannot move to carry electrical charge — so the solid does not conduct. Dissolve the crystal in water or melt it, and the ions become free to move, allowing the liquid to conduct electricity. This is why sodium chloride solution conducts electricity but solid sodium chloride does not. These properties — brittleness, high melting point, conductivity when dissolved or melted — are diagnostic signatures of ionic bonding, all traceable back to the crystal lattice structure.
