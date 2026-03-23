---
id: rna-splicing-introns-exons-spliceosome
title: RNA Splicing, Introns, Exons, and the Spliceosome
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: rna-5-capping-polyadenylation
  type: hard
- id: rna-splicing-mechanisms
  type: soft
builds-toward:
- alternative-rna-splicing
- rna-processing
tags:
- splicing
- introns
- exons
- spliceosome
- rna-processing
stage: formal-systems
status: draft
---

# RNA Splicing, Introns, Exons, and the Spliceosome

## Core Idea
Pre-mRNA contains exons (coding sequences) and introns (non-coding sequences). The spliceosome, a complex of small RNAs and proteins, catalyzes two transesterification reactions that remove introns and join exons. Splice sites (GU-AG rule) define intron boundaries, and spliceosome assembly occurs co-transcriptionally.

## How It's Best Learned
Diagram the two-step splicing mechanism: attack of the 2'-OH of branch-point adenine on the 5' splice site, followed by attack of the released 5' exon on the 3' splice site. Align sequences to identify conserved splice sites and branch points in different organisms.

## Common Misconceptions
- Assuming introns are removed completely and leave no trace; they are retained in some genes and have regulatory functions.
- Not recognizing that spliceosome components are themselves RNAs that catalyze the reaction, not just proteins.
- Thinking splicing is an error to be avoided rather than a regulated, essential process.

## Questions

```yaml
- question: "A point mutation changes the first two nucleotides of an intron from GU to AU. What is the most likely consequence for the mRNA produced from this gene?"
  type: multiple-choice
  options:
    - "Splicing proceeds normally, because the spliceosome recognizes introns by their internal sequences, not the terminal dinucleotides"
    - "The intron is retained in the mature mRNA, disrupting the reading frame or introducing a premature stop codon"
    - "The spliceosome switches to an alternative 5' splice site automatically, restoring normal splicing"
    - "The poly-A tail cannot be added, preventing export of the mRNA from the nucleus"
  answer: 1
  explanation: "The GU at the 5' splice site is part of the nearly universal GU-AG rule and is essential for spliceosome recognition. The U1 snRNA base-pairs with the 5' splice site sequence; a GU→AU mutation disrupts this interaction and abolishes or severely reduces splicing at that site. The result is usually intron retention — the intron remains in the mRNA — which typically disrupts the reading frame or introduces a premature stop codon. Many human genetic diseases are caused precisely by such splice-site mutations."

- question: "What is the catalytic heart of the spliceosome, and what category of enzyme does this make it?"
  type: multiple-choice
  options:
    - "Large splicing proteins (SR proteins) that use ATP to cleave phosphodiester bonds and join exons"
    - "Small nuclear RNAs (snRNAs U1, U2, U4, U5, U6) that position reactive groups and stabilize transition states, making the spliceosome a ribozyme"
    - "RNA polymerase II, which catalyzes splicing co-transcriptionally using the same active site as transcription"
    - "The branch-point adenosine itself, which acts as a protein cofactor in the cleavage reaction"
  answer: 1
  explanation: "The spliceosome's catalytic activity resides in its snRNA components, particularly U2 and U6, which form the active site that positions the reactive groups for both transesterification steps. This makes the spliceosome a ribozyme — an RNA molecule with catalytic activity. The associated proteins facilitate assembly, remodeling, and fidelity, but the chemistry is RNA-catalyzed. This was a significant discovery because it challenged the assumption that all biological catalysts are proteins."

- question: "The two chemical steps of pre-mRNA splicing — lariat formation and exon joining — are transesterification reactions that do not require energy input from ATP hydrolysis because each step breaks one phosphodiester bond while forming another."
  type: true-false
  answer: true
  explanation: "Transesterification exchanges one phosphoester linkage for another, keeping the total number of high-energy bonds constant. No net energy input or output is required for the chemical steps themselves. The energy balance is approximately neutral because a phosphodiester bond is broken and a new one is formed. Note that the spliceosome does require ATP hydrolysis by DEAD-box helicases to drive conformational rearrangements during assembly and activation, but the splicing chemistry itself — the two nucleophilic attacks — is energetically neutral."

- question: "Introns are biologically inert 'junk sequences' that serve no function and are completely degraded immediately after removal from the pre-mRNA."
  type: true-false
  answer: false
  explanation: "This is a significant misconception. Many intron sequences have important regulatory functions: they harbor enhancers, silencers, and noncoding RNA genes (microRNAs, snoRNAs, lncRNAs often encoded within introns). Some introns are retained in the mature transcript as a form of gene regulation (intron retention). The capacity for alternative splicing — choosing which exons to include — is only possible because introns define the boundaries between exonic modules; this is how ~20,000 genes produce >100,000 protein isoforms. Introns are also evolutionarily useful as units that can be shuffled between genes (exon shuffling)."

- question: "Why does the co-transcriptional nature of splicing matter for gene expression regulation?"
  type: short-answer
  answer: "Because splicing occurs while RNA polymerase II is still elongating the pre-mRNA, the cell can regulate splice site choices in response to cellular signals before the transcript is complete. The C-terminal domain of RNA Pol II recruits splicing factors to the nascent transcript, and transcription elongation rate influences which splice sites are recognized — slower elongation gives the spliceosome more time to commit to upstream splice sites. This coupling enables alternative splicing: different exons can be included or skipped depending on which splicing factors are present, allowing the same gene to produce different mRNAs in different cell types, developmental stages, or conditions."
  explanation: "Co-transcriptional splicing is what makes alternative splicing possible at scale. The ~94% of multi-exon human genes that undergo alternative splicing owe that capacity to the tight coupling between transcription and spliceosome assembly. This is why the human genome, with ~20,000 protein-coding genes, can produce a proteome of over 100,000 distinct protein variants — each gene is a modular toolkit, not a single blueprint."
```

