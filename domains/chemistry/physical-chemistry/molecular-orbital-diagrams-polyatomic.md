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
status: draft
---

# Molecular Orbital Diagrams for Polyatomic Molecules

## Core Idea
Polyatomic molecules require systematic approaches to construct molecular orbital diagrams by considering symmetry and orbital overlap among multiple atoms. Group theory simplifies this by classifying orbitals by symmetry type, revealing which atomic orbitals can combine. MO diagrams for polyatomics reveal bonding patterns, predict bond orders, and explain molecular properties like magnetism and reactivity.

## How It's Best Learned
Build diagrams progressively: first simple linear molecules (CO₂), then planar (BF₃, benzene), then tetrahedral (CH₄, SF₆). Use symmetry arguments to predict which orbital combinations are allowed. Compare predictions to experimental spectroscopic data.

## Common Misconceptions
- All p-orbitals on different atoms must combine (they don't if symmetry is wrong).
- Assuming heavier atoms always lower orbital energy (depends on overlap and electronegativity).

## Explainer

From constructing MO diagrams for diatomic molecules, you learned to combine two sets of atomic orbitals — one from each atom — into bonding and antibonding molecular orbitals, fill them with electrons, and read off properties like bond order and magnetism. Polyatomic molecules follow the same logic, but with more atoms participating, the number of possible orbital combinations multiplies rapidly. The key to managing this complexity is **symmetry**: only atomic orbitals that share the same symmetry properties can combine into molecular orbitals.

Consider **water (H₂O)** as an introductory example. Oxygen sits at the center with its 2s and three 2p orbitals, and two hydrogen atoms each contribute a 1s orbital. Rather than trying all possible combinations, you ask: which hydrogen orbital combinations match the symmetry of each oxygen orbital? The two H 1s orbitals can be added in-phase (both positive) or out-of-phase (one positive, one negative). The in-phase combination has the same symmetry as oxygen's 2s and 2pz orbitals, so all three combine to form bonding, nonbonding, and antibonding MOs. The out-of-phase combination matches the symmetry of oxygen's 2py, producing another bonding-antibonding pair. Oxygen's 2px orbital has no hydrogen combination to interact with — it remains a **nonbonding orbital**, a lone pair that sits on oxygen without contributing to bonding. This symmetry-matching approach replaces guesswork with systematic construction.

For larger molecules, **group theory** formalizes the process. You assign the molecule to a point group (C₂v for water, D₃h for BF₃, Tₐ for CH₄), then classify every atomic orbital by its symmetry representation (labeled a₁, b₂, e, t₂, etc. depending on the point group). Orbitals that belong to the same representation can mix; orbitals in different representations cannot — this is a strict selection rule, not a preference. For **methane (CH₄)** in the Tₐ point group, the four H 1s orbitals form one combination of a₁ symmetry and three of t₂ symmetry. Carbon's 2s orbital is a₁ and mixes with the a₁ hydrogen combination; carbon's three 2p orbitals are t₂ and mix with the t₂ hydrogen set. The result is one bonding + one antibonding pair of a₁ symmetry, and three bonding + three antibonding orbitals of t₂ symmetry — eight MOs total from eight atomic orbital inputs. Filling with eight valence electrons (four from C, one from each H) gives four filled bonding orbitals, consistent with methane's four equivalent C–H bonds.

The power of polyatomic MO diagrams lies in what they reveal that simpler models miss. In **CO₂**, the MO diagram shows that the two C=O double bonds are not independent — they are described by delocalized molecular orbitals spanning all three atoms, with π orbitals that extend over the entire molecule. The diagram also predicts that CO₂ has filled bonding orbitals and empty antibonding orbitals with a large HOMO-LUMO gap, explaining its chemical stability and UV absorption properties. For molecules like **O₃** or **NO₂**, where Lewis structures require resonance, the MO diagram naturally produces delocalized orbitals without needing to invoke resonance as a separate concept — the delocalization is built into the orbital construction from the start.
