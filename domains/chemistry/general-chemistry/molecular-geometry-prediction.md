---
id: molecular-geometry-prediction
title: 'Molecular Geometry: VSEPR Theory and 3D Structure'
domain: chemistry
course: general-chemistry
prerequisites:
- id: lewis-structures
  type: hard
- id: 3d-coordinate-systems
  type: soft
builds-toward:
- polarity-and-dipole-moments
- intermolecular-forces
tags:
- VSEPR
- molecular geometry
- electron geometry
- 3D structure
stage: formal-systems
status: validated
---

# Molecular Geometry: VSEPR Theory and 3D Structure

## Core Idea
The Valence Shell Electron Pair Repulsion (VSEPR) theory predicts molecular shape based on the repulsion between electron pairs (bonding and lone pairs) around a central atom. Electron geometry describes all electron pairs; molecular geometry describes only atoms. Common shapes include linear, trigonal planar, tetrahedral, trigonal pyramidal, and bent.

## Questions

```yaml
- question: "Nitrogen in ammonia (NH₃) has 3 bonding pairs and 1 lone pair. A student predicts trigonal planar molecular geometry, reasoning that nitrogen forms 3 bonds. What is the student's error?"
  type: multiple-choice
  options:
    - "NH₃ should be tetrahedral because all four electron groups, including the lone pair, point to atom positions"
    - "The lone pair occupies one position of the tetrahedral electron geometry, making the molecular geometry trigonal pyramidal, not planar"
    - "Nitrogen's 3 bonds do produce trigonal planar geometry; the student's prediction is correct"
    - "Lone pairs do not count as electron groups in VSEPR theory, so the student should use only the 3 bonds"
  answer: 1
  explanation: "The student confused molecular geometry (where atoms are) with electron geometry (where all electron pairs are). NH₃ has 4 electron groups (3 bonds + 1 lone pair), giving tetrahedral electron geometry. But the molecular geometry describes only where the atoms are: the lone pair occupies one tetrahedral corner and is 'invisible,' so the 3 N–H bonds point to the other three corners, producing a trigonal pyramidal shape. Option 3 is the opposite error — lone pairs absolutely count as electron groups; ignoring them is precisely the mistake."

- question: "Water (H₂O) has an H–O–H bond angle of 104.5°, less than the ideal tetrahedral angle of 109.5°. What best explains this compression?"
  type: multiple-choice
  options:
    - "Oxygen's high electronegativity pulls bonding electrons toward itself, drawing the hydrogen atoms closer together"
    - "The two lone pairs exert greater repulsion on the bonding pairs than bonding pairs exert on each other, compressing the bond angle"
    - "Water has trigonal planar electron geometry with an ideal 120° angle, reduced by oxygen's electronegativity to 104.5°"
    - "The hydrogen atoms are too small to maintain 109.5° separation, so they fall closer together"
  answer: 1
  explanation: "Water has tetrahedral electron geometry (4 groups: 2 bonds + 2 lone pairs). Lone pairs are held closer to the central atom and spread out over a wider angular region than bonding pairs, exerting stronger repulsion on neighboring groups. The two lone pairs squeeze the two O–H bonds closer together, compressing the bond angle below the ideal 109.5°. Each additional lone pair adds more compression: NH₃ (1 lone pair) has 107°; H₂O (2 lone pairs) has 104.5°. Option 2 is wrong — water does not have trigonal planar electron geometry (which requires 3 electron groups, not 4)."

- question: "The electron geometry and molecular geometry of a molecule are always identical."
  type: true-false
  answer: false
  explanation: "They differ whenever the central atom has lone pairs. Electron geometry includes lone pairs in determining spatial arrangement; molecular geometry describes only where the atoms are. For example, NH₃ has tetrahedral electron geometry but trigonal pyramidal molecular geometry, and H₂O has tetrahedral electron geometry but bent molecular geometry. Electron and molecular geometry are the same only when all electron groups are bonding pairs (e.g., CH₄ is tetrahedral in both)."

- question: "A molecule with 4 electron groups and 1 lone pair on the central atom has trigonal pyramidal molecular geometry."
  type: true-false
  answer: true
  explanation: "Four electron groups give tetrahedral electron geometry (109.5° ideal angles). With 1 of those groups being a lone pair, only 3 groups are bonds to atoms. The three bonded atoms sit at three corners of the tetrahedron, with the lone pair occupying the fourth — producing a trigonal pyramidal molecular shape. NH₃ is the canonical example. This is distinct from trigonal planar geometry (3 electron groups, all bonding, 120° angles, no lone pair)."

- question: "What is the difference between electron geometry and molecular geometry? Use SF₄ (5 electron groups: 4 bonds and 1 lone pair) to illustrate why the distinction matters."
  type: short-answer
  answer: "Electron geometry describes the spatial arrangement of ALL electron groups around the central atom, including lone pairs. Molecular geometry describes only where the bonded atoms are, ignoring lone pairs. For SF₄, 5 electron groups give trigonal bipyramidal electron geometry. The lone pair preferentially occupies an equatorial position (less repulsion there), leaving 4 S–F bonds: 2 axial and 2 equatorial. This produces a 'see-saw' molecular geometry — not trigonal bipyramidal. Without the distinction, you would incorrectly predict a symmetric trigonal bipyramidal shape and make wrong predictions about polarity and reactivity."
  explanation: "The lone pair's position in SF₄ is not arbitrary — it occupies equatorial rather than axial because equatorial positions have fewer 90° interactions with other groups (which are the most repulsive). This preference for equatorial lone pairs is a specific application of VSEPR logic that is only visible once you distinguish electron from molecular geometry and think carefully about where repulsion is minimized."
```

