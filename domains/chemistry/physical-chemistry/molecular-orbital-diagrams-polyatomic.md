---
id: molecular-orbital-diagrams-polyatomic
title: Molecular Orbital Diagrams for Polyatomic Molecules
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-diagrams
  type: hard
- id: molecular-geometry-basics
  type: hard
builds-toward:
- electron-correlation-approximations
- group-theory-molecular-symmetry
tags:
- orbital
- bonding
- polyatomic
- diagrams
stage: advanced
status: validated
---

# Molecular Orbital Diagrams for Polyatomic Molecules

## Core Idea
Polyatomic molecules require systematic approaches to construct molecular orbital diagrams by considering symmetry and orbital overlap among multiple atoms. Group theory simplifies this by classifying orbitals by symmetry type, revealing which atomic orbitals can combine. MO diagrams for polyatomics reveal bonding patterns, predict bond orders, and explain molecular properties like magnetism and reactivity.

## How It's Best Learned
Build diagrams progressively: first simple linear molecules (CO₂), then planar (BF₃, benzene), then tetrahedral (CH₄, SF₆). Use symmetry arguments to predict which orbital combinations are allowed. Compare predictions to experimental spectroscopic data.

## Common Misconceptions
- All p-orbitals on different atoms must combine (they don't if symmetry is wrong).
- Assuming heavier atoms always lower orbital energy (depends on overlap and electronegativity).

## Questions

```yaml
- question: "In the MO diagram for water (H₂O), oxygen's 2px orbital ends up as a nonbonding orbital. Why?"
  type: multiple-choice
  options:
    - "The 2px orbital has too high an energy to interact with hydrogen orbitals"
    - "No combination of the two hydrogen 1s orbitals has the same symmetry as oxygen's 2px, so no overlap is possible"
    - "The 2px orbital is fully occupied and cannot accept electrons from hydrogen"
    - "Oxygen's 2px is antibonding and its interaction with hydrogen is forbidden"
  answer: 1
  explanation: "The two hydrogen 1s orbitals can form only two combinations: in-phase (both positive) and out-of-phase (one positive, one negative). These two combinations have specific symmetry properties that match oxygen's 2s, 2pz, and 2py — but not 2px. Because no hydrogen combination shares the symmetry of 2px, there is no overlap integral between them, and 2px cannot mix into any bonding or antibonding MO. It remains as a pure nonbonding lone pair on oxygen. This is the central insight: symmetry mismatch, not energy mismatch, is what determines whether orbitals can combine."

- question: "For methane (CH₄) in the Td point group, the four hydrogen 1s orbitals form symmetry combinations labeled a₁ and t₂. Which carbon orbitals interact with each set?"
  type: multiple-choice
  options:
    - "Carbon 2s interacts with a₁; carbon 2p orbitals interact with t₂"
    - "Carbon 2s interacts with t₂; carbon 2p orbitals interact with a₁"
    - "All four carbon valence orbitals interact with the a₁ combination only"
    - "Carbon 2px, 2py, 2pz each interact with a separate hydrogen orbital individually"
  answer: 0
  explanation: "In the Td point group, carbon's 2s orbital has a₁ symmetry and therefore mixes only with the a₁ hydrogen combination. Carbon's three 2p orbitals (2px, 2py, 2pz together) form a triply degenerate t₂ set that mixes only with the t₂ hydrogen combinations. This produces two bonding/antibonding pairs: one a₁ pair and three degenerate t₂ pairs. Filling all four bonding MOs with 8 valence electrons accounts for methane's four equivalent C-H bonds. Option D represents a localized bonding picture (like Lewis structures) that MO theory replaces."

- question: "In polyatomic MO theory, the rule that orbitals of different symmetry representations cannot mix is a strict selection rule, not merely a preference."
  type: true-false
  answer: true
  explanation: "This is not a guideline — it is a rigorous mathematical result. The overlap integral between two orbitals belonging to different irreducible representations of the molecular point group is exactly zero by symmetry. This means there is no matrix element connecting them in the Hamiltonian, and they cannot mix regardless of how close in energy they are. The selection rule simplifies MO construction enormously: you only need to consider combinations within each symmetry representation separately, ignoring all cross-representation interactions."

- question: "All p-orbitals on different atoms in a polyatomic molecule will form bonding and antibonding MO combinations with each other."
  type: true-false
  answer: false
  explanation: "Orbital mixing requires matching symmetry, not just matching orbital type. A p-orbital on one atom will only combine with orbitals on other atoms that belong to the same symmetry representation under the molecule's point group. If the symmetry doesn't match, the overlap integral is zero and no MO combination forms — the orbital remains nonbonding. For example, in water, oxygen's 2px remains nonbonding because no hydrogen orbital combination has the same symmetry. The common misconception that all orbitals of the same type must combine comes from the diatomic case, where symmetry automatically matches."

- question: "Explain why MO theory for polyatomic molecules naturally handles resonance without needing multiple Lewis structures, using O₃ or benzene as an example."
  type: short-answer
  answer: "In MO theory, atomic orbitals from all atoms are combined simultaneously into molecular orbitals that are delocalized over the entire molecule. For O₃ or benzene, the π MOs extend over all atoms from the start — there is no single-bond/double-bond distinction at the MO level. The delocalization is built into the basis of the calculation, so there is no need to invoke multiple resonance contributors as a conceptual fix. The 'true structure' is just the electron density described by the filled MOs."
  explanation: "Lewis structures force electrons into localized bonds between pairs of atoms. When the actual electron distribution is delocalized, you need multiple resonance structures to hint at this. MO theory sidesteps this entirely by using a basis that allows electrons to occupy orbitals spanning multiple atoms. For benzene, the three π MOs (one bonding, two weakly bonding) are each spread over all six carbons — no bond is intrinsically single or double. The resonance-hybrid picture is an approximation that MO theory makes unnecessary. This is one reason MO theory is more powerful than Lewis/resonance descriptions for understanding reactivity, UV-Vis spectra, and magnetic properties."
```

## Explainer

From constructing MO diagrams for diatomic molecules, you learned to combine two sets of atomic orbitals — one from each atom — into bonding and antibonding molecular orbitals, fill them with electrons, and read off properties like bond order and magnetism. Polyatomic molecules follow the same logic, but with more atoms participating, the number of possible orbital combinations multiplies rapidly. The key to managing this complexity is **symmetry**: only atomic orbitals that share the same symmetry properties can combine into molecular orbitals.

Consider **water (H₂O)** as an introductory example. Oxygen sits at the center with its 2s and three 2p orbitals, and two hydrogen atoms each contribute a 1s orbital. Rather than trying all possible combinations, you ask: which hydrogen orbital combinations match the symmetry of each oxygen orbital? The two H 1s orbitals can be added in-phase (both positive) or out-of-phase (one positive, one negative). The in-phase combination has the same symmetry as oxygen's 2s and 2pz orbitals, so all three combine to form bonding, nonbonding, and antibonding MOs. The out-of-phase combination matches the symmetry of oxygen's 2py, producing another bonding-antibonding pair. Oxygen's 2px orbital has no hydrogen combination to interact with — it remains a **nonbonding orbital**, a lone pair that sits on oxygen without contributing to bonding. This symmetry-matching approach replaces guesswork with systematic construction.

For larger molecules, **group theory** formalizes the process. You assign the molecule to a point group (C₂v for water, D₃h for BF₃, Tₐ for CH₄), then classify every atomic orbital by its symmetry representation (labeled a₁, b₂, e, t₂, etc. depending on the point group). Orbitals that belong to the same representation can mix; orbitals in different representations cannot — this is a strict selection rule, not a preference. For **methane (CH₄)** in the Tₐ point group, the four H 1s orbitals form one combination of a₁ symmetry and three of t₂ symmetry. Carbon's 2s orbital is a₁ and mixes with the a₁ hydrogen combination; carbon's three 2p orbitals are t₂ and mix with the t₂ hydrogen set. The result is one bonding + one antibonding pair of a₁ symmetry, and three bonding + three antibonding orbitals of t₂ symmetry — eight MOs total from eight atomic orbital inputs. Filling with eight valence electrons (four from C, one from each H) gives four filled bonding orbitals, consistent with methane's four equivalent C–H bonds.

The power of polyatomic MO diagrams lies in what they reveal that simpler models miss. In **CO₂**, the MO diagram shows that the two C=O double bonds are not independent — they are described by delocalized molecular orbitals spanning all three atoms, with π orbitals that extend over the entire molecule. The diagram also predicts that CO₂ has filled bonding orbitals and empty antibonding orbitals with a large HOMO-LUMO gap, explaining its chemical stability and UV absorption properties. For molecules like **O₃** or **NO₂**, where Lewis structures require resonance, the MO diagram naturally produces delocalized orbitals without needing to invoke resonance as a separate concept — the delocalization is built into the orbital construction from the start.
