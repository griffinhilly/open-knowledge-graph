---
id: transcription-initiation-eukaryotes
title: 'Eukaryotic Transcription Initiation: TFIID, Mediator, and Chromatin'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: gene-regulation-eukaryotes
  type: hard
- id: chromatin-remodeling-accessibility
  type: soft
- id: transcription-initiation-and-regulation
  type: soft
builds-toward:
- rna-polymerase-ii-and-ctd-regulation
- transcription-factors-and-gene-regulation
tags:
- tfiid
- tata-box
- initiator-elements
- mediator-complex
- chromatin-accessibility
stage: formal-systems
status: draft
---

# Eukaryotic Transcription Initiation: TFIID, Mediator, and Chromatin

## Core Idea
Eukaryotic transcription initiation is substantially more complex than prokaryotic, involving multiple general transcription factors (TFIID, TFIIB, TFIIE, TFIIF, TFIIH) that recognize core promoter elements including the TATA box (consensus TATAAA ~25 nucleotides upstream) and Initiator elements. Chromatin accessibility is a prerequisite—nucleosomes must be remodeled or displaced by chromatin remodeling complexes to expose the promoter. The Mediator complex, a large multiprotein complex, bridges enhancer-bound transcription factors and the RNA polymerase II preinitiation complex, enabling long-range transcriptional regulation across genomic distances. This architectural complexity allows precise developmental and environmental control of gene expression.

## Questions

```yaml
- question: "A gene has a perfect TATA box and all necessary general transcription factors are present in abundant quantities. However, the promoter region is embedded in tightly packed heterochromatin. What will happen?"
  type: multiple-choice
  options:
    - "Transcription will proceed normally — TFIID can recognize the TATA box regardless of chromatin packaging"
    - "TFIIH will use its helicase activity to melt the chromatin and expose the promoter before preinitiation complex assembly"
    - "Transcription will not initiate — chromatin accessibility is a prerequisite; nucleosomes occluding the promoter must be remodeled or displaced before any transcription factor can reach the DNA"
    - "RNA Pol II will transcribe the heterochromatin directly as a non-specific template"
  answer: 2
  explanation: "Chromatin accessibility is the first gate in eukaryotic transcription. The presence of general transcription factors and a perfect promoter sequence is irrelevant if the DNA is physically inaccessible under nucleosomes packed into heterochromatin. ATP-dependent chromatin remodeling complexes (like SWI/SNF) must slide or eject nucleosomes to expose the promoter, and histone-modifying enzymes must create the right chemical environment, before TFIID can bind and PIC assembly can begin. This is a fundamental difference from prokaryotic transcription, where RNA polymerase and sigma factor can access naked DNA directly."

- question: "A transcriptional activator protein is bound to an enhancer 80 kb upstream of a gene's promoter. RNA Pol II is located at the core promoter. How does the activator's signal reach the polymerase?"
  type: multiple-choice
  options:
    - "The transcription factor diffuses along the DNA in three-dimensional space until it contacts RNA Pol II directly at the promoter"
    - "The transcription factor synthesizes a signaling molecule that diffuses through the nucleus to reach the preinitiation complex"
    - "DNA looping brings the enhancer into physical proximity with the promoter; the Mediator complex bridges the enhancer-bound activator and the preinitiation complex, transmitting the activation signal"
    - "TFIIB scans the chromatin for bound transcription factors and relays their activation signals to the core promoter"
  answer: 2
  explanation: "Long-range transcriptional regulation works through DNA looping — the chromosomal region between the enhancer and promoter loops out, bringing the two regulatory elements into physical contact. The Mediator complex serves as the molecular bridge: its tail domain contacts the enhancer-bound transcription factor, and its head domain contacts the preinitiation complex at the promoter. Mediator integrates signals from multiple enhancer-bound factors and relays them to RNA Pol II, explaining how a single gene can respond to dozens of different regulatory inputs simultaneously."

- question: "The Mediator complex directly recognizes the TATA box and serves as the primary DNA-binding component of the preinitiation complex."
  type: true-false
  answer: false
  explanation: "TATA box recognition is the job of TBP (TATA-binding protein), a subunit of TFIID. TBP binds the minor groove of the TATA box consensus sequence approximately 25 bp upstream of the transcription start site, bending the DNA and creating the platform for preinitiation complex assembly. Mediator does not bind DNA at the core promoter; it bridges between enhancer-bound transcription factors and the already-assembled PIC. Confusing Mediator's role with TFIID's role is a common error because both are essential for initiation."

- question: "TFIIH plays a dual role in transcription initiation: its helicase activity separates the DNA strands to form the transcription bubble, and its kinase activity phosphorylates the CTD of RNA Pol II to trigger the transition from initiation to elongation."
  type: true-false
  answer: true
  explanation: "TFIIH is the most enzymatically active general transcription factor. Its XPB/XPD subunits provide ATP-dependent helicase activity to melt about 11-15 bp of DNA at the transcription start site, generating the open complex (transcription bubble) that allows RNA synthesis to begin. Its CDK7 kinase subunit phosphorylates Ser5 of the heptapeptide repeat in the CTD of RNA Pol II, converting the polymerase from its initiation conformation to an elongation-competent form and also recruiting RNA processing factors. Both activities are required for productive transcription."

- question: "Why does eukaryotic transcription initiation require both chromatin remodeling and the Mediator complex, while prokaryotic transcription requires neither? What regulatory capability does this complexity provide?"
  type: short-answer
  answer: "Prokaryotic DNA is not packaged into nucleosomes and lacks enhancer-based regulation; a sigma factor alone can recognize the promoter and recruit RNA polymerase. Eukaryotic DNA is compacted into chromatin, making the promoter physically inaccessible by default — chromatin remodeling is required to expose it. And eukaryotic genes must integrate regulatory signals from multiple enhancers located far from the promoter across the genome; Mediator provides the physical bridge for this long-range communication. Together, these two requirements create a system where a gene's expression integrates many inputs: developmental stage, cell type, environmental signals, all encoded in which transcription factors are bound to which enhancers. The complexity enables the precise, combinatorial gene regulation that underlies eukaryotic development and differentiation."
  explanation: "This architectural logic explains why a human genome with ~20,000 genes can generate hundreds of distinct cell types: the same genes are regulated differently in each cell type by different combinations of transcription factors, chromatin states, and active enhancers — all converging through Mediator onto the core machinery."
```

