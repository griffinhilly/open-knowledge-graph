---
id: rna-5-capping-polyadenylation
title: 5' Capping and 3' Polyadenylation of mRNA
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: rna-types-and-structure
  type: soft
builds-toward:
- rna-splicing-introns-exons-spliceosome
- mrna-stability-decay
tags:
- rna-processing
- mrna
- transcription
- nucleotides
stage: advanced
status: draft
---

# 5' Capping and 3' Polyadenylation of mRNA

## Core Idea
The 5' cap (7-methylguanosine) is added co-transcriptionally to nascent mRNA, protecting it from degradation and aiding in translation. The 3' poly(A) tail is added after cleavage downstream of the polyadenylation signal (AAUAAA). Both modifications are essential for mRNA stability, export from the nucleus, and translation efficiency.

## How It's Best Learned
Trace mRNA processing from initiation to mature transcript. Understand the enzymatic steps: guanylyltransferase (capping), endonuclease (3' cleavage), and poly(A) polymerase (tailing). Study how these modifications protect mRNA from exonucleases.

## Common Misconceptions
- Assuming capping and polyadenylation occur independently of transcription.
- Not recognizing that poly(A) tails vary in length and change dynamically during mRNA metabolism.
- Thinking the 5' cap and 3' poly(A) only function in translation when they also affect mRNA localization, stability, and splicing.

## Explainer

When RNA polymerase II begins transcribing a gene, the emerging mRNA transcript is immediately vulnerable. Cellular exonucleases — enzymes that chew RNA from its exposed ends — would rapidly destroy the naked transcript. The cell solves this problem through two chemical modifications that act like protective bookends: a **5' cap** on the front end and a **poly(A) tail** on the back end. Both modifications are added while the mRNA is still being made, not as an afterthought, and both are required for nearly every downstream function of the mature message.

The **5' cap** is a modified guanosine nucleotide (7-methylguanosine, or m7G) attached in an unusual 5'-to-5' triphosphate linkage to the first nucleotide of the transcript. This happens almost immediately — after only about 20-30 nucleotides have been transcribed. The capping enzyme (guanylyltransferase) is recruited directly to the elongating RNA polymerase II, which is why capping is called **co-transcriptional**. The reversed 5'-5' linkage is critical: normal exonucleases recognize 5'-3' bonds, so the cap makes the mRNA's leading end chemically invisible to degradation machinery. Beyond protection, the cap serves as a molecular badge of identity — it recruits the **cap-binding complex (CBC)** in the nucleus for mRNA export and later recruits the translation initiation factor **eIF4E** in the cytoplasm, positioning the ribosome at the start of the message.

At the other end, the **3' poly(A) tail** is added by a different mechanism. As transcription proceeds past the coding region, the pre-mRNA contains a conserved **polyadenylation signal** (typically the hexamer AAUAAA) followed by a GU-rich or U-rich downstream element. A multi-protein complex recognizes these signals, cleaves the RNA 10-30 nucleotides downstream of the AAUAAA, and then **poly(A) polymerase (PAP)** adds 200-250 adenine nucleotides to the new 3' end without any DNA template. The poly(A) tail is bound by **poly(A)-binding proteins (PABPs)**, which protect the tail from shortening and also interact with the 5' cap-binding machinery to circularize the mRNA — a closed-loop structure that dramatically enhances translation efficiency.

Together, the 5' cap and poly(A) tail do far more than simply prevent degradation. They function as a coordinated system: nuclear export machinery checks for both modifications before allowing the mRNA through nuclear pores, ensuring that only fully processed transcripts reach the cytoplasm. In the cytoplasm, the interaction between eIF4E (bound to the cap) and PABP (bound to the tail) creates the circular mRNA topology that allows ribosomes to efficiently reinitiate translation. When it is time for the mRNA to be degraded, the process typically begins with gradual shortening of the poly(A) tail (**deadenylation**), followed by removal of the cap (**decapping**), and finally exonucleolytic digestion — a controlled demolition that uses the same protective features as destruction signals.
