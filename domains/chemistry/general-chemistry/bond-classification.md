---
id: bond-classification
title: 'Classification of Bonds: Ionic, Covalent, and Metallic'
domain: chemistry
course: general-chemistry
prerequisites:
- id: ionic-bonding-formation
  type: hard
- id: covalent-bonding-formation
  type: hard
builds-toward:
- crystal-structures-and-properties
tags:
- bond classification
- metallic bonding
- electronegativity
stage: formal-systems
status: validated
---

# Classification of Bonds: Ionic, Covalent, and Metallic

## Core Idea
Bonds are classified based on electronegativity difference and electron behavior. Ionic bonds (Δ EN > 1.7) involve electron transfer; covalent bonds (Δ EN < 1.7) involve sharing; metallic bonds involve delocalized electrons in a lattice. This classification predicts compound properties like melting point, solubility, and conductivity.

## Questions

```yaml
- question: "Sodium chloride (NaCl) conducts electricity when dissolved in water but not in the solid state. Which explanation correctly follows from bond classification?"
  type: multiple-choice
  options:
    - "In solution, water molecules break ionic bonds and release free electrons that carry current; in the solid, no free electrons exist"
    - "In solution, the ions dissociate and become mobile, carrying charge; in the solid, ions are locked in the crystal lattice and cannot migrate"
    - "Water itself is a good conductor and carries the current on behalf of the dissolved salt"
    - "Ionic bonds break down at elevated temperatures like dissolution, releasing electrons"
  answer: 1
  explanation: "Electrical conductivity requires mobile charges. In solid NaCl, Na⁺ and Cl⁻ are locked in a rigid electrostatic lattice — they cannot migrate, so no current flows. Dissolving in water breaks the lattice, freeing the ions to move through the solution and carry charge. No free electrons are involved (options A and D are wrong — ionic conduction is via ion movement, not electrons). Water does not carry the current for the ions (option C). This prediction flows directly from ionic bond classification: ionic compounds conduct when ions are free to move."

- question: "Nitrogen trifluoride (NF₃) has a ΔEN of approximately 1.0. A student concludes it must have ionic bonds because 'the ΔEN is substantial.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Electronegativity differences don't apply to compounds involving fluorine"
    - "A ΔEN of 1.0 falls below the ~1.7 ionic threshold — it predicts polar covalent bonding where electrons are shared unequally, not transferred"
    - "NF₃ is a gas at room temperature, which proves it must be covalent regardless of ΔEN"
    - "Nitrogen and fluorine are both nonmetals, so they always form covalent bonds regardless of ΔEN"
  answer: 1
  explanation: "The student is confusing 'non-zero ΔEN' with 'ionic bonding.' The threshold for ionic character is roughly ΔEN > 1.7. At ΔEN = 1.0, bonding is polar covalent: fluorine pulls the shared electrons closer, creating partial charges (δ⁺ on N, δ⁻ on F), but the electrons are not fully transferred. Option D contains a useful heuristic but is not a principled explanation — the ΔEN framework is the correct approach, not element-type rules. The 1.7 threshold itself is a guideline, not a sharp boundary."

- question: "The boundary between ionic and covalent bonding is sharp: a bond is either ionic or covalent, never intermediate."
  type: true-false
  answer: false
  explanation: "Bonding is a continuous spectrum based on ΔEN, not three discrete categories. The 1.7 threshold is a guideline, not a sharp boundary. Real bonds near this value have partial ionic and partial covalent character — HCl, for example, has polar covalent bonding with measurable partial charges but is not fully ionic. As ΔEN increases from 0 (pure covalent, like H₂) toward large values (approaching pure ionic, like CsF at ΔEN ≈ 3.2), bonding character transitions gradually. The spectrum model is more accurate than a three-bin classification."

- question: "Metals conduct electricity in the solid state because their atoms share localized electron pairs in covalent bonds, and those bonded electrons can move when a voltage is applied."
  type: true-false
  answer: false
  explanation: "Metallic bonding is not localized electron-pair sharing — that is covalent bonding. In metallic bonding, valence electrons are delocalized across the entire lattice, forming a 'sea' of electrons not associated with any particular atom. These delocalized electrons move freely under an applied voltage, producing conductivity. Covalent compounds (diamond, plastic) do not conduct precisely because their electrons are localized in bonds and cannot migrate. The delocalized electron model explains not just conductivity but also malleability (ion layers can slide without breaking the electron sea) and metallic luster."

- question: "Explain how identifying a compound's bond type (ionic, covalent, or metallic) allows you to predict its macroscopic properties without memorizing each compound individually."
  type: short-answer
  answer: "Bond type reflects how electrons are distributed: transferred (ionic), shared between specific atoms (covalent), or delocalized across a lattice (metallic). Each electron arrangement produces predictable macroscopic consequences. Ionic compounds form rigid lattices with high melting points and conduct when ions become mobile. Covalent compounds form discrete molecules with weak intermolecular forces (lower melting points) and no free charges. Metals conduct in the solid state due to their electron sea and are malleable because cation layers can slide without disrupting delocalized bonding."
  explanation: "This predictive power is the central payoff of bond classification. A new compound can be characterized by its ΔEN, its bonding type identified, and its properties predicted without memorization. The logic runs from electron behavior (how electrons are distributed) to atomic-scale structure (lattice vs. molecule vs. metallic array) to macroscopic properties (melting point, conductivity, solubility, malleability). Each step follows from the previous one. This is why bond classification is taught as a framework rather than a list — the framework generates the properties rather than requiring them to be individually memorized."
```

