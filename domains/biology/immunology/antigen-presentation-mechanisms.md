---
id: antigen-presentation-mechanisms
title: Antigen Processing and Presentation Pathways
domain: biology
course: immunology
prerequisites:
- id: major-histocompatibility-complex
  type: hard
- id: protein-targeting-and-subcellular-localization
  type: hard
builds-toward:
- t-cell-activation-costimulation
- cd4-helper-t-cells
- cd8-cytotoxic-t-cells
tags:
- adaptive
- antigen-presentation
- mhc
stage: expert
status: validated
---

# Antigen Processing and Presentation Pathways

## Core Idea
Antigen presentation pathways process antigens into peptides and load them onto MHC molecules. The MHC-I pathway (proteasomal degradation) handles intracellular antigens; the MHC-II pathway (endosomal degradation) handles exogenous antigens. Cross-presentation allows dendritic cells to present exogenous antigens on MHC-I, linking innate and adaptive responses.

## Questions

```yaml
- question: "A cell is actively infected by a virus, and viral proteins are being synthesized in the cytoplasm. Which pathway will present viral peptides to T cells, and which T cell type will be activated?"
  type: multiple-choice
  options:
    - "MHC-II pathway via endosomal degradation, activating CD4+ helper T cells"
    - "MHC-I pathway via proteasomal degradation and TAP transport, activating CD8+ cytotoxic T cells"
    - "Both MHC-I and MHC-II pathways present the same viral peptides with equal efficiency"
    - "MHC-I pathway presents to CD4+ T cells because viral infection activates helper responses first"
  answer: 1
  explanation: "The MHC-I pathway is dedicated to sampling intracellular proteins. Viral proteins made in the cytoplasm are ubiquitinated, degraded by the proteasome into 8–10 aa peptides, shuttled into the ER by TAP, loaded onto MHC-I, and trafficked to the cell surface for CD8+ cytotoxic T cell recognition. The MHC-II pathway handles exogenous antigens captured by endocytosis. Option D confuses MHC class with T cell subset — MHC-I presents to CD8+ (not CD4+) T cells."

- question: "A dendritic cell phagocytoses apoptotic tumor cells and successfully presents tumor-derived peptides to naïve CD8+ T cells via MHC-I, even though the tumor proteins were captured from outside the cell. This process is called:"
  type: multiple-choice
  options:
    - "Classical MHC-I presentation — dendritic cells are professional APCs and always use MHC-I"
    - "Cross-presentation — exogenous antigens are routed into the MHC-I pathway by specialized dendritic cells"
    - "MHC-II restricted presentation — CD8+ T cells can use MHC-II in inflammatory conditions"
    - "Invariant chain processing — the CLIP exchange mechanism allows antigen rerouting"
  answer: 1
  explanation: "Cross-presentation is the capacity of certain dendritic cells to take exogenous antigens and route them into the MHC-I pathway (normally reserved for intracellular antigens). This is the exception to the rule that MHC-I only presents endogenous peptides. It is immunologically critical for priming CD8+ T cell responses against viruses that infect tissue cells which are poor at activating T cells directly."

- question: "The invariant chain (Ii) associated with newly synthesized MHC-II molecules serves to protect the peptide-binding groove from loading ER-resident peptides before the MHC-II complex reaches the endosomal compartment."
  type: true-false
  answer: true
  explanation: "The invariant chain physically blocks the MHC-II peptide-binding groove in the ER, preventing premature loading of peptides present in the ER (which are the domain of MHC-I). The MHC-II/Ii complex travels through the Golgi and fuses with endosomes, where cathepsins cleave the invariant chain, leaving only the CLIP fragment. HLA-DM then facilitates CLIP exchange for antigenic peptides from the degraded extracellular proteins. This ensures MHC-II only presents exogenous antigen."

- question: "MHC class I molecules are expressed only on professional antigen-presenting cells (dendritic cells, macrophages, and B cells), because only these cells need to present intracellular antigens to T cells."
  type: true-false
  answer: false
  explanation: "MHC-I is expressed on virtually all nucleated cells in the body — not just professional APCs. This makes biological sense: any cell can become infected by a virus, and the immune system needs to detect infection anywhere it occurs. CD8+ cytotoxic T cells patrol and kill any infected cell displaying foreign peptides on MHC-I. Professional APCs constitutively express both MHC-I and MHC-II; most other nucleated cells express MHC-I but little or no MHC-II."

- question: "Why is cross-presentation immunologically essential? What gap would exist in the adaptive immune response if dendritic cells could only present exogenous antigens on MHC-II?"
  type: short-answer
  answer: "Without cross-presentation, naïve CD8+ cytotoxic T cells could only be primed if a virus directly infected a professional antigen-presenting cell capable of activating T cells. Many viruses infect tissue cells (muscle, epithelium, neurons) that express MHC-I but are poor at providing T cell costimulation. Cross-presentation allows dendritic cells to capture viral material from those infected tissue cells and present it on MHC-I with full costimulatory capacity, priming an effective CD8+ cytotoxic response. Without it, the immune system would fail to mount cytotoxic responses against many viruses and tumors."
  explanation: "Cross-presentation bridges the innate and adaptive immune responses: innate sentinels (dendritic cells) capture extracellular danger signals, but use them to activate the arm of adaptive immunity (CD8+ T cells) normally reserved for intracellular threats. This is why cross-presentation is especially important in cancer immunology and vaccine design — tumor antigens are often extracellular, yet a CD8+ response is needed to kill tumor cells."
```

