---
id: tumor-immune-surveillance
title: Tumor Immune Surveillance and Immunoediting
domain: biology
course: immunology
prerequisites:
- id: tumor-immunology-immune-evasion
  type: hard
- id: cd8-cytotoxic-t-cells
  type: hard
- id: natural-killer-cells
  type: soft
builds-toward:
- cancer-immunotherapy-approaches
- immune-checkpoint-regulators
tags:
- tumor-surveillance
- immunoediting
- tumor-antigens
- CTL-escape
- malignant-transformation
stage: advanced
status: draft
---

# Tumor Immune Surveillance and Immunoediting

## Core Idea
The immune system continually surveils for malignant cells, particularly through CTL recognition of tumor-associated antigens (TAAs) and NK cell detection of altered self. Over decades, most transformed cells are eliminated; those that evade immunity progress. Immunoediting selects for clones with reduced immunogenicity (downregulated MHC, PD-L1 overexpression, altered TAAs), explaining why late-stage tumors are often less immunogenic.

## How It's Best Learned
Study the three phases of immunoediting: elimination, equilibrium, and escape. Examine how checkpoint inhibitors reverse escape.

## Common Misconceptions
Tumors do not 'hide' from immunity passively; they actively suppress it through immunosuppressive cytokines and cells. Not all tumor-infiltrating lymphocytes are functional; many are exhausted or anergic.

## Explainer

Your study of CD8+ cytotoxic T cells and NK cells has shown you how the immune system eliminates abnormal cells — CTLs recognize foreign or altered peptides on MHC class I, while NK cells detect cells that have lost MHC expression altogether. **Tumor immune surveillance** is the application of these principles to cancer: the immune system is constantly scanning for cells that have undergone malignant transformation, and in most cases, it destroys them before they ever become clinically detectable tumors. You have likely accumulated and eliminated precancerous cells many times without knowing it.

The concept is formalized in the **immunoediting** model, which describes three phases. In the **elimination** phase, transformed cells expressing abnormal proteins — called **tumor-associated antigens (TAAs)** — are recognized and killed by CTLs, NK cells, and gamma-delta T cells. Danger signals from tissue damage recruit dendritic cells that cross-present tumor antigens, amplifying the adaptive response. If elimination is complete, no tumor develops. But if some tumor cells survive, the process enters the **equilibrium** phase — a prolonged standoff (potentially lasting years or decades) where the immune system contains tumor growth without fully eradicating it. The tumor population is held in check but not destroyed.

The critical shift occurs in the **escape** phase. Because tumor cells are genetically unstable and rapidly mutating, they are subject to Darwinian selection under immune pressure. Clones that happen to downregulate MHC class I (making them invisible to CTLs), overexpress **immune checkpoint ligands** like PD-L1 (which sends "don't kill me" signals to T cells), or secrete immunosuppressive molecules like TGF-β and IL-10 gain a survival advantage. Over time, these immune-evasive clones dominate the tumor population. This is why clinically detected cancers are often poorly immunogenic — they are the survivors of years of immune selection, not naive cells that the immune system simply missed.

The immunoediting model also explains why immunotherapy works. **Checkpoint inhibitors** (anti-PD-1, anti-CTLA-4 antibodies) do not create new immune responses — they unleash existing ones that the tumor has suppressed. By blocking the inhibitory signals that exhausted T cells receive in the tumor microenvironment, these drugs can shift the balance back from escape toward elimination. Understanding that tumors actively sculpt their immune environment — recruiting regulatory T cells, polarizing macrophages toward immunosuppressive phenotypes, and creating zones of immune exclusion — is essential for grasping both why cancers evade immunity and how modern immunotherapies aim to reverse that evasion.
