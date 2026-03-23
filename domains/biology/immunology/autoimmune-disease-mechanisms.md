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
stage: expert
status: draft
---

# Autoimmune Disease: Loss of Self-Tolerance

## Core Idea
Autoimmune diseases result from loss of self-tolerance where self-reactive B and T cells escape negative selection or are inadequately suppressed by Tregs. Central tolerance defects in thymus/bone marrow fail to eliminate self-reactive cells. Peripheral tolerance defects involve Treg insufficiency, defective immune regulation, or tissue damage breaking sequestration. Environmental triggers (viral infection, tissue damage, molecular mimicry) and genetic predisposition (HLA alleles, polymorphisms in immune regulation genes) together break tolerance in susceptible individuals.

## How It's Best Learned
Classify autoimmune diseases by whether they involve antibodies (Type II hypersensitivity) or T cells (Type IV hypersensitivity). Map genetic risk factors and environmental triggers.

## Common Misconceptions
- Autoimmune disease means immune system is hyperactive (the problem is specifically loss of self-tolerance, not general overactivity). - All autoimmune diseases are T cell-mediated (both T cell and B cell mechanisms occur; antibodies cause Type II hypersensitivity).

## Questions

```yaml
- question: "A physician describes a patient's autoimmune disease as resulting from a 'hyperactive immune system.' What is most misleading about this description?"
  type: multiple-choice
  options:
    - "It is accurate — autoimmune diseases are caused by the immune system being excessively responsive to all antigens, self and foreign alike"
    - "It mischaracterizes the problem — autoimmunity reflects loss of self-tolerance specifically, meaning the immune system attacks self-antigens while remaining normal (or even deficient) toward foreign pathogens"
    - "It is accurate for antibody-mediated diseases but not for T cell-mediated ones"
    - "It is too weak a description — autoimmune diseases actually represent a complete collapse of immune function"
  answer: 1
  explanation: "Autoimmune disease is not general immune hyperactivity — many patients can still fight infections normally. The specific problem is a failure of self-tolerance: self-reactive lymphocytes that should be eliminated or suppressed escape control and attack the body's own tissues. A patient with autoimmune disease may simultaneously be immunocompromised against certain pathogens and over-reactive against self-antigens."

- question: "Mutations in AIRE cause autoimmune polyendocrinopathy syndrome, in which the immune system attacks multiple endocrine glands. Why does AIRE deficiency cause autoimmunity?"
  type: multiple-choice
  options:
    - "AIRE normally suppresses Treg development, so without AIRE, Tregs overactivate and paradoxically destroy peripheral tissues"
    - "AIRE enables thymic medullary epithelial cells to ectopically express tissue-specific proteins, so T cells reactive to those proteins are eliminated before leaving the thymus; without AIRE, these self-reactive T cells survive"
    - "AIRE mutations cause MHC molecules to be overexpressed, leading to excessive T cell activation in the periphery"
    - "AIRE normally promotes anergy in peripheral self-reactive T cells, and its absence allows these cells to become activated"
  answer: 1
  explanation: "Central tolerance depends on the thymus presenting a representative sample of the body's own proteins so that self-reactive T cells can be deleted. AIRE enables medullary epithelial cells to express proteins normally restricted to distant organs — insulin, thyroglobulin, myelin. Without AIRE, T cells that would recognize and attack those organs are never eliminated, and they exit the thymus ready to cause damage."

- question: "Some autoimmune diseases are caused by pathogenic antibodies rather than cytotoxic T cells."
  type: true-false
  answer: true
  explanation: "Both arms of adaptive immunity can drive autoimmune pathology. Antibody-mediated (Type II hypersensitivity) examples include Graves' disease, where antibodies stimulate the TSH receptor and cause hyperthyroidism, and myasthenia gravis, where antibodies block acetylcholine receptors. T cell-mediated (Type IV) examples include type 1 diabetes, where CD8+ T cells destroy pancreatic beta cells. Recognizing which mechanism dominates each disease is essential for selecting the appropriate immunosuppressive therapy."

- question: "Once self-reactive T cells escape thymic negative selection and enter the periphery, autoimmune disease is inevitable."
  type: true-false
  answer: false
  explanation: "Peripheral tolerance mechanisms exist precisely because central tolerance is imperfect. Regulatory T cells (Tregs) actively suppress self-reactive lymphocytes. Anergy renders self-reactive T cells functionally unresponsive in the absence of costimulatory signals. The Fas-FasL pathway triggers apoptosis in chronically stimulated self-reactive cells. Autoimmune disease requires these peripheral checkpoints to fail as well — which is why genetic defects in Fas (causing ALPS) or Treg function each independently cause autoimmunity."

- question: "Why do most autoimmune diseases require both genetic susceptibility and an environmental trigger, rather than either factor alone being sufficient?"
  type: short-answer
  answer: "Genetic susceptibility — particularly HLA alleles that determine which self-peptides are presented to T cells — creates a predisposition but not inevitability. The environmental trigger (infection causing molecular mimicry, tissue damage releasing sequestered antigens, inflammation breaking anergy) provides the activating signal that pushes tolerized self-reactive cells into active disease. Neither alone is sufficient: most people with susceptible HLA types never develop autoimmunity, and most people who encounter triggers do not, because both conditions must be met simultaneously."
  explanation: "This two-hit model explains the incomplete penetrance of autoimmune diseases within families and why identical twins show less than 50% concordance for most autoimmune conditions despite sharing all genetic risk factors. The environmental trigger is often stochastic — which infections you encounter, when, and in what order."
```