## Explainer

From drawing Lewis structures, you know exactly how many bonding pairs and lone pairs surround each atom in a molecule. **VSEPR theory** takes that two-dimensional Lewis structure and predicts the three-dimensional arrangement of atoms by applying one simple principle: electron pairs around a central atom repel each other and arrange themselves as far apart as possible. This minimizes repulsion and determines the molecular shape.

The first step is counting the **electron groups** around the central atom — where an electron group is any region of electron density: a single bond, a double bond, a triple bond, or a lone pair. (Note that double and triple bonds count as one group each, because all the electrons in a multiple bond are concentrated in roughly the same direction.) Two electron groups arrange themselves 180° apart (**linear** electron geometry). Three groups spread to 120° (**trigonal planar**). Four groups adopt 109.5° angles (**tetrahedral**). Five and six groups produce **trigonal bipyramidal** and **octahedral** arrangements, respectively. These are the fundamental electron geometries, and they follow purely from maximizing the distance between repelling electron clouds.

The critical distinction is between **electron geometry** and **molecular geometry**. Electron geometry describes where all electron groups sit, including lone pairs. Molecular geometry describes only where the atoms are — because lone pairs are invisible to experimental structure-determination methods. This means the same electron geometry can produce different molecular shapes depending on how many of the groups are lone pairs versus bonding pairs. Four electron groups in a tetrahedral arrangement can yield three different molecular geometries: **tetrahedral** (zero lone pairs, like CH₄), **trigonal pyramidal** (one lone pair, like NH₃), or **bent** (two lone pairs, like H₂O). In each case the electron geometry is tetrahedral, but the molecular shape changes as lone pairs replace bonding pairs.

Lone pairs also compress bond angles slightly. Because lone pair electrons are held closer to the central atom and spread out more than bonding pairs, they exert greater repulsion on neighboring groups. This is why the H–N–H angle in ammonia (107°) is slightly less than the ideal tetrahedral 109.5°, and the H–O–H angle in water (104.5°) is smaller still — each lone pair squeezes the bonding pairs closer together. The practical workflow for any molecule is: draw the Lewis structure, count electron groups on the central atom, determine electron geometry, identify how many groups are lone pairs, and name the molecular geometry. With practice, this process becomes nearly automatic and gives you the three-dimensional picture you need to predict polarity, intermolecular forces, and chemical behavior.
