---
id: bacterial-conjugation-dna-transfer
title: Bacterial Conjugation and DNA Transfer
domain: biology
course: microbiology
prerequisites:
- id: bacterial-conjugation-plasmid-transfer
  type: hard
- id: bacterial-plasmids-and-extrachromosomal-elements
  type: soft
builds-toward:
- antibiotic-resistance-genetic-mechanisms
tags:
- conjugation
- dna-transfer
- mating
stage: advanced
status: validated
---

# Bacterial Conjugation and DNA Transfer

## Core Idea
Conjugation involves direct cell-to-cell contact via a pilus to transfer plasmids or chromosomal DNA. The donor synthesizes a complementary strand and pumps single-stranded DNA through the pore. This process disseminates antibiotic resistance genes globally and is a major driver of bacterial genetic diversity and pathogenesis.

## Questions

```yaml
- question: "A researcher chemically blocks pilus retraction in donor F⁺ bacteria. The pilus extends and contacts recipient F⁻ cells, but the two cells never pull into close apposition. No plasmid transfer occurs. What does this experiment reveal about the pilus's role in conjugation?"
  type: multiple-choice
  options:
    - "The pilus directly threads DNA into the recipient; blocking retraction therefore blocks DNA transfer"
    - "The pilus must retract to bring cells into contact for mating-channel formation — without stable contact, the transferosome cannot form and DNA transfer cannot occur"
    - "Pilus retraction activates relaxase; without retraction, the oriT nick never forms"
    - "The pilus carries plasmid DNA on its outer surface, and blocking retraction prevents this surface DNA from entering the recipient"
  answer: 1
  explanation: "This is the key misconception to avoid: DNA does not travel through the pilus. The pilus functions as a grappling hook — it extends, contacts the recipient, retracts to pull the cells into stable physical proximity, and the actual DNA transfer occurs through a separate membrane channel called the transferosome. Blocking retraction prevents stable mating-pair formation, which is why no transfer occurs — not because the pilus itself carries DNA. This distinction matters for understanding why pilus-inhibiting strategies are being explored as ways to block resistance spread."

- question: "After conjugation between an F⁺ donor and an F⁻ recipient, the recipient becomes F⁺ and is itself capable of donating to other F⁻ cells. Why is this property particularly dangerous from a public health perspective?"
  type: multiple-choice
  options:
    - "F⁺ cells divide faster than F⁻ cells, giving them a growth advantage"
    - "Each transfer event creates a new donor, enabling exponential spread of resistance plasmids through a bacterial population from a single initial donor cell"
    - "F⁺ cells produce toxins that kill F⁻ competitors, creating antibiotic-like selection pressure"
    - "The plasmid mutates during each transfer, generating increasingly resistant variants"
  answer: 1
  explanation: "The epidemiological danger of conjugation lies in this exponential amplification. A single F⁺ donor in a susceptible F⁻ population can initiate a cascade: one donor produces one new donor, which produces another, and so on. In dense bacterial populations (gut microbiome, hospital environments), a resistance plasmid can sweep through a community in hours. This contrasts with vertical transmission (parent to daughter cell), where resistance spreads only as fast as the resistant cells divide. Horizontal transfer through conjugation is why resistance genes spread across species barriers and why a new resistance mechanism can appear globally within years of a novel antibiotic's deployment."

- question: "In bacterial conjugation, DNA transfer occurs through the pilus itself — the hollow channel within the pilus filament is the conduit through which single-stranded DNA passes into the recipient."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The pilus serves a mechanical role: it extends to contact the recipient, then retracts to pull the cells into stable apposition. DNA transfer occurs through a separate protein channel — the transferosome — formed at the junction between the two cell membranes. The pilus is a grappling hook, not a pipeline. Experimental evidence includes the observation that pilus-mediated contact can be disrupted without affecting transferosome function, and that some conjugation systems form stable mating pairs through direct membrane contact without pili."

- question: "In an Hfr conjugation experiment, only genes located near the integrated origin of transfer (oriT) are reliably transferred to recipient cells, because mating pairs typically separate before the entire chromosome is transmitted."
  type: true-false
  answer: true
  explanation: "Hfr strains form when a conjugative plasmid integrates into the bacterial chromosome. When the Hfr cell mates, the chromosome begins transferring starting from the integrated oriT, threading through the transferosome in sequence. Complete transfer of the E. coli chromosome would take about 100 minutes, but mating pairs typically remain stable for only a fraction of that time. Genes close to the integration site transfer early and reliably; distal genes transfer rarely or never. This property was exploited historically in interrupted mating experiments to map the order of genes on the bacterial chromosome — a powerful technique before DNA sequencing."

- question: "Describe the molecular events from pilus contact to completion of plasmid transfer in conjugation. How do both donor and recipient end up with a complete double-stranded copy of the plasmid?"
  type: short-answer
  answer: "The pilus extends from the donor, contacts the recipient, and retracts to pull the cells into stable apposition, forming a membrane channel (transferosome). A relaxase enzyme nicks one strand of the plasmid at the origin of transfer (oriT), covalently attaches to the 5' end of the nicked strand, and unwinds it. A coupling protein pumps this single strand 5'→3' through the transferosome into the recipient. Simultaneously, DNA polymerase in both cells synthesizes the complementary strand: the donor uses the remaining intact strand as a template to restore its double-stranded plasmid, while the recipient uses the incoming single strand as a template to synthesize its complementary strand. Both cells end up with a complete double-stranded plasmid, and the recipient becomes F⁺."
  explanation: "The rolling-circle replication mechanism is the key to understanding why both cells get complete copies. The donor doesn't 'give away' its plasmid — it copies one strand out while simultaneously replacing it. The recipient receives a single strand and completes it locally. This mechanism is also why transfer is inherently directional and strand-specific: the relaxase nicks a specific strand at oriT and that same strand is always the one transferred, ensuring the correct sequence enters the recipient."
```

