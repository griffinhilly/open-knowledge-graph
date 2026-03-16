---
id: antigen-presentation-mechanisms
title: Antigen Processing and Presentation Pathways
domain: biology
course: immunology
prerequisites:
- id: mhc-structure-function
  type: hard
- id: protein-targeting-and-subcellular-localization
  type: hard
builds-toward:
- t-cell-activation-costimulation
- cd4-t-helper-cells
- cd8-cytotoxic-t-cells
tags:
- adaptive
- antigen-presentation
- mhc
stage: advanced
status: draft
---

# Antigen Processing and Presentation Pathways

## Core Idea
Antigen presentation pathways process antigens into peptides and load them onto MHC molecules. The MHC-I pathway (proteasomal degradation) handles intracellular antigens; the MHC-II pathway (endosomal degradation) handles exogenous antigens. Cross-presentation allows dendritic cells to present exogenous antigens on MHC-I, linking innate and adaptive responses.

## Explainer

From your study of MHC structure and function, you know that MHC molecules display peptide fragments on the cell surface for T cell recognition. But MHC molecules do not simply grab whole proteins and show them — there are elaborate intracellular processing pathways that chop proteins into peptides and load them onto the correct MHC class. The **antigen processing and presentation pathways** are the machinery that converts raw protein antigens into the peptide-MHC complexes that T cells actually see. Understanding these pathways explains why CD8+ T cells detect infections inside cells while CD4+ T cells respond to threats captured from outside.

The **MHC class I pathway** handles intracellular antigens — proteins made within the cell, including viral proteins during infection. These proteins are tagged with ubiquitin and fed into the **proteasome**, a barrel-shaped protease complex in the cytoplasm that chops them into short peptides (typically 8–10 amino acids). These peptides are then shuttled into the endoplasmic reticulum by the **TAP transporter** (Transporter associated with Antigen Processing), where they are loaded onto newly synthesized MHC-I molecules with the help of chaperones like tapasin. The loaded MHC-I complex then travels through the Golgi to the cell surface. Because virtually all nucleated cells express MHC-I and continuously sample their own cytoplasmic proteins through this pathway, any cell that becomes infected will inevitably display foreign viral peptides — flagging itself for destruction by CD8+ cytotoxic T cells.

The **MHC class II pathway** handles exogenous antigens — proteins captured from outside the cell through endocytosis or phagocytosis. Professional antigen-presenting cells (dendritic cells, macrophages, B cells) internalize extracellular material into **endosomes**, which progressively acidify and activate cathepsin proteases that degrade the captured proteins into peptides. Meanwhile, MHC-II molecules are synthesized in the ER with a protective **invariant chain** (Ii) that blocks the peptide-binding groove, preventing premature loading of ER-resident peptides. The MHC-II–invariant chain complex travels through the Golgi to merge with the endosomal compartment. There, cathepsin S cleaves the invariant chain, leaving a small fragment called **CLIP** in the groove, which is then exchanged for an antigenic peptide with the help of the HLA-DM chaperone. The loaded MHC-II complex reaches the cell surface to activate CD4+ helper T cells.

There is one critical exception to the neat division of "MHC-I for internal, MHC-II for external." **Cross-presentation** is the ability of certain dendritic cells to take exogenous antigens — captured from outside — and route them into the MHC-I pathway instead. This is immunologically essential: if a virus infects a tissue cell that is poor at activating T cells, the immune system needs a way for professional antigen-presenting cells to acquire that viral material and present it on MHC-I to prime naïve CD8+ T cells. Cross-presentation solves this problem, bridging the innate capture of extracellular debris with the adaptive cytotoxic response. Without it, the immune system would struggle to mount CD8+ responses against many viruses and tumors.
