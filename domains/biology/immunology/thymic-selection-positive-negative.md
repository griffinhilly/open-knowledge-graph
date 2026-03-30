---
id: thymic-selection-positive-negative
title: 'Thymic Selection: Positive and Negative Selection'
domain: biology
course: immunology
prerequisites:
- id: t-cell-receptor-structure-and-function-and-function
  type: hard
- id: major-histocompatibility-complex
  type: hard
builds-toward:
- cd4-helper-t-cells
- cd8-cytotoxic-t-cells
- regulatory-t-cells-immune-tolerance
tags:
- thymic-selection
- t-cell-education
- tolerance
stage: advanced
status: validated
---

# Thymic Selection: Positive and Negative Selection

## Core Idea
T cell development in the thymus involves two critical selection steps to generate a functional, self-tolerant T cell repertoire. Positive selection retains thymocytes with TCRs that weakly recognize self-MHC on cortical epithelial cells, instructing CD4/CD8 lineage choice. Negative selection eliminates thymocytes with high-affinity TCRs recognizing self-peptide-MHC complexes on medullary epithelial cells and dendritic cells, preventing autoimmunity. ~95% of thymocytes undergo apoptosis during these selections.

## How It's Best Learned
Diagram the cortex and medulla showing positive and negative selection compartments and their cellular inhabitants. Explain how TCR signaling strength (weak vs strong) determines selection outcome.

## Common Misconceptions
- Both selections occur in the same thymic compartment (cortex vs medulla separation is functionally essential). - Negative selection eliminates all self-reactive T cells (Tregs with high self-affinity are specifically selected).

## Questions

```yaml
- question: "A thymocyte's TCR cannot bind any self-MHC molecules on cortical thymic epithelial cells. What is the most likely fate of this cell?"
  type: multiple-choice
  options:
    - "It undergoes negative selection and is deleted to prevent autoimmunity"
    - "It survives positive selection because it poses no autoimmune risk"
    - "It dies by neglect — failing to receive a survival signal during positive selection"
    - "It differentiates into a regulatory T cell that suppresses immune responses"
  answer: 2
  explanation: "Positive selection tests whether a thymocyte's TCR can recognize self-MHC at all. Cells that fail this test — the majority of developing thymocytes — receive no survival signal and die by neglect within about three days. The logic is: a T cell that cannot bind self-MHC is useless in the periphery, because T cells can only 'see' antigens when they are presented on MHC molecules. This is not the same as negative selection (which kills cells that bind too well to self-peptide-MHC, posing autoimmune risk). Failing positive selection means the TCR is nonfunctional, not dangerous."

- question: "A thymocyte that passed positive selection now encounters medullary epithelial cells displaying tissue-specific self-antigens via AIRE. Its TCR binds a self-peptide-MHC complex with very high affinity. The most likely outcome is:"
  type: multiple-choice
  options:
    - "Export to the periphery as a mature, activated T cell primed to respond"
    - "Clonal deletion through apoptosis — strong self-reactivity triggers negative selection"
    - "Differentiation into a memory T cell to respond rapidly if the antigen appears again"
    - "Upregulation of both CD4 and CD8, reverting to a double-positive thymocyte"
  answer: 1
  explanation: "Negative selection operates on signal strength: high-affinity TCR binding to self-peptide-MHC is interpreted as 'this T cell would attack the body's own tissues in the periphery.' The result is clonal deletion via apoptosis. AIRE-expressing mTECs are central to this process — they display tissue-specific proteins from organs throughout the body (insulin, myelin, thyroglobulin), so that T cells are tested against a molecular preview of self. Exporting a high-affinity self-reactive T cell would risk autoimmune destruction of the corresponding tissue."

- question: "Positive selection and negative selection both occur in the thymic cortex, testing the same TCR property (self-MHC recognition) but using different signal thresholds."
  type: true-false
  answer: false
  explanation: "Positive and negative selection are spatially separated in functionally distinct thymic compartments. Positive selection occurs in the thymic cortex, where cortical thymic epithelial cells (cTECs) test whether the TCR can recognize self-MHC at all. Negative selection occurs primarily in the thymic medulla, where medullary thymic epithelial cells (mTECs) and dendritic cells test whether the TCR reacts too strongly to self-peptide-MHC complexes. The spatial separation is essential: the two selections ask different questions (can it function? is it dangerous?) and use different cell types that present different sets of self-antigens."

- question: "The fundamental logic of thymic selection is that TCR signal strength determines fate: weak binding to self-MHC during positive selection ensures the T cell is functional, while strong binding to self-peptide-MHC during negative selection signals potential autoimmunity and triggers deletion."
  type: true-false
  answer: true
  explanation: "Signal strength is the organizing principle of both selections. During positive selection in the cortex: too weak (no binding) → die by neglect; weak but detectable → survive and commit to CD4 or CD8 lineage. During negative selection in the medulla: strong binding to self-peptide-MHC → clonal deletion; weak or no binding → survive and exit to periphery. This creates the 'Goldilocks' repertoire: T cells that can bind MHC (functional) but don't react strongly to self (safe). The ~95-98% death rate reflects how stringent these requirements are — most randomly generated TCRs fail one test or the other."

- question: "Why does the thymus use two separate selection steps rather than one, and what would go wrong if either step were absent?"
  type: short-answer
  answer: "The two selections test different and complementary properties that cannot be tested simultaneously. Positive selection (cortex) ensures every surviving T cell can recognize self-MHC — without it, T cells would exit the thymus unable to see any antigen presented on MHC, rendering the adaptive immune response nonfunctional. Negative selection (medulla) ensures T cells don't react strongly to self-peptide-MHC — without it, self-reactive T cells would enter the periphery and attack the body's own tissues, causing systemic autoimmunity. The first test establishes functionality; the second establishes safety. Both are necessary because these properties are logically independent: a TCR can be MHC-binding but self-reactive, or non-self-reactive but also unable to bind MHC."
  explanation: "The two-filter design is elegant precisely because it solves two different failure modes with two different tests. AIRE is critical to negative selection because it forces mTECs to express tissue-specific proteins that wouldn't otherwise be present in the thymus — without AIRE, T cells that react to pancreatic insulin or brain myelin would pass negative selection undetected and exit to cause organ-specific autoimmune diseases. Human mutations in AIRE cause autoimmune polyendocrinopathy, confirming the essential role of negative selection in peripheral tolerance."
```

