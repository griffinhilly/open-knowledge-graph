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
stage: expert
status: validated
---

# Tumor Immunology and Immune Evasion

## Core Idea
Tumors arise through accumulation of mutations but are normally eliminated by CD8+ cytotoxic T cells recognizing tumor-associated antigens presented on MHC-I. Successful tumors evade immune surveillance through multiple mechanisms: downregulating MHC-I or TAP expression (reduced antigen presentation), producing immunosuppressive cytokines (IL-10, TGF-β, IDO), recruiting Tregs and myeloid-derived suppressor cells, expressing coinhibitory molecules (PD-L1, FasL), and selecting non-immunogenic variants. Cancer immunotherapy (checkpoint inhibitors blocking PD-1/PD-L1, CAR-T cell therapy) reinvigorates anti-tumor immunity.

## How It's Best Learned
Diagram CD8+ T cell killing of MHC-I+ tumor cells. Identify each immune evasion mechanism and therapeutic strategies targeting them. Compare immunotherapy approaches (checkpoint inhibition, CAR-T, vaccines).

## Common Misconceptions
- All cancers are immunogenic (many tumors have low mutation burdens or loss of MHC-I presentation, making them poorly immunogenic). - Checkpoint inhibitors cure all cancers (they generate durable responses in some patients but resistance occurs).

## Questions

```yaml
- question: "A tumor cell has lost expression of all MHC-I molecules on its surface. What is the direct immunological consequence of this?"
  type: multiple-choice
  options:
    - "CD8+ T cells are stimulated more aggressively because the absence of MHC-I triggers a danger signal"
    - "CD8+ T cells cannot recognize tumor neoantigens and therefore cannot kill the cell, since T cell recognition requires peptide displayed on MHC-I"
    - "CD4+ helper T cells compensate by directly killing the MHC-I-deficient tumor cell"
    - "Natural killer cells are suppressed because they require MHC-I to activate"
  answer: 1
  explanation: "CD8+ T cells recognize their targets through a specific molecular interaction: the T cell receptor binds to a peptide fragment displayed on MHC class I. If a tumor cell stops expressing MHC-I — either by downregulating expression or disabling the TAP transporter that loads peptides — it becomes invisible to CD8+ T cells. This is one of the most common tumor evasion strategies. Note: NK cells actually have the opposite relationship with MHC-I (they preferentially kill cells with low MHC-I), but tumors can evade NK cells through other mechanisms."

- question: "Anti-PD-1 checkpoint inhibitor drugs work by:"
  type: multiple-choice
  options:
    - "Directly binding to and killing tumor cells that overexpress PD-L1"
    - "Engineering a patient's T cells in the lab to recognize a tumor-specific surface protein"
    - "Blocking the inhibitory interaction between PD-1 on tumor-infiltrating T cells and PD-L1 on tumor cells, reactivating T cells that the tumor had suppressed"
    - "Depleting regulatory T cells from the tumor microenvironment"
  answer: 2
  explanation: "PD-1 is a natural brake on T cell activation that prevents excessive immune responses. Tumors exploit this by expressing PD-L1, which engages PD-1 on infiltrating T cells and shuts them down — even though those T cells can recognize the tumor as abnormal. Anti-PD-1 antibodies block this interaction, removing the brake and reactivating exhausted T cells in the tumor microenvironment. This is mechanistically distinct from CAR-T therapy (option B), which bypasses MHC-I presentation entirely by engineering T cells with synthetic receptors."

- question: "The tumors that develop into clinically detectable cancers are, in large part, the result of evolutionary selection within the body — the immune system has eliminated less-evasive variants, leaving behind cells that have acquired mechanisms to avoid immune destruction."
  type: true-false
  answer: true
  explanation: "This is immunoediting: the immune system acts as a selective pressure on developing tumor cell populations. It eliminates tumor cells it can recognize and destroy, which over time selects for variants with lower immunogenicity or active evasion mechanisms. The tumors we actually see are the survivors of this selection — they are not average tumor cells but specifically those cells that 'won' the evolutionary competition against immune surveillance. This is why tumors that grow tend to have acquired specific evasion strategies."

- question: "Because tumors accumulate many mutations, a high mutation burden guarantees that a tumor will be recognized and eliminated by the immune system."
  type: true-false
  answer: false
  explanation: "High mutation burden increases the probability of generating neoantigens (immunogenic peptides) that the immune system can recognize, and is associated with better responses to checkpoint inhibitors. But it does not guarantee elimination. Tumors can still downregulate MHC-I expression, suppress T cells via PD-L1, recruit immunosuppressive cells, and select for non-immunogenic variants. Many tumors with moderate mutation burdens also have low MHC-I expression or immunosuppressive microenvironments that prevent effective immune attack regardless of neoantigen quantity."

- question: "Why do tumors that express PD-L1 resist immune attack, and what does this tell us about the mechanism by which anti-PD-1 checkpoint inhibitors work?"
  type: short-answer
  answer: "PD-1 is an inhibitory receptor normally upregulated on activated T cells as a safety brake to prevent excessive immune responses and autoimmunity. Tumors that express PD-L1 (the PD-1 ligand) exploit this mechanism: when a tumor-infiltrating T cell binds PD-L1 through its PD-1 receptor, it receives an inhibitory signal that suppresses its killing function. The tumor essentially hijacks the immune system's own self-regulation to protect itself. Anti-PD-1 antibodies block this interaction, removing the brakes and reactivating the T cells already present in the tumor microenvironment. This explains why checkpoint inhibitors can be so potent — they don't create new immune responses but restore ones that the tumor had actively suppressed."
  explanation: "The key insight is that tumors don't just evade detection — they actively co-opt immune regulation. PD-L1 expression is not passive camouflage; it's an active suppression signal. This is why checkpoint inhibitors work: the T cells are already there and already recognize the tumor, but they've been told to stand down. Removing that signal can be enough to restore killing. It also explains why not all patients respond: if T cells haven't infiltrated the tumor at all, or if the tumor uses multiple redundant evasion mechanisms, restoring PD-1 signaling alone won't be sufficient."
```

