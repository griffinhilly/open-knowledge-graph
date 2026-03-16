---
id: mhc-structure-function
title: Major Histocompatibility Complex Structure and Function
domain: biology
course: immunology
prerequisites:
- id: adaptive-immunity-overview
  type: hard
- id: cell-membrane-structure
  type: hard
- id: protein-tertiary-structure
  type: soft
builds-toward:
- antigen-presentation-mechanisms
- t-cell-development-thymic-selection
tags:
- adaptive
- antigen-presentation
- mhc
stage: advanced
status: draft
---

# Major Histocompatibility Complex Structure and Function

## Core Idea
The major histocompatibility complex displays intracellular and extracellular peptides on cell surfaces for recognition by T cells. MHC-I molecules (on all nucleated cells) present intracellular peptides to CD8+ T cells. MHC-II molecules (on antigen-presenting cells) present exogenous peptides to CD4+ T cells. MHC polymorphism ensures population-level diversity in pathogen recognition.

## Explainer

From your study of adaptive immunity, you know that T cells cannot recognize free-floating proteins — they can only detect short peptide fragments displayed on cell surfaces. The **major histocompatibility complex (MHC)** molecules are the display platform that makes this recognition possible. Think of MHC molecules as molecular picture frames: each one holds a single peptide fragment on the cell surface where passing T cells can inspect it. The structure of the frame determines what kind of peptide it can hold and which type of T cell will examine it.

**MHC class I** molecules are found on virtually every nucleated cell in the body. Their structure consists of a heavy chain (the alpha chain, with three domains: α1, α2, α3) paired with a small protein called **β2-microglobulin**. The α1 and α2 domains fold together to form the **peptide-binding groove** — a cleft that holds peptides 8–10 amino acids long. The groove is closed at both ends, which constrains the peptide length. Every nucleated cell continuously samples its own internal proteins, degrades them into peptides via the proteasome, and loads these peptides onto MHC-I molecules for surface display. CD8+ cytotoxic T cells scan these displays. If a cell is infected by a virus, viral peptides appear in MHC-I molecules alongside normal self-peptides, triggering the CD8+ T cell to kill the infected cell. This is the immune system's internal surveillance system — a continuous audit of what proteins each cell is making.

**MHC class II** molecules have a different structure and a different job. They consist of two chains (alpha and beta), each contributing one domain to the peptide-binding groove. Crucially, the MHC-II groove is **open at both ends**, allowing it to accommodate longer peptides (13–25 amino acids) that hang over the edges. MHC-II expression is restricted to **professional antigen-presenting cells** — dendritic cells, macrophages, and B cells — that specialize in capturing external material, processing it in endosomal compartments, and presenting the resulting peptides to CD4+ helper T cells. This division of labor is fundamental: MHC-I reports on what is happening inside the cell (intracellular surveillance), while MHC-II reports on what has been captured from outside (extracellular surveillance).

The most striking feature of MHC genes is their extraordinary **polymorphism** — they are the most variable genes in the human genome, with thousands of allelic variants in the population. Each MHC allele has a slightly different peptide-binding groove shape, meaning it binds a different set of peptides with high affinity. An individual inherits one set of MHC alleles from each parent and expresses both sets (MHC is **codominantly** expressed), giving them up to 12 different MHC molecules (6 class I and 6 class II) for presenting diverse peptides. At the population level, this polymorphism means that a pathogen peptide that escapes presentation by one person's MHC molecules is likely to be presented by someone else's. This is why MHC diversity is a population-level defense strategy — it makes it nearly impossible for a pathogen to evolve to evade antigen presentation across an entire species. It is also why organ transplant rejection occurs: the recipient's T cells recognize the donor's foreign MHC molecules as non-self, triggering an immune attack against the transplanted tissue.
