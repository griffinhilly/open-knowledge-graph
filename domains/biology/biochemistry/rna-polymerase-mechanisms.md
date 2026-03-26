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
stage: formal-systems
status: validated
---

# RNA Polymerase: Mechanisms and Specificity

## Core Idea
RNA polymerase catalyzes the formation of a phosphodiester bond between the 3'-OH of the growing RNA chain and the α-phosphate of incoming NTP. In prokaryotes, a single RNAP synthesizes all RNA; in eukaryotes, three RNA polymerases (I, II, III) have distinct roles. Sigma factors in prokaryotes confer promoter specificity; in eukaryotes, transcription factors direct RNAP II to promoters.

## Questions

```yaml
- question: "If a bacterial cell's primary sigma factor (σ⁷⁰) is inactivated by mutation, what is the most direct consequence for transcription?"
  type: multiple-choice
  options:
    - "Elongation would slow, since sigma factor is needed to keep RNA polymerase moving along the DNA"
    - "Transcription would continue normally since sigma factor is optional for most constitutively expressed genes"
    - "The core RNA polymerase could not recognize and bind specific promoters, preventing transcription initiation at most genes"
    - "Only rRNA transcription would be affected since σ⁷⁰ specifically regulates ribosomal RNA genes"
  answer: 2
  explanation: "The core enzyme (α₂ββ'ω) is catalytically competent — it can elongate RNA once it has a template — but it cannot find promoters on its own. Sigma factor confers promoter specificity: it recognizes the −10 and −35 elements of prokaryotic promoters and facilitates DNA melting to form the open complex. Without σ⁷⁰, the core enzyme would be unable to initiate transcription at the vast majority of E. coli genes. Different sigma factors (σ³², σ⁵⁴, etc.) recognize different promoter sequences, allowing cells to redirect transcription programs, but σ⁷⁰ is required for housekeeping gene expression."

- question: "Which property distinguishes RNA polymerase from DNA polymerase in a functionally important way?"
  type: multiple-choice
  options:
    - "RNA polymerase requires zinc ions while DNA polymerase requires magnesium ions for catalysis"
    - "RNA polymerase can initiate a new chain de novo without a primer, while DNA polymerase requires a primer with a free 3'-OH group"
    - "RNA polymerase synthesizes in the 3'→5' direction, while DNA polymerase synthesizes in the 5'→3' direction"
    - "RNA polymerase uses deoxyribonucleotides while DNA polymerase uses ribonucleotides"
  answer: 1
  explanation: "Both polymerases synthesize in the 5'→3' direction (C is wrong). Both use magnesium (A is wrong). The substrate specificity is the reverse of D. The critical functional difference is primer requirement: DNA polymerase cannot start a new chain because it requires a free 3'-OH to attack the incoming dNTP. RNA polymerase has an active site geometry that allows it to hold two NTPs and catalyze formation of the first phosphodiester bond de novo — no pre-existing chain is needed. This is why primase (an RNA polymerase) must lay down RNA primers before DNA polymerase can replicate DNA."

- question: "In eukaryotes, a single RNA polymerase transcribes most types of RNA, carrying out the same division of labor as the core enzyme does in prokaryotes."
  type: true-false
  answer: false
  explanation: "Eukaryotes divide transcriptional labor among three RNA polymerases with distinct targets: Pol I transcribes large ribosomal RNAs (28S, 18S, 5.8S) in the nucleolus; Pol II transcribes all protein-coding mRNAs plus snRNAs and microRNAs; Pol III transcribes tRNAs, 5S rRNA, and other small structural RNAs. Each is recruited by its own set of general transcription factors and regulated independently. This division allows each polymerase to be tuned for its product — Pol I operates at extraordinary speed for ribosome biogenesis; Pol II's C-terminal domain coordinates co-transcriptional mRNA processing."

- question: "In prokaryotes, different sigma factors allow the cell to redirect transcription to different sets of genes in response to environmental conditions."
  type: true-false
  answer: true
  explanation: "Different sigma factors recognize different promoter consensus sequences, so swapping sigma factors effectively switches which genes are transcribed. E. coli σ⁷⁰ recognizes housekeeping gene promoters; σ³² is expressed during heat stress and directs transcription of heat-shock protein genes; σ³⁸ (σˢ) governs the stationary-phase response. Because sigma factor dissociates after promoter clearance, producing new sigma factors is a rapid way to reprogram transcription without changing the core polymerase. This modularity is a key feature of prokaryotic gene regulation."

- question: "Why can't the prokaryotic core RNA polymerase initiate transcription on its own? What role does the sigma factor play, and what is the eukaryotic functional equivalent of this mechanism?"
  type: short-answer
  answer: "The core enzyme (α₂ββ'ω) has catalytic activity but lacks the ability to recognize specific promoter sequences. Without sigma factor, it binds DNA non-specifically and cannot discriminate between promoter and non-promoter sequences. Sigma factor adds promoter recognition: it contacts the −10 and −35 consensus elements of the promoter, positions the core enzyme correctly, and facilitates the melting of double-stranded DNA to form the transcription bubble (open complex). Sigma dissociates after the polymerase clears the promoter, leaving the core to elongate on its own. In eukaryotes, the analogous function is performed by general transcription factors (GTFs). For Pol II, a set of GTFs (TFIID, TFIIB, TFIIF, TFIIE, TFIIH) assembles at the promoter to form the pre-initiation complex; TFIIH's helicase activity melts the DNA and its kinase phosphorylates the CTD to trigger elongation. The logic is the same — catalysis and promoter recognition are separated — but eukaryotes use a larger, more complex assembly of factors rather than a single exchangeable subunit."
  explanation: "The separation of catalytic function (core enzyme/Pol II) from promoter-recognition function (sigma/GTFs) is a recurring architectural principle in gene regulation. It allows the transcriptional machinery to be redirected to different genes by swapping or modulating the specificity components without redesigning the entire polymerase — a modular solution to transcriptional control."
```

