---
id: chromatin-remodeling-and-histone-acetylation
title: Chromatin Remodeling Complexes and Histone Acetylation
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: chromatin-remodeling-accessibility
  type: hard
- id: histone-modifications-epigenetic
  type: soft
builds-toward:
- transcription-initiation-eukaryotes
- dna-methylation-and-epigenetic-silencing
tags:
- chromatin-remodeling-complexes
- hat
- hdac
- histone-acetyltransferase
- acetylation
stage: formal-systems
status: draft
---

# Chromatin Remodeling Complexes and Histone Acetylation

## Core Idea
Chromatin-remodeling complexes (SWI/SNF, ISWI, CHD, INO80 families) use ATP hydrolysis to alter nucleosome positioning, eject nucleosomes, or alter histone-DNA contacts, making promoters and enhancers accessible to transcription factors and RNA polymerase. Histone acetyltransferases (HATs) add acetyl groups to lysine residues on histone tails, neutralizing positive charge and loosening DNA-histone interactions, creating 'open' chromatin favorable for transcription. Histone deacetylases (HDACs) remove acetyl groups, promoting repressive chromatin and gene silencing. Acetylation states are dynamically regulated by enzyme recruitment through transcription factors and are inherited through cell division, making acetylation a reversible yet persistent epigenetic mechanism.

## Explainer

From your study of chromatin accessibility and histone modifications, you know that DNA in eukaryotic cells is not naked — it is wrapped around histone octamers to form nucleosomes, and the tightness of this packaging determines whether genes can be read. The problem is straightforward: a transcription factor cannot bind a promoter if a nucleosome is sitting on top of it. The cell solves this problem through two complementary mechanisms — **chromatin-remodeling complexes** that physically move nucleosomes, and **histone acetylation** that chemically loosens them.

**Chromatin-remodeling complexes** are molecular machines powered by ATP hydrolysis. Think of them as motorized bulldozers for nucleosomes. The SWI/SNF family can slide a nucleosome along the DNA, exposing a previously buried promoter sequence. The ISWI family spaces nucleosomes into regular arrays, creating ordered chromatin. The INO80 family can eject entire nucleosomes or swap histone variants into the octamer. These complexes do not act randomly — they are recruited to specific genomic locations by transcription factors, sequence-specific DNA-binding proteins, or modified histone tails. The result is targeted remodeling: the cell opens exactly the chromatin regions that need to be read while keeping the rest compacted.

**Histone acetyltransferases** (HATs) work through a different but complementary mechanism based on electrostatics. Histone tails are rich in lysine residues, which carry a positive charge at physiological pH. This positive charge attracts the negatively charged DNA backbone, holding the nucleosome together tightly. When a HAT adds an **acetyl group** to a lysine, it neutralizes that positive charge, weakening the electrostatic grip between histone and DNA. Multiply this across many lysines on multiple histones, and the nucleosome loosens substantially — the DNA becomes more accessible, and the chromatin shifts toward an "open" or **euchromatic** state. Acetylated histones also serve as binding platforms for proteins with **bromodomains**, which recognize acetylated lysines and recruit additional transcriptional machinery.

The reverse process is equally important. **Histone deacetylases** (HDACs) strip acetyl groups from histone tails, restoring the positive charge and tightening nucleosome-DNA contacts. This promotes a condensed, transcriptionally silent **heterochromatic** state. The balance between HAT and HDAC activity at any given locus determines its transcriptional state, and this balance is dynamically regulated — transcription factors recruit HATs to activate genes and HDACs to silence them. Critically, acetylation patterns can be propagated through cell division, because daughter cells inherit modified histones and the enzymes that maintain them. This makes histone acetylation a key mechanism of **epigenetic memory**: a gene activated by acetylation in a liver cell remains active in its daughter cells, even though the original activating signal may be gone. Drugs that inhibit HDACs are now used in cancer therapy precisely because they can reactivate tumor-suppressor genes that were silenced by deacetylation.
