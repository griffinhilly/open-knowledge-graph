---
id: mrna-5-capping-and-3-polyadenylation
title: mRNA 5' Capping and 3' Polyadenylation
domain: biology
course: cell-biology
prerequisites:
- id: rna-types-and-structure
  type: hard
- id: transcription
  type: hard
builds-toward:
- spliceosome-and-splicing-regulation
tags:
- mRNA-processing
- capping
- polyadenylation
stage: abstract-reasoning
status: draft
---

# mRNA 5' Capping and 3' Polyadenylation

## Core Idea
mRNA 5' capping involves addition of a 7-methylguanosine cap via an unusual 5'-5' triphosphate linkage within the first 20-50 nucleotides of transcription, protecting mRNA from 5' exonucleases and facilitating ribosome binding. 3' polyadenylation, catalyzed by cleavage and polyadenylation specificity factor (CPSF), involves endonucleolytic cleavage 10-30 nucleotides downstream of the AAUAAA signal and addition of ~200 adenine residues by poly(A) polymerase. Both modifications occur co-transcriptionally and are essential for mRNA stability, nuclear export, and efficient translation.

## How It's Best Learned
Measure cap and poly(A) tail synthesis rates in isolated transcription systems; assess their effects on mRNA stability using pulse-chase labeling. Use cap- and poly(A)-binding proteins to map modification sites.

## Common Misconceptions
- 5' cap and 3' poly(A) tail are added post-transcriptionally; they're added during transcription. - Capping requires the 5' triphosphate of the nascent RNA; the first nucleotide becomes the cap's second position.

## Explainer

From your study of transcription, you know that RNA polymerase II synthesizes a pre-mRNA strand by reading the template DNA. But the raw transcript that emerges from the polymerase is vulnerable — exonucleases in the nucleus would quickly degrade it from either end, and ribosomes in the cytoplasm would have no way to recognize it as a legitimate message. The **5' cap** and **3' poly(A) tail** solve both problems by adding protective structures to each end of the mRNA, and they do so while transcription is still in progress, not after it finishes.

The **5' cap** is added remarkably early — as soon as the first 20–30 nucleotides have emerged from RNA polymerase II. A capping enzyme removes the terminal phosphate from the 5' end of the nascent RNA, then attaches a guanosine nucleotide in an unusual **5'-to-5' triphosphate linkage** (most nucleotide bonds are 3'-to-5'). This reversed orientation makes the cap chemically distinct from anything an exonuclease expects to encounter, effectively blocking degradation from the 5' end. A methyltransferase then adds a methyl group to the guanosine, creating the **7-methylguanosine (m⁷G) cap**. Later, when the mRNA reaches the cytoplasm, this cap is what the ribosome recognizes: eukaryotic translation initiation factor eIF4E binds the cap and recruits the small ribosomal subunit, making the cap essential for translation to begin.

At the other end, the **3' poly(A) tail** is produced by a two-step process. As RNA polymerase II transcribes past a conserved **AAUAAA signal sequence**, a protein complex called CPSF (cleavage and polyadenylation specificity factor) recognizes this signal and cleaves the pre-mRNA about 10–30 nucleotides downstream. The enzyme **poly(A) polymerase** then adds approximately 200 adenine nucleotides to the new 3' end, one at a time, without any DNA template. This poly(A) tail is bound by poly(A)-binding proteins that protect it from 3' exonuclease attack and, together with the 5' cap, form a loop structure that enhances translation efficiency.

Together, these two modifications transform a fragile, anonymous RNA strand into a recognized, protected, export-ready messenger. The cap says "start translating here," the poly(A) tail says "this message is complete and stable," and both are required for the mRNA to pass through nuclear pores into the cytoplasm. Over time, the poly(A) tail is gradually shortened by deadenylases — this shortening is a molecular clock that determines mRNA lifespan. Once the tail is too short to bind protective proteins, the mRNA is rapidly degraded, giving cells precise control over how long each message persists.
