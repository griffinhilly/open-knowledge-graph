---
id: rna-splicing-introns-exons-spliceosome
title: RNA Splicing, Introns, Exons, and the Spliceosome
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-5-capping-polyadenylation
  type: hard
- id: rna-splicing-mechanisms
  type: soft
builds-toward:
- alternative-rna-splicing
- rna-processing
tags:
- splicing
- introns
- exons
- spliceosome
- rna-processing
stage: formal-systems
status: draft
---

# RNA Splicing, Introns, Exons, and the Spliceosome

## Core Idea
Pre-mRNA contains exons (coding sequences) and introns (non-coding sequences). The spliceosome, a complex of small RNAs and proteins, catalyzes two transesterification reactions that remove introns and join exons. Splice sites (GU-AG rule) define intron boundaries, and spliceosome assembly occurs co-transcriptionally.

## How It's Best Learned
Diagram the two-step splicing mechanism: attack of the 2'-OH of branch-point adenine on the 5' splice site, followed by attack of the released 5' exon on the 3' splice site. Align sequences to identify conserved splice sites and branch points in different organisms.

## Common Misconceptions
- Assuming introns are removed completely and leave no trace; they are retained in some genes and have regulatory functions.
- Not recognizing that spliceosome components are themselves RNAs that catalyze the reaction, not just proteins.
- Thinking splicing is an error to be avoided rather than a regulated, essential process.

## Explainer

From your work on RNA processing, you know that the pre-mRNA transcript emerging from RNA polymerase II is not yet ready for translation — it needs a 5' cap, a poly-A tail, and the removal of internal sequences that do not code for protein. Those non-coding internal sequences are **introns**, and the protein-coding segments that flank them are **exons**. Splicing is the process that precisely removes every intron and stitches the exons together into a continuous open reading frame. In human genes, introns often vastly outnumber and outsize exons — the dystrophin gene, for instance, spans 2.4 million base pairs but produces an mRNA of only about 14,000 nucleotides.

The molecular machine that performs splicing is the **spliceosome**, a massive complex assembled from five small nuclear RNAs (snRNAs: U1, U2, U4, U5, U6) and over 100 associated proteins. Unlike what you might expect, the catalytic heart of the spliceosome is RNA, not protein — the snRNAs position the reactive groups and stabilize the transition states, making the spliceosome a **ribozyme**. The spliceosome recognizes each intron through three conserved sequence elements: a **5' splice site** (nearly always starting with GU), a **3' splice site** (nearly always ending with AG), and a **branch point** adenosine located 18–40 nucleotides upstream of the 3' splice site. This GU-AG rule is so consistent that mutations at these positions almost always abolish splicing and cause disease.

Splicing proceeds through exactly two **transesterification** reactions — phosphoester bond exchanges that require no external energy input. In the first step, the 2'-hydroxyl of the branch-point adenosine attacks the phosphodiester bond at the 5' splice site. This cuts the RNA at that junction and creates a **lariat** structure: a looped intron connected by an unusual 2'-5' phosphodiester bond. In the second step, the now-free 3'-hydroxyl of the upstream exon attacks the phosphodiester bond at the 3' splice site, simultaneously joining the two exons and releasing the intron lariat. The lariat is then debranched and degraded, while the joined exons form the mature mRNA.

A critical feature of this process is that splicing occurs **co-transcriptionally** — the spliceosome assembles on the pre-mRNA while RNA polymerase II is still elongating downstream. This coupling is coordinated through the C-terminal domain of the polymerase, which recruits splicing factors to the emerging transcript. Because splicing happens before transcription is complete, the cell can regulate gene expression at the splicing level, choosing which exons to include or skip. This capacity for **alternative splicing** — which builds on the mechanism you are learning here — is why the human genome encodes roughly 20,000 genes but produces well over 100,000 distinct protein variants.
