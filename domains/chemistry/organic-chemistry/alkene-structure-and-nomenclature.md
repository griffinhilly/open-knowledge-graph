---
id: alkene-structure-and-nomenclature
title: Alkene Structure, Nomenclature, and E/Z Isomerism
domain: chemistry
course: organic-chemistry
prerequisites:
- id: iupac-nomenclature-alkanes
  type: hard
- id: stereochemistry-intro
  type: hard
- id: sigma-pi-bonds-and-orbitals
  type: hard
builds-toward:
- alkyne-structure-and-nomenclature
- electrophilic-addition-to-alkenes
- aromatic-compounds-intro
tags:
- alkenes
- double bond
- E/Z
- geometric isomerism
- pi bond
- sp2
- Markovnikov
stage: formal-systems
status: validated
---

# Alkene Structure, Nomenclature, and E/Z Isomerism

## Core Idea
Alkenes contain at least one C=C double bond consisting of a sigma bond and a pi bond; the pi bond restricts rotation, locking the geometry around the double bond. This restricted rotation enables cis/trans geometric isomerism, more precisely described by the E/Z system using CIP priority rules: E (entgegen, 'opposite') when higher-priority groups are on opposite sides, Z (zusammen, 'together') when on the same side. Alkene carbons are sp2 hybridized with planar trigonal geometry. The electron-rich pi bond is the site of reactivity in nearly all alkene reactions.

## How It's Best Learned
Practice E/Z assignment starting with disubstituted alkenes, then tetrasubstituted. Confirm CIP rankings using explicit atomic-number comparisons. Connect the planar geometry to why cis/trans isomers have different physical properties.

## Common Misconceptions
- Cis/trans and E/Z are not interchangeable for trisubstituted alkenes; only E/Z is always unambiguous.
- The higher-priority group is assigned by CIP rules applied to the atom directly attached to the double-bond carbon, not by overall substituent size.
- The pi bond is weaker than the sigma bond (lower BDE), making it kinetically accessible to reagents without full C=C homolysis.

## Questions

```yaml
- question: "Why do geometric isomers (E/Z) of alkenes exist as stable, separate compounds at room temperature, unlike conformational isomers of alkanes?"
  type: multiple-choice
  options: ["The sp2 carbons are larger than sp3 carbons and cannot rotate", "Rotation around C=C would require breaking the pi bond, which has a significant energy barrier (~60 kcal/mol)", "Substituents on the double-bond carbons create steric strain that locks the geometry", "The sigma bond in alkenes is stronger than in alkanes, preventing rotation"]
  answer: 1
  explanation: "The pi bond is formed by sideways overlap of p orbitals perpendicular to the C-C axis. Rotation would twist one p orbital out of alignment with the other, breaking the overlap and effectively breaking the pi bond. The energy required (~60 kcal/mol) far exceeds available thermal energy at room temperature, so the two geometric isomers are permanently locked in their configurations and are distinct compounds with different physical properties."

- question: "For a trisubstituted alkene, the cis/trans naming system works just as well as E/Z because one can usually identify which groups are 'the same'."
  type: true-false
  answer: false
  explanation: "Cis/trans nomenclature requires that each double-bond carbon bears two different substituents AND that one substituent on each carbon is the same group (to define 'same side' vs 'opposite side'). For a trisubstituted alkene — where one carbon bears two different groups and the other bears one group and one hydrogen — there is no unambiguous 'same' group to reference. The E/Z system using CIP priority rules assigns priority to any two different substituents unambiguously and always gives a definite answer."

- question: "In CIP priority assignment for E/Z isomers, how do you determine which of two substituents attached to a double-bond carbon has higher priority?"
  type: short-answer
  answer: "Compare the atomic numbers of the atoms directly bonded to the double-bond carbon. The substituent whose first atom has the higher atomic number gets higher priority. If those atoms are the same element, move outward to the next set of attached atoms and compare again, repeating until a difference is found."
  explanation: "For example, -Br beats -Cl because Br (Z=35) > Cl (Z=17). A -CH2Br substituent beats -CH2Cl for the same reason at the second atom. The key mistake is ranking substituents by overall 'size' or molecular weight rather than following the CIP algorithm strictly from the point of attachment outward."
```

## Explainer

When you learned to name alkanes using IUPAC rules, carbon chains were flexible — single bonds allow free rotation, so an alkane can adopt countless conformations that interconvert freely at room temperature. Alkenes introduce a fundamental change in geometry: the C=C double bond consists of a sigma bond (end-on overlap, strong) and a pi bond (sideways overlap of adjacent p orbitals, weaker). That pi bond is the key to everything in alkene chemistry.

The p orbitals forming the pi bond must remain parallel for effective overlap. Rotating one carbon relative to the other would twist those orbitals out of alignment, breaking the pi bond — an energy cost of roughly 60 kcal/mol. This is far too large to overcome at room temperature. The consequence is that the two double-bond carbons are locked in a plane, and any substituents attached to them are frozen in space relative to each other. This is why cis-2-butene and trans-2-butene are two different compounds with different boiling points, not interconvertible conformations.

To name which isomer you have, chemists use the E/Z system based on CIP priority rules. For each double-bond carbon, you compare the two substituents using atomic number: the substituent whose first atom has the higher atomic number gets higher priority. If the higher-priority groups on each carbon are on the same side of the double bond, the isomer is Z (from German *zusammen*, "together"). If they are on opposite sides, it is E (*entgegen*, "opposite"). This system handles all cases — including trisubstituted alkenes where cis/trans is ambiguous — because CIP always produces a definite ranking as long as the two substituents on each carbon are different.

The sp2 hybridization of alkene carbons also determines the geometry around the double bond. Each sp2 carbon forms three bonds arranged at ~120° in a plane, with the remaining p orbital perpendicular to that plane. This means a double-bond carbon and all four atoms directly attached to it (two substituents plus the other alkene carbon) are coplanar. This planarity is exploited by the pi bond itself and has direct consequences for how reagents approach the alkene in reactions you will study next.

Finally, note that the pi bond is both the defining feature of alkene reactivity and the weaker of the two bonds in the C=C double bond. Bond dissociation energy data show the pi bond contributes roughly 60-65 kcal/mol on top of the sigma bond's ~90 kcal/mol. Reagents can selectively attack the pi bond without breaking the sigma bond — this is the basis of all electrophilic addition reactions. The electron-rich pi cloud acts as a nucleophile, attacking incoming electrophiles; the geometry of that pi system determines what faces are accessible and what stereochemical outcomes are possible.
