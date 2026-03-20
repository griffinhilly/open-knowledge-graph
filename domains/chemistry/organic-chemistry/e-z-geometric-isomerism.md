---
id: e-z-geometric-isomerism
title: E/Z Nomenclature and Geometric Isomerism
domain: chemistry
course: organic-chemistry
prerequisites:
- id: alkene-structure-and-nomenclature
  type: hard
- id: covalent-bonding
  type: soft
builds-toward:
- r-s-stereochemical-designation
tags:
- nomenclature
- isomerism
- double-bond
- priority-rules
- cahn-ingold-prelog
stage: advanced
status: draft
---

# E/Z Nomenclature and Geometric Isomerism

## Core Idea
Alkene double bonds cannot rotate freely, creating distinct geometric isomers (cis/trans in simple cases, E/Z in general). The E/Z system uses Cahn-Ingold-Prelog priority rules: higher atomic number atoms get priority 1; at each sp² carbon, the two highest-priority groups determine E (opposite sides) or Z (same side). Unlike cis/trans, E/Z applies regardless of group complexity.

## Explainer

From your study of alkene structure, you know that a carbon-carbon double bond consists of one σ bond and one π bond, and that the π bond locks the two carbons into a planar arrangement. Unlike single bonds, which allow free rotation, double bonds require roughly 260 kJ/mol to break the π bond and rotate — far more energy than is available at room temperature. This rigidity means that the groups attached to each end of the double bond are frozen in place, creating the possibility of distinct **geometric isomers**: two molecules with the same connectivity but different spatial arrangements of substituents around the double bond.

The older **cis/trans** naming convention works for simple cases. If the two "same" groups are on the same side of the double bond, the isomer is cis; if on opposite sides, it is trans. But this system breaks down when all four substituents on the double bond are different — there is no obvious "same group" to compare. The **E/Z system** solves this by using the **Cahn-Ingold-Prelog (CIP) priority rules** to rank substituents. At each sp² carbon of the double bond, you compare the two attached groups: the atom directly bonded to the double-bond carbon with the higher atomic number gets higher priority. If two atoms are identical, you move outward to the next set of atoms until a difference is found.

Once you have assigned priorities at both carbons, the naming is straightforward. If the two higher-priority groups are on the **same side** (zusammen in German), the isomer is **Z**. If they are on **opposite sides** (entgegen), it is **E**. A helpful mnemonic: Z = same side (think "zee zame zide"), E = opposite. Note that Z does not always correspond to cis, and E does not always correspond to trans — the CIP priority ranking may differ from an intuitive "same group" comparison, especially with complex substituents.

These geometric isomers are not just naming exercises — they are genuinely different compounds with different physical and chemical properties. Z and E isomers have different melting points, boiling points, dipole moments, and reactivities. For example, Z-but-2-ene has a slightly higher dipole moment than E-but-2-ene because the methyl groups on the same side create a net molecular dipole, while in the E isomer the symmetry partially cancels it out. In pharmaceutical chemistry, the wrong geometric isomer of a drug can be inactive or even harmful. Mastering E/Z assignment is also preparation for the R/S system at tetrahedral stereocenters, which uses the same CIP priority rules in three dimensions.
