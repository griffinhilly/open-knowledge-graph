---
id: rna-processing
title: RNA Processing and Splicing
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: rna-types-and-structure
  type: hard
builds-toward:
- gene-regulation-eukaryotes
- translation
tags:
- splicing
- introns
- exons
- 5' cap
- poly-A tail
- pre-mRNA
stage: formal-systems
status: validated
---

# RNA Processing and Splicing

## Core Idea
In eukaryotes, the primary RNA transcript (pre-mRNA) undergoes three major processing steps before export to the cytoplasm: addition of a 7-methylguanosine cap at the 5' end, cleavage and polyadenylation at the 3' end, and splicing of introns by the spliceosome. The cap and poly-A tail protect the mRNA from degradation and aid translation initiation. Splicing removes non-coding intron sequences and joins exons; alternative splicing of the same pre-mRNA can produce multiple protein isoforms from a single gene, greatly expanding proteomic diversity.

## How It's Best Learned
Diagram the pre-mRNA and trace each processing event in order. Work through an example of alternative splicing to see how exon inclusion or skipping produces different proteins.

## Common Misconceptions
- Prokaryotes do not perform RNA splicing because their genes lack introns — this is a eukaryote-specific process.
- Introns are not 'junk'; many contain regulatory sequences and non-coding RNA genes.

## Questions

```yaml
- question: "The human genome contains approximately 20,000 protein-coding genes, yet the human proteome contains far more than 20,000 distinct proteins. Which RNA processing mechanism best explains this discrepancy?"
  type: multiple-choice
  options:
    - "The 5' cap adds molecular variants to each mRNA, producing different protein start sites"
    - "Alternative splicing can include or exclude different exons from the same pre-mRNA, producing multiple distinct protein isoforms from a single gene"
    - "Poly-A tail length variation changes mRNA stability and therefore the relative abundance of each protein"
    - "RNA editing changes specific nucleotides after transcription, generating extensive sequence diversity"
  answer: 1
  explanation: "Alternative splicing is the dominant mechanism. Over 90% of human multi-exon genes undergo alternative splicing, and combinatorial inclusion or exclusion of exons can generate dozens or hundreds of distinct mRNA variants from one gene. The Drosophila Dscam gene can theoretically produce over 38,000 variants from a single locus. While RNA editing (option 3) does contribute some diversity, it is far less widespread and impactful than alternative splicing in explaining the proteome-to-genome complexity ratio."

- question: "What would most likely happen to a eukaryotic mRNA if its 5' cap were removed immediately after transcription?"
  type: multiple-choice
  options:
    - "Translation would be faster because ribosomes could access the start codon more easily without the cap in the way"
    - "The mRNA would be rapidly degraded by 5'→3' exonucleases and translation initiation would fail"
    - "Splicing could not occur because the spliceosome requires the cap to identify the correct pre-mRNA"
    - "The poly-A tail would compensate, and the mRNA would function normally"
  answer: 1
  explanation: "The 5' cap serves two critical functions: protecting the mRNA's 5' end from exonuclease degradation, and serving as the recognition signal for the ribosomal initiation complex (via the cap-binding protein eIF4E). Without the cap, the mRNA is vulnerable to rapid 5'→3' degradation and ribosomes cannot efficiently initiate translation. The poly-A tail (option 3) protects the 3' end but cannot compensate for loss of 5' protection or the ribosome-binding function that the cap provides."

- question: "The same pre-mRNA can give rise to proteins with different functions in different cell types through alternative splicing."
  type: true-false
  answer: true
  explanation: "Alternative splicing allows cell-type-specific regulation of which exons are included in mature mRNA. SR proteins that promote exon inclusion and hnRNPs that cause exon skipping are themselves differentially expressed across tissues, creating a tissue-specific splicing code. A gene might produce a membrane-bound isoform in neurons (by including an exon encoding a transmembrane domain) and a soluble isoform in liver cells (by excluding that exon) — two functionally distinct proteins from one gene."

- question: "Prokaryotic genes contain introns that are removed by the spliceosome, just like eukaryotic genes."
  type: true-false
  answer: false
  explanation: "Prokaryotic genes generally lack introns — their protein-coding sequences are continuous. This is why prokaryotes do not require an RNA processing pipeline and can begin translating an mRNA while it is still being transcribed. Spliceosome-mediated splicing is exclusively eukaryotic and evolved alongside the intron-containing genome organization of eukaryotes. (Rare self-splicing introns exist in some prokaryotes and eukaryotic organelles, but these are fundamentally different from spliceosomal splicing.)"

- question: "How does alternative splicing allow the human proteome to be far more complex than the ~20,000 protein-coding genes in the genome, and what machinery controls which isoforms are produced in different cells?"
  type: short-answer
  answer: "Alternative splicing produces multiple distinct mRNA variants from a single gene by including or excluding different combinations of exons. A gene with several exons can generate many functionally distinct proteins through combinatorial exon selection. Over 90% of human multi-exon genes are alternatively spliced. The choice of which splice sites to use is regulated by splicing factors: SR proteins bind enhancer sequences to promote exon inclusion, while hnRNPs bind silencer sequences to cause exon skipping. Because these regulators are differentially expressed across cell types and developmental stages, different tissues produce different isoform profiles from the same gene."
  explanation: "This makes the spliceosome a major layer of gene regulation. Mutations that disrupt splice sites or splicing regulatory sequences can cause disease by shifting the isoform balance — several cancers involve mutations in spliceosome components or splicing regulators, underscoring that splicing is not a mere housekeeping step but a critical control point in gene expression."
```

