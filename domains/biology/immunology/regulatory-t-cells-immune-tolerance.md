---
id: regulatory-t-cells-immune-tolerance
title: Regulatory T Cells and Immune Tolerance
domain: biology
course: immunology
prerequisites:
- id: t-cell-development-thymic-selection
  type: hard
- id: cd4-t-helper-cells
  type: hard
builds-toward:
- autoimmunity-mechanisms
- transplant-immunology
tags:
- adaptive
- t-cell
- tolerance
- regulation
stage: advanced
status: draft
---

# Regulatory T Cells and Immune Tolerance

## Core Idea
Regulatory T cells (Tregs) are specialized CD4+ cells that suppress immunity through IL-10 and TGF-β production, CTLA-4 ligation, and granzyme-mediated killing. Foxp3 is the master regulator of Treg development and function. Central tolerance (thymic negative selection) and peripheral tolerance (Treg-mediated suppression) together prevent autoimmunity.

## Explainer

Your immune system faces a fundamental paradox: it must attack foreign invaders aggressively while leaving your own tissues completely alone. You already know that thymic selection eliminates many self-reactive T cells during development, but this process is imperfect — some self-reactive cells inevitably escape into the periphery. **Regulatory T cells (Tregs)** are the backup system that catches what thymic selection misses, acting as the immune system's internal police force that prevents friendly fire.

Tregs are a specialized subset of CD4+ T helper cells, distinguished by their expression of the transcription factor **Foxp3**, which acts as the master switch for Treg identity. Without functional Foxp3, Tregs fail to develop or function, leading to devastating multi-organ autoimmunity — as seen in IPEX syndrome in humans and the scurfy mouse model. Tregs arise through two main pathways: **thymic Tregs (tTregs)** develop in the thymus when developing T cells with moderate self-reactivity are diverted into the Treg lineage rather than being deleted, and **peripheral Tregs (pTregs)** are induced from conventional CD4+ T cells in peripheral tissues, particularly in the gut, where tolerance to food antigens and commensal bacteria is essential.

Tregs suppress immune responses through multiple complementary mechanisms. They secrete the anti-inflammatory cytokines **IL-10** and **TGF-β**, which dampen activation of nearby immune cells. They express **CTLA-4** on their surface, which outcompetes the co-stimulatory receptor CD28 for binding to B7 molecules on antigen-presenting cells, effectively stealing the activation signal that other T cells need. They can also consume IL-2 — the growth factor that activated T cells depend on — starving effector cells in their vicinity. In some contexts, Tregs even kill target cells directly using granzymes, the same cytotoxic molecules employed by CD8+ killer T cells.

The concept of **immune tolerance** encompasses both the central mechanisms you studied in thymic selection and the peripheral mechanisms Tregs provide. Central tolerance is a one-time checkpoint; peripheral tolerance is an ongoing, dynamic process. Tregs are particularly important at barrier sites like the gut and skin, where the immune system constantly encounters harmless antigens from food, commensal microbes, and the environment. When Treg function breaks down — through genetic defects, infection, or therapeutic depletion — the result is autoimmune disease, where the immune system attacks the body's own tissues. Conversely, tumors sometimes exploit Tregs by recruiting them into the tumor microenvironment, suppressing anti-tumor immunity. Modern cancer immunotherapies like anti-CTLA-4 antibodies work in part by disabling this Treg-mediated immune evasion.
