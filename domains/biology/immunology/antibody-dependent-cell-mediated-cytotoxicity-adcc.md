---
id: antibody-dependent-cell-mediated-cytotoxicity-adcc
title: Antibody-Dependent Cell-Mediated Cytotoxicity (ADCC)
domain: biology
course: immunology
prerequisites:
- id: antibody-isotypes-and-effector-functions
  type: hard
- id: natural-killer-cells
  type: hard
- id: fc-gamma-receptors-igg-signaling
  type: hard
builds-toward:
- tumor-immunology-immune-evasion
- cancer-immunotherapy-approaches
- vaccine-response-and-immunogenicity
tags:
- ADCC
- Fc-receptor-engagement
- cytotoxicity
- antibody-effector-function
- NK-cells
- macrophages
stage: advanced
status: draft
---

# Antibody-Dependent Cell-Mediated Cytotoxicity (ADCC)

## Core Idea
Antibody-dependent cell-mediated cytotoxicity is a mechanism by which antibodies bound to target cell surfaces engage Fc receptors on innate immune cells (NK cells, macrophages, monocytes), triggering their activation and release of lytic granules. ADCC enables the adaptive immune system (antibodies) to recruit and direct innate effectors for target cell destruction without MHC-restricted recognition.

## How It's Best Learned
Study the Fc receptor signaling cascade, the role of immunoglobulin IgG1 and IgG3 isotypes in optimal ADCC, and conditions that enhance or inhibit this activity.

## Common Misconceptions
ADCC is not the same as complement-dependent cytotoxicity; it requires intact Fc regions and functional Fc receptors, not complement activation. Not all antibody isotypes mediate ADCC equally.

## Explainer

From your study of antibody isotypes, you know that the Fab region of an antibody binds antigen while the Fc region mediates effector functions. From your work on NK cells, you know these innate lymphocytes can kill target cells without prior sensitization. **Antibody-dependent cell-mediated cytotoxicity (ADCC)** is the mechanism that connects these two systems — it allows antibodies produced by the adaptive immune response to paint targets for destruction by innate killer cells. Think of it as a targeting system: antibodies act as guided labels, and NK cells act as the weapons platform that reads those labels.

The process begins when antibodies — primarily **IgG1** and **IgG3** subclasses, which you learned have the strongest effector functions — bind to antigens on the surface of a target cell (a virus-infected cell, a tumor cell, or any cell coated with foreign antigen). The antibodies accumulate on the target surface with their Fab ends attached to antigen and their Fc ends projecting outward. NK cells (and to a lesser extent macrophages and eosinophils) express **Fc gamma receptors**, particularly **FcγRIIIa (CD16)**, which bind the clustered Fc regions. This crosslinking of multiple FcγRIIIa receptors triggers an activating signal through the receptor's immunoreceptor tyrosine-based activation motifs (ITAMs), initiating a signaling cascade inside the NK cell. The result is degranulation — the directed release of **perforin** and **granzymes** toward the target cell. Perforin forms pores in the target cell membrane, and granzymes enter through those pores to trigger apoptosis.

What makes ADCC distinctive among killing mechanisms is that it bridges the specificity of adaptive immunity with the cytotoxic power of innate cells. Unlike cytotoxic T cells, which require MHC class I presentation and antigen-specific T cell receptors, NK cells performing ADCC need no prior education about the target antigen — the antibody provides all the specificity. This is especially important when target cells downregulate MHC class I to evade T cell killing (a common strategy of viruses and tumors), because ADCC does not depend on MHC recognition at all. It is also why ADCC is a major mechanism of action for therapeutic monoclonal antibodies in cancer treatment — drugs like rituximab (anti-CD20) and trastuzumab (anti-HER2) work in part by coating tumor cells with antibody and recruiting NK cells to destroy them via ADCC.

Several factors modulate ADCC efficiency. Antibody **glycosylation** of the Fc region significantly affects FcγRIIIa binding — removing the core fucose residue from the Fc N-linked glycan dramatically enhances ADCC, which is why next-generation therapeutic antibodies are often engineered with afucosylated Fc regions. The density of antigen on the target cell surface matters too: more antigen means more antibody coating, which means stronger FcγR crosslinking and a more robust kill signal. Conversely, inhibitory Fc receptors (like FcγRIIb) and competition from serum IgG can dampen the response, providing regulatory checkpoints that prevent ADCC from causing excessive tissue damage.