## Explainer

From your study of transcription, you know that RNA polymerase reads a DNA template and synthesizes an RNA copy. In prokaryotes, that transcript is essentially ready to be translated — ribosomes can even begin translating the mRNA while it is still being transcribed. Eukaryotes, however, insert an entire processing pipeline between transcription and translation. The initial transcript, called **pre-mRNA**, must be modified in three major ways before it can leave the nucleus: capping, polyadenylation, and splicing.

The **5' cap** is a modified guanosine nucleotide (7-methylguanosine) added to the very first nucleotide of the transcript through an unusual 5'-to-5' triphosphate linkage. This cap serves as a molecular passport — it protects the mRNA from exonuclease degradation, signals the ribosome where to begin translation, and helps the mRNA get exported through the nuclear pore. At the other end, the **3' poly-A tail** is added after a specific cleavage event downstream of a polyadenylation signal (typically AAUAAA). An enzyme called poly-A polymerase then adds a string of 100–250 adenine nucleotides. Like the cap, the poly-A tail stabilizes the transcript and aids in translation initiation. Together, these two modifications act like protective bookends.

The most dramatic processing step is **splicing**, in which non-coding sequences called **introns** are removed and the remaining coding sequences, called **exons**, are joined together. This is carried out by the **spliceosome**, a large complex of small nuclear ribonucleoproteins (snRNPs, pronounced "snurps") that recognizes conserved sequences at intron-exon boundaries — the 5' splice site, the branch point, and the 3' splice site. The spliceosome catalyzes two transesterification reactions: first, the 2'-OH of an adenosine at the branch point attacks the 5' splice site, creating a lariat-shaped intermediate; second, the free 3'-OH of the upstream exon attacks the 3' splice site, joining the exons and releasing the intron lariat for degradation.

What makes splicing especially powerful is **alternative splicing** — the ability to include or exclude particular exons in different cell types or developmental stages. A single gene can produce multiple distinct protein isoforms this way. The Drosophila *Dscam* gene, for example, can theoretically generate over 38,000 different mRNA variants from a single gene through combinatorial exon selection. In humans, it is estimated that over 90% of multi-exon genes undergo alternative splicing, which is one reason the human proteome is far more complex than the roughly 20,000 protein-coding genes in the genome would suggest. Splicing regulation involves additional proteins — **SR proteins** that promote exon inclusion and **hnRNPs** that can cause exon skipping — creating a splicing code that rivals transcriptional regulation in its complexity.
