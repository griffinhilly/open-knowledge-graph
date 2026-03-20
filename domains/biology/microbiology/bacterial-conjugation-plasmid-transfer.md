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
builds-toward:
- antibiotic-resistance-mutations-downregulation
- horizontal-gene-transfer
tags:
- conjugation
- plasmids
- gene-transfer
stage: advanced
status: draft
---

# Bacterial Conjugation and Plasmid Transfer

## Core Idea
Conjugation is a direct contact-dependent mechanism of bacterial DNA transfer mediated by F (fertility) plasmids that encode F pili and conjugation apparatus proteins. The donor cell forms a mating pair with a recipient via pilus, and the plasmid DNA is replicated and transferred while maintaining a copy in the donor, enabling rapid spread of genes including antibiotic resistance.

## Explainer

From your study of microbial genetics, you know that bacteria reproduce asexually by binary fission — each daughter cell is a genetic clone of the parent. This means that without some mechanism for acquiring new genes, bacterial populations would evolve only through random mutation. **Conjugation** is the most important mechanism bacteria use to share genes laterally — directly from one living cell to another — and it is the primary reason antibiotic resistance can spread so rapidly through bacterial populations.

The process begins with the **F plasmid** (fertility factor), a circular piece of DNA separate from the bacterial chromosome. The F plasmid carries genes encoding the **F pilus** — the long, filamentous appendage you may have encountered in your study of bacterial surface structures — as well as all the machinery needed for DNA transfer. A cell carrying the F plasmid is designated **F+** (the donor), while a cell lacking it is **F−** (the recipient). The F pilus extends from the donor and binds to receptors on the F− cell surface, then retracts, pulling the two cells into direct contact and forming a **mating bridge** — a channel through which DNA can pass.

Once the mating pair is established, one strand of the F plasmid is nicked at a specific site called the **origin of transfer** (oriT). That single strand is threaded into the recipient cell while **rolling circle replication** simultaneously synthesizes a replacement strand in the donor. The recipient cell then synthesizes the complementary strand to its received single strand, reconstituting a complete double-stranded F plasmid. The result: both cells are now F+, and the new donor can immediately conjugate with other F− cells. This exponential spread is what makes conjugation so powerful — a single resistance plasmid introduced into a bacterial population can sweep through it in hours.

The clinical significance is enormous. Many antibiotic resistance genes reside on conjugative plasmids — often on **R plasmids** (resistance plasmids) that carry multiple resistance determinants simultaneously. A single conjugation event can transfer resistance to several antibiotics at once. Even more dramatically, when the F plasmid integrates into the bacterial chromosome (creating an **Hfr** strain, for "high frequency of recombination"), conjugation can transfer chromosomal genes to recipients, potentially spreading virulence factors and metabolic capabilities across species boundaries. This is why conjugation is a central concern in hospital-acquired infections: resistant organisms sharing plasmids in clinical settings can render entire classes of antibiotics ineffective within a remarkably short time.
