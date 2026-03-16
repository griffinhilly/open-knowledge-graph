---
id: dna-polymerase-structure-and-fidelity
title: 'DNA Polymerase: Structure and Fidelity'
domain: biology
course: biochemistry
prerequisites:
- id: dna-replication-machinery
  type: hard
- id: dna-replication-accuracy-proofreading
  type: soft
tags:
- DNA-polymerase
- fidelity
- error-rate
stage: advanced
status: draft
---

# DNA Polymerase: Structure and Fidelity

## Core Idea
DNA polymerases catalyze the nucleophilic attack of the 3'-OH on the α-phosphate of incoming dNTPs, releasing pyrophosphate and forming a phosphodiester bond. Fidelity is achieved through base-pair geometry constraints and 3'→5' exonuclease proofreading, reducing error rates to ~10⁻10 per base. Pol III synthesizes the leading strand continuously and lagging strand via Okazaki fragments.

## Explainer

From your study of DNA replication machinery, you know that a team of proteins works together to copy the genome. DNA polymerase is the central player in that team — the enzyme that actually builds the new strand, one nucleotide at a time. But what makes this enzyme remarkable is not just that it can polymerize DNA; it is that it does so with extraordinary accuracy, inserting the wrong base only about once every ten billion nucleotides when all fidelity mechanisms are combined.

The chemistry of polymerization follows a straightforward mechanism. The **3'-hydroxyl group** on the last nucleotide of the growing strand acts as a nucleophile, attacking the **α-phosphate** of the incoming deoxynucleoside triphosphate (dNTP). This breaks the bond between the α- and β-phosphates, releasing **pyrophosphate** (PPi), which is immediately hydrolyzed by pyrophosphatase to two inorganic phosphates. That hydrolysis makes the overall reaction thermodynamically irreversible — it pulls the equilibrium decisively toward chain elongation. Two divalent metal ions (typically Mg²⁺) in the active site coordinate the phosphates and stabilize the transition state, a feature conserved across virtually all DNA polymerases.

Fidelity operates at three successive levels. The first is **geometric selection**: the polymerase active site is shaped to accept only a correctly paired Watson-Crick base pair. A mismatched pair has the wrong geometry — it is either too wide (two purines) or too narrow (two pyrimidines) or has misaligned hydrogen bond donors and acceptors — and the polymerase undergoes a conformational change that rejects it. This alone reduces errors to roughly one in 10⁴–10⁵. The second level is **kinetic proofreading**: even after a mismatch is incorporated, the distorted geometry at the primer terminus slows the next polymerization step, giving the enzyme time to transfer the strand to its **3'→5' exonuclease** domain. This proofreading domain clips off the mismatched nucleotide, returns the strand to the polymerase site, and allows a second attempt. Proofreading improves fidelity by another 100-fold. The third level — post-replicative mismatch repair — is handled by separate enzymes, but the polymerase's built-in mechanisms alone achieve error rates near 10⁻⁷.

In *E. coli*, **Pol III holoenzyme** is the primary replicative polymerase. Its β-clamp (sliding clamp) encircles the DNA and tethers the polymerase to the template, granting high processivity — the ability to add thousands of nucleotides without falling off. The leading strand is synthesized continuously in the 5'→3' direction, while the lagging strand is synthesized as short **Okazaki fragments** (1,000–2,000 nucleotides in prokaryotes) that are later joined by DNA ligase. Understanding polymerase structure and fidelity is essential because it explains both why replication is so accurate and why mutations still occur — no proofreading system is perfect, and the residual error rate is a major source of genetic variation and, in some cases, disease.
