---
id: immune-tolerance-central-and-peripheral
title: 'Immune Tolerance: Central and Peripheral Mechanisms'
domain: biology
course: immunology
prerequisites:
- id: regulatory-t-cells-immune-tolerance
  type: hard
- id: thymic-selection-positive-negative
  type: hard
- id: adaptive-immunity-overview
  type: soft
builds-toward:
- autoimmune-disease-pathogenesis
- transplant-immunology
tags:
- tolerance
- central-tolerance
- peripheral-tolerance
- regulatory-mechanisms
- autoimmunity-prevention
stage: advanced
status: draft
---

# Immune Tolerance: Central and Peripheral Mechanisms

## Core Idea
Immune tolerance is maintained through central mechanisms (deletion of self-reactive lymphocytes in thymus and bone marrow) and peripheral mechanisms (anergy, suppression, deletion of self-reactive cells in secondary lymphoid organs). Defects in central tolerance (incomplete negative selection) or peripheral tolerance (Treg insufficiency, inadequate Fas/FasL) predispose to autoimmunity.

## How It's Best Learned
Examine how Aire and other genes control negative selection. Study how TGF-β and IL-2 maintain Treg function and how their loss triggers autoimmunity.

## Common Misconceptions
Central tolerance eliminates some, but not all, self-reactive cells; peripheral mechanisms must catch escaped self-reactive clones. Anergy is reversible under inflammatory conditions, so tolerance is not permanent without active suppression.

## Explainer

From thymic selection, you know that developing T cells are tested against self-peptide–MHC complexes: those that bind too strongly are eliminated by negative selection. From regulatory T cells, you know that a specialized population of CD4+ cells actively suppresses immune responses. **Immune tolerance** is the umbrella term for all the mechanisms that prevent the adaptive immune system from attacking the body's own tissues, and it operates at two complementary levels — central and peripheral — that together form a layered defense against autoimmunity.

**Central tolerance** occurs in the primary lymphoid organs where lymphocytes develop: the thymus for T cells and the bone marrow for B cells. In the thymic medulla, medullary epithelial cells use the transcription factor **AIRE** to express a sampling of tissue-specific proteins — molecules that would normally only be found in the pancreas, thyroid, or eye, for example. Developing T cells whose TCRs bind these self-peptide–MHC complexes with high affinity are eliminated by apoptosis (clonal deletion) or, in some cases, diverted into the regulatory T cell lineage. B cells undergo an analogous process in the bone marrow: immature B cells that strongly bind self-antigens are either deleted, rendered anergic, or undergo **receptor editing** — rearranging their light chain genes to generate a new, non-self-reactive BCR. Central tolerance is powerful but imperfect. Not every self-antigen is expressed in the thymus or bone marrow, and the threshold for deletion is set to preserve useful reactivity, meaning some self-reactive clones inevitably escape.

**Peripheral tolerance** catches what central tolerance misses. Three main mechanisms operate in the secondary lymphoid organs and tissues. First, **anergy**: when a T cell encounters its antigen presented without costimulatory signals (no B7 on the antigen-presenting cell), it becomes functionally unresponsive rather than activated — think of it as the T cell receiving signal 1 (TCR engagement) without signal 2 (costimulation), which produces paralysis instead of activation. Second, **suppression**: regulatory T cells (Tregs) actively inhibit self-reactive lymphocytes through contact-dependent mechanisms and secretion of immunosuppressive cytokines like IL-10 and TGF-β. Tregs are essential — their depletion causes rapid, multi-organ autoimmunity. Third, **peripheral deletion**: chronically stimulated self-reactive cells can be eliminated through the **Fas-FasL** pathway, where repeated antigen encounter triggers apoptosis rather than further proliferation.

The key insight is that tolerance is not a one-time event but an ongoing, active process. Anergy can be broken if inflammation provides the missing costimulatory signals — this is one route by which infections trigger autoimmune disease. Treg function must be continuously maintained through IL-2 signaling, and defects in Treg number or function lead to autoimmunity. The layered architecture — central deletion as the first filter, peripheral anergy and suppression as backup, and peripheral deletion as a last resort — reflects how dangerous a failure of tolerance can be, and why the immune system invests so heavily in redundant safeguards against self-reactivity.
