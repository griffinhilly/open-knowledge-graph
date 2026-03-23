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
stage: expert
status: draft
---

# Regulatory T Cells and Immune Tolerance

## Core Idea
Regulatory T cells (Tregs) are specialized CD4+ cells that suppress immunity through IL-10 and TGF-β production, CTLA-4 ligation, and granzyme-mediated killing. Foxp3 is the master regulator of Treg development and function. Central tolerance (thymic negative selection) and peripheral tolerance (Treg-mediated suppression) together prevent autoimmunity.

## Questions

```yaml
- question: "A patient with IPEX syndrome has non-functional Foxp3 and develops severe multi-organ autoimmunity in infancy, despite apparently normal thymic selection. What does this reveal about immune tolerance?"
  type: multiple-choice
  options:
    - "Thymic selection alone is sufficient for immune tolerance when functioning normally"
    - "Foxp3 is required only for thymic selection, so IPEX is actually a thymic development disorder"
    - "Peripheral Treg-mediated suppression is essential because thymic selection never eliminates all self-reactive T cells"
    - "IPEX autoimmunity results from excess IL-2 production, not from Treg loss"
  answer: 2
  explanation: "IPEX demonstrates that Treg function is indispensable even when thymic selection is intact. Self-reactive T cells inevitably escape negative selection — some because their self-antigens aren't expressed in the thymus, others because their affinity is just below the deletion threshold. Tregs provide a second layer of control that suppresses these escaped cells in the periphery. Loss of Foxp3 (the Treg master switch) means escaped self-reactive cells go unchecked, causing multi-organ autoimmunity. Central and peripheral tolerance are both necessary."

- question: "Anti-CTLA-4 antibodies (checkpoint inhibitors) are used in cancer immunotherapy. They work partly by affecting Tregs. Why would blocking CTLA-4 boost anti-tumor immunity?"
  type: multiple-choice
  options:
    - "CTLA-4 promotes T cell activation, so blocking it reduces the immune response and allows more time to target tumors precisely"
    - "Tregs use CTLA-4 to compete with effector T cells for B7 co-stimulation on antigen-presenting cells; blocking CTLA-4 restores effector T cell activation"
    - "CTLA-4 is expressed on tumor cells; blocking it directly targets and kills the tumor"
    - "Anti-CTLA-4 antibodies stimulate new Treg production that specifically targets tumor tissue"
  answer: 1
  explanation: "CTLA-4 on Tregs outcompetes CD28 on effector T cells for binding to B7 ligands on antigen-presenting cells. By stealing this co-stimulatory signal, Tregs prevent effector T cells from being fully activated. Blocking CTLA-4 prevents this 'signal theft,' restoring effector T cell activation. Tumors often recruit Tregs into the tumor microenvironment to exploit this same suppressive mechanism — which is why disabling CTLA-4 boosts anti-tumor responses."

- question: "Regulatory T cells suppress immune responses through multiple distinct mechanisms rather than a single pathway."
  type: true-false
  answer: true
  explanation: "Tregs employ at least four known suppressive mechanisms: secretion of anti-inflammatory cytokines (IL-10, TGF-β) that dampen nearby immune cells; CTLA-4-mediated competition for B7 co-stimulation; consumption of IL-2 (starving effector T cells of the growth factor they need); and in some contexts, direct cytotoxic killing via granzymes. This redundancy makes Treg-mediated tolerance robust — loss of one mechanism can often be compensated by others, which is why Foxp3 deletion (abolishing all Treg function) is required to produce severe autoimmunity."

- question: "Regulatory T cells are a distinct lineage that develops exclusively in the thymus and cannot be generated in peripheral tissues."
  type: true-false
  answer: false
  explanation: "There are two major Treg populations: thymic Tregs (tTregs), which develop in the thymus when moderately self-reactive cells are diverted into the Treg lineage, and peripheral Tregs (pTregs), which are induced from conventional CD4+ T cells in peripheral tissues under appropriate conditions. The gut is the primary site of peripheral Treg induction, where tolerance to food antigens and commensal bacteria is essential. Peripheral induction is a distinct and important pathway for generating site-specific tolerance."

- question: "Why is peripheral Treg-mediated tolerance necessary if the thymus already performs negative selection to eliminate self-reactive T cells?"
  type: short-answer
  answer: "Thymic negative selection is imperfect and cannot eliminate every self-reactive T cell. Some escape because their target self-antigens are not expressed in the thymus; others because their T cell receptor affinity for self-peptides is just below the deletion threshold. Tregs provide an ongoing second layer of peripheral control that continuously suppresses these escaped self-reactive cells. Additionally, peripheral tolerance is needed at barrier sites (gut, skin) where the immune system constantly encounters harmless foreign antigens that were never 'seen' during thymic development."
  explanation: "The key insight is that central tolerance is a developmental checkpoint that happens once; peripheral Treg-mediated tolerance is a dynamic, ongoing process throughout life. Neither is sufficient alone: thymic selection without Tregs leads to autoimmunity (as in IPEX), and Tregs without thymic selection would be overwhelmed. The two systems are complementary, not redundant."
```

## Explainer

Your immune system faces a fundamental paradox: it must attack foreign invaders aggressively while leaving your own tissues completely alone. You already know that thymic selection eliminates many self-reactive T cells during development, but this process is imperfect — some self-reactive cells inevitably escape into the periphery. **Regulatory T cells (Tregs)** are the backup system that catches what thymic selection misses, acting as the immune system's internal police force that prevents friendly fire.

Tregs are a specialized subset of CD4+ T helper cells, distinguished by their expression of the transcription factor **Foxp3**, which acts as the master switch for Treg identity. Without functional Foxp3, Tregs fail to develop or function, leading to devastating multi-organ autoimmunity — as seen in IPEX syndrome in humans and the scurfy mouse model. Tregs arise through two main pathways: **thymic Tregs (tTregs)** develop in the thymus when developing T cells with moderate self-reactivity are diverted into the Treg lineage rather than being deleted, and **peripheral Tregs (pTregs)** are induced from conventional CD4+ T cells in peripheral tissues, particularly in the gut, where tolerance to food antigens and commensal bacteria is essential.

Tregs suppress immune responses through multiple complementary mechanisms. They secrete the anti-inflammatory cytokines **IL-10** and **TGF-β**, which dampen activation of nearby immune cells. They express **CTLA-4** on their surface, which outcompetes the co-stimulatory receptor CD28 for binding to B7 molecules on antigen-presenting cells, effectively stealing the activation signal that other T cells need. They can also consume IL-2 — the growth factor that activated T cells depend on — starving effector cells in their vicinity. In some contexts, Tregs even kill target cells directly using granzymes, the same cytotoxic molecules employed by CD8+ killer T cells.

The concept of **immune tolerance** encompasses both the central mechanisms you studied in thymic selection and the peripheral mechanisms Tregs provide. Central tolerance is a one-time checkpoint; peripheral tolerance is an ongoing, dynamic process. Tregs are particularly important at barrier sites like the gut and skin, where the immune system constantly encounters harmless antigens from food, commensal microbes, and the environment. When Treg function breaks down — through genetic defects, infection, or therapeutic depletion — the result is autoimmune disease, where the immune system attacks the body's own tissues. Conversely, tumors sometimes exploit Tregs by recruiting them into the tumor microenvironment, suppressing anti-tumor immunity. Modern cancer immunotherapies like anti-CTLA-4 antibodies work in part by disabling this Treg-mediated immune evasion.