## Explainer

From your study of thymic selection, you know that developing T cells undergo negative selection — those that bind self-peptide–MHC complexes too strongly are eliminated by apoptosis. From regulatory T cells, you know that Tregs actively suppress immune responses against self-antigens in the periphery. Together, these mechanisms constitute **self-tolerance**, the immune system's ability to distinguish self from non-self and refrain from attacking the body's own tissues. Autoimmune disease occurs when this tolerance breaks down and the immune system mounts a sustained attack against self-antigens.

Tolerance failures can occur at two levels. **Central tolerance** defects arise when negative selection in the thymus (for T cells) or bone marrow (for B cells) is incomplete. The thymic medullary epithelial cells use a transcription factor called **AIRE** (autoimmune regulator) to ectopically express tissue-specific proteins — insulin, thyroglobulin, myelin — so that T cells reactive to these proteins can be eliminated before they ever leave the thymus. Mutations in AIRE cause autoimmune polyendocrinopathy syndrome, a dramatic illustration of what happens when central tolerance is defective. But even with AIRE functioning normally, some self-reactive T and B cells inevitably escape into the periphery, because no selection process is perfectly efficient.

**Peripheral tolerance** mechanisms exist to catch these escapees. Tregs suppress self-reactive lymphocytes through direct contact and secretion of immunosuppressive cytokines like TGF-β and IL-10. Anergy renders self-reactive T cells functionally unresponsive when they encounter self-antigen without costimulatory signals. The Fas-FasL pathway triggers apoptosis in chronically stimulated self-reactive cells. When any of these peripheral checkpoints fail — Treg numbers drop, anergy is reversed by inflammation, or Fas signaling is defective — self-reactive cells can become activated and cause tissue damage. The autoimmune lymphoproliferative syndrome (ALPS), caused by mutations in Fas, demonstrates the consequences of failed peripheral deletion.

Most autoimmune diseases require both **genetic susceptibility** and an **environmental trigger**. Certain HLA alleles (the genes encoding MHC molecules) dramatically increase risk for specific diseases — HLA-B27 for ankylosing spondylitis, HLA-DR4 for rheumatoid arthritis — because the shape of the MHC binding groove determines which self-peptides are presented and how strongly T cells respond to them. Environmental triggers include infections that cause **molecular mimicry** (microbial peptides resembling self-peptides activate cross-reactive T cells), tissue damage that releases sequestered self-antigens normally hidden from the immune system, and inflammatory conditions that break anergy by providing costimulatory signals to previously tolerized cells. The resulting autoimmune attack can be antibody-mediated (as in Graves' disease, where antibodies stimulate the TSH receptor) or T cell-mediated (as in type 1 diabetes, where CD8+ T cells destroy pancreatic beta cells), and understanding which mechanism drives each disease is essential for choosing the right immunosuppressive therapy.
