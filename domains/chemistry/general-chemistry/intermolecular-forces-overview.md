---
id: intermolecular-forces-overview
title: 'Intermolecular Forces: Dipole-Dipole, Hydrogen Bonding, and Dispersion'
domain: chemistry
course: general-chemistry
prerequisites:
- id: polarity-and-dipole-moments
  type: hard
builds-toward:
- solution-properties
- states-of-matter-phase-changes
tags:
- intermolecular forces
- hydrogen bonding
- dispersion forces
- dipole-dipole
stage: formal-systems
status: validated
---

# Intermolecular Forces: Dipole-Dipole, Hydrogen Bonding, and Dispersion

## Core Idea
Intermolecular forces are attractions between molecules. Dispersion forces (London forces) exist in all molecules and increase with molecular size. Dipole-dipole forces occur between polar molecules. Hydrogen bonding (a special dipole-dipole interaction) is the strongest and occurs when H is bonded to N, O, or F. These forces determine physical properties like boiling point and solubility.

## Questions

```yaml
- question: "Octane (C₈H₁₈, MW ≈ 114 g/mol, nonpolar) and formaldehyde (CH₂O, MW ≈ 30 g/mol, polar) are compared. Which has the higher boiling point, and why?"
  type: multiple-choice
  options:
    - "Formaldehyde, because polar molecules always have stronger IMFs than nonpolar molecules"
    - "Octane, because its much larger size produces stronger London dispersion forces that outweigh formaldehyde's dipole-dipole forces"
    - "They are approximately equal because the polarity effect and size effect cancel"
    - "Octane, because nonpolar molecules have no repulsive forces to overcome when boiling"
  answer: 1
  explanation: "Octane (bp 126°C) boils far higher than formaldehyde (bp −19°C) despite being nonpolar, because London dispersion forces scale with molecular size and polarizability. Octane's large electron cloud generates much stronger dispersion forces than formaldehyde's tiny dipole-dipole forces can produce. The common misconception (option A) is treating IMF type as a hierarchy without considering magnitude — in reality, a large nonpolar molecule can easily outperform a small polar one in total IMF strength."

- question: "Which combination of atoms in a molecule qualifies it to participate in hydrogen bonding as the hydrogen bond donor?"
  type: multiple-choice
  options:
    - "Any hydrogen atom adjacent to a carbon atom"
    - "Hydrogen bonded directly to nitrogen, oxygen, or fluorine"
    - "Any polar bond involving hydrogen"
    - "Hydrogen bonded to any atom with a lone pair"
  answer: 1
  explanation: "Hydrogen bonding requires H bonded directly to N, O, or F — the three most electronegative small atoms. The small atomic radius of these atoms and the resulting large partial positive charge on H allow it to approach the lone pair on another N, O, or F molecule very closely, creating an unusually strong interaction. C-H bonds, despite involving hydrogen, do not typically form hydrogen bonds because carbon is not electronegative enough to create the necessary partial charge on H."

- question: "London dispersion forces are only present in nonpolar molecules; polar molecules experience dipole-dipole forces instead."
  type: true-false
  answer: false
  explanation: "London dispersion forces are present in *all* molecules — polar and nonpolar alike. They arise from instantaneous fluctuations in electron density that create temporary dipoles. Polar molecules experience both dipole-dipole forces AND dispersion forces simultaneously. This matters because it means the total IMFs in a large polar molecule include both contributions. The misconception that polar molecules 'use' a different mechanism misses this additive nature of intermolecular forces."

- question: "Water (H₂O, MW = 18 g/mol) has a higher boiling point than hydrogen sulfide (H₂S, MW = 34 g/mol) despite being significantly lighter."
  type: true-false
  answer: true
  explanation: "Water (bp 100°C) boils far higher than H₂S (bp −60°C) even though H₂S has nearly twice the molecular weight. The reason is hydrogen bonding: water has O-H bonds that form strong hydrogen bonds, while H₂S does not (sulfur is insufficiently electronegative and too large). This single example powerfully illustrates that IMF type can matter more than size. The heavier molecule (H₂S) relies only on dispersion forces and weak dipole forces, while the lighter molecule (H₂O) benefits from the strongest type of IMF available to neutral molecules."

- question: "Why does the boiling point increase steadily going down the noble gas group (He, Ne, Ar, Kr, Xe), even though all these elements are nonpolar with no permanent dipole moment?"
  type: short-answer
  answer: "As you go down the noble gas group, each element has more electrons and a larger, more easily distorted electron cloud — it is more polarizable. More polarizable electron clouds generate stronger instantaneous dipoles and therefore stronger London dispersion forces between atoms. Since dispersion forces are the only IMF present (no permanent dipoles, no hydrogen bonds), the boiling point rises monotonically with polarizability and thus atomic size."
  explanation: "This is the clearest demonstration that London dispersion forces are real and significant. The progression (He: −269°C, Ne: −246°C, Ar: −186°C, Kr: −153°C, Xe: −108°C) shows exactly what increasing dispersion force strength looks like experimentally. The only variable changing is electron cloud size — proving that polarizability drives dispersion force strength."
```

## Explainer

From your study of polarity and dipole moments, you know that some molecules have permanent partial charges — a δ+ end and a δ− end — while others have their electron density distributed symmetrically. **Intermolecular forces** (IMFs) are the attractions that arise between separate molecules as a consequence of these charge distributions. They are much weaker than the covalent bonds holding atoms together within a molecule, but they determine whether a substance is a gas, liquid, or solid at room temperature, and they control properties like boiling point, viscosity, and solubility.

The weakest and most universal type is **London dispersion forces**. Even in a completely nonpolar molecule like methane or argon, the electrons are in constant motion. At any instant, the electron cloud may be slightly lopsided, creating a fleeting, temporary dipole. This instantaneous dipole induces a complementary dipole in a neighboring molecule, and the two attract each other briefly before the electron clouds shift again. Individually, each interaction is tiny, but dispersion forces are present in every molecule — polar or nonpolar — and they grow stronger with molecular size because larger electron clouds are more easily distorted (more **polarizable**). This is why boiling points increase steadily down the noble gases: helium (bp −269°C), neon (−246°C), argon (−186°C), krypton (−153°C), xenon (−108°C) — all nonpolar, differing only in size.

**Dipole-dipole forces** add a second layer of attraction for polar molecules. The permanent δ+ end of one molecule is attracted to the δ− end of a neighbor, and molecules tend to orient themselves to maximize this favorable alignment. Dipole-dipole forces are stronger than dispersion forces alone for molecules of similar size, which is why acetone (polar, bp 56°C) boils higher than propane (nonpolar, bp −42°C) despite having similar molecular weights. **Hydrogen bonding** is a particularly strong form of dipole-dipole interaction that occurs when hydrogen is bonded directly to nitrogen, oxygen, or fluorine — the three most electronegative small atoms. The small size of hydrogen allows the δ+ hydrogen on one molecule to approach the lone pair on the N, O, or F of another molecule very closely, creating an unusually strong attraction. Hydrogen bonding is why water (bp 100°C) boils far higher than hydrogen sulfide (bp −60°C), even though H₂S is heavier.

The practical skill is predicting relative boiling points, melting points, and solubilities by identifying which IMFs are present. First, check for hydrogen bonding capability (H bonded to N, O, or F). Then check for permanent dipole (polar molecule). Finally, consider molecular size for dispersion forces. A large nonpolar molecule can actually have stronger total IMFs than a small polar one — dispersion forces in a large molecule like octane can outweigh the dipole-dipole forces in a small molecule like formaldehyde. The hierarchy is a starting point, but size always matters, and the real comparison requires considering all forces together.
