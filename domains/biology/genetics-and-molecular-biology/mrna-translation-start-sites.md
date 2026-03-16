---
id: mrna-translation-start-sites
title: mRNA Translation Start Sites and Initiation
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: genetic-code
  type: hard
- id: translation
  type: soft
builds-toward:
- ribosomal-initiation-factors-tRNA
- translation-elongation-elongation-factors
tags:
- translation
- initiation
- start-codon
- ribosome
stage: formal-systems
status: draft
---

# mRNA Translation Start Sites and Initiation

## Core Idea
Translation initiation is highly regulated. In prokaryotes, AUG codons in the ribosome-binding site (Shine-Dalgarno sequence) are recognized; in eukaryotes, the 5' cap and Kozak consensus sequence direct ribosome scanning to the first AUG. The start codon establishes the reading frame for all downstream codons.

## How It's Best Learned
Compare prokaryotic and eukaryotic mechanisms of start codon selection. Use Kozak or Shine-Dalgarno matrices to predict translation start sites in real genes. Understand how ribosomal subunits are recruited and positioned at the start codon.

## Common Misconceptions
- Assuming all AUG codons initiate translation; context and regulatory elements determine initiation sites.
- Not recognizing that the reading frame set by the start codon is fixed for the entire mRNA.
- Thinking prokaryotic and eukaryotic initiation mechanisms are identical when they differ significantly.

## Explainer

From the genetic code, you know that triplet codons specify amino acids and that **AUG** serves as the universal start codon, encoding methionine. But knowing that AUG means "start" raises a critical question: an mRNA molecule may contain dozens of AUG triplets — how does the ribosome know which one to use? The answer differs fundamentally between prokaryotes and eukaryotes, and understanding these two mechanisms reveals how translation initiation is one of the most tightly regulated steps in gene expression.

In **prokaryotes**, the answer involves direct RNA-RNA base pairing. Upstream of the start codon, most bacterial mRNAs contain a purine-rich sequence called the **Shine-Dalgarno (SD) sequence**, typically 5'-AGGAGG-3' or a variant. This sequence is complementary to a region near the 3' end of the 16S ribosomal RNA in the 30S ribosomal subunit. Base pairing between the SD sequence and the 16S rRNA positions the ribosome so that the nearby AUG codon sits precisely in the P site, ready for initiation. This mechanism has an important consequence: prokaryotic mRNAs can be **polycistronic** — a single mRNA can encode multiple proteins, each with its own SD sequence and start codon. The ribosome can initiate translation at internal AUG codons independently, which is why bacterial operons can produce several proteins from one transcript.

**Eukaryotic** initiation works entirely differently. There is no Shine-Dalgarno sequence. Instead, the small (40S) ribosomal subunit is recruited to the **5' cap** of the mRNA — the modified guanosine added during mRNA processing. The 40S subunit, loaded with the initiator tRNA (Met-tRNAi) and a suite of **eukaryotic initiation factors (eIFs)**, then **scans** along the mRNA in the 5' to 3' direction until it encounters the first AUG codon in a favorable sequence context. That context is described by the **Kozak consensus sequence**: (gcc)GCC**A/G**CC**AUG**G, where the purine at position -3 (three nucleotides before the AUG) and the G at position +4 are the most critical. If the first AUG is in a strong Kozak context, the ribosome initiates there with high efficiency. If the context is weak, the ribosome may skip it and continue scanning — a phenomenon called **leaky scanning** that can produce alternative protein products from the same mRNA.

The choice of start codon has profound consequences because it sets the **reading frame** for the entire downstream coding sequence. A ribosome initiating at the correct AUG will read every subsequent codon in frame, producing the intended protein. An AUG just one nucleotide off would shift the reading frame, producing a completely different — and almost certainly nonfunctional — amino acid sequence until a premature stop codon is reached. This is why start codon selection is under such tight control: it is not simply about finding methionine, but about ensuring that the entire message is decoded correctly from the very first codon.
