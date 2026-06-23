---
id: bacterial-conjugation-plasmid-transfer
title: Bacterial Conjugation and Plasmid Transfer
domain: biology
course: microbiology
prerequisites:
- id: microbial-genetics-overview
  type: hard
- id: bacterial-pili-fimbriae-types
  type: soft
- id: bacterial-plasmids-and-extrachromosomal-elements
  type: hard
builds-toward:
- antibiotic-resistance-mutations-downregulation
- horizontal-gene-transfer
tags:
- conjugation
- plasmids
- gene-transfer
stage: advanced
status: validated
---

# Bacterial Conjugation and Plasmid Transfer

## Core Idea
Conjugation is a direct contact-dependent mechanism of bacterial DNA transfer mediated by F (fertility) plasmids that encode F pili and conjugation apparatus proteins. The donor cell forms a mating pair with a recipient via pilus, and the plasmid DNA is replicated and transferred while maintaining a copy in the donor, enabling rapid spread of genes including antibiotic resistance.

## Questions

```yaml
- question: "A single F+ bacterium is introduced into a culture of 10,000 F− bacteria. Assuming optimal conditions for conjugation, what is expected after several hours?"
  type: multiple-choice
  options:
    - "About 50% of cells become F+, as the donor's resources limit how many transfers it can perform"
    - "Nearly all cells become F+, because each newly converted F+ cell can immediately conjugate with remaining F− cells, enabling exponential spread"
    - "Only cells that directly contacted the original donor become F+; newly converted cells cannot yet conjugate"
    - "The original donor loses its F plasmid after the first transfer and becomes F−"
  answer: 1
  explanation: "The key is that conjugation transfers a COPY of the F plasmid — the donor retains its own copy. This means the donor cell can conjugate repeatedly, and more importantly, every new F+ recipient becomes a donor capable of spreading the plasmid further. The spread is exponential: one becomes two donors, two become four, and so on. Option 3 reflects the misconception that newly converted cells need time before they can conjugate — in fact, they can conjugate immediately once they carry the F plasmid. Option 3 also misunderstands rolling circle replication."

- question: "After a successful conjugation event, what happens to the F plasmid in the original donor cell?"
  type: multiple-choice
  options:
    - "It is destroyed — the nicking at oriT permanently inactivates the donor's plasmid"
    - "It is halved — each cell receives one strand of the original double-stranded plasmid"
    - "It is maintained intact — rolling circle replication synthesizes a new complementary strand in the donor as the other strand is transferred"
    - "It integrates into the chromosome — the donor becomes an Hfr strain after every transfer"
  answer: 2
  explanation: "Rolling circle replication is the mechanism that makes conjugation so powerful. One strand of the F plasmid is nicked at oriT and fed into the recipient, while the donor simultaneously synthesizes a replacement strand. Both cells end up with a complete double-stranded F plasmid. The donor loses nothing permanently. This is fundamentally different from chromosomal transfer in Hfr strains, and the 'halving' in option 1 confuses strand transfer with molecular splitting."

- question: "A single conjugation event involving an R (resistance) plasmid can simultaneously confer resistance to multiple antibiotics in the recipient cell."
  type: true-false
  answer: true
  explanation: "R plasmids (resistance plasmids) typically carry multiple resistance determinants organized as resistance cassettes, often within mobile genetic elements called integrons. A single transfer event copies the entire plasmid, including all resistance genes it carries. This is a critical feature of the clinical problem: conjugation can, in a single step, convert a pan-susceptible bacterium into one resistant to several antibiotic classes simultaneously — a dramatic change that would take thousands of independent mutations to achieve through chromosomal evolution."

- question: "The F pilus forms a permanent hollow tube through which double-stranded DNA is directly threaded from donor to recipient."
  type: true-false
  answer: false
  explanation: "The F pilus does not remain as a permanent channel. It makes initial contact with the F− cell surface and then retracts, pulling the two cells into direct physical contact. A mating bridge (stabilized junction between cell membranes) forms through which DNA transfer occurs. Additionally, the DNA transferred is a single strand — not double-stranded — which is synthesized as a complement by the recipient cell after transfer. The double-stranded plasmid is reconstituted in the recipient, not transferred intact."

- question: "Why is conjugation clinically more dangerous than chromosomal mutation as a mechanism for spreading antibiotic resistance in bacterial populations?"
  type: short-answer
  answer: "Conjugation is more dangerous for several reasons. First, it is horizontal — it spreads genes between unrelated bacteria (even across species boundaries) rather than only to daughter cells. Second, it is exponential — each newly converted F+ cell becomes a new donor. Third, it transfers entire functional resistance cassettes in a single event rather than accumulating point mutations one at a time. Fourth, R plasmids often carry multiple resistance genes, granting multidrug resistance in a single conjugation. Finally, it occurs in real time within hosts (including hospital settings) without requiring bacterial reproduction, so resistance can spread through a population in hours."
  explanation: "Chromosomal mutation is essentially random and slow — a single bacterium acquires one mutation, and the mutation spreads only through vertical inheritance to daughter cells. Conjugation circumvents all of this: a plasmid can jump horizontally to thousands of cells within hours, bypassing the generational bottleneck entirely. This is why the emergence and spread of resistance plasmids in hospital settings is treated as a public health emergency rather than an ordinary evolutionary phenomenon."
```

## Explainer

From your study of microbial genetics, you know that bacteria reproduce asexually by binary fission — each daughter cell is a genetic clone of the parent. This means that without some mechanism for acquiring new genes, bacterial populations would evolve only through random mutation. **Conjugation** is the most important mechanism bacteria use to share genes laterally — directly from one living cell to another — and it is the primary reason antibiotic resistance can spread so rapidly through bacterial populations.

The process begins with the **F plasmid** (fertility factor), a circular piece of DNA separate from the bacterial chromosome. The F plasmid carries genes encoding the **F pilus** — the long, filamentous appendage you may have encountered in your study of bacterial surface structures — as well as all the machinery needed for DNA transfer. A cell carrying the F plasmid is designated **F+** (the donor), while a cell lacking it is **F−** (the recipient). The F pilus extends from the donor and binds to receptors on the F− cell surface, then retracts, pulling the two cells into direct contact and forming a **mating bridge** — a channel through which DNA can pass.

Once the mating pair is established, one strand of the F plasmid is nicked at a specific site called the **origin of transfer** (oriT). That single strand is threaded into the recipient cell while **rolling circle replication** simultaneously synthesizes a replacement strand in the donor. The recipient cell then synthesizes the complementary strand to its received single strand, reconstituting a complete double-stranded F plasmid. The result: both cells are now F+, and the new donor can immediately conjugate with other F− cells. This exponential spread is what makes conjugation so powerful — a single resistance plasmid introduced into a bacterial population can sweep through it in hours.

The clinical significance is enormous. Many antibiotic resistance genes reside on conjugative plasmids — often on **R plasmids** (resistance plasmids) that carry multiple resistance determinants simultaneously. A single conjugation event can transfer resistance to several antibiotics at once. Even more dramatically, when the F plasmid integrates into the bacterial chromosome (creating an **Hfr** strain, for "high frequency of recombination"), conjugation can transfer chromosomal genes to recipients, potentially spreading virulence factors and metabolic capabilities across species boundaries. This is why conjugation is a central concern in hospital-acquired infections: resistant organisms sharing plasmids in clinical settings can render entire classes of antibiotics ineffective within a remarkably short time.
