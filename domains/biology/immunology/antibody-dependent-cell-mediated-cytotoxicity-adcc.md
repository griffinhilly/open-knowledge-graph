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

## Questions

```yaml
- question: "A tumor cell downregulates MHC class I expression to evade immune surveillance. Which killing mechanism would be most impaired by this strategy?"
  type: multiple-choice
  options:
    - "ADCC by NK cells, because NK cells require MHC class I presentation to identify the target"
    - "Cytotoxic T lymphocyte (CTL) killing, because CTLs recognize antigen presented on MHC class I via their T cell receptors"
    - "ADCC would be unaffected, but complement-dependent cytotoxicity would be eliminated"
    - "Both CTL killing and ADCC equally, since both pathways converge on the same MHC-restricted recognition step"
  answer: 1
  explanation: "Cytotoxic T lymphocytes (CTLs) are MHC class I-restricted: they can only recognize and kill a target if the target presents antigen on MHC class I molecules. Downregulating MHC class I is a direct evasion of CTL killing. ADCC, by contrast, does not require MHC recognition at all — the antibody provides specificity by binding surface antigens, and NK cells detect the Fc regions of the bound antibodies through FcγRIIIa (CD16). As long as the tumor expresses the surface antigen targeted by the antibody, ADCC can still proceed even with no MHC class I present."

- question: "Which part of an antibody molecule triggers ADCC, and which cell receptor on the effector cell does it engage?"
  type: multiple-choice
  options:
    - "The Fab region binds to FcγRIIIa (CD16) on NK cells, crosslinking the receptor to activate killing"
    - "The Fc region of surface-bound antibody is recognized by FcγRIIIa (CD16) on NK cells, triggering degranulation"
    - "The variable regions of the antibody bind directly to activating receptors on NK cells, bypassing the Fc region entirely"
    - "The Fc region binds to MHC class I on the NK cell, which provides the activation signal for cytotoxicity"
  answer: 1
  explanation: "In ADCC, the Fab regions are occupied binding antigen on the target cell surface. The Fc regions project outward and are recognized by FcγRIIIa (CD16) on NK cells (and to a lesser extent macrophages and eosinophils). Crosslinking of multiple FcγRIIIa receptors by clustered Fc regions triggers ITAM-mediated intracellular signaling, leading to degranulation of perforin and granzymes toward the target. The specificity comes entirely from the antibody's Fab-antigen interaction; the NK cell's FcγRIIIa is the activating receptor, not an antigen-recognition receptor."

- question: "ADCC is triggered when NK cells directly recognize antigens on target cells through their own antigen-specific receptors."
  type: true-false
  answer: false
  explanation: "NK cells do not have antigen-specific receptors like T cell receptors. In ADCC, the specificity for the target cell comes entirely from the antibody — its Fab regions bind to surface antigens. The NK cell detects not the antigen but the Fc region of the antibody that has already bound the target. It is the antibody coating the target cell that signals 'destroy this cell,' and the NK cell simply responds to that coating via FcγRIIIa. This is precisely what makes ADCC a bridge between adaptive (antibody) and innate (NK cell) immunity."

- question: "Removing the core fucose residue from the Fc region of a therapeutic antibody enhances its ability to trigger ADCC."
  type: true-false
  answer: true
  explanation: "The N-linked glycan at Asn-297 in the Fc region of IgG influences how tightly the Fc binds to FcγRIIIa. Afucosylation (removal of the core fucose) dramatically increases the affinity of Fc for FcγRIIIa, leading to stronger receptor crosslinking, more robust activating signals in NK cells, and enhanced ADCC activity. This is why next-generation therapeutic monoclonal antibodies (e.g., obinutuzumab vs. rituximab) are often engineered with afucosylated Fc regions to improve clinical efficacy through enhanced ADCC."

- question: "Why is ADCC effective against target cells that have downregulated MHC class I expression, a strategy commonly used by viruses and tumors to evade cytotoxic T cells?"
  type: short-answer
  answer: "ADCC does not use MHC-restricted recognition at any step. The antibody's Fab regions bind directly to antigens expressed on the target cell surface (viral proteins, tumor-associated antigens), and the NK cell's FcγRIIIa detects the Fc regions of the coating antibodies. Neither the antibody-antigen interaction nor the Fc-FcγR interaction requires MHC class I. As long as the target cell continues to express the antigen targeted by the antibody, it can be killed by ADCC regardless of its MHC class I status. This makes ADCC an important immunological backup against pathogens and tumors that exploit MHC downregulation to hide from T cells."
  explanation: "This complementarity — CTLs killing MHC-expressing targets, NK cells killing MHC-low targets (through missing-self recognition), and ADCC killing antibody-coated targets regardless of MHC — illustrates how the immune system uses overlapping and complementary mechanisms to prevent any single evasion strategy from being fully effective. Therapeutic antibodies exploit ADCC precisely because tumor cells frequently downregulate MHC; the antibody repaints the target in a way that NK cells can read without needing MHC-mediated antigen presentation."
```