## Explainer

You already understand that bacteria carry plasmids — small, self-replicating DNA circles — and that conjugation is one mechanism for transferring them between cells. Here we examine the molecular machinery and broader implications of conjugative DNA transfer in detail, because this process is the single most important driver of antibiotic resistance spread across bacterial populations.

The process begins with a **donor cell** (designated F⁺ or Hfr) that carries a conjugative plasmid encoding the genes for transfer machinery. The first visible step is the extension of a **sex pilus** — a long, hollow protein filament assembled from pilin subunits — that makes contact with a **recipient cell** (F⁻). The pilus then retracts, pulling the two cells into direct contact and forming a stable **mating pair** connected by a membrane channel called the **transferosome**. Think of the pilus as a grappling hook: it finds the target and reels it in, but the actual DNA transfer occurs through the channel formed at the junction, not through the pilus itself.

Once stable contact is established, a **relaxase** enzyme nicks one strand of the plasmid at a specific sequence called the **origin of transfer (oriT)**. The nicked single strand is then unwound and threaded 5′-to-3′ through the transferosome into the recipient cell, powered by a coupling protein that acts as a molecular pump. Simultaneously, both cells use DNA polymerase to synthesize the complementary strand — the donor rebuilds its double-stranded plasmid, and the recipient converts the incoming single strand into a complete double-stranded plasmid. The result: both cells now carry the plasmid, and the former F⁻ recipient becomes F⁺, capable of donating to other cells. This exponential spread is what makes conjugation so epidemiologically dangerous — a single resistance plasmid entering a bacterial population can sweep through it rapidly.

A special case occurs when the conjugative plasmid integrates into the bacterial chromosome, creating an **Hfr (high-frequency recombination) strain**. When an Hfr cell conjugates, it begins transferring chromosomal DNA starting from the integrated oriT. Because the entire chromosome takes about 100 minutes to transfer in *E. coli*, and mating pairs rarely remain stable that long, only genes close to the integration site typically make it across. The transferred chromosomal DNA can then recombine with the recipient's chromosome, introducing new alleles. This mechanism was historically used in interrupted mating experiments to map bacterial genes by their order of transfer. Conjugation can cross species barriers — even transferring DNA between gram-negative and gram-positive bacteria or from bacteria to yeast — making it a powerful force for horizontal gene flow across the microbial world.