## Explainer

From your study of MHC structure and function, you know that MHC molecules display peptide fragments on the cell surface for T cell recognition. But MHC molecules do not simply grab whole proteins and show them — there are elaborate intracellular processing pathways that chop proteins into peptides and load them onto the correct MHC class. The **antigen processing and presentation pathways** are the machinery that converts raw protein antigens into the peptide-MHC complexes that T cells actually see. Understanding these pathways explains why CD8+ T cells detect infections inside cells while CD4+ T cells respond to threats captured from outside.

The **MHC class I pathway** handles intracellular antigens — proteins made within the cell, including viral proteins during infection. These proteins are tagged with ubiquitin and fed into the **proteasome**, a barrel-shaped protease complex in the cytoplasm that chops them into short peptides (typically 8–10 amino acids). These peptides are then shuttled into the endoplasmic reticulum by the **TAP transporter** (Transporter associated with Antigen Processing), where they are loaded onto newly synthesized MHC-I molecules with the help of chaperones like tapasin. The loaded MHC-I complex then travels through the Golgi to the cell surface. Because virtually all nucleated cells express MHC-I and continuously sample their own cytoplasmic proteins through this pathway, any cell that becomes infected will inevitably display foreign viral peptides — flagging itself for destruction by CD8+ cytotoxic T cells.

The **MHC class II pathway** handles exogenous antigens — proteins captured from outside the cell through endocytosis or phagocytosis. Professional antigen-presenting cells (dendritic cells, macrophages, B cells) internalize extracellular material into **endosomes**, which progressively acidify and activate cathepsin proteases that degrade the captured proteins into peptides. Meanwhile, MHC-II molecules are synthesized in the ER with a protective **invariant chain** (Ii) that blocks the peptide-binding groove, preventing premature loading of ER-resident peptides. The MHC-II–invariant chain complex travels through the Golgi to merge with the endosomal compartment. There, cathepsin S cleaves the invariant chain, leaving a small fragment called **CLIP** in the groove, which is then exchanged for an antigenic peptide with the help of the HLA-DM chaperone. The loaded MHC-II complex reaches the cell surface to activate CD4+ helper T cells.

There is one critical exception to the neat division of "MHC-I for internal, MHC-II for external." **Cross-presentation** is the ability of certain dendritic cells to take exogenous antigens — captured from outside — and route them into the MHC-I pathway instead. This is immunologically essential: if a virus infects a tissue cell that is poor at activating T cells, the immune system needs a way for professional antigen-presenting cells to acquire that viral material and present it on MHC-I to prime naïve CD8+ T cells. Cross-presentation solves this problem, bridging the innate capture of extracellular debris with the adaptive cytotoxic response. Without it, the immune system would struggle to mount CD8+ responses against many viruses and tumors.