## Explainer

In prokaryotes, transcription initiation is relatively straightforward: a single sigma factor recognizes the promoter, and RNA polymerase binds and begins transcribing. Eukaryotic transcription initiation is fundamentally different in scale and complexity, requiring a large ensemble of proteins to assemble at the promoter before RNA polymerase II can begin work. Understanding why requires remembering what you learned about eukaryotic gene regulation and chromatin structure — the DNA is not naked and freely accessible but is wrapped around histones and packaged into chromatin.

The first barrier to transcription is **chromatin accessibility**. Before any transcription factor can reach the DNA, the nucleosomes occluding the promoter region must be moved or modified. **Chromatin remodeling complexes** (ATP-dependent machines like SWI/SNF) physically slide or eject nucleosomes, while histone-modifying enzymes add chemical marks (acetylation, methylation) that either loosen chromatin or recruit additional regulatory proteins. This is why chromatin state acts as a gatekeeper — a gene buried in tightly packed heterochromatin simply cannot be transcribed, regardless of what transcription factors are present in the cell.

Once the promoter is accessible, the **preinitiation complex (PIC)** assembles in an ordered sequence. The process typically begins with **TFIID**, a multi-subunit complex whose TBP (TATA-binding protein) subunit recognizes the **TATA box** — a conserved AT-rich sequence located about 25 base pairs upstream of the transcription start site. TBP binds the minor groove and bends the DNA sharply, creating a platform for subsequent factors. TFIID also contains **TAFs** (TBP-associated factors) that recognize other core promoter elements like the **Initiator (Inr)** element at the start site and downstream promoter elements. After TFIID binds, **TFIIB** joins and positions the polymerase, followed by **TFIIF** (which escorts RNA Pol II to the promoter), and then **TFIIE** and **TFIIH**. TFIIH is particularly important: its helicase activity melts the DNA double strand to form the transcription bubble, and its kinase activity phosphorylates the **C-terminal domain (CTD)** of RNA Pol II, triggering the transition from initiation to elongation.

The **Mediator complex** is the final critical piece and the key to understanding how eukaryotes achieve precise gene regulation. Mediator is a massive (~30-subunit) complex that acts as a molecular bridge between gene-specific **transcription factors** bound at distant enhancer elements and the general transcription machinery assembled at the core promoter. Enhancers can be located tens or hundreds of kilobases away from the promoter they regulate; DNA looping brings them into physical proximity with the promoter, and Mediator transmits the activating or repressing signals from enhancer-bound factors to the PIC. This architecture means that the decision to transcribe a gene integrates multiple inputs — developmental signals, environmental cues, chromatin state — all converging through Mediator onto the core machinery. The result is a system where a single gene can be regulated by dozens of enhancers and transcription factors, enabling the exquisite cell-type-specific expression patterns that define eukaryotic development.
