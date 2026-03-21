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

## Questions

```yaml
- question: "A cell is infected by a virus and begins synthesizing viral proteins. Which T cell type will recognize this, and through which MHC class?"
  type: multiple-choice
  options:
    - "CD4+ helper T cells through MHC class II molecules on the infected cell"
    - "CD8+ cytotoxic T cells through MHC class I molecules on the infected cell"
    - "B cells through surface antibodies that recognize viral proteins directly"
    - "Natural killer cells through MHC class II molecules on the infected cell"
  answer: 1
  explanation: "Virtually all nucleated cells express MHC class I, which samples the cell's own internal proteins via the proteasome and loads the resulting peptides for display. CD8+ cytotoxic T cells scan these displays — if viral peptides appear, the CD8+ T cell kills the infected cell. MHC class II is restricted to professional antigen-presenting cells (dendritic cells, macrophages, B cells) and presents exogenous peptides to CD4+ helper T cells. Most infected cells lack MHC-II entirely, so option A is mechanistically impossible."

- question: "Why are organ transplants frequently rejected even when donor and recipient have identical ABO blood types?"
  type: multiple-choice
  options:
    - "ABO antigens are expressed on transplanted organ cells and directly activate complement-mediated killing"
    - "The recipient's T cells recognize the donor's foreign MHC molecules as non-self, triggering an immune attack against the transplanted tissue"
    - "Viruses transmitted with the transplanted organ trigger the rejection response"
    - "Transplanted organs express only MHC class II, which activates antibody-mediated rejection"
  answer: 1
  explanation: "MHC genes are the most polymorphic in the human genome. Even with blood type compatibility, the donor's MHC alleles are almost certainly different from the recipient's. The recipient's T cells, trained to respond to foreign peptides only in the context of self-MHC, instead recognize the donor's MHC molecules themselves as foreign — the 'direct allorecognition' pathway. Blood type compatibility is irrelevant to this T-cell-mediated mechanism. This is why immunosuppressive therapy targeting T cells is required after transplantation."

- question: "MHC class I molecules present peptides from proteins taken up from the extracellular environment, while MHC class II molecules present peptides from proteins synthesized inside the cell."
  type: true-false
  answer: false
  explanation: "This is a direct reversal of the actual pathways. MHC class I presents intracellular peptides — proteins synthesized inside the cell are degraded by the proteasome, and the resulting 8–10 amino acid peptides are loaded onto MHC-I for surface display. MHC class II presents exogenous peptides — professional antigen-presenting cells capture external material by endocytosis, degrade it in endosomal compartments, and load the longer (13–25 aa) peptides onto MHC-II. Confusing these two pathways is the most common error in MHC biology."

- question: "The extreme polymorphism of MHC genes benefits the population as a whole by making it nearly impossible for a pathogen to evolve universal escape from antigen presentation."
  type: true-false
  answer: true
  explanation: "Each MHC allele has a slightly different peptide-binding groove that preferentially presents a different set of peptides. A viral peptide that fails to bind one person's MHC alleles is likely to be presented on someone else's. At the population level, this diversity means no single pathogen mutation can evade antigen presentation across an entire species. This is why MHC polymorphism is maintained by balancing selection — individuals with rare MHC alleles have a survival advantage against pathogens adapted to the common alleles. It also explains transplant rejection as a side effect of a population-level defense."

- question: "Explain the functional significance of the structural difference between the MHC class I and class II peptide-binding grooves — specifically why MHC-I has a closed groove and MHC-II has an open groove."
  type: short-answer
  answer: "MHC class I presents peptides from intracellular proteins degraded by the proteasome, which cuts them into precise 8–10 amino acid fragments. The closed groove (sealed at both ends) constrains peptide length — only peptides of the right size fit and stabilize the complex. MHC class II presents peptides from extracellular proteins degraded less precisely in endosomal compartments; these fragments are longer (13–25 amino acids) and more variable. The open groove accommodates this length variability by allowing the peptide ends to hang over the edges. The structural difference directly reflects the biological pathway each class serves."
  explanation: "This is not just structural trivia — the groove architecture enforces the functional separation between intracellular and extracellular surveillance. Understanding why the grooves differ in this way requires grasping both the processing pathways and the T-cell recognition consequences."
```

## Explainer

From your study of adaptive immunity, you know that T cells cannot recognize free-floating proteins — they can only detect short peptide fragments displayed on cell surfaces. The **major histocompatibility complex (MHC)** molecules are the display platform that makes this recognition possible. Think of MHC molecules as molecular picture frames: each one holds a single peptide fragment on the cell surface where passing T cells can inspect it. The structure of the frame determines what kind of peptide it can hold and which type of T cell will examine it.

**MHC class I** molecules are found on virtually every nucleated cell in the body. Their structure consists of a heavy chain (the alpha chain, with three domains: α1, α2, α3) paired with a small protein called **β2-microglobulin**. The α1 and α2 domains fold together to form the **peptide-binding groove** — a cleft that holds peptides 8–10 amino acids long. The groove is closed at both ends, which constrains the peptide length. Every nucleated cell continuously samples its own internal proteins, degrades them into peptides via the proteasome, and loads these peptides onto MHC-I molecules for surface display. CD8+ cytotoxic T cells scan these displays. If a cell is infected by a virus, viral peptides appear in MHC-I molecules alongside normal self-peptides, triggering the CD8+ T cell to kill the infected cell. This is the immune system's internal surveillance system — a continuous audit of what proteins each cell is making.

**MHC class II** molecules have a different structure and a different job. They consist of two chains (alpha and beta), each contributing one domain to the peptide-binding groove. Crucially, the MHC-II groove is **open at both ends**, allowing it to accommodate longer peptides (13–25 amino acids) that hang over the edges. MHC-II expression is restricted to **professional antigen-presenting cells** — dendritic cells, macrophages, and B cells — that specialize in capturing external material, processing it in endosomal compartments, and presenting the resulting peptides to CD4+ helper T cells. This division of labor is fundamental: MHC-I reports on what is happening inside the cell (intracellular surveillance), while MHC-II reports on what has been captured from outside (extracellular surveillance).

The most striking feature of MHC genes is their extraordinary **polymorphism** — they are the most variable genes in the human genome, with thousands of allelic variants in the population. Each MHC allele has a slightly different peptide-binding groove shape, meaning it binds a different set of peptides with high affinity. An individual inherits one set of MHC alleles from each parent and expresses both sets (MHC is **codominantly** expressed), giving them up to 12 different MHC molecules (6 class I and 6 class II) for presenting diverse peptides. At the population level, this polymorphism means that a pathogen peptide that escapes presentation by one person's MHC molecules is likely to be presented by someone else's. This is why MHC diversity is a population-level defense strategy — it makes it nearly impossible for a pathogen to evolve to evade antigen presentation across an entire species. It is also why organ transplant rejection occurs: the recipient's T cells recognize the donor's foreign MHC molecules as non-self, triggering an immune attack against the transplanted tissue.
