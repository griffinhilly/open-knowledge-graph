---
id: rna-polymerase-mechanisms
title: 'RNA Polymerase: Mechanisms and Specificity'
domain: biology
course: biochemistry
prerequisites:
- id: transcription
  type: hard
- id: transcription-initiation-and-regulation
  type: soft
tags:
- RNA-polymerase
- transcription
- catalysis
stage: advanced
status: draft
---

# RNA Polymerase: Mechanisms and Specificity

## Core Idea
RNA polymerase catalyzes the formation of a phosphodiester bond between the 3'-OH of the growing RNA chain and the α-phosphate of incoming NTP. In prokaryotes, a single RNAP synthesizes all RNA; in eukaryotes, three RNA polymerases (I, II, III) have distinct roles. Sigma factors in prokaryotes confer promoter specificity; in eukaryotes, transcription factors direct RNAP II to promoters.

## Explainer

From your study of transcription, you know the basic flow: RNA polymerase reads a DNA template strand and synthesizes a complementary RNA molecule. But the mechanics of how RNA polymerase actually accomplishes this — opening the double helix, selecting the right nucleotide, forming the bond, and moving forward — involve a sophisticated molecular machine with distinct functional domains and a catalytic cycle that repeats thousands of times per gene.

The core chemistry is a **nucleotidyl transfer reaction**. The 3'-hydroxyl group at the end of the growing RNA chain acts as a nucleophile, attacking the α-phosphate of an incoming ribonucleoside triphosphate (NTP). This forms a new **phosphodiester bond**, extending the chain by one nucleotide in the 5'→3' direction and releasing pyrophosphate (PPi). Two magnesium ions in the active site are essential — one positions the 3'-OH for attack, the other stabilizes the departing pyrophosphate. The subsequent hydrolysis of PPi by pyrophosphatase makes the overall reaction essentially irreversible, driving transcription forward. Unlike DNA polymerase, RNA polymerase does not require a primer — it can initiate a new chain de novo, though the first few nucleotides are added inefficiently in a process called **abortive initiation** before the enzyme clears the promoter and enters productive elongation.

In prokaryotes, a single RNA polymerase (the **core enzyme**, composed of subunits α₂ββ'ω) handles all transcription — mRNA, rRNA, and tRNA. But the core enzyme alone cannot find promoters. It requires a dissociable **sigma (σ) factor** that recognizes specific promoter sequences (the −10 and −35 elements for the primary σ⁷⁰ in *E. coli*). The sigma factor binds the core enzyme to form the **holoenzyme**, directs it to the promoter, and facilitates DNA melting to form the open complex. Once the polymerase begins elongation, the sigma factor dissociates, and the core enzyme proceeds on its own. Different sigma factors recognize different promoter sequences, allowing the cell to redirect transcription in response to environmental changes — for example, σ³² directs transcription of heat-shock genes during thermal stress.

Eukaryotes divide the labor among three specialized RNA polymerases. **RNA Polymerase I** (Pol I) transcribes the large ribosomal RNA precursor (28S, 18S, 5.8S rRNA) in the nucleolus — a single gene product that accounts for the majority of cellular RNA. **RNA Polymerase II** (Pol II) transcribes all protein-coding mRNAs, plus most snRNAs and microRNAs, and is the most heavily regulated of the three. **RNA Polymerase III** (Pol III) transcribes tRNAs, 5S rRNA, and other small structural RNAs. Each polymerase is recruited to its target genes by a distinct set of **general transcription factors** (GTFs) rather than by a sigma factor. For Pol II, the assembly of TFIID (which recognizes the TATA box via TBP), TFIIB, TFIIF, TFIIE, and TFIIH at the promoter forms the **pre-initiation complex**. TFIIH is particularly noteworthy — its helicase activity melts the DNA to form the transcription bubble, and its kinase activity phosphorylates the **C-terminal domain (CTD)** of Pol II's largest subunit, triggering promoter clearance and the transition to elongation.

The division of labor in eukaryotes allows each polymerase to be regulated independently and optimized for its product. Pol I operates at extraordinary speed in the nucleolus to meet the cell's massive demand for ribosomes. Pol II's CTD serves as a landing pad for mRNA processing factors — capping, splicing, and polyadenylation enzymes associate with the CTD at different stages of transcription, coupling RNA synthesis to RNA processing. This integrated system ensures that mRNAs are not simply transcribed but are co-transcriptionally processed and quality-checked before export from the nucleus.
