---
id: cd4-t-helper-cells
title: CD4+ T Helper Cells
domain: biology
course: immunology
prerequisites:
- id: t-cell-activation-costimulation
  type: hard
builds-toward:
- t-helper-cell-differentiation-th1-th2
- germinal-center-reactions
- regulatory-t-cells-immune-tolerance
tags:
- adaptive
- t-cell
- helper
- cytokines
stage: advanced
status: draft
---

# CD4+ T Helper Cells

## Core Idea
CD4+ T helper cells coordinate immune responses through cytokine production and cognate help to B cells and other immune cells. CD4+ cells recognize antigen-MHC-II on antigen-presenting cells and differentiate into distinct subsets (Th1, Th2, Th17, Tfh) based on cytokine signals and transcription factors. Different Th subsets promote different effector responses suited to specific pathogen types.

## Explainer

You already know from studying T cell activation that naive T cells require two signals to become activated: TCR recognition of antigen presented on MHC, plus a costimulatory signal (such as B7–CD28 interaction). **CD4+ T helper cells** are the subset that recognizes antigen presented on **MHC class II** molecules — which are found exclusively on antigen-presenting cells like dendritic cells, macrophages, and B cells. Once activated, helper T cells do not kill infected cells directly. Instead, they serve as the immune system's coordinators, directing other cells through **cytokine** secretion and direct cell-cell contact.

The remarkable feature of CD4+ T cells is their ability to **differentiate into specialized subsets**, each tailored to a different category of threat. The cytokine environment present during initial activation determines which subset a naive CD4+ cell becomes. **Th1** cells develop in the presence of IL-12 and IFN-γ, express the master transcription factor **T-bet**, and secrete IFN-γ to activate macrophages — making them specialists against intracellular pathogens like *Mycobacterium tuberculosis*. **Th2** cells develop in response to IL-4, express **GATA-3**, and produce IL-4, IL-5, and IL-13, which drive antibody class switching to IgE and eosinophil recruitment — ideal for combating parasitic worms. **Th17** cells differentiate under IL-6 and TGF-β, express **RORγt**, and secrete IL-17, which recruits neutrophils to fight extracellular bacteria and fungi at barrier surfaces.

A fourth major subset, **T follicular helper (Tfh)** cells, is critical for high-quality antibody responses. Tfh cells migrate to B cell follicles in lymph nodes and provide **cognate help** to B cells — delivering signals (CD40L, IL-21) that drive B cells through germinal center reactions, affinity maturation, and class switching. Without Tfh help, B cells produce only low-affinity IgM and cannot generate the high-affinity IgG antibodies needed for long-term protection. This is why CD4+ T cell depletion, as occurs in HIV/AIDS, devastates not just cell-mediated immunity but also antibody responses.

The subset model explains a pattern you will see throughout immunology: the immune system does not mount a single generic response to every pathogen. Instead, the type of threat determines which helper subset dominates, and that subset shapes the entire downstream response — which antibody classes are produced, which innate cells are recruited, and which effector mechanisms are deployed. Getting the subset wrong (for example, mounting a Th2 response against an intracellular bacterium) can lead to failed pathogen clearance or even immunopathology, which is why the cytokine environment during initial T cell priming is so consequential.
