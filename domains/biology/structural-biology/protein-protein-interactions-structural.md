---
id: protein-protein-interactions-structural
title: Protein-Protein Interactions
domain: biology
course: structural-biology
prerequisites:
- id: x-ray-crystallography
  type: soft
- id: cryo-em
  type: soft
- id: protein-folding-and-chaperones
  type: hard
builds-toward:
- macromolecular-assemblies
tags:
- protein-protein-interaction
- interface
- hotspot
- binding-affinity
- complex-structure
stage: expert
status: validated
---
# Protein-Protein Interactions

## Core Idea
Protein-protein interactions (PPIs) are the physical associations between proteins that underlie virtually all cellular processes — signaling, transcription, translation, metabolism, and structural organization. Structurally, PPI interfaces are large (typically 1,200-2,000 A^2 buried surface area), relatively flat compared to small-molecule binding pockets, and involve complementary shapes, hydrogen bonds, salt bridges, and hydrophobic contacts. A key finding is that binding energy is not uniformly distributed across the interface — a few "hotspot" residues contribute disproportionately to binding affinity, while most interfacial residues contribute little. Understanding PPI structure is critical for drug design targeting PPIs, for engineering protein-protein recognition, and for interpreting the vast PPI networks mapped by proteomics.

## Questions

```yaml
- question: "Why are protein-protein interactions traditionally considered 'undruggable' compared to enzyme active sites?"
  type: multiple-choice
  options:
    - "Proteins never interact with each other in cells"
    - "PPI interfaces are typically large (1,500+ A^2), relatively flat, and lack the deep, well-defined pockets that small molecules can occupy — conventional drugs are too small to cover enough of the interface to compete with the natural protein partner"
    - "PPI interfaces are always identical to enzyme active sites"
    - "Small molecules cannot exist inside cells"
  answer: 1
  explanation: "Enzyme active sites evolved to bind small substrates and typically feature deep, enclosed pockets with specific chemical environments — ideal for small-molecule drugs. PPI interfaces evolved to bind large protein surfaces and are typically broad, flat, and shallow — there is no obvious pocket for a small molecule to occupy. However, the hotspot concept has changed this view: because binding energy is concentrated at a few key residues, a small molecule that targets the hotspot region can potentially disrupt the interaction. Successful PPI inhibitors (venetoclax for Bcl-2/BH3, nutlins for MDM2/p53) bind at hotspot-containing sub-pockets on the interface."

- question: "At a protein-protein interface, every residue in contact contributes equally to the binding affinity."
  type: true-false
  answer: false
  explanation: "Alanine scanning mutagenesis studies (systematically mutating each interfacial residue to alanine and measuring the effect on binding affinity) revealed that binding energy is highly non-uniform. A small number of 'hotspot' residues — typically 3-10% of the interface — contribute most of the binding energy (each contributing >2 kcal/mol when mutated). The remaining interfacial residues contribute little individually. Hotspot residues tend to be at the center of the interface (surrounded by a 'O-ring' of residues that exclude water), are often aromatic (Trp, Tyr, Phe) or charged (Arg), and are more conserved across species than non-hotspot interfacial residues."

- question: "How has the hotspot concept changed the approach to designing small-molecule PPI inhibitors?"
  type: short-answer
  answer: "The hotspot concept showed that disrupting a PPI does not require covering the entire interface — targeting the hotspot region with a small molecule can be sufficient. Drug design efforts focus on identifying the hotspot residues (by alanine scanning or computational prediction), finding or designing small-molecule fragments that mimic the key hotspot interactions, and growing these fragments into drug-like molecules that occupy the hotspot region with high affinity. The hotspot often creates a small sub-pocket on the protein surface where the partner's hotspot residue (like a tryptophan or leucine) inserts — this pocket can serve as a conventional drug binding site. Fragment-based screening and structure-guided optimization from hotspot-binding fragments have produced several clinically approved PPI inhibitors."
  explanation: "The MDM2/p53 interaction illustrates this: p53 binds MDM2 through three hotspot residues (Phe19, Trp23, Leu26) that insert into a hydrophobic pocket on MDM2. Nutlin compounds mimic these three residues and fit into the same pocket, blocking the interaction with nanomolar affinity — a triumph of hotspot-targeted PPI drug design."
```

## Explainer

Proteins rarely work alone. Enzymes form multi-subunit complexes, signaling proteins assemble into cascades through direct binding, transcription factors heterodimerize to read DNA, and the cytoskeleton is built from polymerizing protein subunits. Understanding the structural basis of protein-protein recognition — how two protein surfaces recognize and bind each other with specificity and appropriate affinity — is essential for understanding cellular function and for developing therapies that modulate these interactions.

PPI interfaces differ fundamentally from the small-molecule binding sites that traditional drug discovery targets. A typical PPI buries **1,200-2,000 A^2 of surface area** (compared to ~300-500 A^2 for a drug binding pocket), involves 20-40 residues from each partner, and is relatively flat — lacking the deep invaginations that small molecules exploit for tight binding. The interface features a mix of complementary interactions: **shape complementarity** (the two surfaces fit together like puzzle pieces), **hydrogen bonds** (between polar groups across the interface), **salt bridges** (between oppositely charged residues), and **hydrophobic contacts** (nonpolar residues packed together at the interface center, shielded from solvent by polar peripheral residues — the "O-ring" model).

The **hotspot** concept, established by Clackson and Wells using alanine scanning mutagenesis of the human growth hormone receptor complex, revealed that binding energy is concentrated at a few key residues. Most interfacial residues can be mutated to alanine with minimal effect on binding affinity — they contribute to specificity (correct partner recognition) but not to the total binding energy. The hotspot residues (often tryptophan, tyrosine, arginine) are essential: mutating any one to alanine reduces binding by >2 kcal/mol (10-100x weaker binding). Hotspots are typically clustered at the center of the interface, are enriched in aromatic and charged residues, and are surrounded by peripheral residues that exclude water from the interface (maintaining the low-dielectric environment that strengthens electrostatic interactions).

The hotspot concept has therapeutic implications. If a PPI can be disrupted by targeting just the hotspot, then the "undruggable" nature of PPIs is overstated — the effective target is not the entire 2,000 A^2 interface but the much smaller hotspot region, which may contain pocket-like features suitable for small-molecule binding. This insight has driven the development of **PPI inhibitors** — small molecules that mimic the hotspot interactions and compete with the natural binding partner. Successes include venetoclax (targeting the Bcl-2/BH3 interface in cancer), nutlins (targeting MDM2/p53), and ABT-737 analogs. These compounds represent a new frontier in drug design, enabled by structural understanding of PPI interfaces and hotspot organization.