## Explainer

You have already studied how ionic bonds form through electron transfer and how covalent bonds form through electron sharing. The classification of bonds brings these two models together with a third — metallic bonding — and reveals that these are not three completely separate phenomena but rather points along a continuous spectrum determined by how atoms share or distribute their electrons.

The key variable is **electronegativity difference (ΔEN)** between the bonded atoms. When ΔEN is large (roughly above 1.7), one atom pulls electrons so strongly that they effectively transfer completely, creating oppositely charged ions held together by electrostatic attraction — an **ionic bond**. Sodium chloride is the classic example: sodium (EN ≈ 0.9) and chlorine (EN ≈ 3.2) differ by 2.3, so sodium gives up its valence electron entirely. When ΔEN is small (below about 1.7), neither atom dominates, and electrons are shared between the nuclei — a **covalent bond**. The sharing may be equal (as in H₂ or Cl₂, where ΔEN = 0) or unequal (as in H–Cl, where chlorine pulls the shared pair closer, creating a polar covalent bond). The 1.7 threshold is a guideline, not a sharp boundary — bonding character transitions gradually from purely covalent to purely ionic.

**Metallic bonding** represents a third arrangement that appears when atoms of low electronegativity pack together. Instead of transferring electrons to a partner or sharing them in localized pairs, metal atoms release their valence electrons into a communal "sea" that pervades the entire lattice. Each metal cation sits in a regular array, surrounded by freely mobile electrons that belong to no single atom. This delocalized electron model explains why metals conduct electricity (electrons move freely), are malleable (layers of cations can slide without breaking bonds), and have luster (free electrons absorb and re-emit light across the visible spectrum).

The real power of bond classification is its predictive reach. Once you identify the bond type, you can anticipate macroscopic properties without memorizing them individually. Ionic compounds form crystalline lattices with high melting points because every ion is locked in place by strong electrostatic forces in all directions; they dissolve in polar solvents and conduct electricity when melted or dissolved because the ions become free to move. Covalent compounds form discrete molecules with lower melting points because the forces between molecules (intermolecular forces) are much weaker than the bonds within them; they are often poor conductors because they have no free charges. Metals conduct in the solid state, are ductile, and have moderate to high melting points depending on how many electrons each atom contributes to the sea. Recognizing that these property patterns flow directly from electron behavior — transferred, shared, or delocalized — is the central insight of bond classification.