## Explainer

From your study of transcription, you know the basic flow: RNA polymerase reads a DNA template strand and synthesizes a complementary RNA molecule. But the mechanics of how RNA polymerase actually accomplishes this — opening the double helix, selecting the right nucleotide, forming the bond, and moving forward — involve a sophisticated molecular machine with distinct functional domains and a catalytic cycle that repeats thousands of times per gene.

The core chemistry is a **nucleotidyl transfer reaction**. The 3'-hydroxyl group at the end of the growing RNA chain acts as a nucleophile, attacking the α-phosphate of an incoming ribonucleoside triphosphate (NTP). This forms a new **phosphodiester bond**, extending the chain by one nucleotide in the 5'→3' direction and releasing pyrophosphate (PPi). Two magnesium ions in the active site are essential — one positions the 3'-OH for attack, the other stabilizes the departing pyrophosphate. The subsequent hydrolysis of PPi by pyrophosphatase makes the overall reaction essentially irreversible, driving transcription forward. Unlike DNA polymerase, RNA polymerase does not require a primer — it can initiate a new chain de novo, though the first few nucleotides are added inefficiently in a process called **abortive initiation** before the enzyme clears the promoter and enters productive elongation.

In prokaryotes, a single RNA polymerase (the **core enzyme**, composed of subunits α₂ββ'ω) handles all transcription — mRNA, rRNA, and tRNA. But the core enzyme alone cannot find promoters. It requires a dissociable **sigma (σ) factor** that recognizes specific promoter sequences (the −10 and −35 elements for the primary σ⁷⁰ in *E. coli*). The sigma factor binds the core enzyme to form the **holoenzyme**, directs it to the promoter, and facilitates DNA melting to form the open complex. Once the polymerase begins elongation, the sigma factor dissociates, and the core enzyme proceeds on its own. Different sigma factors recognize different promoter sequences, allowing the cell to redirect transcription in response to environmental changes — for example, σ³² directs transcription of heat-shock genes during thermal stress.

Eukaryotes divide the labor among three specialized RNA polymerases. **RNA Polymerase I** (Pol I) transcribes the large ribosomal RNA precursor (28S, 18S, 5.8S rRNA) in the nucleolus — a single gene product that accounts for the majority of cellular RNA. **RNA Polymerase II** (Pol II) transcribes all protein-coding mRNAs, plus most snRNAs and microRNAs, and is the most heavily regulated of the three. **RNA Polymerase III** (Pol III) transcribes tRNAs, 5S rRNA, and other small structural RNAs. Each polymerase is recruited to its target genes by a distinct set of **general transcription factors** (GTFs) rather than by a sigma factor. For Pol II, the assembly of TFIID (which recognizes the TATA box via TBP), TFIIB, TFIIF, TFIIE, and TFIIH at the promoter forms the **pre-initiation complex**. TFIIH is particularly noteworthy — its helicase activity melts the DNA to form the transcription bubble, and its kinase activity phosphorylates the **C-terminal domain (CTD)** of Pol II's largest subunit, triggering promoter clearance and the transition to elongation.

The division of labor in eukaryotes allows each polymerase to be regulated independently and optimized for its product. Pol I operates at extraordinary speed in the nucleolus to meet the cell's massive demand for ribosomes. Pol II's CTD serves as a landing pad for mRNA processing factors — capping, splicing, and polyadenylation enzymes associate with the CTD at different stages of transcription, coupling RNA synthesis to RNA processing. This integrated system ensures that mRNAs are not simply transcribed but are co-transcriptionally processed and quality-checked before export from the nucleus.
