---
id: covalent-bonding-formation
title: 'Covalent Bonding: Electron Sharing and Bond Types'
domain: chemistry
course: general-chemistry
prerequisites:
- id: periodic-trends-and-properties
  type: hard
builds-toward:
- lewis-structures-basics
- polarity-and-dipole-moments
tags:
- covalent bonding
- electron sharing
- polar covalent
- nonpolar covalent
stage: formal-systems
status: validated
---

# Covalent Bonding: Electron Sharing and Bond Types

## Core Idea
Covalent bonds form when atoms share electrons to fill their valence shells. Bonds can be nonpolar (equal sharing between identical atoms) or polar (unequal sharing based on electronegativity difference). Multiple bonds (double, triple) occur when atoms share more than one pair of electrons. Bond strength depends on both bond type and atomic size.

## Questions

```yaml
- question: "In an H–F bond, the electron density is shifted toward fluorine, giving fluorine a partial negative charge. What property of fluorine is responsible for this unequal sharing?"
  type: multiple-choice
  options:
    - "Fluorine has more protons, making it a larger atom that can hold more electrons"
    - "Fluorine has higher electronegativity, pulling the shared electrons closer to its nucleus"
    - "Fluorine forms a double bond with hydrogen, placing more electron density on its side"
    - "Hydrogen has a lower ionization energy, so it releases its electron to fluorine more readily"
  answer: 1
  explanation: "Electronegativity is the key periodic property: it measures how strongly an atom attracts shared electrons toward itself in a bond. Fluorine is the most electronegative element, so in H–F the shared pair is displaced toward fluorine, creating a bond dipole (δ+ on H, δ− on F). The bond is covalent — the electron pair is shared, not transferred — but the sharing is unequal. Fluorine's smaller atomic size (top of Group 17) also contributes: smaller atoms have higher electronegativity because the shared electrons are closer to the nucleus and feel its pull more strongly."

- question: "A C≡C triple bond (~837 kJ/mol) is much stronger than a C–C single bond (~348 kJ/mol), but is not exactly three times as strong. Why not?"
  type: multiple-choice
  options:
    - "Triple bonds involve weaker pi orbitals that partially cancel the sigma bond's strength"
    - "The second and third electron pairs in a multiple bond occupy less favorable bonding regions than the first pair, so each additional pair contributes less than the first"
    - "Carbon atoms are too small to support three bond pairs at the same internuclear distance"
    - "Multiple bonds introduce electron-electron repulsion that cancels a fixed amount of bonding energy"
  answer: 1
  explanation: "The first shared pair in a bond is a sigma bond — electron density concentrated directly between the two nuclei, in the most favorable bonding region. Additional pairs must form pi bonds, which place electron density above and below the bond axis rather than directly between the nuclei. Pi electrons are less tightly held by both nuclei, so each additional pair contributes less bonding energy than the first. The result is a sublinear scaling: double bonds are stronger than single bonds (but less than 2×), and triple bonds are stronger than double bonds (but less than 1.5× the double bond strength)."

- question: "Whether a bond is classified as nonpolar covalent, polar covalent, or ionic depends on the electronegativity difference between the atoms — these are positions on a continuous spectrum, not discrete categories."
  type: true-false
  answer: true
  explanation: "This is one of the most important conceptual corrections in bonding theory. There is no sharp boundary between polar covalent and ionic: as electronegativity difference increases, the shared electrons are pulled more and more unequally until, in the extreme case, the electron is essentially fully transferred (ionic). In practice, 'ionic' bonds in real compounds still have partial covalent character. The spectrum is: nonpolar covalent (identical atoms, Δχ = 0) → polar covalent (moderate Δχ) → predominantly ionic (large Δχ). The traditional cutoffs (Δχ > 1.7 = ionic) are useful rules of thumb, not fundamental distinctions."

- question: "In a covalent bond, each atom contributes electrons to the bond, but those electrons remain localized on their original atom — they are only 'shared' in the sense that both atoms benefit from proximity to the other."
  type: true-false
  answer: false
  explanation: "Shared electrons in a covalent bond are genuinely delocalized between both nuclei — they cannot be assigned to one atom. The bond forms precisely because the electrons in the shared region are simultaneously attracted to both positive nuclei, lowering the system's energy compared to two separate atoms. This mutual attraction is the source of bond strength. The electrons do not 'belong' to either atom; they occupy a molecular orbital that spans both. This is fundamentally different from ionic bonding, where one electron is transferred and does reside on one atom."

- question: "Why do atoms with high electronegativities tend to form covalent bonds with each other rather than ionic bonds?"
  type: short-answer
  answer: "Ionic bonding requires one atom to give up an electron (becoming a cation) and another to accept it (becoming an anion). Atoms with high electronegativity have strong tendencies to attract electrons toward themselves — not to release them. When two high-electronegativity atoms meet, neither is willing to donate electrons to the other; both want to pull electrons in. The result is a compromise: they share the electrons, with both atoms holding on and neither fully surrendering the shared pair. This is covalent bonding. Ionic bonding typically requires one low-electronegativity atom (which readily loses electrons to become a cation) and one high-electronegativity atom (which accepts them to become an anion)."
  explanation: "The periodic table reflects this: ionic compounds typically involve metals (low electronegativity, lower ionization energy) bonded to nonmetals (high electronegativity, high electron affinity). Nonmetal–nonmetal combinations — like H₂O, CO₂, or CH₄ — are covalent because both partners want to hold their electrons. The electronegativity difference between the bonding partners, not the absolute electronegativity of either alone, determines the bond type."
```

