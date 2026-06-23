---
id: rna-splicing-mechanisms
title: RNA Splicing Mechanisms
domain: biology
course: biochemistry
prerequisites:
- id: rna-processing
  type: hard
- id: rna-types-and-structure
  type: soft
- id: transcription-initiation-and-regulation
  type: soft
builds-toward:
- translation-initiation-and-elongation
tags:
- splicing
- spliceosome
- introns
- exons
- lariat intermediate
stage: formal-systems
status: validated
---

# RNA Splicing Mechanisms

## Core Idea
RNA splicing is the removal of introns and ligation of exons in eukaryotic pre-mRNA, catalyzed by the spliceosome, a complex of small nuclear RNAs (snRNPs) and proteins. Splicing involves two transesterification reactions: the first cuts at the 5' splice site, releasing the intron lariat; the second ligates the upstream exon to the downstream exon. Alternative splicing, where different combinations of exons are joined, vastly increases proteomic diversity from a fixed number of genes. Errors in splicing are a major cause of genetic disease.

## Questions

```yaml
- question: "The human genome contains approximately 20,000 protein-coding genes, yet human cells produce an estimated 80,000–100,000 distinct proteins. What is the primary mechanism responsible for this discrepancy?"
  type: multiple-choice
  options:
    - "Post-translational modifications such as phosphorylation and glycosylation create distinct protein variants."
    - "Alternative splicing generates different mRNA isoforms from the same gene by including or excluding different combinations of exons."
    - "Gene duplication has created extra gene copies not yet fully cataloged by the genome project."
    - "Transcriptional errors randomly produce variant proteins at low frequency."
  answer: 1
  explanation: "Alternative splicing is the primary driver of proteomic diversity beyond the gene count. A gene with 10 alternatively spliced exons can theoretically generate over 1,000 distinct mRNA isoforms, each encoding a protein with different functional domains or regulatory properties. Post-translational modifications also contribute to protein diversity, but alternative splicing is responsible for the largest categorical expansion from genes to protein isoforms. This is why the human proteome vastly exceeds the genome in complexity."

- question: "A researcher introduces a point mutation changing the conserved GU dinucleotide at the 5' splice site of an intron to GC. What is the most likely consequence for gene expression?"
  type: multiple-choice
  options:
    - "The intron is skipped normally because the spliceosome uses the 3' splice site as its primary recognition signal."
    - "Splicing is disrupted — the spliceosome fails to recognize the mutant 5' splice site, likely causing intron retention in the mature mRNA or activation of a nearby cryptic splice site."
    - "The mutation is corrected by RNA editing enzymes before splicing occurs."
    - "Transcription of the gene stops because the promoter recognizes the downstream mutation."
  answer: 1
  explanation: "The 5' splice site GU dinucleotide is recognized by U1 snRNP through base-pairing with U1 snRNA. This recognition is essential for initiating spliceosome assembly. Mutating GU to GC disrupts this base-pairing, preventing U1 snRNP from binding. Without proper 5' splice site recognition, the spliceosome cannot assemble correctly: the intron may be retained in the mRNA (intron retention), or the spliceosome may use a nearby 'cryptic' splice site with a weak GU-containing sequence. Either outcome produces an aberrant mRNA that often encodes a nonfunctional protein. This class of mutation accounts for a significant fraction of disease-causing variants."

- question: "In the first transesterification reaction of RNA splicing, the 2'-OH group of the branch point adenosine attacks the phosphodiester bond at the 5' splice site, forming a lariat intermediate with a 2'-5' phosphodiester bond linking the intron's 5' end to the branch point."
  type: true-false
  answer: true
  explanation: "This is the defining chemical step of step 1 of splicing. The branch point adenosine (located 20–50 nucleotides upstream of the 3' splice site) has a free 2'-OH group — unusual because most phosphodiester bonds in RNA link 3' to 5'. This 2'-OH acts as a nucleophile, attacking the phosphodiester bond at the 5' splice site. The result is: (1) the upstream exon is released with a free 3'-OH, and (2) the intron's 5' end is joined to the branch point via a 2'-5' linkage, creating the characteristic lariat structure. Step 2 then completes splicing by ligating the two exons."

- question: "RNA splicing requires ATP hydrolysis to provide the energy needed to break the phosphodiester bonds at the 5' and 3' splice sites."
  type: true-false
  answer: false
  explanation: "Splicing proceeds by transesterification — a bond-exchange reaction in which one phosphodiester bond is broken while another is simultaneously formed. Because the number of phosphodiester bonds is conserved across each reaction step, the reaction is energetically neutral and requires no external energy input (like ATP hydrolysis) to drive the chemistry itself. ATP is consumed during spliceosome assembly and remodeling (by RNA helicases like Prp28, Brr2), but not for the catalytic transesterification reactions. This makes splicing thermodynamically favorable without requiring energy investment in each catalytic cycle."

- question: "Why does a single nucleotide mutation at a splice site represent such a serious molecular threat to protein function, even though the mutation occurs in a non-coding intronic sequence rather than in the protein-coding exon?"
  type: short-answer
  answer: "Splice site sequences (especially the conserved GU at the 5' splice site and AG at the 3' splice site) are recognition signals for the spliceosome. Even a single nucleotide change can prevent spliceosome assembly at that site, causing intron retention in the mRNA. When an intron remains in the mRNA, it introduces non-coding sequence into what the ribosome reads as coding sequence. This almost certainly causes a frameshift — the ribosome reads the intron's nucleotides as codons, scrambling the downstream protein sequence and typically encountering a premature stop codon. Even if the intron happens to be in-frame, it encodes a foreign amino acid sequence that disrupts the protein's structure. The result is a nonfunctional protein from a mutation in sequence the original gene would have discarded."
  explanation: "This is why splicing mutations (splice site mutations, branch point mutations, or mutations in exonic splicing enhancers) account for an estimated 15–50% of disease-causing mutations — comparable to missense mutations in the coding sequence itself. Splicing fidelity is as critical to gene expression as transcriptional accuracy."
```

