---
id: sigma-pi-bonds-and-orbitals
title: Sigma and Pi Bonds in Molecules
domain: chemistry
course: general-chemistry
prerequisites:
- id: covalent-bonding
  type: hard
builds-toward:
- hybridization-introduction
- alkene-structure-and-nomenclature
tags:
- bonding
- orbitals
- covalent
- molecular-structure
stage: formal-systems
status: draft
---

# Sigma and Pi Bonds in Molecules

## Core Idea
A sigma (σ) bond is formed by direct orbital overlap along the internuclear axis and allows free rotation. A pi (π) bond is formed by lateral overlap of p orbitals above and below the internuclear axis and restricts rotation. Double bonds consist of one σ and one π bond; triple bonds have one σ and two π bonds.

## Questions

```yaml
- question: "A chemist wants to convert the cis isomer of 2-butene to the trans isomer. She heats the molecule gently. Which bond must be disrupted for this interconversion to occur, and why?"
  type: multiple-choice
  options:
    - "The sigma (σ) bond of the C=C double bond — it locks the geometry by connecting the two carbons"
    - "The pi (π) bond of the C=C double bond — its lateral overlap is broken by rotation around the bond axis"
    - "The adjacent C–C single bonds — rotation there allows the double bond geometry to flip"
    - "No bond needs to break; thermal energy allows rotation around any bond at sufficient temperature"
  answer: 1
  explanation: "Cis-trans interconversion requires breaking the pi bond. The pi bond forms by lateral overlap of p orbitals above and below the internuclear axis; rotating around the bond axis would destroy this overlap, effectively breaking the pi bond (~250 kJ/mol). This is why geometric isomers around double bonds are stable, distinct compounds — they cannot interconvert without that energy input. The sigma bond's cylindrical symmetry allows free rotation in single bonds, which is why no cis/trans isomers exist around C–C single bonds."

- question: "A triple bond between two carbon atoms (as in acetylene, C≡C) consists of:"
  type: multiple-choice
  options:
    - "Three sigma bonds arranged at 120° angles around the internuclear axis"
    - "One sigma bond and two pi bonds, with the two pi bonds occupying perpendicular planes around the axis"
    - "Two sigma bonds and one pi bond, making the triple bond stronger than either alone"
    - "One sigma bond and two pi bonds, both pi bonds lying in the same plane"
  answer: 1
  explanation: "A triple bond always comprises one σ bond (head-on overlap along the axis) plus two π bonds (lateral p-orbital overlap). The two pi bonds are oriented in perpendicular planes — one above/below the molecular axis, one in front/behind — creating a cylindrical sheath of pi electron density around the sigma backbone. Students often assume three equivalent bonds or place both pi bonds in the same plane; neither is correct. The sigma bond is always present in every bond type, with pi bonds added on top."

- question: "Pi bonds are generally more reactive than sigma bonds because their electron density is exposed above and below the internuclear axis, making it accessible to attacking electrophiles."
  type: true-false
  answer: true
  explanation: "Correct. The lateral overlap of pi bonds places electron density in two lobes above and below the molecular plane, away from the shielding nuclei. This exposed electron density is far more accessible to incoming electrophiles than sigma electrons, which are concentrated along the axis between the two nuclei. This is why alkenes and alkynes undergo addition reactions at their double and triple bonds, and why pi bonds are the reactive sites in organic chemistry. The sigma bond underneath is more stable and less accessible."

- question: "A pi (π) bond is stronger than a sigma (σ) bond between the same two atoms, because pi bonds involve two lobes of orbital overlap while sigma bonds involve only one."
  type: true-false
  answer: false
  explanation: "Sigma bonds are stronger than individual pi bonds. Head-on overlap (sigma) is more effective than lateral overlap (pi) because the orbitals directly face each other along the internuclear axis, maximizing orbital overlap. The 'two lobes' of a pi bond represent one bond formed by parallel p orbitals, not two separate overlapping regions. The overall double bond is stronger than a single bond — because sigma + pi > sigma alone — but the pi component itself contributes less bond energy than the sigma component. This is confirmed by bond dissociation energies: breaking the pi bond of C=C costs ~260 kJ/mol; breaking the sigma requires ~350 kJ/mol."

- question: "Explain why cis and trans isomers can exist around a C=C double bond but not around a C–C single bond."
  type: short-answer
  answer: "The C=C double bond contains a pi bond formed by lateral p-orbital overlap above and below the internuclear axis. Rotation around the bond axis would destroy this lateral overlap, requiring ~250 kJ/mol — effectively breaking the pi bond. Because this energy barrier traps the molecule in one geometric arrangement, cis and trans forms are stable, distinct compounds that cannot interconvert at room temperature. A C–C single bond is only a sigma bond, whose cylindrical electron distribution is symmetric around the internuclear axis — rotation does not change the orbital overlap geometry, costs no significant energy, and is therefore free at room temperature."
  explanation: "The sigma bond's cylindrical symmetry is the key physical fact. Any rotation around a sigma bond leaves the electron cloud unchanged. The pi bond lacks this symmetry: its lobes are aligned only when the two atoms' p orbitals are parallel. Any deviation from planarity reduces overlap, and 90° rotation eliminates it entirely. This difference in rotational barriers is the structural basis for stereochemistry in organic molecules."
```

## Explainer

You already know from covalent bonding that atoms share electrons by overlapping their orbitals. The next step is recognizing that not all overlaps are equal — the geometry of how orbitals meet determines the bond's properties. A **sigma (σ) bond** forms when two orbitals overlap head-on, directly along the line connecting the two nuclei. Think of two people shaking hands — the contact point is right between them on a straight line. This head-on overlap produces a cylindrically symmetric electron cloud wrapped around the internuclear axis. Because that cloud is symmetric all the way around, one atom can rotate relative to the other without breaking the bond. Every single bond you have drawn so far is a sigma bond.

A **pi (π) bond** forms in a fundamentally different way. Instead of overlapping head-on, two p orbitals sit parallel to each other and overlap sideways — above and below the internuclear axis. Imagine holding two magnets side by side so their fields merge in the space between them, but not along the line connecting their centers. The resulting electron density exists in two lobes, one above and one below the bond axis, with a **node** (a plane of zero electron density) right along the axis itself. This geometry means that rotation around the bond would break the lateral overlap and destroy the pi bond, which is why double bonds are rigid and do not rotate freely.

When you see a **double bond** (like C=C in ethylene), it is not simply "two of the same bond." It is one sigma bond providing the structural backbone plus one pi bond layered on top, locking the molecule into a planar geometry. A **triple bond** (like C≡C in acetylene) takes this further: one sigma bond plus two pi bonds, with the two pi bonds oriented perpendicular to each other. The sigma bond is always stronger than an individual pi bond because head-on overlap is more effective than sideways overlap, but the combination of sigma plus pi makes double and triple bonds progressively shorter and stronger overall.

Understanding sigma and pi bonds is the key to predicting molecular geometry and reactivity. The rigidity of pi bonds explains why cis and trans isomers exist around double bonds — rotation cannot interconvert them without breaking the pi bond. It also explains why pi bonds are more reactive than sigma bonds: the electron density in a pi bond sits exposed above and below the molecular plane, making it accessible to electrophilic attack. This concept becomes central when you move into hybridization theory and the chemistry of alkenes and alkynes.
