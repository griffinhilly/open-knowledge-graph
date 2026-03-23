---
id: nucleosome-positioning-dynamics
title: Nucleosome Positioning and Occupancy Dynamics
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: nucleosomal-core-particle-structure
  type: hard
- id: chromatin-fiber-higher-order-structure
  type: hard
builds-toward:
- chromatin-accessibility-and-remodeling-complexes
tags:
- nucleosome-positioning
- chromatin-organization
- nucleosome-occupancy
- gene-activation
stage: formal-systems
status: draft
---

# Nucleosome Positioning and Occupancy Dynamics

## Core Idea
Nucleosome positioning is not random but determined by DNA sequence preferences, histone-DNA binding energy, and chromatin remodeling factor activity. Promoter regions typically have nucleosome-depleted regions upstream of the transcription start site, while gene bodies display periodic nucleosome spacing. Nucleosome positioning is dynamic: nucleosomes are displaced during transcription initiation and rapidly reassembled afterward, and dynamic repositioning regulates access to regulatory DNA.

## Questions

```yaml
- question: "MNase-seq data shows that a gene promoter has a well-defined nucleosome-depleted region (NDR) flanked by positioned −1 and +1 nucleosomes when the gene is active. When a signaling pathway silences the gene, an MNase-resistant protected fragment now appears in the NDR. What is the most likely interpretation?"
  type: multiple-choice
  options:
    - "A random fluctuation in nucleosome assembly that coincidentally correlates with silencing"
    - "A technical artifact caused by incomplete MNase digestion of the silenced chromatin"
    - "Active repositioning of a nucleosome into the NDR to occlude transcription factor binding sites and block transcription initiation"
    - "DNA methylation within the NDR preventing nucleosome binding"
  answer: 2
  explanation: "The NDR is an actively maintained open space, not a passive default. When a gene is silenced, chromatin remodeling complexes can slide or deposit nucleosomes into the previously depleted region, physically occluding the DNA sequences where transcription factors and RNA polymerase would otherwise bind. This is a primary mechanism of gene silencing — not just the absence of activator binding, but the active covering of regulatory sequences by nucleosomes. The appearance of a new protected fragment in the NDR is direct structural evidence of this repositioning, not a technical artifact."

- question: "A researcher mutates a yeast promoter's nucleosome-depleted region by replacing its poly(dA:dT) tracts with alternating AT dinucleotides (A/T every 10 bp). Compared to wild-type, what would you most likely observe at this promoter?"
  type: multiple-choice
  options:
    - "No effect — nucleosome positioning is determined entirely by remodeling complexes, not DNA sequence"
    - "The NDR widens because poly(dA:dT) tracts normally anchor the −1 nucleosome at the boundary"
    - "Increased nucleosome occupancy at the promoter, since alternating AT dinucleotides every 10 bp favor DNA bending around the histone octamer"
    - "Loss of the +1 nucleosome only, since only gene-body nucleosome positioning depends on sequence"
  answer: 2
  explanation: "DNA sequence is one of three factors determining nucleosome positioning. Poly(dA:dT) tracts are intrinsically stiff and resist bending around the histone octamer — they are nucleosome-excluding sequences that contribute to the NDR. Replacing them with A/T dinucleotides spaced every 10 bp (the helical repeat) creates a sequence that curves naturally around the octamer, dramatically favoring nucleosome formation at that location. The result is that the previously open NDR becomes occupied, reducing transcription factor access. This shows that DNA sequence preferences, while not the only determinant, make a real and predictable contribution."

- question: "In gene bodies (downstream of the transcription start site), nucleosomes are randomly distributed with no consistent spatial relationship to one another or to the +1 nucleosome."
  type: true-false
  answer: false
  explanation: "Gene bodies actually display a highly ordered, regularly spaced nucleosome array. The +1 nucleosome — the first downstream of the NDR — serves as a reference point from which subsequent nucleosomes are spaced at regular intervals (approximately 180–200 bp center-to-center in most eukaryotes). This phased array is actively established and maintained by ATP-dependent remodeling complexes (particularly ISWI-family complexes) that use the +1 nucleosome as an anchor and space subsequent nucleosomes at regular intervals 'like dominoes.' The regularity breaks down toward the 3' end of long genes as polymerase passage disrupts the array."

- question: "During active transcription, RNA polymerase II must traverse nucleosome-covered gene body DNA. Histone chaperones partially disassemble nucleosomes ahead of the elongating polymerase and reassemble them behind it."
  type: true-false
  answer: true
  explanation: "This is the 'nucleosome wave' or 'histone transfer' model of transcription elongation. Nucleosomes in the gene body are not permanent obstacles — they are transiently disrupted as the polymerase passes. FACT (Facilitates Chromatin Transcription) and other histone chaperones coordinate this: they accept histones displaced ahead of the polymerase and redeposit them behind it. This maintains chromatin integrity in the wake of the polymerase, preventing runaway transcription from cryptic start sites that would be exposed if nucleosomes were simply evicted. The dynamic nature of nucleosomes during elongation is as important as their positioning at promoters for regulating gene expression."

- question: "Why does the cell require active, ATP-dependent mechanisms to maintain the nucleosome-depleted region at active promoters, rather than simply relying on DNA sequence to passively keep promoters open?"
  type: short-answer
  answer: "DNA sequence provides a thermodynamic preference — poly(dA:dT) tracts resist wrapping around the histone octamer — but this preference is only partial and probabilistic. Nucleosomes can still occupy these sequences at some frequency, driven by the entropic tendency to fill available DNA and by competition from other nucleosomes pushing in from flanking positions. Additionally, transcription factors and other regulatory proteins constantly compete with histones for binding to promoter sequences. Active ATP-dependent remodeling complexes are needed to continuously evict nucleosomes that reassemble at the NDR, establish the precise boundaries of the depleted region, and respond to signaling inputs that change the cell's transcriptional program. Without ongoing remodeling activity, the NDR would gradually fill in, reducing transcription factor access."
  explanation: "The key insight is that nucleosome positioning reflects a dynamic equilibrium, not a static structural feature. The NDR is not simply an empty space — it is the outcome of a balance between spontaneous nucleosome assembly (thermodynamically favored because DNA wrapping stabilizes the octamer) and active eviction/exclusion by remodeling complexes and competing DNA-binding proteins. When remodeling activity is disrupted — for example, by inactivating SWI/SNF or RSC — promoter NDRs fill in even at sequence-disfavoring locations, demonstrating that active machinery is essential to maintain open chromatin."
```

