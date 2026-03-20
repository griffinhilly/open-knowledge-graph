---
id: protein-trafficking-secretion
title: Protein Trafficking and Secretory Pathways
domain: biology
course: cell-biology
prerequisites:
- id: protein-targeting-and-subcellular-localization
  type: hard
tags:
- protein-trafficking
- secretion
- signal-sequences
- vesicular-transport
stage: advanced
status: draft
---

# Protein Trafficking and Secretory Pathways

## Core Idea
Secreted and membrane proteins bear signal sequences that direct them to the rough ER, where the Signal Recognition Particle (SRP) recognizes them and directs them to the ER translocon for co-translational translocation. Proteins traverse the secretory pathway (ER → Golgi → secretory vesicles), where they are modified (glycosylation, phosphorylation, proteolytic cleavage) and sorted to their destination by coat proteins and adaptors. Misfolded proteins are retained in the ER and targeted for degradation via the proteasome.

## Explainer

From your study of protein targeting and subcellular localization, you know that signal sequences act as molecular zip codes directing proteins to specific compartments. The secretory pathway is the major highway that delivers proteins to the cell surface, the extracellular space, and membrane-bound organelles like lysosomes. Understanding this pathway means following a protein from the moment its signal sequence emerges from the ribosome to its final destination.

The journey begins during translation. As the ribosome synthesizes a secretory protein, the first ~20 amino acids to emerge form a hydrophobic **signal peptide**. The **Signal Recognition Particle (SRP)** — a ribonucleoprotein complex — binds this signal peptide and temporarily pauses translation. SRP then docks with its receptor on the rough ER membrane, threading the growing polypeptide into the **translocon**, a protein-conducting channel. Translation resumes, and the polypeptide is pushed through the translocon into the ER lumen as it is being made — this is **co-translational translocation**. Once inside, signal peptidase cleaves off the signal peptide, and ER-resident chaperones (like BiP) help the protein fold correctly.

Inside the ER, the protein receives its first modifications. **N-linked glycosylation** attaches a pre-assembled sugar tree to asparagine residues, which assists folding and serves as a quality-control tag. Chaperones and lectins (calnexin, calreticulin) inspect the protein's folding state by reading these sugar modifications. Properly folded proteins are packaged into **COPII-coated vesicles** that bud from the ER and fuse with the Golgi apparatus. Misfolded proteins are retained, given additional folding attempts, and if they persistently fail, retrotranslocated back to the cytoplasm for degradation by the proteasome — a process called **ER-associated degradation (ERAD)**.

The **Golgi apparatus** functions as the cell's processing and sorting center. Proteins enter at the cis-Golgi and move through medial and trans cisternae, receiving sequential modifications: trimming and adding sugars, adding sulfate groups, and proteolytic processing (such as cleaving proinsulin into active insulin). At the trans-Golgi network, proteins are sorted into different vesicle populations based on sorting signals in their amino acid sequence. Lysosomal enzymes receive a mannose-6-phosphate tag that directs them to lysosomes. Constitutive secretory proteins are continuously exported to the cell surface. Regulated secretory proteins are stored in dense-core granules and released only upon a specific signal — like calcium influx triggering neurotransmitter release at a synapse. Each of these routes uses distinct **coat proteins** (clathrin, COPI, COPII) and **SNARE proteins** that ensure vesicles fuse only with the correct target membrane.
