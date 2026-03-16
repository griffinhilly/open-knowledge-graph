---
id: thymic-selection-positive-negative
title: 'Thymic Selection: Positive and Negative Selection'
domain: biology
course: immunology
prerequisites:
- id: t-cell-receptor-structure-and-function
  type: hard
- id: major-histocompatibility-complex
  type: hard
builds-toward:
- cd4-helper-t-cells
- cd8-cytotoxic-t-cells
- regulatory-t-cells
tags:
- thymic-selection
- t-cell-education
- tolerance
stage: advanced
status: draft
---

# Thymic Selection: Positive and Negative Selection

## Core Idea
T cell development in the thymus involves two critical selection steps to generate a functional, self-tolerant T cell repertoire. Positive selection retains thymocytes with TCRs that weakly recognize self-MHC on cortical epithelial cells, instructing CD4/CD8 lineage choice. Negative selection eliminates thymocytes with high-affinity TCRs recognizing self-peptide-MHC complexes on medullary epithelial cells and dendritic cells, preventing autoimmunity. ~95% of thymocytes undergo apoptosis during these selections.

## How It's Best Learned
Diagram the cortex and medulla showing positive and negative selection compartments and their cellular inhabitants. Explain how TCR signaling strength (weak vs strong) determines selection outcome.

## Common Misconceptions
- Both selections occur in the same thymic compartment (cortex vs medulla separation is functionally essential). - Negative selection eliminates all self-reactive T cells (Tregs with high self-affinity are specifically selected).

## Explainer

You already know that T cell receptors (TCRs) are generated through random gene rearrangement, producing an enormous diversity of receptors — most of which will be useless or dangerous. The thymus is where this raw repertoire gets quality-controlled through two sequential filters, each testing a different property of the TCR. Think of it as a two-round audition: the first round checks whether you can perform at all, and the second checks whether you will perform safely.

**Positive selection** occurs in the thymic cortex, where immature thymocytes (still expressing both CD4 and CD8) encounter **cortical thymic epithelial cells (cTECs)** displaying self-peptides on MHC molecules. The test is simple: can your TCR recognize self-MHC at all? Thymocytes whose TCRs bind self-MHC with weak but detectable affinity receive a survival signal; those that cannot bind — the majority — die by neglect within about three days. This step ensures that every T cell entering the periphery can actually interact with MHC molecules, which is essential because T cells can only "see" antigens presented on MHC. During positive selection, lineage commitment also occurs: thymocytes that bind MHC class II downregulate CD8 and become CD4+ T cells, while those that bind MHC class I downregulate CD4 and become CD8+ T cells.

**Negative selection** occurs primarily in the thymic medulla, where surviving thymocytes now encounter **medullary thymic epithelial cells (mTECs)** and dendritic cells presenting a broader array of self-antigens. A remarkable protein called **AIRE (autoimmune regulator)** drives mTECs to express tissue-specific proteins from organs throughout the body — insulin from the pancreas, myelin from the brain, thyroglobulin from the thyroid — creating a molecular preview of self. Thymocytes whose TCRs bind these self-peptide-MHC complexes with high affinity are deleted through apoptosis, because a T cell that reacts strongly to self would cause autoimmune destruction in the periphery. The critical variable is **signal strength**: weak binding during positive selection means "functional, keep it," while strong binding during negative selection means "self-reactive, destroy it."

The numbers tell the story of how stringent this quality control is: roughly **95–98% of all thymocytes die** during development, most failing positive selection. Of those that pass, a further fraction is eliminated by negative selection. The tiny surviving population — perhaps 2–5% of the original — consists of T cells that can recognize MHC (proven by positive selection) but do not react strongly to self (proven by negative selection). There is one important exception to the deletion rule: some thymocytes with moderately high self-reactivity are diverted into the regulatory T cell (Treg) lineage rather than being killed, providing a population of cells that will actively suppress self-reactive responses in the periphery. This represents an elegant solution — rather than waste every self-reactive cell, the thymus repurposes some of them as immune regulators.
