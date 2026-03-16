---
id: tumor-immunology-immune-evasion
title: Tumor Immunology and Immune Evasion
domain: biology
course: immunology
prerequisites:
- id: cd8-cytotoxic-t-cells
  type: hard
- id: innate-immune-response
  type: soft
tags:
- tumor-immunology
- immune-evasion
- cancer-immunotherapy
stage: advanced
status: draft
---

# Tumor Immunology and Immune Evasion

## Core Idea
Tumors arise through accumulation of mutations but are normally eliminated by CD8+ cytotoxic T cells recognizing tumor-associated antigens presented on MHC-I. Successful tumors evade immune surveillance through multiple mechanisms: downregulating MHC-I or TAP expression (reduced antigen presentation), producing immunosuppressive cytokines (IL-10, TGF-β, IDO), recruiting Tregs and myeloid-derived suppressor cells, expressing coinhibitory molecules (PD-L1, FasL), and selecting non-immunogenic variants. Cancer immunotherapy (checkpoint inhibitors blocking PD-1/PD-L1, CAR-T cell therapy) reinvigorates anti-tumor immunity.

## How It's Best Learned
Diagram CD8+ T cell killing of MHC-I+ tumor cells. Identify each immune evasion mechanism and therapeutic strategies targeting them. Compare immunotherapy approaches (checkpoint inhibition, CAR-T, vaccines).

## Common Misconceptions
- All cancers are immunogenic (many tumors have low mutation burdens or loss of MHC-I presentation, making them poorly immunogenic). - Checkpoint inhibitors cure all cancers (they generate durable responses in some patients but resistance occurs).

## Explainer

Your understanding of CD8+ cytotoxic T cells provides the foundation for tumor immunology. Recall that CD8+ T cells kill target cells by recognizing foreign peptides displayed on **MHC class I** molecules. Every nucleated cell in the body presents peptide fragments from its internal proteins on MHC-I, giving the immune system a continuous readout of what is happening inside each cell. When a cell accumulates mutations — as cancer cells do — some of those mutations produce abnormal proteins that get processed into **neoantigens**: novel peptide fragments that the immune system has never seen and can recognize as foreign. CD8+ T cells that recognize these neoantigens can, in principle, find and destroy tumor cells. This process, called **immunosurveillance**, is thought to eliminate most nascent tumors before they ever become clinically apparent.

The tumors that do grow into detectable cancers are, almost by definition, the ones that have found ways to evade this surveillance. Think of it as an evolutionary selection process operating within the body: the immune system kills tumor cells it can recognize, which selects for variants that are harder to detect. One of the most common evasion strategies is **downregulating MHC-I expression** — if a tumor cell stops displaying peptides on its surface, CD8+ T cells cannot see it at all. Tumors also disable the antigen-processing machinery (such as the TAP transporter that loads peptides onto MHC-I) to achieve the same invisibility. Other strategies are more aggressive: tumors can secrete **immunosuppressive cytokines** like TGF-β and IL-10 that dampen T cell activity in the tumor microenvironment, or recruit **regulatory T cells (Tregs)** and myeloid-derived suppressor cells that actively shut down anti-tumor immune responses.

One of the most clinically important evasion mechanisms involves **immune checkpoint molecules**. Normally, activated T cells upregulate receptors like **PD-1** as a built-in brake to prevent excessive immune responses. Tumors exploit this by expressing **PD-L1**, the ligand for PD-1, on their surface. When a tumor-infiltrating T cell binds PD-L1 through its PD-1 receptor, the T cell receives an inhibitory signal that suppresses its killing function — effectively telling it to stand down despite recognizing the tumor as abnormal. The tumor hijacks a safety mechanism designed to prevent autoimmunity and repurposes it as a shield.

This understanding of evasion mechanisms directly informs modern **cancer immunotherapy**. Checkpoint inhibitor drugs — antibodies that block PD-1, PD-L1, or CTLA-4 — work by removing the brakes that tumors have engaged on the immune system. By blocking the PD-1/PD-L1 interaction, these drugs reactivate exhausted T cells in the tumor microenvironment, allowing them to resume killing. **CAR-T cell therapy** takes a different approach: a patient's own T cells are engineered in the laboratory to express a synthetic receptor targeting a tumor-specific surface protein, bypassing the need for MHC-I presentation entirely. Both strategies represent a fundamental shift in cancer treatment — rather than attacking the tumor directly with drugs or radiation, they restore the immune system's own ability to eliminate it.
