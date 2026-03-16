---
id: natural-killer-cells
title: Natural Killer Cells and Innate Lymphoid Cells
domain: biology
course: immunology
prerequisites:
- id: innate-immunity-overview
  type: hard
builds-toward:
- cd8-cytotoxic-t-cells
tags:
- innate
- lymphocytes
- cytotoxicity
stage: advanced
status: draft
---

# Natural Killer Cells and Innate Lymphoid Cells

## Core Idea
Natural killer (NK) cells are innate lymphocytes that kill virus-infected or tumor cells without prior sensitization. NK cells detect absence of MHC-I (missing self hypothesis) or engagement of activating ligands via germline-encoded NK receptors. They release perforin and granzymes, mediating target cell apoptosis through granule exocytosis.

## Explainer

Most of innate immunity works by recognizing molecular patterns that are present on pathogens but absent from host cells — PAMPs detected by pattern recognition receptors. **Natural killer (NK) cells** take a fundamentally different approach. Instead of looking for something foreign, they primarily detect the **absence of something that should be there**: MHC class I molecules on the surface of host cells. This strategy, called the **"missing self" hypothesis**, is elegant because it targets a common immune evasion tactic — many viruses and tumor cells downregulate MHC-I to avoid detection by CD8+ cytotoxic T cells, but in doing so they become visible to NK cells.

NK cells achieve this detection through a balance of **inhibitory and activating receptors**, all encoded in the germline (unlike the somatically rearranged receptors of T and B cells). Inhibitory receptors — including **killer immunoglobulin-like receptors (KIRs)** in humans and Ly49 receptors in mice — recognize MHC class I molecules on target cells. When a cell displays normal levels of MHC-I, the inhibitory signals dominate and the NK cell remains inactive, sparing the healthy cell. Simultaneously, activating receptors (such as **NKG2D**) scan for stress-induced ligands — molecules like MICA and MICB that are upregulated on cells undergoing viral infection, DNA damage, or malignant transformation. The NK cell's decision to kill depends on the **net balance** of activating versus inhibitory signals: a cell that has lost MHC-I (removing inhibitory input) or gained stress ligands (increasing activating input) tips the balance toward killing.

When the activating threshold is crossed, NK cells deploy the same cytotoxic machinery that CD8+ T cells use — **perforin** and **granzymes** — released through directed **granule exocytosis**. Perforin polymerizes to form pores in the target cell membrane, and granzymes enter through these pores to activate the caspase cascade, triggering **apoptosis**. NK cells can also kill through the Fas/FasL pathway and by antibody-dependent cellular cytotoxicity (**ADCC**) — when IgG antibodies coat a target cell, the NK cell's FcγRIIIA (CD16) receptor binds the antibody's Fc region, triggering degranulation regardless of MHC-I status. Beyond killing, NK cells are major producers of **IFN-γ**, a cytokine that activates macrophages and promotes Th1 differentiation, linking innate NK cell responses to the adaptive immune system.

NK cells occupy a unique position at the boundary between innate and adaptive immunity. They respond within hours (not days) and require no prior sensitization, making them true innate effectors. Yet recent research has revealed that NK cells can develop forms of **immunological memory** — particularly in response to cytomegalovirus infection — where specific NK cell subsets expand and persist for months, mounting enhanced responses upon re-encounter. This challenges the traditional dichotomy between innate (no memory) and adaptive (memory) immunity and has led to the broader concept of **innate lymphoid cells (ILCs)**, a family of lymphocytes that lack antigen-specific receptors but mirror T helper subset functions: ILC1s produce IFN-γ (like Th1), ILC2s produce IL-4 and IL-13 (like Th2), and ILC3s produce IL-17 and IL-22 (like Th17). NK cells are classified as cytotoxic ILCs, the innate counterpart to CD8+ T cells.
