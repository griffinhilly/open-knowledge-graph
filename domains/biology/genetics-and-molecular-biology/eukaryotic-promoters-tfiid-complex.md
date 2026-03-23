---
id: eukaryotic-promoters-tfiid-complex
title: Eukaryotic Promoters and the TFIID Complex
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: prokaryotic-promoters-sigma-factors
  type: hard
- id: gene-regulation-eukaryotes
  type: soft
builds-toward:
- transcription-factors-binding-domains
- enhancers-silencers-eukaryotic
tags:
- transcription
- eukaryotes
- promoters
- tfiid
- gene-regulation
stage: formal-systems
status: draft
---

# Eukaryotic Promoters and the TFIID Complex

## Core Idea
Eukaryotic promoters (TATA box, CAAT box, GC box) are recognized by transcription factor TFIID and its associated factors, forming the pre-initiation complex. This multi-protein machinery is required to position RNA polymerase II correctly and initiate transcription. Promoter strength depends on the sequence and spacing of these elements.

## How It's Best Learned
Compare prokaryotic and eukaryotic promoter structure and regulation. Map TFIID factor binding to promoter elements. Understand how weak vs. strong promoters have different affinities for TFIID and different transcription rates.

## Common Misconceptions
- Assuming the TATA box alone is sufficient for transcription initiation.
- Not recognizing that multiple DNA-binding proteins must assemble in a precise order to form the pre-initiation complex.
- Thinking TFIID has the same role as prokaryotic sigma factors when their mechanisms differ fundamentally.

## Questions

```yaml
- question: "A researcher mutates the TATA box of a eukaryotic gene's promoter to a random non-binding sequence. What is the most likely consequence for transcription of that gene?"
  type: multiple-choice
  options:
    - "No significant effect — the TATA box is not required for all eukaryotic genes, so transcription continues via alternative elements"
    - "Transcription increases because the mutant sequence no longer bends DNA, allowing more open access for RNA Pol II"
    - "Transcription is severely reduced because TBP cannot bind, blocking assembly of the pre-initiation complex and preventing RNA Pol II from being correctly positioned"
    - "Only the transition from initiation to elongation is impaired — RNA Pol II still assembles at the promoter but cannot begin moving along the template"
  answer: 2
  explanation: "For genes with TATA box-containing promoters, the TATA box is the nucleation point for pre-initiation complex (PIC) assembly. TBP within TFIID binds the TATA box directly, bending DNA ~80° and creating the structural platform for sequential recruitment of TFIIA, TFIIB, RNA Pol II/TFIIF, TFIIE, and TFIIH. If TBP cannot bind, this entire cascade fails and transcription is essentially abolished. Note that TATA-less promoters exist (many housekeeping genes use Inr, DPE, or CpG islands instead), so the answer is specifically about genes that do have a functional TATA box."

- question: "Which step in eukaryotic pre-initiation complex assembly directly triggers the transition from initiation to elongation?"
  type: multiple-choice
  options:
    - "TFIID binding to the TATA box and bending the DNA ~80°, which signals RNA Pol II to begin synthesis"
    - "TFIIB bridging TFIID to RNA Polymerase II and positioning the enzyme at the transcription start site"
    - "TFIIH phosphorylating the C-terminal domain (CTD) of RNA Pol II, releasing the polymerase from the promoter so it can begin elongation"
    - "TFIIA stabilizing the TFIID-DNA interaction against competitive inhibitors"
  answer: 2
  explanation: "TFIIH is the 'launch' signal for elongation. It contains two critical enzymatic activities: helicase activity (to unwind the DNA double helix and create the transcription bubble) and kinase activity (to phosphorylate the RNA Pol II CTD). Phosphorylation of the CTD is the molecular trigger that releases RNA Pol II from the promoter-bound PIC and converts it from an initiation-competent to an elongation-competent form. TFIID binding (option A) nucleates the complex; TFIIB (option B) positions Pol II; TFIIA (option D) stabilizes — but none of these trigger the transition to elongation."

- question: "TFIIH contributes both helicase activity (to unwind DNA at the transcription start site) and kinase activity (to phosphorylate the RNA Pol II CTD), making it essential for both transcription bubble formation and the initiation-to-elongation transition."
  type: true-false
  answer: true
  explanation: "TFIIH is the most enzymatically active component of the pre-initiation complex and serves as the 'activation switch' for transcription. Its XPB and XPD subunits have helicase activity that uses ATP to unwind ~10 bp of DNA at the transcription start site, forming the open complex. Its CDK7 subunit phosphorylates serine residues in the heptapeptide repeats of RNA Pol II's C-terminal domain, which releases the polymerase from the promoter and recruits elongation factors and RNA processing machinery. TFIIH is also part of the nucleotide excision repair pathway, connecting transcription and DNA repair."

- question: "The TATA box in eukaryotic promoters plays the same role as the −10 and −35 elements in prokaryotic promoters: both serve as direct recognition sequences where RNA polymerase itself binds to initiate transcription."
  type: true-false
  answer: false
  explanation: "This is a key conceptual difference between prokaryotic and eukaryotic transcription initiation. In prokaryotes, the sigma factor — which is a direct subunit of the holoenzyme — recognizes the −10 and −35 elements. RNA polymerase itself makes the initial promoter contact. In eukaryotes, RNA Pol II never directly contacts the TATA box. Instead, TBP (within TFIID) binds the TATA box first, and RNA Pol II is recruited downstream through protein-protein interactions with TFIIB and TFIIF. The eukaryotic system requires a full pre-initiation complex assembled before Pol II arrives; the prokaryotic system uses sigma as a direct bridge between polymerase and DNA."

- question: "Why does eukaryotic transcription initiation require a multi-protein pre-initiation complex rather than a single sigma-factor equivalent, and what feature of eukaryotic DNA contributes to this requirement?"
  type: short-answer
  answer: "Eukaryotic DNA is wrapped around histones and compacted into chromatin, making promoter sequences physically inaccessible. A single factor analogous to sigma could not reliably access and open chromatin-embedded promoters. The multi-protein PIC provides a modular, tunable system: different combinations of general transcription factors, chromatin remodelers, and co-activators can be recruited under different conditions, allowing precise regulation of which genes are transcribed at what level in which cell type. The assembly sequence also provides multiple regulatory checkpoints — each step is a potential control point for activators or repressors."
  explanation: "The complexity of eukaryotic transcription initiation is a consequence of the chromatin packaging problem and the need for fine-grained gene regulation in multicellular organisms. Prokaryotic sigma factors work because bacterial DNA is largely accessible and the cell needs only modest transcriptional diversity. Eukaryotic cells must regulate thousands of genes independently across hundreds of cell types, requiring a combinatorial assembly system. The PIC architecture — where TFIID, GTFs, Pol II, Mediator, and chromatin remodelers all contribute — creates the regulatory flexibility that enables cell differentiation and tissue-specific gene expression."
```

