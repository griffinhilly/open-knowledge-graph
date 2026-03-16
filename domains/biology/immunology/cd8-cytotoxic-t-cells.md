---
id: cd8-cytotoxic-t-cells
title: CD8+ Cytotoxic T Lymphocytes (CTLs)
domain: biology
course: immunology
prerequisites:
- id: t-cell-activation-costimulation
  type: hard
- id: antigen-presentation-mechanisms
  type: hard
builds-toward:
- immunological-memory-secondary-response
- tumor-immunology
tags:
- adaptive
- t-cell
- cytotoxicity
- killing
stage: advanced
status: draft
---

# CD8+ Cytotoxic T Lymphocytes (CTLs)

## Core Idea
CD8+ T cells recognize antigen-MHC-I and differentiate into cytotoxic T lymphocytes capable of killing infected or abnormal cells. CD8+ activation requires TCR engagement with MHC-I-peptide and costimulation, often provided by CD4+ T helper cells or innate signaling. CTLs kill via perforin-granzyme and Fas-FasL pathways, inducing target cell apoptosis.

## Explainer

From T cell activation and costimulation, you know that naive T cells require two signals to become activated: TCR recognition of peptide-MHC and a costimulatory signal (typically B7-CD28 interaction). From antigen presentation, you know that **MHC class I** molecules display peptides derived from intracellular proteins — proteins made inside the cell, including viral proteins if the cell is infected. **CD8+ T cells** are the adaptive immune system's targeted killers: they survey MHC-I molecules on nucleated cells, and when they detect a foreign peptide (indicating infection, mutation, or other abnormality), they destroy that specific cell while leaving its neighbors intact.

Activation of a naive CD8+ T cell into a fully functional **cytotoxic T lymphocyte (CTL)** is a carefully regulated process. The CD8 coreceptor binds to the MHC-I molecule and stabilizes the interaction, while the TCR reads the peptide in the MHC groove. But TCR engagement alone is not enough — costimulation is required, and for many CD8+ responses, **CD4+ T helper cells** provide essential help. Helper T cells activate the same dendritic cell that is presenting antigen to the CD8+ cell, licensing the dendritic cell to deliver stronger costimulatory signals. This three-cell interaction — dendritic cell, CD4+ helper, and CD8+ killer — ensures that CTL responses are only launched when the threat has been confirmed by multiple arms of the immune system. Once activated, CD8+ T cells undergo massive clonal expansion, producing thousands of effector CTLs from a single precursor.

CTLs kill their targets through two main mechanisms. The **perforin-granzyme pathway** is the primary killing route: the CTL forms a tight immunological synapse with the target cell and releases specialized granules containing **perforin** (a pore-forming protein) and **granzymes** (serine proteases). Perforin inserts into the target cell membrane and creates channels through which granzymes enter the cytoplasm. Once inside, granzymes activate the caspase cascade, triggering **apoptosis** — programmed cell death. The beauty of this mechanism is its precision: the directed secretion into the synapse means only the contacted cell is killed, not bystanders. The second pathway uses **Fas ligand (FasL)** on the CTL surface, which binds Fas on target cells and directly triggers the apoptotic cascade without requiring granule release.

After the infection is cleared, most effector CTLs die by apoptosis, but a small fraction differentiate into **memory CD8+ T cells** that persist for years. Upon re-exposure to the same pathogen, these memory cells mount a faster and stronger response — expanding more rapidly and killing more efficiently than during the primary response. This is the cellular basis for the long-lasting protection provided by vaccines against intracellular pathogens. CTLs are also central to **tumor immunology**: they can recognize mutant proteins (neoantigens) displayed on MHC-I by cancer cells, and checkpoint immunotherapy works by removing the brakes that tumors impose on CTL activity.
