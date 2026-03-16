---
id: major-histocompatibility-complex
title: Major Histocompatibility Complex Structure and Function
domain: biology
course: immunology
prerequisites:
- id: protein-structure-and-function
  type: hard
- id: cell-signaling-intro
  type: soft
builds-toward:
- mhc-class-i-presentation
- mhc-class-ii-presentation
tags:
- mhc
- antigen-presentation
- hla
stage: advanced
status: draft
---

# Major Histocompatibility Complex Structure and Function

## Core Idea
The major histocompatibility complex (MHC) molecules present peptide antigens to T cells, controlling adaptive immune responses. MHC Class I (α-chain + β2-microglobulin) displays intracellular peptides to CD8+ T cells and is expressed on all nucleated cells. MHC Class II (α + β heterodimer) displays endosomal peptides to CD4+ T cells and is expressed on antigen-presenting cells. MHC polymorphism among individuals ensures population-level pathogen recognition diversity.

## How It's Best Learned
Sketch the three-dimensional MHC-peptide complex showing the peptide-binding groove, anchor residues, and TCR contact surfaces. Compare MHC-I and MHC-II peptide binding pockets and binding preferences.

## Common Misconceptions
- All MHC molecules bind the same peptides (peptide-binding specificity varies with MHC allotype). - MHC-I is only on immune cells (all nucleated cells express MHC-I).

## Explainer

From your study of protein structure, you know that the three-dimensional shape of a protein determines its function and binding specificity. From cell signaling, you know that surface receptors allow cells to communicate information about their internal state. The **major histocompatibility complex (MHC)** molecules combine both principles: they are cell-surface proteins whose sole job is to display short peptide fragments — molecular snapshots of what is happening inside the cell — for inspection by T cells. Without MHC, T cells would be blind to intracellular infections, cancers, and foreign proteins, because T cell receptors cannot recognize free-floating antigens the way antibodies can.

**MHC class I** molecules are expressed on virtually all nucleated cells in the body. They consist of a transmembrane **α chain** with three extracellular domains (α1, α2, α3) non-covalently associated with **β2-microglobulin**, a small soluble protein. The α1 and α2 domains form a **peptide-binding groove** — a cleft with a floor of β-pleated sheet and walls of α-helices — that holds peptides of 8–10 amino acids. These peptides are derived from proteins degraded by the **proteasome** in the cytoplasm: normal self-proteins, viral proteins if the cell is infected, or mutant proteins in cancer cells. The loaded MHC-I complex is then transported to the cell surface, where **CD8+ cytotoxic T cells** survey it. If the displayed peptide is foreign (viral, for example), the CD8+ T cell kills the presenting cell. This system means that every nucleated cell in your body is continuously displaying a sample of its internal protein content for immune surveillance — a cellular "inspection window" that reveals infection or transformation.

**MHC class II** molecules have a different structure and a different job. They are heterodimers of an **α chain** and a **β chain**, each contributing one domain to form the peptide-binding groove. Unlike MHC-I, the groove is open at both ends, accommodating longer peptides of 13–25 amino acids. MHC-II expression is restricted to professional **antigen-presenting cells** — dendritic cells, macrophages, and B cells — rather than all nucleated cells. These cells capture extracellular pathogens and proteins through phagocytosis or receptor-mediated endocytosis, degrade them in acidic endosomal compartments, and load the resulting peptides onto MHC-II molecules. The MHC-II–peptide complexes are presented to **CD4+ helper T cells**, which then orchestrate the broader immune response by activating B cells, macrophages, and other effectors.

The most remarkable feature of MHC is its **polymorphism** — the MHC genes (called **HLA** in humans) are the most genetically variable loci in the human genome, with thousands of alleles in the population. Each allelic variant encodes a slightly different peptide-binding groove with different anchor residue preferences, meaning different MHC alleles present different subsets of peptides from the same pathogen. This diversity operates at the population level: a pathogen that evolves to avoid presentation by one person's MHC alleles will still be presented by someone else's. This is why MHC matching is critical for organ transplantation — the recipient's T cells recognize donor MHC molecules as foreign and attack the graft — and why populations with greater MHC diversity tend to be more resilient against epidemic pathogens.
