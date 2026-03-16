---
id: class-switch-recombination-isotype-switching
title: Class Switch Recombination and Isotype Switching
domain: biology
course: immunology
prerequisites:
- id: b-cell-activation-germinal-center
  type: hard
- id: dna-recombination
  type: soft
builds-toward:
- antibody-isotypes-and-effector-functions
tags:
- class-switch
- isotype-switching
- immunoglobulin-m
stage: advanced
status: draft
---

# Class Switch Recombination and Isotype Switching

## Core Idea
B cells initially express IgM and can switch to other isotypes (IgG, IgA, IgE) through class switch recombination (CSR), a DNA recombination process replacing the IgM constant region with another. AID initiates switching by generating U:G mismatches in switch regions; mismatch repair generates double-strand breaks that are repaired by NHEJ, deleting intervening DNA segments. Different Th cell subsets (Th1, Th2, Th17) drive switching to specific isotypes through cytokine signaling (IFN-γ→IgG, IL-4→IgE, TGF-β→IgA).

## How It's Best Learned
Diagram switch regions upstream of each constant domain and how CSR deletes intervening sequences. Map Th1/Th2/Th17 cytokines to their induced isotypes.

## Common Misconceptions
- IgM is replaced by another single isotype (a B cell can switch to different isotypes sequentially; both switched and unswitched cells coexist). - All B cells undergo class switching (some remain as IgM-expressing cells; switching efficiency varies).

## Explainer

Every B cell begins life expressing IgM on its surface, but the immune system needs antibodies with different functional properties for different situations — IgG to opsonize bacteria in the blood, IgA to protect mucosal surfaces, IgE to combat parasites. **Class switch recombination (CSR)** is the DNA-level mechanism that changes the antibody's constant region (and therefore its isotype and effector function) while preserving the same antigen-binding variable region. The B cell keeps recognizing the same target but equips itself with a different weapon.

To understand the mechanism, picture the immunoglobulin heavy chain locus. After the rearranged VDJ region (which encodes antigen specificity), the constant region genes are arrayed in a fixed order: Cμ (IgM), Cδ (IgD), Cγ3, Cγ1, Cα1, Cγ2, Cγ4, Cε, Cα2. Upstream of each constant region gene (except Cδ) lies a **switch (S) region** — a stretch of repetitive DNA sequences 1-10 kilobases long. CSR works by physically deleting the DNA between two switch regions. The enzyme **activation-induced cytidine deaminase (AID)**, which you encountered in the context of somatic hypermutation, initiates the process by deaminating cytosines to uracils in the donor switch region (Sμ) and a downstream target switch region. The resulting U:G mismatches are processed by base excision repair (UNG) and mismatch repair machinery, generating **double-strand breaks** in both switch regions. The cell then joins the broken ends by **non-homologous end joining (NHEJ)**, looping out and deleting the intervening DNA. The VDJ segment is now directly upstream of the new constant region gene, producing a new antibody isotype.

The choice of which isotype to switch to is not random — it is directed by **cytokine signals** from helper T cells. This is one of the most elegant examples of immune regulation: the T helper cell subset activated during an immune response determines the antibody class that B cells produce. **IFN-γ** (produced by Th1 cells during intracellular infections) drives switching to **IgG1 and IgG3**, which are excellent at opsonization and complement activation. **IL-4** (produced by Th2 cells during parasitic infections and allergic responses) drives switching to **IgE**, which arms mast cells and eosinophils. **TGF-β** (prominent at mucosal surfaces) drives switching to **IgA**, the dominant antibody in secretions. These cytokines work by inducing **germline transcription** through the target switch region, opening the chromatin and making it accessible to AID — the switch region that is transcribed is the one that gets recombined.

Two important features distinguish CSR from other recombination events. First, it is **irreversible** — the deleted DNA is lost as a circular episome that is eventually degraded, so a B cell that has switched to IgG cannot switch back to IgM. However, sequential switching is possible: a cell that switched to IgG can subsequently switch to IgE or IgA if the downstream switch regions remain intact. Second, CSR happens in the **germinal center** during T cell-dependent B cell responses, coordinated with somatic hypermutation and affinity maturation. This means the antibodies produced after class switching are not only of a different isotype but also of higher affinity — the immune system simultaneously upgrades both the targeting precision and the effector capability of its antibody response.