## Explainer

From your study of prokaryotic promoters, you know that bacteria use a relatively simple system: the sigma factor (σ) associates with RNA polymerase, recognizes the –10 and –35 promoter elements, and positions the enzyme to begin transcription. Eukaryotic transcription initiation is fundamentally more complex because eukaryotic DNA is wrapped around histones and packed into chromatin — the promoter is not freely accessible. Instead of a single sigma factor, eukaryotes use an elaborate assembly of **general transcription factors** (GTFs) that build a **pre-initiation complex (PIC)** at the promoter before RNA Polymerase II can begin work.

The process begins with the **TATA box**, a conserved sequence (consensus TATAAA) typically located about 25-30 base pairs upstream of the transcription start site. The **TFIID complex** recognizes and binds this element. TFIID itself is a multi-protein complex containing **TBP (TATA-binding protein)** and approximately 13 **TBP-associated factors (TAFs)**. TBP binds directly to the TATA box in an unusual way — it inserts into the minor groove of DNA and bends it sharply by about 80°, creating a distinctive structural landmark that other factors can recognize. This bending is critical: it physically distorts the DNA in a way that signals "start here" to the rest of the transcription machinery.

Once TFIID is bound, the remaining general transcription factors assemble in a specific order: **TFIIA** stabilizes the TFIID-DNA interaction, **TFIIB** bridges TFIID to RNA Polymerase II and helps position the enzyme at the correct start site, **TFIIF** escorts RNA Pol II to the promoter, and finally **TFIIE** and **TFIIH** complete the complex. TFIIH is particularly important because it has **helicase activity** — it uses ATP energy to unwind the DNA double helix at the start site, creating the transcription bubble that allows RNA synthesis to begin. TFIIH also **phosphorylates** the C-terminal domain (CTD) of RNA Pol II, which triggers the transition from initiation to elongation — the polymerase releases from the promoter and begins moving along the template.

Not all eukaryotic promoters contain a TATA box. Many housekeeping genes — those expressed constitutively in all cell types — use **TATA-less promoters** that instead rely on other elements like the **Inr (initiator)** sequence at the start site, the **DPE (downstream promoter element)**, or **CpG islands**. TFIID can still bind these promoters through its TAF subunits, which recognize these alternative elements. Additional upstream elements like the **CAAT box** (~–80) and **GC box** (~–100) bind specific transcription factors (NF-Y and Sp1, respectively) that enhance TFIID recruitment and increase transcription rates. The strength of a promoter — how frequently it initiates transcription — depends on the combination, spacing, and exact sequences of these elements. This modular architecture is what allows eukaryotic cells to achieve the precise, tunable gene regulation that a complex organism requires.