## Explainer

From your study of antibody isotypes, you know that the Fab region of an antibody binds antigen while the Fc region mediates effector functions. From your work on NK cells, you know these innate lymphocytes can kill target cells without prior sensitization. **Antibody-dependent cell-mediated cytotoxicity (ADCC)** is the mechanism that connects these two systems — it allows antibodies produced by the adaptive immune response to paint targets for destruction by innate killer cells. Think of it as a targeting system: antibodies act as guided labels, and NK cells act as the weapons platform that reads those labels.

The process begins when antibodies — primarily **IgG1** and **IgG3** subclasses, which you learned have the strongest effector functions — bind to antigens on the surface of a target cell (a virus-infected cell, a tumor cell, or any cell coated with foreign antigen). The antibodies accumulate on the target surface with their Fab ends attached to antigen and their Fc ends projecting outward. NK cells (and to a lesser extent macrophages and eosinophils) express **Fc gamma receptors**, particularly **FcγRIIIa (CD16)**, which bind the clustered Fc regions. This crosslinking of multiple FcγRIIIa receptors triggers an activating signal through the receptor's immunoreceptor tyrosine-based activation motifs (ITAMs), initiating a signaling cascade inside the NK cell. The result is degranulation — the directed release of **perforin** and **granzymes** toward the target cell. Perforin forms pores in the target cell membrane, and granzymes enter through those pores to trigger apoptosis.

What makes ADCC distinctive among killing mechanisms is that it bridges the specificity of adaptive immunity with the cytotoxic power of innate cells. Unlike cytotoxic T cells, which require MHC class I presentation and antigen-specific T cell receptors, NK cells performing ADCC need no prior education about the target antigen — the antibody provides all the specificity. This is especially important when target cells downregulate MHC class I to evade T cell killing (a common strategy of viruses and tumors), because ADCC does not depend on MHC recognition at all. It is also why ADCC is a major mechanism of action for therapeutic monoclonal antibodies in cancer treatment — drugs like rituximab (anti-CD20) and trastuzumab (anti-HER2) work in part by coating tumor cells with antibody and recruiting NK cells to destroy them via ADCC.

Several factors modulate ADCC efficiency. Antibody **glycosylation** of the Fc region significantly affects FcγRIIIa binding — removing the core fucose residue from the Fc N-linked glycan dramatically enhances ADCC, which is why next-generation therapeutic antibodies are often engineered with afucosylated Fc regions. The density of antigen on the target cell surface matters too: more antigen means more antibody coating, which means stronger FcγR crosslinking and a more robust kill signal. Conversely, inhibitory Fc receptors (like FcγRIIb) and competition from serum IgG can dampen the response, providing regulatory checkpoints that prevent ADCC from causing excessive tissue damage.
