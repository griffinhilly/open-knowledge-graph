---
id: autoimmune-disease-mechanisms
title: 'Autoimmune Disease: Loss of Self-Tolerance'
domain: biology
course: immunology
prerequisites:
- id: thymic-selection-positive-negative
  type: hard
- id: regulatory-t-cells
  type: hard
tags:
- autoimmunity
- tolerance
- self-reactive
stage: advanced
status: draft
---

# Autoimmune Disease: Loss of Self-Tolerance

## Core Idea
Autoimmune diseases result from loss of self-tolerance where self-reactive B and T cells escape negative selection or are inadequately suppressed by Tregs. Central tolerance defects in thymus/bone marrow fail to eliminate self-reactive cells. Peripheral tolerance defects involve Treg insufficiency, defective immune regulation, or tissue damage breaking sequestration. Environmental triggers (viral infection, tissue damage, molecular mimicry) and genetic predisposition (HLA alleles, polymorphisms in immune regulation genes) together break tolerance in susceptible individuals.

## How It's Best Learned
Classify autoimmune diseases by whether they involve antibodies (Type II hypersensitivity) or T cells (Type IV hypersensitivity). Map genetic risk factors and environmental triggers.

## Common Misconceptions
- Autoimmune disease means immune system is hyperactive (the problem is specifically loss of self-tolerance, not general overactivity). - All autoimmune diseases are T cell-mediated (both T cell and B cell mechanisms occur; antibodies cause Type II hypersensitivity).

## Explainer

From your study of thymic selection, you know that developing T cells undergo negative selection — those that bind self-peptide–MHC complexes too strongly are eliminated by apoptosis. From regulatory T cells, you know that Tregs actively suppress immune responses against self-antigens in the periphery. Together, these mechanisms constitute **self-tolerance**, the immune system's ability to distinguish self from non-self and refrain from attacking the body's own tissues. Autoimmune disease occurs when this tolerance breaks down and the immune system mounts a sustained attack against self-antigens.

Tolerance failures can occur at two levels. **Central tolerance** defects arise when negative selection in the thymus (for T cells) or bone marrow (for B cells) is incomplete. The thymic medullary epithelial cells use a transcription factor called **AIRE** (autoimmune regulator) to ectopically express tissue-specific proteins — insulin, thyroglobulin, myelin — so that T cells reactive to these proteins can be eliminated before they ever leave the thymus. Mutations in AIRE cause autoimmune polyendocrinopathy syndrome, a dramatic illustration of what happens when central tolerance is defective. But even with AIRE functioning normally, some self-reactive T and B cells inevitably escape into the periphery, because no selection process is perfectly efficient.

**Peripheral tolerance** mechanisms exist to catch these escapees. Tregs suppress self-reactive lymphocytes through direct contact and secretion of immunosuppressive cytokines like TGF-β and IL-10. Anergy renders self-reactive T cells functionally unresponsive when they encounter self-antigen without costimulatory signals. The Fas-FasL pathway triggers apoptosis in chronically stimulated self-reactive cells. When any of these peripheral checkpoints fail — Treg numbers drop, anergy is reversed by inflammation, or Fas signaling is defective — self-reactive cells can become activated and cause tissue damage. The autoimmune lymphoproliferative syndrome (ALPS), caused by mutations in Fas, demonstrates the consequences of failed peripheral deletion.

Most autoimmune diseases require both **genetic susceptibility** and an **environmental trigger**. Certain HLA alleles (the genes encoding MHC molecules) dramatically increase risk for specific diseases — HLA-B27 for ankylosing spondylitis, HLA-DR4 for rheumatoid arthritis — because the shape of the MHC binding groove determines which self-peptides are presented and how strongly T cells respond to them. Environmental triggers include infections that cause **molecular mimicry** (microbial peptides resembling self-peptides activate cross-reactive T cells), tissue damage that releases sequestered self-antigens normally hidden from the immune system, and inflammatory conditions that break anergy by providing costimulatory signals to previously tolerized cells. The resulting autoimmune attack can be antibody-mediated (as in Graves' disease, where antibodies stimulate the TSH receptor) or T cell-mediated (as in type 1 diabetes, where CD8+ T cells destroy pancreatic beta cells), and understanding which mechanism drives each disease is essential for choosing the right immunosuppressive therapy.
