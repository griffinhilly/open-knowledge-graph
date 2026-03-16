---
id: transcription-initiation-prokaryotes
title: 'Prokaryotic Transcription Initiation: Sigma Factors and Promoters'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: transcription
  type: hard
- id: gene-regulation-prokaryotes
  type: soft
builds-toward:
- transcription-elongation-and-termination
- promoters-enhancers-and-regulatory-regions
tags:
- sigma-factors
- pribnow-box
- -10-element
- -35-element
- promoter-specificity
stage: formal-systems
status: draft
---

# Prokaryotic Transcription Initiation: Sigma Factors and Promoters

## Core Idea
In prokaryotes, transcription initiation requires sigma factors—dissociable subunits that confer promoter-specific DNA recognition to the core RNA polymerase. Sigma factors recognize consensus sequences upstream of the transcription start site: the -10 region (Pribnow box, consensus TATAAT) and the -35 region (consensus TTGACA). Different sigma factors (σ70 for housekeeping genes, σ32 for heat-shock, σ54 for nitrogen metabolism) recognize distinct promoter variants, enabling global gene regulation in response to stress. Sigma factor dissociates after synthesis of ~8-10 nucleotides of transcript, allowing the polymerase core to transition to elongation.

## Explainer

From your study of transcription, you know that RNA polymerase synthesizes RNA from a DNA template. In prokaryotes like *E. coli*, there is only one core RNA polymerase (composed of subunits α₂ββ'ω), and it handles all transcription — mRNA, rRNA, and tRNA alike. But here is the problem: the core enzyme can bind DNA nonspecifically and can elongate RNA, yet it cannot recognize promoters on its own. It needs a detachable guide to find the right starting points. That guide is the **sigma factor (σ)**, and the combination of core polymerase plus sigma factor is called the **holoenzyme**.

The sigma factor works by recognizing two specific DNA sequences upstream of the transcription start site. The **-10 element** (also called the **Pribnow box**, consensus sequence TATAAT) sits approximately 10 base pairs upstream of where transcription begins, and the **-35 element** (consensus TTGACA) sits about 35 base pairs upstream. Sigma factor makes direct contact with both of these sequences in the major groove of the DNA. The AT-rich nature of the -10 element is functionally important: A-T base pairs have only two hydrogen bonds (compared to three for G-C pairs), making this region easier to melt apart — and strand separation is exactly what must happen for the polymerase to access the template strand. Once sigma recognizes the promoter, the holoenzyme forms a **closed complex** (DNA still double-stranded), then transitions to an **open complex** as the DNA around the -10 region unwinds to create a transcription bubble of roughly 12–14 base pairs.

The elegance of the sigma factor system lies in its modularity. *E. coli* has seven different sigma factors, each recognizing a distinct set of promoter sequences. The primary sigma factor, **σ⁷⁰**, drives transcription of housekeeping genes — the thousands of genes needed for routine growth and metabolism. But when the cell faces environmental stress, alternative sigma factors take over. **σ³²** (RpoH) is stabilized during heat shock and redirects polymerase to promoters controlling chaperones and proteases. **σ⁵⁴** (RpoN) recognizes a completely different promoter architecture (with a -24/-12 element instead of -35/-10) and requires an activator protein to catalyze open complex formation. **σˢ** (RpoS) accumulates during stationary phase and starvation, redirecting transcription toward stress survival genes. Because all sigma factors compete for the same limited pool of core polymerase, increasing the concentration of one sigma factor effectively reprograms the cell's entire transcriptional output — a simple but powerful form of global gene regulation.

After the holoenzyme synthesizes approximately 8–10 nucleotides of RNA, the sigma factor's grip on the promoter weakens and it **dissociates**, leaving the core polymerase to continue elongation on its own. The released sigma factor is then free to associate with another core polymerase and initiate transcription at a new promoter. This recycling mechanism means the cell needs far fewer sigma factors than polymerase molecules — sigma acts catalytically with respect to initiation events. The entire system illustrates a recurring theme in prokaryotic biology: achieving regulatory sophistication through combinatorial use of a small number of interchangeable parts rather than through the elaborate multiprotein assemblies characteristic of eukaryotic transcription.
