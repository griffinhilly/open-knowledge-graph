---
id: cross-presentation-exogenous-antigens
title: Cross-Presentation of Exogenous Antigens
domain: biology
course: immunology
prerequisites:
- id: mhc-class-i-presentation
  type: hard
- id: antigen-processing-pathways
  type: hard
builds-toward:
- cd8-cytotoxic-t-cells
- vaccine-design-immunogenicity-adjuvants
tags:
- cross-presentation
- antigen-processing
- cd8-activation
stage: advanced
status: draft
---

# Cross-Presentation of Exogenous Antigens

## Core Idea
Cross-presentation allows antigen-presenting cells (primarily dendritic cells) to present exogenous antigens on MHC-I to activate CD8+ T cells despite these proteins entering the endosomal rather than cytosolic pathway. Exogenous antigens are internalized into endosomes where some escape into the cytosol (via membrane pores or ER dislocation) to reach proteasomes. This mechanism enables CD8+ T cell responses against extracellular pathogens and tumor antigens.

## How It's Best Learned
Diagram two models of cross-presentation: ER-mediated dislocation and phagosomal dislocation. Identify which dendritic cell subsets excel at cross-presentation and why.

## Common Misconceptions
- All cells can cross-present efficiently (specialized dendritic cell subsets have enhanced capacity). - Cross-presentation uses unmodified endosomal peptides (they may be further processed by proteasomes).

## Explainer

From your study of MHC class I presentation and antigen processing, you know the standard rule: MHC-I presents peptides derived from proteins synthesized *inside* the cell. A virus-infected cell degrades viral proteins in its proteasomes, transports the resulting peptides into the ER via TAP, loads them onto MHC-I, and displays them on the surface for CD8+ T cell surveillance. This system works well for detecting infected cells — but it creates a problem. What happens when a virus infects cells that are poor antigen presenters, or when tumor cells downregulate MHC-I? How do CD8+ T cells get activated in the first place if the antigen is trapped inside cells that cannot properly prime a naive T cell? The answer is **cross-presentation**.

Cross-presentation is the ability of certain **antigen-presenting cells** — primarily a specialized subset of dendritic cells — to take up **exogenous** proteins (proteins from outside the cell, such as debris from dead infected cells or captured tumor fragments) and route them into the MHC class I pathway instead of the MHC class II pathway where exogenous antigens normally go. This is immunologically unusual: the default rule is that exogenous antigens enter endosomes, get degraded there, and load onto MHC-II for presentation to CD4+ T cells. Cross-presentation breaks this rule by diverting exogenous material into the cytosolic, proteasome-dependent, TAP-dependent MHC-I pathway.

Two main models explain how exogenous proteins escape from endosomes into the cytosol. In the **cytosolic pathway**, proteins in the phagosome are translocated across the phagosomal membrane into the cytoplasm — possibly via the same Sec61 channel used for ER-associated degradation — where they encounter proteasomes, get degraded into peptides, and enter the standard TAP-to-ER-to-MHC-I loading pipeline. In the **vacuolar pathway**, proteolytic processing and MHC-I loading both occur within the endosomal compartment itself, without the peptides ever reaching the cytosol. The cytosolic pathway appears to be the dominant mechanism in most experimental systems, but both routes contribute depending on the nature of the antigen and the dendritic cell subset involved.

The biological importance of cross-presentation cannot be overstated. Without it, the immune system could not mount CD8+ T cell responses against pathogens that do not directly infect dendritic cells — and most pathogens do not. It is also the mechanism that underlies the success of many **vaccines**: killed or subunit vaccines deliver exogenous protein, yet they still generate cytotoxic T cell responses because dendritic cells cross-present the vaccine antigens. Conversely, cross-presentation of tumor antigens by dendritic cells is the foundation of cancer immunotherapy strategies that aim to prime tumor-specific CD8+ killer T cells.
