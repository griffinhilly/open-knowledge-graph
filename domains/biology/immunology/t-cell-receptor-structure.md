---
id: t-cell-receptor-structure
title: T Cell Receptor Structure and Recognition
domain: biology
course: immunology
prerequisites:
- id: adaptive-immunity-overview
  type: hard
- id: cell-signaling-intro
  type: hard
- id: protein-secondary-structure
  type: soft
builds-toward:
- t-cell-activation-costimulation
- antigen-presentation-mechanisms
tags:
- adaptive
- t-cell
- receptor
- recognition
stage: advanced
status: draft
---

# T Cell Receptor Structure and Recognition

## Core Idea
The T cell receptor (TCR) is a heterodimer of α and β chains (or γ and δ) that recognizes peptide bound to MHC via its variable domains. TCR diversity comes from V(D)J recombination of segment genes. CD4 and CD8 coreceptors stabilize TCR-MHC binding by recognizing conserved MHC regions.

## Explainer

You already know from adaptive immunity that T cells recognize specific antigens, and from cell signaling that receptors translate extracellular information into intracellular responses. The **T cell receptor (TCR)** is the molecule that makes antigen-specific recognition possible for the entire T cell arm of adaptive immunity. Unlike antibodies, which can bind free-floating antigens directly, the TCR can only recognize antigen that has been processed into a short peptide and presented on the surface of another cell by an MHC molecule. This restriction — called **MHC restriction** — means T cells always inspect what other cells are displaying, never raw pathogens in solution.

Structurally, most TCRs are **αβ heterodimers**: two different protein chains (alpha and beta), each with a variable region and a constant region, linked by a disulfide bond. The variable regions sit at the top of the molecule and form the **antigen-binding site**, which contacts both the peptide fragment and the walls of the MHC groove simultaneously. Think of it like a hand gripping a hotdog in a bun — the TCR "fingers" touch both the peptide (hotdog) and the MHC molecule (bun). A smaller population of T cells carries **γδ TCRs** instead, which recognize antigens through less well-understood mechanisms and often respond to non-peptide molecules without classical MHC presentation.

The enormous diversity of TCR binding specificities — estimated at over 10^15 possible combinations — comes from **V(D)J recombination**, a process you encountered with antibody diversity. During T cell development in the thymus, gene segments (Variable, Diversity, and Joining) are randomly cut and rejoined to assemble unique α and β chain genes. Additional diversity is introduced at the junctions between segments through random nucleotide additions and deletions. Each mature T cell ends up with a single, unique TCR specificity — one lock looking for one particular peptide-MHC key.

The TCR itself has very short cytoplasmic tails and cannot signal on its own. Instead, it associates with a cluster of signaling proteins called the **CD3 complex** (composed of γε, δε, and ζζ dimers), which contain **immunoreceptor tyrosine-based activation motifs (ITAMs)** in their cytoplasmic domains. When the TCR engages peptide-MHC, conformational changes in CD3 allow kinases to phosphorylate these ITAMs, initiating the signaling cascade that activates the T cell. Additionally, **coreceptors CD4 and CD8** bind to conserved regions of MHC class II and MHC class I molecules, respectively. These coreceptors stabilize the TCR-MHC interaction and recruit the kinase Lck to the CD3 ITAMs, dramatically increasing signaling efficiency. This is why CD4+ T cells respond to MHC II (on antigen-presenting cells) and CD8+ T cells respond to MHC I (on virtually all nucleated cells) — the coreceptor determines which class of MHC a T cell can productively engage.