## Explainer

From your work on RNA processing, you know that the pre-mRNA transcript emerging from RNA polymerase II is not yet ready for translation — it needs a 5' cap, a poly-A tail, and the removal of internal sequences that do not code for protein. Those non-coding internal sequences are **introns**, and the protein-coding segments that flank them are **exons**. Splicing is the process that precisely removes every intron and stitches the exons together into a continuous open reading frame. In human genes, introns often vastly outnumber and outsize exons — the dystrophin gene, for instance, spans 2.4 million base pairs but produces an mRNA of only about 14,000 nucleotides.

The molecular machine that performs splicing is the **spliceosome**, a massive complex assembled from five small nuclear RNAs (snRNAs: U1, U2, U4, U5, U6) and over 100 associated proteins. Unlike what you might expect, the catalytic heart of the spliceosome is RNA, not protein — the snRNAs position the reactive groups and stabilize the transition states, making the spliceosome a **ribozyme**. The spliceosome recognizes each intron through three conserved sequence elements: a **5' splice site** (nearly always starting with GU), a **3' splice site** (nearly always ending with AG), and a **branch point** adenosine located 18–40 nucleotides upstream of the 3' splice site. This GU-AG rule is so consistent that mutations at these positions almost always abolish splicing and cause disease.

Splicing proceeds through exactly two **transesterification** reactions — phosphoester bond exchanges that require no external energy input. In the first step, the 2'-hydroxyl of the branch-point adenosine attacks the phosphodiester bond at the 5' splice site. This cuts the RNA at that junction and creates a **lariat** structure: a looped intron connected by an unusual 2'-5' phosphodiester bond. In the second step, the now-free 3'-hydroxyl of the upstream exon attacks the phosphodiester bond at the 3' splice site, simultaneously joining the two exons and releasing the intron lariat. The lariat is then debranched and degraded, while the joined exons form the mature mRNA.

A critical feature of this process is that splicing occurs **co-transcriptionally** — the spliceosome assembles on the pre-mRNA while RNA polymerase II is still elongating downstream. This coupling is coordinated through the C-terminal domain of the polymerase, which recruits splicing factors to the emerging transcript. Because splicing happens before transcription is complete, the cell can regulate gene expression at the splicing level, choosing which exons to include or skip. This capacity for **alternative splicing** — which builds on the mechanism you are learning here — is why the human genome encodes roughly 20,000 genes but produces well over 100,000 distinct protein variants.
