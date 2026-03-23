---
id: coordination-chemistry-basics
title: 'Coordination Chemistry: Complexes and Ligands'
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding
  type: soft
- id: covalent-bonding
  type: soft
builds-toward:
- complex-ions-stability
- complexometric-titration
tags:
- coordination chemistry
- ligands
- complex ions
stage: formal-systems
status: draft
---

# Coordination Chemistry: Complexes and Ligands

## Core Idea
Coordination complexes form when a central metal ion bonds with electron-donating ligands. Ligands donate electron pairs to the metal, forming coordinate covalent bonds. Complex ions have characteristic charges and geometries.

## Questions

```yaml
- question: "What distinguishes a coordinate covalent (dative) bond from an ordinary covalent bond?"
  type: multiple-choice
  options:
    - "A coordinate covalent bond is weaker than an ordinary covalent bond and can be broken at room temperature"
    - "Both electrons in the shared pair originate from the same atom (the ligand), while in an ordinary covalent bond each atom contributes one electron"
    - "Coordinate covalent bonds only form between metals, while ordinary covalent bonds form between nonmetals"
    - "A coordinate covalent bond involves electron transfer from the ligand to the metal, making it similar to an ionic bond"
  answer: 1
  explanation: "In an ordinary covalent bond, each atom donates one electron to form the shared pair. In a coordinate covalent (dative) bond, both electrons come from the same atom — the ligand, which acts as a Lewis base (electron pair donor). The metal ion, with empty d-orbitals, acts as the Lewis acid (electron pair acceptor). Once formed, the bond is indistinguishable from an ordinary covalent bond in terms of strength and properties — the distinction is only in origin. Option D describes ionic bonding (electron transfer), not electron sharing."

- question: "Why does ethylenediamine (en), a bidentate ligand, form more stable complexes with a metal ion than two separate ammonia (NH₃) molecules providing the same number of donor atoms?"
  type: multiple-choice
  options:
    - "Ethylenediamine donates more electron density per donor atom than ammonia"
    - "The geometric arrangement of ethylenediamine matches the metal's preferred orbital geometry better than ammonia"
    - "Detaching ethylenediamine requires breaking two metal-ligand bonds simultaneously, making dissociation much less favorable than losing a single monodentate ligand"
    - "Ethylenediamine forms hydrogen bonds with the metal that ammonia cannot"
  answer: 2
  explanation: "This is the chelate effect. A monodentate ligand can detach from a metal by breaking one bond — a process that becomes increasingly favorable through entropy as ligands dissociate. A bidentate ligand requires both donor atoms to detach simultaneously; since the first arm is still bound, the effective local concentration of the second arm is very high, driving re-attachment. Breaking both bonds simultaneously is far less probable than breaking one. This makes chelating ligands kinetically and thermodynamically more stable than equivalent monodentate ligands."

- question: "The overall charge of a coordination complex equals the sum of the charge of the central metal ion and the combined charges of all its ligands."
  type: true-false
  answer: true
  explanation: "The charge of a coordination complex is additive: add the metal's oxidation state charge to the total charge of all coordinated ligands. For [Cu(NH₃)₄]²⁺: Cu²⁺ (+2) plus four neutral NH₃ ligands (0 each) = +2. For [Fe(CN)₆]⁴⁻: Fe²⁺ (+2) plus six CN⁻ ligands (−6 total) = −4. This calculation is fundamental to naming coordination compounds and predicting their behavior in solution."

- question: "In a coordinate covalent bond between a ligand and a metal ion, the metal ion donates electrons into an empty orbital on the ligand."
  type: true-false
  answer: false
  explanation: "This reverses the direction of electron donation. In a coordinate covalent bond, the ligand (Lewis base) donates a lone pair of electrons into an empty orbital on the metal ion (Lewis acid). The metal ion is the electron pair acceptor, not the donor. This is consistent with why metal ions in coordination complexes are Lewis acids — their empty d-orbitals make them electron-deficient and receptive to lone pair donation from ligands like NH₃, H₂O, Cl⁻, and CN⁻."

- question: "Explain why EDTA is used medically to treat heavy metal poisoning. What property makes it so effective at removing metal ions from the body, and how does this relate to the chelate effect?"
  type: short-answer
  answer: "EDTA is a hexadentate ligand — it has six donor atoms (two nitrogen and four oxygen) that simultaneously coordinate to a metal ion, forming an extraordinarily stable octahedral complex. Because detaching EDTA requires breaking all six metal-ligand bonds at once, the complex is thermodynamically and kinetically very stable — far more so than any combination of six monodentate ligands. When administered, EDTA binds tightly to toxic metal ions (lead, mercury, arsenic) in the bloodstream, forming stable, water-soluble complexes that are excreted through the kidneys, removing the metal from the body before it can cause further damage."
  explanation: "The chelate effect scales with the number of donor atoms: bidentate ligands are more stable than monodentate, and hexadentate EDTA forms among the most stable complexes known for many metals. This is why EDTA is also used industrially as a water softener (chelating calcium and magnesium ions) and in food preservation (chelating metal ions that would catalyze oxidation)."
```

## Explainer

From your study of ionic and covalent bonding, you know that atoms can transfer electrons (ionic) or share them (covalent). Coordination chemistry introduces a third variation: the **coordinate covalent bond** (also called a dative bond), where both electrons in the shared pair come from the same atom. This happens when a metal ion with empty orbitals meets a molecule or ion that has a lone pair to donate. The metal is a Lewis acid (electron pair acceptor), and the donor species is a Lewis base — called a **ligand** in coordination chemistry.

A **coordination complex** consists of a central metal ion surrounded by ligands. Consider the deep blue complex formed when ammonia is added to a solution of copper(II) sulfate: four NH₃ molecules each donate their lone pair to Cu²⁺, forming [Cu(NH₃)₄]²⁺. The metal ion is the center, the ligands are the attachments, and the whole assembly carries a charge equal to the metal's charge plus the charges of all ligands. The number of bonds from ligands to the metal is called the **coordination number** — copper in this example has a coordination number of 4. Common coordination numbers are 2, 4, and 6, with 6 being the most frequent for transition metals.

Ligands come in different varieties based on how many donor atoms they have. **Monodentate** ligands like NH₃, Cl⁻, and H₂O donate through a single atom. **Bidentate** ligands like ethylenediamine (en) have two donor atoms and grip the metal at two points, like a crab's claw — this is why multi-donor ligands are called **chelating** agents (from the Greek word for claw). Chelating ligands form more stable complexes than comparable monodentate ligands because detaching requires breaking multiple bonds simultaneously, an effect known as the **chelate effect**. EDTA, with six donor atoms, is a powerful chelating agent used in everything from water softening to medical treatment of heavy metal poisoning.

The geometry of a coordination complex depends on its coordination number: two ligands typically give a linear arrangement, four can give either tetrahedral or square planar geometry, and six ligands arrange octahedrally. These geometries determine the complex's physical properties — its color, magnetic behavior, and reactivity. The vivid colors of transition metal complexes (the green of chromium(III), the purple of permanganate, the blue of copper-ammonia) arise because d-electrons absorb specific wavelengths of visible light, and the energy gap between d-orbitals depends on the geometry and the identity of the ligands. This is why adding different ligands to the same metal ion can produce dramatically different colors.
