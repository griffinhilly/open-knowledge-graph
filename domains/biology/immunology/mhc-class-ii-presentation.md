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

## Explainer

From your study of the major histocompatibility complex, you know that MHC molecules display peptide fragments on the cell surface for T cell surveillance. The MHC class II pathway is the route by which **exogenous antigens** — proteins captured from outside the cell — get processed and displayed to CD4+ helper T cells. Understanding this pathway means tracing a protein's journey from the extracellular environment, through a series of increasingly acidic intracellular compartments, to the cell surface bound to an MHC-II molecule.

The process begins when a professional antigen-presenting cell (APC) — a dendritic cell, macrophage, or B cell — **endocytoses** extracellular material. This could be a bacterium engulfed by a macrophage, a soluble protein pinocytosed by a dendritic cell, or a specific antigen captured by a B cell's surface immunoglobulin. The internalized material enters **endosomes**, which progressively acidify as they mature (from early endosomes at pH ~6.5 to late endosomes and lysosomes at pH ~4.5). This acidification activates **cathepsin proteases** — particularly cathepsins S, L, and D — that systematically degrade the captured proteins into peptide fragments suitable for MHC-II binding, typically 13–25 amino acids long (longer than the 8–10-mer peptides used by MHC-I, because the MHC-II groove is open at both ends).

Meanwhile, MHC-II molecules are being assembled in the endoplasmic reticulum, but they face a problem: the ER is full of self-peptides and partially folded proteins that could load into the peptide-binding groove prematurely. The cell solves this with the **invariant chain (Ii, or CD74)**, a chaperone protein that threads through the MHC-II groove, blocking it and simultaneously acting as a targeting signal that directs the MHC-II complex from the ER through the Golgi to the endosomal compartment. Once in the acidic endosome, cathepsin S progressively degrades the invariant chain, but a small fragment called **CLIP** (class II-associated invariant chain peptide) remains lodged in the groove. Removing CLIP requires the chaperone **HLA-DM**, a non-classical MHC-II molecule that catalyzes the exchange: it binds the MHC-II-CLIP complex, destabilizes the CLIP interaction, and facilitates loading of the highest-affinity antigenic peptide available in the compartment. HLA-DM effectively acts as a peptide editor, ensuring that the MHC-II molecule displays the most stable peptide-MHC complex rather than a weakly bound fragment.

The loaded **peptide-MHC-II complex** then traffics to the cell surface, where it is available for recognition by CD4+ T cells bearing the appropriate T cell receptor. This pathway is restricted to professional APCs because most other cell types do not express MHC-II (with exceptions during inflammation when interferon-γ can induce MHC-II expression on other cells). The restriction makes biological sense: CD4+ T helper cells coordinate the broader immune response — activating B cells, licensing macrophages, directing the type of immune response — so the system limits which cells can initiate this conversation to the professional sentinels best positioned to have sampled the relevant antigens from the extracellular environment.
