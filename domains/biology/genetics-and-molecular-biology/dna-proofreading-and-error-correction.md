---
id: dna-proofreading-and-error-correction
title: DNA Proofreading and Mismatch Repair
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: dna-replication-accuracy-proofreading
  type: hard
- id: dna-repair-mechanisms
  type: hard
builds-toward:
- genetic-recombination-and-linkage-mapping
tags:
- proofreading
- exonuclease-activity
- mismatch-repair
- fidelity
stage: advanced
status: draft
---

# DNA Proofreading and Mismatch Repair

## Core Idea
DNA replication achieves extraordinarily high fidelity through multiple layers of error correction. DNA polymerase III possesses 3' to 5' exonuclease activity (proofreading) that detects and removes mismatched nucleotides immediately after incorporation, reducing errors to ~1 per 10⁷ nucleotides. Mismatch repair systems (MutS, MutL, MutH in prokaryotes; MLH1, MSH2, MSH6 in eukaryotes) identify and correct errors that escape the polymerase by recognizing strand discontinuities and using strand discrimination signals to remove nucleotides from the newly synthesized strand. Together, these mechanisms reduce the final error rate to approximately 1 per 10⁹ to 10¹⁰ nucleotides, essential for genome stability.

## How It's Best Learned
Compare the consequences of mutations with and without proofreading; calculate error rates at each stage. Examine the specificity of mismatch repair by studying how MutS recognizes distorted DNA without base-pairing information, emphasizing DNA geometry rather than sequence. Relate proofreading to clinical syndromes like Lynch syndrome caused by mismatch repair defects.

## Common Misconceptions
Students may assume that proofreading is the only error-correction mechanism, underestimating the importance of post-replication mismatch repair. Some think polymerase selectivity for correct nucleotides is sufficient without proofreading. The strand discrimination mechanisms in eukaryotes (PCNA and 3' to 5' polarity) are often overlooked.

## Explainer

From your study of DNA replication fidelity and DNA repair, you understand that polymerases select the correct nucleotide with impressive but imperfect accuracy, and that cells possess dedicated repair pathways to fix DNA damage. **DNA proofreading and mismatch repair** represent a layered quality-control system that operates during and immediately after replication, catching errors before they become permanent mutations.

The first layer is built directly into DNA polymerase itself. As the polymerase adds each nucleotide, it checks whether the new base pairs correctly with the template. Correct Watson-Crick base pairs (A-T, G-C) fit snugly into the polymerase's active site, while mismatches create geometric distortions that the enzyme detects. When a mismatch is sensed, the polymerase stalls and its **3' to 5' exonuclease** activity kicks in — a separate catalytic site that chews back the newly synthesized strand, removing the incorrect nucleotide. The polymerase then re-attempts incorporation with the correct base. This proofreading step improves fidelity roughly 100-fold, bringing the error rate from about 1 per 10⁵ nucleotides (polymerase selectivity alone) down to about 1 per 10⁷.

But even 1 error per 10 million bases is too many for a genome of billions of nucleotides. The second layer — **mismatch repair** (MMR) — scans the newly replicated DNA for errors that escaped the polymerase's proofreading. In *E. coli*, the MutS protein slides along the double helix and recognizes mismatched base pairs by detecting subtle distortions in the DNA backbone geometry. MutS then recruits MutL, which activates MutH to nick the unmethylated (newly synthesized) strand — this is the critical **strand discrimination** step, because the repair system must know which strand contains the error. Since the template strand is methylated at GATC sequences and the new strand is transiently unmethylated, MutH can reliably identify the new strand. An exonuclease then degrades the new strand past the mismatch, and the polymerase resynthesizes the gap correctly.

Eukaryotic mismatch repair uses homologous proteins — **MSH2/MSH6** (recognizing single mismatches) and **MLH1/PMS2** — but achieves strand discrimination differently, likely through recognition of nicks and gaps in the lagging strand and the PCNA sliding clamp that marks newly synthesized DNA. Together, proofreading and mismatch repair reduce the final error rate to approximately 1 per 10⁹ to 10¹⁰ nucleotides per cell division. The clinical importance of this system is vividly demonstrated by **Lynch syndrome**: individuals with inherited defects in MLH1 or MSH2 have a dramatically elevated risk of colorectal and other cancers because their cells accumulate mutations at 100 to 1,000 times the normal rate, particularly in repetitive microsatellite sequences where polymerase slippage is common.
