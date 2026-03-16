---
id: dendritic-cells-and-professional-apcs
title: Dendritic Cells and Professional Antigen-Presenting Cells
domain: biology
course: immunology
prerequisites:
- id: antigen-presentation-mechanisms
  type: hard
- id: major-histocompatibility-complex
  type: hard
- id: innate-immunity-overview
  type: soft
builds-toward:
- mhc-class-i-presentation
- mhc-class-ii-presentation
- follicular-helper-t-cells-tfh
tags:
- dendritic-cells
- APCs
- innate-adaptive-bridge
- antigen-presentation
stage: advanced
status: draft
---

# Dendritic Cells and Professional Antigen-Presenting Cells

## Core Idea
Dendritic cells are professional antigen-presenting cells that bridge innate and adaptive immunity. They capture antigens through pattern recognition, process them via MHC pathways, and present them to T cells with appropriate costimulation. Dendritic cell maturation and migration from tissues to secondary lymphoid organs are critical for initiating effective adaptive immune responses.

## How It's Best Learned
Study DC development from bone marrow precursors, the molecular signals that trigger maturation (TLR activation), and how they compete with other APCs to activate T cells.

## Common Misconceptions
Not all APCs are dendritic cells—macrophages and B cells also present antigen. DC maturation requires costimulatory upregulation, not just antigen uptake alone.

## Explainer

You already understand that antigen presentation is the process by which immune cells display processed peptide fragments on MHC molecules for T cell recognition, and you know the structural basis of MHC class I and class II molecules. **Dendritic cells (DCs)** are the most important cells that perform this function — they are the primary link between the innate immune system, which detects pathogens nonspecifically, and the adaptive immune system, which mounts targeted responses. Without dendritic cells, T cells would rarely encounter the antigens they need to become activated.

The life cycle of a dendritic cell has two distinct phases. In their **immature** state, DCs reside in peripheral tissues — skin (where they are called Langerhans cells), mucosal surfaces, and organ interstitia — acting as sentinels. Immature DCs are voracious phagocytes: they constantly sample their environment through macropinocytosis, receptor-mediated endocytosis, and phagocytosis, internalizing pathogens, debris, and dying cells. However, immature DCs are poor at activating T cells because they express low levels of MHC and almost no costimulatory molecules (B7/CD80/CD86). They capture antigen efficiently but cannot yet present it effectively.

**Maturation** is triggered when pattern recognition receptors — particularly **Toll-like receptors (TLRs)** — detect pathogen-associated molecular patterns such as bacterial lipopolysaccharide or viral double-stranded RNA. This signal transforms the dendritic cell: it stops capturing new antigen, upregulates MHC class I and II molecules loaded with the captured pathogen's peptides, dramatically increases expression of costimulatory molecules (CD80, CD86) and the chemokine receptor CCR7, and begins migrating through lymphatic vessels toward the nearest **secondary lymphoid organ** — typically a lymph node. There, the mature DC presents antigen to naive T cells. Because the DC now expresses both the MHC-peptide complex (signal 1) and costimulatory molecules (signal 2), it can fully activate T cells rather than inducing tolerance.

Dendritic cells are not the only **professional antigen-presenting cells** — macrophages and B cells also express MHC class II and can present antigen. But DCs are uniquely suited to *initiate* adaptive responses because of their migration behavior and their ability to cross-present exogenous antigens on MHC class I (activating CD8+ T cells against viruses and tumors that the DC itself is not infected by). Macrophages primarily present antigen to already-activated T cells arriving at infection sites, and B cells present antigen to receive T cell help for antibody production. The division of labor is clear: dendritic cells start the adaptive response, while macrophages and B cells participate in executing it.
