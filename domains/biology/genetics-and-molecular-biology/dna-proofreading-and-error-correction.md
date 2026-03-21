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

## Questions

```yaml
- question: "A mutation eliminates the 3'→5' exonuclease activity of DNA polymerase III but leaves its polymerization activity intact. What would you predict?"
  type: multiple-choice
  options:
    - "Mutation rate would be unchanged — the polymerase's selectivity for correct nucleotides during incorporation is already sufficient for high fidelity"
    - "Mutation rate would increase approximately 100-fold — proofreading provides the second layer of fidelity beyond nucleotide selection, and removing it eliminates correction of errors that escaped initial selectivity"
    - "Mutation rate would increase approximately 10⁹-fold, wiping out genome stability entirely"
    - "Mutation rate would decrease — the polymerase would advance more smoothly without pausing to backtrack"
  answer: 1
  explanation: "Nucleotide selection by the polymerase achieves approximately 1 error per 10⁵ bases. Proofreading (3'→5' exonuclease) then catches and removes most of the remaining mismatches, improving fidelity ~100-fold to ~1 per 10⁷. Removing proofreading restores the ~10⁵ error rate. Option A is wrong because selectivity alone is insufficient — mismatches do occur during initial incorporation and require proofreading to catch them. Option C overstates the effect: even without proofreading, mismatch repair would still provide another ~100-1000x improvement."

- question: "In E. coli, a mutation eliminates MutH protein. MutS and MutL are still functional. What step of mismatch repair would specifically fail?"
  type: multiple-choice
  options:
    - "Mismatch recognition would fail — MutH is required for MutS to bind mismatched bases"
    - "Strand discrimination would fail — MutH nicks the newly synthesized (unmethylated) strand at GATC sequences; without it, the repair system cannot identify which strand contains the error and risks repairing the wrong strand"
    - "Exonuclease removal of mismatched nucleotides would fail — MutH directly degrades the incorrect bases"
    - "DNA re-synthesis after excision would fail — MutH activates the repair polymerase"
  answer: 1
  explanation: "MutS detects the mismatch; MutL coordinates the response. MutH performs the critical and unique step of strand discrimination: it nicks the hemimethylated GATC site on the transiently unmethylated new strand, identifying it as the error-containing strand for repair. Without MutH, the system detects the mismatch but cannot determine which of the two strands is wrong. Repairing the template strand would replace the correct base to match the error — permanently fixing the mutation rather than correcting it."

- question: "The strand discrimination mechanism in E. coli mismatch repair exploits the transient hemimethylated state of newly replicated DNA: the template strand is already methylated at GATC sequences, while the newly synthesized strand is not yet methylated."
  type: true-false
  answer: true
  explanation: "This is the elegant molecular solution to the 'which strand is wrong?' problem. Dam methylase adds methyl groups to adenine in GATC sequences, but there is a brief window after replication when only the template strand carries these marks — the new strand hasn't been methylated yet. MutH recognizes this hemimethylated state and nicks the unmethylated (new) strand, directing repair to the error-containing strand. This timing-based mechanism is critical: without it, the repair system could not reliably distinguish template from new strand."

- question: "DNA polymerase proofreading and mismatch repair detect errors by the same molecular mechanism — recognizing incorrect Watson-Crick base pairs by their chemical properties."
  type: true-false
  answer: false
  explanation: "These mechanisms are distinct. Polymerase proofreading detects geometric distortion in the polymerase's active site during synthesis — a mismatched nucleotide physically doesn't fit the active site's shape, causing the polymerase to stall and backtrack. Mismatch repair (via MutS) detects distortions in the backbone geometry of the already-synthesized double helix as MutS slides along DNA from outside the polymerase. One is an active-site structural check during synthesis; the other is a post-synthesis scanning mechanism. They are mechanistically independent, which is why removing one leaves the other fully functional."

- question: "Why is the ability to distinguish the newly synthesized strand from the template strand essential for mismatch repair, and how does E. coli solve this problem?"
  type: short-answer
  answer: "When MutS detects a mismatch, both strands contain a base at that position — but only one is wrong (the newly synthesized strand). If the repair machinery repaired the template strand instead, it would change the correct base to match the erroneous one, permanently converting the mismatch into a mutation. E. coli solves this using methylation: Dam methylase methylates adenine in GATC sequences on both strands, but newly replicated DNA is transiently hemimethylated — template strand methylated, new strand not yet. MutH recognizes this state and nicks the unmethylated strand, directing all repair activity to the strand most likely to contain the error."
  explanation: "Strand discrimination is the conceptually most subtle part of mismatch repair. Detecting a mismatch is the easy part — any distortion in the helix will do. Knowing which of the two bases is wrong requires an external signal, because the mismatched bases themselves don't tell you which is 'right.' The methylation-based system is a temporal trick: it exploits the gap between replication (which produces the new strand) and methylation (which eventually marks it) as a window during which the new strand is identifiable. Lynch syndrome, caused by defects in human mismatch repair genes, illustrates what happens when this system fails at scale."
```

## Explainer

From your study of DNA replication fidelity and DNA repair, you understand that polymerases select the correct nucleotide with impressive but imperfect accuracy, and that cells possess dedicated repair pathways to fix DNA damage. **DNA proofreading and mismatch repair** represent a layered quality-control system that operates during and immediately after replication, catching errors before they become permanent mutations.

The first layer is built directly into DNA polymerase itself. As the polymerase adds each nucleotide, it checks whether the new base pairs correctly with the template. Correct Watson-Crick base pairs (A-T, G-C) fit snugly into the polymerase's active site, while mismatches create geometric distortions that the enzyme detects. When a mismatch is sensed, the polymerase stalls and its **3' to 5' exonuclease** activity kicks in — a separate catalytic site that chews back the newly synthesized strand, removing the incorrect nucleotide. The polymerase then re-attempts incorporation with the correct base. This proofreading step improves fidelity roughly 100-fold, bringing the error rate from about 1 per 10⁵ nucleotides (polymerase selectivity alone) down to about 1 per 10⁷.

But even 1 error per 10 million bases is too many for a genome of billions of nucleotides. The second layer — **mismatch repair** (MMR) — scans the newly replicated DNA for errors that escaped the polymerase's proofreading. In *E. coli*, the MutS protein slides along the double helix and recognizes mismatched base pairs by detecting subtle distortions in the DNA backbone geometry. MutS then recruits MutL, which activates MutH to nick the unmethylated (newly synthesized) strand — this is the critical **strand discrimination** step, because the repair system must know which strand contains the error. Since the template strand is methylated at GATC sequences and the new strand is transiently unmethylated, MutH can reliably identify the new strand. An exonuclease then degrades the new strand past the mismatch, and the polymerase resynthesizes the gap correctly.

Eukaryotic mismatch repair uses homologous proteins — **MSH2/MSH6** (recognizing single mismatches) and **MLH1/PMS2** — but achieves strand discrimination differently, likely through recognition of nicks and gaps in the lagging strand and the PCNA sliding clamp that marks newly synthesized DNA. Together, proofreading and mismatch repair reduce the final error rate to approximately 1 per 10⁹ to 10¹⁰ nucleotides per cell division. The clinical importance of this system is vividly demonstrated by **Lynch syndrome**: individuals with inherited defects in MLH1 or MSH2 have a dramatically elevated risk of colorectal and other cancers because their cells accumulate mutations at 100 to 1,000 times the normal rate, particularly in repetitive microsatellite sequences where polymerase slippage is common.