## Explainer

From your study of periodic trends, you know that atoms on the right side of the periodic table have high electronegativities and need only a few electrons to complete their valence shells. These atoms — carbon, nitrogen, oxygen, fluorine, and their neighbors — are unlikely to give up electrons entirely to form cations. Instead, when two such atoms come together, they reach stability by **sharing** electron pairs rather than transferring them. This mutual sharing is a **covalent bond**, and it is the dominant bonding mode in molecular compounds, from water to DNA.

Consider the simplest case: two hydrogen atoms approaching each other. Each has one electron and needs two for a filled 1s shell. When they share their electrons, both atoms simultaneously "see" two electrons in the space between the nuclei. This shared pair is attracted to both positive nuclei at once, pulling the atoms together. The distance where the attractive and repulsive forces balance is the **bond length**, and the energy you would need to pull the atoms apart is the **bond energy**. A single shared pair makes a **single bond**. When atoms need to share more electrons — as in O₂ or N₂ — they form **double bonds** (two shared pairs) or **triple bonds** (three shared pairs), which are progressively shorter and stronger.

Not all sharing is equal. When two identical atoms bond — H₂, Cl₂, O₂ — each atom pulls on the shared electrons with equal force, producing a **nonpolar covalent bond** with electron density distributed symmetrically. But when atoms with different electronegativities bond, the more electronegative atom pulls the electron density toward itself. In H–Cl, chlorine's higher electronegativity draws the shared pair closer, creating a **polar covalent bond** with partial charges: δ+ on hydrogen, δ− on chlorine. The degree of polarity depends on the electronegativity difference — a small difference gives a slightly polar bond, while a very large difference approaches ionic character. This continuum from nonpolar covalent to polar covalent to ionic is not three separate categories but a smooth spectrum determined by the periodic properties you already understand.

Bond strength follows predictable patterns rooted in the periodic table. Bonds between small atoms are stronger than bonds between large atoms because the shared electrons are closer to both nuclei and held more tightly. A C–C single bond (~348 kJ/mol) is stronger than a Si–Si bond (~226 kJ/mol) for exactly this reason. Multiple bonds between the same pair of atoms are stronger than single bonds — the C≡C triple bond (~837 kJ/mol) is much stronger than C=C (~614 kJ/mol) or C–C — though not simply three times as strong, because the second and third pairs occupy less favorable bonding regions. These bond energies matter because they determine which reactions are energetically favorable: breaking strong bonds requires energy input, and forming them releases energy.
