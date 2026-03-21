---
id: mhc-class-ii-presentation
title: MHC Class II Antigen Presentation Pathway
domain: biology
course: immunology
prerequisites:
- id: major-histocompatibility-complex
  type: hard
- id: antigen-processing-pathways
  type: hard
builds-toward:
- cd4-helper-t-cells
- germinal-center-reactions
tags:
- mhc-ii
- antigen-presentation
- endosomal
stage: advanced
status: draft
---

# MHC Class II Antigen Presentation Pathway

## Core Idea
MHC Class II presents peptides from endocytosed extracellular proteins to CD4+ T cells. Antigen-presenting cells endocytose pathogens or antigens into vesicles where cathepsin proteases generate peptide fragments. The invariant chain chaperones MHC-II through the secretory pathway and is cleaved by cathepsin S, allowing peptide loading in endosomal compartments. Peptide-MHC-II complexes traffic to the cell surface.

## How It's Best Learned
Trace exogenous antigen from endocytosis through endosomal proteolysis to peptide loading onto nascent MHC-II. Identify where invariant chain functions and is removed.

## Common Misconceptions
- MHC-II presents only pathogenic peptides (exogenous antigens can be pathogenic or non-pathogenic). - All endosomal compartments contain MHC-II loading machinery (specific compartments optimize proteolysis and loading).

## Questions

```yaml
- question: "A macrophage phagocytoses a bacterium. Which sequence of events correctly describes how a bacterial protein ultimately activates a CD4+ T cell?"
  type: multiple-choice
  options:
    - "The bacterial protein is degraded by the proteasome and its peptides are loaded onto MHC-I molecules in the ER, then displayed to CD4+ T cells"
    - "The bacterial protein is degraded by lysosomal cathepsin proteases into peptides that load onto MHC-II molecules in the endosomal compartment, then displayed to CD4+ T cells"
    - "The intact bacterial protein is displayed directly on the macrophage surface for direct recognition by CD4+ T cell receptors"
    - "The bacterial protein is degraded in the ER and loaded onto MHC-II before the complex is targeted to the endosome for final processing"
  answer: 1
  explanation: "MHC-II presents exogenous (extracellular-origin) antigens to CD4+ T cells via the endosomal pathway. Endocytosed bacteria are degraded in progressively acidifying endosomes by cathepsin proteases (not the proteasome, which handles endogenous proteins for MHC-I). The resulting peptides are loaded onto MHC-II in the endosomal compartment (not the ER), and the complex traffics to the cell surface. MHC-I presents endogenous peptides (from proteins made inside the cell) to CD8+ cytotoxic T cells — a completely separate pathway."

- question: "The invariant chain (Ii) serves two essential functions in the MHC-II antigen presentation pathway. It:"
  type: multiple-choice
  options:
    - "Degrades CLIP in the endosome and directly loads high-affinity antigenic peptides onto MHC-II"
    - "Blocks the MHC-II peptide-binding groove to prevent premature peptide loading in the ER, and acts as a targeting signal directing the MHC-II complex from the ER through the Golgi to the endosomal compartment"
    - "Activates cathepsin proteases in early endosomes to initiate antigen degradation"
    - "Prevents MHC-II from associating with HLA-DM before reaching the appropriate endosomal compartment"
  answer: 1
  explanation: "The invariant chain (Ii) solves two problems simultaneously. First, the ER contains many self-peptides and partially folded proteins that would load promiscuously into the empty MHC-II groove — Ii blocks this by physically occupying the groove. Second, Ii contains a targeting sequence in its cytoplasmic tail that routes the MHC-II/Ii complex from the ER through the Golgi to the endosomal compartment where antigen degradation is occurring. CLIP removal (by HLA-DM) and peptide loading are subsequent steps, performed by different molecules."

- question: "HLA-DM catalyzes the removal of CLIP from the MHC-II peptide-binding groove and facilitates loading of high-affinity antigenic peptides, functioning as a peptide editor in the endosomal compartment."
  type: true-false
  answer: true
  explanation: "Correct. After cathepsin S degrades most of the invariant chain in the endosome, a small fragment called CLIP (class II-associated invariant chain peptide) remains lodged in the MHC-II groove. HLA-DM — a non-classical MHC-II molecule that does not itself present peptides — binds the MHC-II/CLIP complex, destabilizes the CLIP interaction, and catalyzes exchange for the highest-affinity antigenic peptide available in the endosome. This editing function ensures that MHC-II displays the most stable peptide-MHC complexes, enriching the surface display for immunologically relevant peptides."

- question: "MHC class II molecules present peptides derived from proteins synthesized inside the presenting cell (endogenous antigens) to CD4+ helper T cells."
  type: true-false
  answer: false
  explanation: "This describes the MHC class I pathway, not MHC class II. MHC-I presents endogenous antigens (proteins made inside the cell, degraded by the proteasome, transported into the ER by TAP, and loaded in the ER) to CD8+ cytotoxic T cells. MHC-II presents exogenous antigens (proteins captured from outside the cell by endocytosis, degraded by lysosomal cathepsins in acidified endosomes, and loaded in the endosomal compartment) to CD4+ helper T cells. The two pathways are separately regulated and serve distinct immunological functions."

- question: "Why is it essential that the invariant chain blocks the MHC-II peptide-binding groove in the ER, and what would happen without this protection?"
  type: short-answer
  answer: "Without the invariant chain, the empty MHC-II groove in the ER would be accessible to self-peptides and other ER-resident peptides generated during normal protein processing. These peptides would load into the groove and be displayed on the cell surface — potentially triggering T cell responses against self-antigens (autoimmunity) or presenting irrelevant peptides that crowd out immunologically relevant ones."
  explanation: "The invariant chain is a solution to the problem of specificity in antigen presentation: MHC-II should display peptides from exogenous antigens sampled in the endosome, not from proteins in the ER. By physically occupying the groove until the molecule reaches the appropriate acidic endosomal compartment, Ii ensures that the groove is only 'open for business' in the right place (endosome) at the right time (after cathepsin-mediated Ii degradation). HLA-DM then further enforces quality control by selecting for high-affinity peptide-MHC interactions."
```

