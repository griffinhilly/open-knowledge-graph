---
id: dna-replication-accuracy-proofreading
title: DNA Replication Accuracy and Proofreading
domain: biology
course: biochemistry
prerequisites:
- id: dna-replication-machinery
  type: hard
builds-toward:
- dna-repair-mechanisms
tags:
- fidelity
- 3' to 5' exonuclease
- mismatch repair
- error rate
stage: advanced
status: draft
---

# DNA Replication Accuracy and Proofreading

## Core Idea
DNA polymerases achieve extraordinary accuracy (~1 error per 10¹⁰ nucleotides) through two mechanisms: nucleotide selection (discrimination at insertion) and 3'→5' exonuclease activity (proofreading, removing mismatched bases). Polymerase selectivity for correct base pairs relies on geometry: correct Watson-Crick pairs fit optimally in the polymerase active site, while mismatches are poorly accommodated. Mismatch repair proteins (MutS, MutL, MutH in bacteria; MSH, MLH in eukaryotes) provide a third level of accuracy by detecting and removing errors on the newly synthesized strand.

## Explainer

From your study of DNA replication machinery, you know that DNA polymerase synthesizes a new strand by adding nucleotides complementary to the template. But consider the scale of the challenge: the human genome contains roughly 6.4 billion base pairs, and every cell division must copy all of them. If the error rate were even one in a million, each division would introduce thousands of mutations — far too many for a complex organism to survive. The cell solves this through three successive layers of error correction, each catching mistakes the previous layer missed.

The first layer is **nucleotide selectivity** at the polymerase active site. DNA polymerase does not simply match bases by hydrogen bonding — it uses the geometry of the entire base pair. A correct Watson-Crick pair (A-T or G-C) has a precise shape that fits snugly into the active site, like a key in a lock. A mismatch distorts this geometry, and the polymerase responds by dramatically slowing the catalytic reaction. This selectivity alone reduces the error rate to roughly one mistake per 10⁵ nucleotides — impressive, but still far too high for a billion-base genome.

The second layer is **3'→5' exonuclease proofreading**. When a mismatched nucleotide is incorporated, the distorted base pair sits poorly in the active site and the polymerase stalls. The mismatched 3' end of the growing strand is then shuttled to a separate exonuclease domain within the same enzyme, which clips off the incorrect nucleotide. The polymerase then re-attempts insertion with the correct base. Think of it as a built-in backspace key — the polymerase can detect its own typo, erase it, and try again. This step improves fidelity by another factor of about 100, bringing the error rate down to roughly one per 10⁷ nucleotides.

The third layer is **mismatch repair (MMR)**, which operates after replication is complete. Specialized proteins scan the newly synthesized DNA for remaining mismatches. In bacteria, MutS recognizes the distortion caused by a mismatch, MutL coordinates the repair, and MutH distinguishes the new strand from the template by detecting methylation patterns (the template strand is methylated, the new strand is not yet). The mismatch is excised from the new strand and resynthesized correctly. Eukaryotes use homologous proteins (MSH and MLH families) and distinguish strands by the presence of nicks in the newly synthesized strand. This final checkpoint reduces the error rate by another factor of 100–1000, achieving the extraordinary overall fidelity of approximately one error per 10⁹ to 10¹⁰ base pairs copied.

Together, these three mechanisms form a hierarchy of quality control: selectivity prevents most errors, proofreading catches the ones that slip through, and mismatch repair sweeps up the rest. When any layer fails — as when MMR genes are mutated in hereditary nonpolyposis colorectal cancer (Lynch syndrome) — mutation rates climb dramatically, illustrating how essential each layer is to genomic stability.
