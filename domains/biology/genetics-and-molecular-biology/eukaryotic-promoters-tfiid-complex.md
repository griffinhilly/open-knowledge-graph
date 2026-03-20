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
stage: advanced
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

## Explainer

From your study of prokaryotic promoters, you know that bacteria use a relatively simple system: the sigma factor (σ) associates with RNA polymerase, recognizes the –10 and –35 promoter elements, and positions the enzyme to begin transcription. Eukaryotic transcription initiation is fundamentally more complex because eukaryotic DNA is wrapped around histones and packed into chromatin — the promoter is not freely accessible. Instead of a single sigma factor, eukaryotes use an elaborate assembly of **general transcription factors** (GTFs) that build a **pre-initiation complex (PIC)** at the promoter before RNA Polymerase II can begin work.

The process begins with the **TATA box**, a conserved sequence (consensus TATAAA) typically located about 25-30 base pairs upstream of the transcription start site. The **TFIID complex** recognizes and binds this element. TFIID itself is a multi-protein complex containing **TBP (TATA-binding protein)** and approximately 13 **TBP-associated factors (TAFs)**. TBP binds directly to the TATA box in an unusual way — it inserts into the minor groove of DNA and bends it sharply by about 80°, creating a distinctive structural landmark that other factors can recognize. This bending is critical: it physically distorts the DNA in a way that signals "start here" to the rest of the transcription machinery.

Once TFIID is bound, the remaining general transcription factors assemble in a specific order: **TFIIA** stabilizes the TFIID-DNA interaction, **TFIIB** bridges TFIID to RNA Polymerase II and helps position the enzyme at the correct start site, **TFIIF** escorts RNA Pol II to the promoter, and finally **TFIIE** and **TFIIH** complete the complex. TFIIH is particularly important because it has **helicase activity** — it uses ATP energy to unwind the DNA double helix at the start site, creating the transcription bubble that allows RNA synthesis to begin. TFIIH also **phosphorylates** the C-terminal domain (CTD) of RNA Pol II, which triggers the transition from initiation to elongation — the polymerase releases from the promoter and begins moving along the template.

Not all eukaryotic promoters contain a TATA box. Many housekeeping genes — those expressed constitutively in all cell types — use **TATA-less promoters** that instead rely on other elements like the **Inr (initiator)** sequence at the start site, the **DPE (downstream promoter element)**, or **CpG islands**. TFIID can still bind these promoters through its TAF subunits, which recognize these alternative elements. Additional upstream elements like the **CAAT box** (~–80) and **GC box** (~–100) bind specific transcription factors (NF-Y and Sp1, respectively) that enhance TFIID recruitment and increase transcription rates. The strength of a promoter — how frequently it initiates transcription — depends on the combination, spacing, and exact sequences of these elements. This modular architecture is what allows eukaryotic cells to achieve the precise, tunable gene regulation that a complex organism requires.
