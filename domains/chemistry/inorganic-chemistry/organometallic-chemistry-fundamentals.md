---
id: organometallic-chemistry-fundamentals
title: Organometallic Chemistry Fundamentals
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: ligand-field-theory
  type: hard
- id: coordination-compounds-nomenclature
  type: soft
builds-toward:
- metal-carbonyls
- sandwich-compounds-metallocenes
- catalytic-cycles-wilkinson-grubbs
tags:
- organometallic
- metal-carbon bond
- electron counting
- 18-electron rule
- hapticity
stage: advanced
status: validated
---

# Organometallic Chemistry Fundamentals

## Core Idea
Organometallic chemistry studies compounds with direct metal-carbon bonds. These compounds follow predictable electron-counting rules — particularly the 18-electron rule (analogous to the octet rule for main group elements) — and their reactivity is governed by fundamental reaction types: oxidative addition, reductive elimination, migratory insertion, and beta-hydride elimination. Understanding these building blocks is essential for catalysis, where organometallic complexes enable transformations impossible for classical coordination compounds.

## Questions

```yaml
- question: "Cr(CO)₆ has 6 CO ligands coordinated to chromium(0). Using the ionic or covalent electron counting method, how many valence electrons surround the chromium?"
  type: multiple-choice
  options:
    - "12 electrons (Cr has 6, each CO donates 1)"
    - "18 electrons (Cr has 6, each CO donates 2)"
    - "16 electrons (Cr has 4 in the d-shell, each CO donates 2)"
    - "24 electrons (Cr has 6, each CO donates 3)"
  answer: 1
  explanation: "In the covalent electron counting method: Cr⁰ contributes 6 valence electrons (Group 6 metal). Each CO is a two-electron donor through its carbon lone pair. Six CO ligands contribute 12 electrons. Total: 6 + 12 = 18 electrons. This satisfies the 18-electron rule — the metal achieves a filled valence shell analogous to a noble gas configuration. The 18-electron rule explains why Cr(CO)₆, Fe(CO)₅, and Ni(CO)₄ all exist as stable, isolable compounds with different numbers of CO ligands."

- question: "The 18-electron rule states that stable organometallic complexes tend to have 18 valence electrons around the metal center, analogous to the octet rule for main group elements."
  type: true-false
  answer: true
  explanation: "The 18-electron rule arises because the metal valence shell consists of nine orbitals (five d, one s, three p) that can accommodate a maximum of 18 electrons. When all nine orbitals are filled through a combination of metal valence electrons and ligand donations, the complex achieves maximum stability — a closed-shell configuration. Like the octet rule, this is a guideline with exceptions: many stable organometallic compounds have 16 electrons (especially d⁸ square planar complexes like Vaska's compound) and some have fewer. But the 18-electron rule is the single most useful predictor of organometallic stoichiometry and reactivity."

- question: "Oxidative addition increases both the oxidation state and the coordination number of the metal center by 2."
  type: true-false
  answer: true
  explanation: "In oxidative addition, a substrate A-B adds across the metal center, breaking the A-B bond and forming two new M-A and M-B bonds. The metal formally goes from M^n to M^(n+2) (oxidized by 2) and from x-coordinate to (x+2)-coordinate. For example, when Vaska's compound IrCl(CO)(PPh₃)₂ (Ir⁺, 16e, 4-coordinate square planar) undergoes oxidative addition of H₂, it forms IrH₂Cl(CO)(PPh₃)₂ (Ir³⁺, 18e, 6-coordinate octahedral). The metal has been oxidized (given up electron density to form two new bonds) while gaining two new ligands."

- question: "Explain the 18-electron rule in terms of molecular orbital theory and identify two important classes of exceptions."
  type: short-answer
  answer: "In an octahedral complex, the nine metal valence orbitals (s + 3p + 5d) combine with ligand orbitals to form nine bonding MOs and nine antibonding MOs. The 18 electrons fill all nine bonding MOs, achieving maximum stability with no antibonding occupation. This is analogous to how the octet rule fills four bonding orbitals in main group chemistry. Two important classes of exceptions: (1) 16-electron complexes of d⁸ metals in square planar geometry (Rh⁺, Ir⁺, Ni²⁺, Pd²⁺, Pt²⁺), where one of the nine orbitals (d_x²−y²) is pushed so high in energy by the strong equatorial field that it remains empty — these are stable because the 'missing' orbital is antibonding. (2) Bulky ligands that sterically prevent enough ligands from coordinating to reach 18 electrons, as in many early transition metal complexes."
  explanation: "The 18-electron rule works best for middle and late transition metals with strong-field ligands (CO, PR₃, Cp). It is less reliable for early transition metals (which often have fewer than 18 electrons due to limited d-electron count and high oxidation states) and for f-block metals (where the f-orbitals add complexity)."
```

## Explainer

Organometallic chemistry occupies the intersection of inorganic and organic chemistry — it studies compounds where metal atoms are bonded directly to carbon. These are not esoteric curiosities: organometallic compounds catalyze the production of polymers, pharmaceuticals, and fuels on industrial scales. The field has produced multiple Nobel Prizes (Fischer and Wilkinson for metallocenes, Grubbs and Schrock for olefin metathesis, Suzuki and Heck for cross-coupling). Understanding organometallic chemistry begins with electron counting and the fundamental reaction types.

The 18-electron rule is the central organizing principle. A metal has nine valence orbitals (one s, three p, five d), and filling all nine with a total of 18 electrons produces maximum stability. To predict whether a compound obeys this rule, you count the metal's valence electrons plus the electrons donated by each ligand. CO donates 2, a cyclopentadienyl ring (Cp) donates 5, a hydride or alkyl group donates 1 (in the covalent counting method), and so on. Cr(CO)₆: 6 + 6(2) = 18. Fe(CO)₅: 8 + 5(2) = 18. Ni(CO)₄: 10 + 4(2) = 18. The rule correctly predicts the stoichiometry of all three metal carbonyls without any additional input.

Four elementary reaction types form the mechanistic alphabet of organometallic chemistry. Oxidative addition: a bond A-B breaks and both fragments add to the metal, increasing its oxidation state and coordination number by two. Reductive elimination: the reverse — two ligands couple and leave the metal, decreasing oxidation state and coordination number by two. Migratory insertion: a ligand migrates to an adjacent coordinated group, forming a new bond (as when a methyl group inserts into a coordinated CO to form an acyl). Beta-hydride elimination: a hydrogen on the beta-carbon of an alkyl ligand transfers to the metal, generating a metal hydride and a coordinated alkene. These four reactions, combined in sequence, constitute the catalytic cycles of virtually all homogeneous transition metal catalysis.

The concept of hapticity (η) describes how many atoms of a ligand are simultaneously bonded to the metal. An η¹-allyl binds through one carbon; an η³-allyl binds through all three carbons of the allyl system. A cyclopentadienyl ring is typically η⁵ (all five carbons bonded to the metal). Hapticity affects electron count — an η⁵-Cp donates 5 electrons while an η¹-Cp donates only 1. Changes in hapticity during reactions (ring slippage) can create or fill coordination vacancies, providing a mechanism for complexes to maintain (or approach) the 18-electron count throughout catalytic cycles.