## Explainer

From your study of nucleosome structure, you know that each nucleosome consists of approximately 147 base pairs of DNA wrapped around a histone octamer, and that nucleosomes are the fundamental repeating unit of chromatin. But knowing the structure raises a critical question: *where* along the genome do nucleosomes sit? If nucleosomes were positioned randomly, every stretch of DNA would be equally accessible. In reality, nucleosome positioning is highly regulated, and it profoundly determines which genes can be read and which are locked away.

Three factors determine where nucleosomes form. First, **DNA sequence preferences**: DNA does not bend equally well everywhere. Sequences with regularly spaced A/T dinucleotides every ~10 base pairs (matching the helical repeat) curve naturally around the histone octamer and form stable nucleosomes, while stiff poly(dA:dT) tracts resist wrapping and tend to exclude nucleosomes. Second, **ATP-dependent chromatin remodeling complexes** — enzymes like SWI/SNF, ISWI, and RSC — actively slide, eject, or restructure nucleosomes, overriding sequence preferences when the cell needs to change access patterns. Third, **competition from other DNA-binding proteins**: transcription factors and the transcription machinery itself can displace nucleosomes or prevent their reassembly at specific locations.

The most functionally important positioning feature is the **nucleosome-depleted region (NDR)** found at most active promoters. In yeast and other eukaryotes, a gap of roughly 150–200 base pairs immediately upstream of the transcription start site is kept clear of nucleosomes, flanked by well-positioned nucleosomes called the **−1 and +1 nucleosomes**. The NDR provides an open landing pad where transcription factors and RNA polymerase can access the DNA. Downstream into the gene body, nucleosomes are arranged in a regular, evenly spaced array — each positioned relative to the +1 nucleosome like dominoes set at fixed intervals. This ordered arrangement is established by remodeling complexes that use the +1 nucleosome as an anchor and space subsequent nucleosomes at regular intervals.

Nucleosome positioning is not static — it is **dynamically regulated** in response to cellular signals. When a gene is activated, remodeling complexes evict or slide nucleosomes away from the promoter to expose transcription factor binding sites. During transcription elongation, RNA polymerase must plow through nucleosomes in the gene body; histone chaperones partially disassemble nucleosomes ahead of the polymerase and reassemble them behind it, maintaining chromatin integrity while permitting transcription. When a gene is silenced, nucleosomes are repositioned to cover the promoter and block access. This constant reshuffling means that nucleosome positions represent a dynamic equilibrium between assembly and disassembly forces, and shifts in that equilibrium are a primary mechanism by which cells turn genes on and off.