## Explainer

Your understanding of CD8+ cytotoxic T cells provides the foundation for tumor immunology. Recall that CD8+ T cells kill target cells by recognizing foreign peptides displayed on **MHC class I** molecules. Every nucleated cell in the body presents peptide fragments from its internal proteins on MHC-I, giving the immune system a continuous readout of what is happening inside each cell. When a cell accumulates mutations — as cancer cells do — some of those mutations produce abnormal proteins that get processed into **neoantigens**: novel peptide fragments that the immune system has never seen and can recognize as foreign. CD8+ T cells that recognize these neoantigens can, in principle, find and destroy tumor cells. This process, called **immunosurveillance**, is thought to eliminate most nascent tumors before they ever become clinically apparent.

The tumors that do grow into detectable cancers are, almost by definition, the ones that have found ways to evade this surveillance. Think of it as an evolutionary selection process operating within the body: the immune system kills tumor cells it can recognize, which selects for variants that are harder to detect. One of the most common evasion strategies is **downregulating MHC-I expression** — if a tumor cell stops displaying peptides on its surface, CD8+ T cells cannot see it at all. Tumors also disable the antigen-processing machinery (such as the TAP transporter that loads peptides onto MHC-I) to achieve the same invisibility. Other strategies are more aggressive: tumors can secrete **immunosuppressive cytokines** like TGF-β and IL-10 that dampen T cell activity in the tumor microenvironment, or recruit **regulatory T cells (Tregs)** and myeloid-derived suppressor cells that actively shut down anti-tumor immune responses.

One of the most clinically important evasion mechanisms involves **immune checkpoint molecules**. Normally, activated T cells upregulate receptors like **PD-1** as a built-in brake to prevent excessive immune responses. Tumors exploit this by expressing **PD-L1**, the ligand for PD-1, on their surface. When a tumor-infiltrating T cell binds PD-L1 through its PD-1 receptor, the T cell receives an inhibitory signal that suppresses its killing function — effectively telling it to stand down despite recognizing the tumor as abnormal. The tumor hijacks a safety mechanism designed to prevent autoimmunity and repurposes it as a shield.

This understanding of evasion mechanisms directly informs modern **cancer immunotherapy**. Checkpoint inhibitor drugs — antibodies that block PD-1, PD-L1, or CTLA-4 — work by removing the brakes that tumors have engaged on the immune system. By blocking the PD-1/PD-L1 interaction, these drugs reactivate exhausted T cells in the tumor microenvironment, allowing them to resume killing. **CAR-T cell therapy** takes a different approach: a patient's own T cells are engineered in the laboratory to express a synthetic receptor targeting a tumor-specific surface protein, bypassing the need for MHC-I presentation entirely. Both strategies represent a fundamental shift in cancer treatment — rather than attacking the tumor directly with drugs or radiation, they restore the immune system's own ability to eliminate it.