## Explainer

From your study of the major histocompatibility complex, you know that MHC molecules display peptide fragments on the cell surface for T cell surveillance. The MHC class II pathway is the route by which **exogenous antigens** — proteins captured from outside the cell — get processed and displayed to CD4+ helper T cells. Understanding this pathway means tracing a protein's journey from the extracellular environment, through a series of increasingly acidic intracellular compartments, to the cell surface bound to an MHC-II molecule.

The process begins when a professional antigen-presenting cell (APC) — a dendritic cell, macrophage, or B cell — **endocytoses** extracellular material. This could be a bacterium engulfed by a macrophage, a soluble protein pinocytosed by a dendritic cell, or a specific antigen captured by a B cell's surface immunoglobulin. The internalized material enters **endosomes**, which progressively acidify as they mature (from early endosomes at pH ~6.5 to late endosomes and lysosomes at pH ~4.5). This acidification activates **cathepsin proteases** — particularly cathepsins S, L, and D — that systematically degrade the captured proteins into peptide fragments suitable for MHC-II binding, typically 13–25 amino acids long (longer than the 8–10-mer peptides used by MHC-I, because the MHC-II groove is open at both ends).

Meanwhile, MHC-II molecules are being assembled in the endoplasmic reticulum, but they face a problem: the ER is full of self-peptides and partially folded proteins that could load into the peptide-binding groove prematurely. The cell solves this with the **invariant chain (Ii, or CD74)**, a chaperone protein that threads through the MHC-II groove, blocking it and simultaneously acting as a targeting signal that directs the MHC-II complex from the ER through the Golgi to the endosomal compartment. Once in the acidic endosome, cathepsin S progressively degrades the invariant chain, but a small fragment called **CLIP** (class II-associated invariant chain peptide) remains lodged in the groove. Removing CLIP requires the chaperone **HLA-DM**, a non-classical MHC-II molecule that catalyzes the exchange: it binds the MHC-II-CLIP complex, destabilizes the CLIP interaction, and facilitates loading of the highest-affinity antigenic peptide available in the compartment. HLA-DM effectively acts as a peptide editor, ensuring that the MHC-II molecule displays the most stable peptide-MHC complex rather than a weakly bound fragment.

The loaded **peptide-MHC-II complex** then traffics to the cell surface, where it is available for recognition by CD4+ T cells bearing the appropriate T cell receptor. This pathway is restricted to professional APCs because most other cell types do not express MHC-II (with exceptions during inflammation when interferon-γ can induce MHC-II expression on other cells). The restriction makes biological sense: CD4+ T helper cells coordinate the broader immune response — activating B cells, licensing macrophages, directing the type of immune response — so the system limits which cells can initiate this conversation to the professional sentinels best positioned to have sampled the relevant antigens from the extracellular environment.
