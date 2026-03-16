---
id: antibody-class-switching
title: Antibody Class Switching (Isotype Switching)
domain: biology
course: immunology
prerequisites:
- id: antibody-structure-and-function
  type: hard
- id: b-cell-development-maturation
  type: soft
builds-toward:
- germinal-center-reactions
- affinity-maturation-somatic-hypermutation
tags:
- adaptive
- b-cell
- antibody
- gene-rearrangement
stage: advanced
status: draft
---

# Antibody Class Switching (Isotype Switching)

## Core Idea
B cells initially produce IgM but can switch to IgG, IgA, IgE, or IgD by deleting intervening heavy chain constant genes through class switch recombination (CSR). CSR is induced by CD40 ligation and specific cytokines (IFN-γ for IgG1, IL-4 for IgE, TGF-β for IgA). Different isotypes have distinct tissue distributions and effector functions suited to specific immune contexts.

## Explainer

From your study of antibody structure, you know that every antibody has two functional regions: the variable region (Fab) that determines antigen specificity, and the constant region (Fc) that determines what the antibody *does* once it binds. The constant region of the heavy chain defines the antibody's **isotype** — IgM, IgG, IgA, IgE, or IgD — and each isotype has different effector capabilities. IgM is excellent at activating complement; IgG is the workhorse of opsonization and crosses the placenta; IgA protects mucosal surfaces; IgE triggers mast cell degranulation against parasites (and in allergies). The question is: how does a B cell change its heavy chain constant region while keeping the same antigen specificity?

The answer is **class switch recombination (CSR)**, a DNA-level rearrangement that literally deletes the gene segments encoding the current constant region and brings a downstream constant region gene next to the rearranged V-D-J segment. The heavy chain gene locus is arranged with Cμ (IgM) closest to the V-D-J region, followed by Cδ, Cγ3, Cγ1, Cα1, Cγ2, Cγ4, Cε, and Cα2 in humans. Upstream of each constant region gene (except Cδ) lies a **switch region** — a repetitive DNA sequence. The enzyme **activation-induced cytidine deaminase (AID)** introduces mutations in these switch regions, creating DNA breaks. The breaks in the donor switch region (typically Sμ) and a downstream switch region are then joined by DNA repair machinery, looping out and deleting everything in between. The V-D-J segment — the part encoding antigen specificity — remains untouched.

What determines *which* isotype a B cell switches to? The answer lies in the signals it receives. **CD40 ligation** by T helper cells (via CD40L) is required to activate AID and initiate CSR in the first place — this is why T-cell help is essential for class switching. The specific isotype is then directed by **cytokines**: IFN-γ drives switching to IgG1 (in humans) for enhanced opsonization during intracellular infections; IL-4 drives switching to IgE for anti-parasitic responses; TGF-β promotes IgA for mucosal immunity. These cytokines work by inducing transcription through specific switch regions before recombination occurs — a process called **germline transcription** — which opens the chromatin and makes the target switch region accessible to AID.

This system is remarkably elegant: the B cell preserves its hard-won antigen specificity (the product of V-D-J recombination and perhaps somatic hypermutation) while swapping out the effector module to match the type of threat. A B cell that began the immune response producing IgM against a bacterial surface antigen can switch to IgG for more efficient opsonization and complement fixation, or to IgA if the infection is at a mucosal surface. CSR is irreversible — once intervening DNA is deleted, the cell cannot switch back — but its descendants can switch further downstream if given appropriate signals. Defects in CSR, such as mutations in AID or CD40L (as in hyper-IgM syndrome), result in patients who produce abundant IgM but cannot generate other isotypes, leaving them vulnerable to infections that require IgG, IgA, or IgE-mediated defense.
