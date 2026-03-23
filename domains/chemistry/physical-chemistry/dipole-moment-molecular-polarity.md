---
id: dipole-moment-molecular-polarity
title: Dipole Moment and Molecular Polarity
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-geometry-basics
  type: hard
- id: electronegativity-and-bond-polarity
  type: hard
builds-toward:
- intermolecular-lennard-jones-potential
tags:
- dipole
- polarity
- moment
- molecular
stage: advanced
status: validated
---

# Dipole Moment and Molecular Polarity

## Core Idea
Dipole moment μ measures charge separation in a molecule (μ = q·r) and determines polarity and reactivity. Individual bond dipoles add vectorially; molecular geometry determines whether bond dipoles cancel (nonpolar) or sum (polar). Dipole moments can be calculated from electronegativity differences or measured spectroscopically. Molecular polarity predicts solubility, boiling point, reactivity, and intermolecular interactions.

## Questions

```yaml
- question: "CO₂ has two highly polar C=O bonds, yet its measured dipole moment is zero. What best explains this?"
  type: multiple-choice
  options:
    - "Carbon and oxygen have nearly the same electronegativity, so the C=O bond dipoles are negligible"
    - "The linear geometry causes the two bond dipole vectors to point in exactly opposite directions and cancel"
    - "An even number of identical bonds always cancels, regardless of geometry"
    - "CO₂ is an ionic compound, so the concept of bond dipoles does not apply"
  answer: 1
  explanation: "Each C=O bond is highly polar (O is much more electronegative than C), so both bond dipoles are large. The reason they cancel is geometry: CO₂ is linear, so the two dipole vectors point in exactly opposite directions and sum to zero. If CO₂ were bent like H₂O, the dipoles would add constructively and CO₂ would be polar. This illustrates the core principle: molecular polarity depends on the vector sum of bond dipoles, which is determined by geometry, not just bond polarity."

- question: "A student argues that CCl₄ must be polar because Cl is much more electronegative than C, making each C–Cl bond highly polar. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — CCl₄ is indeed polar because all four bonds are polar"
    - "The student is correct about the bonds but ignores that the tetrahedral geometry causes all four bond dipole vectors to cancel, giving a net dipole of zero"
    - "The student is wrong because C–Cl bonds are actually nonpolar"
    - "The student confuses ionic character with polarity"
  answer: 1
  explanation: "The student correctly identifies that each C–Cl bond is polar. The error is ignoring geometry. In tetrahedral CCl₄, the four identical C–Cl bond dipoles point symmetrically outward from the central carbon; their vector sum is exactly zero. Replace one Cl with H (giving CHCl₃) and the symmetry breaks — now the dipoles no longer cancel and the molecule is polar. This is the classic illustration that polar bonds do not guarantee a polar molecule."

- question: "A molecule can have polar bonds and still have a net dipole moment of zero."
  type: true-false
  answer: true
  explanation: "This is true, and CO₂ and CCl₄ are the canonical examples. CO₂ has two very polar C=O bonds that cancel because of linear geometry; CCl₄ has four polar C–Cl bonds that cancel because of tetrahedral symmetry. Polarity requires both polar bonds AND an asymmetric arrangement of those bonds such that the vectors do not cancel."

- question: "The molecule with the largest individual bond dipoles will always have the largest molecular dipole moment."
  type: true-false
  answer: false
  explanation: "This is false. Molecular dipole moment is the vector sum of all bond dipoles. A molecule with very large bond dipoles arranged symmetrically (like CCl₄, which has a dipole of 0 D) can have a smaller net dipole than a molecule with smaller but asymmetrically arranged bond dipoles. Geometry — not bond dipole magnitude alone — determines the net result."

- question: "Why does water (H₂O) have a large net dipole moment while carbon dioxide (CO₂) has zero, even though both molecules contain polar bonds?"
  type: short-answer
  answer: "The difference is molecular geometry. Water has a bent geometry (~104.5°), so its two O–H bond dipoles point in directions that partially reinforce each other; their vector sum gives a net molecular dipole of 1.85 D. CO₂ is linear, so its two C=O bond dipoles point in exactly opposite directions and cancel perfectly to zero. The lone pairs on oxygen in water also contribute a dipole component that reinforces the bond dipoles. Same principle applies generally: symmetric geometries cancel bond dipoles; asymmetric geometries produce a net dipole."
  explanation: "The key is vector addition of bond dipoles. In H₂O, the 104.5° angle means the two O–H dipoles are not antiparallel, so they do not cancel. In CO₂, the 180° linear geometry means they are exactly antiparallel and do cancel. Lone pairs add an additional contribution in H₂O, further increasing the dipole. Geometry is the deciding factor."
```

## Explainer

You already know from electronegativity and bond polarity that when two atoms with different electronegativities share a bond, the electron density shifts toward the more electronegative atom, creating a **bond dipole** — a separation of partial positive (δ+) and partial negative (δ−) charges. The **dipole moment** quantifies this: μ = q × d, where q is the magnitude of the separated charge and d is the distance between the charge centers. The unit is the **debye** (D), where 1 D = 3.336 × 10⁻³⁰ C·m. A larger electronegativity difference or a longer bond gives a larger bond dipole.

The crucial insight is that molecular polarity depends on **geometry**, not just on individual bond dipoles. Each bond dipole is a vector — it has both magnitude and direction — and the **molecular dipole moment** is the vector sum of all bond dipoles. This is why CO₂ is nonpolar despite having two very polar C=O bonds: the molecule is linear, so the two bond dipoles point in exactly opposite directions and cancel to zero. Water, by contrast, has a bent geometry (~104.5°), so its two O–H bond dipoles add constructively to produce a net dipole moment of 1.85 D. The same principle applies to more complex molecules: CCl₄ (tetrahedral, four identical C–Cl dipoles) is nonpolar because the vectors cancel; CHCl₃ is polar because replacing one Cl with H breaks the symmetry.

To predict molecular polarity, start from your knowledge of molecular geometry (VSEPR). Draw the structure, assign bond dipoles based on electronegativity differences, and then add the vectors. Highly symmetric molecules (linear with identical bonds, trigonal planar like BF₃, tetrahedral like CH₄ or CCl₄) will be nonpolar regardless of individual bond polarity. Any asymmetry — different substituents, lone pairs that distort geometry — generally produces a net dipole. Lone pairs contribute their own dipole component pointing away from the nucleus, which is why NF₃ (μ = 0.23 D) has a much smaller dipole than NH₃ (μ = 1.47 D): in NH₃ the lone pair dipole reinforces the N–H bond dipoles, while in NF₃ the lone pair dipole opposes the N–F bond dipoles.

Molecular polarity has far-reaching consequences. Polar molecules experience **dipole-dipole interactions** that raise boiling points relative to nonpolar molecules of similar size. They dissolve preferentially in polar solvents ("like dissolves like"). In spectroscopy, only molecules with a permanent dipole moment absorb in the microwave region (pure rotational spectroscopy), and dipole moment changes during vibration determine infrared absorption intensities. In chemical reactivity, the dipole moment reveals where electron density is concentrated, guiding predictions about nucleophilic and electrophilic sites.