## Explainer

You already know that T cell receptors (TCRs) are generated through random gene rearrangement, producing an enormous diversity of receptors — most of which will be useless or dangerous. The thymus is where this raw repertoire gets quality-controlled through two sequential filters, each testing a different property of the TCR. Think of it as a two-round audition: the first round checks whether you can perform at all, and the second checks whether you will perform safely.

**Positive selection** occurs in the thymic cortex, where immature thymocytes (still expressing both CD4 and CD8) encounter **cortical thymic epithelial cells (cTECs)** displaying self-peptides on MHC molecules. The test is simple: can your TCR recognize self-MHC at all? Thymocytes whose TCRs bind self-MHC with weak but detectable affinity receive a survival signal; those that cannot bind — the majority — die by neglect within about three days. This step ensures that every T cell entering the periphery can actually interact with MHC molecules, which is essential because T cells can only "see" antigens presented on MHC. During positive selection, lineage commitment also occurs: thymocytes that bind MHC class II downregulate CD8 and become CD4+ T cells, while those that bind MHC class I downregulate CD4 and become CD8+ T cells.

**Negative selection** occurs primarily in the thymic medulla, where surviving thymocytes now encounter **medullary thymic epithelial cells (mTECs)** and dendritic cells presenting a broader array of self-antigens. A remarkable protein called **AIRE (autoimmune regulator)** drives mTECs to express tissue-specific proteins from organs throughout the body — insulin from the pancreas, myelin from the brain, thyroglobulin from the thyroid — creating a molecular preview of self. Thymocytes whose TCRs bind these self-peptide-MHC complexes with high affinity are deleted through apoptosis, because a T cell that reacts strongly to self would cause autoimmune destruction in the periphery. The critical variable is **signal strength**: weak binding during positive selection means "functional, keep it," while strong binding during negative selection means "self-reactive, destroy it."

The numbers tell the story of how stringent this quality control is: roughly **95–98% of all thymocytes die** during development, most failing positive selection. Of those that pass, a further fraction is eliminated by negative selection. The tiny surviving population — perhaps 2–5% of the original — consists of T cells that can recognize MHC (proven by positive selection) but do not react strongly to self (proven by negative selection). There is one important exception to the deletion rule: some thymocytes with moderately high self-reactivity are diverted into the regulatory T cell (Treg) lineage rather than being killed, providing a population of cells that will actively suppress self-reactive responses in the periphery. This represents an elegant solution — rather than waste every self-reactive cell, the thymus repurposes some of them as immune regulators.