## Explainer

From your study of RNA processing, you know that eukaryotic genes are interrupted by non-coding **introns** that must be removed before the mRNA can be translated. Splicing is the molecular surgery that accomplishes this — precisely excising introns and joining the flanking **exons** into a continuous coding sequence. The precision required is extraordinary: a single nucleotide error would shift the reading frame and produce a nonfunctional protein. Understanding how the spliceosome achieves this accuracy reveals one of the most elegant molecular machines in the cell.

The spliceosome is not a static enzyme but a dynamic assembly of five **small nuclear ribonucleoprotein particles (snRNPs)** — U1, U2, U4, U5, and U6 — plus over 100 associated proteins. It assembles de novo on each intron. The process begins with **U1 snRNP** recognizing the **5' splice site** (nearly always a GU dinucleotide at the intron's start) through base-pairing between U1 snRNA and the pre-mRNA. Meanwhile, **U2 snRNP** binds the **branch point sequence** (a conserved adenosine typically 20–50 nucleotides upstream of the 3' splice site). The remaining snRNPs join as a preassembled U4/U6·U5 tri-snRNP, triggering extensive rearrangements that eject U1 and U4 and form the catalytically active spliceosome.

The chemistry itself consists of two sequential **transesterification** reactions — phosphodiester bond exchanges that require no external energy input. In **step 1**, the 2'-OH of the branch point adenosine attacks the phosphodiester bond at the 5' splice site. This simultaneously frees the upstream exon and creates the distinctive **lariat intermediate**, where the intron's 5' end is linked to the branch point via an unusual 2'-5' phosphodiester bond. In **step 2**, the free 3'-OH of the upstream exon attacks the phosphodiester bond at the 3' splice site (almost always an AG dinucleotide), ligating the two exons and releasing the intron lariat for degradation. The beauty of transesterification is that two bonds are broken and two are formed — the reaction is energetically neutral, requiring only precise positioning by the spliceosome.

The most profound consequence of splicing is **alternative splicing** — the regulated inclusion or exclusion of specific exons to produce different mRNAs from the same gene. A single gene with 10 alternatively spliced exons can theoretically produce over 1,000 distinct mRNA variants, each encoding a protein with different domains, binding properties, or regulatory features. This is how the human genome, with roughly 20,000 protein-coding genes, generates an estimated 80,000–100,000 distinct proteins. Alternative splicing is controlled by **splicing regulatory elements** (enhancers and silencers) within the pre-mRNA and by tissue-specific RNA-binding proteins (such as SR proteins and hnRNPs) that promote or repress particular splice site choices. Mutations that disrupt splice sites or regulatory elements account for an estimated 15–50% of disease-causing mutations in humans, underscoring that splicing fidelity is as important to gene expression as transcriptional accuracy.
