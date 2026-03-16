---
id: regulatory-t-cells
title: Regulatory T Cell Development and Immune Tolerance
domain: biology
course: immunology
prerequisites:
- id: thymic-selection-positive-negative
  type: hard
- id: t-cell-activation-costimulation
  type: soft
builds-toward:
- autoimmune-disease-mechanisms
tags:
- tregs
- regulatory-t-cells
- immune-tolerance
stage: advanced
status: draft
---

# Regulatory T Cell Development and Immune Tolerance

## Core Idea
Regulatory T cells (Tregs) expressing FOXP3, CD25, and CTLA-4 maintain immune tolerance and prevent autoimmunity through suppressive mechanisms including IL-10 and TGF-β production, CTLA-4-mediated inhibition of dendritic cell costimulation, and CD25-mediated IL-2 sequestration. Thymic Tregs (tTregs) develop from self-reactive thymocytes with high-affinity TCRs through unique positive selection. Peripheral Tregs (pTregs) differentiate from naive CD4+ T cells in response to TGF-β and antigen.

## How It's Best Learned
Compare thymic versus peripheral Treg generation and their tissue distributions. Identify the multiple suppressive mechanisms Tregs employ and against which effector cells.

## Common Misconceptions
- Tregs prevent all immune responses (they selectively suppress pathogenic responses while permitting beneficial ones). - Tregs use a single suppressive mechanism (multiple redundant mechanisms ensure robust tolerance).

## Explainer

You already know from thymic selection that developing T cells with strong self-reactivity are normally deleted through negative selection — the immune system's way of purging cells that would attack the body's own tissues. But deletion is not a perfect filter. Some self-reactive T cells inevitably escape into the periphery. **Regulatory T cells (Tregs)** are the immune system's solution to this problem: rather than trying to eliminate every potentially dangerous cell, the body maintains a dedicated population of suppressor cells that actively patrol for and shut down inappropriate immune responses.

The most important Tregs arise in the thymus itself, called **thymic Tregs (tTregs)**. Paradoxically, these develop from the very thymocytes that have high-affinity TCRs for self-antigens — the same cells you might expect to be deleted. The difference lies in a developmental fork: instead of dying, some of these self-reactive cells receive signals that upregulate the transcription factor **FOXP3**, which reprograms them into suppressor cells. Think of it as the thymus converting potential enemies into police officers. These tTregs leave the thymus already equipped to recognize self-antigens and suppress any effector T cells that target the same tissues. A second population, **peripheral Tregs (pTregs)**, differentiates from naive CD4+ T cells in tissues when they encounter antigen in the presence of TGF-β — this allows the immune system to generate tolerance to harmless environmental antigens like food proteins and commensal bacteria.

Tregs suppress immune responses through multiple redundant mechanisms, which is why tolerance is so robust. They constitutively express **CD25** (the high-affinity IL-2 receptor alpha chain), which lets them absorb IL-2 from the local environment — starving nearby effector T cells of the growth factor they need to proliferate. They secrete the anti-inflammatory cytokines **IL-10** and **TGF-β**, which dampen activation of dendritic cells and effector T cells alike. They also express **CTLA-4**, which binds the costimulatory ligands B7-1 and B7-2 on dendritic cells with higher affinity than the activating receptor CD28, effectively stripping away the costimulatory signals that effector T cells need for full activation. This connects directly to what you learned about T cell activation and costimulation: without that second signal, T cells become anergic rather than activated.

The clinical importance of Tregs becomes clear when they fail. Mutations in the FOXP3 gene cause IPEX syndrome (immune dysregulation, polyendocrinopathy, enteropathy, X-linked), a devastating autoimmune disease in which the immune system attacks multiple organs simultaneously. This single-gene defect demonstrates that Tregs are not merely fine-tuning immune responses — they are essential gatekeepers without which self-tolerance collapses entirely. Understanding Treg biology is foundational for grasping autoimmune disease mechanisms, transplant rejection, and emerging immunotherapies that either boost Tregs (for autoimmunity) or deplete them (to unleash anti-tumor immunity in cancer).
