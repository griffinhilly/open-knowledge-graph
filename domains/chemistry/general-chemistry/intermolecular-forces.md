---
id: intermolecular-forces
title: Intermolecular Forces
domain: chemistry
course: general-chemistry
prerequisites:
- id: molecular-polarity
  type: hard
builds-toward:
- solution-concentration
- colligative-properties
tags:
- London-dispersion
- dipole-dipole
- hydrogen-bonding
- van-der-Waals
- boiling-point
- viscosity
stage: formal-systems
status: validated
---

# Intermolecular Forces

## Core Idea
Intermolecular forces (IMFs) are attractive forces between molecules that determine physical properties like boiling point, melting point, viscosity, and surface tension. London dispersion forces (temporary induced dipoles) act on all molecules and increase with molecular size and polarizability. Polar molecules additionally experience dipole-dipole forces. Hydrogen bonding — a strong dipole-dipole interaction — occurs when H is bonded directly to N, O, or F and is responsible for water's anomalously high boiling point and many biological phenomena.

## How It's Best Learned
Rank compounds by expected boiling point by identifying their dominant IMF type and relative strengths. Compare isomers like n-pentane vs. neopentane (both dispersion only, but different surface areas) and ethanol vs. dimethyl ether (H-bonding vs. dipole-dipole).

## Common Misconceptions
- 'Hydrogen bond' is a misnomer suggesting a covalent bond — it is a strong intermolecular attractive force, not a covalent bond.
- London dispersion forces are not always weak: for large molecules like long-chain alkanes, they can exceed hydrogen bonding in total magnitude.

## Questions

```yaml
- question: "Four compounds are listed: CH₄, HCl, NH₃, and C₁₀H₂₂ (decane). Which pair would you expect to have the highest and lowest boiling points, respectively?"
  type: multiple-choice
  options: ["NH₃ highest, CH₄ lowest", "C₁₀H₂₂ highest, CH₄ lowest", "NH₃ highest, HCl lowest", "HCl highest, NH₃ lowest"]
  answer: 1
  explanation: "C₁₀H₂₂ (decane, a large nonpolar alkane) has only London dispersion forces, but with 10 carbons and a large polarizable electron cloud, its total dispersion forces are very strong — giving it a boiling point of 174°C. NH₃ has hydrogen bonding (H bonded to N) but is a small molecule, so it boils at -33°C. CH₄ is the smallest nonpolar molecule with the weakest dispersion forces, boiling at -161°C. This example illustrates that London forces are not always weak."

- question: "A hydrogen bond is a type of covalent bond that forms between a hydrogen atom and an electronegative atom in the same molecule."
  type: true-false
  answer: false
  explanation: "Hydrogen bonds are intermolecular (or intramolecular) attractive forces, not covalent bonds. A hydrogen bond forms between a hydrogen atom that is covalently bonded to N, O, or F (which makes the H highly δ+) and a lone pair on a neighboring N, O, or F atom (which is δ−). This is an electrostatic attraction, far weaker than a covalent bond — roughly 5-30 kJ/mol vs. 200-1000 kJ/mol for covalent bonds."

- question: "Explain why water (H₂O, MW = 18 g/mol) has a much higher boiling point (100°C) than hydrogen sulfide (H₂S, MW = 34 g/mol), even though H₂S is a heavier molecule."
  type: short-answer
  answer: "Water forms hydrogen bonds (H bonded to O, a highly electronegative atom), which are much stronger than the dipole-dipole forces in H₂S. To vaporize water, these strong hydrogen bonds must be broken, requiring substantially more energy than breaking the weaker IMFs in H₂S. Despite H₂S being heavier and having larger London dispersion forces, its dominant IMF (dipole-dipole) is much weaker than hydrogen bonding."
  explanation: "This comparison is a classic demonstration that molecular weight alone does not predict boiling point — IMF type matters more. Oxygen is electronegative enough to create a strong δ+ on H in water, enabling true hydrogen bonding. Sulfur is less electronegative, so H₂S has only dipole-dipole and London forces, which are collectively much weaker. The boiling point difference (100°C vs. -60°C) reflects the energy difference in overcoming these forces."
```

## Explainer

Covalent bonds hold atoms together within a molecule. But what holds molecules close to each other — as a liquid or solid — rather than flying apart as a gas? The answer is intermolecular forces (IMFs): attractive interactions between molecules. These forces are electrostatic in origin (opposite charges attract), but they arise from the distribution of electrons rather than from full ionic charges. Understanding IMFs explains a huge range of physical properties: why water is liquid at room temperature, why oils don't mix with water, why large alkanes are waxes while small ones are gases.

The weakest IMFs are London dispersion forces, which act on every molecule, polar or nonpolar. They arise from instantaneous fluctuations in electron distribution: at any given moment, the electron cloud of a molecule might be shifted slightly to one side, creating a temporary dipole. This temporary dipole induces a complementary dipole in a neighboring molecule, and the two are momentarily attracted. The key variable is polarizability — how easily the electron cloud can be distorted. Large molecules with many electrons are more polarizable and therefore have stronger dispersion forces. This is why boiling points of nonpolar molecules (like the alkane series) increase steadily with molecular size: more carbons mean more electrons, more polarizability, and stronger dispersion forces.

Polar molecules experience dipole-dipole forces in addition to dispersion. When you learned about molecular polarity, you found that molecules like HCl and SO₂ have permanent dipole moments — one end is persistently δ+ and the other δ−. Adjacent polar molecules orient themselves so that opposite partial charges align, creating a net attraction. These dipole-dipole interactions are stronger than dispersion forces for molecules of similar size.

Hydrogen bonding is a special, strong form of dipole-dipole interaction that occurs only when H is covalently bonded to N, O, or F — the three most electronegative elements. Because these elements are so electronegative, they pull the shared electron pair far from the hydrogen, leaving it nearly bare (a proton with very little electron shielding). This δ+ hydrogen can then strongly attract a lone pair on a neighboring N, O, or F atom. The resulting hydrogen bond (typically 15–30 kJ/mol) is much stronger than ordinary dipole-dipole forces, though still far weaker than a covalent bond. Water's unusually high boiling point, surface tension, and its expansion upon freezing all trace back to its extensive hydrogen bonding network. In biology, hydrogen bonds are essential to DNA base pairing and protein secondary structure — they are strong enough to maintain structure but weak enough to be broken and reformed dynamically.
